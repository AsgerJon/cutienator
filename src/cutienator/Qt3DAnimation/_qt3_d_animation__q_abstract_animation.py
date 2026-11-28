"""
Qt3DAnimation::QAbstractAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAnimation(QObject):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractAnimation: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAbstractAnimation.

  It is built on the cute 'QObject', as Qt's
  Qt3DAnimation::QAbstractAnimation is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractAnimation that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'animationName', 'animationType', 'position', 'duration',
  'setAnimationName', 'setPosition', 'setDuration', 'animationNameChanged',
  'positionChanged', 'durationChanged', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAbstractAnimation::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAbstractAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QAbstractAnimation::QAbstractAnimation(
    QAbstractAnimationPrivate &dd, QObject *parent)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QAbstractAnimationPrivate
    *Qt3DAnimation::QAbstractAnimation::d_func() const': takes in Python what
    'QAbstractAnimationPrivate *Qt3DAnimation::QAbstractAnimation::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractAnimation is created at the first use,
    not by 'Qt3DAnimation::QAbstractAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAbstractAnimation.
  - Qt tells when it has removed the C++ Qt3DAnimation::QAbstractAnimation.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QAbstractAnimation that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DAnimation::QAbstractAnimation, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class AnimationType(CuteNum):
    """
    The enum 'Qt3DAnimation::QAbstractAnimation::AnimationType' of Qt, with
    the 3 names Qt gives in it.
    """

    KeyframeAnimation = Kee[int](1)
    MorphingAnimation = Kee[int](2)
    VertexBlendAnimation = Kee[int](3)

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
    Calls Qt's 'QString Qt3DAnimation::QAbstractAnimation::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#tr

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
    #  QString Qt3DAnimation::QAbstractAnimation::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DAnimation::QAbstractAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAbstractAnimation::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAbstractAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def animationName(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QAbstractAnimation::animationName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QAbstractAnimation::animationName() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAbstractAnimation13animationNameEv',
    )

  def animationType(self) -> AnimationType:
    """
    Calls Qt's 'QAbstractAnimation::AnimationType
    Qt3DAnimation::QAbstractAnimation::animationType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html

    Returns
    -------

    AnimationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AnimationType(number)'
      gives.
    """
    #  QAbstractAnimation::AnimationType
    #      Qt3DAnimation::QAbstractAnimation::animationType() const
    return QAbstractAnimation.AnimationType(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAbstractAnimation13animationTypeEv',
    ))

  def position(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAbstractAnimation::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#position
    """
    #  float Qt3DAnimation::QAbstractAnimation::position() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAbstractAnimation8positionEv',
    )

  def duration(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAbstractAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#duration
    """
    #  float Qt3DAnimation::QAbstractAnimation::duration() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QAbstractAnimation8durationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAnimationName(self, name: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractAnimation::setAnimationName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QAbstractAnimation::setAnimationName(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation16setAnimationNameERK7'
        'QString',
        name,
    )

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractAnimation::setPosition(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractAnimation::setPosition(float position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation11setPositionEf',
        position,
    )

  @overload(float)
  def setDuration(self, duration: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractAnimation::setDuration(float
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#setDuration

    Parameters
    ----------

    duration : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractAnimation::setDuration(float duration)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation11setDurationEf',
        duration,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DAnimation::QAbstractAnimation::QAbstractAnimation(
    QAbstractAnimationPrivate &dd, QObject *parent)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAbstractAnimation.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DAnimation::QAbstractAnimation::QAbstractAnimation(QAbstractAni"
        "mationPrivate &dd, QObject *parent)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload(str)
  def animationNameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractAnimation::animationNameChanged(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QAbstractAnimation::animationNameChanged(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation20animationNameChanged'
        'ERK7QString',
        name,
    )

  @overload(float)
  def positionChanged(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractAnimation::positionChanged(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractAnimation::positionChanged(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation15positionChangedEf',
        position,
    )

  @overload(float)
  def durationChanged(self, duration: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAbstractAnimation::durationChanged(float
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html

    Parameters
    ----------

    duration : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractAnimation::durationChanged(float
    #      duration)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation15durationChangedEf',
        duration,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAbstractAnimationPrivate]:
    """
    Calls Qt's 'QAbstractAnimationPrivate
    *Qt3DAnimation::QAbstractAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimation.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationPrivate *Qt3DAnimation::QAbstractAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QAbstractAnimation6d_funcEv',
    )
    return Qt3DAnimation.QAbstractAnimationPrivate._cuteAt(address)
