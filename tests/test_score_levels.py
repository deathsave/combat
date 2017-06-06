import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestFlashScoreMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_score_level_1(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")

        for i in range(29):
            # hit "Flash score" rollover 30 times for 145k points
            self.hit_and_release_switch("s_rollover_top_1")

        # no extra ball awarded yet
        self.assertEqual(0, self.machine.game.player.score_level)
        self.assertEqual(0, self.machine.game.player.extra_balls)

        # now we go over the 150k treshold
        self.hit_and_release_switch("s_rollover_top_1")
        self.assertEqual(150500, self.machine.game.player.score)
        self.assertEqual(1, self.machine.game.player.score_level)
        self.assertEqual(1, self.machine.game.player.extra_balls)
