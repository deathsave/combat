import os
from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestFlashScoreMode(MpfMachineTestCase):

    def test_timer_scoring(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")
        current_score += 500

        # spinner and bumpers pay normally at the moment
        self.assertModeNotRunning('flash_score')
        self.hit_and_release_switch("s_spinner")
        self.hit_and_release_switch("s_bumper_1")
        current_score += 100 * 2
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # activate mode with missile
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1) # wait for ball hold
        current_score += 50
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # during flash score, bumpers pay 10x
        self.assertModeRunning('flash_score')
        self.hit_and_release_switch("s_bumper_1")
        current_score += 1000
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # spinner also goes 10x
        self.hit_and_release_switch("s_spinner")
        current_score += 1000
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # still the case 12 (10 + 1 from hold) seconds later
        self.advance_time_and_run(10)
        self.assertModeRunning('flash_score')
        self.hit_and_release_switch("s_bumper_2")
        current_score += 1000
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # still running at exactly 15 seconds
        self.advance_time_and_run(3)
        self.assertModeRunning('flash_score')
        self.hit_and_release_switch("s_bumper_3")
        current_score += 1000
        self.assertEqual(current_score,
            self.machine.game.player.score)

        # mode ends after 15 seconds
        self.advance_time_and_run(1)
        self.assertModeNotRunning('flash_score')
        self.hit_and_release_switch("s_bumper_3")
        current_score += 100
        self.assertEqual(current_score,
            self.machine.game.player.score)

    def test_future_duration(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")

        # activate mode with gun this time
        self.hit_and_release_switch("s_kicker_gun")
        self.advance_time_and_run(1)
        self.assertModeRunning('flash_score')

        # mode still running 14 (13 + 1 hold)
        # seconds from activation
        self.advance_time_and_run(13)
        self.assertModeRunning('flash_score')

        # mode expires 1 second later
        self.advance_time_and_run(1)
        self.assertModeNotRunning('flash_score')

        # wait 10 seconds and activate again
        self.advance_time_and_run(10)
        self.hit_and_release_switch("s_kicker_gun")
        self.advance_time_and_run(1)
        self.assertModeRunning('flash_score')

        # prove the timer doesn't keep ticking between runs
        # (running at 14s after activation)
        self.advance_time_and_run(13)
        self.assertModeRunning('flash_score')

        # mode expires again 1 second later
        self.advance_time_and_run(1)
        self.assertModeNotRunning('flash_score')
