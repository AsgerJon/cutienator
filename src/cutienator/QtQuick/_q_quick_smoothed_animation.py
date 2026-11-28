"""
QQuickSmoothedAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickSmoothedAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickNumberAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickSmoothedAnimationPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSmoothedAnimation(QQuickNumberAnimation):
  """
  The cute side of Qt's QQuickSmoothedAnimation: a plain Python object
  standing in front of one C++ QQuickSmoothedAnimation.

  It is built on the cute 'QQuickNumberAnimation', as Qt's
  QQuickSmoothedAnimation is built on Qt's QQuickNumberAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSmoothedAnimation that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'd_func',
  'reversingMode', 'setReversingMode', 'duration', 'setDuration', 'velocity',
  'setVelocity', 'maximumEasingTime', 'setMaximumEasingTime',
  'velocityChanged', 'reversingModeChanged', 'maximumEasingTimeChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSmoothedAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSmoothedAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickSmoothedAnimationPrivate
    *QQuickSmoothedAnimation::d_func() const': takes in Python what
    'QQuickSmoothedAnimationPrivate *QQuickSmoothedAnimation::d_func()'
    takes.
  - Qt's 'QAbstractAnimationJob
    *QQuickSmoothedAnimation::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSmoothedAnimation is created at the first use, not by
    'QQuickSmoothedAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSmoothedAnimation.
  - Qt tells when it has removed the C++ QQuickSmoothedAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickSmoothedAnimation, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ReversingMode(CuteNum):
    """
    The enum 'QQuickSmoothedAnimation::ReversingMode' of Qt, with the 3 names
    Qt gives in it.
    """

    Eased = Kee[int](0)
    Immediate = Kee[int](1)
    Sync = Kee[int](2)

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
    Calls Qt's 'QString QQuickSmoothedAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksmoothedanimation.html#tr

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
    #  QString QQuickSmoothedAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickSmoothedAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSmoothedAnimation'

  #  A C++ QQuickSmoothedAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSmoothedAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSmoothedAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSmoothedAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickSmoothedAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reversingMode(self) -> ReversingMode:
    """
    Calls Qt's 'ReversingMode QQuickSmoothedAnimation::reversingMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#reversingMode

    Returns
    -------

    ReversingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ReversingMode(number)'
      gives.
    """
    #  ReversingMode QQuickSmoothedAnimation::reversingMode() const
    return QQuickSmoothedAnimation.ReversingMode(self.uglySide.call(
        'ritual_ZNK23QQuickSmoothedAnimation13reversingModeEv',
    ))

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickSmoothedAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#duration
    """
    #  int QQuickSmoothedAnimation::duration() const
    ritual = 'ritual_ZNK23QQuickSmoothedAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickSmoothedAnimation8durationEv'
    return self.uglySide.call(ritual)

  def velocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickSmoothedAnimation::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#velocity
    """
    #  qreal QQuickSmoothedAnimation::velocity() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSmoothedAnimation8velocityEv',
    )

  def maximumEasingTime(self) -> int:
    """
    Calls Qt's 'int QQuickSmoothedAnimation::maximumEasingTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#maximumEasingTime
    """
    #  int QQuickSmoothedAnimation::maximumEasingTime() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSmoothedAnimation17maximumEasingTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ReversingMode)
  def setReversingMode(self, a0: ReversingMode) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::setReversingMode(ReversingMode
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#setReversingMode

    Parameters
    ----------

    a0 : ReversingMode
      Passed on as its number.
    """
    #  void QQuickSmoothedAnimation::setReversingMode(ReversingMode a0)
    self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation16setReversingModeENS_13Reversin'
        'gModeE',
        a0.value,
    )

  @overload(int)
  def setDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::setDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#setDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickSmoothedAnimation::setDuration(int a0)
    ritual = 'ritual_ZN23QQuickSmoothedAnimation11setDurationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickSmoothedAnimation11setDurationEi'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setVelocity(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::setVelocity(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#setVelocity

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickSmoothedAnimation::setVelocity(qreal a0)
    self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation11setVelocityEd', a0,
    )

  @overload(int)
  def setMaximumEasingTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::setMaximumEasingTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#setMaximumEasingTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickSmoothedAnimation::setMaximumEasingTime(int a0)
    self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation20setMaximumEasingTimeEi', a0,
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
    'QQuickSmoothedAnimation::QQuickSmoothedAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSmoothedAnimation::QQuickSmoothedAnimation(QObject *parent)
    self._noteCreation(QQuickSmoothedAnimation, lambda: Rituals.call(
        'ritual_ZN23QQuickSmoothedAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickSmoothedAnimationPrivate]:
    """
    Calls Qt's 'QQuickSmoothedAnimationPrivate
    *QQuickSmoothedAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#d_func

    Returns
    -------

    Optional[QQuickSmoothedAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSmoothedAnimationPrivate *QQuickSmoothedAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation6d_funcEv',
    )
    from . import QQuickSmoothedAnimationPrivate
    return QQuickSmoothedAnimationPrivate._cuteAt(address)

  def velocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::velocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#velocityChanged
    """
    #  void QQuickSmoothedAnimation::velocityChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation15velocityChangedEv',
    )

  def reversingModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::reversingModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html#reversingModeChanged
    """
    #  void QQuickSmoothedAnimation::reversingModeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation20reversingModeChangedEv',
    )

  def maximumEasingTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSmoothedAnimation::maximumEasingTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimation.html
    """
    #  void QQuickSmoothedAnimation::maximumEasingTimeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSmoothedAnimation24maximumEasingTimeChangedEv',
    )
