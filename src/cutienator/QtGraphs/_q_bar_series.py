"""
QBarSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qbarseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from ..QtQml import QQmlComponent
  from . import QBarSet
  from ..QtCharts import QBarSeriesPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarSet = WAIT['QtGraphs:QBarSet']
  QColor = WAIT['QColor']
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBarSeries(QAbstractSeries):
  """
  The cute side of Qt's QBarSeries: a plain Python object standing in front
  of one C++ QBarSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QBarSeries is built on
  Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBarSeries that has a ritual and that Python can
  call so far, 69 names in all: 'metaObject', 'tr', 'type', 'seriesColors',
  'setSeriesColors', 'borderColors', 'setBorderColors', 'setBarsType',
  'barsType', 'setBarWidth', 'barWidth', 'append', 'take', 'count', 'remove',
  'insert', 'clear', 'replace', 'at', 'find', 'removeMultiple', 'barSets',
  'setLabelsVisible', 'labelsVisible', 'setLabelsFormat', 'labelsFormat',
  'setLabelsMargin', 'labelsMargin', 'setLabelsAngle', 'labelsAngle',
  'setLabelsPosition', 'labelsPosition', 'setLabelsPrecision',
  'labelsPrecision', 'barDelegate', 'setBarDelegate', 'selectAll',
  'deselectAll', 'componentComplete', 'updatedBars', 'seriesColorsChanged',
  'borderColorsChanged', 'countChanged', 'barWidthChanged',
  'labelsVisibleChanged', 'labelsFormatChanged', 'labelsPositionChanged',
  'barsTypeChanged', 'labelsMarginChanged', 'labelsAngleChanged',
  'labelsPrecisionChanged', 'barDelegateChanged', 'barsetsAdded',
  'barsetsReplaced', 'barsetsRemoved', 'setValueChanged', 'setValueAdded',
  'setValueRemoved', 'barSetsChanged', 'clicked', 'doubleClicked', 'pressed',
  'released', 'handleSetValueChange', 'handleSetValueAdd',
  'handleSetValueRemove', 'd_func', 'barDelegateDirty',
  'setBarDelegateDirty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBarSeries::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBarSeries::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBarSeries::~QBarSeries()': the destructor: Python never removes a
    C++ QBarSeries.
  - Qt's 'QBarSeries::QBarSeries(QBarSeriesPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QBarSeriesPrivate *QBarSeries::d_func() const': takes in
    Python what 'QBarSeriesPrivate *QBarSeries::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 83 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QBarSeries is created at the first use, not by 'QBarSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBarSeries.
  - Qt tells when it has removed the C++ QBarSeries. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QBarSeries, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class BarsType(CuteNum, scoped=True):
    """
    The enum 'QBarSeries::BarsType' of Qt, with the 3 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Groups = Kee[int](0)
    Stacked = Kee[int](1)
    StackedPercent = Kee[int](2)

  class LabelsPosition(CuteNum, scoped=True):
    """
    The enum 'QBarSeries::LabelsPosition' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Center = Kee[int](0)
    InsideEnd = Kee[int](1)
    InsideBase = Kee[int](2)
    OutsideEnd = Kee[int](3)

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
    Calls Qt's 'QString QBarSeries::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#tr

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
    #  QString QBarSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QBarSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QBarSeries Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBarSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBarSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBarSeries::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QBarSeries10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractSeries.SeriesType:
    """
    Calls Qt's 'QAbstractSeries::SeriesType QBarSeries::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#type

    Returns
    -------

    QAbstractSeries.SeriesType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSeries.SeriesType(number)' gives.
    """
    #  QAbstractSeries::SeriesType QBarSeries::type() const
    ritual = 'ritual_ZNK10QBarSeries4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QBarSeries4typeEv'
    return QAbstractSeries.SeriesType(self.uglySide.call(ritual))

  def seriesColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QBarSeries::seriesColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#seriesColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QBarSeries::seriesColors() const
    address = self.uglySide.call('ritual_ZNK10QBarSeries12seriesColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def borderColors(self) -> QList[QColor]:
    """
    Calls Qt's 'QList<QColor> QBarSeries::borderColors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#borderColors

    Returns
    -------

    QList[QColor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QColor> QBarSeries::borderColors() const
    address = self.uglySide.call('ritual_ZNK10QBarSeries12borderColorsEv')
    from ..QtGui import QColor
    return QList[QColor]._cuteOwning(address)

  def barsType(self) -> BarsType:
    """
    Calls Qt's 'QBarSeries::BarsType QBarSeries::barsType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barsType

    Returns
    -------

    BarsType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BarsType(number)' gives.
    """
    #  QBarSeries::BarsType QBarSeries::barsType() const
    return QBarSeries.BarsType(self.uglySide.call(
        'ritual_ZNK10QBarSeries8barsTypeEv',
    ))

  def barWidth(self) -> float:
    """
    Calls Qt's 'qreal QBarSeries::barWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barWidth
    """
    #  qreal QBarSeries::barWidth() const
    return self.uglySide.call('ritual_ZNK10QBarSeries8barWidthEv')

  def count(self) -> int:
    """
    Calls Qt's 'qsizetype QBarSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#count
    """
    #  qsizetype QBarSeries::count() const
    return self.uglySide.call('ritual_ZNK10QBarSeries5countEv')

  @overload(QBarSet)
  @overload(NoneType)
  def find(self, set: Optional[QBarSet]) -> int:
    """
    Calls Qt's 'qsizetype QBarSeries::find(QBarSet *set) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#find

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qsizetype QBarSeries::find(QBarSet *set) const
    return self.uglySide.call(
        'ritual_ZNK10QBarSeries4findEP7QBarSet', self._addressOf(set),
    )

  def barSets(self) -> QList[QBarSet]:
    """
    Calls Qt's 'QList<QBarSet *> QBarSeries::barSets() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barSets

    Returns
    -------

    QList[QBarSet]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBarSet *> QBarSeries::barSets() const
    address = self.uglySide.call('ritual_ZNK10QBarSeries7barSetsEv')
    from . import QBarSet
    return QList[QBarSet]._cuteOwning(address)

  def labelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QBarSeries::labelsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsVisible
    """
    #  bool QBarSeries::labelsVisible() const
    return self.uglySide.call('ritual_ZNK10QBarSeries13labelsVisibleEv')

  def labelsFormat(self) -> str:
    """
    Calls Qt's 'QString QBarSeries::labelsFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBarSeries::labelsFormat() const
    return self.uglySide.call('ritual_ZNK10QBarSeries12labelsFormatEv')

  def labelsMargin(self) -> float:
    """
    Calls Qt's 'qreal QBarSeries::labelsMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsMargin
    """
    #  qreal QBarSeries::labelsMargin() const
    return self.uglySide.call('ritual_ZNK10QBarSeries12labelsMarginEv')

  def labelsAngle(self) -> float:
    """
    Calls Qt's 'qreal QBarSeries::labelsAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsAngle
    """
    #  qreal QBarSeries::labelsAngle() const
    return self.uglySide.call('ritual_ZNK10QBarSeries11labelsAngleEv')

  def labelsPosition(self) -> LabelsPosition:
    """
    Calls Qt's 'QBarSeries::LabelsPosition QBarSeries::labelsPosition()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsPosition

    Returns
    -------

    LabelsPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LabelsPosition(number)'
      gives.
    """
    #  QBarSeries::LabelsPosition QBarSeries::labelsPosition() const
    return QBarSeries.LabelsPosition(self.uglySide.call(
        'ritual_ZNK10QBarSeries14labelsPositionEv',
    ))

  def labelsPrecision(self) -> int:
    """
    Calls Qt's 'int QBarSeries::labelsPrecision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsPrecision
    """
    #  int QBarSeries::labelsPrecision() const
    return self.uglySide.call('ritual_ZNK10QBarSeries15labelsPrecisionEv')

  def barDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QBarSeries::barDelegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QBarSeries::barDelegate() const
    address = self.uglySide.call('ritual_ZNK10QBarSeries11barDelegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def barDelegateDirty(self) -> bool:
    """
    Calls Qt's 'bool QBarSeries::barDelegateDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barDelegateDirty
    """
    #  bool QBarSeries::barDelegateDirty() const
    return self.uglySide.call('ritual_ZNK10QBarSeries16barDelegateDirtyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QColor])
  def setSeriesColors(self, newSeriesColors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBarSeries::setSeriesColors(const QList<QColor>
    &newSeriesColors)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setSeriesColors

    Parameters
    ----------

    newSeriesColors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSeries::setSeriesColors(const QList<QColor> &newSeriesColors)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15setSeriesColorsERK5QListI6QColorE',
        self._valueOf(newSeriesColors),
    )

  @overload(QList[QColor])
  def setBorderColors(self, newBorderColors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBarSeries::setBorderColors(const QList<QColor>
    &newBorderColors)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setBorderColors

    Parameters
    ----------

    newBorderColors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSeries::setBorderColors(const QList<QColor> &newBorderColors)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15setBorderColorsERK5QListI6QColorE',
        self._valueOf(newBorderColors),
    )

  @overload(BarsType)
  def setBarsType(self, type: BarsType) -> None:
    """
    Calls Qt's 'void QBarSeries::setBarsType(QBarSeries::BarsType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setBarsType

    Parameters
    ----------

    type : BarsType
      Passed on as its number.
    """
    #  void QBarSeries::setBarsType(QBarSeries::BarsType type)
    self.uglySide.call(
        'ritual_ZN10QBarSeries11setBarsTypeENS_8BarsTypeE', type.value,
    )

  @overload(float)
  def setBarWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QBarSeries::setBarWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setBarWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QBarSeries::setBarWidth(qreal width)
    self.uglySide.call('ritual_ZN10QBarSeries11setBarWidthEd', width)

  @overload()
  @overload(bool)
  def setLabelsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QBarSeries::setLabelsVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QBarSeries::setLabelsVisible(bool visible)
    self.uglySide.call('ritual_ZN10QBarSeries16setLabelsVisibleEb', visible)

  @overload(str)
  def setLabelsFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QBarSeries::setLabelsFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setLabelsFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarSeries::setLabelsFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15setLabelsFormatERK7QString', format,
    )

  @overload(float)
  def setLabelsMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QBarSeries::setLabelsMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setLabelsMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QBarSeries::setLabelsMargin(qreal margin)
    self.uglySide.call('ritual_ZN10QBarSeries15setLabelsMarginEd', margin)

  @overload(float)
  def setLabelsAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QBarSeries::setLabelsAngle(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setLabelsAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBarSeries::setLabelsAngle(qreal angle)
    self.uglySide.call('ritual_ZN10QBarSeries14setLabelsAngleEd', angle)

  @overload(LabelsPosition)
  def setLabelsPosition(self, position: LabelsPosition) -> None:
    """
    Calls Qt's 'void QBarSeries::setLabelsPosition(QBarSeries::LabelsPosition
    position)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setLabelsPosition

    Parameters
    ----------

    position : LabelsPosition
      Passed on as its number.
    """
    #  void QBarSeries::setLabelsPosition(QBarSeries::LabelsPosition
    #      position)
    self.uglySide.call(
        'ritual_ZN10QBarSeries17setLabelsPositionENS_14LabelsPositionE',
        position.value,
    )

  @overload(int)
  def setLabelsPrecision(self, precision: int) -> None:
    """
    Calls Qt's 'void QBarSeries::setLabelsPrecision(int precision)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setLabelsPrecision

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QBarSeries::setLabelsPrecision(int precision)
    self.uglySide.call(
        'ritual_ZN10QBarSeries18setLabelsPrecisionEi', precision,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setBarDelegate(self, newBarDelegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QBarSeries::setBarDelegate(QQmlComponent
    *newBarDelegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setBarDelegate

    Parameters
    ----------

    newBarDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::setBarDelegate(QQmlComponent *newBarDelegate)
    self.uglySide.call(
        'ritual_ZN10QBarSeries14setBarDelegateEP13QQmlComponent',
        self._addressOf(newBarDelegate),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def setValueChanged(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::setValueChanged(qsizetype index, QBarSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setValueChanged

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::setValueChanged(qsizetype index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15setValueChangedExP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, int, QBarSet)
  @overload(int, int, NoneType)
  def setValueAdded(
      self,
      index: int,
      count: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void QBarSeries::setValueAdded(qsizetype index, qsizetype
    count, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setValueAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::setValueAdded(qsizetype index, qsizetype count,
    #      QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries13setValueAddedExxP7QBarSet',
        index, count, self._addressOf(barset),
    )

  @overload(int, int, QBarSet)
  @overload(int, int, NoneType)
  def setValueRemoved(
      self,
      index: int,
      count: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void QBarSeries::setValueRemoved(qsizetype index, qsizetype
    count, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#setValueRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::setValueRemoved(qsizetype index, qsizetype count,
    #      QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15setValueRemovedExxP7QBarSet',
        index, count, self._addressOf(barset),
    )

  @overload(bool)
  def setBarDelegateDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QBarSeries::setBarDelegateDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#setBarDelegateDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QBarSeries::setBarDelegateDirty(bool dirty)
    self.uglySide.call('ritual_ZN10QBarSeries19setBarDelegateDirtyEb', dirty)

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
    Notes what was given, for Qt's 'QBarSeries::QBarSeries(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#QBarSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBarSeries::QBarSeries(QObject *parent)
    self._noteCreation(QBarSeries, lambda: Rituals.call(
        'ritual_ZN10QBarSeriesC1EP7QObject',
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

  @overload(QBarSet)
  @overload(NoneType)
  def append(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QBarSeries::append(QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#append

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBarSeries::append(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries6appendEP7QBarSet', self._addressOf(set),
    )

  @overload(QList[QBarSet])
  def append(self, sets: QList[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QBarSeries::append(const QList<QBarSet *> &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#append

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QBarSeries::append(const QList<QBarSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries6appendERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(QBarSet)
  @overload(NoneType)
  def take(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QBarSeries::take(QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#take

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBarSeries::take(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries4takeEP7QBarSet', self._addressOf(set),
    )

  @overload(QBarSet)
  @overload(NoneType)
  def remove(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QBarSeries::remove(QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#remove

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBarSeries::remove(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries6removeEP7QBarSet', self._addressOf(set),
    )

  @overload(int)
  def remove(self, index: int) -> bool:
    """
    Calls Qt's 'bool QBarSeries::remove(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QBarSeries::remove(qsizetype index)
    return self.uglySide.call('ritual_ZN10QBarSeries6removeEx', index)

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def insert(self, index: int, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QBarSeries::insert(qsizetype index, QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBarSeries::insert(qsizetype index, QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries6insertExP7QBarSet',
        index, self._addressOf(set),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QBarSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#clear
    """
    #  void QBarSeries::clear()
    self.uglySide.call('ritual_ZN10QBarSeries5clearEv')

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def replace(self, index: int, set: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::replace(qsizetype index, QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#replace

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::replace(qsizetype index, QBarSet *set)
    self.uglySide.call(
        'ritual_ZN10QBarSeries7replaceExP7QBarSet',
        index, self._addressOf(set),
    )

  @overload(QBarSet, QBarSet)
  @overload(QBarSet, NoneType)
  @overload(NoneType, QBarSet)
  @overload(NoneType, NoneType)
  def replace(
      self,
      oldValue: Optional[QBarSet],
      newValue: Optional[QBarSet],
  ) -> bool:
    """
    Calls Qt's 'bool QBarSeries::replace(QBarSet *oldValue, QBarSet
    *newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#replace

    Parameters
    ----------

    oldValue : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newValue : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBarSeries::replace(QBarSet *oldValue, QBarSet *newValue)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries7replaceEP7QBarSetS1_',
        self._addressOf(oldValue), self._addressOf(newValue),
    )

  @overload(QList[QBarSet])
  def replace(self, sets: QList[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QBarSeries::replace(const QList<QBarSet *> &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#replace

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QBarSeries::replace(const QList<QBarSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN10QBarSeries7replaceERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(int)
  def at(self, index: int) -> Optional[QBarSet]:
    """
    Calls Qt's 'QBarSet *QBarSeries::at(qsizetype index)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QBarSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSet *QBarSeries::at(qsizetype index)
    address = self.uglySide.call('ritual_ZN10QBarSeries2atEx', index)
    from . import QBarSet
    return QBarSet._cuteAt(address)

  @overload(int, int)
  def removeMultiple(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSeries::removeMultiple(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#removeMultiple

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSeries::removeMultiple(qsizetype index, qsizetype count)
    self.uglySide.call(
        'ritual_ZN10QBarSeries14removeMultipleExx', index, count,
    )

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QBarSeries::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#selectAll
    """
    #  void QBarSeries::selectAll()
    self.uglySide.call('ritual_ZN10QBarSeries9selectAllEv')

  def deselectAll(self) -> None:
    """
    Calls Qt's 'void QBarSeries::deselectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#deselectAll
    """
    #  void QBarSeries::deselectAll()
    self.uglySide.call('ritual_ZN10QBarSeries11deselectAllEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QBarSeries::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#componentComplete
    """
    #  void QBarSeries::componentComplete()
    ritual = 'ritual_ZN10QBarSeries17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBarSeries17componentCompleteEv'
    self.uglySide.call(ritual)

  def updatedBars(self) -> None:
    """
    Calls Qt's 'void QBarSeries::updatedBars()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#updatedBars
    """
    #  void QBarSeries::updatedBars()
    self.uglySide.call('ritual_ZN10QBarSeries11updatedBarsEv')

  def seriesColorsChanged(self) -> None:
    """
    Calls Qt's 'void QBarSeries::seriesColorsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#seriesColorsChanged
    """
    #  void QBarSeries::seriesColorsChanged()
    self.uglySide.call('ritual_ZN10QBarSeries19seriesColorsChangedEv')

  def borderColorsChanged(self) -> None:
    """
    Calls Qt's 'void QBarSeries::borderColorsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#borderColorsChanged
    """
    #  void QBarSeries::borderColorsChanged()
    self.uglySide.call('ritual_ZN10QBarSeries19borderColorsChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QBarSeries::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#countChanged
    """
    #  void QBarSeries::countChanged()
    self.uglySide.call('ritual_ZN10QBarSeries12countChangedEv')

  def barWidthChanged(self) -> None:
    """
    Calls Qt's 'void QBarSeries::barWidthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barWidthChanged
    """
    #  void QBarSeries::barWidthChanged()
    self.uglySide.call('ritual_ZN10QBarSeries15barWidthChangedEv')

  @overload(bool)
  def labelsVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QBarSeries::labelsVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#labelsVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QBarSeries::labelsVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN10QBarSeries20labelsVisibleChangedEb', visible,
    )

  @overload(str)
  def labelsFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QBarSeries::labelsFormatChanged(const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#labelsFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBarSeries::labelsFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN10QBarSeries19labelsFormatChangedERK7QString', format,
    )

  @overload(LabelsPosition)
  def labelsPositionChanged(self, position: LabelsPosition) -> None:
    """
    Calls Qt's 'void
    QBarSeries::labelsPositionChanged(QBarSeries::LabelsPosition position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#labelsPositionChanged

    Parameters
    ----------

    position : LabelsPosition
      Passed on as its number.
    """
    #  void QBarSeries::labelsPositionChanged(QBarSeries::LabelsPosition
    #      position)
    self.uglySide.call(
        'ritual_ZN10QBarSeries21labelsPositionChangedENS_14LabelsPositionE',
        position.value,
    )

  @overload(BarsType)
  def barsTypeChanged(self, type: BarsType) -> None:
    """
    Calls Qt's 'void QBarSeries::barsTypeChanged(QBarSeries::BarsType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barsTypeChanged

    Parameters
    ----------

    type : BarsType
      Passed on as its number.
    """
    #  void QBarSeries::barsTypeChanged(QBarSeries::BarsType type)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15barsTypeChangedENS_8BarsTypeE', type.value,
    )

  @overload(float)
  def labelsMarginChanged(self, margin: float) -> None:
    """
    Calls Qt's 'void QBarSeries::labelsMarginChanged(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#labelsMarginChanged

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QBarSeries::labelsMarginChanged(qreal margin)
    self.uglySide.call(
        'ritual_ZN10QBarSeries19labelsMarginChangedEd', margin,
    )

  @overload(float)
  def labelsAngleChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void QBarSeries::labelsAngleChanged(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#labelsAngleChanged

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBarSeries::labelsAngleChanged(qreal angle)
    self.uglySide.call('ritual_ZN10QBarSeries18labelsAngleChangedEd', angle)

  @overload(int)
  def labelsPrecisionChanged(self, precision: int) -> None:
    """
    Calls Qt's 'void QBarSeries::labelsPrecisionChanged(int precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#labelsPrecisionChanged

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QBarSeries::labelsPrecisionChanged(int precision)
    self.uglySide.call(
        'ritual_ZN10QBarSeries22labelsPrecisionChangedEi', precision,
    )

  def barDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QBarSeries::barDelegateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barDelegateChanged
    """
    #  void QBarSeries::barDelegateChanged()
    self.uglySide.call('ritual_ZN10QBarSeries18barDelegateChangedEv')

  @overload(QList[QBarSet])
  def barsetsAdded(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::barsetsAdded(const QList<QBarSet *> &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barsetsAdded

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSeries::barsetsAdded(const QList<QBarSet *> &sets)
    self.uglySide.call(
        'ritual_ZN10QBarSeries12barsetsAddedERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(QList[QBarSet])
  def barsetsReplaced(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::barsetsReplaced(const QList<QBarSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barsetsReplaced

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSeries::barsetsReplaced(const QList<QBarSet *> &sets)
    self.uglySide.call(
        'ritual_ZN10QBarSeries15barsetsReplacedERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(QList[QBarSet])
  def barsetsRemoved(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::barsetsRemoved(const QList<QBarSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barsetsRemoved

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBarSeries::barsetsRemoved(const QList<QBarSet *> &sets)
    self.uglySide.call(
        'ritual_ZN10QBarSeries14barsetsRemovedERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  def barSetsChanged(self) -> None:
    """
    Calls Qt's 'void QBarSeries::barSetsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#barSetsChanged
    """
    #  void QBarSeries::barSetsChanged()
    self.uglySide.call('ritual_ZN10QBarSeries14barSetsChangedEv')

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def clicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::clicked(qsizetype index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::clicked(qsizetype index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries7clickedExP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def doubleClicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::doubleClicked(qsizetype index, QBarSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::doubleClicked(qsizetype index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries13doubleClickedExP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def pressed(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::pressed(qsizetype index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::pressed(qsizetype index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries7pressedExP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def released(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QBarSeries::released(qsizetype index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBarSeries::released(qsizetype index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN10QBarSeries8releasedExP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int)
  def handleSetValueChange(self, index: int) -> None:
    """
    Calls Qt's 'void QBarSeries::handleSetValueChange(qsizetype index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#handleSetValueChange

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QBarSeries::handleSetValueChange(qsizetype index)
    self.uglySide.call(
        'ritual_ZN10QBarSeries20handleSetValueChangeEx', index,
    )

  @overload(int, int)
  def handleSetValueAdd(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSeries::handleSetValueAdd(qsizetype index, qsizetype
    count)'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#handleSetValueAdd

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSeries::handleSetValueAdd(qsizetype index, qsizetype count)
    self.uglySide.call(
        'ritual_ZN10QBarSeries17handleSetValueAddExx', index, count,
    )

  @overload(int, int)
  def handleSetValueRemove(self, index: int, count: int) -> None:
    """
    Calls Qt's 'void QBarSeries::handleSetValueRemove(qsizetype index,
    qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbarseries.html#handleSetValueRemove

    Parameters
    ----------

    index : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QBarSeries::handleSetValueRemove(qsizetype index, qsizetype
    #      count)
    self.uglySide.call(
        'ritual_ZN10QBarSeries20handleSetValueRemoveExx', index, count,
    )

  def d_func(self) -> Optional[QBarSeriesPrivate]:
    """
    Calls Qt's 'QBarSeriesPrivate *QBarSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qbarseries.html#d_func

    Returns
    -------

    Optional[QBarSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBarSeriesPrivate *QBarSeries::d_func()
    address = self.uglySide.call('ritual_ZN10QBarSeries6d_funcEv')
    from ..QtCharts import QBarSeriesPrivate
    return QBarSeriesPrivate._cuteAt(address)
