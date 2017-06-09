Combat by Zaccaria
==================

*Re-imagined by Pinball Plaid.

Game Rules
----------

### Flash Score

How:

* Launch a missle (northwest kicker) or
* Fire the gun (northeast kicker)

What: 

* Pop Bumpers score 1,000
* Spinner lights and scores 1,000 as well
* Active for 15 seconds only


### Laser-guided Bombs


How:

* Drop all five B.O.M.B.S. targets

What:

* Drop 'Laser-guided' bombs to score 10k
* Fire 'Laser-guided' Torpedo (special) which:
  * Inflicts significant damage (scores 20k)
  * Gives up our position (forfeit 10x bombs multiplier)
* Rolling over outlanes award extra ball


### Missile Launch (Hole Score Bonus)

Fuel up the missile and launch it!

How to advance:

* Shoot the battleship (spinner) or
* Shoot the right-side 'Advance Hole Score' target or
* Roll over in-lanes

How to collect:

* Roll into the hole at the peak of the missile lane.

Points:

* 50 points to 30% lit
* 500 points to 60% lit
* 5,000 points to 90% lit
* 50,000 points fully lit


### Explosion Bonus

How:

* Roll over Cluster Bombs (when lit) or
* Hit right-side 'Explosion Bonus' target

What:

* Collected at end of ball.
* Fire the gun for x10 Multiplier:


### Same Player Shoots Again

How:

* Exceed 150k points for the first time
* Roll over outlanes during 'Laser Bombs'

What:

* Extra ball awarded


### Multiball

How:

* After activating Laser Bombs, load the gun

What:

* 2-ball Multiball
* Flash score all day (Pop Bumpers score 1,000)
* Other targets score 2x
  * Exceptions:
    * Cluster bombs score normally


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
