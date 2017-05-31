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
        self.hit_and_release_switch("s_rollover_top_1")
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

        # lock should be enabled????

        # ball rolls into lock - doesn't score yet...
        self.hit_and_release_switch("s_kicker_gun")
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(1, self.machine.ball_devices.bd_gun.balls)

        # after some time, should be a locked ball in the gun
        # and another ball waiting to plunge
        self.advance_time_and_run(10)
        self.assertModeRunning('multiball')
        # trough is empty, both balls in play
        self.assertEqual(0, self.machine.ball_devices.bd_trough.balls)
        self.assertEqual(2, self.machine.game.balls_in_play)
        self.assertEqual(1, self.machine.ball_devices.bd_gun.balls)
        # the other ball is 'unclaimed', waiting to plunge

        # release lock when a top rollover is hit
        # meaning, user launched the unclaimed' ball
        self.hit_and_release_switch("s_rollover_top_1")
        # advancing only 10 actually fails here
        self.advance_time_and_run(12)
        self.assertEqual(2, self.machine.playfield.balls)
        # after release, gun switch is rolled over again
        # and this time scores 10k
        self.hit_and_release_switch("s_kicker_gun")
        current_score += 10000 # 10x multi on drop targets during mode
        # ensure gun doesn't hold ball infinitely during multiball
        self.advance_time_and_run(12)
        self.assertEqual(2, self.machine.playfield.balls)
        # bumpers score 10x while we have 2 balls in play
        self.hit_and_release_switch("s_bumper_1")
        self.hit_and_release_switch("s_bumper_2")
        self.hit_and_release_switch("s_bumper_3")
        current_score += 3000
        # ball drains, ending multiball but not player's turn
        self.hit_switch_and_run('s_trough_1', 1)
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertModeNotRunning('multiball')
        # bumpers back to normal with single ball in play
        self.hit_and_release_switch("s_bumper_1")
        current_score += 100
        # draining again ends the ball
        self.assertEqual(1, self.machine.game.player.ball)
        self.hit_switch_and_run('s_trough_2', 1)
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(2, self.machine.game.player.ball)
