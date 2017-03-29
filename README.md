Combat by Zaccaria
==================

*Re-imagined by Pinball Plaid.

Development
-----------

Most of the work is handled by a YAML config which we have split into smaller
files contextually in the `.config` directory. The `./monitor` directory
is the configuration of component positioning on the virtual playfield display.

Conventions
-----------

For shows, time things in 0.3s increments (or 1.2s). The idea is 12 seconds
is much more easily divisible than 1 second.

Testing Locally
---------------

You need to run 2 terminal sessions. In the first, run `mpf both -X` which
will launch the MPF engine and the media controller. In the other, run
`mpf monitor` which will launch the virtual monitor for a more "sane"
debugging experience. There is also a virtual keyboard for simulating the
switches. Here is what we have mapped thus far:

* Use the keys `z and /` for left and right flipper respectively
* The key `s` will start a game
* The key `l` will launch a ball
* The key `a` will simulate a playfield switch (top rollover)
* Use the keys `1 and 2` to trigger a trough switch (drains a ball)
