import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestFlashScoreMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_score_level_1(self):
        current_score=0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")
        current_score += 500
        self.assertEqual(current_score, self.machine.game.player.score)

        for i in range(0,249):
            self.hit_and_release_switch("s_stationary_thousand")
            current_score += 1000

        # no extra ball awarded yet
        self.assertEqual(249500, self.machine.game.player.score)
        self.assertEqual(0, self.machine.game.player.score_level)
        self.assertEqual(0, self.machine.game.player.extra_balls)

        # now we go over the 250k treshold
        self.hit_and_release_switch("s_stationary_thousand")
        self.assertEqual(250500, self.machine.game.player.score)
        self.assertEqual(1, self.machine.game.player.score_level)
        self.assertEqual(1, self.machine.game.player.extra_balls)
