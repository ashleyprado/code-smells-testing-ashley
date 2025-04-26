"""
Refactored smells2.py
Run tests with: pytest tests/smells2_test.py
"""

class Nose:
    """
    Represents a Nose which can smell odors.
    Can be human or robot.
    """

    def __init__(self, allergies=None, is_robot=False, air_tank_capacity_liters=20):
        self.smelled_smells = set()
        self.is_robot = is_robot
        self.allergies = allergies or []
        self.air_tank_capacity_liters = air_tank_capacity_liters
        self.current_air_tank_level = 0
        self.immune_response = False

    def smell(self, odor):
        """
        Smell an odor based on whether the nose is human or robot.
        """
        if self.is_robot:
            self._robot_smell(odor)
        else:
            self._human_smell(odor)

    def _robot_smell(self, odor):
        if self.current_air_tank_level < self.air_tank_capacity_liters:
            self.smelled_smells.add(odor)
            self.current_air_tank_level += 1
        else:
            raise RuntimeError("Robot nose cannot smell when air tank is full.")

    def _human_smell(self, odor):
        if self.immune_response:
            raise RuntimeError("Nose cannot smell when immune response is active.")
        if odor in self.allergies:
            self.immune_response = True
        else:
            self.smelled_smells.add(odor)

    def rest(self):
        """
        Resets the nose so it can smell again.
        """
        self.immune_response = False
        self.current_air_tank_level = 0

    def get_smelled_smells(self):
        """
        Returns a copy of smells encountered.
        """
        return self.smelled_smells.copy()

if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")
