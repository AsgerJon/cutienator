"""
QSvgAnimateNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimate_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgAnimateNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QSvgAbstractAnimation, QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgAnimateNode(QSvgNode, QSvgAbstractAnimation):
  """
  The cute side of Qt's QSvgAnimateNode: a plain Python object standing in
  front of one C++ QSvgAnimateNode.

  It is built on the cute 'QSvgNode', as Qt's QSvgAnimateNode is built on
  Qt's QSvgNode, and has everything that class has. It is built on the cute
  'QSvgAbstractAnimation' as well, as Qt's QSvgAnimateNode is built on Qt's
  QSvgAbstractAnimation too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgAnimateNode that has a ritual and that Python
  can call so far, 10 names in all: 'setLinkId', 'linkId', 'animationType',
  'isActive', 'setRunningTime', 'setRepeatCount', 'setFill', 'fill',
  'setAdditiveType', 'additiveType'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimateNode::~QSvgAnimateNode()': the destructor: Python never
    removes a C++ QSvgAnimateNode.
  - Qt's 'void QSvgAnimateNode::drawCommand(QPainter *p, QSvgExtraStates
    &states)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgAnimateNode::shouldDrawNode(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgAnimateNode is created at the first use, not by
    'QSvgAnimateNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAnimateNode.
  """

  #  The enums Qt writes inside QSvgAnimateNode, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Additive(CuteNum):
    """
    The enum 'QSvgAnimateNode::Additive' of Qt, with the 2 names Qt gives in
    it.
    """

    Sum = Kee[int](0)
    Replace = Kee[int](1)

  class Fill(CuteNum):
    """
    The enum 'QSvgAnimateNode::Fill' of Qt, with the 2 names Qt gives in it.
    """

    Freeze = Kee[int](0)
    Remove = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimateNode'

  #  Qt's QSvgAnimateNode is built on more than one class. The part of a C++
  #  QSvgAnimateNode that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSvgAbstractAnimation':
          'ritual_cast_QSvgAnimateNode_QSvgAbstractAnimation',
  }

  #  A C++ QSvgAnimateNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAnimateNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def linkId(self) -> str:
    """
    Calls Qt's 'const QString &QSvgAnimateNode::linkId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#linkId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QSvgAnimateNode::linkId() const
    return self.uglySide.call('ritual_ZNK15QSvgAnimateNode6linkIdEv')

  def animationType(self) -> QSvgAbstractAnimation.AnimationType:
    """
    Calls Qt's 'AnimationType QSvgAnimateNode::animationType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#animationType

    Returns
    -------

    QSvgAbstractAnimation.AnimationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgAbstractAnimation.AnimationType(number)' gives.
    """
    #  AnimationType QSvgAnimateNode::animationType() const
    ritual = 'ritual_ZNK15QSvgAnimateNode13animationTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgAnimateNode13animationTypeEv'
    return QSvgAbstractAnimation.AnimationType(self.uglySide.call(ritual))

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSvgAnimateNode::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#isActive
    """
    #  bool QSvgAnimateNode::isActive() const
    ritual = 'ritual_ZNK15QSvgAnimateNode8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgAnimateNode8isActiveEv'
    return self.uglySide.call(ritual)

  def fill(self) -> Fill:
    """
    Calls Qt's 'Fill QSvgAnimateNode::fill() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#fill

    Returns
    -------

    Fill
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Fill(number)' gives.
    """
    #  Fill QSvgAnimateNode::fill() const
    return QSvgAnimateNode.Fill(self.uglySide.call(
        'ritual_ZNK15QSvgAnimateNode4fillEv',
    ))

  def additiveType(self) -> Additive:
    """
    Calls Qt's 'Additive QSvgAnimateNode::additiveType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#additiveType

    Returns
    -------

    Additive
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Additive(number)' gives.
    """
    #  Additive QSvgAnimateNode::additiveType() const
    return QSvgAnimateNode.Additive(self.uglySide.call(
        'ritual_ZNK15QSvgAnimateNode12additiveTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLinkId(self, link: str) -> None:
    """
    Calls Qt's 'void QSvgAnimateNode::setLinkId(const QString &link)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#setLinkId

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgAnimateNode::setLinkId(const QString &link)
    self.uglySide.call(
        'ritual_ZN15QSvgAnimateNode9setLinkIdERK7QString', link,
    )

  @overload(int, int, int, int)
  def setRunningTime(
      self,
      startMs: int,
      durMs: int,
      endMs: int,
      by: int,
  ) -> None:
    """
    Calls Qt's 'void QSvgAnimateNode::setRunningTime(int startMs, int durMs,
    int endMs, int by)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatenode.html#setRunningTime

    Parameters
    ----------

    startMs : int
      Passed on as it is.

    durMs : int
      Passed on as it is.

    endMs : int
      Passed on as it is.

    by : int
      Passed on as it is.
    """
    #  void QSvgAnimateNode::setRunningTime(int startMs, int durMs, int
    #      endMs, int by)
    self.uglySide.call(
        'ritual_ZN15QSvgAnimateNode14setRunningTimeEiiii',
        startMs, durMs, endMs, by,
    )

  @overload(float)
  def setRepeatCount(self, repeatCount: float) -> None:
    """
    Calls Qt's 'void QSvgAnimateNode::setRepeatCount(qreal repeatCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatenode.html#setRepeatCount

    Parameters
    ----------

    repeatCount : float
      Passed on as it is.
    """
    #  void QSvgAnimateNode::setRepeatCount(qreal repeatCount)
    self.uglySide.call(
        'ritual_ZN15QSvgAnimateNode14setRepeatCountEd', repeatCount,
    )

  @overload(Fill)
  def setFill(self, fill: Fill) -> None:
    """
    Calls Qt's 'void QSvgAnimateNode::setFill(Fill fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimatenode.html#setFill

    Parameters
    ----------

    fill : Fill
      Passed on as its number.
    """
    #  void QSvgAnimateNode::setFill(Fill fill)
    self.uglySide.call(
        'ritual_ZN15QSvgAnimateNode7setFillENS_4FillE', fill.value,
    )

  @overload()
  @overload(Additive)
  def setAdditiveType(self, additive: Additive = Additive.Replace) -> None:
    """
    Calls Qt's 'void QSvgAnimateNode::setAdditiveType(Additive additive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatenode.html#setAdditiveType

    Parameters
    ----------

    additive : Additive
      Passed on as its number. May be left out, as in Qt: it is then
      Additive.Replace.
    """
    #  void QSvgAnimateNode::setAdditiveType(Additive additive)
    self.uglySide.call(
        'ritual_ZN15QSvgAnimateNode15setAdditiveTypeENS_8AdditiveE',
        additive.value,
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
    Notes what was given, for Qt's 'QSvgAnimateNode::QSvgAnimateNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatenode.html#QSvgAnimateNode
    """
    #  QSvgAnimateNode::QSvgAnimateNode()
    self._noteCreation(QSvgAnimateNode, lambda: Rituals.call(
        'ritual_ZN15QSvgAnimateNodeC1Ev',
    ))

  @overload(QSvgNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QSvgNode]) -> None:
    """
    Notes what was given, for Qt's 'QSvgAnimateNode::QSvgAnimateNode(QSvgNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatenode.html#QSvgAnimateNode

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSvgAnimateNode::QSvgAnimateNode(QSvgNode *parent)
    self._noteCreation(QSvgAnimateNode, lambda: Rituals.call(
        'ritual_ZN15QSvgAnimateNodeC1EP8QSvgNode', self._addressOf(parent),
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
