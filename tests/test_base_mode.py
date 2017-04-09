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
        self.hit_and_release_switch("s_bumper_1")
        self.assertEqual(100, self.machine.game.player.score)
        self.hit_and_release_switch("s_bumper_2")
        self.assertEqual(200, self.machine.game.player.score)
        self.hit_and_release_switch("s_bumper_3")
        self.assertEqual(300, self.machine.game.player.score)

        ## test rollover top scoring
        self.hit_and_release_switch("s_rollover_1")
        self.assertEqual(800, self.machine.game.player.score)
        self.hit_and_release_switch("s_rollover_2")
        self.assertEqual(1300, self.machine.game.player.score)
        self.hit_and_release_switch("s_rollover_3")
        self.assertEqual(1800, self.machine.game.player.score)
        self.hit_and_release_switch("s_rollover_4")
        self.assertEqual(2300, self.machine.game.player.score)
        self.hit_and_release_switch("s_rollover_5")
        self.assertEqual(2800, self.machine.game.player.score)
        self.hit_and_release_switch("s_rollover_6")
        self.assertEqual(3300, self.machine.game.player.score)
        self.hit_and_release_switch("s_rollover_7")
        self.assertEqual(3800, self.machine.game.player.score)

        #self.assertTextOnTopSlide("BALL 1    FREE PLAY")
        #self.advance_time_and_run()
        #self.assertEqual(4 * 75020, self.machine.game.player.score)
        #self.assertTextOnTopSlide("300,080")

        ## ball drains
        #self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        ## wait for highscore display
        #self.advance_time_and_run(10)
        #self.assertEqual(0, self.machine.playfield.balls)
        #self.assertEqual(2, self.machine.game.player.ball)

        ## and it should eject a new ball to the pf
        #self.advance_time_and_run(20)
        #self.assertEqual(1, self.machine.playfield.balls)

        ## ball drains again
        #self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        ## wait for highscore display
        #self.advance_time_and_run(10)
        #self.assertEqual(0, self.machine.playfield.balls)
        #self.assertEqual(3, self.machine.game.player.ball)

        ## and it should eject a new ball to the pf
        #self.advance_time_and_run(20)
        #self.assertEqual(1, self.machine.playfield.balls)

        ## ball drains again. game should end
        #self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        #self.advance_time_and_run(10)

        #self.mock_event('text_input_high_score_complete')

        ## enter high score
        #self.assertSlideOnTop("high_score_enter_initials")
        #self.hit_and_release_switch("s_flipper_lower_right")
        #self.hit_and_release_switch("s_flipper_lower_right")
        #self.hit_and_release_switch("s_start")  # C
        #self.advance_time_and_run()
        #self.assertTextOnTopSlide("C")
        #self.hit_and_release_switch("s_flipper_lower_right")
        #self.hit_and_release_switch("s_start")  # CD
        #self.advance_time_and_run()
        #self.assertTextOnTopSlide("CD")
        #self.hit_and_release_switch("s_flipper_lower_right")
        #self.hit_and_release_switch("s_start")  # CDE
        #self.advance_time_and_run()
        #self.assertTextOnTopSlide("CDE")

        # TODO dunno why this doesn't work
        # self.assertEventCalled('text_input_high_score_complete')
        # self.advance_time_and_run(10)
        # self.assertIsNone(self.machine.game)
    def begin_gameplay(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_plunger_lane")
        self.advance_time_and_run(4) # 3+1
