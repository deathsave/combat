import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestBaseMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_scoring(self):
        ## See Cluster Bombs test for rollovers (timed scoring)

        current_score = 0
        self.hit_and_release_switch("s_start")

        # initialize mode happens first
        # when drop target is reset here, it should not score
        # the hit counter resets when base mode begins, too
        self.assertModeNotRunning('base')
        self.hit_and_release_switch("s_drop_target_reset")
        self.hit_and_release_switch("s_drop_target")
        self.assertEqual(current_score, self.machine.game.player.score)

        # base mode activates after 500ms from initialization
        self.advance_time_and_run(1)
        self.assertModeRunning('base')
        self.hit_and_release_switch("s_rollover_top_2")
        self.advance_time_and_run(4) # 3+1
        current_score += 500
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test pop bumper scoring
        self.hit_and_release_switch("s_bumper_1")
        self.hit_and_release_switch("s_bumper_2")
        self.hit_and_release_switch("s_bumper_3")
        current_score += 100 * 3
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test drop target scoring
        for x in range(0,4):
            self.hit_and_release_switch("s_drop_target")
            current_score += 1000
        self.assertEqual(current_score, self.machine.game.player.score)

        # test switch 'behind' drop target
        self.hit_and_release_switch("s_drop_target_behind")
        current_score += 500
        self.assertEqual(current_score, self.machine.game.player.score)

        # test entering the 'Missile' ball device (hole_score collect)
        self.hit_and_release_switch("s_kicker_missile")
        current_score += 50
        self.assertEqual(current_score, self.machine.game.player.score)

        # text entering the 'Gun' ball device
        self.hit_and_release_switch("s_kicker_gun")
        self.advance_time_and_run(2) # wait to get into the mode
        current_score += 5000

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
        current_score += 100 * 2
        self.assertEqual(current_score, self.machine.game.player.score)

        ## test 'scoring' stationary targets
        self.hit_and_release_switch("s_stationary_thousand")
        current_score += 1000
        self.hit_and_release_switch("s_stationary_special")
        current_score += 500 # more when 'lit'
        self.assertEqual(current_score, self.machine.game.player.score)
