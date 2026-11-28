"""
QGraphicsSimpleTextItem binding of the Qt C++
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
  from ..QtGui import QFont, QPainter, QPainterPath
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):
  """
  The cute side of Qt's QGraphicsSimpleTextItem: a plain Python object
  standing in front of one C++ QGraphicsSimpleTextItem.

  It is built on the cute 'QAbstractGraphicsShapeItem', as Qt's
  QGraphicsSimpleTextItem is built on Qt's QAbstractGraphicsShapeItem, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSimpleTextItem that has a ritual and that
  Python can call so far, 12 names in all: 'setText', 'text', 'setFont',
  'font', 'boundingRect', 'shape', 'contains', 'paint', 'isObscuredBy',
  'opaqueArea', 'type', 'extension'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSimpleTextItem::~QGraphicsSimpleTextItem()': the
    destructor: Python never removes a C++ QGraphicsSimpleTextItem.
  - Qt's 'bool QGraphicsSimpleTextItem::supportsExtension(Extension
    extension) const': names the enum 'QGraphicsItem::Extension', whose class
    cannot be named here.
  - Qt's 'void QGraphicsSimpleTextItem::setExtension(Extension extension,
    const QVariant &variant)': names the enum 'QGraphicsItem::Extension',
    whose class cannot be named here.
  - Qt's 'QGraphicsSimpleTextItemPrivate *QGraphicsSimpleTextItem::d_func()':
    gives 'QGraphicsSimpleTextItemPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsSimpleTextItemPrivate
    *QGraphicsSimpleTextItem::d_func() const': gives
    'QGraphicsSimpleTextItemPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSimpleTextItem is created at the first use, not by
    'QGraphicsSimpleTextItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSimpleTextItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSimpleTextItem'

  #  A C++ QGraphicsSimpleTextItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSimpleTextItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString QGraphicsSimpleTextItem::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGraphicsSimpleTextItem::text() const
    return self.uglySide.call('ritual_ZNK23QGraphicsSimpleTextItem4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphicsSimpleTextItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphicsSimpleTextItem::font() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsSimpleTextItem4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsSimpleTextItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsSimpleTextItem::boundingRect() const
    ritual = 'ritual_ZNK23QGraphicsSimpleTextItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QGraphicsSimpleTextItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def shape(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsSimpleTextItem::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#shape

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsSimpleTextItem::shape() const
    ritual = 'ritual_ZNK23QGraphicsSimpleTextItem5shapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QGraphicsSimpleTextItem5shapeEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QGraphicsSimpleTextItem::contains(const QPointF &point)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGraphicsSimpleTextItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK23QGraphicsSimpleTextItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QGraphicsSimpleTextItem8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  @overload(QGraphicsItem)
  @overload(NoneType)
  def isObscuredBy(self, item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsSimpleTextItem::isObscuredBy(const
    QGraphicsItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#isObscuredBy

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsSimpleTextItem::isObscuredBy(const QGraphicsItem *item)
    #      const
    ritual = (
        'ritual_ZNK23QGraphicsSimpleTextItem12isObscuredByEPK13QGraphicsIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QGraphicsSimpleTextItem12isObscuredByEPK13QGraph'
          'icsItem')
    return self.uglySide.call(ritual, self._addressOf(item, 'QGraphicsItem'))

  def opaqueArea(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGraphicsSimpleTextItem::opaqueArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#opaqueArea

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGraphicsSimpleTextItem::opaqueArea() const
    ritual = 'ritual_ZNK23QGraphicsSimpleTextItem10opaqueAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QGraphicsSimpleTextItem10opaqueAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int QGraphicsSimpleTextItem::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#type
    """
    #  int QGraphicsSimpleTextItem::type() const
    ritual = 'ritual_ZNK23QGraphicsSimpleTextItem4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QGraphicsSimpleTextItem4typeEv'
    return self.uglySide.call(ritual)

  @overload(QVariant)
  def extension(self, variant: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsSimpleTextItem::extension(const QVariant
    &variant) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#extension

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
    #  QVariant QGraphicsSimpleTextItem::extension(const QVariant &variant)
    #      const
    ritual = 'ritual_ZNK23QGraphicsSimpleTextItem9extensionERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QGraphicsSimpleTextItem9extensionERK8QVariant')
    address = self.uglySide.call(ritual, self._valueOf(variant))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QGraphicsSimpleTextItem::setText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGraphicsSimpleTextItem::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN23QGraphicsSimpleTextItem7setTextERK7QString', text,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsSimpleTextItem::setFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsSimpleTextItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN23QGraphicsSimpleTextItem7setFontERK5QFont',
        self._valueOf(font),
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
    'QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(QGraphicsItem
    #      *parent)
    self._noteCreation(QGraphicsSimpleTextItem, lambda: Rituals.call(
        'ritual_ZN23QGraphicsSimpleTextItemC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
    ))

  @overload(str)
  @overload(str, QGraphicsItem)
  @overload(str, NoneType)
  def __init__(
      self,
      text: str,
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(const QString &text,
    QGraphicsItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicssimpletextitem.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsSimpleTextItem::QGraphicsSimpleTextItem(const QString &text,
    #      QGraphicsItem *parent)
    self._noteCreation(QGraphicsSimpleTextItem, lambda: Rituals.call(
        'ritual_ZN23QGraphicsSimpleTextItemC1ERK7QStringP13QGraphicsItem',
        text, self._addressOf(parent, 'QGraphicsItem'),
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
    Calls Qt's 'void QGraphicsSimpleTextItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicssimpletextitem.html#paint

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
    #  void QGraphicsSimpleTextItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN23QGraphicsSimpleTextItem5paintEP8QPainterPK24QStyleOptio'
        'nGraphicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QGraphicsSimpleTextItem5paintEP8QPainterPK24QStyl'
          'eOptionGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )
