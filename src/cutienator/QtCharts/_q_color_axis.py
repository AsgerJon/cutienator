"""
QColorAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qcoloraxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QLinearGradient
  from . import QColorAxisPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLinearGradient = WAIT['QLinearGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColorAxis(QAbstractAxis):
  """
  The cute side of Qt's QColorAxis: a plain Python object standing in front
  of one C++ QColorAxis.

  It is built on the cute 'QAbstractAxis', as Qt's QColorAxis is built on
  Qt's QAbstractAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QColorAxis that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'type', 'setMin', 'min',
  'setMax', 'max', 'setRange', 'setTickCount', 'tickCount', 'setSize',
  'size', 'setGradient', 'gradient', 'setAutoRange', 'autoRange',
  'minChanged', 'maxChanged', 'rangeChanged', 'tickCountChanged',
  'gradientChanged', 'sizeChanged', 'autoRangeChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QColorAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QColorAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QColorAxis::~QColorAxis()': the destructor: Python never removes a
    C++ QColorAxis.
  - Qt's 'QColorAxis::QColorAxis(QColorAxisPrivate &d, QObject *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QColorAxisPrivate *QColorAxis::d_func() const': takes in
    Python what 'QColorAxisPrivate *QColorAxis::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QColorAxis is created at the first use, not by 'QColorAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColorAxis.
  - Qt tells when it has removed the C++ QColorAxis. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QColorAxis::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#tr

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
    #  QString QColorAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QColorAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorAxis'

  #  A C++ QColorAxis Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QColorAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QColorAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QColorAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QColorAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QAbstractAxis.AxisType:
    """
    Calls Qt's 'AxisType QColorAxis::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#type

    Returns
    -------

    QAbstractAxis.AxisType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractAxis.AxisType(number)' gives.
    """
    #  AxisType QColorAxis::type() const
    ritual = 'ritual_ZNK10QColorAxis4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QColorAxis4typeEv'
    return QAbstractAxis.AxisType(self.uglySide.call(ritual))

  def min(self) -> float:
    """
    Calls Qt's 'qreal QColorAxis::min() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#min
    """
    #  qreal QColorAxis::min() const
    return self.uglySide.call('ritual_ZNK10QColorAxis3minEv')

  def max(self) -> float:
    """
    Calls Qt's 'qreal QColorAxis::max() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#max
    """
    #  qreal QColorAxis::max() const
    return self.uglySide.call('ritual_ZNK10QColorAxis3maxEv')

  def tickCount(self) -> int:
    """
    Calls Qt's 'int QColorAxis::tickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#tickCount
    """
    #  int QColorAxis::tickCount() const
    return self.uglySide.call('ritual_ZNK10QColorAxis9tickCountEv')

  def size(self) -> float:
    """
    Calls Qt's 'qreal QColorAxis::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#size
    """
    #  qreal QColorAxis::size() const
    return self.uglySide.call('ritual_ZNK10QColorAxis4sizeEv')

  def gradient(self) -> QLinearGradient:
    """
    Calls Qt's 'QLinearGradient QColorAxis::gradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#gradient

    Returns
    -------

    QLinearGradient
      A new cute QLinearGradient around the copy Qt gave back. Python owns
      it.
    """
    #  QLinearGradient QColorAxis::gradient() const
    address = self.uglySide.call('ritual_ZNK10QColorAxis8gradientEv')
    from ..QtGui import QLinearGradient
    return QLinearGradient._cuteOwning(address)

  def autoRange(self) -> bool:
    """
    Calls Qt's 'bool QColorAxis::autoRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#autoRange
    """
    #  bool QColorAxis::autoRange() const
    return self.uglySide.call('ritual_ZNK10QColorAxis9autoRangeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMin(self, min: float) -> None:
    """
    Calls Qt's 'void QColorAxis::setMin(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setMin

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QColorAxis::setMin(qreal min)
    self.uglySide.call('ritual_ZN10QColorAxis6setMinEd', min)

  @overload(float)
  def setMax(self, max: float) -> None:
    """
    Calls Qt's 'void QColorAxis::setMax(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setMax

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QColorAxis::setMax(qreal max)
    self.uglySide.call('ritual_ZN10QColorAxis6setMaxEd', max)

  @overload(float, float)
  def setRange(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QColorAxis::setRange(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QColorAxis::setRange(qreal min, qreal max)
    self.uglySide.call('ritual_ZN10QColorAxis8setRangeEdd', min, max)

  @overload(int)
  def setTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QColorAxis::setTickCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QColorAxis::setTickCount(int count)
    self.uglySide.call('ritual_ZN10QColorAxis12setTickCountEi', count)

  @overload(float)
  def setSize(self, size: float) -> None:
    """
    Calls Qt's 'void QColorAxis::setSize(const qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QColorAxis::setSize(const qreal size)
    self.uglySide.call('ritual_ZN10QColorAxis7setSizeEd', size)

  @overload(QLinearGradient)
  def setGradient(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QColorAxis::setGradient(const QLinearGradient
    &gradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setGradient

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QColorAxis::setGradient(const QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN10QColorAxis11setGradientERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(bool)
  def setAutoRange(self, autoRange: bool) -> None:
    """
    Calls Qt's 'void QColorAxis::setAutoRange(bool autoRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#setAutoRange

    Parameters
    ----------

    autoRange : bool
      Passed on as it is.
    """
    #  void QColorAxis::setAutoRange(bool autoRange)
    self.uglySide.call('ritual_ZN10QColorAxis12setAutoRangeEb', autoRange)

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
    Notes what was given, for Qt's 'QColorAxis::QColorAxis(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#QColorAxis

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QColorAxis::QColorAxis(QObject *parent)
    self._noteCreation(QColorAxis, lambda: Rituals.call(
        'ritual_ZN10QColorAxisC1EP7QObject',
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
    Calls Qt's 'void QColorAxis::minChanged(qreal min)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#minChanged

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QColorAxis::minChanged(qreal min)
    self.uglySide.call('ritual_ZN10QColorAxis10minChangedEd', min)

  @overload(float)
  def maxChanged(self, max: float) -> None:
    """
    Calls Qt's 'void QColorAxis::maxChanged(qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#maxChanged

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QColorAxis::maxChanged(qreal max)
    self.uglySide.call('ritual_ZN10QColorAxis10maxChangedEd', max)

  @overload(float, float)
  def rangeChanged(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QColorAxis::rangeChanged(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#rangeChanged

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QColorAxis::rangeChanged(qreal min, qreal max)
    self.uglySide.call('ritual_ZN10QColorAxis12rangeChangedEdd', min, max)

  @overload(int)
  def tickCountChanged(self, tickCount: int) -> None:
    """
    Calls Qt's 'void QColorAxis::tickCountChanged(int tickCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#tickCountChanged

    Parameters
    ----------

    tickCount : int
      Passed on as it is.
    """
    #  void QColorAxis::tickCountChanged(int tickCount)
    self.uglySide.call(
        'ritual_ZN10QColorAxis16tickCountChangedEi', tickCount,
    )

  @overload(QLinearGradient)
  def gradientChanged(self, gradient: QLinearGradient) -> None:
    """
    Calls Qt's 'void QColorAxis::gradientChanged(const QLinearGradient
    &gradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#gradientChanged

    Parameters
    ----------

    gradient : QLinearGradient
      Passed on as a value: Qt reads the C++ QLinearGradient, which stays
      Python's own.
    """
    #  void QColorAxis::gradientChanged(const QLinearGradient &gradient)
    self.uglySide.call(
        'ritual_ZN10QColorAxis15gradientChangedERK15QLinearGradient',
        self._valueOf(gradient),
    )

  @overload(float)
  def sizeChanged(self, size: float) -> None:
    """
    Calls Qt's 'void QColorAxis::sizeChanged(const qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#sizeChanged

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QColorAxis::sizeChanged(const qreal size)
    self.uglySide.call('ritual_ZN10QColorAxis11sizeChangedEd', size)

  @overload(bool)
  def autoRangeChanged(self, autoRange: bool) -> None:
    """
    Calls Qt's 'void QColorAxis::autoRangeChanged(bool autoRange)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#autoRangeChanged

    Parameters
    ----------

    autoRange : bool
      Passed on as it is.
    """
    #  void QColorAxis::autoRangeChanged(bool autoRange)
    self.uglySide.call(
        'ritual_ZN10QColorAxis16autoRangeChangedEb', autoRange,
    )

  def d_func(self) -> Optional[QColorAxisPrivate]:
    """
    Calls Qt's 'QColorAxisPrivate *QColorAxis::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloraxis.html#d_func

    Returns
    -------

    Optional[QColorAxisPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QColorAxisPrivate *QColorAxis::d_func()
    address = self.uglySide.call('ritual_ZN10QColorAxis6d_funcEv')
    from . import QColorAxisPrivate
    return QColorAxisPrivate._cuteAt(address)
