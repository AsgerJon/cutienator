"""
QLegendPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qlegend_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QLegendPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtWidgets import QGraphicsItemGroup
  from . import ChartPresenter, QAbstractSeries, QChart, QLegend
  from . import QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartPresenter = WAIT['ChartPresenter']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QChart = WAIT['QChart']
  QLegend = WAIT['QLegend']
  QLegendMarker = WAIT['QLegendMarker']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLegendPrivate(QObject):
  """
  The cute side of Qt's QLegendPrivate: a plain Python object standing in
  front of one C++ QLegendPrivate.

  It is built on the cute 'QObject', as Qt's QLegendPrivate is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLegendPrivate that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'setOffset', 'offset',
  'roundness', 'items', 'markers', 'maxMarkerWidth', 'relatedObject',
  'handleSeriesAdded', 'handleSeriesRemoved', 'handleSeriesVisibleChanged',
  'handleCountChanged', 'insertMarkerHelper', 'addMarkers',
  'removeMarkerHelper', 'removeMarkers', 'decorateMarker', 'decorateMarkers',
  'updateToolTips'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLegendPrivate::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLegendPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QLegendPrivate::~QLegendPrivate()': the destructor: Python never
    removes a C++ QLegendPrivate.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLegendPrivate is created at the first use, not by
    'QLegendPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLegendPrivate.
  - Qt tells when it has removed the C++ QLegendPrivate. Every call on the
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
    Calls Qt's 'QString QLegendPrivate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#tr

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
    #  QString QLegendPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QLegendPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QLegendMarker)
  @overload(NoneType)
  def relatedObject(l: Optional[QLegendMarker]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QLegendPrivate::relatedObject(const QLegendMarker
    *l)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#relatedObject

    Parameters
    ----------

    l : Optional[QLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QLegendPrivate::relatedObject(const QLegendMarker *l)
    address = Rituals.call(
        'ritual_ZN14QLegendPrivate13relatedObjectEPK13QLegendMarker',
        CuteMixin._addressOf(l),
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLegendPrivate'

  #  A C++ QLegendPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLegendPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLegendPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLegendPrivate::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QLegendPrivate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QLegendPrivate::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QLegendPrivate::offset() const
    address = self.uglySide.call('ritual_ZNK14QLegendPrivate6offsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def maxMarkerWidth(self) -> float:
    """
    Calls Qt's 'qreal QLegendPrivate::maxMarkerWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#maxMarkerWidth
    """
    #  qreal QLegendPrivate::maxMarkerWidth() const
    return self.uglySide.call('ritual_ZNK14QLegendPrivate14maxMarkerWidthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setOffset(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QLegendPrivate::setOffset(const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#setOffset

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QLegendPrivate::setOffset(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate9setOffsetERK7QPointF',
        self._valueOf(offset, 'QPointF'),
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

  @overload(ChartPresenter, QChart, QLegend)
  @overload(ChartPresenter, QChart, NoneType)
  @overload(ChartPresenter, NoneType, QLegend)
  @overload(ChartPresenter, NoneType, NoneType)
  @overload(NoneType, QChart, QLegend)
  @overload(NoneType, QChart, NoneType)
  @overload(NoneType, NoneType, QLegend)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      presenter: Optional[ChartPresenter],
      chart: Optional[QChart],
      q: Optional[QLegend],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QLegendPrivate::QLegendPrivate(ChartPresenter *presenter, QChart *chart,
    QLegend *q)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#QLegendPrivate

    Parameters
    ----------

    presenter : Optional[ChartPresenter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    q : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QLegendPrivate::QLegendPrivate(ChartPresenter *presenter, QChart
    #      *chart, QLegend *q)
    self._noteCreation(QLegendPrivate, lambda: Rituals.call(
        'ritual_ZN14QLegendPrivateC1EP14ChartPresenterP6QChartP7QLegend',
        self._addressOf(presenter), self._addressOf(chart),
        self._addressOf(q),
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

  @overload(float)
  def roundness(self, size: float) -> int:
    """
    Calls Qt's 'int QLegendPrivate::roundness(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#roundness

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  int QLegendPrivate::roundness(qreal size)
    return self.uglySide.call('ritual_ZN14QLegendPrivate9roundnessEd', size)

  def items(self) -> Optional[QGraphicsItemGroup]:
    """
    Calls Qt's 'QGraphicsItemGroup *QLegendPrivate::items()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#items

    Returns
    -------

    Optional[QGraphicsItemGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemGroup *QLegendPrivate::items()
    address = self.uglySide.call('ritual_ZN14QLegendPrivate5itemsEv')
    from ..QtWidgets import QGraphicsItemGroup
    return QGraphicsItemGroup._cuteAt(address)

  @overload()
  @overload(QAbstractSeries)
  @overload(NoneType)
  def markers(
      self,
      series: Optional[QAbstractSeries] = None,
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QLegendPrivate::markers(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#markers

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QLegendMarker]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLegendMarker *> QLegendPrivate::markers(QAbstractSeries
    #      *series)
    address = self.uglySide.call(
        'ritual_ZN14QLegendPrivate7markersEP15QAbstractSeries',
        self._addressOf(series),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::handleSeriesAdded(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#handleSeriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegendPrivate::handleSeriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate17handleSeriesAddedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def handleSeriesRemoved(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::handleSeriesRemoved(QAbstractSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#handleSeriesRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegendPrivate::handleSeriesRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate19handleSeriesRemovedEP15QAbstractSeries',
        self._addressOf(series),
    )

  def handleSeriesVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QLegendPrivate::handleSeriesVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#handleSeriesVisibleChanged
    """
    #  void QLegendPrivate::handleSeriesVisibleChanged()
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate26handleSeriesVisibleChangedEv',
    )

  def handleCountChanged(self) -> None:
    """
    Calls Qt's 'void QLegendPrivate::handleCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#handleCountChanged
    """
    #  void QLegendPrivate::handleCountChanged()
    self.uglySide.call('ritual_ZN14QLegendPrivate18handleCountChangedEv')

  @overload(QLegendMarker)
  @overload(NoneType)
  def insertMarkerHelper(self, marker: Optional[QLegendMarker]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::insertMarkerHelper(QLegendMarker
    *marker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#insertMarkerHelper

    Parameters
    ----------

    marker : Optional[QLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegendPrivate::insertMarkerHelper(QLegendMarker *marker)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate18insertMarkerHelperEP13QLegendMarker',
        self._addressOf(marker),
    )

  @overload(QList[QLegendMarker])
  def addMarkers(self, markers: QList[QLegendMarker]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::addMarkers(const QList<QLegendMarker *>
    &markers)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#addMarkers

    Parameters
    ----------

    markers : QList[QLegendMarker]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLegendPrivate::addMarkers(const QList<QLegendMarker *> &markers)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate10addMarkersERK5QListIP13QLegendMarkerE',
        self._valueOf(markers),
    )

  @overload(QLegendMarker)
  @overload(NoneType)
  def removeMarkerHelper(self, marker: Optional[QLegendMarker]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::removeMarkerHelper(QLegendMarker
    *marker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#removeMarkerHelper

    Parameters
    ----------

    marker : Optional[QLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegendPrivate::removeMarkerHelper(QLegendMarker *marker)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate18removeMarkerHelperEP13QLegendMarker',
        self._addressOf(marker),
    )

  @overload(QList[QLegendMarker])
  def removeMarkers(self, markers: QList[QLegendMarker]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::removeMarkers(const QList<QLegendMarker
    *> &markers)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#removeMarkers

    Parameters
    ----------

    markers : QList[QLegendMarker]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLegendPrivate::removeMarkers(const QList<QLegendMarker *>
    #      &markers)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate13removeMarkersERK5QListIP13QLegendMarker'
        'E',
        self._valueOf(markers),
    )

  @overload(QLegendMarker)
  @overload(NoneType)
  def decorateMarker(self, marker: Optional[QLegendMarker]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::decorateMarker(QLegendMarker *marker)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#decorateMarker

    Parameters
    ----------

    marker : Optional[QLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLegendPrivate::decorateMarker(QLegendMarker *marker)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate14decorateMarkerEP13QLegendMarker',
        self._addressOf(marker),
    )

  @overload(QList[QLegendMarker])
  def decorateMarkers(self, markers: QList[QLegendMarker]) -> None:
    """
    Calls Qt's 'void QLegendPrivate::decorateMarkers(const
    QList<QLegendMarker *> &markers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendprivate.html#decorateMarkers

    Parameters
    ----------

    markers : QList[QLegendMarker]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QLegendPrivate::decorateMarkers(const QList<QLegendMarker *>
    #      &markers)
    self.uglySide.call(
        'ritual_ZN14QLegendPrivate15decorateMarkersERK5QListIP13QLegendMark'
        'erE',
        self._valueOf(markers),
    )

  def updateToolTips(self) -> None:
    """
    Calls Qt's 'void QLegendPrivate::updateToolTips()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendprivate.html#updateToolTips
    """
    #  void QLegendPrivate::updateToolTips()
    self.uglySide.call('ritual_ZN14QLegendPrivate14updateToolTipsEv')
