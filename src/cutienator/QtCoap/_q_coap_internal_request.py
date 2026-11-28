"""
QCoapInternalRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapinternalrequest_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCoapInternalRequest to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from . import QtCoap, QCoapInternalMessage, QCoapMessage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from . import QCoapConnection, QCoapInternalRequestPrivate, QCoapOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapConnection = WAIT['QCoapConnection']
  QCoapOption = WAIT['QCoapOption']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapInternalRequest(QCoapInternalMessage):
  """
  The cute side of Qt's QCoapInternalRequest: a plain Python object standing
  in front of one C++ QCoapInternalRequest.

  It is built on the cute 'QCoapInternalMessage', as Qt's
  QCoapInternalRequest is built on Qt's QCoapInternalMessage, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapInternalRequest that has a ritual and that
  Python can call so far, 32 names in all: 'metaObject', 'isValid',
  'initEmptyMessage', 'setMessageId', 'setToken', 'setToRequestBlock',
  'setToSendBlock', 'checkBlockNumber', 'addOption', 'token', 'targetUri',
  'method', 'isObserve', 'isObserveCancelled', 'isMulticast', 'connection',
  'retransmissionCounter', 'setMethod', 'setConnection',
  'setObserveCancelled', 'setTargetUri', 'setTimeout',
  'setMaxTransmissionWait', 'setMulticastTimeout', 'restartTransmission',
  'startMulticastTransmission', 'stopTransmission', 'timeout',
  'maxTransmissionSpanReached', 'multicastRequestExpired', 'uriHostOption',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapInternalRequest::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCoapInternalRequest::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QCoapInternalRequestPrivate *QCoapInternalRequest::d_func()
    const': takes in Python what 'QCoapInternalRequestPrivate
    *QCoapInternalRequest::d_func()' takes.

  What has no ritual
  ------------------

  8 of the 43 functions Qt declares: 3 leans on 'QCoapInternalMessage; 2 not
  a gap; 2 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file; 1 leans on 'QCoapInternalRequest.

  What to expect
  --------------

  - The C++ QCoapInternalRequest is created at the first use, not by
    'QCoapInternalRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapInternalRequest.
  - Qt tells when it has removed the C++ QCoapInternalRequest. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoapInternalRequest that has no cute function yet,
    '__init__', 'addUriOptions', 'blockOption', 'toQByteArray', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapInternalRequest'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapInternalRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapInternalRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalRequest::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalrequest.html#isValid
    """
    #  bool QCoapInternalRequest::isValid() const
    ritual = 'ritual_ZNK20QCoapInternalRequest7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QCoapInternalRequest7isValidEv'
    return self.uglySide.call(ritual)

  def token(self) -> QByteArray:
    """
    Calls Qt's 'QCoapToken QCoapInternalRequest::token() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalrequest.html#token

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QCoapToken QCoapInternalRequest::token() const
    address = self.uglySide.call('ritual_ZNK20QCoapInternalRequest5tokenEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def targetUri(self) -> QUrl:
    """
    Calls Qt's 'QUrl QCoapInternalRequest::targetUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#targetUri

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QCoapInternalRequest::targetUri() const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest9targetUriEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def method(self) -> QtCoap.Method:
    """
    Calls Qt's 'QtCoap::Method QCoapInternalRequest::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalrequest.html#method

    Returns
    -------

    QtCoap.Method
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtCoap.Method(number)'
      gives.
    """
    #  QtCoap::Method QCoapInternalRequest::method() const
    return QtCoap.Method(self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest6methodEv',
    ))

  def isObserve(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalRequest::isObserve() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#isObserve
    """
    #  bool QCoapInternalRequest::isObserve() const
    return self.uglySide.call('ritual_ZNK20QCoapInternalRequest9isObserveEv')

  def isObserveCancelled(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalRequest::isObserveCancelled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#isObserveCancelled
    """
    #  bool QCoapInternalRequest::isObserveCancelled() const
    return self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest18isObserveCancelledEv',
    )

  def isMulticast(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalRequest::isMulticast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#isMulticast
    """
    #  bool QCoapInternalRequest::isMulticast() const
    return self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest11isMulticastEv',
    )

  def connection(self) -> Optional[QCoapConnection]:
    """
    Calls Qt's 'QCoapConnection *QCoapInternalRequest::connection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#connection

    Returns
    -------

    Optional[QCoapConnection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapConnection *QCoapInternalRequest::connection() const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest10connectionEv',
    )
    from . import QCoapConnection
    return QCoapConnection._cuteAt(address)

  def retransmissionCounter(self) -> int:
    """
    Calls Qt's 'uint QCoapInternalRequest::retransmissionCounter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#retransmissionCounter
    """
    #  uint QCoapInternalRequest::retransmissionCounter() const
    return self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest21retransmissionCounterEv',
    )

  @overload(QUrl)
  def uriHostOption(self, uri: QUrl) -> QCoapOption:
    """
    Calls Qt's 'QCoapOption QCoapInternalRequest::uriHostOption(const QUrl
    &uri) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#uriHostOption

    Parameters
    ----------

    uri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QCoapOption
      A new cute QCoapOption around the copy Qt gave back. Python owns it.
    """
    #  QCoapOption QCoapInternalRequest::uriHostOption(const QUrl &uri) const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapInternalRequest13uriHostOptionERK4QUrl',
        self._valueOf(uri),
    )
    from . import QCoapOption
    return QCoapOption._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMessageId(self, a0: int) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setMessageId(quint16 a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setMessageId

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCoapInternalRequest::setMessageId(quint16 a0)
    self.uglySide.call('ritual_ZN20QCoapInternalRequest12setMessageIdEt', a0)

  @overload(QByteArray)
  def setToken(self, a0: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setToken(const QCoapToken &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalrequest.html#setToken

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapInternalRequest::setToken(const QCoapToken &a0)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest8setTokenERK10QByteArray',
        self._valueOf(a0),
    )

  @overload(int, int)
  def setToRequestBlock(self, blockNumber: int, blockSize: int) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setToRequestBlock(uint
    blockNumber, uint blockSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setToRequestBlock

    Parameters
    ----------

    blockNumber : int
      Passed on as it is.

    blockSize : int
      Passed on as it is.
    """
    #  void QCoapInternalRequest::setToRequestBlock(uint blockNumber, uint
    #      blockSize)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest17setToRequestBlockEjj',
        blockNumber, blockSize,
    )

  @overload(int, int)
  def setToSendBlock(self, blockNumber: int, blockSize: int) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setToSendBlock(uint blockNumber,
    uint blockSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setToSendBlock

    Parameters
    ----------

    blockNumber : int
      Passed on as it is.

    blockSize : int
      Passed on as it is.
    """
    #  void QCoapInternalRequest::setToSendBlock(uint blockNumber, uint
    #      blockSize)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest14setToSendBlockEjj',
        blockNumber, blockSize,
    )

  @overload(QtCoap.Method)
  def setMethod(self, method: QtCoap.Method) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setMethod(QtCoap::Method method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setMethod

    Parameters
    ----------

    method : QtCoap.Method
      Passed on as its number.
    """
    #  void QCoapInternalRequest::setMethod(QtCoap::Method method)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest9setMethodEN6QtCoap6MethodE',
        method.value,
    )

  @overload(QCoapConnection)
  @overload(NoneType)
  def setConnection(self, connection: Optional[QCoapConnection]) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setConnection(QCoapConnection
    *connection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setConnection

    Parameters
    ----------

    connection : Optional[QCoapConnection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapInternalRequest::setConnection(QCoapConnection *connection)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest13setConnectionEP15QCoapConnection',
        self._addressOf(connection),
    )

  def setObserveCancelled(self) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setObserveCancelled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setObserveCancelled
    """
    #  void QCoapInternalRequest::setObserveCancelled()
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest19setObserveCancelledEv',
    )

  @overload(QUrl)
  def setTargetUri(self, targetUri: QUrl) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setTargetUri(QUrl targetUri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setTargetUri

    Parameters
    ----------

    targetUri : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QCoapInternalRequest::setTargetUri(QUrl targetUri)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest12setTargetUriE4QUrl',
        self._valueOf(targetUri),
    )

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setTimeout(uint timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QCoapInternalRequest::setTimeout(uint timeout)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest10setTimeoutEj', timeout,
    )

  @overload(int)
  def setMaxTransmissionWait(self, timeout: int) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setMaxTransmissionWait(uint
    timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setMaxTransmissionWait

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QCoapInternalRequest::setMaxTransmissionWait(uint timeout)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest22setMaxTransmissionWaitEj', timeout,
    )

  @overload(int)
  def setMulticastTimeout(self, responseDelay: int) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::setMulticastTimeout(uint
    responseDelay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#setMulticastTimeout

    Parameters
    ----------

    responseDelay : int
      Passed on as it is.
    """
    #  void QCoapInternalRequest::setMulticastTimeout(uint responseDelay)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest19setMulticastTimeoutEj',
        responseDelay,
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
    - Qt's 'QCoapInternalRequest::QCoapInternalRequest(QObject *parent)':
      leans on 'QCoapInternalMessage::QCoapInternalMessage(
      QCoapInternalMessagePrivate&, QObject*)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    - Qt's 'QCoapInternalRequest::QCoapInternalRequest(const QCoapRequest
      &request, QObject *parent)': leans on
      'QCoapInternalMessage::addOption(QCoapOption::OptionName, unsigned
      int)', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapInternalRequest.__init__' has no cute function yet. Qt's "
        "'QCoapInternalRequest::QCoapInternalRequest(QObject *parent)': "
        "leans on "
        "'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePri"
        "vate&, QObject*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QCoapInternalRequest::QCoapInternalRequest(const QCoapRequest "
        "&request, QObject *parent)': leans on "
        "'QCoapInternalMessage::addOption(QCoapOption::OptionName, unsigned "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

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

  @overload(int, QCoapMessage.Type)
  def initEmptyMessage(
      self,
      messageId: int,
      type: QCoapMessage.Type,
  ) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::initEmptyMessage(quint16
    messageId, QCoapMessage::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#initEmptyMessage

    Parameters
    ----------

    messageId : int
      Passed on as it is.

    type : QCoapMessage.Type
      Passed on as its number.
    """
    #  void QCoapInternalRequest::initEmptyMessage(quint16 messageId,
    #      QCoapMessage::Type type)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest16initEmptyMessageEtN12QCoapMessage'
        '4TypeE',
        messageId, type.value,
    )

  @overload(int)
  def checkBlockNumber(self, blockNumber: int) -> bool:
    """
    Calls Qt's 'bool QCoapInternalRequest::checkBlockNumber(uint
    blockNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#checkBlockNumber

    Parameters
    ----------

    blockNumber : int
      Passed on as it is.
    """
    #  bool QCoapInternalRequest::checkBlockNumber(uint blockNumber)
    return self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest16checkBlockNumberEj', blockNumber,
    )

  @overload(QCoapOption)
  def addOption(self, option: QCoapOption) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::addOption(const QCoapOption
    &option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#addOption

    Parameters
    ----------

    option : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  void QCoapInternalRequest::addOption(const QCoapOption &option)
    ritual = 'ritual_ZN20QCoapInternalRequest9addOptionERK11QCoapOption'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCoapInternalRequest9addOptionERK11QCoapOption')
    self.uglySide.call(ritual, self._valueOf(option))

  def restartTransmission(self) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::restartTransmission()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#restartTransmission
    """
    #  void QCoapInternalRequest::restartTransmission()
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest19restartTransmissionEv',
    )

  def startMulticastTransmission(self) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::startMulticastTransmission()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html
    """
    #  void QCoapInternalRequest::startMulticastTransmission()
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest26startMulticastTransmissionEv',
    )

  def stopTransmission(self) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::stopTransmission()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#stopTransmission
    """
    #  void QCoapInternalRequest::stopTransmission()
    self.uglySide.call('ritual_ZN20QCoapInternalRequest16stopTransmissionEv')

  @overload(THIS)
  @overload(NoneType)
  def timeout(self, a0: Optional[QCoapInternalRequest]) -> None:
    """
    Calls Qt's 'void QCoapInternalRequest::timeout(QCoapInternalRequest
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalrequest.html#timeout

    Parameters
    ----------

    a0 : Optional[QCoapInternalRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapInternalRequest::timeout(QCoapInternalRequest *a0)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest7timeoutEPS_', self._addressOf(a0),
    )

  @overload(THIS)
  @overload(NoneType)
  def maxTransmissionSpanReached(
      self,
      a0: Optional[QCoapInternalRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QCoapInternalRequest::maxTransmissionSpanReached(QCoapInternalRequest
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html

    Parameters
    ----------

    a0 : Optional[QCoapInternalRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCoapInternalRequest::maxTransmissionSpanReached(
    #      QCoapInternalRequest *a0)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest26maxTransmissionSpanReachedEPS_',
        self._addressOf(a0),
    )

  @overload(THIS)
  @overload(NoneType)
  def multicastRequestExpired(
      self,
      a0: Optional[QCoapInternalRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QCoapInternalRequest::multicastRequestExpired(QCoapInternalRequest *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalrequest.html#multicastRequestExpired

    Parameters
    ----------

    a0 : Optional[QCoapInternalRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QCoapInternalRequest::multicastRequestExpired(QCoapInternalRequest
    #      *a0)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalRequest23multicastRequestExpiredEPS_',
        self._addressOf(a0),
    )

  def d_func(self) -> Optional[QCoapInternalRequestPrivate]:
    """
    Calls Qt's 'QCoapInternalRequestPrivate *QCoapInternalRequest::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalrequest.html#d_func

    Returns
    -------

    Optional[QCoapInternalRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalRequestPrivate *QCoapInternalRequest::d_func()
    address = self.uglySide.call('ritual_ZN20QCoapInternalRequest6d_funcEv')
    from . import QCoapInternalRequestPrivate
    return QCoapInternalRequestPrivate._cuteAt(address)

  @staticmethod
  def addUriOptions(*__, **_) -> Never:
    """
    Qt's 'bool QCoapInternalRequest::addUriOptions(QUrl uri, const QUrl
    &proxyUri)': leans on
    'QCoapInternalMessage::addOption(QCoapOption::OptionName, unsigned int)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapInternalRequest.addUriOptions' has no cute function yet. "
        "Qt's 'bool QCoapInternalRequest::addUriOptions(QUrl uri, const "
        "QUrl &proxyUri)': leans on "
        "'QCoapInternalMessage::addOption(QCoapOption::OptionName, unsigned "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def blockOption(*__, **_) -> Never:
    """
    Qt's 'QCoapOption
    QCoapInternalRequest::blockOption(QCoapOption::OptionName name, uint
    blockNumber, uint blockSize) const': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'appendByte'.
    """
    raise NotImplementedError(
        "'QCoapInternalRequest.blockOption' has no cute function yet. Qt's "
        "'QCoapOption "
        "QCoapInternalRequest::blockOption(QCoapOption::OptionName name, "
        "uint blockNumber, uint blockSize) const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'appendByte'.")

  @staticmethod
  def toQByteArray(*__, **_) -> Never:
    """
    Qt's 'QByteArray QCoapInternalRequest::toQByteArray() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'appendByte'.
    """
    raise NotImplementedError(
        "'QCoapInternalRequest.toQByteArray' has no cute function yet. Qt's "
        "'QByteArray QCoapInternalRequest::toQByteArray() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'appendByte'.")
