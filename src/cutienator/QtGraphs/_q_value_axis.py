"""
QValueAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qvalueaxis.h, Qt 6.12.0. Changes made here are lost.
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
  call so far, 40 names in all: 'metaObject', 'tr', 'type', 'setMin', 'min',
  'setMax', 'max', 'setRange', 'setSubTickCount', 'subTickCount',
  'setTickAnchor', 'tickAnchor', 'setTickInterval', 'tickInterval',
  'setLabelFormat', 'labelFormat', 'setLabelPostFormat', 'labelPostFormat',
  'setLabelDecimals', 'labelDecimals', 'setZoom', 'zoom', 'setPan', 'pan',
  'visualMin', 'visualMax', 'minChanged', 'maxChanged', 'rangeChanged',
  'subTickCountChanged', 'labelFormatChanged', 'labelPostFormatChanged',
  'labelDecimalsChanged', 'tickAnchorChanged', 'tickIntervalChanged',
  'zoomChanged', 'panChanged', 'visualMinChanged', 'visualMaxChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

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

  4 of the 50 functions Qt declares: 2 not a gap; 2 forbidden.

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
  __qt_part__ = 'QtGraphs'

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

  def subTickCount(self) -> int:
    """
    Calls Qt's 'qsizetype QValueAxis::subTickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#subTickCount
    """
    #  qsizetype QValueAxis::subTickCount() const
    return self.uglySide.call('ritual_ZNK10QValueAxis12subTickCountEv')

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

  def labelPostFormat(self) -> str:
    """
    Calls Qt's 'QString QValueAxis::labelPostFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#labelPostFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QValueAxis::labelPostFormat() const
    return self.uglySide.call('ritual_ZNK10QValueAxis15labelPostFormatEv')

  def labelDecimals(self) -> int:
    """
    Calls Qt's 'int QValueAxis::labelDecimals() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#labelDecimals
    """
    #  int QValueAxis::labelDecimals() const
    return self.uglySide.call('ritual_ZNK10QValueAxis13labelDecimalsEv')

  def zoom(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::zoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#zoom
    """
    #  qreal QValueAxis::zoom() const
    return self.uglySide.call('ritual_ZNK10QValueAxis4zoomEv')

  def pan(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::pan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#pan
    """
    #  qreal QValueAxis::pan() const
    return self.uglySide.call('ritual_ZNK10QValueAxis3panEv')

  def visualMin(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::visualMin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#visualMin
    """
    #  qreal QValueAxis::visualMin() const
    return self.uglySide.call('ritual_ZNK10QValueAxis9visualMinEv')

  def visualMax(self) -> float:
    """
    Calls Qt's 'qreal QValueAxis::visualMax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#visualMax
    """
    #  qreal QValueAxis::visualMax() const
    return self.uglySide.call('ritual_ZNK10QValueAxis9visualMaxEv')

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
  def setSubTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QValueAxis::setSubTickCount(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setSubTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QValueAxis::setSubTickCount(qsizetype count)
    self.uglySide.call('ritual_ZN10QValueAxis15setSubTickCountEx', count)

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
  def setTickInterval(self, interval: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setTickInterval(qreal interval)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setTickInterval

    Parameters
    ----------

    interval : float
      Passed on as it is.
    """
    #  void QValueAxis::setTickInterval(qreal interval)
    self.uglySide.call('ritual_ZN10QValueAxis15setTickIntervalEd', interval)

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

  @overload(str)
  def setLabelPostFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QValueAxis::setLabelPostFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setLabelPostFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QValueAxis::setLabelPostFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN10QValueAxis18setLabelPostFormatERK7QString', format,
    )

  @overload(int)
  def setLabelDecimals(self, decimals: int) -> None:
    """
    Calls Qt's 'void QValueAxis::setLabelDecimals(int decimals)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setLabelDecimals

    Parameters
    ----------

    decimals : int
      Passed on as it is.
    """
    #  void QValueAxis::setLabelDecimals(int decimals)
    self.uglySide.call('ritual_ZN10QValueAxis16setLabelDecimalsEi', decimals)

  @overload(float)
  def setZoom(self, zoom: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setZoom(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setZoom

    Parameters
    ----------

    zoom : float
      Passed on as it is.
    """
    #  void QValueAxis::setZoom(qreal zoom)
    self.uglySide.call('ritual_ZN10QValueAxis7setZoomEd', zoom)

  @overload(float)
  def setPan(self, pan: float) -> None:
    """
    Calls Qt's 'void QValueAxis::setPan(qreal pan)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#setPan

    Parameters
    ----------

    pan : float
      Passed on as it is.
    """
    #  void QValueAxis::setPan(qreal pan)
    self.uglySide.call('ritual_ZN10QValueAxis6setPanEd', pan)

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
  def subTickCountChanged(self, subTickCount: int) -> None:
    """
    Calls Qt's 'void QValueAxis::subTickCountChanged(qsizetype
    subTickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxis.html#subTickCountChanged

    Parameters
    ----------

    subTickCount : int
      Passed on as it is.
    """
    #  void QValueAxis::subTickCountChanged(qsizetype subTickCount)
    self.uglySide.call(
        'ritual_ZN10QValueAxis19subTickCountChangedEx', subTickCount,
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

  @overload(str)
  def labelPostFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QValueAxis::labelPostFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxis.html#labelPostFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QValueAxis::labelPostFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN10QValueAxis22labelPostFormatChangedERK7QString', format,
    )

  @overload(int)
  def labelDecimalsChanged(self, decimals: int) -> None:
    """
    Calls Qt's 'void QValueAxis::labelDecimalsChanged(int decimals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxis.html#labelDecimalsChanged

    Parameters
    ----------

    decimals : int
      Passed on as it is.
    """
    #  void QValueAxis::labelDecimalsChanged(int decimals)
    self.uglySide.call(
        'ritual_ZN10QValueAxis20labelDecimalsChangedEi', decimals,
    )

  @overload(float)
  def tickAnchorChanged(self, tickAnchor: float) -> None:
    """
    Calls Qt's 'void QValueAxis::tickAnchorChanged(qreal tickAnchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#tickAnchorChanged

    Parameters
    ----------

    tickAnchor : float
      Passed on as it is.
    """
    #  void QValueAxis::tickAnchorChanged(qreal tickAnchor)
    self.uglySide.call(
        'ritual_ZN10QValueAxis17tickAnchorChangedEd', tickAnchor,
    )

  @overload(float)
  def tickIntervalChanged(self, tickInterval: float) -> None:
    """
    Calls Qt's 'void QValueAxis::tickIntervalChanged(qreal tickInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvalueaxis.html#tickIntervalChanged

    Parameters
    ----------

    tickInterval : float
      Passed on as it is.
    """
    #  void QValueAxis::tickIntervalChanged(qreal tickInterval)
    self.uglySide.call(
        'ritual_ZN10QValueAxis19tickIntervalChangedEd', tickInterval,
    )

  @overload(float)
  def zoomChanged(self, zoom: float) -> None:
    """
    Calls Qt's 'void QValueAxis::zoomChanged(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#zoomChanged

    Parameters
    ----------

    zoom : float
      Passed on as it is.
    """
    #  void QValueAxis::zoomChanged(qreal zoom)
    self.uglySide.call('ritual_ZN10QValueAxis11zoomChangedEd', zoom)

  @overload(float)
  def panChanged(self, pan: float) -> None:
    """
    Calls Qt's 'void QValueAxis::panChanged(qreal pan)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#panChanged

    Parameters
    ----------

    pan : float
      Passed on as it is.
    """
    #  void QValueAxis::panChanged(qreal pan)
    self.uglySide.call('ritual_ZN10QValueAxis10panChangedEd', pan)

  @overload(float)
  def visualMinChanged(self, newVisualMin: float) -> None:
    """
    Calls Qt's 'void QValueAxis::visualMinChanged(qreal newVisualMin)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#visualMinChanged

    Parameters
    ----------

    newVisualMin : float
      Passed on as it is.
    """
    #  void QValueAxis::visualMinChanged(qreal newVisualMin)
    self.uglySide.call(
        'ritual_ZN10QValueAxis16visualMinChangedEd', newVisualMin,
    )

  @overload(float)
  def visualMaxChanged(self, newVisualMax: float) -> None:
    """
    Calls Qt's 'void QValueAxis::visualMaxChanged(qreal newVisualMax)'.

    Qt's own words: https://doc.qt.io/qt-6/qvalueaxis.html#visualMaxChanged

    Parameters
    ----------

    newVisualMax : float
      Passed on as it is.
    """
    #  void QValueAxis::visualMaxChanged(qreal newVisualMax)
    self.uglySide.call(
        'ritual_ZN10QValueAxis16visualMaxChangedEd', newVisualMax,
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
