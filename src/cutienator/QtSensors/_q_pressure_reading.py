"""
QPressureReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qpressuresensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPressureReading(QSensorReading):
  """
  The cute side of Qt's QPressureReading: a plain Python object standing in
  front of one C++ QPressureReading.

  It is built on the cute 'QSensorReading', as Qt's QPressureReading is built
  on Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPressureReading that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'copyValuesFrom',
  'pressure', 'setPressure', 'temperature', 'setTemperature'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPressureReading::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPressureReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPressureReading::~QPressureReading()': the destructor: Python
    never removes a C++ QPressureReading.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPressureReading is created at the first use, not by
    'QPressureReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPressureReading.
  - Qt tells when it has removed the C++ QPressureReading. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPressureReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpressurereading.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPressureReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPressureReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPressureReading'

  #  A C++ QPressureReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPressureReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPressureReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpressurereading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPressureReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPressureReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pressure(self) -> float:
    """
    Calls Qt's 'qreal QPressureReading::pressure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpressurereading.html#pressure
    """
    #  qreal QPressureReading::pressure() const
    return self.uglySide.call('ritual_ZNK16QPressureReading8pressureEv')

  def temperature(self) -> float:
    """
    Calls Qt's 'qreal QPressureReading::temperature() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpressurereading.html#temperature
    """
    #  qreal QPressureReading::temperature() const
    return self.uglySide.call('ritual_ZNK16QPressureReading11temperatureEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPressure(self, pressure: float) -> None:
    """
    Calls Qt's 'void QPressureReading::setPressure(qreal pressure)'.

    Qt's own words: https://doc.qt.io/qt-6/qpressurereading.html#setPressure

    Parameters
    ----------

    pressure : float
      Passed on as it is.
    """
    #  void QPressureReading::setPressure(qreal pressure)
    self.uglySide.call(
        'ritual_ZN16QPressureReading11setPressureEd', pressure,
    )

  @overload(float)
  def setTemperature(self, temperature: float) -> None:
    """
    Calls Qt's 'void QPressureReading::setTemperature(qreal temperature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpressurereading.html#setTemperature

    Parameters
    ----------

    temperature : float
      Passed on as it is.
    """
    #  void QPressureReading::setTemperature(qreal temperature)
    self.uglySide.call(
        'ritual_ZN16QPressureReading14setTemperatureEd', temperature,
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPressureReading::QPressureReading(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpressurereading.html#QPressureReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPressureReading::QPressureReading(QObject *parent)
    self._noteCreation(QPressureReading, lambda: Rituals.call(
        'ritual_ZN16QPressureReadingC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
  def copyValuesFrom(self, other: Optional[QSensorReading]) -> None:
    """
    Calls Qt's 'void QPressureReading::copyValuesFrom(QSensorReading
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpressurereading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPressureReading::copyValuesFrom(QSensorReading *other)
    ritual = 'ritual_ZN16QPressureReading14copyValuesFromEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QPressureReading14copyValuesFromEP14QSensorReadin'
          'g')
    self.uglySide.call(ritual, self._addressOf(other))
