import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase


class TestGame(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_begin_gameplay(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        ## game should be running
        self.assertIsNotNone(self.machine.game)
        self.assertEqual(1, self.machine.game.player.ball)
        ## playfield expects a ball
        self.assertEqual(1, self.machine.playfield.available_balls)
        ## ball is ejected to plunger
        self.assertEqual(1, self.machine.ball_devices.bd_plunger.balls)
        ## no balls on playfield yet
        self.assertEqual(0, self.machine.playfield.balls)
        ## player launches ball
        self.hit_and_release_switch("s_plunger_lane")
        ## not immediately "on the playfield", though
        self.advance_time_and_run(1)
        self.assertEqual(0, self.machine.playfield.balls)
        ## after a brief delay, the ball is now on the playfield...
        ## if this errors, could be system-specific so increase it
        self.advance_time_and_run(3)
        self.assertEqual(1, self.machine.playfield.balls)

    def test_base_mode(self):
        self.begin_gameplay()
        self.assertEqual(1, self.machine.playfield.balls)

        ## test pop bumper scoring
        current_score = 0
        self.hit_and_release_switch("s_bumper_1")
        self.hit_and_release_switch("s_bumper_2")
        self.hit_and_release_switch("s_bumper_3")
        current_score += 100 * 3
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test rollover top scoring
        self.hit_and_release_switch("s_rollover_top_1")
        self.hit_and_release_switch("s_rollover_top_2")
        self.hit_and_release_switch("s_rollover_top_3")
        self.hit_and_release_switch("s_rollover_top_4")
        self.hit_and_release_switch("s_rollover_top_5")
        self.hit_and_release_switch("s_rollover_top_6")
        self.hit_and_release_switch("s_rollover_top_7")
        current_score += 500 * 7
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test drop target scoring
        self.hit_and_release_switch("s_drop_target_1")
        self.hit_and_release_switch("s_drop_target_2")
        self.hit_and_release_switch("s_drop_target_3")
        self.hit_and_release_switch("s_drop_target_4")
        self.hit_and_release_switch("s_drop_target_5")
        current_score += 1000 * 5
        self.assertEqual(current_score, self.machine.game.player.score)

        # test lowest "Hole Score" value (saucer)
        self.hit_and_release_switch("s_kicker_saucer")
        current_score += 50
        self.assertEqual(current_score, self.machine.game.player.score)

        # test gun score
        self.hit_and_release_switch("s_kicker_gun")
        current_score += 5000
        self.assertEqual(current_score, self.machine.game.player.score)

        # test spinner
        self.hit_and_release_switch("s_spinner")
        current_score += 100
        self.assertEqual(current_score, self.machine.game.player.score)

        # test slingshot scoring
        self.hit_and_release_switch("s_slingshot_1")
        self.hit_and_release_switch("s_slingshot_2")
        current_score += 10 * 2
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test drain-area rollovers
        self.hit_and_release_switch("s_rollover_bonus_ball_1")
        self.hit_and_release_switch("s_rollover_bonus_ball_2")
        self.hit_and_release_switch("s_rollover_advance_hole_1")
        self.hit_and_release_switch("s_rollover_advance_hole_2")
        current_score += 1000 * 4
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test 'advancing' stationary targets
        self.hit_and_release_switch("s_stationary_advance_bonus")
        self.hit_and_release_switch("s_stationary_advance_hole_score")
        # no scoring change...
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test 'scoring' stationary targets
        self.hit_and_release_switch("s_stationary_thousand")
        current_score += 1000
        self.hit_and_release_switch("s_stationary_special")
        current_score += 100 # more when 'lit'
        self.assertEqual(current_score, self.machine.game.player.score)

    def begin_gameplay(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_plunger_lane")
        self.advance_time_and_run(4) # 3+1
