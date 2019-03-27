class Timer:
    def __init__(self, init_ticks):
        self._ticks = init_ticks

    @property
    def ticks(self):
        return self._ticks

    def _set_ticks(self, value):
        self._ticks = value

    def forward(self, time_step):
        self._set_ticks(self.ticks - time_step)

    def is_exhausted(self):
        return self.ticks <= 0
