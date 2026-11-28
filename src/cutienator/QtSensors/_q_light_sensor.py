"""
QLightSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qlightsensor.h, Qt 6.12.0. Changes made here are lost.
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
  from . import QLightReading, QLightSensorPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLightSensor(QSensor):
  """
  The cute side of Qt's QLightSensor: a plain Python object standing in front
  of one C++ QLightSensor.

  It is built on the cute 'QSensor', as Qt's QLightSensor is built on Qt's
  QSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLightSensor that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'reading', 'fieldOfView',
  'setFieldOfView', 'fieldOfViewChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLightSensor::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLightSensor::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QLightSensor::~QLightSensor()': the destructor: Python never
    removes a C++ QLightSensor.
  - Qt's 'const QLightSensorPrivate *QLightSensor::d_func() const': takes in
    Python what 'QLightSensorPrivate *QLightSensor::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLightSensor is created at the first use, not by
    'QLightSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLightSensor.
  - Qt tells when it has removed the C++ QLightSensor. Every call on the cute
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
    Calls Qt's 'QString QLightSensor::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#tr

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
    #  QString QLightSensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QLightSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLightSensor'

  #  A C++ QLightSensor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLightSensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLightSensor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLightSensor::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QLightSensor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reading(self) -> Optional[QLightReading]:
    """
    Calls Qt's 'QLightReading *QLightSensor::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#reading

    Returns
    -------

    Optional[QLightReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLightReading *QLightSensor::reading() const
    address = self.uglySide.call('ritual_ZNK12QLightSensor7readingEv')
    from . import QLightReading
    return QLightReading._cuteAt(address)

  def fieldOfView(self) -> float:
    """
    Calls Qt's 'qreal QLightSensor::fieldOfView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#fieldOfView
    """
    #  qreal QLightSensor::fieldOfView() const
    return self.uglySide.call('ritual_ZNK12QLightSensor11fieldOfViewEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFieldOfView(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void QLightSensor::setFieldOfView(qreal fieldOfView)'.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#setFieldOfView

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void QLightSensor::setFieldOfView(qreal fieldOfView)
    self.uglySide.call(
        'ritual_ZN12QLightSensor14setFieldOfViewEd', fieldOfView,
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
    Notes what was given, for Qt's 'QLightSensor::QLightSensor(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#QLightSensor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLightSensor::QLightSensor(QObject *parent)
    self._noteCreation(QLightSensor, lambda: Rituals.call(
        'ritual_ZN12QLightSensorC1EP7QObject',
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

  @overload(float)
  def fieldOfViewChanged(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void QLightSensor::fieldOfViewChanged(qreal fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlightsensor.html#fieldOfViewChanged

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void QLightSensor::fieldOfViewChanged(qreal fieldOfView)
    self.uglySide.call(
        'ritual_ZN12QLightSensor18fieldOfViewChangedEd', fieldOfView,
    )

  def d_func(self) -> Optional[QLightSensorPrivate]:
    """
    Calls Qt's 'QLightSensorPrivate *QLightSensor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlightsensor.html#d_func

    Returns
    -------

    Optional[QLightSensorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLightSensorPrivate *QLightSensor::d_func()
    address = self.uglySide.call('ritual_ZN12QLightSensor6d_funcEv')
    from . import QLightSensorPrivate
    return QLightSensorPrivate._cuteAt(address)
