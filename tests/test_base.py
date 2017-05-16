import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestBaseMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_scoring(self):
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
        # hit drop target only 4/5 times
        # so we don't trigger the bombs_dropped mode
        self.hit_and_release_switch("s_drop_target")
        self.hit_and_release_switch("s_drop_target")
        self.hit_and_release_switch("s_drop_target")
        self.hit_and_release_switch("s_drop_target")
        current_score += 1000 * 4
        self.assertEqual(current_score, self.machine.game.player.score)

        # test switch 'behind' drop target
        self.hit_and_release_switch("s_drop_target_behind")
        current_score += 500
        self.assertEqual(current_score, self.machine.game.player.score)

        # test lowest "Hole Score" value (saucer)
        # TODO: renable when we get wired
        #self.hit_and_release_switch("s_kicker_saucer")
        #current_score += 50
        #self.assertEqual(current_score, self.machine.game.player.score)

        # test gun score
        self.hit_and_release_switch("s_kicker_gun")
        current_score += 5000
        self.assertEqual(current_score, self.machine.game.player.score)

        # test spinner
        self.hit_and_release_switch("s_spinner")
        current_score += 100
        self.assertEqual(current_score, self.machine.game.player.score)

        # test slingshot scoring
        # TODO: reenable when we hook up mechs
        #self.hit_and_release_switch("s_slingshot_1")
        #self.hit_and_release_switch("s_slingshot_2")
        #current_score += 10 * 2
        #self.assertEqual(current_score, self.machine.game.player.score)

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
        current_score += 500 # more when 'lit'
        self.assertEqual(current_score, self.machine.game.player.score)

    #############
    ## Helpers ##
    #############

    def begin_gameplay(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_plunger_lane")
        self.advance_time_and_run(4) # 3+1
