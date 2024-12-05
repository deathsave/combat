from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestDisplays(FullMachineTestCase):

    def test_game_loop(self):
        # attract mode
        self.advance_time_and_run(2)
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn('Zaccaria “Combat”',
            [x.text for x in current_widgets])
        self.assertIn('Reimagined by:',
            [x.text for x in current_widgets])
        self.assertIn('Pinball Plaid',
            [x.text for x in current_widgets])

        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

        self.assertEqual(1, self.machine.game.player.ball)

        # game begins, player is up
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn('Player 1 Up',
            [x.text for x in current_widgets])
        self.assertIn('Ball: 1',
            [x.text for x in current_widgets])
        self.assertIn('00', [x.text for x in current_widgets])

        # scoring is reflected
        self.hit_switch_and_run('s_slingshot_1', 2)
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn('10', [x.text for x in current_widgets])

        # TODO: removed temporarily for 0.57 migration
        #
        # draining during ball save reflected
        # self.hit_switch_and_run('s_trough_1', 2)
        # current_widgets = self.get_dmd_text_widgets()
        # self.assertIn('PLAYER 1 SHOOT AGAIN',
        #   [x.text for x in current_widgets])
        # self.hit_switch_and_run('s_trough_1', 2)

        # drain other 2 balls
        for ball in range(2, 4):
            self.assertEqual(ball, self.machine.game.player.ball)
            # ball drains twice (ball save)
            for i in range(0, 2):
                self.hit_switch_and_run('s_trough_1', 2)

        # game over screen 1
        self.assertModeRunning('game_over')
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn('GAME OVER',
            [x.text for x in current_widgets])
        self.assertIn(
            'Zaccaria Combat reimagined by Pinball Plaid - Steve Prehoda, Josiah Cox & Ryan Richardson',
            [x.text for x in current_widgets])

        # game over screen 2
        self.advance_time_and_run(15)
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn(
            'Music by Josiah Cox, Ryan Richardson, Terence Klein & Elliot Starks',
            [x.text for x in current_widgets])

        # game over screen 3
        self.advance_time_and_run(12)
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn(
            'Sound Effects by Raphael Rodriguez',
            [x.text for x in current_widgets]
        )

        # game over screen 4
        self.advance_time_and_run(12)
        current_widgets = self.get_dmd_text_widgets()
        self.assertIn(
            'Subscribe to the Pinball Plaid Podcast from http://pinballplaid.com/show',
            [x.text for x in current_widgets]
        )

        # back to attract mode
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)
        self.assertModeRunning('attract')

    #############
    ## Helpers ##
    #############

    def get_dmd_text_widgets(self):
        current_widgets = []
        for wgt in self.mc.displays['dmd'].current_slide.widgets:
            if hasattr(wgt.widget, 'text'):
                current_widgets.append(wgt.widget)
        return current_widgets
