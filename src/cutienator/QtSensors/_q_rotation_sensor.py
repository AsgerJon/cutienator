"""
QRotationSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qrotationsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QRotationReading, QRotationSensorPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRotationSensor(QSensor):
  """
  The cute side of Qt's QRotationSensor: a plain Python object standing in
  front of one C++ QRotationSensor.

  It is built on the cute 'QSensor', as Qt's QRotationSensor is built on Qt's
  QSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRotationSensor that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'reading', 'hasZ',
  'setHasZ', 'hasZChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRotationSensor::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QRotationSensor::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QRotationSensor::~QRotationSensor()': the destructor: Python never
    removes a C++ QRotationSensor.
  - Qt's 'const QRotationSensorPrivate *QRotationSensor::d_func() const':
    takes in Python what 'QRotationSensorPrivate *QRotationSensor::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QRotationSensor is created at the first use, not by
    'QRotationSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRotationSensor.
  - Qt tells when it has removed the C++ QRotationSensor. Every call on the
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
    Calls Qt's 'QString QRotationSensor::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#tr

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
    #  QString QRotationSensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QRotationSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRotationSensor'

  #  A C++ QRotationSensor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRotationSensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRotationSensor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRotationSensor::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QRotationSensor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reading(self) -> Optional[QRotationReading]:
    """
    Calls Qt's 'QRotationReading *QRotationSensor::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#reading

    Returns
    -------

    Optional[QRotationReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRotationReading *QRotationSensor::reading() const
    address = self.uglySide.call('ritual_ZNK15QRotationSensor7readingEv')
    from . import QRotationReading
    return QRotationReading._cuteAt(address)

  def hasZ(self) -> bool:
    """
    Calls Qt's 'bool QRotationSensor::hasZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#hasZ
    """
    #  bool QRotationSensor::hasZ() const
    return self.uglySide.call('ritual_ZNK15QRotationSensor4hasZEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasZ(self, hasZ: bool) -> None:
    """
    Calls Qt's 'void QRotationSensor::setHasZ(bool hasZ)'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#setHasZ

    Parameters
    ----------

    hasZ : bool
      Passed on as it is.
    """
    #  void QRotationSensor::setHasZ(bool hasZ)
    self.uglySide.call('ritual_ZN15QRotationSensor7setHasZEb', hasZ)

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
    Notes what was given, for Qt's 'QRotationSensor::QRotationSensor(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrotationsensor.html#QRotationSensor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRotationSensor::QRotationSensor(QObject *parent)
    self._noteCreation(QRotationSensor, lambda: Rituals.call(
        'ritual_ZN15QRotationSensorC1EP7QObject',
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

  @overload(bool)
  def hasZChanged(self, hasZ: bool) -> None:
    """
    Calls Qt's 'void QRotationSensor::hasZChanged(bool hasZ)'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#hasZChanged

    Parameters
    ----------

    hasZ : bool
      Passed on as it is.
    """
    #  void QRotationSensor::hasZChanged(bool hasZ)
    self.uglySide.call('ritual_ZN15QRotationSensor11hasZChangedEb', hasZ)

  def d_func(self) -> Optional[QRotationSensorPrivate]:
    """
    Calls Qt's 'QRotationSensorPrivate *QRotationSensor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qrotationsensor.html#d_func

    Returns
    -------

    Optional[QRotationSensorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRotationSensorPrivate *QRotationSensor::d_func()
    address = self.uglySide.call('ritual_ZN15QRotationSensor6d_funcEv')
    from . import QRotationSensorPrivate
    return QRotationSensorPrivate._cuteAt(address)
