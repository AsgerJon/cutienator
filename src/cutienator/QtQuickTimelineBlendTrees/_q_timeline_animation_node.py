"""
QTimelineAnimationNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimelineBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qtimelineanimationnode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QTimelineAnimationNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QBlendTreeNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuickTimeline import QQuickTimeline, QQuickTimelineAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTimeline = WAIT['QQuickTimeline']
  QQuickTimelineAnimation = WAIT['QQuickTimelineAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTimelineAnimationNode(QBlendTreeNode):
  """
  The cute side of Qt's QTimelineAnimationNode: a plain Python object
  standing in front of one C++ QTimelineAnimationNode.

  It is built on the cute 'QBlendTreeNode', as Qt's QTimelineAnimationNode is
  built on Qt's QBlendTreeNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTimelineAnimationNode that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'animation',
  'setAnimation', 'timeline', 'setTimeline', 'currentFrame',
  'setCurrentFrame', 'animationChanged', 'timelineChanged',
  'currentFrameChanged', 'updateFrameData', 'updateAnimationTarget'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTimelineAnimationNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QTimelineAnimationNode::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTimelineAnimationNode is created at the first use, not by
    'QTimelineAnimationNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTimelineAnimationNode.
  - Qt tells when it has removed the C++ QTimelineAnimationNode. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QTimelineAnimationNode::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimelineanimationnode.html#tr

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
    #  QString QTimelineAnimationNode::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QTimelineAnimationNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimelineAnimationNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTimelineAnimationNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTimelineAnimationNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QTimelineAnimationNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def animation(self) -> Optional[QQuickTimelineAnimation]:
    """
    Calls Qt's 'QQuickTimelineAnimation *QTimelineAnimationNode::animation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#animation

    Returns
    -------

    Optional[QQuickTimelineAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTimelineAnimation *QTimelineAnimationNode::animation() const
    address = self.uglySide.call(
        'ritual_ZNK22QTimelineAnimationNode9animationEv',
    )
    from ..QtQuickTimeline import QQuickTimelineAnimation
    return QQuickTimelineAnimation._cuteAt(address)

  def timeline(self) -> Optional[QQuickTimeline]:
    """
    Calls Qt's 'QQuickTimeline *QTimelineAnimationNode::timeline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#timeline

    Returns
    -------

    Optional[QQuickTimeline]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTimeline *QTimelineAnimationNode::timeline() const
    address = self.uglySide.call(
        'ritual_ZNK22QTimelineAnimationNode8timelineEv',
    )
    from ..QtQuickTimeline import QQuickTimeline
    return QQuickTimeline._cuteAt(address)

  def currentFrame(self) -> float:
    """
    Calls Qt's 'qreal QTimelineAnimationNode::currentFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#currentFrame
    """
    #  qreal QTimelineAnimationNode::currentFrame() const
    return self.uglySide.call(
        'ritual_ZNK22QTimelineAnimationNode12currentFrameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTimelineAnimation)
  @overload(NoneType)
  def setAnimation(
      self,
      newAnimation: Optional[QQuickTimelineAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    QTimelineAnimationNode::setAnimation(QQuickTimelineAnimation
    *newAnimation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#setAnimation

    Parameters
    ----------

    newAnimation : Optional[QQuickTimelineAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTimelineAnimationNode::setAnimation(QQuickTimelineAnimation
    #      *newAnimation)
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode12setAnimationEP23QQuickTimelineA'
        'nimation',
        self._addressOf(newAnimation),
    )

  @overload(QQuickTimeline)
  @overload(NoneType)
  def setTimeline(self, newTimeline: Optional[QQuickTimeline]) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::setTimeline(QQuickTimeline
    *newTimeline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#setTimeline

    Parameters
    ----------

    newTimeline : Optional[QQuickTimeline]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTimelineAnimationNode::setTimeline(QQuickTimeline *newTimeline)
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode11setTimelineEP14QQuickTimeline',
        self._addressOf(newTimeline),
    )

  @overload(float)
  def setCurrentFrame(self, newCurrentFrame: float) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::setCurrentFrame(qreal
    newCurrentFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#setCurrentFrame

    Parameters
    ----------

    newCurrentFrame : float
      Passed on as it is.
    """
    #  void QTimelineAnimationNode::setCurrentFrame(qreal newCurrentFrame)
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode15setCurrentFrameEd',
        newCurrentFrame,
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
    'QTimelineAnimationNode::QTimelineAnimationNode(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#QTimelineAnimationNode

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTimelineAnimationNode::QTimelineAnimationNode(QObject *parent)
    self._noteCreation(QTimelineAnimationNode, lambda: Rituals.call(
        'ritual_ZN22QTimelineAnimationNodeC1EP7QObject',
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

  def animationChanged(self) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::animationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#animationChanged
    """
    #  void QTimelineAnimationNode::animationChanged()
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode16animationChangedEv',
    )

  def timelineChanged(self) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::timelineChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#timelineChanged
    """
    #  void QTimelineAnimationNode::timelineChanged()
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode15timelineChangedEv',
    )

  def currentFrameChanged(self) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::currentFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#currentFrameChanged
    """
    #  void QTimelineAnimationNode::currentFrameChanged()
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode19currentFrameChangedEv',
    )

  def updateFrameData(self) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::updateFrameData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#updateFrameData
    """
    #  void QTimelineAnimationNode::updateFrameData()
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode15updateFrameDataEv',
    )

  def updateAnimationTarget(self) -> None:
    """
    Calls Qt's 'void QTimelineAnimationNode::updateAnimationTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimelineanimationnode.html#updateAnimationTarget
    """
    #  void QTimelineAnimationNode::updateAnimationTarget()
    self.uglySide.call(
        'ritual_ZN22QTimelineAnimationNode21updateAnimationTargetEv',
    )
