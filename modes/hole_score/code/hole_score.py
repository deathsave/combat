from mpf.core.mode import Mode
from mpf.core.delays import DelayManager

class Custom(Mode):
    def mode_start(self, **kwargs):
        player = self.machine.game.player
        print("****************************************")
        print(player.is_player_var('hole_score_count'))
        print(player.hole_score_count)
        if player.is_player_var('hole_score_count'):
            awarded_score = 0
            if player.hole_score_count >= 10:
                print("Awarding 50000 for hole score")
                awarded_score += 50000
                self.machine.events.post("hole_score_redeem_max")
            elif player.hole_score_count > 6:
                print("Awarding 5000 for hole score")
                awarded_score += 5000
                self.machine.events.post("hole_score_redeem")
            elif player.hole_score_count > 3:
                print("Awarding 500 for hole score")
                awarded_score += 500
                self.machine.events.post("hole_score_redeem")
            else:
                print("Hole score count less than 4, awarding 100 per hole")
                awarded_score += 50
                self.machine.events.post("hole_score_redeem")
            if self.machine.modes.multiball.active:
                print("Awarding double hole score")
                awarded_score *= 2
            player.score += awarded_score
            # player.hole_score_count = 0
        print("****************************************")
        del kwargs
