"""
QTapSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qtapsensor.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QTapReading, QTapSensorPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTapSensor(QSensor):
  """
  The cute side of Qt's QTapSensor: a plain Python object standing in front
  of one C++ QTapSensor.

  It is built on the cute 'QSensor', as Qt's QTapSensor is built on Qt's
  QSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTapSensor that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'reading',
  'returnDoubleTapEvents', 'setReturnDoubleTapEvents',
  'returnDoubleTapEventsChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTapSensor::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTapSensor::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTapSensor::~QTapSensor()': the destructor: Python never removes a
    C++ QTapSensor.
  - Qt's 'const QTapSensorPrivate *QTapSensor::d_func() const': takes in
    Python what 'QTapSensorPrivate *QTapSensor::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QTapSensor is created at the first use, not by 'QTapSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTapSensor.
  - Qt tells when it has removed the C++ QTapSensor. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QTapSensor::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapsensor.html#tr

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
    #  QString QTapSensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QTapSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTapSensor'

  #  A C++ QTapSensor Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTapSensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTapSensor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapsensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTapSensor::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTapSensor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reading(self) -> Optional[QTapReading]:
    """
    Calls Qt's 'QTapReading *QTapSensor::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtapsensor.html#reading

    Returns
    -------

    Optional[QTapReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTapReading *QTapSensor::reading() const
    address = self.uglySide.call('ritual_ZNK10QTapSensor7readingEv')
    from . import QTapReading
    return QTapReading._cuteAt(address)

  def returnDoubleTapEvents(self) -> bool:
    """
    Calls Qt's 'bool QTapSensor::returnDoubleTapEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapsensor.html#returnDoubleTapEvents
    """
    #  bool QTapSensor::returnDoubleTapEvents() const
    return self.uglySide.call(
        'ritual_ZNK10QTapSensor21returnDoubleTapEventsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setReturnDoubleTapEvents(self, returnDoubleTapEvents: bool) -> None:
    """
    Calls Qt's 'void QTapSensor::setReturnDoubleTapEvents(bool
    returnDoubleTapEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapsensor.html#setReturnDoubleTapEvents

    Parameters
    ----------

    returnDoubleTapEvents : bool
      Passed on as it is.
    """
    #  void QTapSensor::setReturnDoubleTapEvents(bool returnDoubleTapEvents)
    self.uglySide.call(
        'ritual_ZN10QTapSensor24setReturnDoubleTapEventsEb',
        returnDoubleTapEvents,
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
    Notes what was given, for Qt's 'QTapSensor::QTapSensor(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtapsensor.html#QTapSensor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTapSensor::QTapSensor(QObject *parent)
    self._noteCreation(QTapSensor, lambda: Rituals.call(
        'ritual_ZN10QTapSensorC1EP7QObject',
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
  def returnDoubleTapEventsChanged(
      self,
      returnDoubleTapEvents: bool,
  ) -> None:
    """
    Calls Qt's 'void QTapSensor::returnDoubleTapEventsChanged(bool
    returnDoubleTapEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapsensor.html#returnDoubleTapEventsChanged

    Parameters
    ----------

    returnDoubleTapEvents : bool
      Passed on as it is.
    """
    #  void QTapSensor::returnDoubleTapEventsChanged(bool
    #      returnDoubleTapEvents)
    self.uglySide.call(
        'ritual_ZN10QTapSensor28returnDoubleTapEventsChangedEb',
        returnDoubleTapEvents,
    )

  def d_func(self) -> Optional[QTapSensorPrivate]:
    """
    Calls Qt's 'QTapSensorPrivate *QTapSensor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtapsensor.html#d_func

    Returns
    -------

    Optional[QTapSensorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTapSensorPrivate *QTapSensor::d_func()
    address = self.uglySide.call('ritual_ZN10QTapSensor6d_funcEv')
    from . import QTapSensorPrivate
    return QTapSensorPrivate._cuteAt(address)
