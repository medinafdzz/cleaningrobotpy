from unittest import TestCase
from unittest.mock import Mock, patch, call

from mock import GPIO
from mock.ibs import IBS
from src.cleaning_robot import CleaningRobot


class TestCleaningRobot(TestCase):

    def test_initialize_robot(self):
        robot = CleaningRobot()
        robot.initialize_robot()
        self.assertEqual(robot.pos_x, 0)
        self.assertEqual(robot.pos_y, 0)
        self.assertEqual(robot.heading, 'N')

    def test_robot_status(self):
        robot = CleaningRobot()
        robot.pos_x = 0
        robot.pos_y = 0
        robot.heading = 'N'
        self.assertEqual(robot.robot_status(), '(0,0,N)')

    @patch.object(IBS, 'get_charge_left')
    @patch.object(GPIO, 'output')
    def test_manage_cleaning_system_led_when_charge_left_is_greater_than_10(self, mock_gpio_output,
                                                                            mock_get_charge_left):
        robot = CleaningRobot()

        mock_get_charge_left.return_value = 20
        robot.manage_cleaning_system()
        self.assertTrue(robot.cleaning_system_on)
        self.assertFalse(robot.recharge_led_on)
        mock_gpio_output.assert_has_calls([call(robot.CLEANING_SYSTEM_PIN, True), call(robot.RECHARGE_LED_PIN, False)], any_order=True)

