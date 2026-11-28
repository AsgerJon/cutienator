"""
AbstractBarChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/abstractbarchartitem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means AbstractBarChartItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import ChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QPainter
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import BarAnimation, ChartAnimation, QAbstractSeries, QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  BarAnimation = WAIT['BarAnimation']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QBarSet = WAIT['QtCharts:QBarSet']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractBarChartItem(ChartItem):
  """
  The cute side of Qt's AbstractBarChartItem: a plain Python object standing
  in front of one C++ AbstractBarChartItem.

  It is built on the cute 'ChartItem', as Qt's AbstractBarChartItem is built
  on Qt's ChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AbstractBarChartItem that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'tr', 'paint',
  'boundingRect', 'calculateLayout', 'initializeFullLayout',
  'initializeLayout', 'applyLayout', 'setAnimation', 'animation',
  'setLayout', 'geometry', 'resetAnimation', 'handleDomainUpdated',
  'handleLayoutChanged', 'handleLabelsVisibleChanged',
  'handleDataStructureChanged', 'handleVisibleChanged',
  'handleOpacityChanged', 'handleUpdatedBars', 'handleLabelsPositionChanged',
  'positionLabels', 'handleBarValueChange', 'handleBarValueAdd',
  'handleBarValueRemove', 'handleSeriesAdded', 'handleSeriesRemoved',
  'positionLabelsVertical', 'createLabelItems', 'handleSetStructureChange',
  'generateLabelText', 'updateBarItems', 'markLabelsDirty',
  'calculateSeriesPositionAdjustmentAndWidth'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AbstractBarChartItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int AbstractBarChartItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'AbstractBarChartItem::~AbstractBarChartItem()': the destructor:
    Python never removes a C++ AbstractBarChartItem.

  What has no ritual
  ------------------

  3 of the 40 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ AbstractBarChartItem is created at the first use, not by
    'AbstractBarChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AbstractBarChartItem.
  - Qt tells when it has removed the C++ AbstractBarChartItem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's AbstractBarChartItem that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString AbstractBarChartItem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractbarchartitem.html#tr

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
    #  QString AbstractBarChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20AbstractBarChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AbstractBarChartItem'

  #  A C++ AbstractBarChartItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AbstractBarChartItem'

  #  The functions Qt calls itself that AbstractBarChartItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'calculateLayout': (
          'QList<QRectF> AbstractBarChartItem::calculateLayout()',
      ),
      'applyLayout': (
          'void AbstractBarChartItem::applyLayout(const QList<QRectF> &)',
      ),
  }

  #  The functions Qt calls itself that AbstractBarChartItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeLayout': (
          ('_ZN20AbstractBarChartItem16initializeLayoutEiiib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'setAnimation': (
          ('_ZN20AbstractBarChartItem12setAnimationEP12BarAnimation',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:BarAnimation'),
           )),
      ),
      'positionLabels': (
          ('_ZN20AbstractBarChartItem14positionLabelsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generateLabelText': (
          ('_ZN20AbstractBarChartItem17generateLabelTextEiid',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'markLabelsDirty': (
          ('_ZN20AbstractBarChartItem15markLabelsDirtyEP7QBarSetii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCharts:QBarSet'),
               ('int', 'number', ''),
               ('int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *AbstractBarChartItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AbstractBarChartItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20AbstractBarChartItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractBarChartItem::boundingRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractBarChartItem::boundingRect() const
    ritual = 'ritual_ZNK20AbstractBarChartItem12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20AbstractBarChartItem12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def animation(self) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *AbstractBarChartItem::animation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#animation

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *AbstractBarChartItem::animation() const
    ritual = 'ritual_ZNK20AbstractBarChartItem9animationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20AbstractBarChartItem9animationEv'
    address = self.uglySide.call(ritual)
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  def geometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractBarChartItem::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractbarchartitem.html#geometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractBarChartItem::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK20AbstractBarChartItem8geometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BarAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[BarAnimation]) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::setAnimation(BarAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#setAnimation

    Parameters
    ----------

    animation : Optional[BarAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractBarChartItem::setAnimation(BarAnimation *animation)
    ritual = 'ritual_ZN20AbstractBarChartItem12setAnimationEP12BarAnimation'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20AbstractBarChartItem12setAnimationEP12BarAnimatio'
          'n')
    self.uglySide.call(ritual, self._addressOf(animation))

  @overload(QList[QRectF])
  def setLayout(self, layout: QList[QRectF]) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::setLayout(const QList<QRectF>
    &layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#setLayout

    Parameters
    ----------

    layout : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void AbstractBarChartItem::setLayout(const QList<QRectF> &layout)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem9setLayoutERK5QListI6QRectFE',
        self._valueOf(layout),
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
    Qt's 'AbstractBarChartItem::AbstractBarChartItem(QAbstractBarSeries
    *series, QGraphicsItem *item)': the class is abstract, so C++ cannot make
    one, and the C++ class of ours does not fill in every function it leaves
    open.
    """
    raise NotImplementedError(
        "'AbstractBarChartItem.__init__' has no cute function yet. Qt's "
        "'AbstractBarChartItem::AbstractBarChartItem(QAbstractBarSeries "
        "*series, QGraphicsItem *item)': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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
    Calls Qt's 'void AbstractBarChartItem::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractbarchartitem.html#paint

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
    #  void AbstractBarChartItem::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN20AbstractBarChartItem5paintEP8QPainterPK24QStyleOptionGr'
        'aphicsItemP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20AbstractBarChartItem5paintEP8QPainterPK24QStyleOp'
          'tionGraphicsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  def calculateLayout(self) -> QList[QRectF]:
    """
    Calls Qt's 'QList<QRectF> AbstractBarChartItem::calculateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#calculateLayout

    Returns
    -------

    QList[QRectF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QRectF> AbstractBarChartItem::calculateLayout()
    address = self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem15calculateLayoutEv',
    )
    from ..QtCore import QRectF
    return QList[QRectF]._cuteOwning(address)

  def initializeFullLayout(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::initializeFullLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#initializeFullLayout
    """
    #  void AbstractBarChartItem::initializeFullLayout()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem20initializeFullLayoutEv',
    )

  @overload(int, int, int, bool)
  def initializeLayout(
      self,
      set: int,
      category: int,
      layoutIndex: int,
      resetAnimation: bool,
  ) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::initializeLayout(int set, int
    category, int layoutIndex, bool resetAnimation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#initializeLayout

    Parameters
    ----------

    set : int
      Passed on as it is.

    category : int
      Passed on as it is.

    layoutIndex : int
      Passed on as it is.

    resetAnimation : bool
      Passed on as it is.
    """
    #  void AbstractBarChartItem::initializeLayout(int set, int category, int
    #      layoutIndex, bool resetAnimation)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem16initializeLayoutEiiib',
        set, category, layoutIndex, resetAnimation,
    )

  @overload(QList[QRectF])
  def applyLayout(self, layout: QList[QRectF]) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::applyLayout(const QList<QRectF>
    &layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#applyLayout

    Parameters
    ----------

    layout : QList[QRectF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void AbstractBarChartItem::applyLayout(const QList<QRectF> &layout)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem11applyLayoutERK5QListI6QRectFE',
        self._valueOf(layout),
    )

  def resetAnimation(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::resetAnimation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#resetAnimation
    """
    #  void AbstractBarChartItem::resetAnimation()
    self.uglySide.call('ritual_ZN20AbstractBarChartItem14resetAnimationEv')

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleDomainUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleDomainUpdated
    """
    #  void AbstractBarChartItem::handleDomainUpdated()
    ritual = 'ritual_ZN20AbstractBarChartItem19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20AbstractBarChartItem19handleDomainUpdatedEv'
    self.uglySide.call(ritual)

  def handleLayoutChanged(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleLayoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleLayoutChanged
    """
    #  void AbstractBarChartItem::handleLayoutChanged()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem19handleLayoutChangedEv',
    )

  @overload(bool)
  def handleLabelsVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleLabelsVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void AbstractBarChartItem::handleLabelsVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem26handleLabelsVisibleChangedEb',
        visible,
    )

  def handleDataStructureChanged(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleDataStructureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html
    """
    #  void AbstractBarChartItem::handleDataStructureChanged()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem26handleDataStructureChangedEv',
    )

  def handleVisibleChanged(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleVisibleChanged
    """
    #  void AbstractBarChartItem::handleVisibleChanged()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem20handleVisibleChangedEv',
    )

  def handleOpacityChanged(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleOpacityChanged
    """
    #  void AbstractBarChartItem::handleOpacityChanged()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem20handleOpacityChangedEv',
    )

  def handleUpdatedBars(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleUpdatedBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleUpdatedBars
    """
    #  void AbstractBarChartItem::handleUpdatedBars()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem17handleUpdatedBarsEv',
    )

  def handleLabelsPositionChanged(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleLabelsPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html
    """
    #  void AbstractBarChartItem::handleLabelsPositionChanged()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem27handleLabelsPositionChangedEv',
    )

  def positionLabels(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::positionLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#positionLabels
    """
    #  void AbstractBarChartItem::positionLabels()
    ritual = 'ritual_ZN20AbstractBarChartItem14positionLabelsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20AbstractBarChartItem14positionLabelsEv'
    self.uglySide.call(ritual)

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def handleBarValueChange(
      self,
      index: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleBarValueChange(int index,
    QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleBarValueChange

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractBarChartItem::handleBarValueChange(int index, QBarSet
    #      *barset)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem20handleBarValueChangeEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, int, QBarSet)
  @overload(int, int, NoneType)
  def handleBarValueAdd(
      self,
      index: int,
      count: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleBarValueAdd(int index, int
    count, QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleBarValueAdd

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractBarChartItem::handleBarValueAdd(int index, int count,
    #      QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem17handleBarValueAddEiiP7QBarSet',
        index, count, self._addressOf(barset),
    )

  @overload(int, int, QBarSet)
  @overload(int, int, NoneType)
  def handleBarValueRemove(
      self,
      index: int,
      count: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleBarValueRemove(int index,
    int count, QBarSet *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleBarValueRemove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractBarChartItem::handleBarValueRemove(int index, int count,
    #      QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem20handleBarValueRemoveEiiP7QBarSet',
        index, count, self._addressOf(barset),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleSeriesAdded(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleSeriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractBarChartItem::handleSeriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem17handleSeriesAddedEP15QAbstractSer'
        'ies',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesRemoved(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void
    AbstractBarChartItem::handleSeriesRemoved(QAbstractSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleSeriesRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void AbstractBarChartItem::handleSeriesRemoved(QAbstractSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem19handleSeriesRemovedEP15QAbstractS'
        'eries',
        self._addressOf(series),
    )

  def positionLabelsVertical(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::positionLabelsVertical()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#positionLabelsVertical
    """
    #  void AbstractBarChartItem::positionLabelsVertical()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem22positionLabelsVerticalEv',
    )

  def createLabelItems(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::createLabelItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#createLabelItems
    """
    #  void AbstractBarChartItem::createLabelItems()
    self.uglySide.call('ritual_ZN20AbstractBarChartItem16createLabelItemsEv')

  def handleSetStructureChange(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::handleSetStructureChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#handleSetStructureChange
    """
    #  void AbstractBarChartItem::handleSetStructureChange()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem24handleSetStructureChangeEv',
    )

  @overload(int, int, float)
  def generateLabelText(self, set: int, category: int, value: float) -> str:
    """
    Calls Qt's 'QString AbstractBarChartItem::generateLabelText(int set, int
    category, qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#generateLabelText

    Parameters
    ----------

    set : int
      Passed on as it is.

    category : int
      Passed on as it is.

    value : float
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString AbstractBarChartItem::generateLabelText(int set, int category,
    #      qreal value)
    ritual = 'ritual_ZN20AbstractBarChartItem17generateLabelTextEiid'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20AbstractBarChartItem17generateLabelTextEiid'
    return self.uglySide.call(ritual, set, category, value)

  def updateBarItems(self) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::updateBarItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#updateBarItems
    """
    #  void AbstractBarChartItem::updateBarItems()
    self.uglySide.call('ritual_ZN20AbstractBarChartItem14updateBarItemsEv')

  @overload(QBarSet, int, int)
  @overload(NoneType, int, int)
  def markLabelsDirty(
      self,
      barset: Optional[QBarSet],
      index: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void AbstractBarChartItem::markLabelsDirty(QBarSet *barset,
    int index, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html#markLabelsDirty

    Parameters
    ----------

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void AbstractBarChartItem::markLabelsDirty(QBarSet *barset, int index,
    #      int count)
    ritual = 'ritual_ZN20AbstractBarChartItem15markLabelsDirtyEP7QBarSetii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20AbstractBarChartItem15markLabelsDirtyEP7QBarSetii')
    self.uglySide.call(ritual, self._addressOf(barset), index, count)

  def calculateSeriesPositionAdjustmentAndWidth(self) -> None:
    """
    Calls Qt's 'void
    AbstractBarChartItem::calculateSeriesPositionAdjustmentAndWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractbarchartitem.html
    """
    #  void AbstractBarChartItem::calculateSeriesPositionAdjustmentAndWidth()
    self.uglySide.call(
        'ritual_ZN20AbstractBarChartItem41calculateSeriesPositionAdjustment'
        'AndWidthEv',
    )
