"""
QGraphicsRectItem binding of the Qt C++
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
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsRectItem(QAbstractGraphicsShapeItem):
  """
  The cute side of Qt's QGraphicsRectItem: a plain Python object standing in
  front of one C++ QGraphicsRectItem.

  It is built on the cute 'QAbstractGraphicsShapeItem', as Qt's
  QGraphicsRectItem is built on Qt's QAbstractGraphicsShapeItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsRectItem that has a ritual and that Python
  can call so far, 10 names in all: 'rect', 'setRect', 'boundingRect',
  'shape', 'contains', 'paint', 'isObscuredBy', 'opaqueArea', 'type',
  'extension'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsRectItem::~QGraphicsRectItem()': the destructor: Python
    never removes a C++ QGraphicsRectItem.
  - Qt's 'bool QGraphicsRectItem::supportsExtension(Extension extension)
    const': names the enum 'QGraphicsItem::Extension', whose class cannot be
    named here.
  - Qt's 'void QGraphicsRectItem::setExtension(Extension extension, const
    QVariant &variant)': names the enum 'QGraphicsItem::Extension', whose
    class cannot be named here.
  - Qt's 'QGraphicsRectItemPrivate *QGraphicsRectItem::d_func()': gives
    'QGraphicsRectItemPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsRectItemPrivate *QGraphicsRectItem::d_func() const':
    gives 'QGraphicsRectItemPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsRectItem is created at the first use, not by
    'QGraphicsRectItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsRectItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsRectItem'

  #  A C++ QGraphicsRectItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsRectItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsRectItem::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsRectItem::rect() const
    address = self._callAs(
        'QGraphicsRectItem', 'ritual_ZNK17QGraphicsRectItem4rectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsRectItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsrectitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsRectItem::boundingRect() const
    ritual = 'ritual_ZNK17QGraphicsRectItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRectItem12boundingRectEv'
    address = self._callAs('QGraphicsRectItem', ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsRectItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsRectItem::shape() const
    ritual = 'ritual_ZNK17QGraphicsRectItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRectItem5shapeEv'
    address = self._callAs('QGraphicsRectItem', ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsRectItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsRectItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK17QGraphicsRectItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRectItem8containsERK7QPointF'
    return self._callAs(
        'QGraphicsRectItem', ritual, self._valueOf(point, 'QPointF'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsRectItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsrectitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsRectItem::isObscuredBy(const QGraphicsItem *item) const
    ritual = 'ritual_ZNK17QGraphicsRectItem12isObscuredByEPK13QGraphicsItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QGraphicsRectItem12isObscuredByEPK13QGraphicsIte'
          'm')
    return self._callAs(
        'QGraphicsRectItem', ritual, self._addressOf(item, 'QGraphicsItem'),
    )

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsRectItem::opaqueArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsRectItem::opaqueArea() const
    ritual = 'ritual_ZNK17QGraphicsRectItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRectItem10opaqueAreaEv'
    address = self._callAs('QGraphicsRectItem', ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsRectItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#type
    """
    #  int QGraphicsRectItem::type() const
    ritual = 'ritual_ZNK17QGraphicsRectItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRectItem4typeEv'
    return self._callAs('QGraphicsRectItem', ritual)

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsRectItem::extension(const QVariant
    &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#extension

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
    #  QVariant QGraphicsRectItem::extension(const QVariant &variant) const
    ritual = 'ritual_ZNK17QGraphicsRectItem9extensionERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QGraphicsRectItem9extensionERK8QVariant'
    address = self._callAs(
        'QGraphicsRectItem', ritual, self._valueOf(variant),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsRectItem::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsRectItem::setRect(const QRectF &rect)
    self._callAs(
        'QGraphicsRectItem',
        'ritual_ZN17QGraphicsRectItem7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QGraphicsRectItem::setRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#setRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QGraphicsRectItem::setRect(qreal x, qreal y, qreal w, qreal h)
    self._callAs(
        'QGraphicsRectItem', 'ritual_ZN17QGraphicsRectItem7setRectEdddd',
        x, y, w, h,
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
    'QGraphicsRectItem::QGraphicsRectItem(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsrectitem.html#QGraphicsRectItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsRectItem::QGraphicsRectItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsRectItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsRectItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(QRectF)
  @overload(QRectF, QGraphicsItem)
  @overload(QRectF, NoneType)
  def __init__(
      self,
      rect: QRectF,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsRectItem::QGraphicsRectItem(const QRectF &rect, QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsrectitem.html#QGraphicsRectItem

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsRectItem::QGraphicsRectItem(const QRectF &rect, QGraphicsItem
    #      *parent)
    self._noteCreation(QGraphicsRectItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsRectItemC1ERK6QRectFP13QGraphicsItem',
        self._valueOf(rect), self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(float, float, float, float)
  @overload(float, float, float, float, QGraphicsItem)
  @overload(float, float, float, float, NoneType)
  def __init__(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsRectItem::QGraphicsRectItem(qreal x, qreal y, qreal w, qreal h,
    QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsrectitem.html#QGraphicsRectItem

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsRectItem::QGraphicsRectItem(qreal x, qreal y, qreal w, qreal
    #      h, QGraphicsItem *parent)
    self._noteCreation(QGraphicsRectItem, lambda: Rituals.call(
        'ritual_ZN17QGraphicsRectItemC1EddddP13QGraphicsItem',
        x, y, w, h, self._addressOf(parent, 'QGraphicsItem'),
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
    Calls Qt's 'void QGraphicsRectItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsrectitem.html#paint

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
    #  void QGraphicsRectItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN17QGraphicsRectItem5paintEP8QPainterPK24QStyleOptionGraph'
        'icsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QGraphicsRectItem5paintEP8QPainterPK24QStyleOptio'
          'nGraphicsItemP7QWidget')
    self._callAs(
        'QGraphicsRectItem', ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
