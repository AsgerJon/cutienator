"""
Q3DBarsWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphsWidgets/q3dbarswidgetitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtGraphs import QtGraphs3D
from . import Q3DGraphsWidgetItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSizeF
  from ..QtGui import QImage
  from ..QtGraphs import QAbstract3DAxis, QBar3DSeries, QCategory3DAxis
  from ..QtGraphs import QQuickGraphsBars, QValue3DAxis
  from . import Q3DBarsWidgetItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtGraphs:QAbstract3DAxis']
  QBar3DSeries = WAIT['QtGraphs:QBar3DSeries']
  QCategory3DAxis = WAIT['QtGraphs:QCategory3DAxis']
  QEvent = WAIT['QEvent']
  QImage = WAIT['QImage']
  QSizeF = WAIT['QSizeF']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DBarsWidgetItem(Q3DGraphsWidgetItem):
  """
  The cute side of Qt's Q3DBarsWidgetItem: a plain Python object standing in
  front of one C++ Q3DBarsWidgetItem.

  It is built on the cute 'Q3DGraphsWidgetItem', as Qt's Q3DBarsWidgetItem is
  built on Qt's Q3DGraphsWidgetItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DBarsWidgetItem that has a ritual and that Python
  can call so far, 46 names in all: 'metaObject', 'tr', 'primarySeries',
  'addSeries', 'removeSeries', 'insertSeries', 'seriesList',
  'isMultiSeriesUniform', 'barThickness', 'barSpacing',
  'isBarSpacingRelative', 'barSeriesMargin', 'rowAxis', 'columnAxis',
  'valueAxis', 'addAxis', 'releaseAxis', 'axes', 'selectedSeries',
  'floorLevel', 'renderSliceToImage', 'setPrimarySeries',
  'setMultiSeriesUniform', 'setBarThickness', 'setBarSpacing',
  'setBarSpacingRelative', 'setBarSeriesMargin', 'setRowAxis',
  'setColumnAxis', 'setValueAxis', 'setFloorLevel', 'event',
  'multiSeriesUniformChanged', 'barThicknessChanged', 'barSpacingChanged',
  'barSpacingRelativeChanged', 'barSeriesMarginChanged', 'rowAxisChanged',
  'columnAxisChanged', 'valueAxisChanged', 'primarySeriesChanged',
  'selectedSeriesChanged', 'floorLevelChanged', 'sliceImageChanged',
  'd_func', 'graphBars'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DBarsWidgetItem::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Q3DBarsWidgetItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DBarsWidgetItem::~Q3DBarsWidgetItem()': the destructor: Python
    never removes a C++ Q3DBarsWidgetItem.
  - Qt's 'const Q3DBarsWidgetItemPrivate *Q3DBarsWidgetItem::d_func() const':
    takes in Python what 'Q3DBarsWidgetItemPrivate
    *Q3DBarsWidgetItem::d_func()' takes.
  - Qt's 'const QQuickGraphsBars *Q3DBarsWidgetItem::graphBars() const':
    takes in Python what 'QQuickGraphsBars *Q3DBarsWidgetItem::graphBars()'
    takes.

  What has no ritual
  ------------------

  6 of the 58 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ Q3DBarsWidgetItem is created at the first use, not by
    'Q3DBarsWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DBarsWidgetItem.
  - Qt tells when it has removed the C++ Q3DBarsWidgetItem. Every call on the
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
    Calls Qt's 'QString Q3DBarsWidgetItem::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#tr

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
    #  QString Q3DBarsWidgetItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17Q3DBarsWidgetItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DBarsWidgetItem'

  #  A C++ Q3DBarsWidgetItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DBarsWidgetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DBarsWidgetItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DBarsWidgetItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def primarySeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Q3DBarsWidgetItem::primarySeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#primarySeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Q3DBarsWidgetItem::primarySeries() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem13primarySeriesEv',
    )
    from ..QtGraphs import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def seriesList(self) -> QList[QBar3DSeries]:
    """
    Calls Qt's 'QList<QBar3DSeries *> Q3DBarsWidgetItem::seriesList() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#seriesList

    Returns
    -------

    QList[QBar3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBar3DSeries *> Q3DBarsWidgetItem::seriesList() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem10seriesListEv',
    )
    from ..QtGraphs import QBar3DSeries
    return QList[QBar3DSeries]._cuteOwning(address)

  def isMultiSeriesUniform(self) -> bool:
    """
    Calls Qt's 'bool Q3DBarsWidgetItem::isMultiSeriesUniform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#isMultiSeriesUniform
    """
    #  bool Q3DBarsWidgetItem::isMultiSeriesUniform() const
    return self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem20isMultiSeriesUniformEv',
    )

  def barThickness(self) -> float:
    """
    Calls Qt's 'float Q3DBarsWidgetItem::barThickness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barThickness
    """
    #  float Q3DBarsWidgetItem::barThickness() const
    return self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem12barThicknessEv',
    )

  def barSpacing(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF Q3DBarsWidgetItem::barSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barSpacing

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF Q3DBarsWidgetItem::barSpacing() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem10barSpacingEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isBarSpacingRelative(self) -> bool:
    """
    Calls Qt's 'bool Q3DBarsWidgetItem::isBarSpacingRelative() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#isBarSpacingRelative
    """
    #  bool Q3DBarsWidgetItem::isBarSpacingRelative() const
    return self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem20isBarSpacingRelativeEv',
    )

  def barSeriesMargin(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF Q3DBarsWidgetItem::barSeriesMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barSeriesMargin

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF Q3DBarsWidgetItem::barSeriesMargin() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem15barSeriesMarginEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def rowAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *Q3DBarsWidgetItem::rowAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#rowAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *Q3DBarsWidgetItem::rowAxis() const
    address = self.uglySide.call('ritual_ZNK17Q3DBarsWidgetItem7rowAxisEv')
    from ..QtGraphs import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def columnAxis(self) -> Optional[QCategory3DAxis]:
    """
    Calls Qt's 'QCategory3DAxis *Q3DBarsWidgetItem::columnAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#columnAxis

    Returns
    -------

    Optional[QCategory3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCategory3DAxis *Q3DBarsWidgetItem::columnAxis() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem10columnAxisEv',
    )
    from ..QtGraphs import QCategory3DAxis
    return QCategory3DAxis._cuteAt(address)

  def valueAxis(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DBarsWidgetItem::valueAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#valueAxis

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DBarsWidgetItem::valueAxis() const
    address = self.uglySide.call('ritual_ZNK17Q3DBarsWidgetItem9valueAxisEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axes(self) -> QList[QAbstract3DAxis]:
    """
    Calls Qt's 'QList<QAbstract3DAxis *> Q3DBarsWidgetItem::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#axes

    Returns
    -------

    QList[QAbstract3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstract3DAxis *> Q3DBarsWidgetItem::axes() const
    address = self.uglySide.call('ritual_ZNK17Q3DBarsWidgetItem4axesEv')
    from ..QtGraphs import QAbstract3DAxis
    return QList[QAbstract3DAxis]._cuteOwning(address)

  def selectedSeries(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *Q3DBarsWidgetItem::selectedSeries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#selectedSeries

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *Q3DBarsWidgetItem::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK17Q3DBarsWidgetItem14selectedSeriesEv',
    )
    from ..QtGraphs import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  def floorLevel(self) -> float:
    """
    Calls Qt's 'float Q3DBarsWidgetItem::floorLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#floorLevel
    """
    #  float Q3DBarsWidgetItem::floorLevel() const
    return self.uglySide.call('ritual_ZNK17Q3DBarsWidgetItem10floorLevelEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBar3DSeries)
  @overload(NoneType)
  def setPrimarySeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setPrimarySeries(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setPrimarySeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::setPrimarySeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem16setPrimarySeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def setMultiSeriesUniform(self, uniform: bool) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setMultiSeriesUniform(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setMultiSeriesUniform

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::setMultiSeriesUniform(bool uniform)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem21setMultiSeriesUniformEb', uniform,
    )

  @overload(float)
  def setBarThickness(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setBarThickness(float
    thicknessRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setBarThickness

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::setBarThickness(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem15setBarThicknessEf', thicknessRatio,
    )

  @overload(QSizeF)
  def setBarSpacing(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setBarSpacing(QSizeF spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setBarSpacing

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBarsWidgetItem::setBarSpacing(QSizeF spacing)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem13setBarSpacingE6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def setBarSpacingRelative(self, relative: bool) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setBarSpacingRelative(bool
    relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setBarSpacingRelative

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::setBarSpacingRelative(bool relative)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem21setBarSpacingRelativeEb', relative,
    )

  @overload(QSizeF)
  def setBarSeriesMargin(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setBarSeriesMargin(QSizeF margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setBarSeriesMargin

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBarsWidgetItem::setBarSeriesMargin(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem18setBarSeriesMarginE6QSizeF',
        self._valueOf(margin),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setRowAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setRowAxis(QCategory3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setRowAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::setRowAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem10setRowAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def setColumnAxis(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setColumnAxis(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setColumnAxis

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::setColumnAxis(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem13setColumnAxisEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setValueAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setValueAxis(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setValueAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::setValueAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem12setValueAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(float)
  def setFloorLevel(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::setFloorLevel(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#setFloorLevel

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::setFloorLevel(float level)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem13setFloorLevelEf', level,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Q3DBarsWidgetItem::Q3DBarsWidgetItem(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#Q3DBarsWidgetItem

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DBarsWidgetItem::Q3DBarsWidgetItem(QObject *parent)
    self._noteCreation(Q3DBarsWidgetItem, lambda: Rituals.call(
        'ritual_ZN17Q3DBarsWidgetItemC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QBar3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::addSeries(QBar3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#addSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::addSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem9addSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::removeSeries(QBar3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#removeSeries

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::removeSeries(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem12removeSeriesEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(int, QBar3DSeries)
  @overload(int, NoneType)
  def insertSeries(self, index: int, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::insertSeries(int index, QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#insertSeries

    Parameters
    ----------

    index : int
      Passed on as it is.

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::insertSeries(int index, QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem12insertSeriesEiP12QBar3DSeries',
        index, self._addressOf(series),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::addAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::addAxis(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem7addAxisEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::releaseAxis(QAbstract3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::releaseAxis(QAbstract3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem11releaseAxisEP15QAbstract3DAxis',
        self._addressOf(axis),
    )

  @overload(int, QtGraphs3D.SliceCaptureType)
  def renderSliceToImage(
      self,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::renderSliceToImage(int
    requestedIndex, QtGraphs3D::SliceCaptureType sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#renderSliceToImage

    Parameters
    ----------

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.
    """
    #  void Q3DBarsWidgetItem::renderSliceToImage(int requestedIndex,
    #      QtGraphs3D::SliceCaptureType sliceType)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem18renderSliceToImageEiN10QtGraphs3D16S'
        'liceCaptureTypeE',
        requestedIndex, sliceType.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Q3DBarsWidgetItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Q3DBarsWidgetItem::event(QEvent *event)
    ritual = 'ritual_ZN17Q3DBarsWidgetItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17Q3DBarsWidgetItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def multiSeriesUniformChanged(self, uniform: bool) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::multiSeriesUniformChanged(bool
    uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#multiSeriesUniformChanged

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::multiSeriesUniformChanged(bool uniform)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem25multiSeriesUniformChangedEb', uniform,
    )

  @overload(float)
  def barThicknessChanged(self, thicknessRatio: float) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::barThicknessChanged(float
    thicknessRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barThicknessChanged

    Parameters
    ----------

    thicknessRatio : float
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::barThicknessChanged(float thicknessRatio)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem19barThicknessChangedEf',
        thicknessRatio,
    )

  @overload(QSizeF)
  def barSpacingChanged(self, spacing: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::barSpacingChanged(QSizeF spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barSpacingChanged

    Parameters
    ----------

    spacing : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBarsWidgetItem::barSpacingChanged(QSizeF spacing)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem17barSpacingChangedE6QSizeF',
        self._valueOf(spacing),
    )

  @overload(bool)
  def barSpacingRelativeChanged(self, relative: bool) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::barSpacingRelativeChanged(bool
    relative)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barSpacingRelativeChanged

    Parameters
    ----------

    relative : bool
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::barSpacingRelativeChanged(bool relative)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem25barSpacingRelativeChangedEb',
        relative,
    )

  @overload(QSizeF)
  def barSeriesMarginChanged(self, margin: QSizeF) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::barSeriesMarginChanged(QSizeF
    margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#barSeriesMarginChanged

    Parameters
    ----------

    margin : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void Q3DBarsWidgetItem::barSeriesMarginChanged(QSizeF margin)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem22barSeriesMarginChangedE6QSizeF',
        self._valueOf(margin),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def rowAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::rowAxisChanged(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#rowAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::rowAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem14rowAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QCategory3DAxis)
  @overload(NoneType)
  def columnAxisChanged(self, axis: Optional[QCategory3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::columnAxisChanged(QCategory3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#columnAxisChanged

    Parameters
    ----------

    axis : Optional[QCategory3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::columnAxisChanged(QCategory3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem17columnAxisChangedEP15QCategory3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def valueAxisChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::valueAxisChanged(QValue3DAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#valueAxisChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::valueAxisChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem16valueAxisChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def primarySeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::primarySeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#primarySeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::primarySeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem20primarySeriesChangedEP12QBar3DSeries',
        self._addressOf(series),
    )

  @overload(QBar3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(self, series: Optional[QBar3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::selectedSeriesChanged(QBar3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QBar3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DBarsWidgetItem::selectedSeriesChanged(QBar3DSeries *series)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem21selectedSeriesChangedEP12QBar3DSerie'
        's',
        self._addressOf(series),
    )

  @overload(float)
  def floorLevelChanged(self, level: float) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::floorLevelChanged(float level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#floorLevelChanged

    Parameters
    ----------

    level : float
      Passed on as it is.
    """
    #  void Q3DBarsWidgetItem::floorLevelChanged(float level)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem17floorLevelChangedEf', level,
    )

  @overload(QImage)
  def sliceImageChanged(self, image: QImage) -> None:
    """
    Calls Qt's 'void Q3DBarsWidgetItem::sliceImageChanged(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dbarswidgetitem.html#sliceImageChanged

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void Q3DBarsWidgetItem::sliceImageChanged(const QImage &image)
    self.uglySide.call(
        'ritual_ZN17Q3DBarsWidgetItem17sliceImageChangedERK6QImage',
        self._valueOf(image),
    )

  def d_func(self) -> Optional[Q3DBarsWidgetItemPrivate]:
    """
    Calls Qt's 'Q3DBarsWidgetItemPrivate *Q3DBarsWidgetItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#d_func

    Returns
    -------

    Optional[Q3DBarsWidgetItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DBarsWidgetItemPrivate *Q3DBarsWidgetItem::d_func()
    address = self.uglySide.call('ritual_ZN17Q3DBarsWidgetItem6d_funcEv')
    from . import Q3DBarsWidgetItemPrivate
    return Q3DBarsWidgetItemPrivate._cuteAt(address)

  def graphBars(self) -> Optional[QQuickGraphsBars]:
    """
    Calls Qt's 'QQuickGraphsBars *Q3DBarsWidgetItem::graphBars()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dbarswidgetitem.html#graphBars

    Returns
    -------

    Optional[QQuickGraphsBars]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphsBars *Q3DBarsWidgetItem::graphBars()
    address = self.uglySide.call('ritual_ZN17Q3DBarsWidgetItem9graphBarsEv')
    from ..QtGraphs import QQuickGraphsBars
    return QQuickGraphsBars._cuteAt(address)
