"""
QHttpThreadDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpThreadDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from . import QAuthenticator, QHttpNetworkRequest, QNetworkProxy
  from . import QSslConfiguration, QSslError, QSslPreSharedKeyAuthenticator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QByteArray = WAIT['QByteArray']
  QHttpNetworkRequest = WAIT['QHttpNetworkRequest']
  QNetworkProxy = WAIT['QNetworkProxy']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpThreadDelegate(QObject):
  """
  The cute side of Qt's QHttpThreadDelegate: a plain Python object standing
  in front of one C++ QHttpThreadDelegate.

  It is built on the cute 'QObject', as Qt's QHttpThreadDelegate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpThreadDelegate that has a ritual and that
  Python can call so far, 32 names in all: 'metaObject',
  'authenticationRequired', 'proxyAuthenticationRequired', 'encrypted',
  'sslConfigurationChanged', 'preSharedKeyAuthenticationRequired',
  'socketStartedConnecting', 'requestSent', 'downloadProgress',
  'downloadData', 'error', 'downloadFinished', 'redirected', 'startRequest',
  'abortRequest', 'readBufferSizeChanged', 'readBufferFreed',
  'startRequestSynchronously', 'readyReadSlot', 'finishedSlot',
  'finishedWithErrorSlot', 'synchronousFinishedSlot',
  'synchronousFinishedWithErrorSlot', 'headerChangedSlot',
  'synchronousHeaderChangedSlot', 'dataReadProgressSlot',
  'cacheCredentialsSlot', 'encryptedSlot', 'sslErrorsSlot',
  'preSharedKeyAuthenticationRequiredSlot',
  'synchronousAuthenticationRequiredSlot',
  'synchronousProxyAuthenticationRequiredSlot'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpThreadDelegate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHttpThreadDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHttpThreadDelegate::~QHttpThreadDelegate()': the destructor:
    Python never removes a C++ QHttpThreadDelegate.
  - Qt's 'void QHttpThreadDelegate::sslErrors(const QList<QSslError> &a0,
    bool *a1, QList<QSslError> *a2)': takes a number to change where it is.
  - Qt's 'void QHttpThreadDelegate::downloadMetaData(const QHttpHeaders &a0,
    int a1, const QString &a2, bool a3, QSharedPointer<char> a4, qint64 a5,
    qint64 a6, bool a7, bool a8)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 leans on
  'QHttpThreadDelegate.

  What to expect
  --------------

  - The C++ QHttpThreadDelegate is created at the first use, not by
    'QHttpThreadDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpThreadDelegate.
  - Qt tells when it has removed the C++ QHttpThreadDelegate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpThreadDelegate that has no cute function yet,
    '__init__', 'downloadMetaData', 'sslErrors', holds a function that raises
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
  __qt_class__ = 'QHttpThreadDelegate'

  #  A C++ QHttpThreadDelegate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpThreadDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttpThreadDelegate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpThreadDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QHttpThreadDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QHttpThreadDelegate::QHttpThreadDelegate(QObject *parent)': leans
    on 'QHttpThreadDelegate::connections', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpThreadDelegate.__init__' has no cute function yet. Qt's "
        "'QHttpThreadDelegate::QHttpThreadDelegate(QObject *parent)': leans "
        "on 'QHttpThreadDelegate::connections', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QHttpNetworkRequest, QAuthenticator)
  @overload(QHttpNetworkRequest, NoneType)
  def authenticationRequired(
      self,
      request: QHttpNetworkRequest,
      a1: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::authenticationRequired(const
    QHttpNetworkRequest &request, QAuthenticator *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#authenticationRequired

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    a1 : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::authenticationRequired(const
    #      QHttpNetworkRequest &request, QAuthenticator *a1)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate22authenticationRequiredERK19QHttpNe'
        'tworkRequestP14QAuthenticator',
        self._valueOf(request), self._addressOf(a1),
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      a0: QNetworkProxy,
      a1: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::proxyAuthenticationRequired(const
    QNetworkProxy &a0, QAuthenticator *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html

    Parameters
    ----------

    a0 : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    a1 : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::proxyAuthenticationRequired(const
    #      QNetworkProxy &a0, QAuthenticator *a1)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate27proxyAuthenticationRequiredERK13QN'
        'etworkProxyP14QAuthenticator',
        self._valueOf(a0), self._addressOf(a1),
    )

  def encrypted(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::encrypted()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpthreaddelegate.html#encrypted
    """
    #  void QHttpThreadDelegate::encrypted()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate9encryptedEv')

  @overload(QSslConfiguration)
  def sslConfigurationChanged(self, a0: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::sslConfigurationChanged(const
    QSslConfiguration &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#sslConfigurationChanged

    Parameters
    ----------

    a0 : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QHttpThreadDelegate::sslConfigurationChanged(const
    #      QSslConfiguration &a0)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate23sslConfigurationChangedERK17QSslCo'
        'nfiguration',
        self._valueOf(a0),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      a0: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html

    Parameters
    ----------

    a0 : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::preSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *a0)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate34preSharedKeyAuthenticationRequired'
        'EP29QSslPreSharedKeyAuthenticator',
        self._addressOf(a0),
    )

  def socketStartedConnecting(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::socketStartedConnecting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#socketStartedConnecting
    """
    #  void QHttpThreadDelegate::socketStartedConnecting()
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate23socketStartedConnectingEv',
    )

  def requestSent(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::requestSent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#requestSent
    """
    #  void QHttpThreadDelegate::requestSent()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate11requestSentEv')

  @overload(int, int)
  def downloadProgress(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::downloadProgress(qint64 a0, qint64
    a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#downloadProgress

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QHttpThreadDelegate::downloadProgress(qint64 a0, qint64 a1)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate16downloadProgressExx', a0, a1,
    )

  @overload(QByteArray)
  def downloadData(self, a0: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::downloadData(const QByteArray
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#downloadData

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpThreadDelegate::downloadData(const QByteArray &a0)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate12downloadDataERK10QByteArray',
        self._valueOf(a0),
    )

  @overload(QNetworkReply.NetworkError, str)
  def error(self, a0: QNetworkReply.NetworkError, a1: str) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::error(QNetworkReply::NetworkError
    a0, const QString &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpthreaddelegate.html#error

    Parameters
    ----------

    a0 : QNetworkReply.NetworkError
      Passed on as its number.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpThreadDelegate::error(QNetworkReply::NetworkError a0, const
    #      QString &a1)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate5errorEN13QNetworkReply12NetworkErro'
        'rERK7QString',
        a0.value, a1,
    )

  def downloadFinished(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::downloadFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#downloadFinished
    """
    #  void QHttpThreadDelegate::downloadFinished()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate16downloadFinishedEv')

  @overload(QUrl, int, int)
  def redirected(
      self,
      url: QUrl,
      httpStatus: int,
      maxRedirectsRemainig: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::redirected(const QUrl &url, int
    httpStatus, int maxRedirectsRemainig)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#redirected

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    httpStatus : int
      Passed on as it is.

    maxRedirectsRemainig : int
      Passed on as it is.
    """
    #  void QHttpThreadDelegate::redirected(const QUrl &url, int httpStatus,
    #      int maxRedirectsRemainig)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate10redirectedERK4QUrlii',
        self._valueOf(url), httpStatus, maxRedirectsRemainig,
    )

  def startRequest(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::startRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#startRequest
    """
    #  void QHttpThreadDelegate::startRequest()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate12startRequestEv')

  def abortRequest(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::abortRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#abortRequest
    """
    #  void QHttpThreadDelegate::abortRequest()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate12abortRequestEv')

  @overload(int)
  def readBufferSizeChanged(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::readBufferSizeChanged(qint64
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#readBufferSizeChanged

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpThreadDelegate::readBufferSizeChanged(qint64 size)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate21readBufferSizeChangedEx', size,
    )

  @overload(int)
  def readBufferFreed(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::readBufferFreed(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#readBufferFreed

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpThreadDelegate::readBufferFreed(qint64 size)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate15readBufferFreedEx', size,
    )

  def startRequestSynchronously(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::startRequestSynchronously()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#startRequestSynchronously
    """
    #  void QHttpThreadDelegate::startRequestSynchronously()
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate25startRequestSynchronouslyEv',
    )

  def readyReadSlot(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::readyReadSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#readyReadSlot
    """
    #  void QHttpThreadDelegate::readyReadSlot()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate13readyReadSlotEv')

  def finishedSlot(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::finishedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#finishedSlot
    """
    #  void QHttpThreadDelegate::finishedSlot()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate12finishedSlotEv')

  @overload(QNetworkReply.NetworkError)
  @overload(QNetworkReply.NetworkError, str)
  def finishedWithErrorSlot(
      self,
      errorCode: QNetworkReply.NetworkError,
      detail: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QHttpThreadDelegate::finishedWithErrorSlot(QNetworkReply::NetworkError
    errorCode, const QString &detail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#finishedWithErrorSlot

    Parameters
    ----------

    errorCode : QNetworkReply.NetworkError
      Passed on as its number.

    detail : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QHttpThreadDelegate::finishedWithErrorSlot(QNetworkReply::
    #      NetworkError errorCode, const QString &detail)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate21finishedWithErrorSlotEN13QNetworkR'
        'eply12NetworkErrorERK7QString',
        errorCode.value, detail,
    )

  def synchronousFinishedSlot(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::synchronousFinishedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#synchronousFinishedSlot
    """
    #  void QHttpThreadDelegate::synchronousFinishedSlot()
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate23synchronousFinishedSlotEv',
    )

  @overload(QNetworkReply.NetworkError)
  @overload(QNetworkReply.NetworkError, str)
  def synchronousFinishedWithErrorSlot(
      self,
      errorCode: QNetworkReply.NetworkError,
      detail: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QHttpThreadDelegate::synchronousFinishedWithErrorSlot(QNetworkReply::
    NetworkError errorCode, const QString &detail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html

    Parameters
    ----------

    errorCode : QNetworkReply.NetworkError
      Passed on as its number.

    detail : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QHttpThreadDelegate::synchronousFinishedWithErrorSlot(
    #      QNetworkReply::NetworkError errorCode, const QString &detail)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate32synchronousFinishedWithErrorSlotEN'
        '13QNetworkReply12NetworkErrorERK7QString',
        errorCode.value, detail,
    )

  def headerChangedSlot(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::headerChangedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#headerChangedSlot
    """
    #  void QHttpThreadDelegate::headerChangedSlot()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate17headerChangedSlotEv')

  def synchronousHeaderChangedSlot(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::synchronousHeaderChangedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html
    """
    #  void QHttpThreadDelegate::synchronousHeaderChangedSlot()
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate28synchronousHeaderChangedSlotEv',
    )

  @overload(int, int)
  def dataReadProgressSlot(self, done: int, total: int) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::dataReadProgressSlot(qint64 done,
    qint64 total)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#dataReadProgressSlot

    Parameters
    ----------

    done : int
      Passed on as it is.

    total : int
      Passed on as it is.
    """
    #  void QHttpThreadDelegate::dataReadProgressSlot(qint64 done, qint64
    #      total)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate20dataReadProgressSlotExx',
        done, total,
    )

  @overload(QHttpNetworkRequest, QAuthenticator)
  @overload(QHttpNetworkRequest, NoneType)
  def cacheCredentialsSlot(
      self,
      request: QHttpNetworkRequest,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::cacheCredentialsSlot(const
    QHttpNetworkRequest &request, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#cacheCredentialsSlot

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::cacheCredentialsSlot(const
    #      QHttpNetworkRequest &request, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate20cacheCredentialsSlotERK19QHttpNetw'
        'orkRequestP14QAuthenticator',
        self._valueOf(request), self._addressOf(authenticator),
    )

  def encryptedSlot(self) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::encryptedSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#encryptedSlot
    """
    #  void QHttpThreadDelegate::encryptedSlot()
    self.uglySide.call('ritual_ZN19QHttpThreadDelegate13encryptedSlotEv')

  @overload(QList[QSslError])
  def sslErrorsSlot(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QHttpThreadDelegate::sslErrorsSlot(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html#sslErrorsSlot

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHttpThreadDelegate::sslErrorsSlot(const QList<QSslError>
    #      &errors)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate13sslErrorsSlotERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequiredSlot(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QHttpThreadDelegate::preSharedKeyAuthenticationRequiredSlot(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::preSharedKeyAuthenticationRequiredSlot(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate38preSharedKeyAuthenticationRequired'
        'SlotEP29QSslPreSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  @overload(QHttpNetworkRequest, QAuthenticator)
  @overload(QHttpNetworkRequest, NoneType)
  def synchronousAuthenticationRequiredSlot(
      self,
      request: QHttpNetworkRequest,
      a1: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QHttpThreadDelegate::synchronousAuthenticationRequiredSlot(const
    QHttpNetworkRequest &request, QAuthenticator *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    a1 : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::synchronousAuthenticationRequiredSlot(const
    #      QHttpNetworkRequest &request, QAuthenticator *a1)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate37synchronousAuthenticationRequiredS'
        'lotERK19QHttpNetworkRequestP14QAuthenticator',
        self._valueOf(request), self._addressOf(a1),
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def synchronousProxyAuthenticationRequiredSlot(
      self,
      a0: QNetworkProxy,
      a1: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QHttpThreadDelegate::synchronousProxyAuthenticationRequiredSlot(const
    QNetworkProxy &a0, QAuthenticator *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpthreaddelegate.html

    Parameters
    ----------

    a0 : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    a1 : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpThreadDelegate::synchronousProxyAuthenticationRequiredSlot(
    #      const QNetworkProxy &a0, QAuthenticator *a1)
    self.uglySide.call(
        'ritual_ZN19QHttpThreadDelegate42synchronousProxyAuthenticationRequ'
        'iredSlotERK13QNetworkProxyP14QAuthenticator',
        self._valueOf(a0), self._addressOf(a1),
    )

  @staticmethod
  def downloadMetaData(*__, **_) -> Never:
    """
    Qt's 'void QHttpThreadDelegate::downloadMetaData(const QHttpHeaders &a0,
    int a1, const QString &a2, bool a3, QSharedPointer<char> a4, qint64 a5,
    qint64 a6, bool a7, bool a8)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QHttpThreadDelegate.downloadMetaData' has no cute function yet. "
        "Qt's 'void QHttpThreadDelegate::downloadMetaData(const "
        "QHttpHeaders &a0, int a1, const QString &a2, bool a3, "
        "QSharedPointer<char> a4, qint64 a5, qint64 a6, bool a7, bool a8)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def sslErrors(*__, **_) -> Never:
    """
    Qt's 'void QHttpThreadDelegate::sslErrors(const QList<QSslError> &a0,
    bool *a1, QList<QSslError> *a2)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QHttpThreadDelegate.sslErrors' has no cute function yet. Qt's "
        "'void QHttpThreadDelegate::sslErrors(const QList<QSslError> &a0, "
        "bool *a1, QList<QSslError> *a2)': takes a number to change where "
        "it is.")
