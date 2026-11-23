"""
QGraphicsPixmapItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF, QVariant
  from ..QtGui import QPainter, QPainterPath, QPixmap
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsPixmapItem(QGraphicsItem):
  """
  The cute side of Qt's QGraphicsPixmapItem: a plain Python object standing
  in front of one C++ QGraphicsPixmapItem.

  It is built on the cute 'QGraphicsItem', as Qt's QGraphicsPixmapItem is
  built on Qt's QGraphicsItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsPixmapItem that has a ritual and that
  Python can call so far, 16 names in all: 'pixmap', 'setPixmap',
  'transformationMode', 'setTransformationMode', 'offset', 'setOffset',
  'boundingRect', 'shape', 'contains', 'paint', 'isObscuredBy', 'opaqueArea',
  'type', 'shapeMode', 'setShapeMode', 'extension'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsPixmapItem::~QGraphicsPixmapItem()': the destructor:
    Python never removes a C++ QGraphicsPixmapItem.
  - Qt's 'bool QGraphicsPixmapItem::supportsExtension(Extension extension)
    const': names the enum 'QGraphicsItem::Extension', whose class cannot be
    named here.
  - Qt's 'void QGraphicsPixmapItem::setExtension(Extension extension, const
    QVariant &variant)': names the enum 'QGraphicsItem::Extension', whose
    class cannot be named here.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 forbidden; 2 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QGraphicsPixmapItem is created at the first use, not by
    'QGraphicsPixmapItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsPixmapItem.
  """

  #  The enums Qt writes inside QGraphicsPixmapItem, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ShapeMode(CuteNum):
    """
    The enum 'QGraphicsPixmapItem::ShapeMode' of Qt, with the 3 names Qt
    gives in it.
    """

    MaskShape = Kee[int](0)
    BoundingRectShape = Kee[int](1)
    HeuristicMaskShape = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsPixmapItem'

  #  A C++ QGraphicsPixmapItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsPixmapItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QGraphicsPixmapItem::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QGraphicsPixmapItem::pixmap() const
    address = self.uglySide.call('ritual_ZNK19QGraphicsPixmapItem6pixmapEv')
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def transformationMode(self) -> Qt.TransformationMode:
    """
    Calls Qt's 'Qt::TransformationMode
    QGraphicsPixmapItem::transformationMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#transformationMode

    Returns
    -------

    Qt.TransformationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.TransformationMode(number)' gives.
    """
    #  Qt::TransformationMode QGraphicsPixmapItem::transformationMode() const
    return Qt.TransformationMode(self.uglySide.call(
        'ritual_ZNK19QGraphicsPixmapItem18transformationModeEv',
    ))

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsPixmapItem::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsPixmapItem::offset() const
    address = self.uglySide.call('ritual_ZNK19QGraphicsPixmapItem6offsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsPixmapItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsPixmapItem::boundingRect() const
    ritual = 'ritual_ZNK19QGraphicsPixmapItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsPixmapItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPixmapItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPixmapItem::shape() const
    ritual = 'ritual_ZNK19QGraphicsPixmapItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsPixmapItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsPixmapItem::contains(const QPointF &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsPixmapItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK19QGraphicsPixmapItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsPixmapItem8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsPixmapItem::isObscuredBy(const QGraphicsItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsPixmapItem::isObscuredBy(const QGraphicsItem *item)
    #      const
    ritual = (
        'ritual_ZNK19QGraphicsPixmapItem12isObscuredByEPK13QGraphicsItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QGraphicsPixmapItem12isObscuredByEPK13QGraphicsI'
          'tem')
    return self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsPixmapItem::opaqueArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsPixmapItem::opaqueArea() const
    ritual = 'ritual_ZNK19QGraphicsPixmapItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsPixmapItem10opaqueAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsPixmapItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#type
    """
    #  int QGraphicsPixmapItem::type() const
    ritual = 'ritual_ZNK19QGraphicsPixmapItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsPixmapItem4typeEv'
    return self.uglySide.call(ritual)

  def shapeMode(self) -> ShapeMode:
    """
    Calls Qt's 'ShapeMode QGraphicsPixmapItem::shapeMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#shapeMode

    Returns
    -------

    ShapeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ShapeMode(number)' gives.
    """
    #  ShapeMode QGraphicsPixmapItem::shapeMode() const
    return QGraphicsPixmapItem.ShapeMode(self.uglySide.call(
        'ritual_ZNK19QGraphicsPixmapItem9shapeModeEv',
    ))

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsPixmapItem::extension(const QVariant
    &variant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#extension

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
    #  QVariant QGraphicsPixmapItem::extension(const QVariant &variant) const
    ritual = 'ritual_ZNK19QGraphicsPixmapItem9extensionERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsPixmapItem9extensionERK8QVariant'
    address = self.uglySide.call(ritual, self._valueOf(variant))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPixmap)
  def setPixmap(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QGraphicsPixmapItem::setPixmap(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#setPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QGraphicsPixmapItem::setPixmap(const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN19QGraphicsPixmapItem9setPixmapERK7QPixmap',
        self._valueOf(pixmap),
    )

  @overload(Qt.TransformationMode)
  def setTransformationMode(self, mode: Qt.TransformationMode) -> None:
    """
    Calls Qt's 'void
    QGraphicsPixmapItem::setTransformationMode(Qt::TransformationMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#setTransformationMode

    Parameters
    ----------

    mode : Qt.TransformationMode
      Passed on as its number.
    """
    #  void QGraphicsPixmapItem::setTransformationMode(Qt::TransformationMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN19QGraphicsPixmapItem21setTransformationModeEN2Qt18Transf'
        'ormationModeE',
        mode.value,
    )

  @overload(QPointF)
  def setOffset(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsPixmapItem::setOffset(const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#setOffset

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsPixmapItem::setOffset(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN19QGraphicsPixmapItem9setOffsetERK7QPointF',
        self._valueOf(offset),
    )

  @overload(float, float)
  def setOffset(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QGraphicsPixmapItem::setOffset(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#setOffset

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QGraphicsPixmapItem::setOffset(qreal x, qreal y)
    self.uglySide.call('ritual_ZN19QGraphicsPixmapItem9setOffsetEdd', x, y)

  @overload(ShapeMode)
  def setShapeMode(self, mode: ShapeMode) -> None:
    """
    Calls Qt's 'void QGraphicsPixmapItem::setShapeMode(ShapeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#setShapeMode

    Parameters
    ----------

    mode : ShapeMode
      Passed on as its number.
    """
    #  void QGraphicsPixmapItem::setShapeMode(ShapeMode mode)
    self.uglySide.call(
        'ritual_ZN19QGraphicsPixmapItem12setShapeModeENS_9ShapeModeE',
        mode.value,
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
    'QGraphicsPixmapItem::QGraphicsPixmapItem(QGraphicsItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#QGraphicsPixmapItem

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsPixmapItem::QGraphicsPixmapItem(QGraphicsItem *parent)
    self._noteCreation(QGraphicsPixmapItem, lambda: Rituals.call(
        'ritual_ZN19QGraphicsPixmapItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(QPixmap)
  @overload(QPixmap, QGraphicsItem)
  @overload(QPixmap, NoneType)
  def __init__(
      self,
      pixmap: QPixmap,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsPixmapItem::QGraphicsPixmapItem(const QPixmap &pixmap,
    QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicspixmapitem.html#QGraphicsPixmapItem

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsPixmapItem::QGraphicsPixmapItem(const QPixmap &pixmap,
    #      QGraphicsItem *parent)
    self._noteCreation(QGraphicsPixmapItem, lambda: Rituals.call(
        'ritual_ZN19QGraphicsPixmapItemC1ERK7QPixmapP13QGraphicsItem',
        self._valueOf(pixmap), self._addressOf(parent, 'QGraphicsItem'),
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
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsPixmapItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicspixmapitem.html#paint

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
      object.
    """
    #  void QGraphicsPixmapItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN19QGraphicsPixmapItem5paintEP8QPainterPK24QStyleOptionGra'
        'phicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QGraphicsPixmapItem5paintEP8QPainterPK24QStyleOpt'
          'ionGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
