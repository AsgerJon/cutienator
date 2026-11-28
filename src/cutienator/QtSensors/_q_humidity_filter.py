"""
QHumidityFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qhumiditysensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSensorFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QHumidityReading, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHumidityReading = WAIT['QHumidityReading']
  QSensorReading = WAIT['QSensorReading']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHumidityFilter(QSensorFilter):
  """
  The cute side of Qt's QHumidityFilter: a plain Python object standing in
  front of one C++ QHumidityFilter.

  It is built on the cute 'QSensorFilter', as Qt's QHumidityFilter is built
  on Qt's QSensorFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHumidityFilter that has a ritual and that Python
  can call so far, 1 name in all: 'filter'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QHumidityFilter is created at the first use, not by
    'QHumidityFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHumidityFilter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHumidityFilter'

  #  The functions Qt calls itself that QHumidityFilter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'filter': (
          ('_ZN15QHumidityFilter6filterEP16QHumidityReading',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSensors:QHumidityReading'),
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

  @overload(QHumidityReading)
  @overload(NoneType)
  def filter(self, reading: Optional[QHumidityReading]) -> bool:
    """
    Calls Qt's 'bool QHumidityFilter::filter(QHumidityReading *reading)'.

    Qt's own words: https://doc.qt.io/qt-6/qhumidityfilter.html#filter

    Parameters
    ----------

    reading : Optional[QHumidityReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHumidityFilter::filter(QHumidityReading *reading)
    return self.uglySide.call(
        'ritual_ZN15QHumidityFilter6filterEP16QHumidityReading',
        self._addressOf(reading),
    )

  @overload(QSensorReading)
  def filter(self, reading: Optional[QSensorReading]) -> bool:
    """
    Calls Qt's 'bool QHumidityFilter::filter(QSensorReading *reading)'.

    Qt's own words: https://doc.qt.io/qt-6/qhumidityfilter.html#filter

    Parameters
    ----------

    reading : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHumidityFilter::filter(QSensorReading *reading)
    ritual = 'ritual_ZN15QHumidityFilter6filterEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QHumidityFilter6filterEP14QSensorReading'
    return self.uglySide.call(ritual, self._addressOf(reading))
