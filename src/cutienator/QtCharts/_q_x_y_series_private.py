"""
QXYSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qxyseries_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QXYSeriesPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QAbstractAxis, QAbstractSeriesPrivate, QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QPainter
  from . import QLegend, QLegendMarker, QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLegend = WAIT['QLegend']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXYSeriesPrivate(QAbstractSeriesPrivate):
  """
  The cute side of Qt's QXYSeriesPrivate: a plain Python object standing in
  front of one C++ QXYSeriesPrivate.

  It is built on the cute 'QAbstractSeriesPrivate', as Qt's QXYSeriesPrivate
  is built on Qt's QAbstractSeriesPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXYSeriesPrivate that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'initializeDomain',
  'initializeAxes', 'createLegendMarkers', 'defaultAxisType',
  'createDefaultAxis', 'drawPointLabels', 'drawBestFitLine',
  'isPointSelected', 'isMarkerSizeDefault', 'setMarkerSize', 'seriesUpdated',
  'q_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXYSeriesPrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QXYSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QXYSeriesPrivate::initializeAnimations(QChart::AnimationOptions options,
    int duration, QEasingCurve &curve)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QXYSeriesPrivate::drawSeriesPointLabels(QPainter *painter,
    const QList<QPointF> &points, const int offset, const QHash<int, int>
    &offsets, const QList<int> &indexesToSkip, const QHash<int, QString>
    &customLabels)': takes a type Python has no way to hand over yet.
  - Qt's 'QPair<qreal, qreal> QXYSeriesPrivate::bestFitLineEquation(bool &ok)
    const': takes a number to change where it is.
  - Qt's 'void QXYSeriesPrivate::setPointSelected(int index, bool selected,
    bool &callSignal)': takes a number to change where it is.
  - Qt's 'QList<qreal> QXYSeriesPrivate::colorByData() const': gives a type
    Python has no way to take yet.
  - Qt's 'bool QXYSeriesPrivate::setPointConfiguration(const int index, const
    QXYSeries::PointConfiguration key, const QVariant &value)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QXYSeries *QXYSeriesPrivate::q_func() const': takes in Python
    what 'QXYSeries *QXYSeriesPrivate::q_func()' takes.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QXYSeriesPrivate is created at the first use, not by
    'QXYSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXYSeriesPrivate.
  - Qt tells when it has removed the C++ QXYSeriesPrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QXYSeriesPrivate that has no cute function yet,
    '__init__', 'bestFitLineEquation', 'colorByData',
    'drawSeriesPointLabels', 'setPointConfiguration', 'setPointSelected',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QXYSeriesPrivate::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseriesprivate.html#tr

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
    #  QString QXYSeriesPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QXYSeriesPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXYSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QXYSeriesPrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QXYSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QXYSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.Orientation)
  def defaultAxisType(
      self,
      orientation: Qt.Orientation,
  ) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'QAbstractAxis::AxisType
    QXYSeriesPrivate::defaultAxisType(Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#defaultAxisType

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  QAbstractAxis::AxisType
    #      QXYSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
    #      const
    ritual = (
        'ritual_ZNK16QXYSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QXYSeriesPrivate15defaultAxisTypeEN2Qt11Orientat'
          'ionE')
    return QAbstractAxis.AxisType(self.uglySide.call(
        ritual, orientation.value,
    ))

  @overload(Qt.Orientation)
  def createDefaultAxis(
      self,
      orientation: Qt.Orientation,
  ) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis
    *QXYSeriesPrivate::createDefaultAxis(Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#createDefaultAxis

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *QXYSeriesPrivate::createDefaultAxis(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK16QXYSeriesPrivate17createDefaultAxisEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QXYSeriesPrivate17createDefaultAxisEN2Qt11Orient'
          'ationE')
    address = self.uglySide.call(ritual, orientation.value)
    return QAbstractAxis._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMarkerSize(self, markerSize: float) -> None:
    """
    Calls Qt's 'void QXYSeriesPrivate::setMarkerSize(qreal markerSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#setMarkerSize

    Parameters
    ----------

    markerSize : float
      Passed on as it is.
    """
    #  void QXYSeriesPrivate::setMarkerSize(qreal markerSize)
    self.uglySide.call(
        'ritual_ZN16QXYSeriesPrivate13setMarkerSizeEd', markerSize,
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
    Qt's 'QXYSeriesPrivate::QXYSeriesPrivate(QXYSeries *q)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QXYSeriesPrivate.__init__' has no cute function yet. Qt's "
        "'QXYSeriesPrivate::QXYSeriesPrivate(QXYSeries *q)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def initializeDomain(self) -> None:
    """
    Calls Qt's 'void QXYSeriesPrivate::initializeDomain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#initializeDomain
    """
    #  void QXYSeriesPrivate::initializeDomain()
    ritual = 'ritual_ZN16QXYSeriesPrivate16initializeDomainEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXYSeriesPrivate16initializeDomainEv'
    self.uglySide.call(ritual)

  def initializeAxes(self) -> None:
    """
    Calls Qt's 'void QXYSeriesPrivate::initializeAxes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#initializeAxes
    """
    #  void QXYSeriesPrivate::initializeAxes()
    ritual = 'ritual_ZN16QXYSeriesPrivate14initializeAxesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXYSeriesPrivate14initializeAxesEv'
    self.uglySide.call(ritual)

  @overload(QLegend)
  @overload(NoneType)
  def createLegendMarkers(
      self,
      legend: Optional[QLegend],
  ) -> QList[QLegendMarker]:
    """
    Calls Qt's 'QList<QLegendMarker *>
    QXYSeriesPrivate::createLegendMarkers(QLegend *legend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#createLegendMarkers

    Parameters
    ----------

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QLegendMarker]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLegendMarker *> QXYSeriesPrivate::createLegendMarkers(QLegend
    #      *legend)
    address = self.uglySide.call(
        'ritual_ZN16QXYSeriesPrivate19createLegendMarkersEP7QLegend',
        self._addressOf(legend),
    )
    from . import QLegendMarker
    return QList[QLegendMarker]._cuteOwning(address)

  @overload(QPainter, QList[QPointF])
  @overload(NoneType, QList[QPointF])
  @overload(QPainter, QList[QPointF], int)
  @overload(NoneType, QList[QPointF], int)
  def drawPointLabels(
      self,
      painter: Optional[QPainter],
      allPoints: QList[QPointF],
      offset: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QXYSeriesPrivate::drawPointLabels(QPainter *painter,
    const QList<QPointF> &allPoints, const int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#drawPointLabels

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    allPoints : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QXYSeriesPrivate::drawPointLabels(QPainter *painter, const
    #      QList<QPointF> &allPoints, const int offset)
    self.uglySide.call(
        'ritual_ZN16QXYSeriesPrivate15drawPointLabelsEP8QPainterRK5QListI7Q'
        'PointFEi',
        self._addressOf(painter), self._valueOf(allPoints), offset,
    )

  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  def drawBestFitLine(
      self,
      painter: Optional[QPainter],
      clipRect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QXYSeriesPrivate::drawBestFitLine(QPainter *painter,
    const QRectF &clipRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#drawBestFitLine

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    clipRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QXYSeriesPrivate::drawBestFitLine(QPainter *painter, const QRectF
    #      &clipRect)
    self.uglySide.call(
        'ritual_ZN16QXYSeriesPrivate15drawBestFitLineEP8QPainterRK6QRectF',
        self._addressOf(painter), self._valueOf(clipRect),
    )

  @overload(int)
  def isPointSelected(self, index: int) -> bool:
    """
    Calls Qt's 'bool QXYSeriesPrivate::isPointSelected(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#isPointSelected

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QXYSeriesPrivate::isPointSelected(int index)
    return self.uglySide.call(
        'ritual_ZN16QXYSeriesPrivate15isPointSelectedEi', index,
    )

  def isMarkerSizeDefault(self) -> bool:
    """
    Calls Qt's 'bool QXYSeriesPrivate::isMarkerSizeDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#isMarkerSizeDefault
    """
    #  bool QXYSeriesPrivate::isMarkerSizeDefault()
    return self.uglySide.call(
        'ritual_ZN16QXYSeriesPrivate19isMarkerSizeDefaultEv',
    )

  def seriesUpdated(self) -> None:
    """
    Calls Qt's 'void QXYSeriesPrivate::seriesUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxyseriesprivate.html#seriesUpdated
    """
    #  void QXYSeriesPrivate::seriesUpdated()
    self.uglySide.call('ritual_ZN16QXYSeriesPrivate13seriesUpdatedEv')

  def q_func(self) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *QXYSeriesPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qxyseriesprivate.html#q_func

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *QXYSeriesPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QXYSeriesPrivate6q_funcEv')
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  @staticmethod
  def bestFitLineEquation(*__, **_) -> Never:
    """
    Qt's 'QPair<qreal, qreal> QXYSeriesPrivate::bestFitLineEquation(bool &ok)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QXYSeriesPrivate.bestFitLineEquation' has no cute function yet. "
        "Qt's 'QPair<qreal, qreal> "
        "QXYSeriesPrivate::bestFitLineEquation(bool &ok) const': takes a "
        "number to change where it is.")

  @staticmethod
  def colorByData(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QXYSeriesPrivate::colorByData() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXYSeriesPrivate.colorByData' has no cute function yet. Qt's "
        "'QList<qreal> QXYSeriesPrivate::colorByData() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def drawSeriesPointLabels(*__, **_) -> Never:
    """
    Qt's 'void QXYSeriesPrivate::drawSeriesPointLabels(QPainter *painter,
    const QList<QPointF> &points, const int offset, const QHash<int, int>
    &offsets, const QList<int> &indexesToSkip, const QHash<int, QString>
    &customLabels)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeriesPrivate.drawSeriesPointLabels' has no cute function yet. "
        "Qt's 'void QXYSeriesPrivate::drawSeriesPointLabels(QPainter "
        "*painter, const QList<QPointF> &points, const int offset, const "
        "QHash<int, int> &offsets, const QList<int> &indexesToSkip, const "
        "QHash<int, QString> &customLabels)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def setPointConfiguration(*__, **_) -> Never:
    """
    Qt's 'bool QXYSeriesPrivate::setPointConfiguration(const int index, const
    QXYSeries::PointConfiguration key, const QVariant &value)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXYSeriesPrivate.setPointConfiguration' has no cute function yet. "
        "Qt's 'bool QXYSeriesPrivate::setPointConfiguration(const int "
        "index, const QXYSeries::PointConfiguration key, const QVariant "
        "&value)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setPointSelected(*__, **_) -> Never:
    """
    Qt's 'void QXYSeriesPrivate::setPointSelected(int index, bool selected,
    bool &callSignal)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QXYSeriesPrivate.setPointSelected' has no cute function yet. Qt's "
        "'void QXYSeriesPrivate::setPointSelected(int index, bool selected, "
        "bool &callSignal)': takes a number to change where it is.")
