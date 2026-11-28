"""
QQuickRotationAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRotationAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickPropertyAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickRotationAnimationPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRotationAnimation(QQuickPropertyAnimation):
  """
  The cute side of Qt's QQuickRotationAnimation: a plain Python object
  standing in front of one C++ QQuickRotationAnimation.

  It is built on the cute 'QQuickPropertyAnimation', as Qt's
  QQuickRotationAnimation is built on Qt's QQuickPropertyAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRotationAnimation that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'd_func',
  'from_', 'setFrom', 'to', 'setTo', 'direction', 'setDirection',
  'directionChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRotationAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRotationAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickRotationAnimationPrivate
    *QQuickRotationAnimation::d_func() const': takes in Python what
    'QQuickRotationAnimationPrivate *QQuickRotationAnimation::d_func()'
    takes.
  - Qt's 'QQuickRotationAnimation::~QQuickRotationAnimation()': the
    destructor: Python never removes a C++ QQuickRotationAnimation.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRotationAnimation is created at the first use, not by
    'QQuickRotationAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRotationAnimation.
  - Qt tells when it has removed the C++ QQuickRotationAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickRotationAnimation, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class RotationDirection(CuteNum):
    """
    The enum 'QQuickRotationAnimation::RotationDirection' of Qt, with the 4
    names Qt gives in it.
    """

    Numerical = Kee[int](0)
    Shortest = Kee[int](1)
    Clockwise = Kee[int](2)
    Counterclockwise = Kee[int](3)

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
    Calls Qt's 'QString QQuickRotationAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotationanimation.html#tr

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
    #  QString QQuickRotationAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickRotationAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRotationAnimation'

  #  A C++ QQuickRotationAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRotationAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRotationAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRotationAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickRotationAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickRotationAnimation::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotationanimation.html#from
    """
    #  qreal QQuickRotationAnimation::from() const
    return self.uglySide.call('ritual_ZNK23QQuickRotationAnimation4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickRotationAnimation::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotationanimation.html#to
    """
    #  qreal QQuickRotationAnimation::to() const
    return self.uglySide.call('ritual_ZNK23QQuickRotationAnimation2toEv')

  def direction(self) -> RotationDirection:
    """
    Calls Qt's 'RotationDirection QQuickRotationAnimation::direction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html#direction

    Returns
    -------

    RotationDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RotationDirection(number)' gives.
    """
    #  RotationDirection QQuickRotationAnimation::direction() const
    return QQuickRotationAnimation.RotationDirection(self.uglySide.call(
        'ritual_ZNK23QQuickRotationAnimation9directionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimation::setFrom(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html#setFrom

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickRotationAnimation::setFrom(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickRotationAnimation7setFromEd', a0)

  @overload(float)
  def setTo(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimation::setTo(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotationanimation.html#setTo

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickRotationAnimation::setTo(qreal a0)
    self.uglySide.call('ritual_ZN23QQuickRotationAnimation5setToEd', a0)

  @overload(RotationDirection)
  def setDirection(self, direction: RotationDirection) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimation::setDirection(RotationDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html#setDirection

    Parameters
    ----------

    direction : RotationDirection
      Passed on as its number.
    """
    #  void QQuickRotationAnimation::setDirection(RotationDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN23QQuickRotationAnimation12setDirectionENS_17RotationDire'
        'ctionE',
        direction.value,
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
    'QQuickRotationAnimation::QQuickRotationAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRotationAnimation::QQuickRotationAnimation(QObject *parent)
    self._noteCreation(QQuickRotationAnimation, lambda: Rituals.call(
        'ritual_ZN23QQuickRotationAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickRotationAnimationPrivate]:
    """
    Calls Qt's 'QQuickRotationAnimationPrivate
    *QQuickRotationAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html#d_func

    Returns
    -------

    Optional[QQuickRotationAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRotationAnimationPrivate *QQuickRotationAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickRotationAnimation6d_funcEv',
    )
    from . import QQuickRotationAnimationPrivate
    return QQuickRotationAnimationPrivate._cuteAt(address)

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimation::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimation.html#directionChanged
    """
    #  void QQuickRotationAnimation::directionChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickRotationAnimation16directionChangedEv',
    )
