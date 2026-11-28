"""
Q3DSurfaceWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphsWidgets/q3dsurfacewidgetitem.h, Qt 6.12.0. Changes made here are
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

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QImage
  from ..QtGraphs import QQuickGraphsSurface, QSurface3DSeries, QValue3DAxis
  from . import Q3DSurfaceWidgetItemPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QImage = WAIT['QImage']
  QSurface3DSeries = WAIT['QtGraphs:QSurface3DSeries']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DSurfaceWidgetItem(Q3DGraphsWidgetItem):
  """
  The cute side of Qt's Q3DSurfaceWidgetItem: a plain Python object standing
  in front of one C++ Q3DSurfaceWidgetItem.

  It is built on the cute 'Q3DGraphsWidgetItem', as Qt's Q3DSurfaceWidgetItem
  is built on Qt's Q3DGraphsWidgetItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DSurfaceWidgetItem that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr', 'addSeries',
  'removeSeries', 'seriesList', 'axisX', 'axisY', 'axisZ', 'addAxis',
  'releaseAxis', 'axes', 'selectedSeries', 'flipHorizontalGrid',
  'renderSliceToImage', 'setAxisX', 'setAxisY', 'setAxisZ',
  'setFlipHorizontalGrid', 'event', 'axisXChanged', 'axisYChanged',
  'axisZChanged', 'selectedSeriesChanged', 'flipHorizontalGridChanged',
  'sliceImageChanged', 'd_func', 'graphSurface'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DSurfaceWidgetItem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Q3DSurfaceWidgetItem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DSurfaceWidgetItem::~Q3DSurfaceWidgetItem()': the destructor:
    Python never removes a C++ Q3DSurfaceWidgetItem.
  - Qt's 'const Q3DSurfaceWidgetItemPrivate *Q3DSurfaceWidgetItem::d_func()
    const': takes in Python what 'Q3DSurfaceWidgetItemPrivate
    *Q3DSurfaceWidgetItem::d_func()' takes.
  - Qt's 'const QQuickGraphsSurface *Q3DSurfaceWidgetItem::graphSurface()
    const': takes in Python what 'QQuickGraphsSurface
    *Q3DSurfaceWidgetItem::graphSurface()' takes.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Q3DSurfaceWidgetItem is created at the first use, not by
    'Q3DSurfaceWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DSurfaceWidgetItem.
  - Qt tells when it has removed the C++ Q3DSurfaceWidgetItem. Every call on
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
    Calls Qt's 'QString Q3DSurfaceWidgetItem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#tr

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
    #  QString Q3DSurfaceWidgetItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20Q3DSurfaceWidgetItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DSurfaceWidgetItem'

  #  A C++ Q3DSurfaceWidgetItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DSurfaceWidgetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DSurfaceWidgetItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DSurfaceWidgetItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20Q3DSurfaceWidgetItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seriesList(self) -> QList[QSurface3DSeries]:
    """
    Calls Qt's 'QList<QSurface3DSeries *> Q3DSurfaceWidgetItem::seriesList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#seriesList

    Returns
    -------

    QList[QSurface3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSurface3DSeries *> Q3DSurfaceWidgetItem::seriesList() const
    address = self.uglySide.call(
        'ritual_ZNK20Q3DSurfaceWidgetItem10seriesListEv',
    )
    from ..QtGraphs import QSurface3DSeries
    return QList[QSurface3DSeries]._cuteOwning(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DSurfaceWidgetItem::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DSurfaceWidgetItem::axisX() const
    address = self.uglySide.call('ritual_ZNK20Q3DSurfaceWidgetItem5axisXEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DSurfaceWidgetItem::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DSurfaceWidgetItem::axisY() const
    address = self.uglySide.call('ritual_ZNK20Q3DSurfaceWidgetItem5axisYEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DSurfaceWidgetItem::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DSurfaceWidgetItem::axisZ() const
    address = self.uglySide.call('ritual_ZNK20Q3DSurfaceWidgetItem5axisZEv')
    from ..QtGraphs import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axes(self) -> QList[QValue3DAxis]:
    """
    Calls Qt's 'QList<QValue3DAxis *> Q3DSurfaceWidgetItem::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axes

    Returns
    -------

    QList[QValue3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QValue3DAxis *> Q3DSurfaceWidgetItem::axes() const
    address = self.uglySide.call('ritual_ZNK20Q3DSurfaceWidgetItem4axesEv')
    from ..QtGraphs import QValue3DAxis
    return QList[QValue3DAxis]._cuteOwning(address)

  def selectedSeries(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *Q3DSurfaceWidgetItem::selectedSeries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#selectedSeries

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *Q3DSurfaceWidgetItem::selectedSeries() const
    address = self.uglySide.call(
        'ritual_ZNK20Q3DSurfaceWidgetItem14selectedSeriesEv',
    )
    from ..QtGraphs import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def flipHorizontalGrid(self) -> bool:
    """
    Calls Qt's 'bool Q3DSurfaceWidgetItem::flipHorizontalGrid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#flipHorizontalGrid
    """
    #  bool Q3DSurfaceWidgetItem::flipHorizontalGrid() const
    return self.uglySide.call(
        'ritual_ZNK20Q3DSurfaceWidgetItem18flipHorizontalGridEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def setFlipHorizontalGrid(self, flip: bool) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::setFlipHorizontalGrid(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#setFlipHorizontalGrid

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Q3DSurfaceWidgetItem::setFlipHorizontalGrid(bool flip)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem21setFlipHorizontalGridEb', flip,
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
    'Q3DSurfaceWidgetItem::Q3DSurfaceWidgetItem(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#Q3DSurfaceWidgetItem

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DSurfaceWidgetItem::Q3DSurfaceWidgetItem(QObject *parent)
    self._noteCreation(Q3DSurfaceWidgetItem, lambda: Rituals.call(
        'ritual_ZN20Q3DSurfaceWidgetItemC1EP7QObject',
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

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::addSeries(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#addSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::addSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem9addSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::removeSeries(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#removeSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::removeSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem12removeSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::addAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#addAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::addAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem7addAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::releaseAxis(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::releaseAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem11releaseAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(int, int, QtGraphs3D.SliceCaptureType)
  def renderSliceToImage(
      self,
      index: int,
      requestedIndex: int,
      sliceType: QtGraphs3D.SliceCaptureType,
  ) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::renderSliceToImage(int index, int
    requestedIndex, QtGraphs3D::SliceCaptureType sliceType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#renderSliceToImage

    Parameters
    ----------

    index : int
      Passed on as it is.

    requestedIndex : int
      Passed on as it is.

    sliceType : QtGraphs3D.SliceCaptureType
      Passed on as its number.
    """
    #  void Q3DSurfaceWidgetItem::renderSliceToImage(int index, int
    #      requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem18renderSliceToImageEiiN10QtGraphs3'
        'D16SliceCaptureTypeE',
        index, requestedIndex, sliceType.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Q3DSurfaceWidgetItem::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Q3DSurfaceWidgetItem::event(QEvent *event)
    ritual = 'ritual_ZN20Q3DSurfaceWidgetItem5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20Q3DSurfaceWidgetItem5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void
    Q3DSurfaceWidgetItem::selectedSeriesChanged(QSurface3DSeries *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurfaceWidgetItem::selectedSeriesChanged(QSurface3DSeries
    #      *series)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem21selectedSeriesChangedEP16QSurface'
        '3DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def flipHorizontalGridChanged(self, flip: bool) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::flipHorizontalGridChanged(bool
    flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Q3DSurfaceWidgetItem::flipHorizontalGridChanged(bool flip)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem25flipHorizontalGridChangedEb', flip,
    )

  @overload(QImage)
  def sliceImageChanged(self, image: QImage) -> None:
    """
    Calls Qt's 'void Q3DSurfaceWidgetItem::sliceImageChanged(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#sliceImageChanged

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void Q3DSurfaceWidgetItem::sliceImageChanged(const QImage &image)
    self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem17sliceImageChangedERK6QImage',
        self._valueOf(image),
    )

  def d_func(self) -> Optional[Q3DSurfaceWidgetItemPrivate]:
    """
    Calls Qt's 'Q3DSurfaceWidgetItemPrivate *Q3DSurfaceWidgetItem::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#d_func

    Returns
    -------

    Optional[Q3DSurfaceWidgetItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DSurfaceWidgetItemPrivate *Q3DSurfaceWidgetItem::d_func()
    address = self.uglySide.call('ritual_ZN20Q3DSurfaceWidgetItem6d_funcEv')
    from . import Q3DSurfaceWidgetItemPrivate
    return Q3DSurfaceWidgetItemPrivate._cuteAt(address)

  def graphSurface(self) -> Optional[QQuickGraphsSurface]:
    """
    Calls Qt's 'QQuickGraphsSurface *Q3DSurfaceWidgetItem::graphSurface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurfacewidgetitem.html#graphSurface

    Returns
    -------

    Optional[QQuickGraphsSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGraphsSurface *Q3DSurfaceWidgetItem::graphSurface()
    address = self.uglySide.call(
        'ritual_ZN20Q3DSurfaceWidgetItem12graphSurfaceEv',
    )
    from ..QtGraphs import QQuickGraphsSurface
    return QQuickGraphsSurface._cuteAt(address)
