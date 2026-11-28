"""
QDateTimeAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qdatetimeaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QMetaObject
  from . import QDateTimeAxisPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDateTimeAxis(QAbstractAxis):
  """
  The cute side of Qt's QDateTimeAxis: a plain Python object standing in
  front of one C++ QDateTimeAxis.

  It is built on the cute 'QAbstractAxis', as Qt's QDateTimeAxis is built on
  Qt's QAbstractAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDateTimeAxis that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'type', 'setMin', 'min',
  'setMax', 'max', 'setRange', 'setFormat', 'format', 'setTickCount',
  'tickCount', 'minChanged', 'maxChanged', 'rangeChanged', 'formatChanged',
  'tickCountChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDateTimeAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDateTimeAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QDateTimeAxis::~QDateTimeAxis()': the destructor: Python never
    removes a C++ QDateTimeAxis.
  - Qt's 'QDateTimeAxis::QDateTimeAxis(QDateTimeAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QDateTimeAxisPrivate *QDateTimeAxis::d_func() const': takes
    in Python what 'QDateTimeAxisPrivate *QDateTimeAxis::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDateTimeAxis is created at the first use, not by
    'QDateTimeAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDateTimeAxis.
  - Qt tells when it has removed the C++ QDateTimeAxis. Every call on the
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
    Calls Qt's 'QString QDateTimeAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#tr

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
    #  QString QDateTimeAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QDateTimeAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTimeAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QDateTimeAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDateTimeAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDateTimeAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDateTimeAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'AxisType QDateTimeAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#type

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  AxisType QDateTimeAxis::type() const
    ritual = 'ritual_ZNK13QDateTimeAxis4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QDateTimeAxis4typeEv'
    return QAbstractAxis.AxisType(self.uglySide.call(ritual))

  def min(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeAxis::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#min

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeAxis::min() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeAxis3minEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def max(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeAxis::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#max

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeAxis::max() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeAxis3maxEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def format(self) -> str:
    """
    Calls Qt's 'QString QDateTimeAxis::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#format

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeAxis::format() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis6formatEv')

  def tickCount(self) -> int:
    """
    Calls Qt's 'int QDateTimeAxis::tickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#tickCount
    """
    #  int QDateTimeAxis::tickCount() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis9tickCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setMin(self, min: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setMin(QDateTime min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setMin

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::setMin(QDateTime min)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis6setMinE9QDateTime', self._valueOf(min),
    )

  @overload(QDateTime)
  def setMax(self, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setMax(QDateTime max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setMax

    Parameters
    ----------

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::setMax(QDateTime max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis6setMaxE9QDateTime', self._valueOf(max),
    )

  @overload(QDateTime, QDateTime)
  def setRange(self, min: QDateTime, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setRange(QDateTime min, QDateTime max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setRange

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::setRange(QDateTime min, QDateTime max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis8setRangeE9QDateTimeS0_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(str)
  def setFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setFormat(QString format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDateTimeAxis::setFormat(QString format)
    self.uglySide.call('ritual_ZN13QDateTimeAxis9setFormatE7QString', format)

  @overload(int)
  def setTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setTickCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QDateTimeAxis::setTickCount(int count)
    self.uglySide.call('ritual_ZN13QDateTimeAxis12setTickCountEi', count)

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
    Notes what was given, for Qt's 'QDateTimeAxis::QDateTimeAxis(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#QDateTimeAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDateTimeAxis::QDateTimeAxis(QObject *parent)
    self._noteCreation(QDateTimeAxis, lambda: Rituals.call(
        'ritual_ZN13QDateTimeAxisC1EP7QObject',
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

  @overload(QDateTime)
  def minChanged(self, min: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::minChanged(QDateTime min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#minChanged

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::minChanged(QDateTime min)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis10minChangedE9QDateTime',
        self._valueOf(min),
    )

  @overload(QDateTime)
  def maxChanged(self, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::maxChanged(QDateTime max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#maxChanged

    Parameters
    ----------

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::maxChanged(QDateTime max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis10maxChangedE9QDateTime',
        self._valueOf(max),
    )

  @overload(QDateTime, QDateTime)
  def rangeChanged(self, min: QDateTime, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::rangeChanged(QDateTime min, QDateTime
    max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#rangeChanged

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::rangeChanged(QDateTime min, QDateTime max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis12rangeChangedE9QDateTimeS0_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(str)
  def formatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::formatChanged(QString format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#formatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDateTimeAxis::formatChanged(QString format)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis13formatChangedE7QString', format,
    )

  @overload(int)
  def tickCountChanged(self, tick: int) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::tickCountChanged(int tick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#tickCountChanged

    Parameters
    ----------

    tick : int
      Passed on as it is.
    """
    #  void QDateTimeAxis::tickCountChanged(int tick)
    self.uglySide.call('ritual_ZN13QDateTimeAxis16tickCountChangedEi', tick)

  def d_func(self) -> Optional[QDateTimeAxisPrivate]:
    """
    Calls Qt's 'QDateTimeAxisPrivate *QDateTimeAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#d_func

    Returns
    -------

    Optional[QDateTimeAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDateTimeAxisPrivate *QDateTimeAxis::d_func()
    address = self.uglySide.call('ritual_ZN13QDateTimeAxis6d_funcEv')
    from . import QDateTimeAxisPrivate
    return QDateTimeAxisPrivate._cuteAt(address)
