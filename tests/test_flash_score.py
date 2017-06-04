import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestFlashScoreMode(FullMachineTestCase):

    def getMachinePath(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_timer_scoring(self):
        current_score = 0
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")
        current_score += 500
        # bumpers pay normally at the moment
        self.assertModeNotRunning('flash_score')
        self.hit_and_release_switch("s_bumper_1")
        current_score += 100

        # activate mode with missile
        self.hit_and_release_switch("s_kicker_missile")
        self.advance_time_and_run(1) # wait for ball hold
        current_score += 50

        # during flash score, bumpers pay 10x
        self.assertModeRunning('flash_score')
        self.hit_and_release_switch("s_bumper_1")
        current_score += 1000

        # still the case 12 (10 + 1 from hold) seconds later
        self.advance_time_and_run(10)
        self.assertModeRunning('flash_score')
        self.hit_and_release_switch("s_bumper_2")
        current_score += 1000

        # still running at exactly 15 seconds
        self.advance_time_and_run(3)
        self.assertModeRunning('flash_score')
        self.hit_and_release_switch("s_bumper_3")
        current_score += 1000

        # mode ends after 15 seconds
        self.advance_time_and_run(1)
        self.assertModeNotRunning('flash_score')
        self.hit_and_release_switch("s_bumper_3")
        current_score += 100

    def test_future_duration(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)

        # begin gameplay
        self.hit_and_release_switch("s_rollover_top_2")

        # activate mode with gun this time
        self.hit_and_release_switch("s_kicker_gun")
        self.advance_time_and_run(1)
        self.assertModeRunning('flash_score')

        # mode still running 14 (13 + 1 hold) seconds from activation
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
