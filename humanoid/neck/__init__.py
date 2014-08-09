from humanoid.joints import ArticulatedJoint


class Neck(ArticulatedJoint):
    """
    The tilt of the robot's head is controlled by two
    motors (one on eiter side on the front of the neck).
    """

    def __init__(self):
        super(Neck, self).__init__()
        self.data["href"] = "/api/robot/body/neck/"