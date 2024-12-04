"""Tests General/Base Functionality"""
import os
from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestGeneral(MpfMachineTestCase):

    """Tests start-up sequence"""

    def get_config_file(self):
        return 'development.yaml'

    def get_machine_path(self):
        return os.path.abspath(os.path.join(
            os.path.realpath(__file__),
            os.pardir,os.pardir
        ))

    def test_game_start(self):
        self.assertEqual(2,
            self.machine.ball_devices.bd_trough.balls)
        self.assertModeRunning('attract')
        self.assertModeNotRunning('base')
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.assertModeRunning('initialize')
        self.assertEqual(1,
            self.machine.ball_devices.bd_trough.balls)
        self.assertEqual(1,
            self.machine.ball_devices.bd_shooter_lane.balls)
        self.assertModeNotRunning('attract')
        self.assertModeRunning('base')
        self.hit_and_release_switch("s_shooter_lane")
        self.hit_and_release_switch("s_rollover_top_1")
        self.advance_time_and_run(4)
        self.assertEqual(1, self.machine.playfield.balls)
