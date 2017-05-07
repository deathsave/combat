import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestBombsDroppedMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_scoring(self):
        # before mode
        current_score = 0
        self.begin_gameplay()
        self.hit_and_release_switch("s_stationary_special")
        current_score += 500
        self.assertEqual(current_score, self.machine.game.player.score)
        self.trigger_mode()
        current_score += 5000
        self.assertEqual(current_score, self.machine.game.player.score)
        # mode is now live
        self.hit_and_release_switch("s_drop_target")
        current_score += 10000 # 10x multi on drop targets during mode
        self.advance_time_and_run(1)
        self.assertEqual(current_score, self.machine.game.player.score)
        self.hit_and_release_switch("s_stationary_special")
        current_score += 20000
        self.assertEqual(current_score, self.machine.game.player.score)
        self.assertModeNotRunning('bombs_dropped')
        self.assertModeRunning('base')
        print('mode no longer running, should NOT block')
        # hitting special ends mode
        # assert our return to base mode scoring
        self.hit_and_release_switch("s_drop_target")
        current_score += 1000
        self.assertEqual(current_score, self.machine.game.player.score)


    def test_lighting(self):
        # TODO
        pass

    # show something??? "Hit the Special!"
    def test_dmd_display(self):
        # TODO
        pass

    # coil should fire to reset drop targets
    def test_targets_reset(self):
        # TODO
        pass

    #############
    ## Helpers ##
    #############

    def begin_gameplay(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_plunger_lane")
        self.advance_time_and_run(4) # 3+1
        self.assertEqual(1, self.machine.playfield.balls)

    def trigger_mode(self):
        for x in range(0, 5):
            self.hit_and_release_switch("s_drop_target")
        # the mech itself triggers this switch
        # as soon as all 5 targets have dropped
        self.hit_and_release_switch("s_drop_target_reset")
        self.assertModeRunning('bombs_dropped')
