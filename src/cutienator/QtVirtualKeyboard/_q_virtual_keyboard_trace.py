"""
QVirtualKeyboardTrace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboardtrace.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QTimerEvent, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QTimerEvent = WAIT['QTimerEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardTrace(QObject):
  """
  The cute side of Qt's QVirtualKeyboardTrace: a plain Python object standing
  in front of one C++ QVirtualKeyboardTrace.

  It is built on the cute 'QObject', as Qt's QVirtualKeyboardTrace is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardTrace that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'traceId',
  'setTraceId', 'channels', 'setChannels', 'length', 'points', 'addPoint',
  'setChannelData', 'channelData', 'isFinal', 'setFinal', 'isCanceled',
  'setCanceled', 'opacity', 'setOpacity', 'startHideTimer', 'timerEvent',
  'traceIdChanged', 'channelsChanged', 'lengthChanged', 'finalChanged',
  'canceledChanged', 'opacityChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardTrace::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QVirtualKeyboardTrace::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QVirtualKeyboardTracePrivate *QVirtualKeyboardTrace::d_func()':
    gives 'QVirtualKeyboardTracePrivate', which has no cute class yet.
  - Qt's 'const QVirtualKeyboardTracePrivate *QVirtualKeyboardTrace::d_func()
    const': gives 'QVirtualKeyboardTracePrivate', which has no cute class
    yet.
  - Qt's 'void QVirtualKeyboardTrace::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QVirtualKeyboardTrace::~QVirtualKeyboardTrace()': the destructor:
    Python never removes a C++ QVirtualKeyboardTrace.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVirtualKeyboardTrace is created at the first use, not by
    'QVirtualKeyboardTrace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardTrace.
  - Qt tells when it has removed the C++ QVirtualKeyboardTrace. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QVirtualKeyboardTrace::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#tr

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
    #  QString QVirtualKeyboardTrace::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QVirtualKeyboardTrace2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardTrace'

  #  A C++ QVirtualKeyboardTrace Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardTrace'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVirtualKeyboardTrace::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardTrace::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QVirtualKeyboardTrace10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def traceId(self) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardTrace::traceId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#traceId
    """
    #  int QVirtualKeyboardTrace::traceId() const
    return self.uglySide.call('ritual_ZNK21QVirtualKeyboardTrace7traceIdEv')

  def channels(self) -> QStringList:
    """
    Calls Qt's 'QStringList QVirtualKeyboardTrace::channels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#channels

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVirtualKeyboardTrace::channels() const
    address = self.uglySide.call(
        'ritual_ZNK21QVirtualKeyboardTrace8channelsEv',
    )
    return QStringList._cuteOwning(address)

  def length(self) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardTrace::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#length
    """
    #  int QVirtualKeyboardTrace::length() const
    return self.uglySide.call('ritual_ZNK21QVirtualKeyboardTrace6lengthEv')

  @overload()
  @overload(int)
  @overload(int, int)
  def points(self, pos: int = 0, count: int = -1) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QVirtualKeyboardTrace::points(int pos, int
    count) const'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#points

    Parameters
    ----------

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QVirtualKeyboardTrace::points(int pos, int count) const
    address = self.uglySide.call(
        'ritual_ZNK21QVirtualKeyboardTrace6pointsEii', pos, count,
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  def channelData(
      self,
      channel: str,
      pos: int = 0,
      count: int = -1,
  ) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QVirtualKeyboardTrace::channelData(const QString
    &channel, int pos, int count) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#channelData

    Parameters
    ----------

    channel : str
      Passed on as it is: a QString is made of it for the call.

    pos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QVirtualKeyboardTrace::channelData(const QString
    #      &channel, int pos, int count) const
    address = self.uglySide.call(
        'ritual_ZNK21QVirtualKeyboardTrace11channelDataERK7QStringii',
        channel, pos, count,
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardTrace::isFinal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#isFinal
    """
    #  bool QVirtualKeyboardTrace::isFinal() const
    return self.uglySide.call('ritual_ZNK21QVirtualKeyboardTrace7isFinalEv')

  def isCanceled(self) -> bool:
    """
    Calls Qt's 'bool QVirtualKeyboardTrace::isCanceled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#isCanceled
    """
    #  bool QVirtualKeyboardTrace::isCanceled() const
    return self.uglySide.call(
        'ritual_ZNK21QVirtualKeyboardTrace10isCanceledEv',
    )

  def opacity(self) -> float:
    """
    Calls Qt's 'qreal QVirtualKeyboardTrace::opacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#opacity
    """
    #  qreal QVirtualKeyboardTrace::opacity() const
    return self.uglySide.call('ritual_ZNK21QVirtualKeyboardTrace7opacityEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTraceId(self, id: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::setTraceId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#setTraceId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::setTraceId(int id)
    self.uglySide.call('ritual_ZN21QVirtualKeyboardTrace10setTraceIdEi', id)

  @overload(QStringList)
  def setChannels(self, channels: QStringList) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::setChannels(const QStringList
    &channels)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#setChannels

    Parameters
    ----------

    channels : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVirtualKeyboardTrace::setChannels(const QStringList &channels)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace11setChannelsERK5QListI7QStringE',
        self._valueOf(channels),
    )

  @overload(str, int, QVariant)
  def setChannelData(self, channel: str, index: int, data: QVariant) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::setChannelData(const QString
    &channel, int index, const QVariant &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#setChannelData

    Parameters
    ----------

    channel : str
      Passed on as it is: a QString is made of it for the call.

    index : int
      Passed on as it is.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QVirtualKeyboardTrace::setChannelData(const QString &channel, int
    #      index, const QVariant &data)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace14setChannelDataERK7QStringiRK8QVa'
        'riant',
        channel, index, self._valueOf(data),
    )

  @overload(bool)
  def setFinal(self, final: bool) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::setFinal(bool final)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#setFinal

    Parameters
    ----------

    final : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::setFinal(bool final)
    self.uglySide.call('ritual_ZN21QVirtualKeyboardTrace8setFinalEb', final)

  @overload(bool)
  def setCanceled(self, canceled: bool) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::setCanceled(bool canceled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#setCanceled

    Parameters
    ----------

    canceled : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::setCanceled(bool canceled)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace11setCanceledEb', canceled,
    )

  @overload(float)
  def setOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::setOpacity(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#setOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::setOpacity(qreal opacity)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace10setOpacityEd', opacity,
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
    Notes what was given, for Qt's
    'QVirtualKeyboardTrace::QVirtualKeyboardTrace(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#QVirtualKeyboardTrace

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVirtualKeyboardTrace::QVirtualKeyboardTrace(QObject *parent)
    self._noteCreation(QVirtualKeyboardTrace, lambda: Rituals.call(
        'ritual_ZN21QVirtualKeyboardTraceC1EP7QObject',
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

  @overload(QPointF)
  def addPoint(self, point: QPointF) -> int:
    """
    Calls Qt's 'int QVirtualKeyboardTrace::addPoint(const QPointF &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#addPoint

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  int QVirtualKeyboardTrace::addPoint(const QPointF &point)
    return self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace8addPointERK7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(int)
  def startHideTimer(self, delayMs: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::startHideTimer(int delayMs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#startHideTimer

    Parameters
    ----------

    delayMs : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::startHideTimer(int delayMs)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace14startHideTimerEi', delayMs,
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::timerEvent(QTimerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVirtualKeyboardTrace::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN21QVirtualKeyboardTrace10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QVirtualKeyboardTrace10timerEventEP11QTimerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(int)
  def traceIdChanged(self, traceId: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::traceIdChanged(int traceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#traceIdChanged

    Parameters
    ----------

    traceId : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::traceIdChanged(int traceId)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace14traceIdChangedEi', traceId,
    )

  def channelsChanged(self) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::channelsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#channelsChanged
    """
    #  void QVirtualKeyboardTrace::channelsChanged()
    self.uglySide.call('ritual_ZN21QVirtualKeyboardTrace15channelsChangedEv')

  @overload(int)
  def lengthChanged(self, length: int) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::lengthChanged(int length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#lengthChanged

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::lengthChanged(int length)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace13lengthChangedEi', length,
    )

  @overload(bool)
  def finalChanged(self, isFinal: bool) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::finalChanged(bool isFinal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#finalChanged

    Parameters
    ----------

    isFinal : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::finalChanged(bool isFinal)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace12finalChangedEb', isFinal,
    )

  @overload(bool)
  def canceledChanged(self, isCanceled: bool) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::canceledChanged(bool
    isCanceled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#canceledChanged

    Parameters
    ----------

    isCanceled : bool
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::canceledChanged(bool isCanceled)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace15canceledChangedEb', isCanceled,
    )

  @overload(float)
  def opacityChanged(self, opacity: float) -> None:
    """
    Calls Qt's 'void QVirtualKeyboardTrace::opacityChanged(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboardtrace.html#opacityChanged

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QVirtualKeyboardTrace::opacityChanged(qreal opacity)
    self.uglySide.call(
        'ritual_ZN21QVirtualKeyboardTrace14opacityChangedEd', opacity,
    )


#  Qt's 'QList<QVirtualKeyboardTrace *>': the list of QVirtualKeyboardTrace,
#  which 'QList[QVirtualKeyboardTrace]' gives. It is made here, so that there
#  is one as soon as there can be a QVirtualKeyboardTrace.
QList.createKind(
    QVirtualKeyboardTrace, 'address',
    make='ritual_list_make_QVirtualKeyboardTrace_ptr',
    add='ritual_list_add_QVirtualKeyboardTrace_ptr',
    size='ritual_list_size_QVirtualKeyboardTrace_ptr',
    at='ritual_list_at_QVirtualKeyboardTrace_ptr',
    drop='ritual_list_drop_QVirtualKeyboardTrace_ptr',
)
