"""
ChartAxisElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartaxiselement_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ChartAxisElement to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from ..QtWidgets import QGraphicsItem, QGraphicsLayoutItem
from . import ChartElement, QValueAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDateTime, QMetaObject, QRectF
  from ..QtGui import QBrush, QColor, QFont, QPainter, QPen
  from ..QtWidgets import QGraphicsItemGroup, QGraphicsPixmapItem
  from ..QtWidgets import QGraphicsTextItem, QStyleOptionGraphicsItem
  from ..QtWidgets import QWidget
  from . import AxisAnimation, QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AxisAnimation = WAIT['AxisAnimation']
  QBrush = WAIT['QBrush']
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QDateTime = WAIT['QDateTime']
  QFont = WAIT['QFont']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QRectF = WAIT['QRectF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartAxisElement(ChartElement, QGraphicsLayoutItem):
  """
  The cute side of Qt's ChartAxisElement: a plain Python object standing in
  front of one C++ ChartAxisElement.

  It is built on the cute 'ChartElement', as Qt's ChartAxisElement is built
  on Qt's ChartElement, and has everything that class has. It is built on the
  cute 'QGraphicsLayoutItem' as well, as Qt's ChartAxisElement is built on
  Qt's QGraphicsLayoutItem too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartAxisElement that has a ritual and that Python
  can call so far, 78 names in all: 'metaObject', 'tr', 'gridGeometry',
  'setGeometry', 'emptyAxis', 'setAnimation', 'animation', 'axis',
  'labelPadding', 'titlePadding', 'colorScalePadding', 'setLabels', 'labels',
  'min', 'max', 'tickInterval', 'tickAnchor', 'axisGeometry',
  'setAxisGeometry', 'axisSelected', 'intervalAxis', 'createValueLabels',
  'createLogValueLabels', 'createDateTimeLabels', 'createColorLabels',
  'boundingRect', 'paint', 'labelsEditable', 'setLabelsEditable',
  'labelsVisible', 'gridItems', 'minorGridItems', 'labelItems', 'shadeItems',
  'arrowItems', 'minorArrowItems', 'titleItem', 'colorScaleItem',
  'gridGroup', 'minorGridGroup', 'labelGroup', 'shadeGroup', 'arrowGroup',
  'minorArrowGroup', 'prepareColorScale', 'handleVisibleChanged',
  'handleArrowVisibleChanged', 'handleGridVisibleChanged',
  'handleLabelsVisibleChanged', 'handleShadesVisibleChanged',
  'handleLabelsAngleChanged', 'handleShadesBrushChanged',
  'handleShadesPenChanged', 'handleArrowPenChanged', 'handleGridPenChanged',
  'handleMinorArrowPenChanged', 'handleMinorGridPenChanged',
  'handleMinorGridLineColorChanged', 'handleGridLineColorChanged',
  'handleLabelsBrushChanged', 'handleLabelsFontChanged',
  'handleTitleBrushChanged', 'handleTitleFontChanged',
  'handleTitleTextChanged', 'handleTitleVisibleChanged',
  'handleRangeChanged', 'handleReverseChanged',
  'handleMinorArrowVisibleChanged', 'handleMinorGridVisibleChanged',
  'handleLabelsPositionChanged', 'handleTruncateLabelsChanged',
  'handleColorScaleSizeChanged', 'handleColorScaleGradientChanged',
  'valueLabelEdited', 'dateTimeLabelEdited', 'clicked', 'connectSlots',
  'formatLabel'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartAxisElement::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int ChartAxisElement::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'ChartAxisElement::~ChartAxisElement()': the destructor: Python
    never removes a C++ ChartAxisElement.
  - Qt's 'void ChartAxisElement::setLayout(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<qreal> &ChartAxisElement::layout()': gives a type Python has
    no way to take yet.
  - Qt's 'void ChartAxisElement::setDynamicMinorTickLayout(const QList<qreal>
    &layout)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<qreal> &ChartAxisElement::dynamicMinorTicklayout()': gives a
    type Python has no way to take yet.
  - Qt's 'QList<qreal> ChartAxisElement::calculateLayout() const': gives a
    type Python has no way to take yet.
  - Qt's 'void ChartAxisElement::updateLayout(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 90 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ ChartAxisElement is created at the first use, not by
    'ChartAxisElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartAxisElement.
  - Qt tells when it has removed the C++ ChartAxisElement. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ChartAxisElement that has no cute function yet,
    '__init__', 'calculateLayout', 'dynamicMinorTicklayout', 'layout',
    'setDynamicMinorTickLayout', 'setLayout', 'updateLayout', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString ChartAxisElement::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#tr

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
    #  QString ChartAxisElement::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16ChartAxisElement2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartAxisElement'

  #  Qt's ChartAxisElement is built on more than one class. The part of a C++
  #  ChartAxisElement that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGraphicsLayoutItem':
          'ritual_cast_ChartAxisElement_QGraphicsLayoutItem',
  }

  #  A C++ ChartAxisElement Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartAxisElement'

  #  The functions Qt calls itself that ChartAxisElement is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'calculateLayout': (
          'QList<qreal> ChartAxisElement::calculateLayout() const',
      ),
      'updateLayout': (
          'void ChartAxisElement::updateLayout(const QList<qreal> &)',
      ),
  }

  #  The functions Qt calls itself that ChartAxisElement is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'gridGeometry': (
          ('_ZNK16ChartAxisElement12gridGeometryEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'setGeometry': (
          ('_ZN16ChartAxisElement11setGeometryERK6QRectFS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'emptyAxis': (
          ('_ZNK16ChartAxisElement9emptyAxisEv',
           ('bool', 'number', ''),
           ()),
      ),
      'handleShadesBrushChanged': (
          ('_ZN16ChartAxisElement24handleShadesBrushChangedERK6QBrush',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QBrush'),
           )),
      ),
      'handleShadesPenChanged': (
          ('_ZN16ChartAxisElement22handleShadesPenChangedERK4QPen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPen'),
           )),
      ),
      'handleArrowPenChanged': (
          ('_ZN16ChartAxisElement21handleArrowPenChangedERK4QPen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPen'),
           )),
      ),
      'handleGridPenChanged': (
          ('_ZN16ChartAxisElement20handleGridPenChangedERK4QPen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPen'),
           )),
      ),
      'handleMinorArrowPenChanged': (
          ('_ZN16ChartAxisElement26handleMinorArrowPenChangedERK4QPen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPen'),
           )),
      ),
      'handleMinorGridPenChanged': (
          ('_ZN16ChartAxisElement25handleMinorGridPenChangedERK4QPen',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPen'),
           )),
      ),
      'handleMinorGridLineColorChanged': (
          ('_ZN16ChartAxisElement31handleMinorGridLineColorChangedERK6QColo'
           'r',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'handleGridLineColorChanged': (
          ('_ZN16ChartAxisElement26handleGridLineColorChangedERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartAxisElement::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartAxisElement::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def gridGeometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF ChartAxisElement::gridGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#gridGeometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF ChartAxisElement::gridGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement12gridGeometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def emptyAxis(self) -> bool:
    """
    Calls Qt's 'bool ChartAxisElement::emptyAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#emptyAxis
    """
    #  bool ChartAxisElement::emptyAxis() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement9emptyAxisEv')

  def animation(self) -> Optional[AxisAnimation]:
    """
    Calls Qt's 'AxisAnimation *ChartAxisElement::animation() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#animation

    Returns
    -------

    Optional[AxisAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AxisAnimation *ChartAxisElement::animation() const
    ritual = 'ritual_ZNK16ChartAxisElement9animationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16ChartAxisElement9animationEv'
    address = self.uglySide.call(ritual)
    from . import AxisAnimation
    return AxisAnimation._cuteAt(address)

  def axis(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *ChartAxisElement::axis() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#axis

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *ChartAxisElement::axis() const
    address = self.uglySide.call('ritual_ZNK16ChartAxisElement4axisEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def labelPadding(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::labelPadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#labelPadding
    """
    #  qreal ChartAxisElement::labelPadding() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement12labelPaddingEv')

  def titlePadding(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::titlePadding() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#titlePadding
    """
    #  qreal ChartAxisElement::titlePadding() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement12titlePaddingEv')

  def colorScalePadding(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::colorScalePadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#colorScalePadding
    """
    #  qreal ChartAxisElement::colorScalePadding() const
    return self.uglySide.call(
        'ritual_ZNK16ChartAxisElement17colorScalePaddingEv',
    )

  def labels(self) -> QStringList:
    """
    Calls Qt's 'QStringList ChartAxisElement::labels() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#labels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList ChartAxisElement::labels() const
    address = self.uglySide.call('ritual_ZNK16ChartAxisElement6labelsEv')
    return QStringList._cuteOwning(address)

  def min(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#min
    """
    #  qreal ChartAxisElement::min() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#max
    """
    #  qreal ChartAxisElement::max() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement3maxEv')

  def tickInterval(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::tickInterval() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#tickInterval
    """
    #  qreal ChartAxisElement::tickInterval() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement12tickIntervalEv')

  def tickAnchor(self) -> float:
    """
    Calls Qt's 'qreal ChartAxisElement::tickAnchor() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#tickAnchor
    """
    #  qreal ChartAxisElement::tickAnchor() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement10tickAnchorEv')

  def axisGeometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF ChartAxisElement::axisGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#axisGeometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF ChartAxisElement::axisGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement12axisGeometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def intervalAxis(self) -> bool:
    """
    Calls Qt's 'bool ChartAxisElement::intervalAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#intervalAxis
    """
    #  bool ChartAxisElement::intervalAxis() const
    return self.uglySide.call('ritual_ZNK16ChartAxisElement12intervalAxisEv')

  @overload(float, float, int, float, float, QValueAxis.TickType, str)
  def createValueLabels(
      self,
      max: float,
      min: float,
      ticks: int,
      tickInterval: float,
      tickAnchor: float,
      tickType: QValueAxis.TickType,
      format: str,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList ChartAxisElement::createValueLabels(qreal max,
    qreal min, int ticks, qreal tickInterval, qreal tickAnchor,
    QValueAxis::TickType tickType, const QString &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#createValueLabels

    Parameters
    ----------

    max : float
      Passed on as it is.

    min : float
      Passed on as it is.

    ticks : int
      Passed on as it is.

    tickInterval : float
      Passed on as it is.

    tickAnchor : float
      Passed on as it is.

    tickType : QValueAxis.TickType
      Passed on as its number.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList ChartAxisElement::createValueLabels(qreal max, qreal min,
    #      int ticks, qreal tickInterval, qreal tickAnchor,
    #      QValueAxis::TickType tickType, const QString &format) const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement17createValueLabelsEddiddN10QValueAxis'
        '8TickTypeERK7QString',
        max, min, ticks, tickInterval, tickAnchor, tickType.value, format,
    )
    return QStringList._cuteOwning(address)

  @overload(float, float, float, int, str)
  def createLogValueLabels(
      self,
      min: float,
      max: float,
      base: float,
      ticks: int,
      format: str,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList ChartAxisElement::createLogValueLabels(qreal min,
    qreal max, qreal base, int ticks, const QString &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#createLogValueLabels

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.

    base : float
      Passed on as it is.

    ticks : int
      Passed on as it is.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList ChartAxisElement::createLogValueLabels(qreal min, qreal
    #      max, qreal base, int ticks, const QString &format) const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement20createLogValueLabelsEdddiRK7QString',
        min, max, base, ticks, format,
    )
    return QStringList._cuteOwning(address)

  @overload(float, float, int, str)
  def createDateTimeLabels(
      self,
      max: float,
      min: float,
      ticks: int,
      format: str,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList ChartAxisElement::createDateTimeLabels(qreal max,
    qreal min, int ticks, const QString &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#createDateTimeLabels

    Parameters
    ----------

    max : float
      Passed on as it is.

    min : float
      Passed on as it is.

    ticks : int
      Passed on as it is.

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList ChartAxisElement::createDateTimeLabels(qreal max, qreal
    #      min, int ticks, const QString &format) const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement20createDateTimeLabelsEddiRK7QString',
        max, min, ticks, format,
    )
    return QStringList._cuteOwning(address)

  @overload(float, float, int)
  def createColorLabels(
      self,
      min: float,
      max: float,
      ticks: int,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList ChartAxisElement::createColorLabels(qreal min,
    qreal max, int ticks) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#createColorLabels

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.

    ticks : int
      Passed on as it is.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList ChartAxisElement::createColorLabels(qreal min, qreal max,
    #      int ticks) const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement17createColorLabelsEddi',
        min, max, ticks,
    )
    return QStringList._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF ChartAxisElement::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF ChartAxisElement::boundingRect() const
    ritual = 'ritual_ZNK16ChartAxisElement12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16ChartAxisElement12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def labelsEditable(self) -> bool:
    """
    Calls Qt's 'bool ChartAxisElement::labelsEditable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#labelsEditable
    """
    #  bool ChartAxisElement::labelsEditable() const
    return self.uglySide.call(
        'ritual_ZNK16ChartAxisElement14labelsEditableEv',
    )

  def labelsVisible(self) -> bool:
    """
    Calls Qt's 'bool ChartAxisElement::labelsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#labelsVisible
    """
    #  bool ChartAxisElement::labelsVisible() const
    return self.uglySide.call(
        'ritual_ZNK16ChartAxisElement13labelsVisibleEv',
    )

  def titleItem(self) -> Optional[QGraphicsTextItem]:
    """
    Calls Qt's 'QGraphicsTextItem *ChartAxisElement::titleItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#titleItem

    Returns
    -------

    Optional[QGraphicsTextItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsTextItem *ChartAxisElement::titleItem() const
    address = self.uglySide.call('ritual_ZNK16ChartAxisElement9titleItemEv')
    from ..QtWidgets import QGraphicsTextItem
    return QGraphicsTextItem._cuteAt(address)

  def colorScaleItem(self) -> Optional[QGraphicsPixmapItem]:
    """
    Calls Qt's 'QGraphicsPixmapItem *ChartAxisElement::colorScaleItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#colorScaleItem

    Returns
    -------

    Optional[QGraphicsPixmapItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsPixmapItem *ChartAxisElement::colorScaleItem() const
    address = self.uglySide.call(
        'ritual_ZNK16ChartAxisElement14colorScaleItemEv',
    )
    from ..QtWidgets import QGraphicsPixmapItem
    return QGraphicsPixmapItem._cuteAt(address)

  @overload(str, QByteArray, float, int, str, str)
  def formatLabel(
      self,
      formatSpec: str,
      array: QByteArray,
      value: float,
      precision: int,
      preStr: str,
      postStr: str,
  ) -> str:
    """
    Calls Qt's 'QString ChartAxisElement::formatLabel(const QString
    &formatSpec, const QByteArray &array, qreal value, int precision, const
    QString &preStr, const QString &postStr) const'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#formatLabel

    Parameters
    ----------

    formatSpec : str
      Passed on as it is: a QString is made of it for the call.

    array : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : float
      Passed on as it is.

    precision : int
      Passed on as it is.

    preStr : str
      Passed on as it is: a QString is made of it for the call.

    postStr : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString ChartAxisElement::formatLabel(const QString &formatSpec, const
    #      QByteArray &array, qreal value, int precision, const QString
    #      &preStr, const QString &postStr) const
    return self.uglySide.call(
        'ritual_ZNK16ChartAxisElement11formatLabelERK7QStringRK10QByteArray'
        'diS2_S2_',
        formatSpec, self._valueOf(array), value, precision, preStr, postStr,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF, QRectF)
  def setGeometry(self, axis: QRectF, grid: QRectF) -> None:
    """
    Calls Qt's 'void ChartAxisElement::setGeometry(const QRectF &axis, const
    QRectF &grid)'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#setGeometry

    Parameters
    ----------

    axis : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    grid : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartAxisElement::setGeometry(const QRectF &axis, const QRectF
    #      &grid)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement11setGeometryERK6QRectFS2_',
        self._valueOf(axis), self._valueOf(grid),
    )

  @overload(AxisAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[AxisAnimation]) -> None:
    """
    Calls Qt's 'void ChartAxisElement::setAnimation(AxisAnimation
    *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#setAnimation

    Parameters
    ----------

    animation : Optional[AxisAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartAxisElement::setAnimation(AxisAnimation *animation)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement12setAnimationEP13AxisAnimation',
        self._addressOf(animation),
    )

  @overload(QStringList)
  def setLabels(self, labels: QStringList) -> None:
    """
    Calls Qt's 'void ChartAxisElement::setLabels(const QStringList &labels)'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#setLabels

    Parameters
    ----------

    labels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ChartAxisElement::setLabels(const QStringList &labels)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement9setLabelsERK5QListI7QStringE',
        self._valueOf(labels),
    )

  @overload(QRectF)
  def setAxisGeometry(self, axisGeometry: QRectF) -> None:
    """
    Calls Qt's 'void ChartAxisElement::setAxisGeometry(const QRectF
    &axisGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#setAxisGeometry

    Parameters
    ----------

    axisGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartAxisElement::setAxisGeometry(const QRectF &axisGeometry)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement15setAxisGeometryERK6QRectF',
        self._valueOf(axisGeometry),
    )

  @overload(bool)
  def setLabelsEditable(self, labelsEditable: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::setLabelsEditable(bool
    labelsEditable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#setLabelsEditable

    Parameters
    ----------

    labelsEditable : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::setLabelsEditable(bool labelsEditable)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement17setLabelsEditableEb', labelsEditable,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'ChartAxisElement::ChartAxisElement(QAbstractAxis *axis,
    QGraphicsItem *item, bool intervalAxis)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'ChartAxisElement.__init__' has no cute function yet. Qt's "
        "'ChartAxisElement::ChartAxisElement(QAbstractAxis *axis, "
        "QGraphicsItem *item, bool intervalAxis)': the class is abstract, "
        "so C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  def axisSelected(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::axisSelected()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#axisSelected
    """
    #  void ChartAxisElement::axisSelected()
    self.uglySide.call('ritual_ZN16ChartAxisElement12axisSelectedEv')

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
      a0: Optional[QPainter],
      a1: Optional[QStyleOptionGraphicsItem],
      a2: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void ChartAxisElement::paint(QPainter *a0, const
    QStyleOptionGraphicsItem *a1, QWidget *a2)'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#paint

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartAxisElement::paint(QPainter *a0, const
    #      QStyleOptionGraphicsItem *a1, QWidget *a2)
    ritual = (
        'ritual_ZN16ChartAxisElement5paintEP8QPainterPK24QStyleOptionGraphi'
        'csItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ChartAxisElement5paintEP8QPainterPK24QStyleOption'
          'GraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(a0), self._addressOf(a1), self._addressOf(a2),
    )

  def gridItems(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> ChartAxisElement::gridItems()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#gridItems

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> ChartAxisElement::gridItems()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement9gridItemsEv')
    return QList[QGraphicsItem]._cuteOwning(address)

  def minorGridItems(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> ChartAxisElement::minorGridItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#minorGridItems

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> ChartAxisElement::minorGridItems()
    address = self.uglySide.call(
        'ritual_ZN16ChartAxisElement14minorGridItemsEv',
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  def labelItems(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> ChartAxisElement::labelItems()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#labelItems

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> ChartAxisElement::labelItems()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement10labelItemsEv')
    return QList[QGraphicsItem]._cuteOwning(address)

  def shadeItems(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> ChartAxisElement::shadeItems()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#shadeItems

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> ChartAxisElement::shadeItems()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement10shadeItemsEv')
    return QList[QGraphicsItem]._cuteOwning(address)

  def arrowItems(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> ChartAxisElement::arrowItems()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#arrowItems

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> ChartAxisElement::arrowItems()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement10arrowItemsEv')
    return QList[QGraphicsItem]._cuteOwning(address)

  def minorArrowItems(self) -> QList[QGraphicsItem]:
    """
    Calls Qt's 'QList<QGraphicsItem *> ChartAxisElement::minorArrowItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#minorArrowItems

    Returns
    -------

    QList[QGraphicsItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGraphicsItem *> ChartAxisElement::minorArrowItems()
    address = self.uglySide.call(
        'ritual_ZN16ChartAxisElement15minorArrowItemsEv',
    )
    return QList[QGraphicsItem]._cuteOwning(address)

  def gridGroup(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *ChartAxisElement::gridGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#gridGroup

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *ChartAxisElement::gridGroup()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement9gridGroupEv')
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  def minorGridGroup(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *ChartAxisElement::minorGridGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#minorGridGroup

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *ChartAxisElement::minorGridGroup()
    address = self.uglySide.call(
        'ritual_ZN16ChartAxisElement14minorGridGroupEv',
    )
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  def labelGroup(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *ChartAxisElement::labelGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#labelGroup

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *ChartAxisElement::labelGroup()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement10labelGroupEv')
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  def shadeGroup(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *ChartAxisElement::shadeGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#shadeGroup

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *ChartAxisElement::shadeGroup()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement10shadeGroupEv')
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  def arrowGroup(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *ChartAxisElement::arrowGroup()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#arrowGroup

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *ChartAxisElement::arrowGroup()
    address = self.uglySide.call('ritual_ZN16ChartAxisElement10arrowGroupEv')
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  def minorArrowGroup(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *ChartAxisElement::minorArrowGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#minorArrowGroup

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *ChartAxisElement::minorArrowGroup()
    address = self.uglySide.call(
        'ritual_ZN16ChartAxisElement15minorArrowGroupEv',
    )
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  @overload(float, float)
  def prepareColorScale(self, width: float, height: float) -> None:
    """
    Calls Qt's 'void ChartAxisElement::prepareColorScale(const qreal width,
    const qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#prepareColorScale

    Parameters
    ----------

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void ChartAxisElement::prepareColorScale(const qreal width, const
    #      qreal height)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement17prepareColorScaleEdd', width, height,
    )

  @overload(bool)
  def handleVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement20handleVisibleChangedEb', visible,
    )

  @overload(bool)
  def handleArrowVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleArrowVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleArrowVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleArrowVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement25handleArrowVisibleChangedEb', visible,
    )

  @overload(bool)
  def handleGridVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleGridVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleGridVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleGridVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement24handleGridVisibleChangedEb', visible,
    )

  @overload(bool)
  def handleLabelsVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleLabelsVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleLabelsVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleLabelsVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement26handleLabelsVisibleChangedEb', visible,
    )

  @overload(bool)
  def handleShadesVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleShadesVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleShadesVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleShadesVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement26handleShadesVisibleChangedEb', visible,
    )

  @overload(int)
  def handleLabelsAngleChanged(self, angle: int) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleLabelsAngleChanged(int angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleLabelsAngleChanged

    Parameters
    ----------

    angle : int
      Passed on as it is.
    """
    #  void ChartAxisElement::handleLabelsAngleChanged(int angle)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement24handleLabelsAngleChangedEi', angle,
    )

  @overload(QBrush)
  def handleShadesBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleShadesBrushChanged(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleShadesBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ChartAxisElement::handleShadesBrushChanged(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement24handleShadesBrushChangedERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def handleShadesPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleShadesPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleShadesPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartAxisElement::handleShadesPenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement22handleShadesPenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QPen)
  def handleArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleArrowPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleArrowPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartAxisElement::handleArrowPenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement21handleArrowPenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QPen)
  def handleGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleGridPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleGridPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartAxisElement::handleGridPenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement20handleGridPenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QPen)
  def handleMinorArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleMinorArrowPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleMinorArrowPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartAxisElement::handleMinorArrowPenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement26handleMinorArrowPenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QPen)
  def handleMinorGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleMinorGridPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleMinorGridPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void ChartAxisElement::handleMinorGridPenChanged(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement25handleMinorGridPenChangedERK4QPen',
        self._valueOf(pen),
    )

  @overload(QColor)
  def handleMinorGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleMinorGridLineColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ChartAxisElement::handleMinorGridLineColorChanged(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement31handleMinorGridLineColorChangedERK6QC'
        'olor',
        self._valueOf(color),
    )

  @overload(QColor)
  def handleGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleGridLineColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleGridLineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void ChartAxisElement::handleGridLineColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement26handleGridLineColorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(QBrush)
  def handleLabelsBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleLabelsBrushChanged(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleLabelsBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ChartAxisElement::handleLabelsBrushChanged(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement24handleLabelsBrushChangedERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QFont)
  def handleLabelsFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleLabelsFontChanged(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleLabelsFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void ChartAxisElement::handleLabelsFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement23handleLabelsFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QBrush)
  def handleTitleBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleTitleBrushChanged(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleTitleBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void ChartAxisElement::handleTitleBrushChanged(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement23handleTitleBrushChangedERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QFont)
  def handleTitleFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleTitleFontChanged(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleTitleFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void ChartAxisElement::handleTitleFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement22handleTitleFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(str)
  def handleTitleTextChanged(self, title: str) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleTitleTextChanged(const QString
    &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleTitleTextChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ChartAxisElement::handleTitleTextChanged(const QString &title)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement22handleTitleTextChangedERK7QString',
        title,
    )

  @overload(bool)
  def handleTitleVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleTitleVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleTitleVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleTitleVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement25handleTitleVisibleChangedEb', visible,
    )

  @overload(float, float)
  def handleRangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleRangeChanged(qreal min, qreal
    max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleRangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void ChartAxisElement::handleRangeChanged(qreal min, qreal max)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement18handleRangeChangedEdd', min, max,
    )

  @overload(bool)
  def handleReverseChanged(self, reverse: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleReverseChanged(bool reverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleReverseChanged

    Parameters
    ----------

    reverse : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleReverseChanged(bool reverse)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement20handleReverseChangedEb', reverse,
    )

  @overload(bool)
  def handleMinorArrowVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleMinorArrowVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleMinorArrowVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement30handleMinorArrowVisibleChangedEb',
        visible,
    )

  @overload(bool)
  def handleMinorGridVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleMinorGridVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ChartAxisElement::handleMinorGridVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement29handleMinorGridVisibleChangedEb',
        visible,
    )

  def handleLabelsPositionChanged(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleLabelsPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleLabelsPositionChanged
    """
    #  void ChartAxisElement::handleLabelsPositionChanged()
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement27handleLabelsPositionChangedEv',
    )

  def handleTruncateLabelsChanged(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleTruncateLabelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleTruncateLabelsChanged
    """
    #  void ChartAxisElement::handleTruncateLabelsChanged()
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement27handleTruncateLabelsChangedEv',
    )

  def handleColorScaleSizeChanged(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleColorScaleSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#handleColorScaleSizeChanged
    """
    #  void ChartAxisElement::handleColorScaleSizeChanged()
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement27handleColorScaleSizeChangedEv',
    )

  def handleColorScaleGradientChanged(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::handleColorScaleGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html
    """
    #  void ChartAxisElement::handleColorScaleGradientChanged()
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement31handleColorScaleGradientChangedEv',
    )

  @overload(float, float)
  def valueLabelEdited(self, oldValue: float, newValue: float) -> None:
    """
    Calls Qt's 'void ChartAxisElement::valueLabelEdited(qreal oldValue, qreal
    newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#valueLabelEdited

    Parameters
    ----------

    oldValue : float
      Passed on as it is.

    newValue : float
      Passed on as it is.
    """
    #  void ChartAxisElement::valueLabelEdited(qreal oldValue, qreal
    #      newValue)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement16valueLabelEditedEdd',
        oldValue, newValue,
    )

  @overload(QDateTime, QDateTime)
  def dateTimeLabelEdited(
      self,
      oldTime: QDateTime,
      newTime: QDateTime,
  ) -> None:
    """
    Calls Qt's 'void ChartAxisElement::dateTimeLabelEdited(const QDateTime
    &oldTime, const QDateTime &newTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartaxiselement.html#dateTimeLabelEdited

    Parameters
    ----------

    oldTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    newTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void ChartAxisElement::dateTimeLabelEdited(const QDateTime &oldTime,
    #      const QDateTime &newTime)
    self.uglySide.call(
        'ritual_ZN16ChartAxisElement19dateTimeLabelEditedERK9QDateTimeS2_',
        self._valueOf(oldTime), self._valueOf(newTime),
    )

  def clicked(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::clicked()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#clicked
    """
    #  void ChartAxisElement::clicked()
    self.uglySide.call('ritual_ZN16ChartAxisElement7clickedEv')

  def connectSlots(self) -> None:
    """
    Calls Qt's 'void ChartAxisElement::connectSlots()'.

    Qt's own words: https://doc.qt.io/qt-6/chartaxiselement.html#connectSlots
    """
    #  void ChartAxisElement::connectSlots()
    self.uglySide.call('ritual_ZN16ChartAxisElement12connectSlotsEv')

  @staticmethod
  def calculateLayout(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> ChartAxisElement::calculateLayout() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ChartAxisElement.calculateLayout' has no cute function yet. Qt's "
        "'QList<qreal> ChartAxisElement::calculateLayout() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def dynamicMinorTicklayout(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> &ChartAxisElement::dynamicMinorTicklayout()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ChartAxisElement.dynamicMinorTicklayout' has no cute function "
        "yet. Qt's 'QList<qreal> "
        "&ChartAxisElement::dynamicMinorTicklayout()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def layout(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> &ChartAxisElement::layout()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'ChartAxisElement.layout' has no cute function yet. Qt's "
        "'QList<qreal> &ChartAxisElement::layout()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setDynamicMinorTickLayout(*__, **_) -> Never:
    """
    Qt's 'void ChartAxisElement::setDynamicMinorTickLayout(const QList<qreal>
    &layout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ChartAxisElement.setDynamicMinorTickLayout' has no cute function "
        "yet. Qt's 'void ChartAxisElement::setDynamicMinorTickLayout(const "
        "QList<qreal> &layout)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setLayout(*__, **_) -> Never:
    """
    Qt's 'void ChartAxisElement::setLayout(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ChartAxisElement.setLayout' has no cute function yet. Qt's 'void "
        "ChartAxisElement::setLayout(const QList<qreal> &layout)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def updateLayout(*__, **_) -> Never:
    """
    Qt's 'void ChartAxisElement::updateLayout(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ChartAxisElement.updateLayout' has no cute function yet. Qt's "
        "'void ChartAxisElement::updateLayout(const QList<qreal> &layout)': "
        "takes a type Python has no way to hand over yet.")


#  Qt's 'QList<ChartAxisElement *>': the list of ChartAxisElement, which
#  'QList[ChartAxisElement]' gives. It is made here, so that there is one as
#  soon as there can be a ChartAxisElement.
QList.createKind(
    ChartAxisElement, 'address',
    make='ritual_list_make_ChartAxisElement_ptr',
    add='ritual_list_add_ChartAxisElement_ptr',
    size='ritual_list_size_ChartAxisElement_ptr',
    at='ritual_list_at_ChartAxisElement_ptr',
    drop='ritual_list_drop_ChartAxisElement_ptr',
)
