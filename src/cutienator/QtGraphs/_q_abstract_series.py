"""
QAbstractSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qabstractseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QAbstractAxis, QGraphsView, QLegendData
  from ..QtCharts import QAbstractSeriesPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtGraphs:QAbstractAxis']
  QGraphsView = WAIT['QGraphsView']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSeries(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QAbstractSeries: a plain Python object standing in
  front of one C++ QAbstractSeries.

  It is built on the cute 'QObject', as Qt's QAbstractSeries is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QAbstractSeries is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSeries that has a ritual and that Python
  can call so far, 47 names in all: 'metaObject', 'tr', 'd_func',
  'classBegin', 'componentComplete', 'type', 'name', 'setName', 'isVisible',
  'setVisible', 'isSelectable', 'setSelectable', 'opacity', 'setOpacity',
  'valuesMultiplier', 'setValuesMultiplier', 'graph', 'setGraph',
  'legendData', 'show', 'hide', 'isHoverable', 'setHoverable', 'hasLoaded',
  'isHovered', 'setHovered', 'axisX', 'setAxisX', 'axisY', 'setAxisY',
  'zValue', 'setZValue', 'update', 'nameChanged', 'visibleChanged',
  'selectableChanged', 'hoverableChanged', 'opacityChanged',
  'valuesMultiplierChanged', 'legendDataChanged', 'hoverEnter', 'hoverExit',
  'hover', 'hoveredChanged', 'axisXChanged', 'axisYChanged', 'zValueChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QAbstractSeriesPrivate *QAbstractSeries::d_func() const':
    takes in Python what 'QAbstractSeriesPrivate *QAbstractSeries::d_func()'
    takes.
  - Qt's 'void QAbstractSeries::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractSeries::~QAbstractSeries()': the destructor: Python never
    removes a C++ QAbstractSeries.
  - Qt's 'QQmlListProperty<QObject> QAbstractSeries::seriesChildren()': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 56 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractSeries is created at the first use, not by
    'QAbstractSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSeries.
  - Qt tells when it has removed the C++ QAbstractSeries. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractSeries that has no cute function yet,
    '__init__', 'seriesChildren', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractSeries, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SeriesType(CuteNum, scoped=True):
    """
    The enum 'QAbstractSeries::SeriesType' of Qt, with the 7 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Line = Kee[int](0)
    Area = Kee[int](1)
    Bar = Kee[int](2)
    Pie = Kee[int](3)
    Scatter = Kee[int](4)
    Spline = Kee[int](5)
    Custom = Kee[int](6)

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
    Calls Qt's 'QString QAbstractSeries::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#tr

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
    #  QString QAbstractSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstractSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  Qt's QAbstractSeries is built on more than one class. The part of a C++
  #  QAbstractSeries that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QAbstractSeries_QQmlParserStatus',
  }

  #  A C++ QAbstractSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSeries'

  #  The functions Qt calls itself that QAbstractSeries is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'type': (
          ('_ZNK15QAbstractSeries4typeEv',
           ('int', 'enum', 'QtGraphs:QAbstractSeries.SeriesType'),
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
    Calls Qt's 'const QMetaObject *QAbstractSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> SeriesType:
    """
    Calls Qt's 'SeriesType QAbstractSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#type

    Returns
    -------

    SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SeriesType(number)'
      gives.
    """
    #  SeriesType QAbstractSeries::type() const
    return QAbstractSeries.SeriesType(self.uglySide.call(
        'ritual_ZNK15QAbstractSeries4typeEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QAbstractSeries::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractSeries::name() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries4nameEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#isVisible
    """
    #  bool QAbstractSeries::isVisible() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries9isVisibleEv')

  def isSelectable(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::isSelectable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#isSelectable
    """
    #  bool QAbstractSeries::isSelectable() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries12isSelectableEv')

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QAbstractSeries::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#opacity
    """
    #  qreal QAbstractSeries::opacity() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries7opacityEv')

  def valuesMultiplier(self) -> float:
    """
    Calls Qt's 'qreal QAbstractSeries::valuesMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#valuesMultiplier
    """
    #  qreal QAbstractSeries::valuesMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractSeries16valuesMultiplierEv',
    )

  def graph(self) -> Optional[QGraphsView]:
    """
    Calls Qt's 'QGraphsView *QAbstractSeries::graph() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#graph

    Returns
    -------

    Optional[QGraphsView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphsView *QAbstractSeries::graph() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries5graphEv')
    from . import QGraphsView
    return QGraphsView._cuteAt(address)

  def legendData(self) -> QList[QLegendData]:
    """
    Calls Qt's 'const QList<QLegendData> QAbstractSeries::legendData()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#legendData

    Returns
    -------

    QList[QLegendData]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QLegendData> QAbstractSeries::legendData() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries10legendDataEv')
    from . import QLegendData
    return QList[QLegendData]._cuteOwning(address)

  def isHoverable(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::isHoverable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#isHoverable
    """
    #  bool QAbstractSeries::isHoverable() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries11isHoverableEv')

  def hasLoaded(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::hasLoaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#hasLoaded
    """
    #  bool QAbstractSeries::hasLoaded() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries9hasLoadedEv')

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSeries::isHovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#isHovered
    """
    #  bool QAbstractSeries::isHovered() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries9isHoveredEv')

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QAbstractSeries::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QAbstractSeries::axisX() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries5axisXEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *QAbstractSeries::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QAbstractSeries::axisY() const
    address = self.uglySide.call('ritual_ZNK15QAbstractSeries5axisYEv')
    from . import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def zValue(self) -> int:
    """
    Calls Qt's 'int QAbstractSeries::zValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#zValue
    """
    #  int QAbstractSeries::zValue() const
    return self.uglySide.call('ritual_ZNK15QAbstractSeries6zValueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSeries::setName(const QString &name)
    self.uglySide.call('ritual_ZN15QAbstractSeries7setNameERK7QString', name)

  @overload()
  @overload(bool)
  def setVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractSeries::setVisible(bool visible)
    self.uglySide.call('ritual_ZN15QAbstractSeries10setVisibleEb', visible)

  @overload(bool)
  def setSelectable(self, selectable: bool) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setSelectable(bool selectable)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setSelectable

    Parameters
    ----------

    selectable : bool
      Passed on as it is.
    """
    #  void QAbstractSeries::setSelectable(bool selectable)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries13setSelectableEb', selectable,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setOpacity(qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QAbstractSeries::setOpacity(qreal opacity)
    self.uglySide.call('ritual_ZN15QAbstractSeries10setOpacityEd', opacity)

  @overload(float)
  def setValuesMultiplier(self, valuesMultiplier: float) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setValuesMultiplier(qreal
    valuesMultiplier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#setValuesMultiplier

    Parameters
    ----------

    valuesMultiplier : float
      Passed on as it is.
    """
    #  void QAbstractSeries::setValuesMultiplier(qreal valuesMultiplier)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries19setValuesMultiplierEd',
        valuesMultiplier,
    )

  @overload(QGraphsView)
  @overload(NoneType)
  def setGraph(self, graph: Optional[QGraphsView]) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setGraph(QGraphsView *graph)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setGraph

    Parameters
    ----------

    graph : Optional[QGraphsView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeries::setGraph(QGraphsView *graph)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries8setGraphEP11QGraphsView',
        self._addressOf(graph),
    )

  @overload(bool)
  def setHoverable(self, newHoverable: bool) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setHoverable(bool newHoverable)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setHoverable

    Parameters
    ----------

    newHoverable : bool
      Passed on as it is.
    """
    #  void QAbstractSeries::setHoverable(bool newHoverable)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries12setHoverableEb', newHoverable,
    )

  @overload(bool)
  def setHovered(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setHovered(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setHovered

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QAbstractSeries::setHovered(bool enabled)
    self.uglySide.call('ritual_ZN15QAbstractSeries10setHoveredEb', enabled)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, newAxisX: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setAxisX(QAbstractAxis *newAxisX)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setAxisX

    Parameters
    ----------

    newAxisX : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeries::setAxisX(QAbstractAxis *newAxisX)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries8setAxisXEP13QAbstractAxis',
        self._addressOf(newAxisX),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, newAxisY: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setAxisY(QAbstractAxis *newAxisY)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setAxisY

    Parameters
    ----------

    newAxisY : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeries::setAxisY(QAbstractAxis *newAxisY)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries8setAxisYEP13QAbstractAxis',
        self._addressOf(newAxisY),
    )

  @overload(int)
  def setZValue(self, newDrawOrder: int) -> None:
    """
    Calls Qt's 'void QAbstractSeries::setZValue(int newDrawOrder)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#setZValue

    Parameters
    ----------

    newDrawOrder : int
      Passed on as it is.
    """
    #  void QAbstractSeries::setZValue(int newDrawOrder)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries9setZValueEi', newDrawOrder,
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
    Qt's 'QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractSeries.__init__' has no cute function yet. Qt's "
        "'QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &dd, "
        "QObject *parent)': takes a type Python has no way to hand over yet."
    )

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

  def d_func(self) -> Optional[QAbstractSeriesPrivate]:
    """
    Calls Qt's 'QAbstractSeriesPrivate *QAbstractSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#d_func

    Returns
    -------

    Optional[QAbstractSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeriesPrivate *QAbstractSeries::d_func()
    address = self.uglySide.call('ritual_ZN15QAbstractSeries6d_funcEv')
    from ..QtCharts import QAbstractSeriesPrivate
    return QAbstractSeriesPrivate._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#classBegin
    """
    #  void QAbstractSeries::classBegin()
    ritual = 'ritual_ZN15QAbstractSeries10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSeries10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#componentComplete
    """
    #  void QAbstractSeries::componentComplete()
    ritual = 'ritual_ZN15QAbstractSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  def show(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::show()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#show
    """
    #  void QAbstractSeries::show()
    self.uglySide.call('ritual_ZN15QAbstractSeries4showEv')

  def hide(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#hide
    """
    #  void QAbstractSeries::hide()
    self.uglySide.call('ritual_ZN15QAbstractSeries4hideEv')

  def update(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#update
    """
    #  void QAbstractSeries::update()
    self.uglySide.call('ritual_ZN15QAbstractSeries6updateEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#nameChanged
    """
    #  void QAbstractSeries::nameChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries11nameChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#visibleChanged
    """
    #  void QAbstractSeries::visibleChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries14visibleChangedEv')

  def selectableChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::selectableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#selectableChanged
    """
    #  void QAbstractSeries::selectableChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries17selectableChangedEv')

  def hoverableChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hoverableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#hoverableChanged
    """
    #  void QAbstractSeries::hoverableChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries16hoverableChangedEv')

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::opacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#opacityChanged
    """
    #  void QAbstractSeries::opacityChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries14opacityChangedEv')

  def valuesMultiplierChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::valuesMultiplierChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#valuesMultiplierChanged
    """
    #  void QAbstractSeries::valuesMultiplierChanged()
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries23valuesMultiplierChangedEv',
    )

  def legendDataChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractSeries::legendDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#legendDataChanged
    """
    #  void QAbstractSeries::legendDataChanged()
    self.uglySide.call('ritual_ZN15QAbstractSeries17legendDataChangedEv')

  @overload(str, QPointF, QPointF)
  def hoverEnter(
      self,
      seriesName: str,
      position: QPointF,
      value: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hoverEnter(const QString &seriesName,
    QPointF position, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#hoverEnter

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAbstractSeries::hoverEnter(const QString &seriesName, QPointF
    #      position, QPointF value)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries10hoverEnterERK7QString7QPointFS3_',
        seriesName, self._valueOf(position, 'QPointF'), self._valueOf(value,
        'QPointF'),
    )

  @overload(str, QPointF)
  def hoverExit(self, seriesName: str, position: QPointF) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hoverExit(const QString &seriesName,
    QPointF position)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#hoverExit

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAbstractSeries::hoverExit(const QString &seriesName, QPointF
    #      position)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries9hoverExitERK7QString7QPointF',
        seriesName, self._valueOf(position, 'QPointF'),
    )

  @overload(str, QPointF, QPointF)
  def hover(
      self,
      seriesName: str,
      position: QPointF,
      value: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hover(const QString &seriesName,
    QPointF position, QPointF value)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#hover

    Parameters
    ----------

    seriesName : str
      Passed on as it is: a QString is made of it for the call.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAbstractSeries::hover(const QString &seriesName, QPointF
    #      position, QPointF value)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries5hoverERK7QString7QPointFS3_',
        seriesName, self._valueOf(position, 'QPointF'), self._valueOf(value,
        'QPointF'),
    )

  @overload(bool)
  def hoveredChanged(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QAbstractSeries::hoveredChanged(bool hovered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractseries.html#hoveredChanged

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QAbstractSeries::hoveredChanged(bool hovered)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries14hoveredChangedEb', hovered,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, newAxis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QAbstractSeries::axisXChanged(QAbstractAxis *newAxis)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#axisXChanged

    Parameters
    ----------

    newAxis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeries::axisXChanged(QAbstractAxis *newAxis)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries12axisXChangedEP13QAbstractAxis',
        self._addressOf(newAxis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, newAxis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void QAbstractSeries::axisYChanged(QAbstractAxis *newAxis)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#axisYChanged

    Parameters
    ----------

    newAxis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSeries::axisYChanged(QAbstractAxis *newAxis)
    self.uglySide.call(
        'ritual_ZN15QAbstractSeries12axisYChangedEP13QAbstractAxis',
        self._addressOf(newAxis),
    )

  @overload(int)
  def zValueChanged(self, z: int) -> None:
    """
    Calls Qt's 'void QAbstractSeries::zValueChanged(int z)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractseries.html#zValueChanged

    Parameters
    ----------

    z : int
      Passed on as it is.
    """
    #  void QAbstractSeries::zValueChanged(int z)
    self.uglySide.call('ritual_ZN15QAbstractSeries13zValueChangedEi', z)

  @staticmethod
  def seriesChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QAbstractSeries::seriesChildren()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractSeries.seriesChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QAbstractSeries::seriesChildren()': "
        "gives a type Python has no way to take yet.")
