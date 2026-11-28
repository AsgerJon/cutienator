"""
QLogValueAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qlogvalueaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QLogValueAxisPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLogValueAxis(QAbstractAxis):
  """
  The cute side of Qt's QLogValueAxis: a plain Python object standing in
  front of one C++ QLogValueAxis.

  It is built on the cute 'QAbstractAxis', as Qt's QLogValueAxis is built on
  Qt's QAbstractAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLogValueAxis that has a ritual and that Python can
  call so far, 23 names in all: 'metaObject', 'tr', 'type', 'setMin', 'min',
  'setMax', 'max', 'setRange', 'setLabelFormat', 'labelFormat', 'setBase',
  'base', 'tickCount', 'setMinorTickCount', 'minorTickCount', 'minChanged',
  'maxChanged', 'rangeChanged', 'labelFormatChanged', 'baseChanged',
  'tickCountChanged', 'minorTickCountChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLogValueAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QLogValueAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QLogValueAxis::~QLogValueAxis()': the destructor: Python never
    removes a C++ QLogValueAxis.
  - Qt's 'QLogValueAxis::QLogValueAxis(QLogValueAxisPrivate &d, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QLogValueAxisPrivate *QLogValueAxis::d_func() const': takes
    in Python what 'QLogValueAxisPrivate *QLogValueAxis::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 33 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QLogValueAxis is created at the first use, not by
    'QLogValueAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLogValueAxis.
  - Qt tells when it has removed the C++ QLogValueAxis. Every call on the
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
    Calls Qt's 'QString QLogValueAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#tr

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
    #  QString QLogValueAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QLogValueAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLogValueAxis'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtCharts'

  #  A C++ QLogValueAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLogValueAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLogValueAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLogValueAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QLogValueAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'AxisType QLogValueAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#type

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  AxisType QLogValueAxis::type() const
    ritual = 'ritual_ZNK13QLogValueAxis4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QLogValueAxis4typeEv'
    return QAbstractAxis.AxisType(self.uglySide.call(ritual))

  def min(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#min
    """
    #  qreal QLogValueAxis::min() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#max
    """
    #  qreal QLogValueAxis::max() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis3maxEv')

  def labelFormat(self) -> str:
    """
    Calls Qt's 'QString QLogValueAxis::labelFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#labelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLogValueAxis::labelFormat() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis11labelFormatEv')

  def base(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#base
    """
    #  qreal QLogValueAxis::base() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis4baseEv')

  def tickCount(self) -> int:
    """
    Calls Qt's 'int QLogValueAxis::tickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#tickCount
    """
    #  int QLogValueAxis::tickCount() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis9tickCountEv')

  def minorTickCount(self) -> int:
    """
    Calls Qt's 'int QLogValueAxis::minorTickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#minorTickCount
    """
    #  int QLogValueAxis::minorTickCount() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis14minorTickCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setMin(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QLogValueAxis::setMin(qreal min)
    self.uglySide.call('ritual_ZN13QLogValueAxis6setMinEd', min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setMax(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QLogValueAxis::setMax(qreal max)
    self.uglySide.call('ritual_ZN13QLogValueAxis6setMaxEd', max)

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QLogValueAxis::setRange(qreal min, qreal max)
    self.uglySide.call('ritual_ZN13QLogValueAxis8setRangeEdd', min, max)

  @overload(str)
  def setLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setLabelFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLogValueAxis::setLabelFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis14setLabelFormatERK7QString', format,
    )

  @overload(float)
  def setBase(self, base: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setBase(qreal base)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setBase

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void QLogValueAxis::setBase(qreal base)
    self.uglySide.call('ritual_ZN13QLogValueAxis7setBaseEd', base)

  @overload(int)
  def setMinorTickCount(self, minorTickCount: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setMinorTickCount(int minorTickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#setMinorTickCount

    Parameters
    ----------

    minorTickCount : int
      Passed on as it is.
    """
    #  void QLogValueAxis::setMinorTickCount(int minorTickCount)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis17setMinorTickCountEi', minorTickCount,
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
    Notes what was given, for Qt's 'QLogValueAxis::QLogValueAxis(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#QLogValueAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLogValueAxis::QLogValueAxis(QObject *parent)
    self._noteCreation(QLogValueAxis, lambda: Rituals.call(
        'ritual_ZN13QLogValueAxisC1EP7QObject',
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

  @overload(float)
  def minChanged(self, min: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::minChanged(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#minChanged

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QLogValueAxis::minChanged(qreal min)
    self.uglySide.call('ritual_ZN13QLogValueAxis10minChangedEd', min)

  @overload(float)
  def maxChanged(self, max: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::maxChanged(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#maxChanged

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QLogValueAxis::maxChanged(qreal max)
    self.uglySide.call('ritual_ZN13QLogValueAxis10maxChangedEd', max)

  @overload(float, float)
  def rangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::rangeChanged(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#rangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QLogValueAxis::rangeChanged(qreal min, qreal max)
    self.uglySide.call('ritual_ZN13QLogValueAxis12rangeChangedEdd', min, max)

  @overload(str)
  def labelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QLogValueAxis::labelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#labelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLogValueAxis::labelFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis18labelFormatChangedERK7QString', format,
    )

  @overload(float)
  def baseChanged(self, base: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::baseChanged(qreal base)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#baseChanged

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void QLogValueAxis::baseChanged(qreal base)
    self.uglySide.call('ritual_ZN13QLogValueAxis11baseChangedEd', base)

  @overload(int)
  def tickCountChanged(self, tickCount: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::tickCountChanged(int tickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#tickCountChanged

    Parameters
    ----------

    tickCount : int
      Passed on as it is.
    """
    #  void QLogValueAxis::tickCountChanged(int tickCount)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis16tickCountChangedEi', tickCount,
    )

  @overload(int)
  def minorTickCountChanged(self, minorTickCount: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::minorTickCountChanged(int
    minorTickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#minorTickCountChanged

    Parameters
    ----------

    minorTickCount : int
      Passed on as it is.
    """
    #  void QLogValueAxis::minorTickCountChanged(int minorTickCount)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis21minorTickCountChangedEi', minorTickCount,
    )

  def d_func(self) -> Optional[QLogValueAxisPrivate]:
    """
    Calls Qt's 'QLogValueAxisPrivate *QLogValueAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#d_func

    Returns
    -------

    Optional[QLogValueAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLogValueAxisPrivate *QLogValueAxis::d_func()
    address = self.uglySide.call('ritual_ZN13QLogValueAxis6d_funcEv')
    from . import QLogValueAxisPrivate
    return QLogValueAxisPrivate._cuteAt(address)
