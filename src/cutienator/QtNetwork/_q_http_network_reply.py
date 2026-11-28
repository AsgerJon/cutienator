"""
QHttpNetworkReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkreply_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkReply to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QHttpNetworkHeader, QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QMetaObject, QUrl
  from . import QAuthenticator, QHttpHeaders, QHttpNetworkConnection
  from . import QHttpNetworkReplyPrivate, QHttpNetworkRequest, QNetworkProxy
  from . import QSslConfiguration, QSslError, QSslPreSharedKeyAuthenticator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QHttpNetworkRequest = WAIT['QHttpNetworkRequest']
  QNetworkProxy = WAIT['QNetworkProxy']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpNetworkReply(QObject, QHttpNetworkHeader):
  """
  The cute side of Qt's QHttpNetworkReply: a plain Python object standing in
  front of one C++ QHttpNetworkReply.

  It is built on the cute 'QObject', as Qt's QHttpNetworkReply is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QHttpNetworkHeader' as well, as Qt's QHttpNetworkReply is built on Qt's
  QHttpNetworkHeader too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpNetworkReply that has a ritual and that Python
  can call so far, 66 names in all: 'metaObject', 'tr', 'url', 'setUrl',
  'majorVersion', 'minorVersion', 'setMajorVersion', 'setMinorVersion',
  'contentLength', 'setContentLength', 'header', 'headerField',
  'setHeaderField', 'appendHeaderField', 'parseHeader', 'request',
  'setRequest', 'statusCode', 'setStatusCode', 'errorString',
  'setErrorString', 'errorCode', 'reasonPhrase', 'setReasonPhrase',
  'bytesAvailable', 'bytesAvailableNextBlock', 'readAnyAvailable', 'readAny',
  'readAll', 'read', 'sizeNextBlock', 'setDownstreamLimited',
  'setReadBufferSize', 'supportsUserProvidedDownloadBuffer', 'abort',
  'isAborted', 'isFinished', 'isPipeliningUsed', 'isHttp2Used',
  'setHttp2WasUsed', 'removedContentLength', 'isRedirecting', 'connection',
  'redirectUrl', 'setRedirectUrl', 'isHttpRedirect', 'isCompressed',
  'sslConfiguration', 'setSslConfiguration', 'ignoreSslErrors', 'encrypted',
  'sslErrors', 'preSharedKeyAuthenticationRequired',
  'socketStartedConnecting', 'requestSent', 'readyRead', 'finished',
  'finishedWithError', 'headerChanged', 'dataReadProgress',
  'dataSendProgress', 'cacheCredentials', 'proxyAuthenticationRequired',
  'authenticationRequired', 'redirected', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpNetworkReply::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHttpNetworkReply::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHttpNetworkReply::~QHttpNetworkReply()': the destructor: Python
    never removes a C++ QHttpNetworkReply.
  - Qt's 'void QHttpNetworkReply::setUserProvidedDownloadBuffer(char *a0)':
    names 'char', which has no cute class yet.
  - Qt's 'char *QHttpNetworkReply::userProvidedDownloadBuffer()': gives
    'char', which has no cute class yet.
  - Qt's 'const QHttpNetworkReplyPrivate *QHttpNetworkReply::d_func() const':
    takes in Python what 'QHttpNetworkReplyPrivate
    *QHttpNetworkReply::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 76 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHttpNetworkReply is created at the first use, not by
    'QHttpNetworkReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpNetworkReply.
  - Qt tells when it has removed the C++ QHttpNetworkReply. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpNetworkReply that has no cute function yet,
    'setUserProvidedDownloadBuffer', 'userProvidedDownloadBuffer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QHttpNetworkReply::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#tr

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
    #  QString QHttpNetworkReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QHttpNetworkReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int)
  def isHttpRedirect(statusCode: int) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isHttpRedirect(int statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#isHttpRedirect

    Parameters
    ----------

    statusCode : int
      Passed on as it is.
    """
    #  bool QHttpNetworkReply::isHttpRedirect(int statusCode)
    return Rituals.call(
        'ritual_ZN17QHttpNetworkReply14isHttpRedirectEi', statusCode,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkReply'

  #  Qt's QHttpNetworkReply is built on more than one class. The part of a
  #  C++ QHttpNetworkReply that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QHttpNetworkHeader':
          'ritual_cast_QHttpNetworkReply_QHttpNetworkHeader',
  }

  #  A C++ QHttpNetworkReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpNetworkReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttpNetworkReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpNetworkReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHttpNetworkReply::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHttpNetworkReply::url() const
    ritual = 'ritual_ZNK17QHttpNetworkReply3urlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpNetworkReply3urlEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkReply::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#majorVersion
    """
    #  int QHttpNetworkReply::majorVersion() const
    ritual = 'ritual_ZNK17QHttpNetworkReply12majorVersionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpNetworkReply12majorVersionEv'
    return self.uglySide.call(ritual)

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkReply::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#minorVersion
    """
    #  int QHttpNetworkReply::minorVersion() const
    ritual = 'ritual_ZNK17QHttpNetworkReply12minorVersionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpNetworkReply12minorVersionEv'
    return self.uglySide.call(ritual)

  def contentLength(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReply::contentLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#contentLength
    """
    #  qint64 QHttpNetworkReply::contentLength() const
    ritual = 'ritual_ZNK17QHttpNetworkReply13contentLengthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpNetworkReply13contentLengthEv'
    return self.uglySide.call(ritual)

  def header(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QHttpNetworkReply::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#header

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QHttpNetworkReply::header() const
    ritual = 'ritual_ZNK17QHttpNetworkReply6headerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QHttpNetworkReply6headerEv'
    address = self.uglySide.call(ritual)
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  @overload(QByteArrayView)
  @overload(QByteArrayView, QByteArray)
  def headerField(
      self,
      name: QByteArrayView,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkReply::headerField(QByteArrayView
    name, const QByteArray &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#headerField

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    defaultValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkReply::headerField(QByteArrayView name, const
    #      QByteArray &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArray
      defaultValue = QByteArray()
    ritual = (
        'ritual_ZNK17QHttpNetworkReply11headerFieldE14QByteArrayViewRK10QBy'
        'teArray')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QHttpNetworkReply11headerFieldE14QByteArrayViewR'
          'K10QByteArray')
    address = self.uglySide.call(
        ritual, self._valueOf(name), self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def request(self) -> QHttpNetworkRequest:
    """
    Calls Qt's 'QHttpNetworkRequest QHttpNetworkReply::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#request

    Returns
    -------

    QHttpNetworkRequest
      A new cute QHttpNetworkRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QHttpNetworkRequest QHttpNetworkReply::request() const
    address = self.uglySide.call('ritual_ZNK17QHttpNetworkReply7requestEv')
    from . import QHttpNetworkRequest
    return QHttpNetworkRequest._cuteOwning(address)

  def statusCode(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkReply::statusCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#statusCode
    """
    #  int QHttpNetworkReply::statusCode() const
    return self.uglySide.call('ritual_ZNK17QHttpNetworkReply10statusCodeEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QHttpNetworkReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkReply::errorString() const
    return self.uglySide.call('ritual_ZNK17QHttpNetworkReply11errorStringEv')

  def errorCode(self) -> QNetworkReply.NetworkError:
    """
    Calls Qt's 'QNetworkReply::NetworkError QHttpNetworkReply::errorCode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#errorCode

    Returns
    -------

    QNetworkReply.NetworkError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkReply.NetworkError(number)' gives.
    """
    #  QNetworkReply::NetworkError QHttpNetworkReply::errorCode() const
    return QNetworkReply.NetworkError(self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply9errorCodeEv',
    ))

  def reasonPhrase(self) -> str:
    """
    Calls Qt's 'QString QHttpNetworkReply::reasonPhrase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#reasonPhrase

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkReply::reasonPhrase() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply12reasonPhraseEv',
    )

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReply::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#bytesAvailable
    """
    #  qint64 QHttpNetworkReply::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply14bytesAvailableEv',
    )

  def bytesAvailableNextBlock(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReply::bytesAvailableNextBlock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#bytesAvailableNextBlock
    """
    #  qint64 QHttpNetworkReply::bytesAvailableNextBlock() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply23bytesAvailableNextBlockEv',
    )

  def readAnyAvailable(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::readAnyAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#readAnyAvailable
    """
    #  bool QHttpNetworkReply::readAnyAvailable() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply16readAnyAvailableEv',
    )

  def isAborted(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isAborted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#isAborted
    """
    #  bool QHttpNetworkReply::isAborted() const
    return self.uglySide.call('ritual_ZNK17QHttpNetworkReply9isAbortedEv')

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#isFinished
    """
    #  bool QHttpNetworkReply::isFinished() const
    return self.uglySide.call('ritual_ZNK17QHttpNetworkReply10isFinishedEv')

  def isPipeliningUsed(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isPipeliningUsed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#isPipeliningUsed
    """
    #  bool QHttpNetworkReply::isPipeliningUsed() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply16isPipeliningUsedEv',
    )

  def isHttp2Used(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isHttp2Used() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#isHttp2Used
    """
    #  bool QHttpNetworkReply::isHttp2Used() const
    return self.uglySide.call('ritual_ZNK17QHttpNetworkReply11isHttp2UsedEv')

  def removedContentLength(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReply::removedContentLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#removedContentLength
    """
    #  qint64 QHttpNetworkReply::removedContentLength() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply20removedContentLengthEv',
    )

  def isRedirecting(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isRedirecting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#isRedirecting
    """
    #  bool QHttpNetworkReply::isRedirecting() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply13isRedirectingEv',
    )

  def redirectUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHttpNetworkReply::redirectUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#redirectUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHttpNetworkReply::redirectUrl() const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply11redirectUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isCompressed(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkReply::isCompressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#isCompressed
    """
    #  bool QHttpNetworkReply::isCompressed() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply12isCompressedEv',
    )

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QHttpNetworkReply::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QHttpNetworkReply::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpNetworkReply16sslConfigurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHttpNetworkReply::setUrl(const QUrl &url)
    ritual = 'ritual_ZN17QHttpNetworkReply6setUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QHttpNetworkReply6setUrlERK4QUrl'
    self.uglySide.call(ritual, self._valueOf(url))

  @overload(int)
  def setMajorVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setMajorVersion(int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setMajorVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setMajorVersion(int version)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply15setMajorVersionEi', version,
    )

  @overload(int)
  def setMinorVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setMinorVersion(int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setMinorVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setMinorVersion(int version)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply15setMinorVersionEi', version,
    )

  @overload(int)
  def setContentLength(self, length: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setContentLength(qint64 length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setContentLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setContentLength(qint64 length)
    ritual = 'ritual_ZN17QHttpNetworkReply16setContentLengthEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QHttpNetworkReply16setContentLengthEx'
    self.uglySide.call(ritual, length)

  @overload(QByteArray, QByteArray)
  def setHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkReply::setHeaderField(const QByteArray &name, const
    #      QByteArray &data)
    ritual = 'ritual_ZN17QHttpNetworkReply14setHeaderFieldERK10QByteArrayS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QHttpNetworkReply14setHeaderFieldERK10QByteArrayS'
          '2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(data))

  @overload(QHttpNetworkRequest)
  def setRequest(self, request: QHttpNetworkRequest) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setRequest(const QHttpNetworkRequest
    &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#setRequest

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.
    """
    #  void QHttpNetworkReply::setRequest(const QHttpNetworkRequest &request)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply10setRequestERK19QHttpNetworkRequest',
        self._valueOf(request),
    )

  @overload(int)
  def setStatusCode(self, code: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setStatusCode(int code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setStatusCode

    Parameters
    ----------

    code : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setStatusCode(int code)
    self.uglySide.call('ritual_ZN17QHttpNetworkReply13setStatusCodeEi', code)

  @overload(str)
  def setErrorString(self, error: str) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setErrorString(const QString
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setErrorString

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpNetworkReply::setErrorString(const QString &error)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply14setErrorStringERK7QString', error,
    )

  @overload(str)
  def setReasonPhrase(self, reason: str) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setReasonPhrase(const QString
    &reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setReasonPhrase

    Parameters
    ----------

    reason : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpNetworkReply::setReasonPhrase(const QString &reason)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply15setReasonPhraseERK7QString', reason,
    )

  @overload(bool)
  def setDownstreamLimited(self, t: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setDownstreamLimited(bool t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setDownstreamLimited

    Parameters
    ----------

    t : bool
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setDownstreamLimited(bool t)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply20setDownstreamLimitedEb', t,
    )

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setReadBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setReadBufferSize(qint64 size)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply17setReadBufferSizeEx', size,
    )

  @overload(bool)
  def setHttp2WasUsed(self, h2Used: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setHttp2WasUsed(bool h2Used)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setHttp2WasUsed

    Parameters
    ----------

    h2Used : bool
      Passed on as it is.
    """
    #  void QHttpNetworkReply::setHttp2WasUsed(bool h2Used)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply15setHttp2WasUsedEb', h2Used,
    )

  @overload(QUrl)
  def setRedirectUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setRedirectUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setRedirectUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHttpNetworkReply::setRedirectUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply14setRedirectUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, config: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::setSslConfiguration(const
    QSslConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#setSslConfiguration

    Parameters
    ----------

    config : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QHttpNetworkReply::setSslConfiguration(const QSslConfiguration
    #      &config)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply19setSslConfigurationERK17QSslConfigur'
        'ation',
        self._valueOf(config),
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
  @overload(QUrl)
  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def __init__(
      self,
      url: Optional[QUrl] = None,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkReply::QHttpNetworkReply(const QUrl &url, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#QHttpNetworkReply

    Parameters
    ----------

    url : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHttpNetworkReply::QHttpNetworkReply(const QUrl &url, QObject *parent)
    if url is None:
      from ..QtCore import QUrl
      url = QUrl()
    self._noteCreation(QHttpNetworkReply, lambda: Rituals.call(
        'ritual_ZN17QHttpNetworkReplyC1ERK4QUrlP7QObject',
        self._valueOf(url), self._addressOf(parent, 'QObject'),
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

  @overload(QByteArray, QByteArray)
  def appendHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::appendHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#appendHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkReply::appendHeaderField(const QByteArray &name,
    #      const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply17appendHeaderFieldERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(data),
    )

  @overload(QByteArrayView)
  def parseHeader(self, header: QByteArrayView) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::parseHeader(QByteArrayView header)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#parseHeader

    Parameters
    ----------

    header : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QHttpNetworkReply::parseHeader(QByteArrayView header)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply11parseHeaderE14QByteArrayView',
        self._valueOf(header),
    )

  def readAny(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkReply::readAny()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#readAny

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkReply::readAny()
    address = self.uglySide.call('ritual_ZN17QHttpNetworkReply7readAnyEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def readAll(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkReply::readAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#readAll

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkReply::readAll()
    address = self.uglySide.call('ritual_ZN17QHttpNetworkReply7readAllEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def read(self, amount: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkReply::read(qint64 amount)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#read

    Parameters
    ----------

    amount : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkReply::read(qint64 amount)
    address = self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply4readEx', amount,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def sizeNextBlock(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkReply::sizeNextBlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#sizeNextBlock
    """
    #  qint64 QHttpNetworkReply::sizeNextBlock()
    return self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply13sizeNextBlockEv',
    )

  def supportsUserProvidedDownloadBuffer(self) -> bool:
    """
    Calls Qt's 'bool
    QHttpNetworkReply::supportsUserProvidedDownloadBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html
    """
    #  bool QHttpNetworkReply::supportsUserProvidedDownloadBuffer()
    return self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply34supportsUserProvidedDownloadBufferEv',
    )

  def abort(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#abort
    """
    #  void QHttpNetworkReply::abort()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply5abortEv')

  def connection(self) -> Optional[QHttpNetworkConnection]:
    """
    Calls Qt's 'QHttpNetworkConnection *QHttpNetworkReply::connection()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#connection

    Returns
    -------

    Optional[QHttpNetworkConnection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkConnection *QHttpNetworkReply::connection()
    address = self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply10connectionEv',
    )
    from . import QHttpNetworkConnection
    return QHttpNetworkConnection._cuteAt(address)

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::ignoreSslErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#ignoreSslErrors
    """
    #  void QHttpNetworkReply::ignoreSslErrors()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply15ignoreSslErrorsEv')

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::ignoreSslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHttpNetworkReply::ignoreSslErrors(const QList<QSslError>
    #      &errors)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply15ignoreSslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  def encrypted(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::encrypted()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#encrypted
    """
    #  void QHttpNetworkReply::encrypted()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply9encryptedEv')

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::sslErrors(const QList<QSslError>
    &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHttpNetworkReply::sslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply9sslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkReply::preSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply34preSharedKeyAuthenticationRequiredEP'
        '29QSslPreSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  def socketStartedConnecting(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::socketStartedConnecting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#socketStartedConnecting
    """
    #  void QHttpNetworkReply::socketStartedConnecting()
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply23socketStartedConnectingEv',
    )

  def requestSent(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::requestSent()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#requestSent
    """
    #  void QHttpNetworkReply::requestSent()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply11requestSentEv')

  def readyRead(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::readyRead()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#readyRead
    """
    #  void QHttpNetworkReply::readyRead()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply9readyReadEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#finished
    """
    #  void QHttpNetworkReply::finished()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply8finishedEv')

  @overload(QNetworkReply.NetworkError)
  @overload(QNetworkReply.NetworkError, str)
  def finishedWithError(
      self,
      errorCode: QNetworkReply.NetworkError,
      detail: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QHttpNetworkReply::finishedWithError(QNetworkReply::NetworkError
    errorCode, const QString &detail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#finishedWithError

    Parameters
    ----------

    errorCode : QNetworkReply.NetworkError
      Passed on as its number.

    detail : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QHttpNetworkReply::finishedWithError(QNetworkReply::NetworkError
    #      errorCode, const QString &detail)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply17finishedWithErrorEN13QNetworkReply12'
        'NetworkErrorERK7QString',
        errorCode.value, detail,
    )

  def headerChanged(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::headerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#headerChanged
    """
    #  void QHttpNetworkReply::headerChanged()
    self.uglySide.call('ritual_ZN17QHttpNetworkReply13headerChangedEv')

  @overload(int, int)
  def dataReadProgress(self, done: int, total: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::dataReadProgress(qint64 done, qint64
    total)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#dataReadProgress

    Parameters
    ----------

    done : int
      Passed on as it is.

    total : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::dataReadProgress(qint64 done, qint64 total)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply16dataReadProgressExx', done, total,
    )

  @overload(int, int)
  def dataSendProgress(self, done: int, total: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::dataSendProgress(qint64 done, qint64
    total)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#dataSendProgress

    Parameters
    ----------

    done : int
      Passed on as it is.

    total : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::dataSendProgress(qint64 done, qint64 total)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply16dataSendProgressExx', done, total,
    )

  @overload(QHttpNetworkRequest, QAuthenticator)
  @overload(QHttpNetworkRequest, NoneType)
  def cacheCredentials(
      self,
      request: QHttpNetworkRequest,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::cacheCredentials(const
    QHttpNetworkRequest &request, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#cacheCredentials

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkReply::cacheCredentials(const QHttpNetworkRequest
    #      &request, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply16cacheCredentialsERK19QHttpNetworkReq'
        'uestP14QAuthenticator',
        self._valueOf(request), self._addressOf(authenticator),
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#proxyAuthenticationRequired

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkReply::proxyAuthenticationRequired(const
    #      QNetworkProxy &proxy, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply27proxyAuthenticationRequiredERK13QNet'
        'workProxyP14QAuthenticator',
        self._valueOf(proxy), self._addressOf(authenticator),
    )

  @overload(QHttpNetworkRequest, QAuthenticator)
  @overload(QHttpNetworkRequest, NoneType)
  def authenticationRequired(
      self,
      request: QHttpNetworkRequest,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::authenticationRequired(const
    QHttpNetworkRequest &request, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkreply.html#authenticationRequired

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpNetworkReply::authenticationRequired(const
    #      QHttpNetworkRequest &request, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply22authenticationRequiredERK19QHttpNetw'
        'orkRequestP14QAuthenticator',
        self._valueOf(request), self._addressOf(authenticator),
    )

  @overload(QUrl, int, int)
  def redirected(
      self,
      url: QUrl,
      httpStatus: int,
      maxRedirectsRemaining: int,
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkReply::redirected(const QUrl &url, int
    httpStatus, int maxRedirectsRemaining)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#redirected

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    httpStatus : int
      Passed on as it is.

    maxRedirectsRemaining : int
      Passed on as it is.
    """
    #  void QHttpNetworkReply::redirected(const QUrl &url, int httpStatus,
    #      int maxRedirectsRemaining)
    self.uglySide.call(
        'ritual_ZN17QHttpNetworkReply10redirectedERK4QUrlii',
        self._valueOf(url), httpStatus, maxRedirectsRemaining,
    )

  def d_func(self) -> Optional[QHttpNetworkReplyPrivate]:
    """
    Calls Qt's 'QHttpNetworkReplyPrivate *QHttpNetworkReply::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkreply.html#d_func

    Returns
    -------

    Optional[QHttpNetworkReplyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkReplyPrivate *QHttpNetworkReply::d_func()
    address = self.uglySide.call('ritual_ZN17QHttpNetworkReply6d_funcEv')
    from . import QHttpNetworkReplyPrivate
    return QHttpNetworkReplyPrivate._cuteAt(address)

  @staticmethod
  def setUserProvidedDownloadBuffer(*__, **_) -> Never:
    """
    Qt's 'void QHttpNetworkReply::setUserProvidedDownloadBuffer(char *a0)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkReply.setUserProvidedDownloadBuffer' has no cute "
        "function yet. Qt's 'void "
        "QHttpNetworkReply::setUserProvidedDownloadBuffer(char *a0)': names "
        "'char', which has no cute class yet.")

  @staticmethod
  def userProvidedDownloadBuffer(*__, **_) -> Never:
    """
    Qt's 'char *QHttpNetworkReply::userProvidedDownloadBuffer()': gives
    'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkReply.userProvidedDownloadBuffer' has no cute "
        "function yet. Qt's 'char "
        "*QHttpNetworkReply::userProvidedDownloadBuffer()': gives 'char', "
        "which has no cute class yet.")
