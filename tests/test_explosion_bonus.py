from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestExplosionBonusMode(MpfMachineTestCase):

    def test_normal_scoring(self):
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

        # advance the bonus with target 5 times
        for x in range(0, 5):
            self.hit_and_release_switch(
                "s_stationary_advance_bonus"
            )
            # bonus points not added now...
            # just the base 100 points for each
            current_score += 100
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # TODO: advance the bonus with LIT rollover
        # self.hit_and_release_switch("s_rollover_top_1")

        # wait for "shoot again" to expire
        self.advance_time_and_run(15)

        # drain and collect bonus
        self.hit_switch_and_run('s_trough_1', 2)
        self.assertEqual(2, self.machine.game.player.ball)
        # at the end of the ball, the player collects the bonus
        current_score += 5000
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_multiplied_scoring(self):
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

        # TODO: advance the bonus with LIT rollover
        # self.hit_and_release_switch("s_rollover_top_1")

        # advance the bonus with target 5 times
        for x in range(0, 5):
            self.hit_and_release_switch(
                "s_stationary_advance_bonus"
            )
            # bonus points not added now...
            # just the base 100 points for each
            current_score += 100
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # wait for "shoot again" to expire
        self.advance_time_and_run(15)

        # trigger the Gun to activate 10x
        self.hit_and_release_switch("s_kicker_gun")
        self.advance_time_and_run(1)
        current_score += 5000 # score for hitting gun
        self.assertModeRunning('explosion_multiplier')

        # drain and collect bonus
        self.hit_switch_and_run('s_trough_1', 2)
        self.assertEqual(2, self.machine.game.player.ball)
        # at the end of the ball, the player collects the bonus
        current_score += 50000
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_tilted(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # activate base mode
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_and_release_switch("s_rollover_top_2")
        # wait for "shoot again" to expire
        self.advance_time_and_run(12)

        current_score += 500
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # advance the bonus with target 5 times
        for _ in range(5):
            self.hit_and_release_switch(
                "s_stationary_advance_bonus"
            )
            # bonus points not added now...
            # just the base 100 points for each
            current_score += 100
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # TILT the fucker!
        self.assertPlayerVarEqual(0, "tilt_warnings")
        for _ in range(2):
            self.hit_and_release_switch("s_tilt")
            self.advance_time_and_run(4)
        self.assertPlayerVarEqual(2, "tilt_warnings")

        self.hit_and_release_switch("s_tilt")
        self.assertTrue(self.machine.game.tilted)

        # TILT has a 3 second settle time
        self.advance_time_and_run(3)
        self.hit_switch_and_run('s_trough_1', 5)
        self.assertEqual(2, self.machine.game.player.ball)

        # at the end of the ball, the player
        # collects no bonus because the game is tilted
        current_score += 0
        self.assertEqual(current_score,
            self.machine.game.player.score)
