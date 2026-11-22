[![Tokens](https://img.shields.io/badge/Tokens-0-D97757)](https://claude.com/claude-code)
[![PyPI version](https://img.shields.io/pypi/v/cutienator)](https://pypi.org/project/cutienator/)
[![Python versions](https://img.shields.io/pypi/pyversions/cutienator)](https://pypi.org/project/cutienator/)
[![Systems](https://img.shields.io/badge/Systems-Linux_%7C_macOS_%7C_Windows-informational)](#where-it-runs)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# cutienator v0.0.1-dev2 (development build)
A vastly superior binding of Qt C++ to Python. 

# I Survived 1000 Classes in Qt!

Qt is big. Its parts QtCore, QtGui and QtWidgets alone hold 770 classes,
and the classes name each other all over: `QWidget` takes a `QFont`, a
`QIcon`, a `QPalette`, a `QLayout` and eighteen classes more.

In **cutienator** a class of Qt is a plain Python class in a file of its
own, and each of its functions is Python you can read, with its
`@overload` lines. That is the point of it, and it has a price: Python
has to run the file of a class before the class exists, about a
hundredth of a second for each. Running them all would keep a program
waiting for seconds before its first line.

So **cutienator** runs as few of them as it can: **a program pays for
the classes it uses, and for no others.** It gets there in three steps.

## 1. A class is brought in when it is asked for

```python
from cutienator.QtWidgets import QWidget
```

This brings in the file of `QWidget`. It does not bring in QtWidgets.
The package of each part only knows in which file each of its classes
is, and fetches a class the first time it is asked for.

## 2. A file brings in only what its class is built on

`QWidget` is built on `QObject` and `QPaintDevice`, as in C++, so the
file of `QWidget` brings in the files of those two. It asks for them the
way your program would, with `from ..QtCore import Qt, QObject`, and the
package fetches the one file each is in, so nothing comes along that was
not needed.

An enum is written inside its class, as in C++: `QPalette.ColorRole` is
a class in the body of `QPalette`, and has no other name. So a file
also brings in the few classes that hold an enum it names, as `QWidget`
brings in `QPalette` for `setBackgroundRole`. For `QWidget` that makes
seven files in all.

## 3. Every other class waits

`QWidget.setFont` takes a `QFont`, and `QWidget` is not built on
`QFont`. In C++ the header of `QWidget` gets by with one line,
`class QFont;`, which says that a class of that name is coming.
**cutienator** has the same line. It is called `WAIT`:

```python
if TYPE_CHECKING:
  from ..QtGui import QFont    # for your editor
else:
  QFont = WAIT['QFont']        # for Python, when it runs


class QWidget(QObject):

  @overload(QFont)
  def setFont(self, a0: QFont) -> None:
    ...
```

The file of `QFont` is not brought in. The signature `(QFont)` waits,
and `QWidget` is made without it. The moment the class `QFont` is made,
whoever brings it in, the signature is put back where it was written,
on `QWidget` and on every class built on `QWidget` so far.

## Why nothing is lost by waiting

A signature that takes a `QFont` only matters to a call that hands over
a `QFont`. For such a call there has to be an object of `QFont`, and an
object of `QFont` cannot be before the class `QFont` is.

- Your program makes one, as `QFont('Arial')`. For that it has brought
  in `QFont`.
- Qt hands one back, as `widget.font()` does. A function that gives a
  class its file did not bring in brings in the file of that class
  itself, before it makes the object.

Either way the class `QFont` is made first, and putting the waiting
signatures back is the last part of making it. No object of `QFont`
exists before every function that waited for `QFont` takes one. So a
call never meets a signature that is still waiting for what the call
hands over.

## What You Will Notice

Mostly nothing. Bring in what you use, as with any binding. Four things
are different from a binding that loads everything at once:

- **A function whose every signature waits takes no call yet.**
  `QWidget.setFont` is on the class from the start, but until `QFont`
  is brought in it refuses every call with `DispatchException`. To call
  it you need a `QFont`, and by then it takes one.
- **A class changes when a class it waited for comes in.** The function
  is built again with the signature that came back. A function you read
  off an object earlier and kept, as `kept = widget.setFont`, still
  goes by what the function was when you read it.
- **A class that is waited for is known by its name.** A class of your
  own that is built on a class of **cutienator** must not have the name
  of a class of Qt, as `QFont` or `Connection`. Any other name is fine.
- **A class holds the classes it waited for.** Once `QFont` is brought
  in, `QWidget.QFont` is `QFont`.

Your editor and your type checker see none of this. They read the
branch under `if TYPE_CHECKING:`, where every class is the real one.

## What It Buys

Measured on one Linux machine with Python 3.15 and Qt 6.12, each line
in a Python of its own, the best of five:

| A program that brings in      | everything at once | with the three steps |
|-------------------------------|-------------------:|---------------------:|
| `QWidget`                     |          about 4 s |               0.24 s |
| a window, shown and closed    |          about 4 s |               0.46 s |
| 78 classes, a large program   |          about 4 s |               0.95 s |
| all 694 classes there are yet |          about 4 s |               4.27 s |

Without the three steps every program would bring in every class,
whatever it uses, so the first column is the last line for all of them.
The last line is also the price: a program that really uses every class
pays a little more than it would at once, since each class that comes
in late has its signatures put back. When there were 190 classes, that
was 2.32 s against 2.17 s.

The whole story of a waiting class is in the docstring of
`cutienator.cute.WAIT`.

# Overriding: Qt Calls What You Wrote

Qt calls some of its functions itself: `paintEvent` when a widget has
to be drawn, `sizeHint` when a layout wants to know how big a widget
would like to be, `event` for everything that happens to an object. A
class of your program writes such a function anew, and Qt calls yours:

```python
from cutienator.QtGui import QColor, QPainter, QPaintEvent
from cutienator.QtWidgets import QWidget


class Canvas(QWidget):

  def paintEvent(self, event: QPaintEvent) -> None:
    painter = QPainter(self)
    painter.fillRect(0, 0, self.width(), self.height(), QColor(255, 0, 0))
    painter.end()
```

`super().paintEvent(event)` runs Qt's own function, as you would expect.

## How Qt gets to Python

Every object your program makes is of a C++ class of ours, built on the
class of Qt: a `Canvas` stands in front of a `CuteQWidget`, which is a
`QWidget`. In that class each function Qt calls itself asks Python
first, when Python has handed it a function, and runs Qt's own
otherwise.

**Only the functions your class wrote are handed over**, when the object
is made. A plain `QWidget` hands over nothing, and Qt runs as if Python
were not there.

## What You Will Notice

- **An exception is not swallowed.** What your `paintEvent` raises
  cannot travel up through C++, so it is kept, Qt's loop of events is
  told to stop, and it is raised from the function of Qt your program
  was in: `app.exec()`, or `widget.grab()`. While it is kept, Qt asks
  Python nothing more.
- **Keep what Qt still uses.** After `layout.addItem(MySpacer(10, 10))`
  your program holds the spacer no more, and Qt still does. When Qt then
  calls a function `MySpacer` wrote, that raises `RuntimeError`, naming
  the function and the class. Qt's own function is not run in its place,
  which would hide the mistake. Keep the object, as an attribute of the
  window it is in.
- **Give what Qt's function gives.** `None` where Qt's function gives a
  `bool`, or a number where it gives text, raises `TypeError`.
- **Some functions cannot be handed to Python yet.** Of the 711 names of
  functions Qt calls itself in the classes there are so far, 639 can.
  The others take or give a list or a map, change a text in place, or
  read raw memory, as `QValidator.validate` and `QIODevice.readData`. A
  class that writes one of those anew is refused with
  `NotImplementedError` as soon as an object of it is used, naming the
  function. Qt would otherwise go on calling its own, without a word.
- **A class Qt has no code for in some function cannot be built on
  yet**, as `QAbstractListModel`, which leaves `rowCount` and `data` to
  your program.

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
