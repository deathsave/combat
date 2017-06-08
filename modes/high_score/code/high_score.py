from mpf.core.mode import Mode as m

class Custom(m):
    def mode_init(self):
        pass

    def set_high_score_indication(self, **kwargs):
        self.machine.is_high_score_set = True
        pass

    def mode_start(self, **kwargs):
        self.machine.events.add_handler(
            'high_score_enter_initials', self.set_high_score_indication)

        del kwargs

    def mode_stop(self, **kwargs):
        pass
