import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestGameStart(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_game_start(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()
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
        self.advance_time_and_run()
        self.assertEqual(0, self.machine.playfield.balls)
        ## after a brief delay, the ball is now on the playfield...
        ## if this errors, could be system-specific so increase it
        self.advance_time_and_run(3)
        self.assertEqual(1, self.machine.playfield.balls)

