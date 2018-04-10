import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestDisplays(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_attract_mode_display(self):
        self.advance_time_and_run(2)
        # verify widget is on the DMD
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn('Zaccaria “Combat”', [x.text for x in current_widgets])
        self.assertIn('Reimagined by:', [x.text for x in current_widgets])
        self.assertIn('Pinball Plaid', [x.text for x in current_widgets])
        # stop the mode and verify the widget has been removed
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()
        current_widgets = self.get_dmd_text_widgets()
        self.assertNotIn('Zaccaria “Combat”', [x.text for x in current_widgets])

    def test_game_loop(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.assertModeRunning('base')
        self.assertEqual(1, self.machine.game.player.ball)

        # ball 1
        self.hit_and_release_switch("s_slingshot_1")
        self.advance_time_and_run(4)
        self.hit_and_release_switch('s_trough_2')
        self.advance_time_and_run(1)
        self.hit_and_release_switch('s_trough_2')
        self.advance_time_and_run(1)
        self.assertEqual(2, self.machine.game.player.ball)

        # ball 2
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_slingshot_1")
        self.advance_time_and_run(4)
        self.hit_switch_and_run('s_trough_2', 1)
        self.hit_switch_and_run('s_trough_2', 1)
        self.assertEqual(3, self.machine.game.player.ball)

        # ball 3
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_slingshot_1")
        self.advance_time_and_run(4)
        self.hit_switch_and_run('s_trough_2', 1)
        self.hit_switch_and_run('s_trough_2', 1)
        self.assertModeRunning('attract')

    #############
    ## Helpers ##
    #############

    def get_dmd_text_widgets(self):
        current_widgets = []
        for widget_container in self.mc.displays['dmd'].current_slide.widgets:
            if hasattr(widget_container.widget, 'text'): current_widgets.\
                append(widget_container.widget)
        return current_widgets
