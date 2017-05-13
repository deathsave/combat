import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestAttractMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_dmd_display(self):
        self.advance_time_and_run()
        # verify widget is on the DMD
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn('Pinball Plaid', [x.text for x in current_widgets])
        # stop the mode and verify the widget has been removed
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()
        current_widgets = self.get_dmd_text_widgets()
        self.assertNotIn('Pinball Plaid', [x.text for x in current_widgets])

    #############
    ## Helpers ##
    #############

    def get_dmd_text_widgets(self):
        current_widgets = []
        virtual_dmd = self.mc.displays['dmd'].\
            children[0].\
            children[0].\
            children[0].\
            children[0].\
            children[0]
        for widget in virtual_dmd.children:
            if hasattr(widget, 'text'): current_widgets.append(widget)
        return current_widgets
