import os
from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestGameStart(MpfMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(
            os.path.realpath(__file__), os.pardir, os.pardir)
        )

    def test_game_start(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()
        ## game should be running
        self.assertIsNotNone(self.machine.game)
        self.assertEqual(1, self.machine.game.player.ball)
        ## playfield expects a ball
        self.assertEqual(1, self.machine.playfield.available_balls)
        ## ball is ejected to plunger
        self.assertEqual(
            1, self.machine.ball_devices["bd_shooter_lane"].balls
        )
        self.assertEqual(0, self.machine.playfield.balls)
        ## player launches a ball
        self.hit_and_release_switch('s_shooter_lane')
        self.advance_time_and_run()
        ## and it hits a playfield switch
        self.hit_and_release_switch("s_rollover_top_2")
        ## not immediately "on the playfield", though
        self.assertBallsOnPlayfield(0)
        ## after a brief delay, the ball is now on the playfield...
        self.advance_time_and_run()
        self.assertEventCalled("playfield_active")
        self.assertBallsOnPlayfield(1)

