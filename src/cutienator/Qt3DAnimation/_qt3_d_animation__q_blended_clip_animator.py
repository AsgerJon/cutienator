"""
Qt3DAnimation::QBlendedClipAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qblendedclipanimator.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlendedClipAnimator(Qt3DAnimation.QAbstractClipAnimator):
  """
  The cute side of Qt's Qt3DAnimation::QBlendedClipAnimator: a plain Python
  object standing in front of one C++ Qt3DAnimation::QBlendedClipAnimator.

  It is built on the cute 'Qt3DAnimation::QAbstractClipAnimator', as Qt's
  Qt3DAnimation::QBlendedClipAnimator is built on Qt's
  Qt3DAnimation::QAbstractClipAnimator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QBlendedClipAnimator that has a
  ritual and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'blendTree', 'setBlendTree', 'blendTreeChanged', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QBlendedClipAnimator::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QBlendedClipAnimator::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QBlendedClipAnimator::~QBlendedClipAnimator()': the
    destructor: Python never removes a C++
    Qt3DAnimation::QBlendedClipAnimator.
  - Qt's 'Qt3DAnimation::QBlendedClipAnimator::QBlendedClipAnimator(
    QBlendedClipAnimatorPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QBlendedClipAnimatorPrivate
    *Qt3DAnimation::QBlendedClipAnimator::d_func() const': takes in Python
    what 'QBlendedClipAnimatorPrivate
    *Qt3DAnimation::QBlendedClipAnimator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QBlendedClipAnimator is created at the first use,
    not by 'Qt3DAnimation::QBlendedClipAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QBlendedClipAnimator.
  - Qt tells when it has removed the C++ Qt3DAnimation::QBlendedClipAnimator.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DAnimation::QBlendedClipAnimator::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html#tr

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
    #  QString Qt3DAnimation::QBlendedClipAnimator::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation20QBlendedClipAnimator2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QBlendedClipAnimator'

  #  A C++ Qt3DAnimation::QBlendedClipAnimator Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QBlendedClipAnimator'

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
    *Qt3DAnimation::QBlendedClipAnimator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QBlendedClipAnimator::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QBlendedClipAnimator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def blendTree(self) -> Optional[Qt3DAnimation.QAbstractClipBlendNode]:
    """
    Calls Qt's 'QAbstractClipBlendNode
    *Qt3DAnimation::QBlendedClipAnimator::blendTree() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html#blendTree

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipBlendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractClipBlendNode
    #      *Qt3DAnimation::QBlendedClipAnimator::blendTree() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QBlendedClipAnimator9blendTreeEv',
    )
    return Qt3DAnimation.QAbstractClipBlendNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DAnimation.QAbstractClipBlendNode'])
  @overload(NoneType)
  def setBlendTree(
      self,
      blendTree: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QBlendedClipAnimator::setBlendTree(QAbstractClipBlendNode
    *blendTree)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html

    Parameters
    ----------

    blendTree : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QBlendedClipAnimator::setBlendTree(
    #      QAbstractClipBlendNode *blendTree)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QBlendedClipAnimator12setBlendTreeEPNS_2'
        '2QAbstractClipBlendNodeE',
        self._addressOf(blendTree),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QBlendedClipAnimator::QBlendedClipAnimator(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QBlendedClipAnimator::QBlendedClipAnimator(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QBlendedClipAnimator, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation20QBlendedClipAnimatorC1EPN8Qt3DCore5QNode'
        'E',
        self._addressOf(parent),
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

  @overload(WAIT['Qt3DAnimation.QAbstractClipBlendNode'])
  @overload(NoneType)
  def blendTreeChanged(
      self,
      blendTree: Optional[Qt3DAnimation.QAbstractClipBlendNode],
  ) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QBlendedClipAnimator::blendTreeChanged(
    QAbstractClipBlendNode *blendTree)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html

    Parameters
    ----------

    blendTree : Optional[Qt3DAnimation.QAbstractClipBlendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QBlendedClipAnimator::blendTreeChanged(
    #      QAbstractClipBlendNode *blendTree)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QBlendedClipAnimator16blendTreeChangedEP'
        'NS_22QAbstractClipBlendNodeE',
        self._addressOf(blendTree),
    )

  def d_func(self) -> Optional[Qt3DAnimation.QBlendedClipAnimatorPrivate]:
    """
    Calls Qt's 'QBlendedClipAnimatorPrivate
    *Qt3DAnimation::QBlendedClipAnimator::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qblendedclipanimator.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QBlendedClipAnimatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlendedClipAnimatorPrivate
    #      *Qt3DAnimation::QBlendedClipAnimator::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QBlendedClipAnimator6d_funcEv',
    )
    return Qt3DAnimation.QBlendedClipAnimatorPrivate._cuteAt(address)
