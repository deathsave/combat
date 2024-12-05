from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestGameOverMode(MpfMachineTestCase):

    def test_game_over(self):
        self.hit_and_release_switch("s_start")
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_switch_and_run('s_rollover_top_2', 4)

        # drain all 3 balls
        for ball in range(1, 4):
            self.assertEqual(ball, self.machine.game.player.ball)
            # ball drains twice (ball save)
            for i in range(0, 2):
                self.hit_and_release_switch("s_shooter_lane")
                self.hit_switch_and_run('s_trough_1', 4)

        self.assertModeRunning('game_over')

    def test_game_over_with_high_score_set(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_switch_and_run('s_rollover_top_2', 4)

        # exceeds 50k points to set low end of board
        for x in range(0, 51):
            current_score += 1000
            self.hit_and_release_switch("s_stationary_thousand")

        # drain all 3 balls
        for ball in range(1, 4):
            # ball drains twice (ball save)
            for i in range(0, 2):
                self.hit_and_release_switch("s_shooter_lane")
                self.hit_switch_and_run('s_trough_1', 4)

        self.assertModeRunning('high_score')

        # enter initials as "AAA"
        for x in range(0, 3):
            self.hit_and_release_switch("s_start")
            self.advance_time_and_run(4)

        self.advance_time_and_run(5)
        self.assertModeRunning('game_over')
