"""
QmlAccelerometer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlaccelerometer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlAccelerometer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QmlSensor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QSensor
  from . import QmlSensorReading

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlAccelerometer(QmlSensor):
  """
  The cute side of Qt's QmlAccelerometer: a plain Python object standing in
  front of one C++ QmlAccelerometer.

  It is built on the cute 'QmlSensor', as Qt's QmlAccelerometer is built on
  Qt's QmlSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlAccelerometer that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'accelerationMode',
  'setAccelerationMode', 'sensor', 'accelerationModeChanged',
  'createReading'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlAccelerometer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QmlAccelerometer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QmlAccelerometer::~QmlAccelerometer()': the destructor: Python
    never removes a C++ QmlAccelerometer.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlAccelerometer is created at the first use, not by
    'QmlAccelerometer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlAccelerometer.
  - Qt tells when it has removed the C++ QmlAccelerometer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QmlAccelerometer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AccelerationMode(CuteNum):
    """
    The enum 'QmlAccelerometer::AccelerationMode' of Qt, with the 3 names Qt
    gives in it.
    """

    Combined = Kee[int](0)
    Gravity = Kee[int](1)
    User = Kee[int](2)

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
    Calls Qt's 'QString QmlAccelerometer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometer.html#tr

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
    #  QString QmlAccelerometer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QmlAccelerometer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlAccelerometer'

  #  A C++ QmlAccelerometer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlAccelerometer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlAccelerometer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlAccelerometer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QmlAccelerometer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def accelerationMode(self) -> AccelerationMode:
    """
    Calls Qt's 'AccelerationMode QmlAccelerometer::accelerationMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometer.html#accelerationMode

    Returns
    -------

    AccelerationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AccelerationMode(number)'
      gives.
    """
    #  AccelerationMode QmlAccelerometer::accelerationMode() const
    return QmlAccelerometer.AccelerationMode(self.uglySide.call(
        'ritual_ZNK16QmlAccelerometer16accelerationModeEv',
    ))

  def sensor(self) -> Optional[QSensor]:
    """
    Calls Qt's 'QSensor *QmlAccelerometer::sensor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometer.html#sensor

    Returns
    -------

    Optional[QSensor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensor *QmlAccelerometer::sensor() const
    ritual = 'ritual_ZNK16QmlAccelerometer6sensorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QmlAccelerometer6sensorEv'
    address = self.uglySide.call(ritual)
    from ..QtSensors import QSensor
    return QSensor._cuteAt(address)

  def createReading(self) -> Optional[QmlSensorReading]:
    """
    Calls Qt's 'QmlSensorReading *QmlAccelerometer::createReading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometer.html#createReading

    Returns
    -------

    Optional[QmlSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlSensorReading *QmlAccelerometer::createReading() const
    ritual = 'ritual_ZNK16QmlAccelerometer13createReadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QmlAccelerometer13createReadingEv'
    address = self.uglySide.call(ritual)
    from . import QmlSensorReading
    return QmlSensorReading._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AccelerationMode)
  def setAccelerationMode(self, accelerationMode: AccelerationMode) -> None:
    """
    Calls Qt's 'void QmlAccelerometer::setAccelerationMode(AccelerationMode
    accelerationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometer.html#setAccelerationMode

    Parameters
    ----------

    accelerationMode : AccelerationMode
      Passed on as its number.
    """
    #  void QmlAccelerometer::setAccelerationMode(AccelerationMode
    #      accelerationMode)
    self.uglySide.call(
        'ritual_ZN16QmlAccelerometer19setAccelerationModeENS_16Acceleration'
        'ModeE',
        accelerationMode.value,
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
    'QmlAccelerometer::QmlAccelerometer(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometer.html#QmlAccelerometer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlAccelerometer::QmlAccelerometer(QObject *parent)
    self._noteCreation(QmlAccelerometer, lambda: Rituals.call(
        'ritual_ZN16QmlAccelerometerC1EP7QObject',
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

  @overload(AccelerationMode)
  def accelerationModeChanged(
      self,
      accelerationMode: AccelerationMode,
  ) -> None:
    """
    Calls Qt's 'void
    QmlAccelerometer::accelerationModeChanged(AccelerationMode
    accelerationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometer.html#accelerationModeChanged

    Parameters
    ----------

    accelerationMode : AccelerationMode
      Passed on as its number.
    """
    #  void QmlAccelerometer::accelerationModeChanged(AccelerationMode
    #      accelerationMode)
    self.uglySide.call(
        'ritual_ZN16QmlAccelerometer23accelerationModeChangedENS_16Accelera'
        'tionModeE',
        accelerationMode.value,
    )
