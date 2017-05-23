import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestHoleScoreMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_default(self):
        current_score = self._init_game()
        # wah, wah... only 50 points collected if you don't advance the hole
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 50
        self.assertEqual(current_score, self.machine.game.player.score)

    def test_low_block(self):
        current_score = self._init_game()
        # begin at 1, in low throughin first block for up to two advancements
        for i in range(2):
            self.hit_and_release_switch("s_stationary_advance_hole_score")
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 50
        self.assertEqual(current_score, self.machine.game.player.score)
        # 550 != 1000

    def test_mid_block(self):
        current_score = self._init_game()
        # begin at 1, in mid through 6
        for i in range(5):
            self.hit_and_release_switch("s_stationary_advance_hole_score")
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 500
        self.assertEqual(current_score, self.machine.game.player.score)
        # 1000 != 5500

    def test_high_block(self):
        current_score = self._init_game()
        # begin at 1, in high through 9
        for i in range(8):
            self.hit_and_release_switch("s_stationary_advance_hole_score")
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 5000
        self.assertEqual(current_score, self.machine.game.player.score)

    def test_max_value(self):
        current_score = self._init_game()
        # 10 advancements for max value...
        for i in range(1,10):
            self.hit_and_release_switch("s_stationary_advance_hole_score")
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 50000
        self.assertEqual(current_score, self.machine.game.player.score)

    def _init_game(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        # activate base mode
        self.hit_and_release_switch("s_rollover_top_1")
        self.advance_time_and_run(4) # 3+1
        current_score += 500
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(current_score, self.machine.game.player.score)
        return current_score
