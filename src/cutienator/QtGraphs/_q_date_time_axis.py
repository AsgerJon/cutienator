"""
QDateTimeAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qdatetimeaxis.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QMetaObject, QTimeZone
  from . import QDateTimeAxisPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QTimeZone = WAIT['QTimeZone']

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
  call so far, 37 names in all: 'metaObject', 'tr', 'type', 'setMin', 'min',
  'setMax', 'max', 'setLabelFormat', 'labelFormat', 'tickInterval',
  'setTickInterval', 'subTickCount', 'setSubTickCount', 'timeZone',
  'setTimeZone', 'setZoom', 'zoom', 'pan', 'setPan', 'visualMin',
  'visualMax', 'timeZoneFromString', 'timeZoneAsString', 'tickCount',
  'setTickCount', 'minChanged', 'maxChanged', 'labelFormatChanged',
  'tickIntervalChanged', 'subTickCountChanged', 'timeZoneChanged',
  'zoomChanged', 'panChanged', 'visualMinChanged', 'visualMaxChanged',
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

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

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
  __qt_part__ = 'QtGraphs'

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

  def labelFormat(self) -> str:
    """
    Calls Qt's 'QString QDateTimeAxis::labelFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#labelFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeAxis::labelFormat() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis11labelFormatEv')

  def tickInterval(self) -> float:
    """
    Calls Qt's 'qreal QDateTimeAxis::tickInterval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#tickInterval
    """
    #  qreal QDateTimeAxis::tickInterval() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis12tickIntervalEv')

  def subTickCount(self) -> int:
    """
    Calls Qt's 'int QDateTimeAxis::subTickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#subTickCount
    """
    #  int QDateTimeAxis::subTickCount() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis12subTickCountEv')

  def timeZone(self) -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QDateTimeAxis::timeZone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#timeZone

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QDateTimeAxis::timeZone() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeAxis8timeZoneEv')
    from ..QtCore import QTimeZone
    return QTimeZone._cuteOwning(address)

  def zoom(self) -> float:
    """
    Calls Qt's 'qreal QDateTimeAxis::zoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#zoom
    """
    #  qreal QDateTimeAxis::zoom() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis4zoomEv')

  def pan(self) -> float:
    """
    Calls Qt's 'qreal QDateTimeAxis::pan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#pan
    """
    #  qreal QDateTimeAxis::pan() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis3panEv')

  def visualMin(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeAxis::visualMin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#visualMin

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeAxis::visualMin() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeAxis9visualMinEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def visualMax(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeAxis::visualMax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#visualMax

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeAxis::visualMax() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeAxis9visualMaxEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(str)
  def timeZoneFromString(self, zoneId: str) -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QDateTimeAxis::timeZoneFromString(const QString
    &zoneId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#timeZoneFromString

    Parameters
    ----------

    zoneId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QDateTimeAxis::timeZoneFromString(const QString &zoneId)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QDateTimeAxis18timeZoneFromStringERK7QString', zoneId,
    )
    from ..QtCore import QTimeZone
    return QTimeZone._cuteOwning(address)

  def timeZoneAsString(self) -> str:
    """
    Calls Qt's 'QString QDateTimeAxis::timeZoneAsString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#timeZoneAsString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeAxis::timeZoneAsString() const
    return self.uglySide.call(
        'ritual_ZNK13QDateTimeAxis16timeZoneAsStringEv',
    )

  def tickCount(self) -> int:
    """
    Calls Qt's 'qsizetype QDateTimeAxis::tickCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#tickCount
    """
    #  qsizetype QDateTimeAxis::tickCount() const
    return self.uglySide.call('ritual_ZNK13QDateTimeAxis9tickCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setMin(self, min: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setMin(const QDateTime &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setMin

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::setMin(const QDateTime &min)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis6setMinERK9QDateTime', self._valueOf(min),
    )

  @overload(QDateTime)
  def setMax(self, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setMax(const QDateTime &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setMax

    Parameters
    ----------

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::setMax(const QDateTime &max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis6setMaxERK9QDateTime', self._valueOf(max),
    )

  @overload(str)
  def setLabelFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setLabelFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setLabelFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDateTimeAxis::setLabelFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis14setLabelFormatERK7QString', format,
    )

  @overload(float)
  def setTickInterval(self, newTickInterval: float) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setTickInterval(qreal newTickInterval)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setTickInterval

    Parameters
    ----------

    newTickInterval : float
      Passed on as it is.
    """
    #  void QDateTimeAxis::setTickInterval(qreal newTickInterval)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis15setTickIntervalEd', newTickInterval,
    )

  @overload(int)
  def setSubTickCount(self, newSubTickCount: int) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setSubTickCount(int newSubTickCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setSubTickCount

    Parameters
    ----------

    newSubTickCount : int
      Passed on as it is.
    """
    #  void QDateTimeAxis::setSubTickCount(int newSubTickCount)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis15setSubTickCountEi', newSubTickCount,
    )

  @overload(QTimeZone)
  def setTimeZone(self, zoneId: QTimeZone) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setTimeZone(const QTimeZone &zoneId)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setTimeZone

    Parameters
    ----------

    zoneId : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.
    """
    #  void QDateTimeAxis::setTimeZone(const QTimeZone &zoneId)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis11setTimeZoneERK9QTimeZone',
        self._valueOf(zoneId),
    )

  @overload(float)
  def setZoom(self, zoom: float) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setZoom(qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setZoom

    Parameters
    ----------

    zoom : float
      Passed on as it is.
    """
    #  void QDateTimeAxis::setZoom(qreal zoom)
    self.uglySide.call('ritual_ZN13QDateTimeAxis7setZoomEd', zoom)

  @overload(float)
  def setPan(self, pan: float) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setPan(qreal pan)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setPan

    Parameters
    ----------

    pan : float
      Passed on as it is.
    """
    #  void QDateTimeAxis::setPan(qreal pan)
    self.uglySide.call('ritual_ZN13QDateTimeAxis6setPanEd', pan)

  @overload(int)
  def setTickCount(self, count: int) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::setTickCount(qsizetype count)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#setTickCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QDateTimeAxis::setTickCount(qsizetype count)
    self.uglySide.call('ritual_ZN13QDateTimeAxis12setTickCountEx', count)

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
    Calls Qt's 'void QDateTimeAxis::minChanged(const QDateTime &min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#minChanged

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::minChanged(const QDateTime &min)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis10minChangedERK9QDateTime',
        self._valueOf(min),
    )

  @overload(QDateTime)
  def maxChanged(self, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::maxChanged(const QDateTime &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#maxChanged

    Parameters
    ----------

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::maxChanged(const QDateTime &max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis10maxChangedERK9QDateTime',
        self._valueOf(max),
    )

  @overload(str)
  def labelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::labelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#labelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDateTimeAxis::labelFormatChanged(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis18labelFormatChangedERK7QString', format,
    )

  def tickIntervalChanged(self) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::tickIntervalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#tickIntervalChanged
    """
    #  void QDateTimeAxis::tickIntervalChanged()
    self.uglySide.call('ritual_ZN13QDateTimeAxis19tickIntervalChangedEv')

  def subTickCountChanged(self) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::subTickCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#subTickCountChanged
    """
    #  void QDateTimeAxis::subTickCountChanged()
    self.uglySide.call('ritual_ZN13QDateTimeAxis19subTickCountChangedEv')

  @overload(QTimeZone)
  def timeZoneChanged(self, newTimeZone: QTimeZone) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::timeZoneChanged(const QTimeZone
    &newTimeZone)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#timeZoneChanged

    Parameters
    ----------

    newTimeZone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.
    """
    #  void QDateTimeAxis::timeZoneChanged(const QTimeZone &newTimeZone)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis15timeZoneChangedERK9QTimeZone',
        self._valueOf(newTimeZone),
    )

  @overload(float)
  def zoomChanged(self, newZoom: float) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::zoomChanged(qreal newZoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#zoomChanged

    Parameters
    ----------

    newZoom : float
      Passed on as it is.
    """
    #  void QDateTimeAxis::zoomChanged(qreal newZoom)
    self.uglySide.call('ritual_ZN13QDateTimeAxis11zoomChangedEd', newZoom)

  @overload(float)
  def panChanged(self, newPan: float) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::panChanged(qreal newPan)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeaxis.html#panChanged

    Parameters
    ----------

    newPan : float
      Passed on as it is.
    """
    #  void QDateTimeAxis::panChanged(qreal newPan)
    self.uglySide.call('ritual_ZN13QDateTimeAxis10panChangedEd', newPan)

  @overload(QDateTime)
  def visualMinChanged(self, newMin: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::visualMinChanged(const QDateTime
    &newMin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#visualMinChanged

    Parameters
    ----------

    newMin : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::visualMinChanged(const QDateTime &newMin)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis16visualMinChangedERK9QDateTime',
        self._valueOf(newMin),
    )

  @overload(QDateTime)
  def visualMaxChanged(self, newMax: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::visualMaxChanged(const QDateTime
    &newMax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#visualMaxChanged

    Parameters
    ----------

    newMax : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeAxis::visualMaxChanged(const QDateTime &newMax)
    self.uglySide.call(
        'ritual_ZN13QDateTimeAxis16visualMaxChangedERK9QDateTime',
        self._valueOf(newMax),
    )

  @overload(int)
  def tickCountChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QDateTimeAxis::tickCountChanged(qsizetype count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeaxis.html#tickCountChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QDateTimeAxis::tickCountChanged(qsizetype count)
    self.uglySide.call('ritual_ZN13QDateTimeAxis16tickCountChangedEx', count)

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
