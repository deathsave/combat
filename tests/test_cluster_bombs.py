import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestBombsDroppedMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_timer_scoring(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # LIT cluster is 1, 4 and 7
        self.hit_and_release_switch("s_rollover_top_1")
        self.hit_and_release_switch("s_rollover_top_4")
        self.hit_and_release_switch("s_rollover_top_7")
        current_score += 5000 * 3
        # base cluster is 2, 3, 5 and 6
        self.hit_and_release_switch("s_rollover_top_2")
        self.hit_and_release_switch("s_rollover_top_3")
        self.hit_and_release_switch("s_rollover_top_5")
        self.hit_and_release_switch("s_rollover_top_6")
        current_score += 500 * 4
        self.assertEqual(current_score, self.machine.game.player.score)
        self.assertModeRunning('cluster_bombs_a')

        # after 8 seconds, base cluster is 1, 4 and 7
        self.advance_time_and_run(8)
        self.hit_and_release_switch("s_rollover_top_1")
        self.hit_and_release_switch("s_rollover_top_4")
        self.hit_and_release_switch("s_rollover_top_7")
        current_score += 500 * 3
        # LIT cluster is 2, 3, 5 and 6
        self.hit_and_release_switch("s_rollover_top_2")
        self.hit_and_release_switch("s_rollover_top_3")
        self.hit_and_release_switch("s_rollover_top_5")
        self.hit_and_release_switch("s_rollover_top_6")
        current_score += 5000 * 4
        self.assertEqual(current_score, self.machine.game.player.score)
        self.assertModeRunning('cluster_bombs_b')

    def test_bumper_hits(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        self.assertModeRunning('cluster_bombs_a')
        self.hit_and_release_switch("s_bumper_1")
        self.assertModeRunning('cluster_bombs_b')
        self.hit_and_release_switch("s_bumper_2")
        self.assertModeRunning('cluster_bombs_a')
        self.hit_and_release_switch("s_bumper_3")
        self.assertModeRunning('cluster_bombs_b')
