"""
QPieSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qpieseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QAbstractSeries, QPieSlice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtCharts import QPieSeriesPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPieSeries(QAbstractSeries):
  """
  The cute side of Qt's QPieSeries: a plain Python object standing in front
  of one C++ QPieSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QPieSeries is built on
  Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPieSeries that has a ritual and that Python can
  call so far, 57 names in all: 'metaObject', 'tr', 'type', 'append',
  'insert', 'remove', 'clear', 'at', 'find', 'replace', 'removeMultiple',
  'take', 'slices', 'count', 'isEmpty', 'sum', 'setHorizontalPosition',
  'horizontalPosition', 'setVerticalPosition', 'verticalPosition',
  'setPieSize', 'pieSize', 'setStartAngle', 'startAngle', 'setEndAngle',
  'endAngle', 'setHoleSize', 'holeSize', 'setLabelsVisible',
  'setLabelsPosition', 'angleSpanVisibleLimit', 'setAngleSpanVisibleLimit',
  'angleSpanLabelVisibility', 'setAngleSpanLabelVisibility', 'sliceLabels',
  'setSliceLabels', 'handleSliceChange', 'componentComplete', 'added',
  'removed', 'replaced', 'countChanged', 'sumChanged', 'pieSizeChanged',
  'startAngleChanged', 'endAngleChanged', 'horizontalPositionChanged',
  'verticalPositionChanged', 'holeSizeChanged', 'clicked', 'doubleClicked',
  'pressed', 'released', 'angleSpanVisibleLimitChanged',
  'angleSpanLabelVisibilityChanged', 'sliceLabelsChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPieSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPieSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPieSeries::~QPieSeries()': the destructor: Python never removes a
    C++ QPieSeries.
  - Qt's 'QPieSeries &QPieSeries::operator<<(QPieSlice *slice)': gives a type
    Python has no way to take yet.
  - Qt's 'QList<qreal> QPieSeries::sliceData() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QPieSeries::setSliceData(const QList<qreal> &newSliceData)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QPieSeries::QPieSeries(QPieSeriesPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QPieSeries::sliceDataChanged(const QList<qreal> &sliceData)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QPieSeriesPrivate *QPieSeries::d_func() const': takes in
    Python what 'QPieSeriesPrivate *QPieSeries::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 77 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPieSeries is created at the first use, not by 'QPieSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPieSeries.
  - Qt tells when it has removed the C++ QPieSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QPieSeries that has no cute function yet,
    'setSliceData', 'sliceData', 'sliceDataChanged', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPieSeries, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LabelVisibility(CuteNum, scoped=True):
    """
    The enum 'QPieSeries::LabelVisibility' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    First = Kee[int](1)
    Even = Kee[int](2)
    Odd = Kee[int](3)

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
    Calls Qt's 'QString QPieSeries::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#tr

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
    #  QString QPieSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QPieSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPieSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QPieSeries Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPieSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPieSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPieSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QPieSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QPieSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QPieSeries::type() const
    ritual = 'ritual_ZNK10QPieSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QPieSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def slices(self) -> QList[QPieSlice]:
    """
    Calls Qt's 'QList<QPieSlice *> QPieSeries::slices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#slices

    Returns
    -------

    QList[QPieSlice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPieSlice *> QPieSeries::slices() const
    address = self.uglySide.call('ritual_ZNK10QPieSeries6slicesEv')
    return QList[QPieSlice]._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QPieSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#count
    """
    #  qsizetype QPieSeries::count() const
    return self.uglySide.call('ritual_ZNK10QPieSeries5countEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPieSeries::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#isEmpty
    """
    #  bool QPieSeries::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QPieSeries7isEmptyEv')

  def sum(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::sum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#sum
    """
    #  qreal QPieSeries::sum() const
    return self.uglySide.call('ritual_ZNK10QPieSeries3sumEv')

  def horizontalPosition(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::horizontalPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#horizontalPosition
    """
    #  qreal QPieSeries::horizontalPosition() const
    return self.uglySide.call('ritual_ZNK10QPieSeries18horizontalPositionEv')

  def verticalPosition(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::verticalPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#verticalPosition
    """
    #  qreal QPieSeries::verticalPosition() const
    return self.uglySide.call('ritual_ZNK10QPieSeries16verticalPositionEv')

  def pieSize(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::pieSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#pieSize
    """
    #  qreal QPieSeries::pieSize() const
    return self.uglySide.call('ritual_ZNK10QPieSeries7pieSizeEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#startAngle
    """
    #  qreal QPieSeries::startAngle() const
    return self.uglySide.call('ritual_ZNK10QPieSeries10startAngleEv')

  def endAngle(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::endAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#endAngle
    """
    #  qreal QPieSeries::endAngle() const
    return self.uglySide.call('ritual_ZNK10QPieSeries8endAngleEv')

  def holeSize(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::holeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#holeSize
    """
    #  qreal QPieSeries::holeSize() const
    return self.uglySide.call('ritual_ZNK10QPieSeries8holeSizeEv')

  def angleSpanVisibleLimit(self) -> float:
    """
    Calls Qt's 'qreal QPieSeries::angleSpanVisibleLimit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#angleSpanVisibleLimit
    """
    #  qreal QPieSeries::angleSpanVisibleLimit() const
    return self.uglySide.call(
        'ritual_ZNK10QPieSeries21angleSpanVisibleLimitEv',
    )

  def angleSpanLabelVisibility(self) -> LabelVisibility:
    """
    Calls Qt's 'LabelVisibility QPieSeries::angleSpanLabelVisibility()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#angleSpanLabelVisibility

    Returns
    -------

    LabelVisibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LabelVisibility(number)'
      gives.
    """
    #  LabelVisibility QPieSeries::angleSpanLabelVisibility() const
    return QPieSeries.LabelVisibility(self.uglySide.call(
        'ritual_ZNK10QPieSeries24angleSpanLabelVisibilityEv',
    ))

  def sliceLabels(self) -> QStringList:
    """
    Calls Qt's 'const QStringList &QPieSeries::sliceLabels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#sliceLabels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QPieSeries::sliceLabels() const
    address = self.uglySide.call('ritual_ZNKR10QPieSeries11sliceLabelsEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setHorizontalPosition(self, relativePosition: float) -> None:
    """
    Calls Qt's 'void QPieSeries::setHorizontalPosition(qreal
    relativePosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#setHorizontalPosition

    Parameters
    ----------

    relativePosition : float
      Passed on as it is.
    """
    #  void QPieSeries::setHorizontalPosition(qreal relativePosition)
    self.uglySide.call(
        'ritual_ZN10QPieSeries21setHorizontalPositionEd', relativePosition,
    )

  @overload(float)
  def setVerticalPosition(self, relativePosition: float) -> None:
    """
    Calls Qt's 'void QPieSeries::setVerticalPosition(qreal
    relativePosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#setVerticalPosition

    Parameters
    ----------

    relativePosition : float
      Passed on as it is.
    """
    #  void QPieSeries::setVerticalPosition(qreal relativePosition)
    self.uglySide.call(
        'ritual_ZN10QPieSeries19setVerticalPositionEd', relativePosition,
    )

  @overload(float)
  def setPieSize(self, relativeSize: float) -> None:
    """
    Calls Qt's 'void QPieSeries::setPieSize(qreal relativeSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setPieSize

    Parameters
    ----------

    relativeSize : float
      Passed on as it is.
    """
    #  void QPieSeries::setPieSize(qreal relativeSize)
    self.uglySide.call('ritual_ZN10QPieSeries10setPieSizeEd', relativeSize)

  @overload(float)
  def setStartAngle(self, startAngle: float) -> None:
    """
    Calls Qt's 'void QPieSeries::setStartAngle(qreal startAngle)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setStartAngle

    Parameters
    ----------

    startAngle : float
      Passed on as it is.
    """
    #  void QPieSeries::setStartAngle(qreal startAngle)
    self.uglySide.call('ritual_ZN10QPieSeries13setStartAngleEd', startAngle)

  @overload(float)
  def setEndAngle(self, endAngle: float) -> None:
    """
    Calls Qt's 'void QPieSeries::setEndAngle(qreal endAngle)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setEndAngle

    Parameters
    ----------

    endAngle : float
      Passed on as it is.
    """
    #  void QPieSeries::setEndAngle(qreal endAngle)
    self.uglySide.call('ritual_ZN10QPieSeries11setEndAngleEd', endAngle)

  @overload(float)
  def setHoleSize(self, holeSize: float) -> None:
    """
    Calls Qt's 'void QPieSeries::setHoleSize(qreal holeSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setHoleSize

    Parameters
    ----------

    holeSize : float
      Passed on as it is.
    """
    #  void QPieSeries::setHoleSize(qreal holeSize)
    self.uglySide.call('ritual_ZN10QPieSeries11setHoleSizeEd', holeSize)

  @overload(bool)
  def setLabelsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPieSeries::setLabelsVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPieSeries::setLabelsVisible(bool visible)
    self.uglySide.call('ritual_ZN10QPieSeries16setLabelsVisibleEb', visible)

  @overload(QPieSlice.LabelPosition)
  def setLabelsPosition(self, position: QPieSlice.LabelPosition) -> None:
    """
    Calls Qt's 'void QPieSeries::setLabelsPosition(QPieSlice::LabelPosition
    position)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setLabelsPosition

    Parameters
    ----------

    position : QPieSlice.LabelPosition
      Passed on as its number.
    """
    #  void QPieSeries::setLabelsPosition(QPieSlice::LabelPosition position)
    self.uglySide.call(
        'ritual_ZN10QPieSeries17setLabelsPositionEN9QPieSlice13LabelPositio'
        'nE',
        position.value,
    )

  @overload(float)
  def setAngleSpanVisibleLimit(
      self,
      newAngleSpanVisibleLimit: float,
  ) -> None:
    """
    Calls Qt's 'void QPieSeries::setAngleSpanVisibleLimit(qreal
    newAngleSpanVisibleLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#setAngleSpanVisibleLimit

    Parameters
    ----------

    newAngleSpanVisibleLimit : float
      Passed on as it is.
    """
    #  void QPieSeries::setAngleSpanVisibleLimit(qreal
    #      newAngleSpanVisibleLimit)
    self.uglySide.call(
        'ritual_ZN10QPieSeries24setAngleSpanVisibleLimitEd',
        newAngleSpanVisibleLimit,
    )

  @overload(LabelVisibility)
  def setAngleSpanLabelVisibility(
      self,
      newAngleSpanVisibleMode: LabelVisibility,
  ) -> None:
    """
    Calls Qt's 'void QPieSeries::setAngleSpanLabelVisibility(LabelVisibility
    newAngleSpanVisibleMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#setAngleSpanLabelVisibility

    Parameters
    ----------

    newAngleSpanVisibleMode : LabelVisibility
      Passed on as its number.
    """
    #  void QPieSeries::setAngleSpanLabelVisibility(LabelVisibility
    #      newAngleSpanVisibleMode)
    self.uglySide.call(
        'ritual_ZN10QPieSeries27setAngleSpanLabelVisibilityENS_15LabelVisib'
        'ilityE',
        newAngleSpanVisibleMode.value,
    )

  @overload(QStringList)
  def setSliceLabels(self, newLabels: QStringList) -> None:
    """
    Calls Qt's 'void QPieSeries::setSliceLabels(QStringList newLabels)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#setSliceLabels

    Parameters
    ----------

    newLabels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSeries::setSliceLabels(QStringList newLabels)
    self.uglySide.call(
        'ritual_ZN10QPieSeries14setSliceLabelsE5QListI7QStringE',
        self._valueOf(newLabels),
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
    Notes what was given, for Qt's 'QPieSeries::QPieSeries(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#QPieSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPieSeries::QPieSeries(QObject *parent)
    self._noteCreation(QPieSeries, lambda: Rituals.call(
        'ritual_ZN10QPieSeriesC1EP7QObject',
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

  @overload(QPieSlice)
  @overload(NoneType)
  def append(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::append(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#append

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSeries::append(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries6appendEP9QPieSlice', self._addressOf(slice),
    )

  @overload(QList[QPieSlice])
  def append(self, slices: QList[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::append(const QList<QPieSlice *> &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#append

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QPieSeries::append(const QList<QPieSlice *> &slices)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries6appendERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  @overload(str, float)
  def append(self, label: str, value: float) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSeries::append(const QString &label, qreal
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#append

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSeries::append(const QString &label, qreal value)
    address = self.uglySide.call(
        'ritual_ZN10QPieSeries6appendERK7QStringd', label, value,
    )
    return QPieSlice._cuteAt(address)

  @overload(int, QPieSlice)
  @overload(int, NoneType)
  def insert(self, index: int, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::insert(qsizetype index, QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSeries::insert(qsizetype index, QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries6insertExP9QPieSlice',
        index, self._addressOf(slice),
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def remove(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::remove(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#remove

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSeries::remove(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries6removeEP9QPieSlice', self._addressOf(slice),
    )

  @overload(int)
  def remove(self, index: int) -> bool:
    """
    Calls Qt's 'bool QPieSeries::remove(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QPieSeries::remove(qsizetype index)
    return self.uglySide.call('ritual_ZN10QPieSeries6removeEx', index)

  def clear(self) -> None:
    """
    Calls Qt's 'void QPieSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#clear
    """
    #  void QPieSeries::clear()
    self.uglySide.call('ritual_ZN10QPieSeries5clearEv')

  @overload(int)
  def at(self, index: int) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSeries::at(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSeries::at(qsizetype index)
    address = self.uglySide.call('ritual_ZN10QPieSeries2atEx', index)
    return QPieSlice._cuteAt(address)

  @overload(str)
  def find(self, label: str) -> Optional[QPieSlice]:
    """
    Calls Qt's 'QPieSlice *QPieSeries::find(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#find

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPieSlice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSlice *QPieSeries::find(const QString &label)
    address = self.uglySide.call(
        'ritual_ZN10QPieSeries4findERK7QString', label,
    )
    return QPieSlice._cuteAt(address)

  @overload(int, QPieSlice)
  @overload(int, NoneType)
  def replace(self, index: int, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::replace(qsizetype index, QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSeries::replace(qsizetype index, QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries7replaceExP9QPieSlice',
        index, self._addressOf(slice),
    )

  @overload(QPieSlice, QPieSlice)
  @overload(QPieSlice, NoneType)
  @overload(NoneType, QPieSlice)
  @overload(NoneType, NoneType)
  def replace(
      self,
      oldSlice: Optional[QPieSlice],
      newSlice: Optional[QPieSlice],
  ) -> bool:
    """
    Calls Qt's 'bool QPieSeries::replace(QPieSlice *oldSlice, QPieSlice
    *newSlice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#replace

    Parameters
    ----------

    oldSlice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newSlice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSeries::replace(QPieSlice *oldSlice, QPieSlice *newSlice)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries7replaceEP9QPieSliceS1_',
        self._addressOf(oldSlice), self._addressOf(newSlice),
    )

  @overload(QList[QPieSlice])
  def replace(self, slices: QList[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::replace(const QList<QPieSlice *> &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#replace

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QPieSeries::replace(const QList<QPieSlice *> &slices)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries7replaceERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  @overload(int, int)
  def removeMultiple(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QPieSeries::removeMultiple(qsizetype index, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#removeMultiple

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QPieSeries::removeMultiple(qsizetype index, int count)
    self.uglySide.call(
        'ritual_ZN10QPieSeries14removeMultipleExi', index, count,
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def take(self, slice: Optional[QPieSlice]) -> bool:
    """
    Calls Qt's 'bool QPieSeries::take(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#take

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPieSeries::take(QPieSlice *slice)
    return self.uglySide.call(
        'ritual_ZN10QPieSeries4takeEP9QPieSlice', self._addressOf(slice),
    )

  def handleSliceChange(self) -> None:
    """
    Calls Qt's 'void QPieSeries::handleSliceChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#handleSliceChange
    """
    #  void QPieSeries::handleSliceChange()
    self.uglySide.call('ritual_ZN10QPieSeries17handleSliceChangeEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QPieSeries::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#componentComplete
    """
    #  void QPieSeries::componentComplete()
    ritual = 'ritual_ZN10QPieSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QPieSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QList[QPieSlice])
  def added(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::added(const QList<QPieSlice *> &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#added

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSeries::added(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN10QPieSeries5addedERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  @overload(QList[QPieSlice])
  def removed(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::removed(const QList<QPieSlice *> &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#removed

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSeries::removed(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN10QPieSeries7removedERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  @overload(QList[QPieSlice])
  def replaced(self, slices: QList[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::replaced(const QList<QPieSlice *> &slices)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#replaced

    Parameters
    ----------

    slices : QList[QPieSlice]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSeries::replaced(const QList<QPieSlice *> &slices)
    self.uglySide.call(
        'ritual_ZN10QPieSeries8replacedERK5QListIP9QPieSliceE',
        self._valueOf(slices),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#countChanged
    """
    #  void QPieSeries::countChanged()
    self.uglySide.call('ritual_ZN10QPieSeries12countChangedEv')

  def sumChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::sumChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#sumChanged
    """
    #  void QPieSeries::sumChanged()
    self.uglySide.call('ritual_ZN10QPieSeries10sumChangedEv')

  def pieSizeChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::pieSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#pieSizeChanged
    """
    #  void QPieSeries::pieSizeChanged()
    self.uglySide.call('ritual_ZN10QPieSeries14pieSizeChangedEv')

  def startAngleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::startAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#startAngleChanged
    """
    #  void QPieSeries::startAngleChanged()
    self.uglySide.call('ritual_ZN10QPieSeries17startAngleChangedEv')

  def endAngleChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::endAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#endAngleChanged
    """
    #  void QPieSeries::endAngleChanged()
    self.uglySide.call('ritual_ZN10QPieSeries15endAngleChangedEv')

  def horizontalPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::horizontalPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#horizontalPositionChanged
    """
    #  void QPieSeries::horizontalPositionChanged()
    self.uglySide.call('ritual_ZN10QPieSeries25horizontalPositionChangedEv')

  def verticalPositionChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::verticalPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#verticalPositionChanged
    """
    #  void QPieSeries::verticalPositionChanged()
    self.uglySide.call('ritual_ZN10QPieSeries23verticalPositionChangedEv')

  def holeSizeChanged(self) -> None:
    """
    Calls Qt's 'void QPieSeries::holeSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#holeSizeChanged
    """
    #  void QPieSeries::holeSizeChanged()
    self.uglySide.call('ritual_ZN10QPieSeries15holeSizeChangedEv')

  @overload(QPieSlice)
  @overload(NoneType)
  def clicked(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::clicked(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#clicked

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieSeries::clicked(QPieSlice *slice)
    self.uglySide.call(
        'ritual_ZN10QPieSeries7clickedEP9QPieSlice', self._addressOf(slice),
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def doubleClicked(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::doubleClicked(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#doubleClicked

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieSeries::doubleClicked(QPieSlice *slice)
    self.uglySide.call(
        'ritual_ZN10QPieSeries13doubleClickedEP9QPieSlice',
        self._addressOf(slice),
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def pressed(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::pressed(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#pressed

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieSeries::pressed(QPieSlice *slice)
    self.uglySide.call(
        'ritual_ZN10QPieSeries7pressedEP9QPieSlice', self._addressOf(slice),
    )

  @overload(QPieSlice)
  @overload(NoneType)
  def released(self, slice: Optional[QPieSlice]) -> None:
    """
    Calls Qt's 'void QPieSeries::released(QPieSlice *slice)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#released

    Parameters
    ----------

    slice : Optional[QPieSlice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPieSeries::released(QPieSlice *slice)
    self.uglySide.call(
        'ritual_ZN10QPieSeries8releasedEP9QPieSlice', self._addressOf(slice),
    )

  @overload(float)
  def angleSpanVisibleLimitChanged(self, limit: float) -> None:
    """
    Calls Qt's 'void QPieSeries::angleSpanVisibleLimitChanged(qreal limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#angleSpanVisibleLimitChanged

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QPieSeries::angleSpanVisibleLimitChanged(qreal limit)
    self.uglySide.call(
        'ritual_ZN10QPieSeries28angleSpanVisibleLimitChangedEd', limit,
    )

  @overload(LabelVisibility)
  def angleSpanLabelVisibilityChanged(
      self,
      visibility: LabelVisibility,
  ) -> None:
    """
    Calls Qt's 'void
    QPieSeries::angleSpanLabelVisibilityChanged(LabelVisibility visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpieseries.html#angleSpanLabelVisibilityChanged

    Parameters
    ----------

    visibility : LabelVisibility
      Passed on as its number.
    """
    #  void QPieSeries::angleSpanLabelVisibilityChanged(LabelVisibility
    #      visibility)
    self.uglySide.call(
        'ritual_ZN10QPieSeries31angleSpanLabelVisibilityChangedENS_15LabelV'
        'isibilityE',
        visibility.value,
    )

  @overload(QStringList)
  def sliceLabelsChanged(self, sliceLabels: QStringList) -> None:
    """
    Calls Qt's 'void QPieSeries::sliceLabelsChanged(const QStringList
    &sliceLabels)'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#sliceLabelsChanged

    Parameters
    ----------

    sliceLabels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPieSeries::sliceLabelsChanged(const QStringList &sliceLabels)
    self.uglySide.call(
        'ritual_ZN10QPieSeries18sliceLabelsChangedERK5QListI7QStringE',
        self._valueOf(sliceLabels),
    )

  def d_func(self) -> Optional[QPieSeriesPrivate]:
    """
    Calls Qt's 'QPieSeriesPrivate *QPieSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpieseries.html#d_func

    Returns
    -------

    Optional[QPieSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPieSeriesPrivate *QPieSeries::d_func()
    address = self.uglySide.call('ritual_ZN10QPieSeries6d_funcEv')
    from ..QtCharts import QPieSeriesPrivate
    return QPieSeriesPrivate._cuteAt(address)

  @staticmethod
  def setSliceData(*__, **_) -> Never:
    """
    Qt's 'void QPieSeries::setSliceData(const QList<qreal> &newSliceData)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPieSeries.setSliceData' has no cute function yet. Qt's 'void "
        "QPieSeries::setSliceData(const QList<qreal> &newSliceData)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def sliceData(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QPieSeries::sliceData() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPieSeries.sliceData' has no cute function yet. Qt's "
        "'QList<qreal> QPieSeries::sliceData() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def sliceDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QPieSeries::sliceDataChanged(const QList<qreal> &sliceData)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPieSeries.sliceDataChanged' has no cute function yet. Qt's 'void "
        "QPieSeries::sliceDataChanged(const QList<qreal> &sliceData)': "
        "takes a type Python has no way to hand over yet.")
