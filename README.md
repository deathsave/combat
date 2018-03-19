Combat by Zaccaria
==================

Brought back from the dead by [Pinball Plaid](http://pinballplaid.com/). Thanks to the guys at [FAST](http://fastpinballdev.gdsocial.com/) and the [Mission Pinball Project](https://github.com/missionpinball) for all the support.


Development
-----------

Most of the work is handled by a YAML config which we have split into smaller
files contextually in the `./config` directory. The `./monitor` directory
is the configuration of component positioning on the virtual playfield display.


Conventions
-----------

* time shows in with 0.3s base (0.15s, 0.6s, 1.2s, etc.).


Testing
-------

Run the test suite with `python -m unittest tests/*.py`.


Tinkering
---------

It's ideal to run 2 separate terminal sessions.

* In the first, run `mpf both -X` which will launch the MPF engine 
and the media controller.
* In the other, run `mpf monitor` which will launch the virtual 
playfield and state monitor.

There is also a virtual keyboard for simulating the switch hits. Here 
is what we have mapped thus far:

* Use the keys `z and /` for left and right flipper respectively
* The key `s` will start a game
* The key `l` will launch a ball
* The key `a` will simulate a playfield switch (top rollover)
* Use the keys `1 and 2` to trigger a trough switch (drains a ball)
