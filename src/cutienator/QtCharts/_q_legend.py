"""
QLegend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qlegend.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtWidgets import QGraphicsWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QColor, QFont, QHideEvent, QPainter, QPen
  from ..QtGui import QShowEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import QAbstractSeries, QChart, QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QBrush = WAIT['QBrush']
  QChart = WAIT['QChart']
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QHideEvent = WAIT['QHideEvent']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QShowEvent = WAIT['QShowEvent']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLegend(QGraphicsWidget):
  """
  The cute side of Qt's QLegend: a plain Python object standing in front of
  one C++ QLegend.

  It is built on the cute 'QGraphicsWidget', as Qt's QLegend is built on Qt's
  QGraphicsWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLegend that has a ritual and that Python can call
  so far, 45 names in all: 'metaObject', 'tr', 'paint', 'setBrush', 'brush',
  'setColor', 'color', 'setPen', 'pen', 'setBorderColor', 'borderColor',
  'setFont', 'font', 'setLabelBrush', 'labelBrush', 'setLabelColor',
  'labelColor', 'setAlignment', 'alignment', 'detachFromChart',
  'attachToChart', 'isAttachedToChart', 'setBackgroundVisible',
  'isBackgroundVisible', 'markers', 'reverseMarkers', 'setReverseMarkers',
  'showToolTips', 'setShowToolTips', 'isInteractive', 'setInteractive',
  'markerShape', 'setMarkerShape', 'hideEvent', 'showEvent',
  'backgroundVisibleChanged', 'colorChanged', 'borderColorChanged',
  'fontChanged', 'labelColorChanged', 'reverseMarkersChanged',
  'showToolTipsChanged', 'markerShapeChanged', 'attachedToChartChanged',
  'interactiveChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLegend::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QLegend::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QLegend::~QLegend()': the destructor: Python never removes a C++
    QLegend.

  What has no ritual
  ------------------

  4 of the 53 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLegend is created at the first use, not by 'QLegend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLegend.
  - Qt tells when it has removed the C++ QLegend. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QLegend, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class MarkerShape(CuteNum):
    """
    The enum 'QLegend::MarkerShape' of Qt, with the 8 names Qt gives in it.
    """

    MarkerShapeDefault = Kee[int](0)
    MarkerShapeRectangle = Kee[int](1)
    MarkerShapeCircle = Kee[int](2)
    MarkerShapeFromSeries = Kee[int](3)
    MarkerShapeRotatedRectangle = Kee[int](4)
    MarkerShapeTriangle = Kee[int](5)
    MarkerShapeStar = Kee[int](6)
    MarkerShapePentagon = Kee[int](7)

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
    Calls Qt's 'QString QLegend::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#tr

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
    #  QString QLegend::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QLegend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLegend'

  #  A C++ QLegend Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLegend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLegend::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLegend::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QLegend10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QLegend::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QLegend::brush() const
    address = self.uglySide.call('ritual_ZNK7QLegend5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QLegend::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QLegend::pen() const
    address = self.uglySide.call('ritual_ZNK7QLegend3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QLegend::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QLegend::font() const
    address = self.uglySide.call('ritual_ZNK7QLegend4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def labelBrush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QLegend::labelBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#labelBrush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QLegend::labelBrush() const
    address = self.uglySide.call('ritual_ZNK7QLegend10labelBrushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def labelColor(self) -> QColor:
    """
    Calls Qt's 'QColor QLegend::labelColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#labelColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLegend::labelColor() const
    address = self.uglySide.call('ritual_ZNK7QLegend10labelColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QLegend::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QLegend::alignment() const
    return Qt.Alignment(self.uglySide.call('ritual_ZNK7QLegend9alignmentEv'))

  def isBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QLegend::isBackgroundVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#isBackgroundVisible
    """
    #  bool QLegend::isBackgroundVisible() const
    return self.uglySide.call('ritual_ZNK7QLegend19isBackgroundVisibleEv')

  @overload()
  @overload(QAbstractSeries)
  @overload(NoneType)
  def markers(
      self,
      series: Optional[QAbstractSeries] = None,
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *> QLegend::markers(QAbstractSeries
    *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#markers

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QLegendMarker]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLegendMarker *> QLegend::markers(QAbstractSeries *series) const
    address = self.uglySide.call(
        'ritual_ZNK7QLegend7markersEP15QAbstractSeries',
        self._addressOf(series),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  def showToolTips(self) -> bool:
    """
    Calls Qt's 'bool QLegend::showToolTips() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#showToolTips
    """
    #  bool QLegend::showToolTips() const
    return self.uglySide.call('ritual_ZNK7QLegend12showToolTipsEv')

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QLegend::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#isInteractive
    """
    #  bool QLegend::isInteractive() const
    return self.uglySide.call('ritual_ZNK7QLegend13isInteractiveEv')

  def markerShape(self) -> MarkerShape:
    """
    Calls Qt's 'MarkerShape QLegend::markerShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#markerShape

    Returns
    -------

    MarkerShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MarkerShape(number)'
      gives.
    """
    #  MarkerShape QLegend::markerShape() const
    return QLegend.MarkerShape(self.uglySide.call(
        'ritual_ZNK7QLegend11markerShapeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QLegend::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QLegend::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN7QLegend8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QLegend::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QLegend::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QLegend8setColorE6QColor', self._valueOf(color),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QLegend::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QLegend::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN7QLegend6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(QColor)
  def setBorderColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QLegend::setBorderColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setBorderColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QLegend::setBorderColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QLegend14setBorderColorE6QColor', self._valueOf(color),
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QLegend::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QLegend::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN7QLegend7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QBrush)
  def setLabelBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QLegend::setLabelBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setLabelBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QLegend::setLabelBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN7QLegend13setLabelBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QColor)
  def setLabelColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QLegend::setLabelColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setLabelColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QLegend::setLabelColor(QColor color)
    self.uglySide.call(
        'ritual_ZN7QLegend13setLabelColorE6QColor', self._valueOf(color),
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QLegend::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QLegend::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN7QLegend12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        alignment.value,
    )

  @overload()
  @overload(bool)
  def setBackgroundVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QLegend::setBackgroundVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QLegend::setBackgroundVisible(bool visible)
    self.uglySide.call('ritual_ZN7QLegend20setBackgroundVisibleEb', visible)

  @overload()
  @overload(bool)
  def setReverseMarkers(self, reverseMarkers: bool = True) -> None:
    """
    Calls Qt's 'void QLegend::setReverseMarkers(bool reverseMarkers)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setReverseMarkers

    Parameters
    ----------

    reverseMarkers : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QLegend::setReverseMarkers(bool reverseMarkers)
    self.uglySide.call(
        'ritual_ZN7QLegend17setReverseMarkersEb', reverseMarkers,
    )

  @overload(bool)
  def setShowToolTips(self, show: bool) -> None:
    """
    Calls Qt's 'void QLegend::setShowToolTips(bool show)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setShowToolTips

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QLegend::setShowToolTips(bool show)
    self.uglySide.call('ritual_ZN7QLegend15setShowToolTipsEb', show)

  @overload(bool)
  def setInteractive(self, interactive: bool) -> None:
    """
    Calls Qt's 'void QLegend::setInteractive(bool interactive)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setInteractive

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void QLegend::setInteractive(bool interactive)
    self.uglySide.call('ritual_ZN7QLegend14setInteractiveEb', interactive)

  @overload(MarkerShape)
  def setMarkerShape(self, shape: MarkerShape) -> None:
    """
    Calls Qt's 'void QLegend::setMarkerShape(MarkerShape shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#setMarkerShape

    Parameters
    ----------

    shape : MarkerShape
      Passed on as its number.
    """
    #  void QLegend::setMarkerShape(MarkerShape shape)
    self.uglySide.call(
        'ritual_ZN7QLegend14setMarkerShapeENS_11MarkerShapeE', shape.value,
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

  @overload(QChart)
  @overload(NoneType)
  def __init__(self, chart: Optional[QChart]) -> None:
    """
    Notes what was given, for Qt's 'QLegend::QLegend(QChart *chart)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#QLegend

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QLegend::QLegend(QChart *chart)
    self._noteCreation(QLegend, lambda: Rituals.call(
        'ritual_ZN7QLegendC1EP6QChart', self._addressOf(chart),
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
    Calls Qt's 'void QLegend::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#paint

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
    #  void QLegend::paint(QPainter *painter, const QStyleOptionGraphicsItem
    #      *option, QWidget *widget)
    ritual = (
        'ritual_ZN7QLegend5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QW'
        'idget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QLegend5paintEP8QPainterPK24QStyleOptionGraphicsIt'
          'emP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QLegend::color()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLegend::color()
    address = self.uglySide.call('ritual_ZN7QLegend5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def borderColor(self) -> QColor:
    """
    Calls Qt's 'QColor QLegend::borderColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#borderColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QLegend::borderColor()
    address = self.uglySide.call('ritual_ZN7QLegend11borderColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def detachFromChart(self) -> None:
    """
    Calls Qt's 'void QLegend::detachFromChart()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#detachFromChart
    """
    #  void QLegend::detachFromChart()
    self.uglySide.call('ritual_ZN7QLegend15detachFromChartEv')

  def attachToChart(self) -> None:
    """
    Calls Qt's 'void QLegend::attachToChart()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#attachToChart
    """
    #  void QLegend::attachToChart()
    self.uglySide.call('ritual_ZN7QLegend13attachToChartEv')

  def isAttachedToChart(self) -> bool:
    """
    Calls Qt's 'bool QLegend::isAttachedToChart()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#isAttachedToChart
    """
    #  bool QLegend::isAttachedToChart()
    return self.uglySide.call('ritual_ZN7QLegend17isAttachedToChartEv')

  def reverseMarkers(self) -> bool:
    """
    Calls Qt's 'bool QLegend::reverseMarkers()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#reverseMarkers
    """
    #  bool QLegend::reverseMarkers()
    return self.uglySide.call('ritual_ZN7QLegend14reverseMarkersEv')

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, event: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QLegend::hideEvent(QHideEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#hideEvent

    Parameters
    ----------

    event : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegend::hideEvent(QHideEvent *event)
    ritual = 'ritual_ZN7QLegend9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLegend9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QLegend::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegend::showEvent(QShowEvent *event)
    ritual = 'ritual_ZN7QLegend9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QLegend9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def backgroundVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QLegend::backgroundVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegend.html#backgroundVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QLegend::backgroundVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN7QLegend24backgroundVisibleChangedEb', visible,
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QLegend::colorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QLegend::colorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QLegend12colorChangedE6QColor', self._valueOf(color),
    )

  @overload(QColor)
  def borderColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QLegend::borderColorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#borderColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QLegend::borderColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QLegend18borderColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QLegend::fontChanged(QFont font)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QLegend::fontChanged(QFont font)
    self.uglySide.call(
        'ritual_ZN7QLegend11fontChangedE5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def labelColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QLegend::labelColorChanged(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#labelColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QLegend::labelColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN7QLegend17labelColorChangedE6QColor', self._valueOf(color),
    )

  @overload(bool)
  def reverseMarkersChanged(self, reverseMarkers: bool) -> None:
    """
    Calls Qt's 'void QLegend::reverseMarkersChanged(bool reverseMarkers)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#reverseMarkersChanged

    Parameters
    ----------

    reverseMarkers : bool
      Passed on as it is.
    """
    #  void QLegend::reverseMarkersChanged(bool reverseMarkers)
    self.uglySide.call(
        'ritual_ZN7QLegend21reverseMarkersChangedEb', reverseMarkers,
    )

  @overload(bool)
  def showToolTipsChanged(self, showToolTips: bool) -> None:
    """
    Calls Qt's 'void QLegend::showToolTipsChanged(bool showToolTips)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#showToolTipsChanged

    Parameters
    ----------

    showToolTips : bool
      Passed on as it is.
    """
    #  void QLegend::showToolTipsChanged(bool showToolTips)
    self.uglySide.call(
        'ritual_ZN7QLegend19showToolTipsChangedEb', showToolTips,
    )

  @overload(MarkerShape)
  def markerShapeChanged(self, shape: MarkerShape) -> None:
    """
    Calls Qt's 'void QLegend::markerShapeChanged(MarkerShape shape)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#markerShapeChanged

    Parameters
    ----------

    shape : MarkerShape
      Passed on as its number.
    """
    #  void QLegend::markerShapeChanged(MarkerShape shape)
    self.uglySide.call(
        'ritual_ZN7QLegend18markerShapeChangedENS_11MarkerShapeE',
        shape.value,
    )

  @overload(bool)
  def attachedToChartChanged(self, attachedToChart: bool) -> None:
    """
    Calls Qt's 'void QLegend::attachedToChartChanged(bool attachedToChart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegend.html#attachedToChartChanged

    Parameters
    ----------

    attachedToChart : bool
      Passed on as it is.
    """
    #  void QLegend::attachedToChartChanged(bool attachedToChart)
    self.uglySide.call(
        'ritual_ZN7QLegend22attachedToChartChangedEb', attachedToChart,
    )

  @overload(bool)
  def interactiveChanged(self, interactive: bool) -> None:
    """
    Calls Qt's 'void QLegend::interactiveChanged(bool interactive)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegend.html#interactiveChanged

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void QLegend::interactiveChanged(bool interactive)
    self.uglySide.call(
        'ritual_ZN7QLegend18interactiveChangedEb', interactive,
    )
