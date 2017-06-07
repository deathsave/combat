# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode as m

class Custom(m):
    def stop_bombs_dropped_mode(self, **kwargs):
        # because we don't want to award
        # extra balls while in multiball
        self.machine.modes.bombs_dropped.stop()
        del kwargs

    def mode_start(self, **kwargs):
        self.machine.events.add_handler(
            'ball_hold_gun_multi_balls_released', self.stop_bombs_dropped_mode)
        del kwargs

    def mode_stop(self, **kwargs):
        """This code will run every time this mode stops."""
        pass
