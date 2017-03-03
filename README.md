Combat by Zaccaria
==================

*Re-imagined by Pinball Plaid.

Development
-----------

Most of the work is handled by a YAML config which we have split into smaller
files contextually in the `.config` directory. The `./monitor` directory
is the configuration of component positioning on the virtual playfield display.

Testing Locally
---------------

* Run a virtual session with `mpf both -X`
   * You do not need actual hardware connected
* The key `s` will start a game
* The key `l` will launch a ball
* The key `a` will simulate a playfield switch (top rollover specifically)
* Use the keys `1, 2, or 3` to trigger a trough switch (draining the ball)
