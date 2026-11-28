"""
QAccelerometerReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qaccelerometer.h, Qt 6.12.0. Changes made here are lost.
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


class QAccelerometerReading(QSensorReading):
  """
  The cute side of Qt's QAccelerometerReading: a plain Python object standing
  in front of one C++ QAccelerometerReading.

  It is built on the cute 'QSensorReading', as Qt's QAccelerometerReading is
  built on Qt's QSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccelerometerReading that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'copyValuesFrom', 'x', 'setX', 'y', 'setY', 'z', 'setZ'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAccelerometerReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAccelerometerReading::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAccelerometerReading::~QAccelerometerReading()': the destructor:
    Python never removes a C++ QAccelerometerReading.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAccelerometerReading is created at the first use, not by
    'QAccelerometerReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccelerometerReading.
  - Qt tells when it has removed the C++ QAccelerometerReading. Every call on
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
    Calls Qt's 'QString QAccelerometerReading::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#tr

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
    #  QString QAccelerometerReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QAccelerometerReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccelerometerReading'

  #  A C++ QAccelerometerReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccelerometerReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAccelerometerReading::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccelerometerreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAccelerometerReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QAccelerometerReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QAccelerometerReading::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#x
    """
    #  qreal QAccelerometerReading::x() const
    return self.uglySide.call('ritual_ZNK21QAccelerometerReading1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QAccelerometerReading::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#y
    """
    #  qreal QAccelerometerReading::y() const
    return self.uglySide.call('ritual_ZNK21QAccelerometerReading1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QAccelerometerReading::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#z
    """
    #  qreal QAccelerometerReading::z() const
    return self.uglySide.call('ritual_ZNK21QAccelerometerReading1zEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QAccelerometerReading::setX(qreal x)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QAccelerometerReading::setX(qreal x)
    self.uglySide.call('ritual_ZN21QAccelerometerReading4setXEd', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QAccelerometerReading::setY(qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QAccelerometerReading::setY(qreal y)
    self.uglySide.call('ritual_ZN21QAccelerometerReading4setYEd', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QAccelerometerReading::setZ(qreal z)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometerreading.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QAccelerometerReading::setZ(qreal z)
    self.uglySide.call('ritual_ZN21QAccelerometerReading4setZEd', z)

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
    'QAccelerometerReading::QAccelerometerReading(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccelerometerreading.html#QAccelerometerReading

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAccelerometerReading::QAccelerometerReading(QObject *parent)
    self._noteCreation(QAccelerometerReading, lambda: Rituals.call(
        'ritual_ZN21QAccelerometerReadingC1EP7QObject',
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
    Calls Qt's 'void QAccelerometerReading::copyValuesFrom(QSensorReading
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccelerometerreading.html#copyValuesFrom

    Parameters
    ----------

    other : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccelerometerReading::copyValuesFrom(QSensorReading *other)
    ritual = (
        'ritual_ZN21QAccelerometerReading14copyValuesFromEP14QSensorReading')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QAccelerometerReading14copyValuesFromEP14QSensorR'
          'eading')
    self.uglySide.call(ritual, self._addressOf(other))
