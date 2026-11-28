"""
XYChart binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/xychart_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means XYChart to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QGraphicsItem
from . import ChartItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import ChartAnimation, QXYSeries, XYAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QXYSeries = WAIT['QtCharts:QXYSeries']
  XYAnimation = WAIT['XYAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class XYChart(ChartItem):
  """
  The cute side of Qt's XYChart: a plain Python object standing in front of
  one C++ XYChart.

  It is built on the cute 'ChartItem', as Qt's XYChart is built on Qt's
  ChartItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's XYChart that has a ritual and that Python can call
  so far, 28 names in all: 'metaObject', 'tr', 'setGeometryPoints',
  'geometryPoints', 'setAnimation', 'animation', 'updateGeometry', 'isDirty',
  'setDirty', 'handlePointAdded', 'handlePointRemoved',
  'handlePointsRemoved', 'handlePointReplaced', 'handlePointsReplaced',
  'handleDomainUpdated', 'handleSeriesUpdated', 'clicked', 'hovered',
  'pressed', 'released', 'doubleClicked', 'updateChart', 'updateGlChart',
  'refreshGlChart', 'matchForLightMarker', 'isEmpty', 'hoverPoint',
  'fuzzyComparePointF'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *XYChart::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int XYChart::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'XYChart::~XYChart()': the destructor: Python never removes a C++
    XYChart.
  - Qt's 'QList<bool> XYChart::offGridStatusVector()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  3 of the 36 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ XYChart is created at the first use, not by 'XYChart(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ XYChart.
  - Qt tells when it has removed the C++ XYChart. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's XYChart that has no cute function yet,
    'getSeriesRanges', 'offGridStatusVector', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString XYChart::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#tr

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
    #  QString XYChart::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7XYChart2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPointF, QPointF)
  def fuzzyComparePointF(p1: QPointF, p2: QPointF) -> bool:
    """
    Calls Qt's 'bool XYChart::fuzzyComparePointF(const QPointF &p1, const
    QPointF &p2)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#fuzzyComparePointF

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool XYChart::fuzzyComparePointF(const QPointF &p1, const QPointF &p2)
    return Rituals.call(
        'ritual_ZN7XYChart18fuzzyComparePointFERK7QPointFS2_',
        CuteMixin._valueOf(p1, 'QPointF'), CuteMixin._valueOf(p2, 'QPointF'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'XYChart'

  #  A C++ XYChart Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_XYChart'

  #  The functions Qt calls itself that XYChart is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'updateChart': (
          'void XYChart::updateChart(const QList<QPointF> &, const '
          'QList<QPointF> &, int)',
      ),
  }

  #  The functions Qt calls itself that XYChart is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'updateGeometry': (
          ('_ZN7XYChart14updateGeometryEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleSeriesUpdated': (
          ('_ZN7XYChart19handleSeriesUpdatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateGlChart': (
          ('_ZN7XYChart13updateGlChartEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'refreshGlChart': (
          ('_ZN7XYChart14refreshGlChartEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *XYChart::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *XYChart::metaObject() const
    address = self.uglySide.call('ritual_ZNK7XYChart10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def geometryPoints(self) -> QList[QPointF]:
    """
    Calls Qt's 'QList<QPointF> XYChart::geometryPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#geometryPoints

    Returns
    -------

    QList[QPointF]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPointF> XYChart::geometryPoints() const
    address = self.uglySide.call('ritual_ZNK7XYChart14geometryPointsEv')
    from ..QtCore import QPointF
    return QList[QPointF]._cuteOwning(address)

  def animation(self) -> Optional[ChartAnimation]:
    """
    Calls Qt's 'ChartAnimation *XYChart::animation() const'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#animation

    Returns
    -------

    Optional[ChartAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ChartAnimation *XYChart::animation() const
    ritual = 'ritual_ZNK7XYChart9animationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7XYChart9animationEv'
    address = self.uglySide.call(ritual)
    from . import ChartAnimation
    return ChartAnimation._cuteAt(address)

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool XYChart::isDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#isDirty
    """
    #  bool XYChart::isDirty() const
    return self.uglySide.call('ritual_ZNK7XYChart7isDirtyEv')

  @overload(QPointF)
  def matchForLightMarker(self, eventPos: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF XYChart::matchForLightMarker(const QPointF &eventPos)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#matchForLightMarker

    Parameters
    ----------

    eventPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF XYChart::matchForLightMarker(const QPointF &eventPos) const
    address = self.uglySide.call(
        'ritual_ZNK7XYChart19matchForLightMarkerERK7QPointF',
        self._valueOf(eventPos, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def hoverPoint(self, eventPos: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF XYChart::hoverPoint(const QPointF &eventPos) const'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#hoverPoint

    Parameters
    ----------

    eventPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF XYChart::hoverPoint(const QPointF &eventPos) const
    address = self.uglySide.call(
        'ritual_ZNK7XYChart10hoverPointERK7QPointF',
        self._valueOf(eventPos, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPointF])
  def setGeometryPoints(self, points: QList[QPointF]) -> None:
    """
    Calls Qt's 'void XYChart::setGeometryPoints(const QList<QPointF>
    &points)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#setGeometryPoints

    Parameters
    ----------

    points : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void XYChart::setGeometryPoints(const QList<QPointF> &points)
    self.uglySide.call(
        'ritual_ZN7XYChart17setGeometryPointsERK5QListI7QPointFE',
        self._valueOf(points),
    )

  @overload(XYAnimation)
  @overload(NoneType)
  def setAnimation(self, animation: Optional[XYAnimation]) -> None:
    """
    Calls Qt's 'void XYChart::setAnimation(XYAnimation *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#setAnimation

    Parameters
    ----------

    animation : Optional[XYAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void XYChart::setAnimation(XYAnimation *animation)
    self.uglySide.call(
        'ritual_ZN7XYChart12setAnimationEP11XYAnimation',
        self._addressOf(animation),
    )

  @overload(bool)
  def setDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void XYChart::setDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#setDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void XYChart::setDirty(bool dirty)
    self.uglySide.call('ritual_ZN7XYChart8setDirtyEb', dirty)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QXYSeries)
  @overload(NoneType)
  @overload(QXYSeries, QGraphicsItem)
  @overload(QXYSeries, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      series: Optional[QXYSeries],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'XYChart::XYChart(QXYSeries *series,
    QGraphicsItem *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#XYChart

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  XYChart::XYChart(QXYSeries *series, QGraphicsItem *item)
    self._noteCreation(XYChart, lambda: Rituals.call(
        'ritual_ZN7XYChartC1EP9QXYSeriesP13QGraphicsItem',
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

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void XYChart::updateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#updateGeometry
    """
    #  void XYChart::updateGeometry()
    self.uglySide.call('ritual_ZN7XYChart14updateGeometryEv')

  @overload(int)
  def handlePointAdded(self, index: int) -> None:
    """
    Calls Qt's 'void XYChart::handlePointAdded(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handlePointAdded

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void XYChart::handlePointAdded(int index)
    self.uglySide.call('ritual_ZN7XYChart16handlePointAddedEi', index)

  @overload(int)
  def handlePointRemoved(self, index: int) -> None:
    """
    Calls Qt's 'void XYChart::handlePointRemoved(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handlePointRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void XYChart::handlePointRemoved(int index)
    self.uglySide.call('ritual_ZN7XYChart18handlePointRemovedEi', index)

  @overload(int, int)
  def handlePointsRemoved(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void XYChart::handlePointsRemoved(int index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handlePointsRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void XYChart::handlePointsRemoved(int index, int count)
    self.uglySide.call(
        'ritual_ZN7XYChart19handlePointsRemovedEii', index, count,
    )

  @overload(int)
  def handlePointReplaced(self, index: int) -> None:
    """
    Calls Qt's 'void XYChart::handlePointReplaced(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handlePointReplaced

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void XYChart::handlePointReplaced(int index)
    self.uglySide.call('ritual_ZN7XYChart19handlePointReplacedEi', index)

  def handlePointsReplaced(self) -> None:
    """
    Calls Qt's 'void XYChart::handlePointsReplaced()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handlePointsReplaced
    """
    #  void XYChart::handlePointsReplaced()
    self.uglySide.call('ritual_ZN7XYChart20handlePointsReplacedEv')

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void XYChart::handleDomainUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handleDomainUpdated
    """
    #  void XYChart::handleDomainUpdated()
    ritual = 'ritual_ZN7XYChart19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7XYChart19handleDomainUpdatedEv'
    self.uglySide.call(ritual)

  def handleSeriesUpdated(self) -> None:
    """
    Calls Qt's 'void XYChart::handleSeriesUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#handleSeriesUpdated
    """
    #  void XYChart::handleSeriesUpdated()
    ritual = 'ritual_ZN7XYChart19handleSeriesUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7XYChart19handleSeriesUpdatedEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def clicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void XYChart::clicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#clicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void XYChart::clicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN7XYChart7clickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF, bool)
  def hovered(self, point: QPointF, state: bool) -> None:
    """
    Calls Qt's 'void XYChart::hovered(const QPointF &point, bool state)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#hovered

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    state : bool
      Passed on as it is.
    """
    #  void XYChart::hovered(const QPointF &point, bool state)
    self.uglySide.call(
        'ritual_ZN7XYChart7hoveredERK7QPointFb',
        self._valueOf(point, 'QPointF'), state,
    )

  @overload(QPointF)
  def pressed(self, point: QPointF) -> None:
    """
    Calls Qt's 'void XYChart::pressed(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#pressed

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void XYChart::pressed(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN7XYChart7pressedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def released(self, point: QPointF) -> None:
    """
    Calls Qt's 'void XYChart::released(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#released

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void XYChart::released(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN7XYChart8releasedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QPointF)
  def doubleClicked(self, point: QPointF) -> None:
    """
    Calls Qt's 'void XYChart::doubleClicked(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#doubleClicked

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void XYChart::doubleClicked(const QPointF &point)
    self.uglySide.call(
        'ritual_ZN7XYChart13doubleClickedERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(QList[QPointF], QList[QPointF])
  @overload(QList[QPointF], QList[QPointF], int)
  def updateChart(
      self,
      oldPoints: QList[QPointF],
      newPoints: QList[QPointF],
      index: int = -1,
  ) -> None:
    """
    Calls Qt's 'void XYChart::updateChart(const QList<QPointF> &oldPoints,
    const QList<QPointF> &newPoints, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#updateChart

    Parameters
    ----------

    oldPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    newPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void XYChart::updateChart(const QList<QPointF> &oldPoints, const
    #      QList<QPointF> &newPoints, int index)
    self.uglySide.call(
        'ritual_ZN7XYChart11updateChartERK5QListI7QPointFES4_i',
        self._valueOf(oldPoints), self._valueOf(newPoints), index,
    )

  def updateGlChart(self) -> None:
    """
    Calls Qt's 'void XYChart::updateGlChart()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#updateGlChart
    """
    #  void XYChart::updateGlChart()
    ritual = 'ritual_ZN7XYChart13updateGlChartEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7XYChart13updateGlChartEv'
    self.uglySide.call(ritual)

  def refreshGlChart(self) -> None:
    """
    Calls Qt's 'void XYChart::refreshGlChart()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#refreshGlChart
    """
    #  void XYChart::refreshGlChart()
    ritual = 'ritual_ZN7XYChart14refreshGlChartEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7XYChart14refreshGlChartEv'
    self.uglySide.call(ritual)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool XYChart::isEmpty()'.

    Qt's own words: https://doc.qt.io/qt-6/xychart.html#isEmpty
    """
    #  bool XYChart::isEmpty()
    return self.uglySide.call('ritual_ZN7XYChart7isEmptyEv')

  @staticmethod
  def getSeriesRanges(*__, **_) -> Never:
    """
    Qt's 'void XYChart::getSeriesRanges(qreal &minX, qreal &maxX, qreal
    &minY, qreal &maxY)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'XYChart.getSeriesRanges' has no cute function yet. Qt's 'void "
        "XYChart::getSeriesRanges(qreal &minX, qreal &maxX, qreal &minY, "
        "qreal &maxY)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def offGridStatusVector(*__, **_) -> Never:
    """
    Qt's 'QList<bool> XYChart::offGridStatusVector()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'XYChart.offGridStatusVector' has no cute function yet. Qt's "
        "'QList<bool> XYChart::offGridStatusVector()': gives a type Python "
        "has no way to take yet.")
