"""
Q3DScatter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dscatter.h, Qt 6.12.0. Changes made here are lost.
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
  from . import Q3DScatterPrivate, QScatter3DSeries, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScatter3DSeries = WAIT['QtDataVisualization:QScatter3DSeries']
  QSurfaceFormat = WAIT['QSurfaceFormat']
  QValue3DAxis = WAIT['QtDataVisualization:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DScatter(QAbstract3DGraph):
  """
  The cute side of Qt's Q3DScatter: a plain Python object standing in front
  of one C++ Q3DScatter.

  It is built on the cute 'QAbstract3DGraph', as Qt's Q3DScatter is built on
  Qt's QAbstract3DGraph, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DScatter that has a ritual and that Python can
  call so far, 21 names in all: 'metaObject', 'tr', 'addSeries',
  'removeSeries', 'seriesList', 'setAxisX', 'axisX', 'setAxisY', 'axisY',
  'setAxisZ', 'axisZ', 'addAxis', 'releaseAxis', 'axes', 'selectedSeries',
  'axisXChanged', 'axisYChanged', 'axisZChanged', 'selectedSeriesChanged',
  'dptr', 'dptrc'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DScatter::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int Q3DScatter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DScatter::~Q3DScatter()': the destructor: Python never removes a
    C++ Q3DScatter.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DScatter is created at the first use, not by 'Q3DScatter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DScatter.
  - Qt tells when it has removed the C++ Q3DScatter. Every call on the cute
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
    Calls Qt's 'QString Q3DScatter::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#tr

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
    #  QString Q3DScatter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Q3DScatter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DScatter'

  #  A C++ Q3DScatter Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DScatter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DScatter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DScatter::metaObject() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seriesList(self) -> QList[QScatter3DSeries]:
    """
    Calls Qt's 'QList<QScatter3DSeries *> Q3DScatter::seriesList() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#seriesList

    Returns
    -------

    QList[QScatter3DSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScatter3DSeries *> Q3DScatter::seriesList() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter10seriesListEv')
    from . import QScatter3DSeries
    return QList[QScatter3DSeries]._cuteOwning(address)

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DScatter::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DScatter::axisX() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter5axisXEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DScatter::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DScatter::axisY() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter5axisYEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *Q3DScatter::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *Q3DScatter::axisZ() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter5axisZEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axes(self) -> QList[QValue3DAxis]:
    """
    Calls Qt's 'QList<QValue3DAxis *> Q3DScatter::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axes

    Returns
    -------

    QList[QValue3DAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QValue3DAxis *> Q3DScatter::axes() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter4axesEv')
    from . import QValue3DAxis
    return QList[QValue3DAxis]._cuteOwning(address)

  def selectedSeries(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *Q3DScatter::selectedSeries() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#selectedSeries

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *Q3DScatter::selectedSeries() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter14selectedSeriesEv')
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)

  def dptrc(self) -> Optional[Q3DScatterPrivate]:
    """
    Calls Qt's 'const Q3DScatterPrivate *Q3DScatter::dptrc() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#dptrc

    Returns
    -------

    Optional[Q3DScatterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Q3DScatterPrivate *Q3DScatter::dptrc() const
    address = self.uglySide.call('ritual_ZNK10Q3DScatter5dptrcEv')
    from . import Q3DScatterPrivate
    return Q3DScatterPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter8setAxisZEP12QValue3DAxis',
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
    Notes what was given, for Qt's 'Q3DScatter::Q3DScatter(const
    QSurfaceFormat *format, QWindow *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#Q3DScatter

    Parameters
    ----------

    format : Optional[QSurfaceFormat]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DScatter::Q3DScatter(const QSurfaceFormat *format, QWindow *parent)
    self._noteCreation(Q3DScatter, lambda: Rituals.call(
        'ritual_ZN10Q3DScatterC1EPK14QSurfaceFormatP7QWindow',
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

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DScatter::addSeries(QScatter3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#addSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::addSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter9addSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QScatter3DSeries]) -> None:
    """
    Calls Qt's 'void Q3DScatter::removeSeries(QScatter3DSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#removeSeries

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::removeSeries(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter12removeSeriesEP16QScatter3DSeries',
        self._addressOf(series),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def addAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::addAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#addAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::addAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter7addAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def releaseAxis(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::releaseAxis(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#releaseAxis

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::releaseAxis(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter11releaseAxisEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void Q3DScatter::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QScatter3DSeries)
  @overload(NoneType)
  def selectedSeriesChanged(
      self,
      series: Optional[QScatter3DSeries],
  ) -> None:
    """
    Calls Qt's 'void Q3DScatter::selectedSeriesChanged(QScatter3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscatter.html#selectedSeriesChanged

    Parameters
    ----------

    series : Optional[QScatter3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DScatter::selectedSeriesChanged(QScatter3DSeries *series)
    self.uglySide.call(
        'ritual_ZN10Q3DScatter21selectedSeriesChangedEP16QScatter3DSeries',
        self._addressOf(series),
    )

  def dptr(self) -> Optional[Q3DScatterPrivate]:
    """
    Calls Qt's 'Q3DScatterPrivate *Q3DScatter::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscatter.html#dptr

    Returns
    -------

    Optional[Q3DScatterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScatterPrivate *Q3DScatter::dptr()
    address = self.uglySide.call('ritual_ZN10Q3DScatter4dptrEv')
    from . import Q3DScatterPrivate
    return Q3DScatterPrivate._cuteAt(address)
