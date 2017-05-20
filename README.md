Combat by Zaccaria
==================

*Re-imagined by Pinball Plaid.

Game Rules
----------

### TODO: Flash Score

Launch a missle (northwest kicker) or fire the gun (northeast kicker)

* Active for 15 seconds.
* Pop Bumpers score 1,000
* Cluster Bombs (north rollovers) score 5,000


### Laser-guided Bombs (bombs_dropped)

Enemy is in plain sight. Attack!

* Laser-guided bombs are deadly accurate and score 10k
* Laser-guided Torpedo (special):
  * Pro: Inflicts significant damage (scores 20k)
  * Con: Gives up our position (forfeit 10x bombs multiplier)
* Outlanes light and award extra ball


### Hole Score Bonus

Shoot the battleship (spinner), right-side target or in-lane to advance.
Launch a missle to collect.

* 50 points to 30% lit
* 500 points to 60% lit
* 5,000 points to 90% lit
* 50,000 points fully lit


### TODO: Explosion Bonus (use MPF built-in game-over bonus)

Shoot the Cluster Bombs (when lit) or right-side target to advance.

* Collected at end of ball.

#### TODO: x10 Explosion Bonus Multiplier

* South-most led lit
* Activation Logic TODO


### TODO: Same Player Shoots Again

Awarded after 100 battleships (spins) on a single ball.
Only awarded once per game, per player.

* Lights the led at bottom of playfield
* Free ball after draining


### Multiball

After dropping the bombs, load the gun to activate.


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

Run the automated tests with `python -m unittest tests/*.py`.

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
