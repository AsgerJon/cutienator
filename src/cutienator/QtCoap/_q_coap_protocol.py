"""
QCoapProtocol binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapprotocol_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapProtocol to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QtCoap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtNetwork import QHostAddress
  from . import QCoapMessage, QCoapProtocolPrivate, QCoapReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCoapMessage = WAIT['QCoapMessage']
  QCoapReply = WAIT['QCoapReply']
  QHostAddress = WAIT['QHostAddress']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapProtocol(QObject):
  """
  The cute side of Qt's QCoapProtocol: a plain Python object standing in
  front of one C++ QCoapProtocol.

  It is built on the cute 'QObject', as Qt's QCoapProtocol is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapProtocol that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'ackTimeout',
  'ackRandomFactor', 'maximumRetransmitCount', 'blockSize',
  'maximumTransmitSpan', 'maximumTransmitWait', 'maximumLatency',
  'minimumTimeout', 'maximumTimeout', 'nonConfirmLifetime',
  'maximumServerResponseDelay', 'finished', 'responseToMulticastReceived',
  'error', 'setAckTimeout', 'setAckRandomFactor',
  'setMaximumRetransmitCount', 'setBlockSize',
  'setMaximumServerResponseDelay', 'setMinimumTokenSize', 'd_func'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapProtocol::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCoapProtocol::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCoapProtocol::~QCoapProtocol()': the destructor: Python never
    removes a C++ QCoapProtocol.
  - Qt's 'void QCoapProtocol::sendRequest(QPointer<QCoapReply> reply,
    QCoapConnection *connection)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QCoapProtocolPrivate *QCoapProtocol::d_func() const': takes
    in Python what 'QCoapProtocolPrivate *QCoapProtocol::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 33 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here; 2 leans on 'QCoapProtocol.

  What to expect
  --------------

  - The C++ QCoapProtocol is created at the first use, not by
    'QCoapProtocol(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapProtocol.
  - Qt tells when it has removed the C++ QCoapProtocol. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoapProtocol that has no cute function yet,
    '__init__', 'cancelObserve', 'sendRequest', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapProtocol'

  #  A C++ QCoapProtocol Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapProtocol'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapProtocol::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapProtocol::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QCoapProtocol10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ackTimeout(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::ackTimeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#ackTimeout
    """
    #  uint QCoapProtocol::ackTimeout() const
    return self.uglySide.call('ritual_ZNK13QCoapProtocol10ackTimeoutEv')

  def ackRandomFactor(self) -> float:
    """
    Calls Qt's 'double QCoapProtocol::ackRandomFactor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#ackRandomFactor
    """
    #  double QCoapProtocol::ackRandomFactor() const
    return self.uglySide.call('ritual_ZNK13QCoapProtocol15ackRandomFactorEv')

  def maximumRetransmitCount(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::maximumRetransmitCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#maximumRetransmitCount
    """
    #  uint QCoapProtocol::maximumRetransmitCount() const
    return self.uglySide.call(
        'ritual_ZNK13QCoapProtocol22maximumRetransmitCountEv',
    )

  def blockSize(self) -> int:
    """
    Calls Qt's 'quint16 QCoapProtocol::blockSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#blockSize
    """
    #  quint16 QCoapProtocol::blockSize() const
    return self.uglySide.call('ritual_ZNK13QCoapProtocol9blockSizeEv')

  def maximumTransmitSpan(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::maximumTransmitSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#maximumTransmitSpan
    """
    #  uint QCoapProtocol::maximumTransmitSpan() const
    return self.uglySide.call(
        'ritual_ZNK13QCoapProtocol19maximumTransmitSpanEv',
    )

  def maximumTransmitWait(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::maximumTransmitWait() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#maximumTransmitWait
    """
    #  uint QCoapProtocol::maximumTransmitWait() const
    return self.uglySide.call(
        'ritual_ZNK13QCoapProtocol19maximumTransmitWaitEv',
    )

  def maximumLatency(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::maximumLatency() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#maximumLatency
    """
    #  uint QCoapProtocol::maximumLatency() const
    return self.uglySide.call('ritual_ZNK13QCoapProtocol14maximumLatencyEv')

  def minimumTimeout(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::minimumTimeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#minimumTimeout
    """
    #  uint QCoapProtocol::minimumTimeout() const
    return self.uglySide.call('ritual_ZNK13QCoapProtocol14minimumTimeoutEv')

  def maximumTimeout(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::maximumTimeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#maximumTimeout
    """
    #  uint QCoapProtocol::maximumTimeout() const
    return self.uglySide.call('ritual_ZNK13QCoapProtocol14maximumTimeoutEv')

  def nonConfirmLifetime(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::nonConfirmLifetime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#nonConfirmLifetime
    """
    #  uint QCoapProtocol::nonConfirmLifetime() const
    return self.uglySide.call(
        'ritual_ZNK13QCoapProtocol18nonConfirmLifetimeEv',
    )

  def maximumServerResponseDelay(self) -> int:
    """
    Calls Qt's 'uint QCoapProtocol::maximumServerResponseDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#maximumServerResponseDelay
    """
    #  uint QCoapProtocol::maximumServerResponseDelay() const
    return self.uglySide.call(
        'ritual_ZNK13QCoapProtocol26maximumServerResponseDelayEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAckTimeout(self, ackTimeout: int) -> None:
    """
    Calls Qt's 'void QCoapProtocol::setAckTimeout(uint ackTimeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#setAckTimeout

    Parameters
    ----------

    ackTimeout : int
      Passed on as it is.
    """
    #  void QCoapProtocol::setAckTimeout(uint ackTimeout)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol13setAckTimeoutEj', ackTimeout,
    )

  @overload(float)
  def setAckRandomFactor(self, ackRandomFactor: float) -> None:
    """
    Calls Qt's 'void QCoapProtocol::setAckRandomFactor(double
    ackRandomFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#setAckRandomFactor

    Parameters
    ----------

    ackRandomFactor : float
      Passed on as it is.
    """
    #  void QCoapProtocol::setAckRandomFactor(double ackRandomFactor)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol18setAckRandomFactorEd', ackRandomFactor,
    )

  @overload(int)
  def setMaximumRetransmitCount(self, maximumRetransmitCount: int) -> None:
    """
    Calls Qt's 'void QCoapProtocol::setMaximumRetransmitCount(uint
    maximumRetransmitCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#setMaximumRetransmitCount

    Parameters
    ----------

    maximumRetransmitCount : int
      Passed on as it is.
    """
    #  void QCoapProtocol::setMaximumRetransmitCount(uint
    #      maximumRetransmitCount)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol25setMaximumRetransmitCountEj',
        maximumRetransmitCount,
    )

  @overload(int)
  def setBlockSize(self, blockSize: int) -> None:
    """
    Calls Qt's 'void QCoapProtocol::setBlockSize(quint16 blockSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#setBlockSize

    Parameters
    ----------

    blockSize : int
      Passed on as it is.
    """
    #  void QCoapProtocol::setBlockSize(quint16 blockSize)
    self.uglySide.call('ritual_ZN13QCoapProtocol12setBlockSizeEt', blockSize)

  @overload(int)
  def setMaximumServerResponseDelay(self, responseDelay: int) -> None:
    """
    Calls Qt's 'void QCoapProtocol::setMaximumServerResponseDelay(uint
    responseDelay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#setMaximumServerResponseDelay

    Parameters
    ----------

    responseDelay : int
      Passed on as it is.
    """
    #  void QCoapProtocol::setMaximumServerResponseDelay(uint responseDelay)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol29setMaximumServerResponseDelayEj',
        responseDelay,
    )

  @overload(int)
  def setMinimumTokenSize(self, tokenSize: int) -> None:
    """
    Calls Qt's 'void QCoapProtocol::setMinimumTokenSize(int tokenSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#setMinimumTokenSize

    Parameters
    ----------

    tokenSize : int
      Passed on as it is.
    """
    #  void QCoapProtocol::setMinimumTokenSize(int tokenSize)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol19setMinimumTokenSizeEi', tokenSize,
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
    Qt's 'QCoapProtocol::QCoapProtocol(QObject *parent)': leans on
    'QCoapProtocol::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCoapProtocol.__init__' has no cute function yet. Qt's "
        "'QCoapProtocol::QCoapProtocol(QObject *parent)': leans on "
        "'QCoapProtocol::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QCoapReply)
  @overload(NoneType)
  def finished(self, reply: Optional[QCoapReply]) -> None:
    """
    Calls Qt's 'void QCoapProtocol::finished(QCoapReply *reply)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#finished

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapProtocol::finished(QCoapReply *reply)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol8finishedEP10QCoapReply',
        self._addressOf(reply),
    )

  @overload(QCoapReply, QCoapMessage, QHostAddress)
  @overload(NoneType, QCoapMessage, QHostAddress)
  def responseToMulticastReceived(
      self,
      reply: Optional[QCoapReply],
      message: QCoapMessage,
      sender: QHostAddress,
  ) -> None:
    """
    Calls Qt's 'void QCoapProtocol::responseToMulticastReceived(QCoapReply
    *reply, const QCoapMessage &message, const QHostAddress &sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapprotocol.html#responseToMulticastReceived

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    message : QCoapMessage
      Passed on as a value: Qt reads the C++ QCoapMessage, which stays
      Python's own.

    sender : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QCoapProtocol::responseToMulticastReceived(QCoapReply *reply,
    #      const QCoapMessage &message, const QHostAddress &sender)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol27responseToMulticastReceivedEP10QCoapRepl'
        'yRK12QCoapMessageRK12QHostAddress',
        self._addressOf(reply), self._valueOf(message),
        self._valueOf(sender),
    )

  @overload(QCoapReply, QtCoap.Error)
  @overload(NoneType, QtCoap.Error)
  def error(self, reply: Optional[QCoapReply], error: QtCoap.Error) -> None:
    """
    Calls Qt's 'void QCoapProtocol::error(QCoapReply *reply, QtCoap::Error
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#error

    Parameters
    ----------

    reply : Optional[QCoapReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    error : QtCoap.Error
      Passed on as its number.
    """
    #  void QCoapProtocol::error(QCoapReply *reply, QtCoap::Error error)
    self.uglySide.call(
        'ritual_ZN13QCoapProtocol5errorEP10QCoapReplyN6QtCoap5ErrorE',
        self._addressOf(reply), error.value,
    )

  def d_func(self) -> Optional[QCoapProtocolPrivate]:
    """
    Calls Qt's 'QCoapProtocolPrivate *QCoapProtocol::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapprotocol.html#d_func

    Returns
    -------

    Optional[QCoapProtocolPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapProtocolPrivate *QCoapProtocol::d_func()
    address = self.uglySide.call('ritual_ZN13QCoapProtocol6d_funcEv')
    from . import QCoapProtocolPrivate
    return QCoapProtocolPrivate._cuteAt(address)

  @staticmethod
  def cancelObserve(*__, **_) -> Never:
    """
    - Qt's 'void QCoapProtocol::cancelObserve(QPointer<QCoapReply> reply)
      const': the compiler refuses its ritual as it would be written here:
      static_cast from 'const QCoapProtocol *' to 'QObject *', which are not
      related by inheritance, is not allowed.
    - Qt's 'void QCoapProtocol::cancelObserve(const QUrl &url) const': the
      compiler refuses its ritual as it would be written here: static_cast
      from 'const QCoapProtocol *' to 'QObject *', which are not related by
      inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QCoapProtocol.cancelObserve' has no cute function yet. Qt's 'void "
        "QCoapProtocol::cancelObserve(QPointer<QCoapReply> reply) const': "
        "the compiler refuses its ritual as it would be written here: "
        "static_cast from 'const QCoapProtocol *' to 'QObject *', which are "
        "not related by inheritance, is not allowed. Qt's 'void "
        "QCoapProtocol::cancelObserve(const QUrl &url) const': the compiler "
        "refuses its ritual as it would be written here: static_cast from "
        "'const QCoapProtocol *' to 'QObject *', which are not related by "
        "inheritance, is not allowed.")

  @staticmethod
  def sendRequest(*__, **_) -> Never:
    """
    Qt's 'void QCoapProtocol::sendRequest(QPointer<QCoapReply> reply,
    QCoapConnection *connection)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QCoapProtocol.sendRequest' has no cute function yet. Qt's 'void "
        "QCoapProtocol::sendRequest(QPointer<QCoapReply> reply, "
        "QCoapConnection *connection)': takes a type Python has no way to "
        "hand over yet.")
