"""
QAmbientTemperatureReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qambienttemperaturesensor.h, Qt 6.12.0. Changes made here are
#  lost.
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


class QAmbientTemperatureReading(QSensorReading):
  """
  The cute side of Qt's QAmbientTemperatureReading: a plain Python object
  standing in front of one C++ QAmbientTemperatureReading.

  It is built on the cute 'QSensorReading', as Qt's
  QAmbientTemperatureReading is built on Qt's QSensorReading, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAmbientTemperatureReading that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'copyValuesFrom', 'temperature', 'setTemperature'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAmbientTemperatureReading::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAmbientTemperatureReading::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAmbientTemperatureReading::~QAmbientTemperatureReading()': the
    destructor: Python never removes a C++ QAmbientTemperatureReading.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAmbientTemperatureReading is created at the first use, not by
    'QAmbientTemperatureReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAmbientTemperatureReading.
  - Qt tells when it has removed the C++ QAmbientTemperatureReading. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QAmbientTemperatureReading::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qambienttemperaturereading.html#tr

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
    #  QString QAmbientTemperatureReading::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QAmbientTemperatureReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAmbientTemperatureReading'

  #  A C++ QAmbientTemperatureReading Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAmbientTemperatureReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAmbientTemperatureReading::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambienttemperaturereading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAmbientTemperatureReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QAmbientTemperatureReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def temperature(self) -> float:
    """
    Calls Qt's 'qreal QAmbientTemperatureReading::temperature() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambienttemperaturereading.html#temperature
    """
    #  qreal QAmbientTemperatureReading::temperature() const
    return self.uglySide.call(
        'ritual_ZNK26QAmbientTemperatureReading11temperatureEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTemperature(self, temperature: float) -> None:
    """
    Calls Qt's 'void QAmbientTemperatureReading::setTemperature(qreal
    temperature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambienttemperaturereading.html#setTemperature

    Parameters
    ----------

    temperature : float
      Passed on as it is.
    """
    #  void QAmbientTemperatureReading::setTemperature(qreal temperature)
    self.uglySide.call(
        'ritual_ZN26QAmbientTemperatureReading14setTemperatureEd',
        temperature,
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
    'QAmbientTemperatureReading::QAmbientTemperatureReading(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qambienttemperaturereading.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAmbientTemperatureReading::QAmbientTemperatureReading(QObject
    #      *parent)
    self._noteCreation(QAmbientTemperatureReading, lambda: Rituals.call(
        'ritual_ZN26QAmbientTemperatureReadingC1EP7QObject',
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
    Calls Qt's 'void
    QAmbientTemperatureReading::copyValuesFrom(QSensorReading *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambienttemperaturereading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAmbientTemperatureReading::copyValuesFrom(QSensorReading *other)
    ritual = (
        'ritual_ZN26QAmbientTemperatureReading14copyValuesFromEP14QSensorRe'
        'ading')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAmbientTemperatureReading14copyValuesFromEP14QSe'
          'nsorReading')
    self.uglySide.call(ritual, self._addressOf(other))
