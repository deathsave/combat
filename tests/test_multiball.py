import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestMultiballMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_scoring(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # activate base mode
        self.hit_and_release_switch("s_rollover_top_2")
        self.advance_time_and_run(4) # 3+1
        current_score += 500
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(current_score, self.machine.game.player.score)

        # activate bombs dropped mode
        for x in range(0, 5):
            self.hit_and_release_switch("s_drop_target")
        # the mech itself triggers this switch
        # as soon as all 5 targets have dropped
        self.hit_and_release_switch("s_drop_target_reset")
        self.assertModeRunning('bombs_dropped')
        current_score += 5000
        self.assertEqual(current_score, self.machine.game.player.score)

        # ball rolls into lock - doesn't score yet...
        self.hit_switch_and_run('s_kicker_gun', 1)
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(1, self.machine.ball_devices.bd_gun.balls)

        # after some time, should be a locked ball in the gun
        # and another ball waiting to plunge
        self.advance_time_and_run(2)
        self.assertModeRunning('multiball')
        # trough is empty, both balls in play
        self.assertEqual(0, self.machine.ball_devices.bd_trough.balls)
        self.assertEqual(2, self.machine.game.balls_in_play)
        self.assertEqual(1, self.machine.ball_devices.bd_gun.balls)
        # the other ball is 'unclaimed', waiting to plunge

        ##################
        ## TEST SCORING ##
        ##################

        # release lock when 'playfield_active' switch hit
        # cluster bombs vary by time so mock with a slingshot
        self.hit_and_release_switch("s_slingshot_1")
        self.hit_and_release_switch("s_slingshot_2")
        current_score += 20 * 2
        self.assertEqual(current_score, self.machine.game.player.score)

        self.advance_time_and_run(2)
        self.assertEqual(2, self.machine.playfield.balls)

        self.hit_and_release_switch("s_bumper_1")
        self.hit_and_release_switch("s_bumper_2")
        self.hit_and_release_switch("s_bumper_3")
        current_score += 1000 * 3
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_spinner")
        current_score += 200
        self.assertEqual(current_score, self.machine.game.player.score)

        # These award an extra ball, so skip
        # but leaving here for scoring reference
        #self.hit_and_release_switch("s_rollover_bonus_ball_1")
        #self.hit_and_release_switch("s_rollover_bonus_ball_2")
        #current_score += 2000 * 2

        self.hit_and_release_switch("s_stationary_thousand")
        current_score += 2000
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_stationary_advance_bonus")
        current_score += 200
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_stationary_advance_hole_score")
        current_score += 200
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_kicker_missile")
        current_score += 100 # first 3 counters of hole_score mode
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_rollover_advance_hole_1")
        self.hit_and_release_switch("s_rollover_advance_hole_2")
        current_score += 2000 * 2
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_drop_target_behind")
        current_score += 1000 # normally 500
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_stationary_special")
        current_score += 1000
        self.assertEqual(current_score, self.machine.game.player.score)

        self.hit_and_release_switch("s_kicker_gun")
        current_score += 10000

        # bumpers score 10x while we have 2 balls in play
        self.hit_and_release_switch("s_bumper_1")
        self.hit_and_release_switch("s_bumper_2")
        self.hit_and_release_switch("s_bumper_3")
        current_score += 3000

        # wait for "shoot again" to expire
        self.advance_time_and_run(15)
        # ball drains, ending multiball but not player's turn
        self.hit_switch_and_run('s_trough_1', 2)
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertModeNotRunning('multiball')
        # bumpers back to normal with single ball in play
        self.hit_and_release_switch("s_bumper_1")
        current_score += 100
        # draining again ends the ball
        self.assertEqual(1, self.machine.game.player.ball)
        self.hit_switch_and_run('s_trough_2', 1)
        self.assertEqual(2, self.machine.game.player.ball)
