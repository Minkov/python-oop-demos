class Robot:
    _sensors_amount = 1

    def __init__(self, name):
        self.name = name

    @classmethod
    def sensors_amount(cls):
        return cls._sensors_amount


class MedicalRobot(Robot):
    _sensors_amount = 6


class ChefRobot(Robot):
    _sensors_amount = 4


class WarRobot(Robot):
    _sensors_amount = 12


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())
    # if isinstance(robot, Robot):
    #     print(robot.sensors_amount())
    # if isinstance(robot, MedicalRobot):
    #     print(robot.medical_robot_sensors_amount())
    # elif isinstance(robot, ChefRobot):
    #     print(robot.chef_robot_sensors_amount())
    # elif isinstance(robot, WarRobot):
    #     print(robot.war_robot_sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

# print(da_vinci.medical_robot_sensors_amount())
# print(da_vinci.sensors_amount())

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
