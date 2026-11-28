"""
ChartDataSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartdataset_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means ChartDataSet to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import AbstractDomain, QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from . import GLXYSeriesDataManager, QAbstractSeries, QChart
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']
  QChart = WAIT['QChart']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartDataSet(QObject):
  """
  The cute side of Qt's ChartDataSet: a plain Python object standing in front
  of one C++ ChartDataSet.

  It is built on the cute 'QObject', as Qt's ChartDataSet is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartDataSet that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'tr', 'addSeries',
  'removeSeries', 'series', 'addAxis', 'removeAxis', 'axes', 'attachAxis',
  'detachAxis', 'createDefaultAxes', 'zoomInDomain', 'zoomOutDomain',
  'zoomResetDomain', 'isZoomedDomain', 'scrollDomain', 'mapToValue',
  'mapToPosition', 'glXYSeriesDataManager', 'createDomain',
  'domainForSeries', 'axisAdded', 'axisRemoved', 'seriesAdded',
  'seriesRemoved', 'reverseChanged', 'createAxes', 'selectDomain',
  'deleteAllAxes', 'deleteAllSeries'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartDataSet::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ChartDataSet::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'ChartDataSet::~ChartDataSet()': the destructor: Python never
    removes a C++ ChartDataSet.
  - Qt's 'void ChartDataSet::findMinMaxForSeries(const QList<QAbstractSeries
    *> &series, Qt::Orientations orientation, qreal &min, qreal &max)': takes
    a number to change where it is.

  What has no ritual
  ------------------

  3 of the 38 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ ChartDataSet is created at the first use, not by
    'ChartDataSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartDataSet.
  - Qt tells when it has removed the C++ ChartDataSet. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's ChartDataSet that has no cute function yet,
    'findMinMaxForSeries', holds a function that raises
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
    Calls Qt's 'QString ChartDataSet::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#tr

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
    #  QString ChartDataSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12ChartDataSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartDataSet'

  #  A C++ ChartDataSet Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartDataSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartDataSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartDataSet::metaObject() const
    address = self.uglySide.call('ritual_ZNK12ChartDataSet10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def series(self) -> QList[QAbstractSeries]:
    """
    Calls Qt's 'QList<QAbstractSeries *> ChartDataSet::series() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#series

    Returns
    -------

    QList[QAbstractSeries]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractSeries *> ChartDataSet::series() const
    address = self.uglySide.call('ritual_ZNK12ChartDataSet6seriesEv')
    from . import QAbstractSeries
    return QList[QAbstractSeries]._cuteOwning(address)

  def axes(self) -> QList[QAbstractAxis]:
    """
    Calls Qt's 'QList<QAbstractAxis *> ChartDataSet::axes() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#axes

    Returns
    -------

    QList[QAbstractAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractAxis *> ChartDataSet::axes() const
    address = self.uglySide.call('ritual_ZNK12ChartDataSet4axesEv')
    return QList[QAbstractAxis]._cuteOwning(address)

  @overload(QAbstractSeries)
  @overload(NoneType)
  def domainForSeries(
      self,
      series: Optional[QAbstractSeries],
  ) -> Optional[AbstractDomain]:
    """
    Calls Qt's 'AbstractDomain *ChartDataSet::domainForSeries(QAbstractSeries
    *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#domainForSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[AbstractDomain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractDomain *ChartDataSet::domainForSeries(QAbstractSeries *series)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12ChartDataSet15domainForSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )
    return AbstractDomain._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChart)
  @overload(NoneType)
  def __init__(self, chart: Optional[QChart]) -> None:
    """
    Notes what was given, for Qt's 'ChartDataSet::ChartDataSet(QChart
    *chart)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#ChartDataSet

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ChartDataSet::ChartDataSet(QChart *chart)
    self._noteCreation(ChartDataSet, lambda: Rituals.call(
        'ritual_ZN12ChartDataSetC1EP6QChart', self._addressOf(chart),
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

  @overload(QAbstractSeries)
  @overload(NoneType)
  def addSeries(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartDataSet::addSeries(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#addSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::addSeries(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet9addSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def removeSeries(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartDataSet::removeSeries(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#removeSeries

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::removeSeries(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet12removeSeriesEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractAxis, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def addAxis(
      self,
      axis: Optional[QAbstractAxis],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void ChartDataSet::addAxis(QAbstractAxis *axis, Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void ChartDataSet::addAxis(QAbstractAxis *axis, Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet7addAxisEP13QAbstractAxis6QFlagsIN2Qt13Alig'
        'nmentFlagEE',
        self._addressOf(axis), alignment.value,
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def removeAxis(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartDataSet::removeAxis(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#removeAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::removeAxis(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet10removeAxisEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractSeries, QAbstractAxis)
  @overload(QAbstractSeries, NoneType)
  @overload(NoneType, QAbstractAxis)
  @overload(NoneType, NoneType)
  def attachAxis(
      self,
      series: Optional[QAbstractSeries],
      axis: Optional[QAbstractAxis],
  ) -> bool:
    """
    Calls Qt's 'bool ChartDataSet::attachAxis(QAbstractSeries *series,
    QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#attachAxis

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool ChartDataSet::attachAxis(QAbstractSeries *series, QAbstractAxis
    #      *axis)
    return self.uglySide.call(
        'ritual_ZN12ChartDataSet10attachAxisEP15QAbstractSeriesP13QAbstract'
        'Axis',
        self._addressOf(series), self._addressOf(axis),
    )

  @overload(QAbstractSeries, QAbstractAxis)
  @overload(QAbstractSeries, NoneType)
  @overload(NoneType, QAbstractAxis)
  @overload(NoneType, NoneType)
  def detachAxis(
      self,
      series: Optional[QAbstractSeries],
      axis: Optional[QAbstractAxis],
  ) -> bool:
    """
    Calls Qt's 'bool ChartDataSet::detachAxis(QAbstractSeries *series,
    QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#detachAxis

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool ChartDataSet::detachAxis(QAbstractSeries *series, QAbstractAxis
    #      *axis)
    return self.uglySide.call(
        'ritual_ZN12ChartDataSet10detachAxisEP15QAbstractSeriesP13QAbstract'
        'Axis',
        self._addressOf(series), self._addressOf(axis),
    )

  def createDefaultAxes(self) -> None:
    """
    Calls Qt's 'void ChartDataSet::createDefaultAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartdataset.html#createDefaultAxes
    """
    #  void ChartDataSet::createDefaultAxes()
    self.uglySide.call('ritual_ZN12ChartDataSet17createDefaultAxesEv')

  @overload(QRectF)
  def zoomInDomain(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void ChartDataSet::zoomInDomain(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#zoomInDomain

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartDataSet::zoomInDomain(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet12zoomInDomainERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def zoomOutDomain(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void ChartDataSet::zoomOutDomain(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#zoomOutDomain

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void ChartDataSet::zoomOutDomain(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet13zoomOutDomainERK6QRectF',
        self._valueOf(rect),
    )

  def zoomResetDomain(self) -> None:
    """
    Calls Qt's 'void ChartDataSet::zoomResetDomain()'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#zoomResetDomain
    """
    #  void ChartDataSet::zoomResetDomain()
    self.uglySide.call('ritual_ZN12ChartDataSet15zoomResetDomainEv')

  def isZoomedDomain(self) -> bool:
    """
    Calls Qt's 'bool ChartDataSet::isZoomedDomain()'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#isZoomedDomain
    """
    #  bool ChartDataSet::isZoomedDomain()
    return self.uglySide.call('ritual_ZN12ChartDataSet14isZoomedDomainEv')

  @overload(float, float)
  def scrollDomain(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void ChartDataSet::scrollDomain(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#scrollDomain

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void ChartDataSet::scrollDomain(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN12ChartDataSet12scrollDomainEdd', dx, dy)

  @overload(QPointF)
  @overload(QPointF, QAbstractSeries)
  @overload(QPointF, NoneType)
  def mapToValue(
      self,
      position: QPointF,
      series: Optional[QAbstractSeries] = None,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF ChartDataSet::mapToValue(const QPointF &position,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#mapToValue

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF ChartDataSet::mapToValue(const QPointF &position,
    #      QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN12ChartDataSet10mapToValueERK7QPointFP15QAbstractSeries',
        self._valueOf(position, 'QPointF'), self._addressOf(series),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  @overload(QPointF, QAbstractSeries)
  @overload(QPointF, NoneType)
  def mapToPosition(
      self,
      value: QPointF,
      series: Optional[QAbstractSeries] = None,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF ChartDataSet::mapToPosition(const QPointF &value,
    QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#mapToPosition

    Parameters
    ----------

    value : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF ChartDataSet::mapToPosition(const QPointF &value,
    #      QAbstractSeries *series)
    address = self.uglySide.call(
        'ritual_ZN12ChartDataSet13mapToPositionERK7QPointFP15QAbstractSerie'
        's',
        self._valueOf(value, 'QPointF'), self._addressOf(series),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def glXYSeriesDataManager(self) -> Optional[GLXYSeriesDataManager]:
    """
    Calls Qt's 'GLXYSeriesDataManager
    *ChartDataSet::glXYSeriesDataManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartdataset.html#glXYSeriesDataManager

    Returns
    -------

    Optional[GLXYSeriesDataManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  GLXYSeriesDataManager *ChartDataSet::glXYSeriesDataManager()
    address = self.uglySide.call(
        'ritual_ZN12ChartDataSet21glXYSeriesDataManagerEv',
    )
    from . import GLXYSeriesDataManager
    return GLXYSeriesDataManager._cuteAt(address)

  @overload(AbstractDomain.DomainType)
  def createDomain(
      self,
      type: AbstractDomain.DomainType,
  ) -> Optional[AbstractDomain]:
    """
    Calls Qt's 'AbstractDomain
    *ChartDataSet::createDomain(AbstractDomain::DomainType type)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#createDomain

    Parameters
    ----------

    type : AbstractDomain.DomainType
      Passed on as its number.

    Returns
    -------

    Optional[AbstractDomain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractDomain *ChartDataSet::createDomain(AbstractDomain::DomainType
    #      type)
    address = self.uglySide.call(
        'ritual_ZN12ChartDataSet12createDomainEN14AbstractDomain10DomainTyp'
        'eE',
        type.value,
    )
    return AbstractDomain._cuteAt(address)

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisAdded(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartDataSet::axisAdded(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#axisAdded

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::axisAdded(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet9axisAddedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisRemoved(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void ChartDataSet::axisRemoved(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#axisRemoved

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::axisRemoved(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet11axisRemovedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesAdded(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartDataSet::seriesAdded(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#seriesAdded

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::seriesAdded(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet11seriesAddedEP15QAbstractSeries',
        self._addressOf(series),
    )

  @overload(QAbstractSeries)
  @overload(NoneType)
  def seriesRemoved(self, series: Optional[QAbstractSeries]) -> None:
    """
    Calls Qt's 'void ChartDataSet::seriesRemoved(QAbstractSeries *series)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#seriesRemoved

    Parameters
    ----------

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ChartDataSet::seriesRemoved(QAbstractSeries *series)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet13seriesRemovedEP15QAbstractSeries',
        self._addressOf(series),
    )

  def reverseChanged(self) -> None:
    """
    Calls Qt's 'void ChartDataSet::reverseChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#reverseChanged
    """
    #  void ChartDataSet::reverseChanged()
    self.uglySide.call('ritual_ZN12ChartDataSet14reverseChangedEv')

  @overload(QAbstractAxis.AxisTypes, Qt.Orientation)
  def createAxes(
      self,
      type: QAbstractAxis.AxisTypes,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void ChartDataSet::createAxes(QAbstractAxis::AxisTypes type,
    Qt::Orientation orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#createAxes

    Parameters
    ----------

    type : QAbstractAxis.AxisTypes
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void ChartDataSet::createAxes(QAbstractAxis::AxisTypes type,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN12ChartDataSet10createAxesE6QFlagsIN13QAbstractAxis8AxisT'
        'ypeEEN2Qt11OrientationE',
        type.value, orientation.value,
    )

  @overload(QList[QAbstractAxis])
  def selectDomain(
      self,
      axes: QList[QAbstractAxis],
  ) -> AbstractDomain.DomainType:
    """
    Calls Qt's 'AbstractDomain::DomainType ChartDataSet::selectDomain(const
    QList<QAbstractAxis *> &axes)'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#selectDomain

    Parameters
    ----------

    axes : QList[QAbstractAxis]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    AbstractDomain.DomainType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AbstractDomain.DomainType(number)' gives.
    """
    #  AbstractDomain::DomainType ChartDataSet::selectDomain(const
    #      QList<QAbstractAxis *> &axes)
    return AbstractDomain.DomainType(self.uglySide.call(
        'ritual_ZN12ChartDataSet12selectDomainERK5QListIP13QAbstractAxisE',
        self._valueOf(axes),
    ))

  def deleteAllAxes(self) -> None:
    """
    Calls Qt's 'void ChartDataSet::deleteAllAxes()'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#deleteAllAxes
    """
    #  void ChartDataSet::deleteAllAxes()
    self.uglySide.call('ritual_ZN12ChartDataSet13deleteAllAxesEv')

  def deleteAllSeries(self) -> None:
    """
    Calls Qt's 'void ChartDataSet::deleteAllSeries()'.

    Qt's own words: https://doc.qt.io/qt-6/chartdataset.html#deleteAllSeries
    """
    #  void ChartDataSet::deleteAllSeries()
    self.uglySide.call('ritual_ZN12ChartDataSet15deleteAllSeriesEv')

  @staticmethod
  def findMinMaxForSeries(*__, **_) -> Never:
    """
    Qt's 'void ChartDataSet::findMinMaxForSeries(const QList<QAbstractSeries
    *> &series, Qt::Orientations orientation, qreal &min, qreal &max)': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'ChartDataSet.findMinMaxForSeries' has no cute function yet. Qt's "
        "'void ChartDataSet::findMinMaxForSeries(const "
        "QList<QAbstractSeries *> &series, Qt::Orientations orientation, "
        "qreal &min, qreal &max)': takes a number to change where it is.")
