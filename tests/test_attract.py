import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestAttractMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_dmd_display(self):
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

    #############
    ## Helpers ##
    #############

    def get_dmd_text_widgets(self):
        current_widgets = []
        for widget_container in self.mc.displays['dmd'].current_slide.widgets:
            if hasattr(widget_container.widget, 'text'): current_widgets.\
                append(widget_container.widget)
        return current_widgets
