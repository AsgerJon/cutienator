"""
QBlendAnimationNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTimelineBlendTrees/6.12.0/QtQuickTimelineBlendTrees/private/qblendanimationnode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QBlendAnimationNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QBlendTreeNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBlendAnimationNode(QBlendTreeNode):
  """
  The cute side of Qt's QBlendAnimationNode: a plain Python object standing
  in front of one C++ QBlendAnimationNode.

  It is built on the cute 'QBlendTreeNode', as Qt's QBlendAnimationNode is
  built on Qt's QBlendTreeNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBlendAnimationNode that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'source1',
  'setSource1', 'source2', 'setSource2', 'weight', 'setWeight',
  'handleInputFrameDataChanged', 'source1Changed', 'source2Changed',
  'weightChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBlendAnimationNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBlendAnimationNode::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QBlendAnimationNode is created at the first use, not by
    'QBlendAnimationNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBlendAnimationNode.
  - Qt tells when it has removed the C++ QBlendAnimationNode. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QBlendAnimationNode::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qblendanimationnode.html#tr

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
    #  QString QBlendAnimationNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QBlendAnimationNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBlendAnimationNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBlendAnimationNode::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBlendAnimationNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QBlendAnimationNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source1(self) -> Optional[QBlendTreeNode]:
    """
    Calls Qt's 'QBlendTreeNode *QBlendAnimationNode::source1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblendanimationnode.html#source1

    Returns
    -------

    Optional[QBlendTreeNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlendTreeNode *QBlendAnimationNode::source1() const
    address = self.uglySide.call('ritual_ZNK19QBlendAnimationNode7source1Ev')
    return QBlendTreeNode._cuteAt(address)

  def source2(self) -> Optional[QBlendTreeNode]:
    """
    Calls Qt's 'QBlendTreeNode *QBlendAnimationNode::source2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblendanimationnode.html#source2

    Returns
    -------

    Optional[QBlendTreeNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlendTreeNode *QBlendAnimationNode::source2() const
    address = self.uglySide.call('ritual_ZNK19QBlendAnimationNode7source2Ev')
    return QBlendTreeNode._cuteAt(address)

  def weight(self) -> float:
    """
    Calls Qt's 'qreal QBlendAnimationNode::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblendanimationnode.html#weight
    """
    #  qreal QBlendAnimationNode::weight() const
    return self.uglySide.call('ritual_ZNK19QBlendAnimationNode6weightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBlendTreeNode)
  @overload(NoneType)
  def setSource1(self, newSource1: Optional[QBlendTreeNode]) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::setSource1(QBlendTreeNode
    *newSource1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#setSource1

    Parameters
    ----------

    newSource1 : Optional[QBlendTreeNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBlendAnimationNode::setSource1(QBlendTreeNode *newSource1)
    self.uglySide.call(
        'ritual_ZN19QBlendAnimationNode10setSource1EP14QBlendTreeNode',
        self._addressOf(newSource1),
    )

  @overload(QBlendTreeNode)
  @overload(NoneType)
  def setSource2(self, newSource2: Optional[QBlendTreeNode]) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::setSource2(QBlendTreeNode
    *newSource2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#setSource2

    Parameters
    ----------

    newSource2 : Optional[QBlendTreeNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBlendAnimationNode::setSource2(QBlendTreeNode *newSource2)
    self.uglySide.call(
        'ritual_ZN19QBlendAnimationNode10setSource2EP14QBlendTreeNode',
        self._addressOf(newSource2),
    )

  @overload(float)
  def setWeight(self, newWeight: float) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::setWeight(qreal newWeight)'.

    Qt's own words: https://doc.qt.io/qt-6/qblendanimationnode.html#setWeight

    Parameters
    ----------

    newWeight : float
      Passed on as it is.
    """
    #  void QBlendAnimationNode::setWeight(qreal newWeight)
    self.uglySide.call(
        'ritual_ZN19QBlendAnimationNode9setWeightEd', newWeight,
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
    'QBlendAnimationNode::QBlendAnimationNode(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#QBlendAnimationNode

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBlendAnimationNode::QBlendAnimationNode(QObject *parent)
    self._noteCreation(QBlendAnimationNode, lambda: Rituals.call(
        'ritual_ZN19QBlendAnimationNodeC1EP7QObject',
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

  def handleInputFrameDataChanged(self) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::handleInputFrameDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html
    """
    #  void QBlendAnimationNode::handleInputFrameDataChanged()
    self.uglySide.call(
        'ritual_ZN19QBlendAnimationNode27handleInputFrameDataChangedEv',
    )

  def source1Changed(self) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::source1Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#source1Changed
    """
    #  void QBlendAnimationNode::source1Changed()
    self.uglySide.call('ritual_ZN19QBlendAnimationNode14source1ChangedEv')

  def source2Changed(self) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::source2Changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#source2Changed
    """
    #  void QBlendAnimationNode::source2Changed()
    self.uglySide.call('ritual_ZN19QBlendAnimationNode14source2ChangedEv')

  def weightChanged(self) -> None:
    """
    Calls Qt's 'void QBlendAnimationNode::weightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qblendanimationnode.html#weightChanged
    """
    #  void QBlendAnimationNode::weightChanged()
    self.uglySide.call('ritual_ZN19QBlendAnimationNode13weightChangedEv')
