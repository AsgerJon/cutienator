"""
QLogValueAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qlogvalueaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QLogValueAxisPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

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
  call so far, 40 names in all: 'metaObject', 'tr', 'event', 'type',
  'setMin', 'min', 'setMax', 'max', 'setRange', 'setBase', 'base',
  'setSubTickCount', 'subTickCount', 'tickCount', 'setLabelFormat',
  'labelFormat', 'setLabelPostFormat', 'labelPostFormat',
  'setLabelPrecision', 'labelPrecision', 'setZoom', 'zoom', 'setPan', 'pan',
  'visualMin', 'visualMax', 'minChanged', 'maxChanged', 'baseChanged',
  'rangeChanged', 'subTickCountChanged', 'labelFormatChanged',
  'labelPostFormatChanged', 'labelPrecisionChanged', 'tickCountChanged',
  'zoomChanged', 'panChanged', 'visualMinChanged', 'visualMaxChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

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

  6 of the 52 functions Qt declares: 4 forbidden; 2 not a gap.

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
  __qt_part__ = 'QtGraphs'

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

  def base(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::base() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#base
    """
    #  qreal QLogValueAxis::base() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis4baseEv')

  def subTickCount(self) -> int:
    """
    Calls Qt's 'qsizetype QLogValueAxis::subTickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#subTickCount
    """
    #  qsizetype QLogValueAxis::subTickCount() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis12subTickCountEv')

  def tickCount(self) -> int:
    """
    Calls Qt's 'qsizetype QLogValueAxis::tickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#tickCount
    """
    #  qsizetype QLogValueAxis::tickCount() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis9tickCountEv')

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

  def labelPostFormat(self) -> str:
    """
    Calls Qt's 'QString QLogValueAxis::labelPostFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#labelPostFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLogValueAxis::labelPostFormat() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis15labelPostFormatEv')

  def labelPrecision(self) -> int:
    """
    Calls Qt's 'int QLogValueAxis::labelPrecision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#labelPrecision
    """
    #  int QLogValueAxis::labelPrecision() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis14labelPrecisionEv')

  def zoom(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::zoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#zoom
    """
    #  qreal QLogValueAxis::zoom() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis4zoomEv')

  def pan(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::pan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#pan
    """
    #  qreal QLogValueAxis::pan() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis3panEv')

  def visualMin(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::visualMin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#visualMin
    """
    #  qreal QLogValueAxis::visualMin() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis9visualMinEv')

  def visualMax(self) -> float:
    """
    Calls Qt's 'qreal QLogValueAxis::visualMax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#visualMax
    """
    #  qreal QLogValueAxis::visualMax() const
    return self.uglySide.call('ritual_ZNK13QLogValueAxis9visualMaxEv')

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
  def setSubTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setSubTickCount(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setSubTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QLogValueAxis::setSubTickCount(qsizetype count)
    self.uglySide.call('ritual_ZN13QLogValueAxis15setSubTickCountEx', count)

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

  @overload(str)
  def setLabelPostFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setLabelPostFormat(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#setLabelPostFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLogValueAxis::setLabelPostFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis18setLabelPostFormatERK7QString', format,
    )

  @overload(int)
  def setLabelPrecision(self, decimals: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setLabelPrecision(int decimals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#setLabelPrecision

    Parameters
    ----------

    decimals : int
      Passed on as it is.
    """
    #  void QLogValueAxis::setLabelPrecision(int decimals)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis17setLabelPrecisionEi', decimals,
    )

  @overload(float)
  def setZoom(self, zoom: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setZoom(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setZoom

    Parameters
    ----------

    zoom : float
      Passed on as it is.
    """
    #  void QLogValueAxis::setZoom(qreal zoom)
    self.uglySide.call('ritual_ZN13QLogValueAxis7setZoomEd', zoom)

  @overload(float)
  def setPan(self, pan: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::setPan(qreal pan)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#setPan

    Parameters
    ----------

    pan : float
      Passed on as it is.
    """
    #  void QLogValueAxis::setPan(qreal pan)
    self.uglySide.call('ritual_ZN13QLogValueAxis6setPanEd', pan)

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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QLogValueAxis::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLogValueAxis::event(QEvent *event)
    ritual = 'ritual_ZN13QLogValueAxis5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QLogValueAxis5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

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

  @overload(int)
  def subTickCountChanged(self, subTickCount: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::subTickCountChanged(qsizetype
    subTickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#subTickCountChanged

    Parameters
    ----------

    subTickCount : int
      Passed on as it is.
    """
    #  void QLogValueAxis::subTickCountChanged(qsizetype subTickCount)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis19subTickCountChangedEx', subTickCount,
    )

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

  @overload(str)
  def labelPostFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QLogValueAxis::labelPostFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#labelPostFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLogValueAxis::labelPostFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis22labelPostFormatChangedERK7QString',
        format,
    )

  @overload(int)
  def labelPrecisionChanged(self, precision: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::labelPrecisionChanged(int precision)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#labelPrecisionChanged

    Parameters
    ----------

    precision : int
      Passed on as it is.
    """
    #  void QLogValueAxis::labelPrecisionChanged(int precision)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis21labelPrecisionChangedEi', precision,
    )

  @overload(int)
  def tickCountChanged(self, tickCount: int) -> None:
    """
    Calls Qt's 'void QLogValueAxis::tickCountChanged(qsizetype tickCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#tickCountChanged

    Parameters
    ----------

    tickCount : int
      Passed on as it is.
    """
    #  void QLogValueAxis::tickCountChanged(qsizetype tickCount)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis16tickCountChangedEx', tickCount,
    )

  @overload(float)
  def zoomChanged(self, zoom: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::zoomChanged(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#zoomChanged

    Parameters
    ----------

    zoom : float
      Passed on as it is.
    """
    #  void QLogValueAxis::zoomChanged(qreal zoom)
    self.uglySide.call('ritual_ZN13QLogValueAxis11zoomChangedEd', zoom)

  @overload(float)
  def panChanged(self, pan: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::panChanged(qreal pan)'.

    Qt's own words: https://doc.qt.io/qt-6/qlogvalueaxis.html#panChanged

    Parameters
    ----------

    pan : float
      Passed on as it is.
    """
    #  void QLogValueAxis::panChanged(qreal pan)
    self.uglySide.call('ritual_ZN13QLogValueAxis10panChangedEd', pan)

  @overload(float)
  def visualMinChanged(self, visualMin: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::visualMinChanged(qreal visualMin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#visualMinChanged

    Parameters
    ----------

    visualMin : float
      Passed on as it is.
    """
    #  void QLogValueAxis::visualMinChanged(qreal visualMin)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis16visualMinChangedEd', visualMin,
    )

  @overload(float)
  def visualMaxChanged(self, visualMax: float) -> None:
    """
    Calls Qt's 'void QLogValueAxis::visualMaxChanged(qreal visualMax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlogvalueaxis.html#visualMaxChanged

    Parameters
    ----------

    visualMax : float
      Passed on as it is.
    """
    #  void QLogValueAxis::visualMaxChanged(qreal visualMax)
    self.uglySide.call(
        'ritual_ZN13QLogValueAxis16visualMaxChangedEd', visualMax,
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
