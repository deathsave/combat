from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestHoleScoreMode(MpfMachineTestCase):

    def test_default(self):
        current_score = self._init_game_and_get_score()
        self.assertModeNotRunning("hole_score")
        # wah, wah... only 50 points collected
        # if you don't advance the hole
        self.hit_and_release_switch("s_kicker_missile")
        self.assertModeRunning("hole_score")
        current_score += 50
        # no lights should be on, yet
        self.assertLightColor("l_hole_score_lane_1", "off")
        self.assertLightColor('l_hole_score_lane_2', "off")
        self.assertLightColor('l_hole_score_lane_5', "off")
        self.assertLightColor('l_hole_score_lane_10', "off")
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_low_block(self):
        current_score = self._init_game_and_get_score()
        # begin at 1, in low throughin first
        # block for up to two advancements
        for i in range(2):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
            self.assertLightColor("l_hole_score_lane_{}". \
                format(i+1), '56A20A')
        self.hit_and_release_switch("s_kicker_missile")
        self.assertLightColor("l_hole_score_lane_1", "black")
        current_score += 50
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_mid_block(self):
        current_score = self._init_game_and_get_score()
        # begin at 1, in mid through 6
        for i in range(5):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 500
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_high_block(self):
        current_score = self._init_game_and_get_score()
        # begin at 1, in high through 9
        for i in range(8):
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            current_score += 100
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 5000
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_max_value(self):
        current_score = self._init_game_and_get_score()
        # 10 advancements for max value...
        for i in range(10):
            current_score += 100
            self.hit_and_release_switch(
                "s_stationary_advance_hole_score"
            )
            self.advance_time_and_run(1)
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(4)
        current_score += 50000
        self.assertEqual(current_score,
            self.machine.game.player.score)

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
        return current_score
