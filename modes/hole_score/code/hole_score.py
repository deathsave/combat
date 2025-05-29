from mpf.core.mode import Mode
from mpf.core.delays import DelayManager

class Custom(Mode):
    def mode_start(self, **kwargs):
        player = self.machine.game.player
        if player.is_player_var('hole_score_count'):
            awarded_score = 0
            if player.hole_score_count >= 10:
                print("Awarding 50000 for hole score")
                awarded_score += 50000
            elif player.hole_score_count > 6:
                awarded_score += 5000
            elif player.hole_score_count > 3:
                awarded_score += 500
            else:
                awarded_score += 50
            if self.machine.modes.multiball.active:
                awarded_score *= 2
            player.score += awarded_score
            player.hole_score_count = 0
        del kwargs
