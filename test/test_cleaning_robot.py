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
    def test_manage_cleaning_system_led_when_charge_left_is_greater_than_10(self, mock_gpio_output,mock_get_charge_left):
        robot = CleaningRobot()

        mock_get_charge_left.return_value = 20
        robot.manage_cleaning_system()

        self.assertTrue(robot.cleaning_system_on)
        self.assertFalse(robot.recharge_led_on)
        mock_gpio_output.assert_has_calls([call(robot.CLEANING_SYSTEM_PIN, True), call(robot.RECHARGE_LED_PIN, False)], any_order=True)

    @patch.object(IBS, 'get_charge_left')
    @patch.object(GPIO, 'output')
    def test_manage_cleaning_system_led_when_charge_left_is_equal_to_or_less_than_10(self, mock_gpio_output, mock_get_charge_left):
        robot = CleaningRobot()

        mock_get_charge_left.return_value = 10
        robot.manage_cleaning_system()

        self.assertFalse(robot.cleaning_system_on)
        self.assertTrue(robot.recharge_led_on)
        mock_gpio_output.assert_has_calls([call(robot.CLEANING_SYSTEM_PIN, False), call(robot.RECHARGE_LED_PIN, True)], any_order=True)

    @patch.object(CleaningRobot, 'activate_wheel_motor')
    def test_execute_command_forward(self, mock_activate_wheel_motor):
        robot = CleaningRobot()
        robot.initialize_robot()
        result = robot.execute_command('f')

        mock_activate_wheel_motor.assert_called_once()
        self.assertEqual(result, '(0,1,N)')

    @patch.object(CleaningRobot, 'activate_rotation_motor')
    def test_execute_command_turn_right(self, mock_activate_rotation_motor):
        robot = CleaningRobot()
        robot.initialize_robot()
        result = robot.execute_command('r')

        mock_activate_rotation_motor.assert_called_once_with('r')
        self.assertEqual(result, '(0,0,E)')

    @patch.object(CleaningRobot, 'activate_rotation_motor')
    def test_execute_command_turn_left(self, mock_activate_rotation_motor):
        robot = CleaningRobot()
        robot.initialize_robot()
        result = robot.execute_command('l')

        mock_activate_rotation_motor.assert_called_once_with('l')
        self.assertEqual(result, '(0,0,W)')

    @patch.object(GPIO, 'input')
    def test_obstacle_found_detects_obstacle(self, mock_gpio_input):
        robot = CleaningRobot()
        mock_gpio_input.return_value = True  # Obstacle detected
        self.assertTrue(robot.obstacle_found())

    @patch.object(GPIO, 'input')
    def test_obstacle_found_no_obstacle(self, mock_gpio_input):
        robot = CleaningRobot()
        mock_gpio_input.return_value = False
        self.assertFalse(robot.obstacle_found())

    @patch.object(GPIO, 'input')
    @patch.object(CleaningRobot, 'activate_wheel_motor')
    def test_execute_command_forward_with_obstacle(self, mock_activate_wheel_motor, mock_gpio_input):
        robot = CleaningRobot()
        robot.initialize_robot()
        mock_gpio_input.return_value = True   # Obstacle detected

        result = robot.execute_command('f')

        mock_activate_wheel_motor.assert_not_called()  # Wheel motor should not be activated
        self.assertEqual(result, '(0,0,N)(0,1)')

    @patch.object(GPIO, 'input')
    @patch.object(CleaningRobot, 'activate_wheel_motor')
    def test_execute_command_forward_no_obstacle(self, mock_activate_wheel_motor, mock_gpio_input):
        robot = CleaningRobot()
        robot.initialize_robot()
        mock_gpio_input.return_value = False  # No obstacle detected

        result = robot.execute_command('f')

        mock_activate_wheel_motor.assert_called_once()  # Wheel motor should be activated
        self.assertEqual(result, '(0,1,N)')

    #I know the next test is unnecessary, but I wanted to show how to test if it turns when there is an obstacle
    @patch.object(GPIO, 'input')
    @patch.object(CleaningRobot, 'activate_rotation_motor')
    def test_execute_command_turn_left_with_obstacle(self, mock_activate_rotation_motor, mock_gpio_input):
        robot = CleaningRobot()
        robot.initialize_robot()
        mock_gpio_input.return_value = True

        result = robot.execute_command('l')

        mock_activate_rotation_motor.assert_called_once_with('l')
        self.assertEqual(result, '(0,0,W)')  # Robot should turn left

    @patch.object(IBS, 'get_charge_left')
    @patch.object(CleaningRobot, 'activate_wheel_motor')
    @patch.object(CleaningRobot, 'activate_rotation_motor')
    def test_execute_command_with_low_battery(self, mock_activate_rotation_motor, mock_activate_wheel_motor,
                                              mock_get_charge_left):
        robot = CleaningRobot()
        robot.initialize_robot()

        mock_get_charge_left.return_value = 10

        result = robot.execute_command('f')

        mock_activate_wheel_motor.assert_not_called()
        mock_activate_rotation_motor.assert_not_called()

        self.assertEqual(result, '!(1,1,N)')

    @patch.object(IBS, 'get_charge_left')
    @patch.object(CleaningRobot, 'activate_wheel_motor')
    @patch.object(CleaningRobot, 'activate_rotation_motor')
    def test_execute_command_with_sufficient_battery(self, mock_activate_rotation_motor, mock_activate_wheel_motor,
                                                     mock_get_charge_left):
        robot = CleaningRobot()
        robot.initialize_robot()

        mock_get_charge_left.return_value = 20

        result = robot.execute_command('f')

        mock_activate_wheel_motor.assert_called_once()
        mock_activate_rotation_motor.assert_not_called()
        self.assertEqual(result, '(0,1,N)')









