"""
QAbstractBarSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qabstractbarseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QAbstractSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstractBarSeriesPrivate, QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarSet = WAIT['QtCharts:QBarSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractBarSeries(QAbstractSeries):
  """
  The cute side of Qt's QAbstractBarSeries: a plain Python object standing in
  front of one C++ QAbstractBarSeries.

  It is built on the cute 'QAbstractSeries', as Qt's QAbstractBarSeries is
  built on Qt's QAbstractSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractBarSeries that has a ritual and that Python
  can call so far, 35 names in all: 'metaObject', 'tr', 'setBarWidth',
  'barWidth', 'append', 'remove', 'take', 'insert', 'count', 'barSets',
  'clear', 'setLabelsVisible', 'isLabelsVisible', 'setLabelsFormat',
  'labelsFormat', 'setLabelsAngle', 'labelsAngle', 'setLabelsPosition',
  'labelsPosition', 'setLabelsPrecision', 'labelsPrecision', 'clicked',
  'hovered', 'pressed', 'released', 'doubleClicked', 'countChanged',
  'labelsVisibleChanged', 'labelsFormatChanged', 'labelsPositionChanged',
  'labelsAngleChanged', 'labelsPrecisionChanged', 'barsetsAdded',
  'barsetsRemoved', 'd_func'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractBarSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractBarSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractBarSeries::~QAbstractBarSeries()': the destructor: Python
    never removes a C++ QAbstractBarSeries.
  - Qt's 'QAbstractBarSeries::QAbstractBarSeries(QAbstractBarSeriesPrivate
    &d, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QAbstractBarSeriesPrivate *QAbstractBarSeries::d_func()
    const': takes in Python what 'QAbstractBarSeriesPrivate
    *QAbstractBarSeries::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 43 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractBarSeries is created at the first use, not by
    'QAbstractBarSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractBarSeries.
  - Qt tells when it has removed the C++ QAbstractBarSeries. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractBarSeries that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QAbstractBarSeries, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LabelsPosition(CuteNum):
    """
    The enum 'QAbstractBarSeries::LabelsPosition' of Qt, with the 4 names Qt
    gives in it.
    """

    LabelsCenter = Kee[int](0)
    LabelsInsideEnd = Kee[int](1)
    LabelsInsideBase = Kee[int](2)
    LabelsOutsideEnd = Kee[int](3)

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
    Calls Qt's 'QString QAbstractBarSeries::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#tr

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
    #  QString QAbstractBarSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAbstractBarSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractBarSeries'

  #  A C++ QAbstractBarSeries Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractBarSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractBarSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractBarSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractBarSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def barWidth(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeries::barWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#barWidth
    """
    #  qreal QAbstractBarSeries::barWidth() const
    return self.uglySide.call('ritual_ZNK18QAbstractBarSeries8barWidthEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QAbstractBarSeries::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#count
    """
    #  int QAbstractBarSeries::count() const
    return self.uglySide.call('ritual_ZNK18QAbstractBarSeries5countEv')

  def barSets(self) -> QList[QBarSet]:
    """
    Calls Qt's 'QList<QBarSet *> QAbstractBarSeries::barSets() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#barSets

    Returns
    -------

    QList[QBarSet]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBarSet *> QAbstractBarSeries::barSets() const
    address = self.uglySide.call('ritual_ZNK18QAbstractBarSeries7barSetsEv')
    from . import QBarSet
    return QList[QBarSet]._cuteOwning(address)

  def isLabelsVisible(self) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeries::isLabelsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#isLabelsVisible
    """
    #  bool QAbstractBarSeries::isLabelsVisible() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractBarSeries15isLabelsVisibleEv',
    )

  def labelsFormat(self) -> str:
    """
    Calls Qt's 'QString QAbstractBarSeries::labelsFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractBarSeries::labelsFormat() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractBarSeries12labelsFormatEv',
    )

  def labelsAngle(self) -> float:
    """
    Calls Qt's 'qreal QAbstractBarSeries::labelsAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsAngle
    """
    #  qreal QAbstractBarSeries::labelsAngle() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractBarSeries11labelsAngleEv',
    )

  def labelsPosition(self) -> LabelsPosition:
    """
    Calls Qt's 'QAbstractBarSeries::LabelsPosition
    QAbstractBarSeries::labelsPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsPosition

    Returns
    -------

    LabelsPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LabelsPosition(number)'
      gives.
    """
    #  QAbstractBarSeries::LabelsPosition
    #      QAbstractBarSeries::labelsPosition() const
    return QAbstractBarSeries.LabelsPosition(self.uglySide.call(
        'ritual_ZNK18QAbstractBarSeries14labelsPositionEv',
    ))

  def labelsPrecision(self) -> int:
    """
    Calls Qt's 'int QAbstractBarSeries::labelsPrecision() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsPrecision
    """
    #  int QAbstractBarSeries::labelsPrecision() const
    return self.uglySide.call(
        'ritual_ZNK18QAbstractBarSeries15labelsPrecisionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBarWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::setBarWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#setBarWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QAbstractBarSeries::setBarWidth(qreal width)
    self.uglySide.call('ritual_ZN18QAbstractBarSeries11setBarWidthEd', width)

  @overload()
  @overload(bool)
  def setLabelsVisible(self, visible: bool = True) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::setLabelsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#setLabelsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QAbstractBarSeries::setLabelsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries16setLabelsVisibleEb', visible,
    )

  @overload(str)
  def setLabelsFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::setLabelsFormat(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#setLabelsFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractBarSeries::setLabelsFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries15setLabelsFormatERK7QString', format,
    )

  @overload(float)
  def setLabelsAngle(self, angle: float) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::setLabelsAngle(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#setLabelsAngle

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QAbstractBarSeries::setLabelsAngle(qreal angle)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries14setLabelsAngleEd', angle,
    )

  @overload(LabelsPosition)
  def setLabelsPosition(self, position: LabelsPosition) -> None:
    """
    Calls Qt's 'void
    QAbstractBarSeries::setLabelsPosition(QAbstractBarSeries::LabelsPosition
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#setLabelsPosition

    Parameters
    ----------

    position : LabelsPosition
      Passed on as its number.
    """
    #  void QAbstractBarSeries::setLabelsPosition(QAbstractBarSeries::
    #      LabelsPosition position)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries17setLabelsPositionENS_14LabelsPositi'
        'onE',
        position.value,
    )

  @overload(int)
  def setLabelsPrecision(self, precision: int) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::setLabelsPrecision(int precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#setLabelsPrecision

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QAbstractBarSeries::setLabelsPrecision(int precision)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries18setLabelsPrecisionEi', precision,
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
    Qt's 'QAbstractBarSeries::QAbstractBarSeries(QAbstractBarSeriesPrivate
    &d, QObject *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractBarSeries.__init__' has no cute function yet. Qt's "
        "'QAbstractBarSeries::QAbstractBarSeries(QAbstractBarSeriesPrivate "
        "&d, QObject *parent)': takes a type Python has no way to hand over "
        "yet.")

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
    Calls Qt's 'bool QAbstractBarSeries::append(QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#append

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeries::append(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries6appendEP7QBarSet',
        self._addressOf(set),
    )

  @overload(QList[QBarSet])
  def append(self, sets: QList[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeries::append(const QList<QBarSet *>
    &sets)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#append

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QAbstractBarSeries::append(const QList<QBarSet *> &sets)
    return self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries6appendERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(QBarSet)
  @overload(NoneType)
  def remove(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeries::remove(QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#remove

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeries::remove(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries6removeEP7QBarSet',
        self._addressOf(set),
    )

  @overload(QBarSet)
  @overload(NoneType)
  def take(self, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeries::take(QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#take

    Parameters
    ----------

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeries::take(QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries4takeEP7QBarSet', self._addressOf(set),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def insert(self, index: int, set: Optional[QBarSet]) -> bool:
    """
    Calls Qt's 'bool QAbstractBarSeries::insert(int index, QBarSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#insert

    Parameters
    ----------

    index : int
      Passed on as it is.

    set : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractBarSeries::insert(int index, QBarSet *set)
    return self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries6insertEiP7QBarSet',
        index, self._addressOf(set),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#clear
    """
    #  void QAbstractBarSeries::clear()
    self.uglySide.call('ritual_ZN18QAbstractBarSeries5clearEv')

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def clicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::clicked(int index, QBarSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeries::clicked(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries7clickedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(bool, int, QBarSet)
  @overload(bool, int, NoneType)
  def hovered(
      self,
      status: bool,
      index: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::hovered(bool status, int index,
    QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeries::hovered(bool status, int index, QBarSet
    #      *barset)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries7hoveredEbiP7QBarSet',
        status, index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def pressed(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::pressed(int index, QBarSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeries::pressed(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries7pressedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def released(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::released(int index, QBarSet
    *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeries::released(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries8releasedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def doubleClicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::doubleClicked(int index, QBarSet
    *barset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractBarSeries::doubleClicked(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries13doubleClickedEiP7QBarSet',
        index, self._addressOf(barset),
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#countChanged
    """
    #  void QAbstractBarSeries::countChanged()
    self.uglySide.call('ritual_ZN18QAbstractBarSeries12countChangedEv')

  def labelsVisibleChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::labelsVisibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsVisibleChanged
    """
    #  void QAbstractBarSeries::labelsVisibleChanged()
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries20labelsVisibleChangedEv',
    )

  @overload(str)
  def labelsFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::labelsFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractBarSeries::labelsFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries19labelsFormatChangedERK7QString',
        format,
    )

  @overload(LabelsPosition)
  def labelsPositionChanged(self, position: LabelsPosition) -> None:
    """
    Calls Qt's 'void
    QAbstractBarSeries::labelsPositionChanged(QAbstractBarSeries::
    LabelsPosition position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsPositionChanged

    Parameters
    ----------

    position : LabelsPosition
      Passed on as its number.
    """
    #  void QAbstractBarSeries::labelsPositionChanged(QAbstractBarSeries::
    #      LabelsPosition position)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries21labelsPositionChangedENS_14LabelsPo'
        'sitionE',
        position.value,
    )

  @overload(float)
  def labelsAngleChanged(self, angle: float) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::labelsAngleChanged(qreal angle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsAngleChanged

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QAbstractBarSeries::labelsAngleChanged(qreal angle)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries18labelsAngleChangedEd', angle,
    )

  @overload(int)
  def labelsPrecisionChanged(self, precision: int) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::labelsPrecisionChanged(int
    precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#labelsPrecisionChanged

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QAbstractBarSeries::labelsPrecisionChanged(int precision)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries22labelsPrecisionChangedEi', precision,
    )

  @overload(QList[QBarSet])
  def barsetsAdded(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::barsetsAdded(const QList<QBarSet *>
    &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#barsetsAdded

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAbstractBarSeries::barsetsAdded(const QList<QBarSet *> &sets)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries12barsetsAddedERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  @overload(QList[QBarSet])
  def barsetsRemoved(self, sets: QList[QBarSet]) -> None:
    """
    Calls Qt's 'void QAbstractBarSeries::barsetsRemoved(const QList<QBarSet
    *> &sets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbarseries.html#barsetsRemoved

    Parameters
    ----------

    sets : QList[QBarSet]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAbstractBarSeries::barsetsRemoved(const QList<QBarSet *> &sets)
    self.uglySide.call(
        'ritual_ZN18QAbstractBarSeries14barsetsRemovedERK5QListIP7QBarSetE',
        self._valueOf(sets),
    )

  def d_func(self) -> Optional[QAbstractBarSeriesPrivate]:
    """
    Calls Qt's 'QAbstractBarSeriesPrivate *QAbstractBarSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbarseries.html#d_func

    Returns
    -------

    Optional[QAbstractBarSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractBarSeriesPrivate *QAbstractBarSeries::d_func()
    address = self.uglySide.call('ritual_ZN18QAbstractBarSeries6d_funcEv')
    from . import QAbstractBarSeriesPrivate
    return QAbstractBarSeriesPrivate._cuteAt(address)
