"""
QAccelerometerFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qaccelerometer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSensorFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAccelerometerReading, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccelerometerReading = WAIT['QAccelerometerReading']
  QSensorReading = WAIT['QSensorReading']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccelerometerFilter(QSensorFilter):
  """
  The cute side of Qt's QAccelerometerFilter: a plain Python object standing
  in front of one C++ QAccelerometerFilter.

  It is built on the cute 'QSensorFilter', as Qt's QAccelerometerFilter is
  built on Qt's QSensorFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccelerometerFilter that has a ritual and that
  Python can call so far, 1 name in all: 'filter'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QAccelerometerFilter is created at the first use, not by
    'QAccelerometerFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccelerometerFilter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccelerometerFilter'

  #  The functions Qt calls itself that QAccelerometerFilter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'filter': (
          ('_ZN20QAccelerometerFilter6filterEP21QAccelerometerReading',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSensors:QAccelerometerReading'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccelerometerReading)
  @overload(NoneType)
  def filter(self, reading: Optional[QAccelerometerReading]) -> bool:
    """
    Calls Qt's 'bool QAccelerometerFilter::filter(QAccelerometerReading
    *reading)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerfilter.html#filter

    Parameters
    ----------

    reading : Optional[QAccelerometerReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccelerometerFilter::filter(QAccelerometerReading *reading)
    return self.uglySide.call(
        'ritual_ZN20QAccelerometerFilter6filterEP21QAccelerometerReading',
        self._addressOf(reading),
    )

  @overload(QSensorReading)
  def filter(self, reading: Optional[QSensorReading]) -> bool:
    """
    Calls Qt's 'bool QAccelerometerFilter::filter(QSensorReading *reading)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerfilter.html#filter

    Parameters
    ----------

    reading : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccelerometerFilter::filter(QSensorReading *reading)
    ritual = 'ritual_ZN20QAccelerometerFilter6filterEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QAccelerometerFilter6filterEP14QSensorReading'
    return self.uglySide.call(ritual, self._addressOf(reading))
