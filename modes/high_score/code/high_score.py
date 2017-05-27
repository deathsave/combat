from mpf.core.mode import Mode as m

class Custom(m):
    def mode_init(self):
        pass

    def mode_start(self, **kwargs):
        del kwargs

    def mode_stop(self, **kwargs):
        pass
