# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode

class Custom(Mode):
    # MPF persists player's scores so they can display in the attact
    # mode, but then they akwardly display immediately in a new game
    # until scoring happens. this clears them
    def initialize_player_scores(self, **kwargs):
        # TODO: this is not working. cant seem to clear the persisted
        # values for scores between games... (issue #939 in MPF core)
        for player in self.machine.game.player_list:
            self.machine.remove_machine_var(
                name='player{}_score'.format(player.number))
            self.machine.create_machine_var(
                'player{}_score'.format(player.number),
                value=0,
                persist=False,
                expire_secs=None,
                silent=False)
        del kwargs

    def track_score_levels(self, **kwargs):
        # Tracks the player's score to see if they are entitled
        # to an extra ball at various levels (currently only 1 level)
        player = self.machine.game.player
        if player.score_level > 0:
            return
        elif player.score_level == 0 and player.score >= 250000:
            self.machine.extra_balls.score_level_1.award()
            self.machine.coils.c_knocker.pulse()
            player.score_level = 1
        del kwargs

    def mode_init(self):
        self.machine.events.add_handler(
            'multiplayer_game', self.initialize_player_scores)
        self.machine.events.add_handler(
            'player_score', self.track_score_levels)

    def mode_start(self, **kwargs):
        #print('Resetting Drop Target')
        self.machine.coils.c_drop_target.pulse()
