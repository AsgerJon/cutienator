"""
QCandlestickSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qcandlestickseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QBrush, QColor, QPen
  from . import QCandlestickSeriesPrivate, QCandlestickSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QCandlestickSet = WAIT['QCandlestickSet']
  QColor = WAIT['QColor']
  QPen = WAIT['QPen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCandlestickSeries(QAbstractSeries):
  """
  The cute side of Qt's QCandlestickSeries: a plain Python object standing in
  front of one C++ QCandlestickSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QCandlestickSeries is
  built on Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCandlestickSeries that has a ritual and that Python
  can call so far, 49 names in all: 'metaObject', 'tr', 'append', 'remove',
  'insert', 'take', 'clear', 'sets', 'count', 'type',
  'setMaximumColumnWidth', 'maximumColumnWidth', 'setMinimumColumnWidth',
  'minimumColumnWidth', 'setBodyWidth', 'bodyWidth', 'setBodyOutlineVisible',
  'bodyOutlineVisible', 'setCapsWidth', 'capsWidth', 'setCapsVisible',
  'capsVisible', 'setIncreasingColor', 'increasingColor',
  'setDecreasingColor', 'decreasingColor', 'setBrush', 'brush', 'setPen',
  'pen', 'clicked', 'hovered', 'pressed', 'released', 'doubleClicked',
  'candlestickSetsAdded', 'candlestickSetsRemoved', 'countChanged',
  'maximumColumnWidthChanged', 'minimumColumnWidthChanged',
  'bodyWidthChanged', 'bodyOutlineVisibilityChanged', 'capsWidthChanged',
  'capsVisibilityChanged', 'increasingColorChanged',
  'decreasingColorChanged', 'brushChanged', 'penChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCandlestickSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCandlestickSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCandlestickSeries::~QCandlestickSeries()': the destructor: Python
    never removes a C++ QCandlestickSeries.
  - Qt's 'const QCandlestickSeriesPrivate *QCandlestickSeries::d_func()
    const': takes in Python what 'QCandlestickSeriesPrivate
    *QCandlestickSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 60 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCandlestickSeries is created at the first use, not by
    'QCandlestickSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCandlestickSeries.
  - Qt tells when it has removed the C++ QCandlestickSeries. Every call on
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
    Calls Qt's 'QString QCandlestickSeries::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#tr

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
    #  QString QCandlestickSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QCandlestickSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCandlestickSeries'

  #  A C++ QCandlestickSeries Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCandlestickSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCandlestickSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCandlestickSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sets(self) -> QList[QCandlestickSet]:
    """
    Calls Qt's 'QList<QCandlestickSet *> QCandlestickSeries::sets() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#sets

    Returns
    -------

    QList[QCandlestickSet]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCandlestickSet *> QCandlestickSeries::sets() const
    address = self.uglySide.call('ritual_ZNK18QCandlestickSeries4setsEv')
    from . import QCandlestickSet
    return QList[QCandlestickSet]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QCandlestickSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#count
    """
    #  int QCandlestickSeries::count() const
    return self.uglySide.call('ritual_ZNK18QCandlestickSeries5countEv')

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QCandlestickSeries::type()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QCandlestickSeries::type() const
    ritual = 'ritual_ZNK18QCandlestickSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QCandlestickSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def maximumColumnWidth(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSeries::maximumColumnWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#maximumColumnWidth
    """
    #  qreal QCandlestickSeries::maximumColumnWidth() const
    return self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries18maximumColumnWidthEv',
    )

  def minimumColumnWidth(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSeries::minimumColumnWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#minimumColumnWidth
    """
    #  qreal QCandlestickSeries::minimumColumnWidth() const
    return self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries18minimumColumnWidthEv',
    )

  def bodyWidth(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSeries::bodyWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#bodyWidth
    """
    #  qreal QCandlestickSeries::bodyWidth() const
    return self.uglySide.call('ritual_ZNK18QCandlestickSeries9bodyWidthEv')

  def bodyOutlineVisible(self) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::bodyOutlineVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#bodyOutlineVisible
    """
    #  bool QCandlestickSeries::bodyOutlineVisible() const
    return self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries18bodyOutlineVisibleEv',
    )

  def capsWidth(self) -> float:
    """
    Calls Qt's 'qreal QCandlestickSeries::capsWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#capsWidth
    """
    #  qreal QCandlestickSeries::capsWidth() const
    return self.uglySide.call('ritual_ZNK18QCandlestickSeries9capsWidthEv')

  def capsVisible(self) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::capsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#capsVisible
    """
    #  bool QCandlestickSeries::capsVisible() const
    return self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries11capsVisibleEv',
    )

  def increasingColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCandlestickSeries::increasingColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#increasingColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCandlestickSeries::increasingColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries15increasingColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def decreasingColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCandlestickSeries::decreasingColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#decreasingColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCandlestickSeries::decreasingColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QCandlestickSeries15decreasingColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QCandlestickSeries::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QCandlestickSeries::brush() const
    address = self.uglySide.call('ritual_ZNK18QCandlestickSeries5brushEv')
    from ..QtGui import QBrush
    return QBrush._cuteOwning(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QCandlestickSeries::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QCandlestickSeries::pen() const
    address = self.uglySide.call('ritual_ZNK18QCandlestickSeries3penEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMaximumColumnWidth(self, maximumColumnWidth: float) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setMaximumColumnWidth(qreal
    maximumColumnWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setMaximumColumnWidth

    Parameters
    ----------

    maximumColumnWidth : float
      Passed on as it is.
    """
    #  void QCandlestickSeries::setMaximumColumnWidth(qreal
    #      maximumColumnWidth)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries21setMaximumColumnWidthEd',
        maximumColumnWidth,
    )

  @overload(float)
  def setMinimumColumnWidth(self, minimumColumnWidth: float) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setMinimumColumnWidth(qreal
    minimumColumnWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setMinimumColumnWidth

    Parameters
    ----------

    minimumColumnWidth : float
      Passed on as it is.
    """
    #  void QCandlestickSeries::setMinimumColumnWidth(qreal
    #      minimumColumnWidth)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries21setMinimumColumnWidthEd',
        minimumColumnWidth,
    )

  @overload(float)
  def setBodyWidth(self, bodyWidth: float) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setBodyWidth(qreal bodyWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setBodyWidth

    Parameters
    ----------

    bodyWidth : float
      Passed on as it is.
    """
    #  void QCandlestickSeries::setBodyWidth(qreal bodyWidth)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries12setBodyWidthEd', bodyWidth,
    )

  @overload(bool)
  def setBodyOutlineVisible(self, bodyOutlineVisible: bool) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setBodyOutlineVisible(bool
    bodyOutlineVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setBodyOutlineVisible

    Parameters
    ----------

    bodyOutlineVisible : bool
      Passed on as it is.
    """
    #  void QCandlestickSeries::setBodyOutlineVisible(bool
    #      bodyOutlineVisible)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries21setBodyOutlineVisibleEb',
        bodyOutlineVisible,
    )

  @overload(float)
  def setCapsWidth(self, capsWidth: float) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setCapsWidth(qreal capsWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setCapsWidth

    Parameters
    ----------

    capsWidth : float
      Passed on as it is.
    """
    #  void QCandlestickSeries::setCapsWidth(qreal capsWidth)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries12setCapsWidthEd', capsWidth,
    )

  @overload(bool)
  def setCapsVisible(self, capsVisible: bool) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setCapsVisible(bool capsVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setCapsVisible

    Parameters
    ----------

    capsVisible : bool
      Passed on as it is.
    """
    #  void QCandlestickSeries::setCapsVisible(bool capsVisible)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries14setCapsVisibleEb', capsVisible,
    )

  @overload(QColor)
  def setIncreasingColor(self, increasingColor: QColor) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setIncreasingColor(const QColor
    &increasingColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setIncreasingColor

    Parameters
    ----------

    increasingColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCandlestickSeries::setIncreasingColor(const QColor
    #      &increasingColor)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries18setIncreasingColorERK6QColor',
        self._valueOf(increasingColor),
    )

  @overload(QColor)
  def setDecreasingColor(self, decreasingColor: QColor) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setDecreasingColor(const QColor
    &decreasingColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#setDecreasingColor

    Parameters
    ----------

    decreasingColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCandlestickSeries::setDecreasingColor(const QColor
    #      &decreasingColor)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries18setDecreasingColorERK6QColor',
        self._valueOf(decreasingColor),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QCandlestickSeries::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries8setBrushERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void QCandlestickSeries::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries6setPenERK4QPen', self._valueOf(pen),
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
    'QCandlestickSeries::QCandlestickSeries(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#QCandlestickSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCandlestickSeries::QCandlestickSeries(QObject *parent)
    self._noteCreation(QCandlestickSeries, lambda: Rituals.call(
        'ritual_ZN18QCandlestickSeriesC1EP7QObject',
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

  @overload(QCandlestickSet)
  @overload(NoneType)
  def append(self, set: Optional[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::append(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#append

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCandlestickSeries::append(QCandlestickSet *set)
    return self.uglySide.call(
        'ritual_ZN18QCandlestickSeries6appendEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QList[QCandlestickSet])
  def append(self, sets: QList[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::append(const QList<QCandlestickSet
    *> &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#append

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCandlestickSeries::append(const QList<QCandlestickSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN18QCandlestickSeries6appendERK5QListIP15QCandlestickSetE',
        self._valueOf(sets),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def remove(self, set: Optional[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::remove(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#remove

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCandlestickSeries::remove(QCandlestickSet *set)
    return self.uglySide.call(
        'ritual_ZN18QCandlestickSeries6removeEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QList[QCandlestickSet])
  def remove(self, sets: QList[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::remove(const QList<QCandlestickSet
    *> &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#remove

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCandlestickSeries::remove(const QList<QCandlestickSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN18QCandlestickSeries6removeERK5QListIP15QCandlestickSetE',
        self._valueOf(sets),
    )

  @overload(int, QCandlestickSet)
  @overload(int, NoneType)
  def insert(self, index: int, set: Optional[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::insert(int index, QCandlestickSet
    *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCandlestickSeries::insert(int index, QCandlestickSet *set)
    return self.uglySide.call(
        'ritual_ZN18QCandlestickSeries6insertEiP15QCandlestickSet',
        index, self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def take(self, set: Optional[QCandlestickSet]) -> bool:
    """
    Calls Qt's 'bool QCandlestickSeries::take(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#take

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCandlestickSeries::take(QCandlestickSet *set)
    return self.uglySide.call(
        'ritual_ZN18QCandlestickSeries4takeEP15QCandlestickSet',
        self._addressOf(set),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#clear
    """
    #  void QCandlestickSeries::clear()
    self.uglySide.call('ritual_ZN18QCandlestickSeries5clearEv')

  @overload(QCandlestickSet)
  @overload(NoneType)
  def clicked(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::clicked(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#clicked

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeries::clicked(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries7clickedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(bool, QCandlestickSet)
  @overload(bool, NoneType)
  def hovered(self, status: bool, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::hovered(bool status, QCandlestickSet
    *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeries::hovered(bool status, QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries7hoveredEbP15QCandlestickSet',
        status, self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def pressed(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::pressed(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#pressed

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeries::pressed(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries7pressedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def released(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::released(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#released

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeries::released(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries8releasedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def doubleClicked(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::doubleClicked(QCandlestickSet
    *set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#doubleClicked

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCandlestickSeries::doubleClicked(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries13doubleClickedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QList[QCandlestickSet])
  def candlestickSetsAdded(self, sets: QList[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::candlestickSetsAdded(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#candlestickSetsAdded

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCandlestickSeries::candlestickSetsAdded(const
    #      QList<QCandlestickSet *> &sets)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries20candlestickSetsAddedERK5QListIP15QC'
        'andlestickSetE',
        self._valueOf(sets),
    )

  @overload(QList[QCandlestickSet])
  def candlestickSetsRemoved(self, sets: QList[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::candlestickSetsRemoved(const
    QList<QCandlestickSet *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#candlestickSetsRemoved

    Parameters
    ----------

    sets : QList[QCandlestickSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCandlestickSeries::candlestickSetsRemoved(const
    #      QList<QCandlestickSet *> &sets)
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries22candlestickSetsRemovedERK5QListIP15'
        'QCandlestickSetE',
        self._valueOf(sets),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#countChanged
    """
    #  void QCandlestickSeries::countChanged()
    self.uglySide.call('ritual_ZN18QCandlestickSeries12countChangedEv')

  def maximumColumnWidthChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::maximumColumnWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#maximumColumnWidthChanged
    """
    #  void QCandlestickSeries::maximumColumnWidthChanged()
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries25maximumColumnWidthChangedEv',
    )

  def minimumColumnWidthChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::minimumColumnWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#minimumColumnWidthChanged
    """
    #  void QCandlestickSeries::minimumColumnWidthChanged()
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries25minimumColumnWidthChangedEv',
    )

  def bodyWidthChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::bodyWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#bodyWidthChanged
    """
    #  void QCandlestickSeries::bodyWidthChanged()
    self.uglySide.call('ritual_ZN18QCandlestickSeries16bodyWidthChangedEv')

  def bodyOutlineVisibilityChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::bodyOutlineVisibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html
    """
    #  void QCandlestickSeries::bodyOutlineVisibilityChanged()
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries28bodyOutlineVisibilityChangedEv',
    )

  def capsWidthChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::capsWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#capsWidthChanged
    """
    #  void QCandlestickSeries::capsWidthChanged()
    self.uglySide.call('ritual_ZN18QCandlestickSeries16capsWidthChangedEv')

  def capsVisibilityChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::capsVisibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#capsVisibilityChanged
    """
    #  void QCandlestickSeries::capsVisibilityChanged()
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries21capsVisibilityChangedEv',
    )

  def increasingColorChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::increasingColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#increasingColorChanged
    """
    #  void QCandlestickSeries::increasingColorChanged()
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries22increasingColorChangedEv',
    )

  def decreasingColorChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::decreasingColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#decreasingColorChanged
    """
    #  void QCandlestickSeries::decreasingColorChanged()
    self.uglySide.call(
        'ritual_ZN18QCandlestickSeries22decreasingColorChangedEv',
    )

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::brushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandlestickseries.html#brushChanged
    """
    #  void QCandlestickSeries::brushChanged()
    self.uglySide.call('ritual_ZN18QCandlestickSeries12brushChangedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QCandlestickSeries::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#penChanged
    """
    #  void QCandlestickSeries::penChanged()
    self.uglySide.call('ritual_ZN18QCandlestickSeries10penChangedEv')

  def d_func(self) -> Optional[QCandlestickSeriesPrivate]:
    """
    Calls Qt's 'QCandlestickSeriesPrivate *QCandlestickSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcandlestickseries.html#d_func

    Returns
    -------

    Optional[QCandlestickSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCandlestickSeriesPrivate *QCandlestickSeries::d_func()
    address = self.uglySide.call('ritual_ZN18QCandlestickSeries6d_funcEv')
    from . import QCandlestickSeriesPrivate
    return QCandlestickSeriesPrivate._cuteAt(address)
