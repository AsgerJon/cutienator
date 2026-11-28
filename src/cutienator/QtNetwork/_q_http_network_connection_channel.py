"""
QHttpNetworkConnectionChannel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnectionchannel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QHttpNetworkConnectionChannel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QList, QObject
from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QHttp2ProtocolHandler, QHttpNetworkConnection, QNetworkProxy
  from . import QSslConfiguration, QSslError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttpNetworkConnection = WAIT['QHttpNetworkConnection']
  QNetworkProxy = WAIT['QNetworkProxy']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpNetworkConnectionChannel(QObject):
  """
  The cute side of Qt's QHttpNetworkConnectionChannel: a plain Python object
  standing in front of one C++ QHttpNetworkConnectionChannel.

  It is built on the cute 'QObject', as Qt's QHttpNetworkConnectionChannel is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpNetworkConnectionChannel that has a ritual and
  that Python can call so far, 26 names in all: 'h2ProtocolHandler',
  'isPendingReconnect', 'clearPendingReconnect', 'requeueHttp2Requests',
  'ignoreSslErrors', 'setSslConfiguration', 'emitFinishedWithError',
  'pipelineFlush', 'requeueCurrentlyPipelinedRequests',
  'detectPipeliningSupport', 'setConnection', 'setProxy', 'close', 'abort',
  'sendRequest', 'sendRequestDelayed', 'handleStatus', 'resetUploadData',
  'handleUnexpectedEOF', 'closeAndResendCurrentRequest',
  'resendCurrentRequest', 'checkAndResumeCommunication', 'isSocketBusy',
  'isSocketWriting', 'isSocketWaiting', 'isSocketReading'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QHttpNetworkConnectionChannel::pipelineInto(HttpMessagePair
    &pair)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  25 of the 53 functions Qt declares: 21 leans on
  'QHttpNetworkConnectionChannel; 2 not a gap; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'vtable for QHttpNetworkConnectionChannel', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QHttpNetworkConnectionChannel is created at the first use, not by
    'QHttpNetworkConnectionChannel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpNetworkConnectionChannel.
  - Qt tells when it has removed the C++ QHttpNetworkConnectionChannel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpNetworkConnectionChannel that has no cute function
    yet, '__init__', '_q_bytesWritten', '_q_connected',
    '_q_connected_abstract_socket', '_q_connected_local_socket',
    '_q_disconnected', '_q_encrypted', '_q_encryptedBytesWritten',
    '_q_error', '_q_preSharedKeyAuthenticationRequired',
    '_q_proxyAuthenticationRequired', '_q_readyRead', '_q_receiveReply',
    '_q_sslErrors', '_q_uploadDataReadyRead', 'allDone', 'ensureConnection',
    'init', 'pipelineInto', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttpNetworkConnectionChannel, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class ChannelState(CuteNum):
    """
    The enum 'QHttpNetworkConnectionChannel::ChannelState' of Qt, with the 7
    names Qt gives in it.
    """

    IdleState = Kee[int](0)
    ConnectingState = Kee[int](1)
    WritingState = Kee[int](2)
    WaitingState = Kee[int](4)
    ReadingState = Kee[int](8)
    ClosingState = Kee[int](16)
    BusyState = Kee[int](31)

  class PipeliningSupport(CuteNum):
    """
    The enum 'QHttpNetworkConnectionChannel::PipeliningSupport' of Qt, with
    the 3 names Qt gives in it.
    """

    PipeliningSupportUnknown = Kee[int](0)
    PipeliningProbablySupported = Kee[int](1)
    PipeliningNotSupported = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkConnectionChannel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def h2ProtocolHandler(self) -> Optional[QHttp2ProtocolHandler]:
    """
    Calls Qt's 'QHttp2ProtocolHandler
    *QHttpNetworkConnectionChannel::h2ProtocolHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html

    Returns
    -------

    Optional[QHttp2ProtocolHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttp2ProtocolHandler
    #      *QHttpNetworkConnectionChannel::h2ProtocolHandler() const
    address = self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionChannel17h2ProtocolHandlerEv',
    )
    from . import QHttp2ProtocolHandler
    return QHttp2ProtocolHandler._cuteAt(address)

  def isPendingReconnect(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::isPendingReconnect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  bool QHttpNetworkConnectionChannel::isPendingReconnect() const
    return self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionChannel18isPendingReconnectEv',
    )

  def isSocketBusy(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::isSocketBusy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#isSocketBusy
    """
    #  bool QHttpNetworkConnectionChannel::isSocketBusy() const
    return self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionChannel12isSocketBusyEv',
    )

  def isSocketWriting(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::isSocketWriting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#isSocketWriting
    """
    #  bool QHttpNetworkConnectionChannel::isSocketWriting() const
    return self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionChannel15isSocketWritingEv',
    )

  def isSocketWaiting(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::isSocketWaiting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#isSocketWaiting
    """
    #  bool QHttpNetworkConnectionChannel::isSocketWaiting() const
    return self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionChannel15isSocketWaitingEv',
    )

  def isSocketReading(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::isSocketReading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#isSocketReading
    """
    #  bool QHttpNetworkConnectionChannel::isSocketReading() const
    return self.uglySide.call(
        'ritual_ZNK29QHttpNetworkConnectionChannel15isSocketReadingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSslConfiguration)
  def setSslConfiguration(self, config: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::setSslConfiguration(const
    QSslConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html

    Parameters
    ----------

    config : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QHttpNetworkConnectionChannel::setSslConfiguration(const
    #      QSslConfiguration &config)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel19setSslConfigurationERK17'
        'QSslConfiguration',
        self._valueOf(config),
    )

  @overload(QHttpNetworkConnection)
  @overload(NoneType)
  def setConnection(self, c: Optional[QHttpNetworkConnection]) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionChannel::setConnection(QHttpNetworkConnection *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#setConnection

    Parameters
    ----------

    c : Optional[QHttpNetworkConnection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkConnectionChannel::setConnection(
    #      QHttpNetworkConnection *c)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel13setConnectionEP22QHttpNe'
        'tworkConnection',
        self._addressOf(c),
    )

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::setProxy(const
    QNetworkProxy &networkProxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QHttpNetworkConnectionChannel::setProxy(const QNetworkProxy
    #      &networkProxy)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel8setProxyERK13QNetworkProx'
        'y',
        self._valueOf(networkProxy),
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
    Qt's 'QHttpNetworkConnectionChannel::QHttpNetworkConnectionChannel()':
    leans on 'vtable for QHttpNetworkConnectionChannel', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel.__init__' has no cute function yet. "
        "Qt's "
        "'QHttpNetworkConnectionChannel::QHttpNetworkConnectionChannel()': "
        "leans on 'vtable for QHttpNetworkConnectionChannel', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def clearPendingReconnect(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::clearPendingReconnect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  bool QHttpNetworkConnectionChannel::clearPendingReconnect()
    return self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel21clearPendingReconnectEv',
    )

  def requeueHttp2Requests(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::requeueHttp2Requests()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::requeueHttp2Requests()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel20requeueHttp2RequestsEv',
    )

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::ignoreSslErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#ignoreSslErrors
    """
    #  void QHttpNetworkConnectionChannel::ignoreSslErrors()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel15ignoreSslErrorsEv',
    )

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::ignoreSslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHttpNetworkConnectionChannel::ignoreSslErrors(const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel15ignoreSslErrorsERK5QList'
        'I9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QNetworkReply.NetworkError, str)
  def emitFinishedWithError(
      self,
      error: QNetworkReply.NetworkError,
      message: str,
  ) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionChannel::emitFinishedWithError(QNetworkReply::
    NetworkError error, const QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html

    Parameters
    ----------

    error : QNetworkReply.NetworkError
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpNetworkConnectionChannel::emitFinishedWithError(
    #      QNetworkReply::NetworkError error, const QString &message)
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel21emitFinishedWithErrorEN1'
        '3QNetworkReply12NetworkErrorERK7QString',
        error.value, message,
    )

  def pipelineFlush(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::pipelineFlush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#pipelineFlush
    """
    #  void QHttpNetworkConnectionChannel::pipelineFlush()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel13pipelineFlushEv',
    )

  def requeueCurrentlyPipelinedRequests(self) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionChannel::requeueCurrentlyPipelinedRequests()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void
    #      QHttpNetworkConnectionChannel::requeueCurrentlyPipelinedRequests()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel33requeueCurrentlyPipeline'
        'dRequestsEv',
    )

  def detectPipeliningSupport(self) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionChannel::detectPipeliningSupport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::detectPipeliningSupport()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel23detectPipeliningSupportE'
        'v',
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::close()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#close
    """
    #  void QHttpNetworkConnectionChannel::close()
    self.uglySide.call('ritual_ZN29QHttpNetworkConnectionChannel5closeEv')

  def abort(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::abort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#abort
    """
    #  void QHttpNetworkConnectionChannel::abort()
    self.uglySide.call('ritual_ZN29QHttpNetworkConnectionChannel5abortEv')

  def sendRequest(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::sendRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#sendRequest
    """
    #  void QHttpNetworkConnectionChannel::sendRequest()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel11sendRequestEv',
    )

  def sendRequestDelayed(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::sendRequestDelayed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::sendRequestDelayed()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel18sendRequestDelayedEv',
    )

  def handleStatus(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::handleStatus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#handleStatus
    """
    #  void QHttpNetworkConnectionChannel::handleStatus()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel12handleStatusEv',
    )

  def resetUploadData(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnectionChannel::resetUploadData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html#resetUploadData
    """
    #  bool QHttpNetworkConnectionChannel::resetUploadData()
    return self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel15resetUploadDataEv',
    )

  def handleUnexpectedEOF(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::handleUnexpectedEOF()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::handleUnexpectedEOF()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel19handleUnexpectedEOFEv',
    )

  def closeAndResendCurrentRequest(self) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionChannel::closeAndResendCurrentRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::closeAndResendCurrentRequest()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel28closeAndResendCurrentReq'
        'uestEv',
    )

  def resendCurrentRequest(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnectionChannel::resendCurrentRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::resendCurrentRequest()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel20resendCurrentRequestEv',
    )

  def checkAndResumeCommunication(self) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkConnectionChannel::checkAndResumeCommunication()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnectionchannel.html
    """
    #  void QHttpNetworkConnectionChannel::checkAndResumeCommunication()
    self.uglySide.call(
        'ritual_ZN29QHttpNetworkConnectionChannel27checkAndResumeCommunicat'
        'ionEv',
    )

  @staticmethod
  def _q_bytesWritten(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_bytesWritten(qint64 bytes)':
    leans on 'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_bytesWritten' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_bytesWritten(qint64 bytes)': "
        "leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_connected(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_connected()': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_connected' has no cute function "
        "yet. Qt's 'void QHttpNetworkConnectionChannel::_q_connected()': "
        "leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_connected_abstract_socket(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_connected_abstract_socket(
    QAbstractSocket *socket)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_connected_abstract_socket' has "
        "no cute function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_connected_abstract_socket(QAbstra"
        "ctSocket *socket)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_connected_local_socket(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpNetworkConnectionChannel::_q_connected_local_socket(QLocalSocket
    *socket)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_connected_local_socket' has no "
        "cute function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_connected_local_socket(QLocalSock"
        "et *socket)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_disconnected(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_disconnected()': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_disconnected' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_disconnected()': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_encrypted(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_encrypted()': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_encrypted' has no cute function "
        "yet. Qt's 'void QHttpNetworkConnectionChannel::_q_encrypted()': "
        "leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_encryptedBytesWritten(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_encryptedBytesWritten(qint64
    bytes)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_encryptedBytesWritten' has no "
        "cute function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_encryptedBytesWritten(qint64 "
        "bytes)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_error(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpNetworkConnectionChannel::_q_error(QAbstractSocket::SocketError
    a0)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_error' has no cute function yet. "
        "Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_error(QAbstractSocket::SocketErro"
        "r a0)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_preSharedKeyAuthenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpNetworkConnectionChannel::_q_preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *a0)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_preSharedKeyAuthenticationRequire"
        "d' has no cute function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_preSharedKeyAuthenticationRequire"
        "d(QSslPreSharedKeyAuthenticator *a0)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_proxyAuthenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpNetworkConnectionChannel::_q_proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *auth)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_proxyAuthenticationRequired' has "
        "no cute function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_proxyAuthenticationRequired(const"
        " QNetworkProxy &proxy, QAuthenticator *auth)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_readyRead(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_readyRead()': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_readyRead' has no cute function "
        "yet. Qt's 'void QHttpNetworkConnectionChannel::_q_readyRead()': "
        "leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_receiveReply(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_receiveReply()': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_receiveReply' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_receiveReply()': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_sslErrors(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_sslErrors(const
    QList<QSslError> &errors)': leans on
    'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_sslErrors' has no cute function "
        "yet. Qt's 'void QHttpNetworkConnectionChannel::_q_sslErrors(const "
        "QList<QSslError> &errors)': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def _q_uploadDataReadyRead(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::_q_uploadDataReadyRead()':
    leans on 'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel._q_uploadDataReadyRead' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::_q_uploadDataReadyRead()': leans on "
        "'QHttpNetworkConnectionChannel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def allDone(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::allDone()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'reconnectAttemptsDefault'; did you
    mean 'reconnectAttempts'?.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel.allDone' has no cute function yet. "
        "Qt's 'void QHttpNetworkConnectionChannel::allDone()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'reconnectAttemptsDefault'; did you mean 'reconnectAttempts'?.")

  @staticmethod
  def ensureConnection(*__, **_) -> Never:
    """
    Qt's 'bool QHttpNetworkConnectionChannel::ensureConnection()': leans on
    'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel.ensureConnection' has no cute "
        "function yet. Qt's 'bool "
        "QHttpNetworkConnectionChannel::ensureConnection()': leans on "
        "'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::init()': leans on
    'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel.init' has no cute function yet. "
        "Qt's 'void QHttpNetworkConnectionChannel::init()': leans on "
        "'QHttpNetworkConnectionChannel::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def pipelineInto(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkConnectionChannel::pipelineInto(HttpMessagePair
    &pair)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnectionChannel.pipelineInto' has no cute function "
        "yet. Qt's 'void "
        "QHttpNetworkConnectionChannel::pipelineInto(HttpMessagePair "
        "&pair)': takes a type Python has no way to hand over yet.")
