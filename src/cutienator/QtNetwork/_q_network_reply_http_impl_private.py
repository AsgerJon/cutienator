"""
QNetworkReplyHttpImplPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyhttpimpl_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkReplyHttpImplPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QHttpNetworkRequest, QNetworkAccessManager, QNetworkReply
from . import QNetworkReplyPrivate, QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QNonContiguousByteDevice, QUrl
  from . import QNetworkReplyHttpImpl, QSslConfiguration
  from . import QSslPreSharedKeyAuthenticator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkReplyHttpImplPrivate(QNetworkReplyPrivate):
  """
  The cute side of Qt's QNetworkReplyHttpImplPrivate: a plain Python object
  standing in front of one C++ QNetworkReplyHttpImplPrivate.

  It is built on the cute 'QNetworkReplyPrivate', as Qt's
  QNetworkReplyHttpImplPrivate is built on Qt's QNetworkReplyPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyHttpImplPrivate that has a ritual and
  that Python can call so far, 30 names in all: 'convert',
  '_q_bufferOutgoingData', '_q_bufferOutgoingDataFinished',
  '_q_cacheSaveDeviceAboutToClose', '_q_finished', 'finished', 'error',
  '_q_error', '_q_metaDataChanged', 'checkForRedirect',
  'maybeDropUploadDevice', 'createUploadByteDevice', 'createCache',
  'completeCacheSave', 'setCachingEnabled', 'isCachingEnabled',
  'isCachingAllowed', 'canResume', 'setResumeOffset', 'invalidateCache',
  'getRedirectOperation', 'createRedirectRequest', 'isHttpRedirectResponse',
  'replyFinished', 'httpError', 'replyEncrypted',
  'replySslConfigurationChanged',
  'replyPreSharedKeyAuthenticationRequiredSlot', 'sentUploadDataSlot',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkReplyHttpImplPrivate::~QNetworkReplyHttpImplPrivate()': the
    destructor: Python never removes a C++ QNetworkReplyHttpImplPrivate.
  - Qt's 'void QNetworkReplyHttpImplPrivate::replySslErrors(const
    QList<QSslError> &a0, bool *a1, QList<QSslError> *a2)': takes a number to
    change where it is.
  - Qt's 'void QNetworkReplyHttpImplPrivate::resetUploadDataSlot(bool *r)':
    takes a number to change where it is.
  - Qt's 'const QNetworkReplyHttpImpl *QNetworkReplyHttpImplPrivate::q_func()
    const': takes in Python what 'QNetworkReplyHttpImpl
    *QNetworkReplyHttpImplPrivate::q_func()' takes.

  What has no ritual
  ------------------

  19 of the 54 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'QNetworkReplyPrivate; 4 leans on 'QNetworkReplyHttpImplPrivate; 3 leans on
  'QNetworkReplyHttpImpl; 2 leans on 'QNetworkAccessAuthenticationManager; 1
  leans on 'QNetworkHeadersPrivate.

  What to expect
  --------------

  - The C++ QNetworkReplyHttpImplPrivate is created at the first use, not by
    'QNetworkReplyHttpImplPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyHttpImplPrivate.
  - Each name of Qt's QNetworkReplyHttpImplPrivate that has no cute function
    yet, '_q_cacheLoadReadyRead', '_q_startOperation', '_q_transferTimedOut',
    'emitReplyUploadProgress', 'fetchCacheMetaData', 'followRedirect',
    'httpAuthenticationRequired', 'initCacheSaveDevice',
    'loadFromCacheIfAllowed', 'onRedirected', 'postRequest',
    'proxyAuthenticationRequired', 'replyDownloadData',
    'replyDownloadMetaData', 'replyDownloadProgressSlot', 'replySslErrors',
    'resetUploadDataSlot', 'sendCacheContents', 'setupTransferTimeout',
    'uploadByteDeviceReadyReadSlot', 'wantUploadDataSlot', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNetworkRequest.Priority)
  def convert(
      prio: QNetworkRequest.Priority,
  ) -> QHttpNetworkRequest.Priority:
    """
    Calls Qt's 'QHttpNetworkRequest::Priority
    QNetworkReplyHttpImplPrivate::convert(QNetworkRequest::Priority prio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#convert

    Parameters
    ----------

    prio : QNetworkRequest.Priority
      Passed on as its number.

    Returns
    -------

    QHttpNetworkRequest.Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QHttpNetworkRequest.Priority(number)' gives.
    """
    #  QHttpNetworkRequest::Priority
    #      QNetworkReplyHttpImplPrivate::convert(QNetworkRequest::Priority
    #      prio)
    return QHttpNetworkRequest.Priority(Rituals.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate7convertEN15QNetworkRequest'
        '8PriorityE',
        prio.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkReplyHttpImplPrivate'

  #  A C++ QNetworkReplyHttpImplPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyHttpImplPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCachingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyHttpImplPrivate::isCachingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#isCachingEnabled
    """
    #  bool QNetworkReplyHttpImplPrivate::isCachingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK28QNetworkReplyHttpImplPrivate16isCachingEnabledEv',
    )

  def isCachingAllowed(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyHttpImplPrivate::isCachingAllowed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#isCachingAllowed
    """
    #  bool QNetworkReplyHttpImplPrivate::isCachingAllowed() const
    return self.uglySide.call(
        'ritual_ZNK28QNetworkReplyHttpImplPrivate16isCachingAllowedEv',
    )

  def canResume(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyHttpImplPrivate::canResume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#canResume
    """
    #  bool QNetworkReplyHttpImplPrivate::canResume() const
    return self.uglySide.call(
        'ritual_ZNK28QNetworkReplyHttpImplPrivate9canResumeEv',
    )

  def isHttpRedirectResponse(self) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyHttpImplPrivate::isHttpRedirectResponse()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  bool QNetworkReplyHttpImplPrivate::isHttpRedirectResponse() const
    return self.uglySide.call(
        'ritual_ZNK28QNetworkReplyHttpImplPrivate22isHttpRedirectResponseEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCachingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::setCachingEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImplPrivate::setCachingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate17setCachingEnabledEb',
        enable,
    )

  @overload(int)
  def setResumeOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::setResumeOffset(quint64
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#setResumeOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImplPrivate::setResumeOffset(quint64 offset)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate15setResumeOffsetEy', offset,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkReplyHttpImplPrivate::QNetworkReplyHttpImplPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  QNetworkReplyHttpImplPrivate::QNetworkReplyHttpImplPrivate()
    self._noteCreation(QNetworkReplyHttpImplPrivate, lambda: Rituals.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivateC1Ev',
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

  def _q_bufferOutgoingData(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingData()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate21_q_bufferOutgoingDataEv',
    )

  def _q_bufferOutgoingDataFinished(self) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::_q_bufferOutgoingDataFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingDataFinished()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate29_q_bufferOutgoingDataFini'
        'shedEv',
    )

  def _q_cacheSaveDeviceAboutToClose(self) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::_q_cacheSaveDeviceAboutToClose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  void QNetworkReplyHttpImplPrivate::_q_cacheSaveDeviceAboutToClose()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate30_q_cacheSaveDeviceAboutTo'
        'CloseEv',
    )

  def _q_finished(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::_q_finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#_q_finished
    """
    #  void QNetworkReplyHttpImplPrivate::_q_finished()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate11_q_finishedEv',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#finished
    """
    #  void QNetworkReplyHttpImplPrivate::finished()
    self.uglySide.call('ritual_ZN28QNetworkReplyHttpImplPrivate8finishedEv')

  @overload(QNetworkReply.NetworkError, str)
  def error(
      self,
      code: QNetworkReply.NetworkError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::error(QNetworkReply::NetworkError code,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#error

    Parameters
    ----------

    code : QNetworkReply.NetworkError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkReplyHttpImplPrivate::error(QNetworkReply::NetworkError
    #      code, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate5errorEN13QNetworkReply12Ne'
        'tworkErrorERK7QString',
        code.value, errorString,
    )

  @overload(QNetworkReply.NetworkError, str)
  def _q_error(
      self,
      code: QNetworkReply.NetworkError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::_q_error(QNetworkReply::NetworkError code,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#_q_error

    Parameters
    ----------

    code : QNetworkReply.NetworkError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QNetworkReplyHttpImplPrivate::_q_error(QNetworkReply::NetworkError
    #      code, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate8_q_errorEN13QNetworkReply1'
        '2NetworkErrorERK7QString',
        code.value, errorString,
    )

  def _q_metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::_q_metaDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  void QNetworkReplyHttpImplPrivate::_q_metaDataChanged()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate18_q_metaDataChangedEv',
    )

  @overload(int)
  def checkForRedirect(self, statusCode: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::checkForRedirect(const int
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#checkForRedirect

    Parameters
    ----------

    statusCode : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImplPrivate::checkForRedirect(const int
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate16checkForRedirectEi',
        statusCode,
    )

  @overload(QNetworkRequest)
  def maybeDropUploadDevice(self, newHttpRequest: QNetworkRequest) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::maybeDropUploadDevice(const QNetworkRequest
    &newHttpRequest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    newHttpRequest : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  void QNetworkReplyHttpImplPrivate::maybeDropUploadDevice(const
    #      QNetworkRequest &newHttpRequest)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate21maybeDropUploadDeviceERK1'
        '5QNetworkRequest',
        self._valueOf(newHttpRequest),
    )

  def createUploadByteDevice(self) -> Optional[QNonContiguousByteDevice]:
    """
    Calls Qt's 'QNonContiguousByteDevice
    *QNetworkReplyHttpImplPrivate::createUploadByteDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Returns
    -------

    Optional[QNonContiguousByteDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNonContiguousByteDevice
    #      *QNetworkReplyHttpImplPrivate::createUploadByteDevice()
    address = self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate22createUploadByteDeviceEv',
    )
    from ..QtCore import QNonContiguousByteDevice
    return QNonContiguousByteDevice._cuteAt(address)

  def createCache(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::createCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#createCache
    """
    #  void QNetworkReplyHttpImplPrivate::createCache()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate11createCacheEv',
    )

  def completeCacheSave(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::completeCacheSave()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html
    """
    #  void QNetworkReplyHttpImplPrivate::completeCacheSave()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate17completeCacheSaveEv',
    )

  def invalidateCache(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::invalidateCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#invalidateCache
    """
    #  void QNetworkReplyHttpImplPrivate::invalidateCache()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate15invalidateCacheEv',
    )

  @overload(QNetworkAccessManager.Operation, int)
  def getRedirectOperation(
      self,
      currentOp: QNetworkAccessManager.Operation,
      httpStatus: int,
  ) -> QNetworkAccessManager.Operation:
    """
    Calls Qt's 'QNetworkAccessManager::Operation
    QNetworkReplyHttpImplPrivate::getRedirectOperation(
    QNetworkAccessManager::Operation currentOp, int httpStatus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    currentOp : QNetworkAccessManager.Operation
      Passed on as its number.

    httpStatus : int
      Passed on as it is.

    Returns
    -------

    QNetworkAccessManager.Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkAccessManager.Operation(number)' gives.
    """
    #  QNetworkAccessManager::Operation
    #      QNetworkReplyHttpImplPrivate::getRedirectOperation(
    #      QNetworkAccessManager::Operation currentOp, int httpStatus)
    return QNetworkAccessManager.Operation(self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate20getRedirectOperationEN21Q'
        'NetworkAccessManager9OperationEi',
        currentOp.value, httpStatus,
    ))

  @overload(QNetworkRequest, QUrl, int)
  def createRedirectRequest(
      self,
      originalRequests: QNetworkRequest,
      url: QUrl,
      maxRedirectsRemainig: int,
  ) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest
    QNetworkReplyHttpImplPrivate::createRedirectRequest(const QNetworkRequest
    &originalRequests, const QUrl &url, int maxRedirectsRemainig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    originalRequests : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    maxRedirectsRemainig : int
      Passed on as it is.

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest
    #      QNetworkReplyHttpImplPrivate::createRedirectRequest(const
    #      QNetworkRequest &originalRequests, const QUrl &url, int
    #      maxRedirectsRemainig)
    address = self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate21createRedirectRequestERK1'
        '5QNetworkRequestRK4QUrli',
        self._valueOf(originalRequests), self._valueOf(url),
        maxRedirectsRemainig,
    )
    return QNetworkRequest._cuteOwning(address)

  def replyFinished(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::replyFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#replyFinished
    """
    #  void QNetworkReplyHttpImplPrivate::replyFinished()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate13replyFinishedEv',
    )

  @overload(QNetworkReply.NetworkError, str)
  def httpError(
      self,
      error: QNetworkReply.NetworkError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::httpError(QNetworkReply::NetworkError
    error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#httpError

    Parameters
    ----------

    error : QNetworkReply.NetworkError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkReplyHttpImplPrivate::httpError(QNetworkReply::
    #      NetworkError error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate9httpErrorEN13QNetworkReply'
        '12NetworkErrorERK7QString',
        error.value, errorString,
    )

  def replyEncrypted(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::replyEncrypted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#replyEncrypted
    """
    #  void QNetworkReplyHttpImplPrivate::replyEncrypted()
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate14replyEncryptedEv',
    )

  @overload(QSslConfiguration)
  def replySslConfigurationChanged(
      self,
      newSslConfiguration: QSslConfiguration,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyHttpImplPrivate::replySslConfigurationChanged(const
    QSslConfiguration &newSslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    newSslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkReplyHttpImplPrivate::replySslConfigurationChanged(const
    #      QSslConfiguration &newSslConfiguration)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate28replySslConfigurationChan'
        'gedERK17QSslConfiguration',
        self._valueOf(newSslConfiguration),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def replyPreSharedKeyAuthenticationRequiredSlot(
      self,
      a0: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::
    replyPreSharedKeyAuthenticationRequiredSlot(QSslPreSharedKeyAuthenticator
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    a0 : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkReplyHttpImplPrivate::
    #      replyPreSharedKeyAuthenticationRequiredSlot(
    #      QSslPreSharedKeyAuthenticator *a0)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate43replyPreSharedKeyAuthenti'
        'cationRequiredSlotEP29QSslPreSharedKeyAuthenticator',
        self._addressOf(a0),
    )

  @overload(int, int)
  def sentUploadDataSlot(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyHttpImplPrivate::sentUploadDataSlot(qint64
    a0, qint64 a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QNetworkReplyHttpImplPrivate::sentUploadDataSlot(qint64 a0,
    #      qint64 a1)
    self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate18sentUploadDataSlotExx',
        a0, a1,
    )

  def q_func(self) -> Optional[QNetworkReplyHttpImpl]:
    """
    Calls Qt's 'QNetworkReplyHttpImpl
    *QNetworkReplyHttpImplPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyhttpimplprivate.html#q_func

    Returns
    -------

    Optional[QNetworkReplyHttpImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyHttpImpl *QNetworkReplyHttpImplPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QNetworkReplyHttpImplPrivate6q_funcEv',
    )
    from . import QNetworkReplyHttpImpl
    return QNetworkReplyHttpImpl._cuteAt(address)

  @staticmethod
  def _q_cacheLoadReadyRead(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::_q_cacheLoadReadyRead()': leans
    on 'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate._q_cacheLoadReadyRead' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::_q_cacheLoadReadyRead()': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def _q_startOperation(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::_q_startOperation()': leans on
    'QNetworkReplyHttpImplPrivate::postRequest(QNetworkRequest const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate._q_startOperation' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::_q_startOperation()': leans on "
        "'QNetworkReplyHttpImplPrivate::postRequest(QNetworkRequest "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def _q_transferTimedOut(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::_q_transferTimedOut()': leans on
    'QNetworkReplyHttpImpl::abortHttpRequest()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate._q_transferTimedOut' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::_q_transferTimedOut()': leans on "
        "'QNetworkReplyHttpImpl::abortHttpRequest()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def emitReplyUploadProgress(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::emitReplyUploadProgress(qint64
    bytesSent, qint64 bytesTotal)': leans on
    'QNetworkReplyPrivate::progressSignalInterval', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.emitReplyUploadProgress' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::emitReplyUploadProgress(qint64 "
        "bytesSent, qint64 bytesTotal)': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def fetchCacheMetaData(*__, **_) -> Never:
    """
    Qt's 'QNetworkCacheMetaData
    QNetworkReplyHttpImplPrivate::fetchCacheMetaData(const
    QNetworkCacheMetaData &metaData) const': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'isAsciiDigit'; did you mean
    'QtMiscUtils::isAsciiDigit'?.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.fetchCacheMetaData' has no cute "
        "function yet. Qt's 'QNetworkCacheMetaData "
        "QNetworkReplyHttpImplPrivate::fetchCacheMetaData(const "
        "QNetworkCacheMetaData &metaData) const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'isAsciiDigit'; did you "
        "mean 'QtMiscUtils::isAsciiDigit'?.")

  @staticmethod
  def followRedirect(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::followRedirect()': leans on
    'QNetworkReplyHttpImplPrivate::postRequest(QNetworkRequest const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.followRedirect' has no cute function "
        "yet. Qt's 'void QNetworkReplyHttpImplPrivate::followRedirect()': "
        "leans on "
        "'QNetworkReplyHttpImplPrivate::postRequest(QNetworkRequest "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def httpAuthenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::httpAuthenticationRequired(const
    QHttpNetworkRequest &request, QAuthenticator *auth)': leans on
    'QNetworkAccessAuthenticationManager::cacheCredentials(QUrl const&,
    QAuthenticator const*)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.httpAuthenticationRequired' has no "
        "cute function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::httpAuthenticationRequired(const "
        "QHttpNetworkRequest &request, QAuthenticator *auth)': leans on "
        "'QNetworkAccessAuthenticationManager::cacheCredentials(QUrl "
        "const&, QAuthenticator const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def initCacheSaveDevice(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::initCacheSaveDevice()': leans on
    'QNetworkReplyHttpImplPrivate::fetchCacheMetaData(QNetworkCacheMetaData
    const&) const', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.initCacheSaveDevice' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::initCacheSaveDevice()': leans on "
        "'QNetworkReplyHttpImplPrivate::fetchCacheMetaData(QNetworkCacheMeta"
        "Data const&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadFromCacheIfAllowed(*__, **_) -> Never:
    """
    Qt's 'bool
    QNetworkReplyHttpImplPrivate::loadFromCacheIfAllowed(QHttpNetworkRequest
    &httpRequest)': leans on
    'QNetworkHeadersPrivate::setHeaders(QHttpHeaders&&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.loadFromCacheIfAllowed' has no cute "
        "function yet. Qt's 'bool "
        "QNetworkReplyHttpImplPrivate::loadFromCacheIfAllowed(QHttpNetworkRe"
        "quest &httpRequest)': leans on "
        "'QNetworkHeadersPrivate::setHeaders(QHttpHeaders&&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def onRedirected(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::onRedirected(const QUrl
    &redirectUrl, int httpStatus, int maxRedirectsRemainig)': leans on
    'QNetworkReplyHttpImplPrivate::postRequest(QNetworkRequest const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.onRedirected' has no cute function "
        "yet. Qt's 'void QNetworkReplyHttpImplPrivate::onRedirected(const "
        "QUrl &redirectUrl, int httpStatus, int maxRedirectsRemainig)': "
        "leans on "
        "'QNetworkReplyHttpImplPrivate::postRequest(QNetworkRequest "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def postRequest(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::postRequest(const
    QNetworkRequest &newHttpRequest)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'bytesEqualPrefix'.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.postRequest' has no cute function "
        "yet. Qt's 'void QNetworkReplyHttpImplPrivate::postRequest(const "
        "QNetworkRequest &newHttpRequest)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'bytesEqualPrefix'.")

  @staticmethod
  def proxyAuthenticationRequired(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReplyHttpImplPrivate::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *auth)': leans on
    'QNetworkAccessAuthenticationManager::cacheProxyCredentials(QNetworkProxy
    const&, QAuthenticator const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.proxyAuthenticationRequired' has no "
        "cute function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::proxyAuthenticationRequired(const "
        "QNetworkProxy &proxy, QAuthenticator *auth)': leans on "
        "'QNetworkAccessAuthenticationManager::cacheProxyCredentials(QNetwor"
        "kProxy const&, QAuthenticator const*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def replyDownloadData(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::replyDownloadData(QByteArray
    a0)': leans on 'QNetworkReplyPrivate::progressSignalInterval', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.replyDownloadData' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::replyDownloadData(QByteArray a0)': "
        "leans on 'QNetworkReplyPrivate::progressSignalInterval', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def replyDownloadMetaData(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::replyDownloadMetaData(const
    QHttpHeaders &a0, int a1, const QString &a2, bool a3,
    QSharedPointer<char> a4, qint64 a5, qint64 a6, bool a7, bool a8)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'locationHeader'.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.replyDownloadMetaData' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::replyDownloadMetaData(const "
        "QHttpHeaders &a0, int a1, const QString &a2, bool a3, "
        "QSharedPointer<char> a4, qint64 a5, qint64 a6, bool a7, bool a8)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'locationHeader'.")

  @staticmethod
  def replyDownloadProgressSlot(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::replyDownloadProgressSlot(qint64
    a0, qint64 a1)': leans on 'QNetworkReplyPrivate::progressSignalInterval',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.replyDownloadProgressSlot' has no "
        "cute function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::replyDownloadProgressSlot(qint64 a0, "
        "qint64 a1)': leans on "
        "'QNetworkReplyPrivate::progressSignalInterval', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def replySslErrors(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::replySslErrors(const
    QList<QSslError> &a0, bool *a1, QList<QSslError> *a2)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.replySslErrors' has no cute function "
        "yet. Qt's 'void QNetworkReplyHttpImplPrivate::replySslErrors(const "
        "QList<QSslError> &a0, bool *a1, QList<QSslError> *a2)': takes a "
        "number to change where it is.")

  @staticmethod
  def resetUploadDataSlot(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::resetUploadDataSlot(bool *r)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.resetUploadDataSlot' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::resetUploadDataSlot(bool *r)': takes "
        "a number to change where it is.")

  @staticmethod
  def sendCacheContents(*__, **_) -> Never:
    """
    Qt's 'bool QNetworkReplyHttpImplPrivate::sendCacheContents(const
    QNetworkCacheMetaData &metaData)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'locationHeader'.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.sendCacheContents' has no cute "
        "function yet. Qt's 'bool "
        "QNetworkReplyHttpImplPrivate::sendCacheContents(const "
        "QNetworkCacheMetaData &metaData)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'locationHeader'.")

  @staticmethod
  def setupTransferTimeout(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::setupTransferTimeout()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no matching literal operator for call to
    'operator""ms' with argument of type 'unsigned long long' or 'const char
    *', and no matching literal operator template.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.setupTransferTimeout' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::setupTransferTimeout()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no matching literal operator for call "
        "to 'operator\"\"ms' with argument of type 'unsigned long long' or "
        "'const char *', and no matching literal operator template.")

  @staticmethod
  def uploadByteDeviceReadyReadSlot(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkReplyHttpImplPrivate::uploadByteDeviceReadyReadSlot()': leans on
    'QNetworkReplyHttpImpl::haveUploadData(long long, QByteArray const&,
    bool, long long)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.uploadByteDeviceReadyReadSlot' has "
        "no cute function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::uploadByteDeviceReadyReadSlot()': "
        "leans on 'QNetworkReplyHttpImpl::haveUploadData(long long, "
        "QByteArray const&, bool, long long)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def wantUploadDataSlot(*__, **_) -> Never:
    """
    Qt's 'void QNetworkReplyHttpImplPrivate::wantUploadDataSlot(qint64 a0)':
    leans on 'QNetworkReplyHttpImpl::haveUploadData(long long, QByteArray
    const&, bool, long long)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyHttpImplPrivate.wantUploadDataSlot' has no cute "
        "function yet. Qt's 'void "
        "QNetworkReplyHttpImplPrivate::wantUploadDataSlot(qint64 a0)': "
        "leans on 'QNetworkReplyHttpImpl::haveUploadData(long long, "
        "QByteArray const&, bool, long long)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
