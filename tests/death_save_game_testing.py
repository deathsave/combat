import os
from mpf.core.rgb_color import RGBColor
from mpf.tests.MpfGameTestCase import MpfGameTestCase

class DeathSaveGameTesting(MpfGameTestCase):

    def get_config_file(self):
        return 'development.yaml'

    def get_machine_path(self):
        return os.path.abspath(os.path.join(
            os.path.realpath(__file__),
            os.pardir,os.pardir
        ))

    ##################
    # Helper Methods #
    ##################

    # For given :var, activate given :switch and check
    # whether value has increased by given :value
    #
    # @param var: variable to check (score, bonus, etc.)
    # @param switch: switch to activate (s_spinner, s_pop1, etc.)
    # @param value: amount we expect the :var to increase by
    #
    # Example: self.assertIncrement("score", "s_spinner", 10)
    #
    def assertIncrement(self, var, switch, value):
        current_val = getattr(self.machine.game.player, var)
        value, getattr(self.machine.game.player, var)
        self.hit_and_release_switch(switch)
        self.advance_time_and_run(1)
        new_val = getattr(self.machine.game.player, var)
        self.assertEqual(
            value, new_val - current_val,
            "Expected %s, got %s" % (value, new_val - current_val)
        )
