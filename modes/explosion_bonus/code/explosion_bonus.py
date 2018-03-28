# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode as m

class Custom(m):
    def mode_start(self, **kwargs):
        #   NICE TO HAVE - unlight each led and fire a sound in sequence
        player = self.machine.game.player
        base_bonus_score = ((player.explosion_bonus_state.value - 1) * 1000)
        if player.tilt_warnings < 2:
            if self.machine.modes.explosion_multiplier.active:
                player.score += (base_bonus_score * 10)
            else:
                player.score += base_bonus_score
        del kwargs
