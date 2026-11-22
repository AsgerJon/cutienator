"""
QGraphicsPathItem binding of the Qt C++
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
from . import QAbstractGraphicsShapeItem, QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF, QVariant
  from ..QtGui import QPainter, QPainterPath
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPainterPath = WAIT['QPainterPath']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsPathItem(QAbstractGraphicsShapeItem):
  """
  The cute side of Qt's QGraphicsPathItem: a plain Python object standing in
  front of one C++ QGraphicsPathItem.

  It is built on the cute 'QAbstractGraphicsShapeItem', as Qt's
  QGraphicsPathItem is built on Qt's QAbstractGraphicsShapeItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsPathItem that has a ritual and that Python
  can call so far, 10 names in all: 'path', 'setPath', 'boundingRect',
  'shape', 'contains', 'paint', 'isObscuredBy', 'opaqueArea', 'type',
  'extension'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsPathItem::~QGraphicsPathItem()': the destructor: Python
    never removes a C++ QGraphicsPathItem.

  What has no ritual
  ------------------

  6 of the 19 functions Qt declares: 2 protected; 2 forbidden; 2 private.

  What to expect
  --------------

  - The C++ QGraphicsPathItem is created at the first use, not by
    'QGraphicsPathItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsPathItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsPathItem'

  #  A C++ QGraphicsPathItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsPathItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def path(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPathItem::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#path

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPathItem::path() const
    address = self.uglySide.call('ritual_ZNK17QGraphicsPathItem4pathEv')
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsPathItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspathitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsPathItem::boundingRect() const
    ritual = 'ritual_ZNK17QGraphicsPathItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsPathItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPathItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPathItem::shape() const
    ritual = 'ritual_ZNK17QGraphicsPathItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsPathItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsPathItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsPathItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK17QGraphicsPathItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsPathItem8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsPathItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspathitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsPathItem::isObscuredBy(const QGraphicsItem *item) const
    ritual = 'ritual_ZNK17QGraphicsPathItem12isObscuredByEPK13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGraphicsPathItem12isObscuredByEPK13QGraphicsIte'
          'm')
    return self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPathItem::opaqueArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPathItem::opaqueArea() const
    ritual = 'ritual_ZNK17QGraphicsPathItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsPathItem10opaqueAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsPathItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#type
    """
    #  int QGraphicsPathItem::type() const
    ritual = 'ritual_ZNK17QGraphicsPathItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsPathItem4typeEv'
    return self.uglySide.call(ritual)

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsPathItem::extension(const QVariant
    &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#extension

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsPathItem::extension(const QVariant &variant) const
    address = self.uglySide.call(
        'ritual_own_ZNK17QGraphicsPathItem9extensionERK8QVariant',
        self._valueOf(variant),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainterPath)
  def setPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QGraphicsPathItem::setPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#setPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QGraphicsPathItem::setPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN17QGraphicsPathItem7setPathERK12QPainterPath',
        self._valueOf(path),
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
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsPathItem::QGraphicsPathItem(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspathitem.html#QGraphicsPathItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsPathItem::QGraphicsPathItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsPathItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsPathItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(QPainterPath)
  @overload(QPainterPath, QGraphicsItem)
  @overload(QPainterPath, NoneType)
  def __init__(
      self,
      path: QPainterPath,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsPathItem::QGraphicsPathItem(const QPainterPath &path,
    QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspathitem.html#QGraphicsPathItem

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsPathItem::QGraphicsPathItem(const QPainterPath &path,
    #      QGraphicsItem *parent)
    self._noteCreation(QGraphicsPathItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsPathItemC1ERK12QPainterPathP13QGraphicsItem',
        self._valueOf(path), self._addressOf(parent, 'QGraphicsItem'),
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
    Calls Qt's 'void QGraphicsPathItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspathitem.html#paint

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
    #  void QGraphicsPathItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN17QGraphicsPathItem5paintEP8QPainterPK24QStyleOptionGraph'
        'icsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsPathItem5paintEP8QPainterPK24QStyleOptio'
          'nGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
