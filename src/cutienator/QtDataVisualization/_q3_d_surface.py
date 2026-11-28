"""
Q3DSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dsurface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QWindow
from . import QAbstract3DGraph

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QSurfaceFormat
  from . import Q3DSurfacePrivate, QSurface3DSeries, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSurface3DSeries = WAIT['QtDataVisualization:QSurface3DSeries']
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QValue3DAxis = WAIT['QtDataVisualization:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DSurface(QAbstract3DGraph):
  """
  The cute side of Qt's Q3DSurface: a plain Python object standing in front
  of one C++ Q3DSurface.

  It is built on the cute 'QAbstract3DGraph', as Qt's Q3DSurface is built on
  Qt's QAbstract3DGraph, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DSurface that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'addSeries',
  'removeSeries', 'seriesList', 'setAxisX', 'axisX', 'setAxisY', 'axisY',
  'setAxisZ', 'axisZ', 'addAxis', 'releaseAxis', 'axes', 'selectedSeries',
  'setFlipHorizontalGrid', 'flipHorizontalGrid', 'axisXChanged',
  'axisYChanged', 'axisZChanged', 'selectedSeriesChanged',
  'flipHorizontalGridChanged', 'dptr', 'dptrc'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DSurface::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int Q3DSurface::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DSurface::~Q3DSurface()': the destructor: Python never removes a
    C++ Q3DSurface.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DSurface is created at the first use, not by 'Q3DSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DSurface.
  - Qt tells when it has removed the C++ Q3DSurface. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString Q3DSurface::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#tr

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
    #  QString Q3DSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Q3DSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DSurface'

  #  A C++ Q3DSurface Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DSurface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DSurface::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DSurface::metaObject() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seriesList(self) -> QList[QSurface3DSeries]:
    """
    Calls Qt's 'QList<QSurface3DSeries *> Q3DSurface::seriesList() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#seriesList

    Returns
    -------

    QList[QSurface3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSurface3DSeries *> Q3DSurface::seriesList() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface10seriesListEv')
    from . import QSurface3DSeries
    return QList[QSurface3DSeries]._cuteOwning(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DSurface::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DSurface::axisX() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface5axisXEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DSurface::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DSurface::axisY() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface5axisYEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DSurface::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DSurface::axisZ() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface5axisZEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axes(self) -> QList[QValue3DAxis]:
    """
    Calls Qt's 'QList<QValue3DAxis *> Q3DSurface::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axes

    Returns
    -------

    QList[QValue3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QValue3DAxis *> Q3DSurface::axes() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface4axesEv')
    from . import QValue3DAxis
    return QList[QValue3DAxis]._cuteOwning(address)

  def selectedSeries(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *Q3DSurface::selectedSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#selectedSeries

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *Q3DSurface::selectedSeries() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface14selectedSeriesEv')
    from . import QSurface3DSeries
    return QSurface3DSeries._cuteAt(address)

  def flipHorizontalGrid(self) -> bool:
    """
    Calls Qt's 'bool Q3DSurface::flipHorizontalGrid() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#flipHorizontalGrid
    """
    #  bool Q3DSurface::flipHorizontalGrid() const
    return self.uglySide.call('ritual_ZNK10Q3DSurface18flipHorizontalGridEv')

  def dptrc(self) -> Optional[Q3DSurfacePrivate]:
    """
    Calls Qt's 'const Q3DSurfacePrivate *Q3DSurface::dptrc() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#dptrc

    Returns
    -------

    Optional[Q3DSurfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Q3DSurfacePrivate *Q3DSurface::dptrc() const
    address = self.uglySide.call('ritual_ZNK10Q3DSurface5dptrcEv')
    from . import Q3DSurfacePrivate
    return Q3DSurfacePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(bool)
  def setFlipHorizontalGrid(self, flip: bool) -> None:
    """
    Calls Qt's 'void Q3DSurface::setFlipHorizontalGrid(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurface.html#setFlipHorizontalGrid

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Q3DSurface::setFlipHorizontalGrid(bool flip)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface21setFlipHorizontalGridEb', flip,
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
  @overload(QSurfaceFormat)
  @overload(NoneType)
  @overload(QSurfaceFormat, QWindow)
  @overload(QSurfaceFormat, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      format: Optional[QSurfaceFormat] = None,
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Q3DSurface::Q3DSurface(const
    QSurfaceFormat *format, QWindow *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#Q3DSurface

    Parameters
    ----------

    format : Optional[QSurfaceFormat]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DSurface::Q3DSurface(const QSurfaceFormat *format, QWindow *parent)
    self._noteCreation(Q3DSurface, lambda: Rituals.call(
        'ritual_ZN10Q3DSurfaceC1EPK14QSurfaceFormatP7QWindow',
        self._addressOf(format), self._addressOf(parent),
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
    Calls Qt's 'void Q3DSurface::addSeries(QSurface3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#addSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::addSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface9addSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QSurface3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DSurface::removeSeries(QSurface3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#removeSeries

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::removeSeries(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface12removeSeriesEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::addAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#addAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::addAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface7addAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::releaseAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::releaseAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface11releaseAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DSurface::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QSurface3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QSurface3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Q3DSurface::selectedSeriesChanged(QSurface3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurface.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QSurface3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DSurface::selectedSeriesChanged(QSurface3DSeries *series)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface21selectedSeriesChangedEP16QSurface3DSeries',
        self._addressOf(series),
    )

  @overload(bool)
  def flipHorizontalGridChanged(self, flip: bool) -> None:
    """
    Calls Qt's 'void Q3DSurface::flipHorizontalGridChanged(bool flip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsurface.html#flipHorizontalGridChanged

    Parameters
    ----------

    flip : bool
      Passed on as it is.
    """
    #  void Q3DSurface::flipHorizontalGridChanged(bool flip)
    self.uglySide.call(
        'ritual_ZN10Q3DSurface25flipHorizontalGridChangedEb', flip,
    )

  def dptr(self) -> Optional[Q3DSurfacePrivate]:
    """
    Calls Qt's 'Q3DSurfacePrivate *Q3DSurface::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsurface.html#dptr

    Returns
    -------

    Optional[Q3DSurfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DSurfacePrivate *Q3DSurface::dptr()
    address = self.uglySide.call('ritual_ZN10Q3DSurface4dptrEv')
    from . import Q3DSurfacePrivate
    return Q3DSurfacePrivate._cuteAt(address)
