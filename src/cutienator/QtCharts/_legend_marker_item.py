"""
LegendMarkerItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/legendmarkeritem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means LegendMarkerItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsLayoutItem, QGraphicsObject
from . import QLegend

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
  from ..QtGui import QBrush, QFont, QImage, QPainter, QPen
  from ..QtWidgets import QGraphicsSceneHoverEvent, QStyleOptionGraphicsItem
  from ..QtWidgets import QWidget
  from . import QLegendMarkerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QFont = WAIT['QFont']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QImage = WAIT['QImage']
  QLegendMarkerPrivate = WAIT['QLegendMarkerPrivate']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LegendMarkerItem(QGraphicsObject, QGraphicsLayoutItem):
  """
  The cute side of Qt's LegendMarkerItem: a plain Python object standing in
  front of one C++ LegendMarkerItem.

  It is built on the cute 'QGraphicsObject', as Qt's LegendMarkerItem is
  built on Qt's QGraphicsObject, and has everything that class has. It is
  built on the cute 'QGraphicsLayoutItem' as well, as Qt's LegendMarkerItem
  is built on Qt's QGraphicsLayoutItem too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's LegendMarkerItem that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'setPen', 'pen',
  'setBrush', 'brush', 'setSeriesPen', 'setSeriesBrush',
  'setSeriesLightMarker', 'setFont', 'font', 'setLabel', 'label',
  'setLabelBrush', 'labelBrush', 'setGeometry', 'boundingRect', 'markerRect',
  'paint', 'sizeHint', 'hoverEnterEvent', 'hoverLeaveEvent',
  'displayedLabel', 'setToolTip', 'markerShape', 'setMarkerShape',
  'updateMarkerShapeAndSize', 'effectiveMarkerShape', 'effectiveMarkerWidth',
  'itemType', 'markerRectChanged', 'setItemBrushAndPen', 'setItemRect',
  'useMaxWidth'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *LegendMarkerItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int LegendMarkerItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'LegendMarkerItem::~LegendMarkerItem()': the destructor: Python
    never removes a C++ LegendMarkerItem.

  What has no ritual
  ------------------

  2 of the 40 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ LegendMarkerItem is created at the first use, not by
    'LegendMarkerItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ LegendMarkerItem.
  - Qt tells when it has removed the C++ LegendMarkerItem. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside LegendMarkerItem, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ItemType(CuteNum):
    """
    The enum 'LegendMarkerItem::ItemType' of Qt, with the 7 names Qt gives in
    it.
    """

    TypeRect = Kee[int](0)
    TypeLine = Kee[int](1)
    TypeCircle = Kee[int](2)
    TypeRotatedRect = Kee[int](3)
    TypeTriangle = Kee[int](4)
    TypeStar = Kee[int](5)
    TypePentagon = Kee[int](6)

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
    Calls Qt's 'QString LegendMarkerItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#tr

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
    #  QString LegendMarkerItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16LegendMarkerItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LegendMarkerItem'

  #  Qt's LegendMarkerItem is built on more than one class. The part of a C++
  #  LegendMarkerItem that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGraphicsLayoutItem':
          'ritual_cast_LegendMarkerItem_QGraphicsLayoutItem',
  }

  #  A C++ LegendMarkerItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_LegendMarkerItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *LegendMarkerItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *LegendMarkerItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen LegendMarkerItem::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen LegendMarkerItem::pen() const
    address = self.uglySide.call('ritual_ZNK16LegendMarkerItem3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush LegendMarkerItem::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush LegendMarkerItem::brush() const
    address = self.uglySide.call('ritual_ZNK16LegendMarkerItem5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont LegendMarkerItem::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont LegendMarkerItem::font() const
    address = self.uglySide.call('ritual_ZNK16LegendMarkerItem4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def label(self) -> str:
    """
    Calls Qt's 'QString LegendMarkerItem::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString LegendMarkerItem::label() const
    return self.uglySide.call('ritual_ZNK16LegendMarkerItem5labelEv')

  def labelBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush LegendMarkerItem::labelBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#labelBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush LegendMarkerItem::labelBrush() const
    address = self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem10labelBrushEv',
    )
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF LegendMarkerItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF LegendMarkerItem::boundingRect() const
    ritual = 'ritual_ZNK16LegendMarkerItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16LegendMarkerItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def markerRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF LegendMarkerItem::markerRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#markerRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF LegendMarkerItem::markerRect() const
    address = self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem10markerRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF LegendMarkerItem::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF LegendMarkerItem::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    ritual = 'ritual_ZNK16LegendMarkerItem8sizeHintEN2Qt8SizeHintERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16LegendMarkerItem8sizeHintEN2Qt8SizeHintERK6QSize'
          'F')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def displayedLabel(self) -> str:
    """
    Calls Qt's 'QString LegendMarkerItem::displayedLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#displayedLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString LegendMarkerItem::displayedLabel() const
    return self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem14displayedLabelEv',
    )

  def markerShape(self) -> QLegend.MarkerShape:
    """
    Calls Qt's 'QLegend::MarkerShape LegendMarkerItem::markerShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#markerShape

    Returns
    -------

    QLegend.MarkerShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegend.MarkerShape(number)' gives.
    """
    #  QLegend::MarkerShape LegendMarkerItem::markerShape() const
    return QLegend.MarkerShape(self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem11markerShapeEv',
    ))

  def effectiveMarkerShape(self) -> QLegend.MarkerShape:
    """
    Calls Qt's 'QLegend::MarkerShape LegendMarkerItem::effectiveMarkerShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#effectiveMarkerShape

    Returns
    -------

    QLegend.MarkerShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLegend.MarkerShape(number)' gives.
    """
    #  QLegend::MarkerShape LegendMarkerItem::effectiveMarkerShape() const
    return QLegend.MarkerShape(self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem20effectiveMarkerShapeEv',
    ))

  def effectiveMarkerWidth(self) -> float:
    """
    Calls Qt's 'qreal LegendMarkerItem::effectiveMarkerWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#effectiveMarkerWidth
    """
    #  qreal LegendMarkerItem::effectiveMarkerWidth() const
    return self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem20effectiveMarkerWidthEv',
    )

  def itemType(self) -> ItemType:
    """
    Calls Qt's 'ItemType LegendMarkerItem::itemType() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#itemType

    Returns
    -------

    ItemType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ItemType(number)' gives.
    """
    #  ItemType LegendMarkerItem::itemType() const
    return LegendMarkerItem.ItemType(self.uglySide.call(
        'ritual_ZNK16LegendMarkerItem8itemTypeEv',
    ))

  def useMaxWidth(self) -> bool:
    """
    Calls Qt's 'bool LegendMarkerItem::useMaxWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#useMaxWidth
    """
    #  bool LegendMarkerItem::useMaxWidth() const
    return self.uglySide.call('ritual_ZNK16LegendMarkerItem11useMaxWidthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void LegendMarkerItem::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void LegendMarkerItem::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem8setBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setSeriesPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setSeriesPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setSeriesPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void LegendMarkerItem::setSeriesPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem12setSeriesPenERK4QPen',
        self._valueOf(pen),
    )

  @overload(QBrush)
  def setSeriesBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setSeriesBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#setSeriesBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void LegendMarkerItem::setSeriesBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem14setSeriesBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QImage)
  def setSeriesLightMarker(self, image: QImage) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setSeriesLightMarker(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#setSeriesLightMarker

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void LegendMarkerItem::setSeriesLightMarker(const QImage &image)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem20setSeriesLightMarkerERK6QImage',
        self._valueOf(image),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void LegendMarkerItem::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem7setFontERK5QFont', self._valueOf(font),
    )

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setLabel(const QString label)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void LegendMarkerItem::setLabel(const QString label)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem8setLabelE7QString', label,
    )

  @overload(QBrush)
  def setLabelBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setLabelBrush(const QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#setLabelBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void LegendMarkerItem::setLabelBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem13setLabelBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setGeometry(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void LegendMarkerItem::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN16LegendMarkerItem11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16LegendMarkerItem11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(str)
  def setToolTip(self, tooltip: str) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setToolTip(const QString &tooltip)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setToolTip

    Parameters
    ----------

    tooltip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void LegendMarkerItem::setToolTip(const QString &tooltip)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem10setToolTipERK7QString', tooltip,
    )

  @overload(QLegend.MarkerShape)
  def setMarkerShape(self, shape: QLegend.MarkerShape) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setMarkerShape(QLegend::MarkerShape
    shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#setMarkerShape

    Parameters
    ----------

    shape : QLegend.MarkerShape
      Passed on as its number.
    """
    #  void LegendMarkerItem::setMarkerShape(QLegend::MarkerShape shape)
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem14setMarkerShapeEN7QLegend11MarkerShape'
        'E',
        shape.value,
    )

  def setItemBrushAndPen(self) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setItemBrushAndPen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#setItemBrushAndPen
    """
    #  void LegendMarkerItem::setItemBrushAndPen()
    self.uglySide.call('ritual_ZN16LegendMarkerItem18setItemBrushAndPenEv')

  def setItemRect(self) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::setItemRect()'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#setItemRect
    """
    #  void LegendMarkerItem::setItemRect()
    self.uglySide.call('ritual_ZN16LegendMarkerItem11setItemRectEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLegendMarkerPrivate)
  @overload(NoneType)
  @overload(QLegendMarkerPrivate, QGraphicsObject)
  @overload(QLegendMarkerPrivate, NoneType)
  @overload(NoneType, QGraphicsObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      marker: Optional[QLegendMarkerPrivate],
      parent: Optional[QGraphicsObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'LegendMarkerItem::LegendMarkerItem(QLegendMarkerPrivate *marker,
    QGraphicsObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#LegendMarkerItem

    Parameters
    ----------

    marker : Optional[QLegendMarkerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QGraphicsObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  LegendMarkerItem::LegendMarkerItem(QLegendMarkerPrivate *marker,
    #      QGraphicsObject *parent)
    self._noteCreation(LegendMarkerItem, lambda: Rituals.call(
        'ritual_ZN16LegendMarkerItemC1EP20QLegendMarkerPrivateP15QGraphicsO'
        'bject',
        self._addressOf(marker), self._addressOf(parent),
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
    Calls Qt's 'void LegendMarkerItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/legendmarkeritem.html#paint

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
    #  void LegendMarkerItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN16LegendMarkerItem5paintEP8QPainterPK24QStyleOptionGraphi'
        'csItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16LegendMarkerItem5paintEP8QPainterPK24QStyleOption'
          'GraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMarkerItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMarkerItem::hoverEnterEvent(QGraphicsSceneHoverEvent
    #      *event)
    ritual = (
        'ritual_ZN16LegendMarkerItem15hoverEnterEventEP24QGraphicsSceneHove'
        'rEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16LegendMarkerItem15hoverEnterEventEP24QGraphicsSce'
          'neHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMarkerItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMarkerItem::hoverLeaveEvent(QGraphicsSceneHoverEvent
    #      *event)
    ritual = (
        'ritual_ZN16LegendMarkerItem15hoverLeaveEventEP24QGraphicsSceneHove'
        'rEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16LegendMarkerItem15hoverLeaveEventEP24QGraphicsSce'
          'neHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def updateMarkerShapeAndSize(self) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::updateMarkerShapeAndSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#updateMarkerShapeAndSize
    """
    #  void LegendMarkerItem::updateMarkerShapeAndSize()
    self.uglySide.call(
        'ritual_ZN16LegendMarkerItem24updateMarkerShapeAndSizeEv',
    )

  def markerRectChanged(self) -> None:
    """
    Calls Qt's 'void LegendMarkerItem::markerRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmarkeritem.html#markerRectChanged
    """
    #  void LegendMarkerItem::markerRectChanged()
    self.uglySide.call('ritual_ZN16LegendMarkerItem17markerRectChangedEv')
