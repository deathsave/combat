from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestHoleScoreMode(MpfMachineTestCase):

    def test_default(self):
        current_score = self._init_game_and_get_score()
        self.assertModeNotRunning("hole_score")

        self.assertEqual(0,
            self.machine.game.player.hole_score_count)
        # wah, wah... only 50 points collected
        # if you don't advance the hole
        self.hit_and_release_switch("s_kicker_missile")
        self.assertModeRunning("hole_score")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        current_score += 50
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # no lights should be on, yet
        self.assertLightColor("l_hole_score_lane_1", "off")
        self.assertLightColor('l_hole_score_lane_2', "off")
        self.assertLightColor('l_hole_score_lane_5', "off")
        self.assertLightColor('l_hole_score_lane_10', "off")
        # hole score count resets
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

    def test_low_block(self):
        current_score = self._init_game_and_get_score()
        self.assertModeNotRunning("hole_score")
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

        # advance the hole score to "2"
        for i in range(2):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
            self.assertLightColor("l_hole_score_lane_{}". \
                format(i+1), '56A20A')
        self.assertEqual(2,
            self.machine.game.player.hole_score_count)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        self.assertLightColor("l_hole_score_lane_1", "black")
        current_score += 50
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

    def test_mid_block(self):
        current_score = self._init_game_and_get_score()
        # advance the hole score to "5"
        for i in range(5):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
        self.assertEqual(5,
            self.machine.game.player.hole_score_count)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        current_score += 500
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

    def test_high_block(self):
        current_score = self._init_game_and_get_score()
        # begin at 1, in high through 9
        for i in range(8):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
        self.assertEqual(8,
            self.machine.game.player.hole_score_count)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        current_score += 5000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

    def test_max_value(self):
        current_score = self._init_game_and_get_score()
        # 10 advancements for max value...
        for i in range(10):
            current_score += 100
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            self.advance_time_and_run(1)
        self.assertEqual(10,
            self.machine.game.player.hole_score_count)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        current_score += 50000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

    def test_reactivation(self):
        current_score = self._init_game_and_get_score()
        for i in range(5):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
        self.assertEqual(5,
            self.machine.game.player.hole_score_count)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        current_score += 500
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)
        for i in range(10):
            current_score += 100
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            self.advance_time_and_run(1)
        self.assertEqual(10,
            self.machine.game.player.hole_score_count)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1)

        self.assertModeNotRunning("hole_score")
        current_score += 50000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)

    def _init_game_and_get_score(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        # activate base mode
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_and_release_switch("s_rollover_top_2")
        self.advance_time_and_run(4) # 3+1
        current_score += 500
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertEqual(0,
            self.machine.game.player.hole_score_count)
        return current_score
