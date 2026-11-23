"""
QGraphicsItemGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QPainter, QPainterPath
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsItemGroup(QGraphicsItem):
  """
  The cute side of Qt's QGraphicsItemGroup: a plain Python object standing in
  front of one C++ QGraphicsItemGroup.

  It is built on the cute 'QGraphicsItem', as Qt's QGraphicsItemGroup is
  built on Qt's QGraphicsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsItemGroup that has a ritual and that Python
  can call so far, 7 names in all: 'addToGroup', 'removeFromGroup',
  'boundingRect', 'paint', 'isObscuredBy', 'opaqueArea', 'type'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsItemGroup::~QGraphicsItemGroup()': the destructor: Python
    never removes a C++ QGraphicsItemGroup.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 forbidden; 2 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QGraphicsItemGroup is created at the first use, not by
    'QGraphicsItemGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsItemGroup.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsItemGroup'

  #  A C++ QGraphicsItemGroup Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsItemGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItemGroup::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemgroup.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItemGroup::boundingRect() const
    ritual = 'ritual_ZNK18QGraphicsItemGroup12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGraphicsItemGroup12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemGroup::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemgroup.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItemGroup::isObscuredBy(const QGraphicsItem *item) const
    ritual = 'ritual_ZNK18QGraphicsItemGroup12isObscuredByEPK13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QGraphicsItemGroup12isObscuredByEPK13QGraphicsIt'
          'em')
    return self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsItemGroup::opaqueArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemgroup.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsItemGroup::opaqueArea() const
    ritual = 'ritual_ZNK18QGraphicsItemGroup10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGraphicsItemGroup10opaqueAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsItemGroup::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemgroup.html#type
    """
    #  int QGraphicsItemGroup::type() const
    ritual = 'ritual_ZNK18QGraphicsItemGroup4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGraphicsItemGroup4typeEv'
    return self.uglySide.call(ritual)

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

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsItemGroup::QGraphicsItemGroup(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemgroup.html#QGraphicsItemGroup

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsItemGroup::QGraphicsItemGroup(QGraphicsItem *parent)
    self._noteCreation(QGraphicsItemGroup, lambda: Rituals.call(
        'ritual_ZN18QGraphicsItemGroupC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QGraphicsItem)
  @overload(NoneType)
  def addToGroup(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItemGroup::addToGroup(QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemgroup.html#addToGroup

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemGroup::addToGroup(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN18QGraphicsItemGroup10addToGroupEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def removeFromGroup(self, item: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItemGroup::removeFromGroup(QGraphicsItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemgroup.html#removeFromGroup

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemGroup::removeFromGroup(QGraphicsItem *item)
    self.uglySide.call(
        'ritual_ZN18QGraphicsItemGroup15removeFromGroupEP13QGraphicsItem',
        self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QPainter, QStyleOptionGraphicsItem)
  @overload(QPainter, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem)
  @overload(NoneType, NoneType)
  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemGroup::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemgroup.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsItemGroup::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN18QGraphicsItemGroup5paintEP8QPainterPK24QStyleOptionGrap'
        'hicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QGraphicsItemGroup5paintEP8QPainterPK24QStyleOpti'
          'onGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
