"""
QAbstractAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractAnimationPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractAnimation, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAnimationPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractAnimationPrivate: a plain Python object
  standing in front of one C++ QAbstractAnimationPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstractAnimationPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractAnimationPrivate that has a ritual and that
  Python can call so far, 12 names in all: 'get',
  '_qt_property_state_offset', 'setState', 'setDirection',
  'emitDirectionChanged', '_qt_property_direction_offset', 'setCurrentTime',
  '_qt_property_totalCurrentTime_offset', '_qt_property_loopCount_offset',
  'emitCurrentLoopChanged', '_qt_property_currentLoop_offset', 'q_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractAnimationPrivate::~QAbstractAnimationPrivate()': the
    destructor: Python never removes a C++ QAbstractAnimationPrivate.
  - Qt's 'const QAbstractAnimation *QAbstractAnimationPrivate::q_func()
    const': takes in Python what 'QAbstractAnimation
    *QAbstractAnimationPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QAbstractAnimationPrivate is created at the first use, not by
    'QAbstractAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractAnimationPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAbstractAnimation)
  @overload(NoneType)
  def get(
      q: Optional[QAbstractAnimation],
  ) -> Optional[QAbstractAnimationPrivate]:
    """
    Calls Qt's 'QAbstractAnimationPrivate
    *QAbstractAnimationPrivate::get(QAbstractAnimation *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractanimationprivate.html#get

    Parameters
    ----------

    q : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationPrivate
    #      *QAbstractAnimationPrivate::get(QAbstractAnimation *q)
    address = Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivate3getEP18QAbstractAnimation',
        CuteMixin._addressOf(q),
    )
    return QAbstractAnimationPrivate._cuteAt(address)

  @staticmethod
  def _qt_property_state_offset() -> int:
    """
    Calls Qt's 'size_t
    QAbstractAnimationPrivate::_qt_property_state_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  size_t QAbstractAnimationPrivate::_qt_property_state_offset()
    return Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivate25_qt_property_state_offsetEv',
    )

  @staticmethod
  def _qt_property_direction_offset() -> int:
    """
    Calls Qt's 'size_t
    QAbstractAnimationPrivate::_qt_property_direction_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  size_t QAbstractAnimationPrivate::_qt_property_direction_offset()
    return Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivate29_qt_property_direction_offse'
        'tEv',
    )

  @staticmethod
  def _qt_property_totalCurrentTime_offset() -> int:
    """
    Calls Qt's 'size_t
    QAbstractAnimationPrivate::_qt_property_totalCurrentTime_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  size_t
    #      QAbstractAnimationPrivate::_qt_property_totalCurrentTime_offset()
    return Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivate36_qt_property_totalCurrentTim'
        'e_offsetEv',
    )

  @staticmethod
  def _qt_property_loopCount_offset() -> int:
    """
    Calls Qt's 'size_t
    QAbstractAnimationPrivate::_qt_property_loopCount_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  size_t QAbstractAnimationPrivate::_qt_property_loopCount_offset()
    return Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivate29_qt_property_loopCount_offse'
        'tEv',
    )

  @staticmethod
  def _qt_property_currentLoop_offset() -> int:
    """
    Calls Qt's 'size_t
    QAbstractAnimationPrivate::_qt_property_currentLoop_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  size_t QAbstractAnimationPrivate::_qt_property_currentLoop_offset()
    return Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivate31_qt_property_currentLoop_off'
        'setEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractAnimationPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAnimation.State)
  def setState(self, state: QAbstractAnimation.State) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationPrivate::setState(QAbstractAnimation::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html#setState

    Parameters
    ----------

    state : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void QAbstractAnimationPrivate::setState(QAbstractAnimation::State
    #      state)
    self.uglySide.call(
        'ritual_ZN25QAbstractAnimationPrivate8setStateEN18QAbstractAnimatio'
        'n5StateE',
        state.value,
    )

  @overload(QAbstractAnimation.Direction)
  def setDirection(self, direction: QAbstractAnimation.Direction) -> None:
    """
    Calls Qt's 'void
    QAbstractAnimationPrivate::setDirection(QAbstractAnimation::Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html#setDirection

    Parameters
    ----------

    direction : QAbstractAnimation.Direction
      Passed on as its number.
    """
    #  void QAbstractAnimationPrivate::setDirection(QAbstractAnimation::
    #      Direction direction)
    self.uglySide.call(
        'ritual_ZN25QAbstractAnimationPrivate12setDirectionEN18QAbstractAni'
        'mation9DirectionE',
        direction.value,
    )

  @overload(int)
  def setCurrentTime(self, msecs: int) -> None:
    """
    Calls Qt's 'void QAbstractAnimationPrivate::setCurrentTime(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html#setCurrentTime

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QAbstractAnimationPrivate::setCurrentTime(int msecs)
    self.uglySide.call(
        'ritual_ZN25QAbstractAnimationPrivate14setCurrentTimeEi', msecs,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractAnimationPrivate::QAbstractAnimationPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  QAbstractAnimationPrivate::QAbstractAnimationPrivate()
    self._noteCreation(QAbstractAnimationPrivate, lambda: Rituals.call(
        'ritual_ZN25QAbstractAnimationPrivateC1Ev',
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

  def emitDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationPrivate::emitDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  void QAbstractAnimationPrivate::emitDirectionChanged()
    self.uglySide.call(
        'ritual_ZN25QAbstractAnimationPrivate20emitDirectionChangedEv',
    )

  def emitCurrentLoopChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractAnimationPrivate::emitCurrentLoopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html
    """
    #  void QAbstractAnimationPrivate::emitCurrentLoopChanged()
    self.uglySide.call(
        'ritual_ZN25QAbstractAnimationPrivate22emitCurrentLoopChangedEv',
    )

  def q_func(self) -> Optional[QAbstractAnimation]:
    """
    Calls Qt's 'QAbstractAnimation *QAbstractAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractanimationprivate.html#q_func

    Returns
    -------

    Optional[QAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimation *QAbstractAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QAbstractAnimationPrivate6q_funcEv',
    )
    return QAbstractAnimation._cuteAt(address)
