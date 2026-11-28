"""
BoxPlotChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/boxplotchartitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means BoxPlotChartItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QGraphicsItem
from . import ChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import BoxPlotAnimation, BoxWhiskers, QBoxPlotSeries, QBoxSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BoxPlotAnimation = WAIT['BoxPlotAnimation']
  BoxWhiskers = WAIT['BoxWhiskers']
  QBoxPlotSeries = WAIT['QBoxPlotSeries']
  QBoxSet = WAIT['QBoxSet']
  QPainter = WAIT['QPainter']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoxPlotChartItem(ChartItem):
  """
  The cute side of Qt's BoxPlotChartItem: a plain Python object standing in
  front of one C++ BoxPlotChartItem.

  It is built on the cute 'ChartItem', as Qt's BoxPlotChartItem is built on
  Qt's ChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's BoxPlotChartItem that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'setAnimation',
  'paint', 'boundingRect', 'handleSeriesVisibleChanged',
  'handleOpacityChanged', 'handleDataStructureChanged',
  'handleDomainUpdated', 'handleLayoutChanged', 'handleUpdatedBars',
  'handleBoxsetRemove', 'calculateLayout', 'initializeLayout',
  'updateBoxGeometry'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BoxPlotChartItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int BoxPlotChartItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'BoxPlotChartItem::~BoxPlotChartItem()': the destructor: Python
    never removes a C++ BoxPlotChartItem.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ BoxPlotChartItem is created at the first use, not by
    'BoxPlotChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BoxPlotChartItem.
  - Qt tells when it has removed the C++ BoxPlotChartItem. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString BoxPlotChartItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotchartitem.html#tr

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
    #  QString BoxPlotChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16BoxPlotChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BoxPlotChartItem'

  #  A C++ BoxPlotChartItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BoxPlotChartItem'

  #  The functions Qt calls itself that BoxPlotChartItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'calculateLayout': (
          'QList<QRectF> BoxPlotChartItem::calculateLayout()',
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
    Calls Qt's 'const QMetaObject *BoxPlotChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotchartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BoxPlotChartItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16BoxPlotChartItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF BoxPlotChartItem::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotchartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF BoxPlotChartItem::boundingRect() const
    ritual = 'ritual_ZNK16BoxPlotChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16BoxPlotChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BoxPlotAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[BoxPlotAnimation]) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::setAnimation(BoxPlotAnimation
    *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotchartitem.html#setAnimation

    Parameters
    ----------

    animation : Optional[BoxPlotAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxPlotChartItem::setAnimation(BoxPlotAnimation *animation)
    self.uglySide.call(
        'ritual_ZN16BoxPlotChartItem12setAnimationEP16BoxPlotAnimation',
        self._addressOf(animation),
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

  @overload(QBoxPlotSeries)
  @overload(NoneType)
  @overload(QBoxPlotSeries, QGraphicsItem)
  @overload(QBoxPlotSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QBoxPlotSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'BoxPlotChartItem::BoxPlotChartItem(QBoxPlotSeries *series, QGraphicsItem
    *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#BoxPlotChartItem

    Parameters
    ----------

    series : Optional[QBoxPlotSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  BoxPlotChartItem::BoxPlotChartItem(QBoxPlotSeries *series,
    #      QGraphicsItem *item)
    self._noteCreation(BoxPlotChartItem, lambda: Rituals.call(
        'ritual_ZN16BoxPlotChartItemC1EP14QBoxPlotSeriesP13QGraphicsItem',
        self._addressOf(series), self._addressOf(item, 'QGraphicsItem'),
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
    Calls Qt's 'void BoxPlotChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/boxplotchartitem.html#paint

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
    #  void BoxPlotChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN16BoxPlotChartItem5paintEP8QPainterPK24QStyleOptionGraphi'
        'csItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16BoxPlotChartItem5paintEP8QPainterPK24QStyleOption'
          'GraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def handleSeriesVisibleChanged(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleSeriesVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleSeriesVisibleChanged
    """
    #  void BoxPlotChartItem::handleSeriesVisibleChanged()
    self.uglySide.call(
        'ritual_ZN16BoxPlotChartItem26handleSeriesVisibleChangedEv',
    )

  def handleOpacityChanged(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleOpacityChanged
    """
    #  void BoxPlotChartItem::handleOpacityChanged()
    self.uglySide.call('ritual_ZN16BoxPlotChartItem20handleOpacityChangedEv')

  def handleDataStructureChanged(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleDataStructureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleDataStructureChanged
    """
    #  void BoxPlotChartItem::handleDataStructureChanged()
    self.uglySide.call(
        'ritual_ZN16BoxPlotChartItem26handleDataStructureChangedEv',
    )

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleDomainUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleDomainUpdated
    """
    #  void BoxPlotChartItem::handleDomainUpdated()
    ritual = 'ritual_ZN16BoxPlotChartItem19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16BoxPlotChartItem19handleDomainUpdatedEv'
    self.uglySide.call(ritual)

  def handleLayoutChanged(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleLayoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleLayoutChanged
    """
    #  void BoxPlotChartItem::handleLayoutChanged()
    self.uglySide.call('ritual_ZN16BoxPlotChartItem19handleLayoutChangedEv')

  def handleUpdatedBars(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleUpdatedBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleUpdatedBars
    """
    #  void BoxPlotChartItem::handleUpdatedBars()
    self.uglySide.call('ritual_ZN16BoxPlotChartItem17handleUpdatedBarsEv')

  @overload(QList[QBoxSet])
  def handleBoxsetRemove(self, barSets: QList[QBoxSet]) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::handleBoxsetRemove(const QList<QBoxSet
    *> &barSets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#handleBoxsetRemove

    Parameters
    ----------

    barSets : QList[QBoxSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void BoxPlotChartItem::handleBoxsetRemove(const QList<QBoxSet *>
    #      &barSets)
    self.uglySide.call(
        'ritual_ZN16BoxPlotChartItem18handleBoxsetRemoveERK5QListIP7QBoxSet'
        'E',
        self._valueOf(barSets),
    )

  def calculateLayout(self) -> QList[QRectF]:
    """
    Calls Qt's 'QList<QRectF> BoxPlotChartItem::calculateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#calculateLayout

    Returns
    -------

    QList[QRectF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QRectF> BoxPlotChartItem::calculateLayout()
    address = self.uglySide.call(
        'ritual_ZN16BoxPlotChartItem15calculateLayoutEv',
    )
    from ..QtCore import QRectF
    return QList[QRectF]._cuteOwning(address)

  def initializeLayout(self) -> None:
    """
    Calls Qt's 'void BoxPlotChartItem::initializeLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#initializeLayout
    """
    #  void BoxPlotChartItem::initializeLayout()
    self.uglySide.call('ritual_ZN16BoxPlotChartItem16initializeLayoutEv')

  @overload(BoxWhiskers, int)
  @overload(NoneType, int)
  def updateBoxGeometry(
      self,
      box: Optional[BoxWhiskers],
      index: int,
  ) -> bool:
    """
    Calls Qt's 'bool BoxPlotChartItem::updateBoxGeometry(BoxWhiskers *box,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxplotchartitem.html#updateBoxGeometry

    Parameters
    ----------

    box : Optional[BoxWhiskers]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  bool BoxPlotChartItem::updateBoxGeometry(BoxWhiskers *box, int index)
    return self.uglySide.call(
        'ritual_ZN16BoxPlotChartItem17updateBoxGeometryEP11BoxWhiskersi',
        self._addressOf(box), index,
    )
