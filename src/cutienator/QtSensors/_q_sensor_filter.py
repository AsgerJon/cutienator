"""
QSensorFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSensor, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSensor = WAIT['QSensor']
  QSensorReading = WAIT['QSensorReading']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSensorFilter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSensorFilter: a plain Python object standing in
  front of one C++ QSensorFilter.

  What exists
  -----------

  Every function of Qt's QSensorFilter that has a ritual and that Python can
  call so far, 2 names in all: 'filter', 'setSensor'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSensorFilter::~QSensorFilter()': the destructor: Python never
    removes a C++ QSensorFilter.

  What to expect
  --------------

  - The C++ QSensorFilter is created at the first use, not by
    'QSensorFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSensorFilter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSensorFilter'

  #  A C++ QSensorFilter Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSensorFilter'

  #  The functions Qt calls itself that QSensorFilter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'filter': (
          ('_ZN13QSensorFilter6filterEP14QSensorReading',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSensors:QSensorReading'),
           )),
      ),
      'setSensor': (
          ('_ZN13QSensorFilter9setSensorEP7QSensor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtSensors:QSensor'),
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

  @overload(QSensor)
  @overload(NoneType)
  def setSensor(self, sensor: Optional[QSensor]) -> None:
    """
    Calls Qt's 'void QSensorFilter::setSensor(QSensor *sensor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorfilter.html#setSensor

    Parameters
    ----------

    sensor : Optional[QSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensorFilter::setSensor(QSensor *sensor)
    ritual = 'ritual_ZN13QSensorFilter9setSensorEP7QSensor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QSensorFilter9setSensorEP7QSensor'
    self.uglySide.call(ritual, self._addressOf(sensor))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSensorFilter::QSensorFilter()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsensorfilter.html#QSensorFilter
    """
    #  QSensorFilter::QSensorFilter()
    self._noteCreation(QSensorFilter, lambda: Rituals.call(
        'ritual_ZN13QSensorFilterC1Ev',
    ))

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

  @overload(QSensorReading)
  @overload(NoneType)
  def filter(self, reading: Optional[QSensorReading]) -> bool:
    """
    Calls Qt's 'bool QSensorFilter::filter(QSensorReading *reading)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorfilter.html#filter

    Parameters
    ----------

    reading : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSensorFilter::filter(QSensorReading *reading)
    return self.uglySide.call(
        'ritual_ZN13QSensorFilter6filterEP14QSensorReading',
        self._addressOf(reading),
    )


#  Qt's 'QList<QSensorFilter *>': the list of QSensorFilter, which
#  'QList[QSensorFilter]' gives. It is made here, so that there is one as
#  soon as there can be a QSensorFilter. Qt has a name of its own for it.
QFilterList = QList.createKind(
    QSensorFilter, 'address',
    name='QFilterList',
    make='ritual_list_make_QSensorFilter_ptr',
    add='ritual_list_add_QSensorFilter_ptr',
    size='ritual_list_size_QSensorFilter_ptr',
    at='ritual_list_at_QSensorFilter_ptr',
    drop='ritual_list_drop_QSensorFilter_ptr',
)
