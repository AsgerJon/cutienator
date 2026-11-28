"""
QAccelerometer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qaccelerometer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAccelerometerPrivate, QAccelerometerReading

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccelerometer(QSensor):
  """
  The cute side of Qt's QAccelerometer: a plain Python object standing in
  front of one C++ QAccelerometer.

  It is built on the cute 'QSensor', as Qt's QAccelerometer is built on Qt's
  QSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccelerometer that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'accelerationMode',
  'setAccelerationMode', 'reading', 'accelerationModeChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAccelerometer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAccelerometer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAccelerometer::~QAccelerometer()': the destructor: Python never
    removes a C++ QAccelerometer.
  - Qt's 'const QAccelerometerPrivate *QAccelerometer::d_func() const': takes
    in Python what 'QAccelerometerPrivate *QAccelerometer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAccelerometer is created at the first use, not by
    'QAccelerometer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccelerometer.
  - Qt tells when it has removed the C++ QAccelerometer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAccelerometer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AccelerationMode(CuteNum):
    """
    The enum 'QAccelerometer::AccelerationMode' of Qt, with the 3 names Qt
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
    Calls Qt's 'QString QAccelerometer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometer.html#tr

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
    #  QString QAccelerometer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QAccelerometer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccelerometer'

  #  A C++ QAccelerometer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccelerometer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAccelerometer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAccelerometer::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QAccelerometer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def accelerationMode(self) -> AccelerationMode:
    """
    Calls Qt's 'AccelerationMode QAccelerometer::accelerationMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccelerometer.html#accelerationMode

    Returns
    -------

    AccelerationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AccelerationMode(number)'
      gives.
    """
    #  AccelerationMode QAccelerometer::accelerationMode() const
    return QAccelerometer.AccelerationMode(self.uglySide.call(
        'ritual_ZNK14QAccelerometer16accelerationModeEv',
    ))

  def reading(self) -> Optional[QAccelerometerReading]:
    """
    Calls Qt's 'QAccelerometerReading *QAccelerometer::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometer.html#reading

    Returns
    -------

    Optional[QAccelerometerReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccelerometerReading *QAccelerometer::reading() const
    address = self.uglySide.call('ritual_ZNK14QAccelerometer7readingEv')
    from . import QAccelerometerReading
    return QAccelerometerReading._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AccelerationMode)
  def setAccelerationMode(self, accelerationMode: AccelerationMode) -> None:
    """
    Calls Qt's 'void QAccelerometer::setAccelerationMode(AccelerationMode
    accelerationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccelerometer.html#setAccelerationMode

    Parameters
    ----------

    accelerationMode : AccelerationMode
      Passed on as its number.
    """
    #  void QAccelerometer::setAccelerationMode(AccelerationMode
    #      accelerationMode)
    self.uglySide.call(
        'ritual_ZN14QAccelerometer19setAccelerationModeENS_16AccelerationMo'
        'deE',
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
    Notes what was given, for Qt's 'QAccelerometer::QAccelerometer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometer.html#QAccelerometer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAccelerometer::QAccelerometer(QObject *parent)
    self._noteCreation(QAccelerometer, lambda: Rituals.call(
        'ritual_ZN14QAccelerometerC1EP7QObject',
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
    Calls Qt's 'void QAccelerometer::accelerationModeChanged(AccelerationMode
    accelerationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccelerometer.html#accelerationModeChanged

    Parameters
    ----------

    accelerationMode : AccelerationMode
      Passed on as its number.
    """
    #  void QAccelerometer::accelerationModeChanged(AccelerationMode
    #      accelerationMode)
    self.uglySide.call(
        'ritual_ZN14QAccelerometer23accelerationModeChangedENS_16Accelerati'
        'onModeE',
        accelerationMode.value,
    )

  def d_func(self) -> Optional[QAccelerometerPrivate]:
    """
    Calls Qt's 'QAccelerometerPrivate *QAccelerometer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccelerometer.html#d_func

    Returns
    -------

    Optional[QAccelerometerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccelerometerPrivate *QAccelerometer::d_func()
    address = self.uglySide.call('ritual_ZN14QAccelerometer6d_funcEv')
    from . import QAccelerometerPrivate
    return QAccelerometerPrivate._cuteAt(address)
