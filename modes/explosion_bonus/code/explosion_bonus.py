from mpf.core.mode import Mode as m

class Custom(m):
    def mode_start(self, **kwargs):
        # NICE TO HAVE - unlight each led and fire
        # a sound in sequence
        player = self.machine.game.player
        base_bonus_score = (
            (player.explosion_bonus_state.value - 1) * 1000)
        print("bonus_active: %s" % player.is_bonus_active)
        if not self.machine.game.tilted:
            if self.machine.modes.explosion_multiplier.active:
                player.score += (base_bonus_score * 10)
            else:
                player.score += base_bonus_score
        del kwargs
