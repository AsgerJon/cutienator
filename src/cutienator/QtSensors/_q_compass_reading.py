"""
QCompassReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qcompass.h, Qt 6.12.0. Changes made here are lost.
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


class QCompassReading(QSensorReading):
  """
  The cute side of Qt's QCompassReading: a plain Python object standing in
  front of one C++ QCompassReading.

  It is built on the cute 'QSensorReading', as Qt's QCompassReading is built
  on Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCompassReading that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'copyValuesFrom',
  'azimuth', 'setAzimuth', 'calibrationLevel', 'setCalibrationLevel'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCompassReading::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCompassReading::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCompassReading::~QCompassReading()': the destructor: Python never
    removes a C++ QCompassReading.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCompassReading is created at the first use, not by
    'QCompassReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCompassReading.
  - Qt tells when it has removed the C++ QCompassReading. Every call on the
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
    Calls Qt's 'QString QCompassReading::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompassreading.html#tr

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
    #  QString QCompassReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QCompassReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCompassReading'

  #  A C++ QCompassReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCompassReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCompassReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompassreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCompassReading::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QCompassReading10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def azimuth(self) -> float:
    """
    Calls Qt's 'qreal QCompassReading::azimuth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompassreading.html#azimuth
    """
    #  qreal QCompassReading::azimuth() const
    return self.uglySide.call('ritual_ZNK15QCompassReading7azimuthEv')

  def calibrationLevel(self) -> float:
    """
    Calls Qt's 'qreal QCompassReading::calibrationLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompassreading.html#calibrationLevel
    """
    #  qreal QCompassReading::calibrationLevel() const
    return self.uglySide.call(
        'ritual_ZNK15QCompassReading16calibrationLevelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAzimuth(self, azimuth: float) -> None:
    """
    Calls Qt's 'void QCompassReading::setAzimuth(qreal azimuth)'.

    Qt's own words: https://doc.qt.io/qt-6/qcompassreading.html#setAzimuth

    Parameters
    ----------

    azimuth : float
      Passed on as it is.
    """
    #  void QCompassReading::setAzimuth(qreal azimuth)
    self.uglySide.call('ritual_ZN15QCompassReading10setAzimuthEd', azimuth)

  @overload(float)
  def setCalibrationLevel(self, calibrationLevel: float) -> None:
    """
    Calls Qt's 'void QCompassReading::setCalibrationLevel(qreal
    calibrationLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompassreading.html#setCalibrationLevel

    Parameters
    ----------

    calibrationLevel : float
      Passed on as it is.
    """
    #  void QCompassReading::setCalibrationLevel(qreal calibrationLevel)
    self.uglySide.call(
        'ritual_ZN15QCompassReading19setCalibrationLevelEd',
        calibrationLevel,
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
    Notes what was given, for Qt's 'QCompassReading::QCompassReading(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompassreading.html#QCompassReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCompassReading::QCompassReading(QObject *parent)
    self._noteCreation(QCompassReading, lambda: Rituals.call(
        'ritual_ZN15QCompassReadingC1EP7QObject',
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
    Calls Qt's 'void QCompassReading::copyValuesFrom(QSensorReading *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompassreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCompassReading::copyValuesFrom(QSensorReading *other)
    ritual = 'ritual_ZN15QCompassReading14copyValuesFromEP14QSensorReading'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QCompassReading14copyValuesFromEP14QSensorReading')
    self.uglySide.call(ritual, self._addressOf(other))
