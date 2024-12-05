from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestBombsDroppedMode(MpfMachineTestCase):

    def test_scoring(self):
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

        self.hit_and_release_switch("s_stationary_special")
        current_score += 500
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.trigger_mode()
        current_score += 5000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        # mode is now live
        self.hit_and_release_switch("s_drop_target")
        current_score += 10000
        # 10x multi on drop targets during mode
        self.advance_time_and_run(1)
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.hit_and_release_switch("s_stationary_special")
        current_score += 20000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertModeNotRunning('bombs_dropped')
        self.assertModeRunning('base')
        # hitting special ends mode
        # special scores 500 again
        self.hit_and_release_switch("s_stationary_special")
        current_score += 500
        self.assertEqual(current_score,
            self.machine.game.player.score)
        # assert our return to base mode scoring
        # and confirm we can trigger the mode again
        self.trigger_mode()
        current_score += 5000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertModeRunning('bombs_dropped')
        # and end it once more
        self.hit_and_release_switch("s_stationary_special")
        current_score += 20000
        self.assertEqual(current_score,
            self.machine.game.player.score)
        self.assertModeNotRunning('bombs_dropped')
        self.assertModeRunning('base')

    #############
    ## Helpers ##
    #############

    def trigger_mode(self):
        for x in range(0, 5):
            self.hit_and_release_switch("s_drop_target")
        # the mech itself triggers this switch
        # as soon as all 5 targets have dropped
        self.hit_and_release_switch("s_drop_target_reset")
        self.assertModeRunning('bombs_dropped')
