[![Tokens](https://img.shields.io/badge/Tokens-0-D97757)](https://claude.com/claude-code)
[![PyPI version](https://img.shields.io/pypi/v/cutienator)](https://pypi.org/project/cutienator/)
[![Python versions](https://img.shields.io/pypi/pyversions/cutienator)](https://pypi.org/project/cutienator/)
[![Systems](https://img.shields.io/badge/Systems-Linux_%7C_macOS_%7C_Windows-informational)](#where-it-runs)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# cutienator v0.0.1-dev1 (development build)
A vastly superior binding of Qt C++ to Python. 

# Where It Runs

On Linux, on macOS and on Windows. On Intel chips and on Apple silicon.
On every Python from 3.7* to 3.15.

Each release is tested on all of them before it goes out: 35 fresh
machines, each with its own system and its own Python, each building
cutienator against Qt 6.12 and calling Qt for real. A release happens
only if all 35 pass.

| System               | Pythons     | Machines |
|----------------------|-------------|---------:|
| Linux                | 3.7 to 3.15 |        9 |
| macOS, Apple silicon | 3.8 to 3.15 |        8 |
| macOS, Intel chips   | 3.7 to 3.15 |        9 |
| Windows              | 3.7 to 3.15 |        9 |

*There is no Python 3.7 for Apple silicon. Maybe it is time to consider
updating if you are still using Python 3.7.

# What It Needs

**cutienator** compiles its own bridge to Qt on your machine, so it
needs what a build needs: Qt 6.12 with its program `qmake6`, and the
compiler `clang++`. On Windows that is the Qt built with Visual Studio,
and the `clang++` that comes with Visual Studio.

Both programs are found by name, so their folders have to be in `PATH`.
On Windows the `clang++` of Visual Studio lies in `VC\Tools\Llvm\x64\bin`
of the Visual Studio folder, and that folder has to come first.
