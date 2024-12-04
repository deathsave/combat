import os
from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestGameOverMode(MpfMachineTestCase):

    def test_game_over(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

        # drain all 3 balls
        for ball in range(1, 4):
            self.assertEqual(ball, self.machine.game.player.ball)
            # ball drains twice (ball save)
            for i in range(0, 2):
                self.hit_switch_and_run('s_trough_1', 2)

        self.assertModeRunning('game_over')

    def test_game_over_with_high_score_set(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

        # hit a ton of drop targets...
        for x in range(0, 20):
            self.hit_and_release_switch("s_kicker_gun")

        # drain all 3 balls (plus bonus ball for hitting score level 1
        for ball in range(1, 5):
            # ball drains twice (ball save)
            for i in range(0, 2):
                self.hit_switch_and_run('s_trough_1', 2)

        self.advance_time_and_run(2)
        self.assertModeRunning('high_score')

        # enter initials as "AAA"
        for x in range(0, 3):
            self.advance_time_and_run(2)
            self.hit_and_release_switch("s_start")

        self.advance_time_and_run(9)
        self.assertModeRunning('game_over')
