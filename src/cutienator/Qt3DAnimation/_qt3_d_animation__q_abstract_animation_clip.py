"""
Qt3DAnimation::QAbstractAnimationClip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qabstractanimationclip.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAnimationClip(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractAnimationClip: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAbstractAnimationClip.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DAnimation::QAbstractAnimationClip is built on Qt's Qt3DCore::QNode, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractAnimationClip that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'duration', 'durationChanged', 'd_func'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAbstractAnimationClip::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAbstractAnimationClip::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QAbstractAnimationClip::~QAbstractAnimationClip()':
    the destructor: Python never removes a C++
    Qt3DAnimation::QAbstractAnimationClip.
  - Qt's 'Qt3DAnimation::QAbstractAnimationClip::QAbstractAnimationClip(
    QAbstractAnimationClipPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QAbstractAnimationClipPrivate
    *Qt3DAnimation::QAbstractAnimationClip::d_func() const': takes in Python
    what 'QAbstractAnimationClipPrivate
    *Qt3DAnimation::QAbstractAnimationClip::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractAnimationClip is created at the first
    use, not by 'Qt3DAnimation::QAbstractAnimationClip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAbstractAnimationClip.
  - Qt tells when it has removed the C++
    Qt3DAnimation::QAbstractAnimationClip. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's Qt3DAnimation::QAbstractAnimationClip that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DAnimation::QAbstractAnimationClip::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclip.html#tr

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
    #  QString Qt3DAnimation::QAbstractAnimationClip::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation22QAbstractAnimationClip2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractAnimationClip'

  #  A C++ Qt3DAnimation::QAbstractAnimationClip Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAbstractAnimationClip'

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
    *Qt3DAnimation::QAbstractAnimationClip::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclip.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAbstractAnimationClip::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation22QAbstractAnimationClip10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAbstractAnimationClip::duration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclip.html#duration
    """
    #  float Qt3DAnimation::QAbstractAnimationClip::duration() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation22QAbstractAnimationClip8durationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'Qt3DAnimation::QAbstractAnimationClip::QAbstractAnimationClip(
    QAbstractAnimationClipPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAbstractAnimationClip.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DAnimation::QAbstractAnimationClip::QAbstractAnimationClip(QAbs"
        "tractAnimationClipPrivate &dd, Qt3DCore::QNode *parent)': takes a "
        "type Python has no way to hand over yet.")

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
  def durationChanged(self, duration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractAnimationClip::durationChanged(float duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclip.html

    Parameters
    ----------

    duration : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractAnimationClip::durationChanged(float
    #      duration)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation22QAbstractAnimationClip15durationChangedE'
        'f',
        duration,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAbstractAnimationClipPrivate]:
    """
    Calls Qt's 'QAbstractAnimationClipPrivate
    *Qt3DAnimation::QAbstractAnimationClip::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclip.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractAnimationClipPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationClipPrivate
    #      *Qt3DAnimation::QAbstractAnimationClip::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation22QAbstractAnimationClip6d_funcEv',
    )
    return Qt3DAnimation.QAbstractAnimationClipPrivate._cuteAt(address)
