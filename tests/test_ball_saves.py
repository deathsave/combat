import os
from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestBallSaves(MpfMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_timer(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")

        # timer begins on first switch hit
        self.hit_and_release_switch("s_spinner")
        self.assertTrue(self.machine.
            ball_saves["default"].enabled)
        self.advance_time_and_run(11) # within 2s grace period

        # draining before timer expires will save the ball
        self.hit_switch_and_run('s_trough_1', 4)
        self.assertEqual(1, self.machine.game.player.ball)
        self.assertEqual(1,
            self.machine.ball_devices.bd_shooter_lane.balls)
        self.assertFalse(self.machine.
            ball_saves["default"].enabled)
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_and_release_switch("s_spinner")

        # playing/draining again ends the ball
        self.hit_switch_and_run('s_trough_1', 4)
        self.assertEqual(2, self.machine.game.player.ball)
        self.assertEqual(1,
            self.machine.ball_devices.bd_shooter_lane.balls)
        self.assertTrue(self.machine.
            ball_saves["default"].enabled)
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_and_release_switch("s_spinner")

        # wating to drain after timer expiry
        # will NOT save the ball
        self.advance_time_and_run(10) # 10s+2s grace
        self.assertTrue(self.machine.
            ball_saves["default"].enabled)

        # after 2s grace, we lose the ball
        self.advance_time_and_run(2)
        self.assertFalse(self.machine.
            ball_saves["default"].enabled)
        self.hit_switch_and_run('s_trough_1', 4)
        self.advance_time_and_run(4)
        self.assertEqual(3, self.machine.game.player.ball)

    def test_laser_bombs_outlane(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")
        # expire ball save timer
        self.advance_time_and_run(12) # 10s+2s grace

        # activate bombs dropped mode
        for x in range(0, 5):
            self.hit_and_release_switch("s_drop_target")
        # the mech itself triggers this switch
        # as soon as all 5 targets have dropped
        self.hit_and_release_switch("s_drop_target_reset")
        self.assertModeRunning('bombs_dropped')

        # outlane awards extra ball during laser bombs
        # but will often drain - more like a ball save
        self.hit_and_release_switch("s_rollover_bonus_ball_1")
        self.hit_switch_and_run('s_trough_1', 4)
        self.assertEqual(1, self.machine.game.player.ball)
