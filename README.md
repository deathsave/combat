Combat by Zaccaria
==================

Brought back from the dead by [Pinball Plaid](http://pinballplaid.com/). Thanks to the guys at [FAST](http://fastpinballdev.gdsocial.com/) and the [Mission Pinball Project](https://github.com/missionpinball) for all the support.


Development
-----------

Most of the work is handled by a YAML config which we have split into smaller
files contextually in the `./config` directory. The `./monitor` directory
is the configuration of component positioning on the virtual playfield display.

### Up and Running on MacOS

Install Homebrew.

```bash
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then, install pyenv (and Python 3.5.3).

```bash
  brew install pyenv
  pyenv install 3.5.3
  pyenv global 3.5.3
  echo 'if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi' >> ~/.bashrc
  source ~/.bashrc
```

...and the mac-specific deps.

```bash
  wget https://mpf.kantert.net/mpf_mac_frameworks.zip
  unzip mpf_mac_frameworks.zip
  sudo mv Frameworks/* /Library/Frameworks/
  rm -Rf Frameworks
  rm -Rf __MACOSX
  rm -Rf ReadMe.txt
  rm -Rf License.txt
  rm -Rf mpf_mac_frameworks.zip
```

Finally, install mpf-recommended `cython` version and "dev" mpf.

```bash
  pip3 install pip setuptools cython==0.24.1 --upgrade
  pip3 install mpf mpf-mc mpf-monitor --pre
```


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
