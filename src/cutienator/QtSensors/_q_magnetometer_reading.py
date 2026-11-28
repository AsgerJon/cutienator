"""
QMagnetometerReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qmagnetometer.h, Qt 6.12.0. Changes made here are lost.
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


class QMagnetometerReading(QSensorReading):
  """
  The cute side of Qt's QMagnetometerReading: a plain Python object standing
  in front of one C++ QMagnetometerReading.

  It is built on the cute 'QSensorReading', as Qt's QMagnetometerReading is
  built on Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMagnetometerReading that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr',
  'copyValuesFrom', 'x', 'setX', 'y', 'setY', 'z', 'setZ',
  'calibrationLevel', 'setCalibrationLevel'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMagnetometerReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QMagnetometerReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QMagnetometerReading::~QMagnetometerReading()': the destructor:
    Python never removes a C++ QMagnetometerReading.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QMagnetometerReading is created at the first use, not by
    'QMagnetometerReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMagnetometerReading.
  - Qt tells when it has removed the C++ QMagnetometerReading. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QMagnetometerReading::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#tr

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
    #  QString QMagnetometerReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QMagnetometerReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMagnetometerReading'

  #  A C++ QMagnetometerReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMagnetometerReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMagnetometerReading::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometerreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMagnetometerReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QMagnetometerReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QMagnetometerReading::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#x
    """
    #  qreal QMagnetometerReading::x() const
    return self.uglySide.call('ritual_ZNK20QMagnetometerReading1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QMagnetometerReading::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#y
    """
    #  qreal QMagnetometerReading::y() const
    return self.uglySide.call('ritual_ZNK20QMagnetometerReading1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QMagnetometerReading::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#z
    """
    #  qreal QMagnetometerReading::z() const
    return self.uglySide.call('ritual_ZNK20QMagnetometerReading1zEv')

  def calibrationLevel(self) -> float:
    """
    Calls Qt's 'qreal QMagnetometerReading::calibrationLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometerreading.html#calibrationLevel
    """
    #  qreal QMagnetometerReading::calibrationLevel() const
    return self.uglySide.call(
        'ritual_ZNK20QMagnetometerReading16calibrationLevelEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QMagnetometerReading::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QMagnetometerReading::setX(qreal x)
    self.uglySide.call('ritual_ZN20QMagnetometerReading4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QMagnetometerReading::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QMagnetometerReading::setY(qreal y)
    self.uglySide.call('ritual_ZN20QMagnetometerReading4setYEd', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QMagnetometerReading::setZ(qreal z)'.

    Qt's own words: https://doc.qt.io/qt-6/qmagnetometerreading.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QMagnetometerReading::setZ(qreal z)
    self.uglySide.call('ritual_ZN20QMagnetometerReading4setZEd', z)

  @overload(float)
  def setCalibrationLevel(self, calibrationLevel: float) -> None:
    """
    Calls Qt's 'void QMagnetometerReading::setCalibrationLevel(qreal
    calibrationLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometerreading.html#setCalibrationLevel

    Parameters
    ----------

    calibrationLevel : float
      Passed on as it is.
    """
    #  void QMagnetometerReading::setCalibrationLevel(qreal calibrationLevel)
    self.uglySide.call(
        'ritual_ZN20QMagnetometerReading19setCalibrationLevelEd',
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
    Notes what was given, for Qt's
    'QMagnetometerReading::QMagnetometerReading(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometerreading.html#QMagnetometerReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMagnetometerReading::QMagnetometerReading(QObject *parent)
    self._noteCreation(QMagnetometerReading, lambda: Rituals.call(
        'ritual_ZN20QMagnetometerReadingC1EP7QObject',
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
    Calls Qt's 'void QMagnetometerReading::copyValuesFrom(QSensorReading
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmagnetometerreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMagnetometerReading::copyValuesFrom(QSensorReading *other)
    ritual = (
        'ritual_ZN20QMagnetometerReading14copyValuesFromEP14QSensorReading')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QMagnetometerReading14copyValuesFromEP14QSensorRe'
          'ading')
    self.uglySide.call(ritual, self._addressOf(other))
