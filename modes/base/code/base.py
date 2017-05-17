# This is a template file you can use to add Python code to a mode.

# To use it, and it to <your_machine>/modes/<your_mode>/code/<your_mode>.py

# Also, add a blank file called __init__.py to your machine folder root, and
# to your "modes" folder, and to your mode's "code" folder. (3 total)

# Also add a "code: your_mode.YourMode" (or whatever you call it) to the
# "mode:" section of your mode's <mode_name>.yaml configuration file.

from mpf.core.mode import Mode as m

class Custom(m):
    # MPF persists player's scores so they can display in the attact
    # mode, but then they akwardly display immediately in a new game
    # until scoring happens. this clears them
    def initialize_player_scores(self, **kwargs):
        # TODO: this is not working. cant seem to clear the persisted
        # values for scores between games...
        for player in self.machine.game.player_list:
            print('Removing player{}s score'.format(player.number))
            self.machine.remove_machine_var(
                name='player{}_score'.format(player.number))
            self.machine.create_machine_var(
                'player{}_score'.format(player.number),
                value=0,
                persist=False,
                expire_secs=None,
                silent=False)
        del kwargs

    def mode_init(self):
        """This code that will run once mode when MPF boots."""
        self.machine.events.add_handler(
            'multiplayer_game', self.initialize_player_scores)
        pass

    def mode_start(self, **kwargs):
        """This code will run every time this mode starts."""
        print('base mode started')
        del kwargs

        # call seek(self.player.bgm_position) to resume OR start music

    def mode_stop(self, **kwargs):
        """This code will run every time this mode stops."""
        # call get_pos() on sound and save
        # to self.player.bgm_position
        print('base mode ended')
        pass
