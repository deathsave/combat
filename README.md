Combat by Zaccaria
==================

Brought back from the dead by [Pinball Plaid](http://pinballplaid.com/). Thanks to the guys at [FAST](http://fastpinballdev.gdsocial.com/) and the [Mission Pinball Project](https://github.com/missionpinball) for all the support.

Development
-----------

### Installing MPF

**On Ubuntu/Debia Linux**

See `./.github/workflows/python-app.yml` to match the CI build.

**On MacOS**

1. Install `brew` with:
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
1. Install system deps and `pyenv`with:
   `brew install SDL2 SDL2_mixer SDL2_image SDL2_ttf gstreamer pkg-config pyenv` and follow instructions to add `pyenv`
   to your shell.
1. Install Python 3.11 with:
   `pyenv install 3.11.10`
1. Install mpf with:
   `pip install mpf==0.57`
1. Install mpf-mc with:
   `pip install mpf-mc==0.57`
1. Install mpf-monitor with:
   `pip install mpf-monitor==0.57`
1. Install foreman with:
   `gem install foreman` - this makes it possible to run all 3
   processes in single terminal window for local development.

### Running

- **Development** - `bin/dev` will run both `mpf` and `mpf-mc`
  without the console GUI. It will also run `mpf monitor` so
  you can interact with it.
- **Production** - `bin/run` will run for production using
  the real hardware devices and the console GUI.
- **Test** - Run a test with `bin/test tests/test_something.py` or
  simply `bin/test` to run all tests from the `./tests` folder.

Tinkering
---------

Run `bin/dev` to start the game in development mode. Then use
the keyboard for simulating switch hits.

Here is what we have mapped thus far:

**Primary Switches**

* Use the keys `z and /` for left and right flipper respectively
* The key `s` will start a game
* The key `l` will launch a ball
* Use the keys `1 and 2` to trigger a trough switch (drains a ball)

**Scoring Switches**

* The key `p` hits a Pop Bumper
* The key `d` hits a "B.O.M.B.S." Drop Target
* The key `g` simulates a ball entering the "Gun" (right hole)
* The key `m` simulates a ball entering the "Missile" (left hole)
* The key `h` advances the "hole score" value
* The key `b` advances the "end of ball bonus" value
* The key `c` hits the "Special" stationary target
* The key `n` simulates one *tick* of the "Spinner"
* The key `t` triggers a tilt (3 ends the ball)

Conventions
-----------

* time shows in with 0.3s base (0.15s, 0.6s, 1.2s, etc.).
