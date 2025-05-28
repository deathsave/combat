# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode
from mpf.core.delays import DelayManager

class Custom(Mode):
    def mode_start(self, **kwargs):
        player = self.machine.game.player
        awarded_score = 0
        if player.hole_score_state.value == 10:
            awarded_score += 50000
        elif player.hole_score_state.value > 6:
            awarded_score += 5000
        elif player.hole_score_state.value > 3:
            awarded_score += 500
        else:
            awarded_score += 50
        if self.machine.modes.multiball.active:
            awarded_score *= 2
        player.score += awarded_score
        # FUTURE? - award fragment of total for each count
        # for a "bonus collection" experience
        #awarded_part = awarded_score / player.hole_score_state.value

        #for i in range(player.hole_score_state.value):
        #    player.score += int(awarded_part) # rounding errors...
        # self.machine.modes.hole_score.stop()
        del kwargs
