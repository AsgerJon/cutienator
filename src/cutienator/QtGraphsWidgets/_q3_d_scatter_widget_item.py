"""
Q3DScatterWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphsWidgets/q3dscatterwidgetitem.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import Q3DGraphsWidgetItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGraphs import QQuickGraphsScatter, QScatter3DSeries, QValue3DAxis
  from . import Q3DScatterWidgetItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QScatter3DSeries = WAIT['QtGraphs:QScatter3DSeries']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DScatterWidgetItem(Q3DGraphsWidgetItem):
  """
  The cute side of Qt's Q3DScatterWidgetItem: a plain Python object standing
  in front of one C++ Q3DScatterWidgetItem.

  It is built on the cute 'Q3DGraphsWidgetItem', as Qt's Q3DScatterWidgetItem
  is built on Qt's Q3DGraphsWidgetItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DScatterWidgetItem that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'addSeries',
  'removeSeries', 'seriesList', 'axisX', 'axisY', 'axisZ', 'addAxis',
  'releaseAxis', 'axes', 'selectedSeries', 'setAxisX', 'setAxisY',
  'setAxisZ', 'event', 'axisXChanged', 'axisYChanged', 'axisZChanged',
  'selectedSeriesChanged', 'd_func', 'graphScatter'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DScatterWidgetItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Q3DScatterWidgetItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DScatterWidgetItem::~Q3DScatterWidgetItem()': the destructor:
    Python never removes a C++ Q3DScatterWidgetItem.
  - Qt's 'const Q3DScatterWidgetItemPrivate *Q3DScatterWidgetItem::d_func()
    const': takes in Python what 'Q3DScatterWidgetItemPrivate
    *Q3DScatterWidgetItem::d_func()' takes.
  - Qt's 'const QQuickGraphsScatter *Q3DScatterWidgetItem::graphScatter()
    const': takes in Python what 'QQuickGraphsScatter
    *Q3DScatterWidgetItem::graphScatter()' takes.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DScatterWidgetItem is created at the first use, not by
    'Q3DScatterWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DScatterWidgetItem.
  - Qt tells when it has removed the C++ Q3DScatterWidgetItem. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Q3DScatterWidgetItem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#tr

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
    #  QString Q3DScatterWidgetItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20Q3DScatterWidgetItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DScatterWidgetItem'

  #  A C++ Q3DScatterWidgetItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DScatterWidgetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DScatterWidgetItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DScatterWidgetItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20Q3DScatterWidgetItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seriesList(self) -> QList[QScatter3DSeries]:
    """
    Calls Qt's 'QList<QScatter3DSeries *> Q3DScatterWidgetItem::seriesList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#seriesList

    Returns
    -------

    QList[QScatter3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScatter3DSeries *> Q3DScatterWidgetItem::seriesList() const
    address = self.uglySide.call(
        'ritual_ZNK20Q3DScatterWidgetItem10seriesListEv',
    )
    from ..QtGraphs import QScatter3DSeries
    return QList[QScatter3DSeries]._cuteOwning(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DScatterWidgetItem::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DScatterWidgetItem::axisX() const
    address = self.uglySide.call('ritual_ZNK20Q3DScatterWidgetItem5axisXEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DScatterWidgetItem::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DScatterWidgetItem::axisY() const
    address = self.uglySide.call('ritual_ZNK20Q3DScatterWidgetItem5axisYEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DScatterWidgetItem::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DScatterWidgetItem::axisZ() const
    address = self.uglySide.call('ritual_ZNK20Q3DScatterWidgetItem5axisZEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axes(self) -> QList[QValue3DAxis]:
    """
    Calls Qt's 'QList<QValue3DAxis *> Q3DScatterWidgetItem::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axes

    Returns
    -------

    QList[QValue3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QValue3DAxis *> Q3DScatterWidgetItem::axes() const
    address = self.uglySide.call('ritual_ZNK20Q3DScatterWidgetItem4axesEv')
    from ..QtGraphs import QValue3DAxis
    return QList[QValue3DAxis]._cuteOwning(address)

  def selectedSeries(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *Q3DScatterWidgetItem::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#selectedSeries

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *Q3DScatterWidgetItem::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK20Q3DScatterWidgetItem14selectedSeriesEv',
    )
    from ..QtGraphs import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
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
    'Q3DScatterWidgetItem::Q3DScatterWidgetItem(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#Q3DScatterWidgetItem

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DScatterWidgetItem::Q3DScatterWidgetItem(QObject *parent)
    self._noteCreation(Q3DScatterWidgetItem, lambda: Rituals.call(
        'ritual_ZN20Q3DScatterWidgetItemC1EP7QObject',
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

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::addSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#addSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::addSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem9addSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::removeSeries(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#removeSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::removeSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem12removeSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::addAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#addAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::addAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem7addAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::releaseAxis(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::releaseAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem11releaseAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Q3DScatterWidgetItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Q3DScatterWidgetItem::event(QEvent *event)
    ritual = 'ritual_ZN20Q3DScatterWidgetItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Q3DScatterWidgetItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatterWidgetItem::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    Q3DScatterWidgetItem::selectedSeriesChanged(QScatter3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatterWidgetItem::selectedSeriesChanged(QScatter3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem21selectedSeriesChangedEP16QScatter'
        '3DSeries',
        self._addressOf(series),
    )

  def d_func(self) -> Optional[Q3DScatterWidgetItemPrivate]:
    """
    Calls Qt's 'Q3DScatterWidgetItemPrivate *Q3DScatterWidgetItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#d_func

    Returns
    -------

    Optional[Q3DScatterWidgetItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScatterWidgetItemPrivate *Q3DScatterWidgetItem::d_func()
    address = self.uglySide.call('ritual_ZN20Q3DScatterWidgetItem6d_funcEv')
    from . import Q3DScatterWidgetItemPrivate
    return Q3DScatterWidgetItemPrivate._cuteAt(address)

  def graphScatter(self) -> Optional[QQuickGraphsScatter]:
    """
    Calls Qt's 'QQuickGraphsScatter *Q3DScatterWidgetItem::graphScatter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatterwidgetitem.html#graphScatter

    Returns
    -------

    Optional[QQuickGraphsScatter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphsScatter *Q3DScatterWidgetItem::graphScatter()
    address = self.uglySide.call(
        'ritual_ZN20Q3DScatterWidgetItem12graphScatterEv',
    )
    from ..QtGraphs import QQuickGraphsScatter
    return QQuickGraphsScatter._cuteAt(address)
