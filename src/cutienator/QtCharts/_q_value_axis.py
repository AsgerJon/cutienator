"""
QValueAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qvalueaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QValueAxisPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QValueAxis(QAbstractAxis):
  """
  The cute side of Qt's QValueAxis: a plain Python object standing in front
  of one C++ QValueAxis.

  It is built on the cute 'QAbstractAxis', as Qt's QValueAxis is built on
  Qt's QAbstractAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QValueAxis that has a ritual and that Python can
  call so far, 31 names in all: 'metaObject', 'tr', 'type', 'setMin', 'min',
  'setMax', 'max', 'setRange', 'setTickCount', 'tickCount',
  'setMinorTickCount', 'minorTickCount', 'setTickAnchor', 'tickAnchor',
  'setTickInterval', 'tickInterval', 'setTickType', 'tickType',
  'setLabelFormat', 'labelFormat', 'applyNiceNumbers', 'minChanged',
  'maxChanged', 'rangeChanged', 'tickCountChanged', 'minorTickCountChanged',
  'labelFormatChanged', 'tickIntervalChanged', 'tickAnchorChanged',
  'tickTypeChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QValueAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QValueAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QValueAxis::~QValueAxis()': the destructor: Python never removes a
    C++ QValueAxis.
  - Qt's 'QValueAxis::QValueAxis(QValueAxisPrivate &d, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QValueAxisPrivate *QValueAxis::d_func() const': takes in
    Python what 'QValueAxisPrivate *QValueAxis::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QValueAxis is created at the first use, not by 'QValueAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QValueAxis.
  - Qt tells when it has removed the C++ QValueAxis. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QValueAxis, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class TickType(CuteNum):
    """
    The enum 'QValueAxis::TickType' of Qt, with the 2 names Qt gives in it.
    """

    TicksDynamic = Kee[int](0)
    TicksFixed = Kee[int](1)

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
    Calls Qt's 'QString QValueAxis::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tr

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
    #  QString QValueAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QValueAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QValueAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QValueAxis Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QValueAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QValueAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QValueAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QValueAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'AxisType QValueAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#type

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  AxisType QValueAxis::type() const
    ritual = 'ritual_ZNK10QValueAxis4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QValueAxis4typeEv'
    return QAbstractAxis.AxisType(self.uglySide.call(ritual))

  def min(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#min
    """
    #  qreal QValueAxis::min() const
    return self.uglySide.call('ritual_ZNK10QValueAxis3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#max
    """
    #  qreal QValueAxis::max() const
    return self.uglySide.call('ritual_ZNK10QValueAxis3maxEv')

  def tickCount(self) -> int:
    """
    Calls Qt's 'int QValueAxis::tickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickCount
    """
    #  int QValueAxis::tickCount() const
    return self.uglySide.call('ritual_ZNK10QValueAxis9tickCountEv')

  def minorTickCount(self) -> int:
    """
    Calls Qt's 'int QValueAxis::minorTickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#minorTickCount
    """
    #  int QValueAxis::minorTickCount() const
    return self.uglySide.call('ritual_ZNK10QValueAxis14minorTickCountEv')

  def tickAnchor(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::tickAnchor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickAnchor
    """
    #  qreal QValueAxis::tickAnchor() const
    return self.uglySide.call('ritual_ZNK10QValueAxis10tickAnchorEv')

  def tickInterval(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::tickInterval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickInterval
    """
    #  qreal QValueAxis::tickInterval() const
    return self.uglySide.call('ritual_ZNK10QValueAxis12tickIntervalEv')

  def tickType(self) -> TickType:
    """
    Calls Qt's 'QValueAxis::TickType QValueAxis::tickType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickType

    Returns
    -------

    TickType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TickType(number)' gives.
    """
    #  QValueAxis::TickType QValueAxis::tickType() const
    return QValueAxis.TickType(self.uglySide.call(
        'ritual_ZNK10QValueAxis8tickTypeEv',
    ))

  def labelFormat(self) -> str:
    """
    Calls Qt's 'QString QValueAxis::labelFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#labelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QValueAxis::labelFormat() const
    return self.uglySide.call('ritual_ZNK10QValueAxis11labelFormatEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setMin(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QValueAxis::setMin(qreal min)
    self.uglySide.call('ritual_ZN10QValueAxis6setMinEd', min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setMax(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QValueAxis::setMax(qreal max)
    self.uglySide.call('ritual_ZN10QValueAxis6setMaxEd', max)

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QValueAxis::setRange(qreal min, qreal max)
    self.uglySide.call('ritual_ZN10QValueAxis8setRangeEdd', min, max)

  @overload(int)
  def setTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QValueAxis::setTickCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValueAxis::setTickCount(int count)
    self.uglySide.call('ritual_ZN10QValueAxis12setTickCountEi', count)

  @overload(int)
  def setMinorTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QValueAxis::setMinorTickCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setMinorTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValueAxis::setMinorTickCount(int count)
    self.uglySide.call('ritual_ZN10QValueAxis17setMinorTickCountEi', count)

  @overload(float)
  def setTickAnchor(self, anchor: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setTickAnchor(qreal anchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setTickAnchor

    Parameters
    ----------

    anchor : float
      Passed on as it is.
    """
    #  void QValueAxis::setTickAnchor(qreal anchor)
    self.uglySide.call('ritual_ZN10QValueAxis13setTickAnchorEd', anchor)

  @overload(float)
  def setTickInterval(self, insterval: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setTickInterval(qreal insterval)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setTickInterval

    Parameters
    ----------

    insterval : float
      Passed on as it is.
    """
    #  void QValueAxis::setTickInterval(qreal insterval)
    self.uglySide.call('ritual_ZN10QValueAxis15setTickIntervalEd', insterval)

  @overload(TickType)
  def setTickType(self, type: TickType) -> None:
    """
    Calls Qt's 'void QValueAxis::setTickType(QValueAxis::TickType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setTickType

    Parameters
    ----------

    type : TickType
      Passed on as its number.
    """
    #  void QValueAxis::setTickType(QValueAxis::TickType type)
    self.uglySide.call(
        'ritual_ZN10QValueAxis11setTickTypeENS_8TickTypeE', type.value,
    )

  @overload(str)
  def setLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QValueAxis::setLabelFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QValueAxis::setLabelFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN10QValueAxis14setLabelFormatERK7QString', format,
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
    Notes what was given, for Qt's 'QValueAxis::QValueAxis(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#QValueAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QValueAxis::QValueAxis(QObject *parent)
    self._noteCreation(QValueAxis, lambda: Rituals.call(
        'ritual_ZN10QValueAxisC1EP7QObject',
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

  def applyNiceNumbers(self) -> None:
    """
    Calls Qt's 'void QValueAxis::applyNiceNumbers()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#applyNiceNumbers
    """
    #  void QValueAxis::applyNiceNumbers()
    self.uglySide.call('ritual_ZN10QValueAxis16applyNiceNumbersEv')

  @overload(float)
  def minChanged(self, min: float) -> None:
    """
    Calls Qt's 'void QValueAxis::minChanged(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#minChanged

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QValueAxis::minChanged(qreal min)
    self.uglySide.call('ritual_ZN10QValueAxis10minChangedEd', min)

  @overload(float)
  def maxChanged(self, max: float) -> None:
    """
    Calls Qt's 'void QValueAxis::maxChanged(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#maxChanged

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QValueAxis::maxChanged(qreal max)
    self.uglySide.call('ritual_ZN10QValueAxis10maxChangedEd', max)

  @overload(float, float)
  def rangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QValueAxis::rangeChanged(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#rangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QValueAxis::rangeChanged(qreal min, qreal max)
    self.uglySide.call('ritual_ZN10QValueAxis12rangeChangedEdd', min, max)

  @overload(int)
  def tickCountChanged(self, tickCount: int) -> None:
    """
    Calls Qt's 'void QValueAxis::tickCountChanged(int tickCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickCountChanged

    Parameters
    ----------

    tickCount : int
      Passed on as it is.
    """
    #  void QValueAxis::tickCountChanged(int tickCount)
    self.uglySide.call(
        'ritual_ZN10QValueAxis16tickCountChangedEi', tickCount,
    )

  @overload(int)
  def minorTickCountChanged(self, tickCount: int) -> None:
    """
    Calls Qt's 'void QValueAxis::minorTickCountChanged(int tickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxis.html#minorTickCountChanged

    Parameters
    ----------

    tickCount : int
      Passed on as it is.
    """
    #  void QValueAxis::minorTickCountChanged(int tickCount)
    self.uglySide.call(
        'ritual_ZN10QValueAxis21minorTickCountChangedEi', tickCount,
    )

  @overload(str)
  def labelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QValueAxis::labelFormatChanged(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#labelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QValueAxis::labelFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN10QValueAxis18labelFormatChangedERK7QString', format,
    )

  @overload(float)
  def tickIntervalChanged(self, interval: float) -> None:
    """
    Calls Qt's 'void QValueAxis::tickIntervalChanged(qreal interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxis.html#tickIntervalChanged

    Parameters
    ----------

    interval : float
      Passed on as it is.
    """
    #  void QValueAxis::tickIntervalChanged(qreal interval)
    self.uglySide.call(
        'ritual_ZN10QValueAxis19tickIntervalChangedEd', interval,
    )

  @overload(float)
  def tickAnchorChanged(self, anchor: float) -> None:
    """
    Calls Qt's 'void QValueAxis::tickAnchorChanged(qreal anchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickAnchorChanged

    Parameters
    ----------

    anchor : float
      Passed on as it is.
    """
    #  void QValueAxis::tickAnchorChanged(qreal anchor)
    self.uglySide.call('ritual_ZN10QValueAxis17tickAnchorChangedEd', anchor)

  @overload(TickType)
  def tickTypeChanged(self, type: TickType) -> None:
    """
    Calls Qt's 'void QValueAxis::tickTypeChanged(QValueAxis::TickType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickTypeChanged

    Parameters
    ----------

    type : TickType
      Passed on as its number.
    """
    #  void QValueAxis::tickTypeChanged(QValueAxis::TickType type)
    self.uglySide.call(
        'ritual_ZN10QValueAxis15tickTypeChangedENS_8TickTypeE', type.value,
    )

  def d_func(self) -> Optional[QValueAxisPrivate]:
    """
    Calls Qt's 'QValueAxisPrivate *QValueAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#d_func

    Returns
    -------

    Optional[QValueAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValueAxisPrivate *QValueAxis::d_func()
    address = self.uglySide.call('ritual_ZN10QValueAxis6d_funcEv')
    from . import QValueAxisPrivate
    return QValueAxisPrivate._cuteAt(address)
