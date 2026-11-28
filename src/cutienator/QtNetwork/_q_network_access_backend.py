"""
QNetworkAccessBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessbackend_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkAccessBackend to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QNetworkAccessManager, QNetworkReply, QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QIODevice, QMetaObject
  from ..QtCore import QUrl, QVariant
  from . import QAbstractNetworkCache, QAuthenticator, QHttpHeaders
  from . import QNetworkAccessManagerPrivate, QNetworkProxy
  from . import QNetworkReplyImplPrivate, QSslConfiguration, QSslError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QByteArray = WAIT['QByteArray']
  QHttpHeaders = WAIT['QHttpHeaders']
  QNetworkAccessManagerPrivate = WAIT['QNetworkAccessManagerPrivate']
  QNetworkProxy = WAIT['QNetworkProxy']
  QNetworkReplyImplPrivate = WAIT['QNetworkReplyImplPrivate']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkAccessBackend(QObject):
  """
  The cute side of Qt's QNetworkAccessBackend: a plain Python object standing
  in front of one C++ QNetworkAccessBackend.

  It is built on the cute 'QObject', as Qt's QNetworkAccessBackend is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessBackend that has a ritual and that
  Python can call so far, 43 names in all: 'metaObject', 'tr',
  'securityFeatures', 'targetTypes', 'ioFeatures',
  'needsResetableUploadData', 'start', 'open', 'close',
  'setSslConfiguration', 'sslConfiguration', 'ignoreSslErrors',
  'bytesAvailable', 'readPointer', 'advanceReadPointer', 'wantToRead',
  'proxyList', 'url', 'setUrl', 'header', 'setHeader', 'rawHeader',
  'setRawHeader', 'headers', 'setHeaders', 'operation', 'isCachingEnabled',
  'setCachingEnabled', 'setAttribute', 'createUploadByteDevice',
  'uploadByteDevice', 'networkCache', 'readyRead', 'finished', 'error',
  'proxyAuthenticationRequired', 'authenticationRequired', 'metaDataChanged',
  'redirectionRequested', 'setReplyPrivate', 'setManagerPrivate',
  'isSynchronous', 'setSynchronous'. It can be made from Python, in 4 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkAccessBackend::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QNetworkAccessBackend::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkAccessBackendPrivate *QNetworkAccessBackend::d_func()':
    gives 'QNetworkAccessBackendPrivate', which has no cute class yet.
  - Qt's 'const QNetworkAccessBackendPrivate *QNetworkAccessBackend::d_func()
    const': gives 'QNetworkAccessBackendPrivate', which has no cute class
    yet.
  - Qt's 'QNetworkAccessBackend::~QNetworkAccessBackend()': the destructor:
    Python never removes a C++ QNetworkAccessBackend.
  - Qt's 'qint64 QNetworkAccessBackend::read(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'void QNetworkAccessBackend::setHeaders(QHttpHeaders &&newHeaders)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 57 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkAccessBackend is created at the first use, not by
    'QNetworkAccessBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessBackend.
  - Qt tells when it has removed the C++ QNetworkAccessBackend. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkAccessBackend that has no cute function yet,
    'read', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QNetworkAccessBackend, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class IOFeature(CuteFlags, scoped=True):
    """
    The flags enum 'QNetworkAccessBackend::IOFeature' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QNetworkAccessBackend::IOFeatures'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    ZeroCopy = 0x1
    NeedResetableUpload = 0x2
    SupportsSynchronousMode = 0x4

  IOFeatures = IOFeature

  class SecurityFeature(CuteFlags, scoped=True):
    """
    The flags enum 'QNetworkAccessBackend::SecurityFeature' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QNetworkAccessBackend::SecurityFeatures'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    TLS = 0x1

  SecurityFeatures = SecurityFeature

  class TargetType(CuteFlags, scoped=True):
    """
    The flags enum 'QNetworkAccessBackend::TargetType' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QNetworkAccessBackend::TargetTypes'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Networked = 0x1
    Local = 0x2

  TargetTypes = TargetType

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
    Calls Qt's 'QString QNetworkAccessBackend::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#tr

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
    #  QString QNetworkAccessBackend::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QNetworkAccessBackend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessBackend'

  #  A C++ QNetworkAccessBackend Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessBackend'

  #  The functions Qt calls itself that QNetworkAccessBackend is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'read': (
          'qint64 QNetworkAccessBackend::read(char *, qint64)',
      ),
  }

  #  The functions Qt calls itself that QNetworkAccessBackend is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'start': (
          ('_ZN21QNetworkAccessBackend5startEv',
           ('bool', 'number', ''),
           ()),
      ),
      'open': (
          ('_ZN21QNetworkAccessBackend4openEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'close': (
          ('_ZN21QNetworkAccessBackend5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setSslConfiguration': (
          ('_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfigu'
           'ration',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QSslConfiguration'),
           )),
      ),
      'sslConfiguration': (
          ('_ZNK21QNetworkAccessBackend16sslConfigurationEv',
           ('address', 'value', 'QtNetwork:QSslConfiguration'),
           ()),
      ),
      'ignoreSslErrors': (
          ('_ZN21QNetworkAccessBackend15ignoreSslErrorsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bytesAvailable': (
          ('_ZNK21QNetworkAccessBackend14bytesAvailableEv',
           ('long long', 'number', ''),
           ()),
      ),
      'readPointer': (
          ('_ZN21QNetworkAccessBackend11readPointerEv',
           ('address', 'value', 'QtCore:QByteArrayView'),
           ()),
      ),
      'advanceReadPointer': (
          ('_ZN21QNetworkAccessBackend18advanceReadPointerEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'wantToRead': (
          ('_ZN21QNetworkAccessBackend10wantToReadEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkAccessBackend::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkAccessBackend::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def securityFeatures(self) -> SecurityFeatures:
    """
    Calls Qt's 'SecurityFeatures QNetworkAccessBackend::securityFeatures()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#securityFeatures

    Returns
    -------

    SecurityFeatures
      The value standing for the combination Qt gave back.
    """
    #  SecurityFeatures QNetworkAccessBackend::securityFeatures() const
    return QNetworkAccessBackend.SecurityFeatures(self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend16securityFeaturesEv',
    ))

  def targetTypes(self) -> TargetTypes:
    """
    Calls Qt's 'TargetTypes QNetworkAccessBackend::targetTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#targetTypes

    Returns
    -------

    TargetTypes
      The value standing for the combination Qt gave back.
    """
    #  TargetTypes QNetworkAccessBackend::targetTypes() const
    return QNetworkAccessBackend.TargetTypes(self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend11targetTypesEv',
    ))

  def ioFeatures(self) -> IOFeatures:
    """
    Calls Qt's 'IOFeatures QNetworkAccessBackend::ioFeatures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#ioFeatures

    Returns
    -------

    IOFeatures
      The value standing for the combination Qt gave back.
    """
    #  IOFeatures QNetworkAccessBackend::ioFeatures() const
    return QNetworkAccessBackend.IOFeatures(self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend10ioFeaturesEv',
    ))

  def needsResetableUploadData(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessBackend::needsResetableUploadData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html
    """
    #  bool QNetworkAccessBackend::needsResetableUploadData() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend24needsResetableUploadDataEv',
    )

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QNetworkAccessBackend::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
    ritual = 'ritual_ZNK21QNetworkAccessBackend16sslConfigurationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QNetworkAccessBackend16sslConfigurationEv'
    address = self.uglySide.call(ritual)
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkAccessBackend::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#bytesAvailable
    """
    #  qint64 QNetworkAccessBackend::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend14bytesAvailableEv',
    )

  def proxyList(self) -> QList[QNetworkProxy]:
    """
    Calls Qt's 'QList<QNetworkProxy> QNetworkAccessBackend::proxyList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#proxyList

    Returns
    -------

    QList[QNetworkProxy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkProxy> QNetworkAccessBackend::proxyList() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend9proxyListEv',
    )
    from . import QNetworkProxy
    return QList[QNetworkProxy]._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNetworkAccessBackend::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNetworkAccessBackend::url() const
    address = self.uglySide.call('ritual_ZNK21QNetworkAccessBackend3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QNetworkRequest.KnownHeaders)
  def header(self, header: QNetworkRequest.KnownHeaders) -> QVariant:
    """
    Calls Qt's 'QVariant
    QNetworkAccessBackend::header(QNetworkRequest::KnownHeaders header)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#header

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNetworkAccessBackend::header(QNetworkRequest::KnownHeaders
    #      header) const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend6headerEN15QNetworkRequest12Known'
        'HeadersE',
        header.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QByteArray)
  def rawHeader(self, header: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkAccessBackend::rawHeader(const QByteArray
    &header) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#rawHeader

    Parameters
    ----------

    header : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkAccessBackend::rawHeader(const QByteArray &header)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend9rawHeaderERK10QByteArray',
        self._valueOf(header),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkAccessBackend::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkAccessBackend::headers() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend7headersEv',
    )
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  def operation(self) -> QNetworkAccessManager.Operation:
    """
    Calls Qt's 'QNetworkAccessManager::Operation
    QNetworkAccessBackend::operation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#operation

    Returns
    -------

    QNetworkAccessManager.Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QNetworkAccessManager.Operation(number)' gives.
    """
    #  QNetworkAccessManager::Operation QNetworkAccessBackend::operation()
    #      const
    return QNetworkAccessManager.Operation(self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend9operationEv',
    ))

  def isCachingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessBackend::isCachingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#isCachingEnabled
    """
    #  bool QNetworkAccessBackend::isCachingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend16isCachingEnabledEv',
    )

  def networkCache(self) -> Optional[QAbstractNetworkCache]:
    """
    Calls Qt's 'QAbstractNetworkCache *QNetworkAccessBackend::networkCache()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#networkCache

    Returns
    -------

    Optional[QAbstractNetworkCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractNetworkCache *QNetworkAccessBackend::networkCache() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend12networkCacheEv',
    )
    from . import QAbstractNetworkCache
    return QAbstractNetworkCache._cuteAt(address)

  def isSynchronous(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessBackend::isSynchronous() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#isSynchronous
    """
    #  bool QNetworkAccessBackend::isSynchronous() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkAccessBackend13isSynchronousEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSslConfiguration)
  def setSslConfiguration(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::setSslConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setSslConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkAccessBackend::setSslConfiguration(const
    #      QSslConfiguration &configuration)
    ritual = (
        'ritual_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConf'
        'iguration')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QNetworkAccessBackend19setSslConfigurationERK17QS'
          'slConfiguration')
    self.uglySide.call(ritual, self._valueOf(configuration))

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkAccessBackend::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend6setUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QNetworkRequest.KnownHeaders, QVariant)
  def setHeader(
      self,
      header: QNetworkRequest.KnownHeaders,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessBackend::setHeader(QNetworkRequest::KnownHeaders header,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setHeader

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkAccessBackend::setHeader(QNetworkRequest::KnownHeaders
    #      header, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend9setHeaderEN15QNetworkRequest12Kno'
        'wnHeadersERK8QVariant',
        header.value, self._valueOf(value),
    )

  @overload(QByteArray, QByteArray)
  def setRawHeader(self, header: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::setRawHeader(const QByteArray
    &header, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setRawHeader

    Parameters
    ----------

    header : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkAccessBackend::setRawHeader(const QByteArray &header,
    #      const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend12setRawHeaderERK10QByteArrayS2_',
        self._valueOf(header), self._valueOf(value),
    )

  @overload(QHttpHeaders)
  def setHeaders(self, newHeaders: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::setHeaders(const QHttpHeaders
    &newHeaders)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setHeaders

    Parameters
    ----------

    newHeaders : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QNetworkAccessBackend::setHeaders(const QHttpHeaders &newHeaders)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend10setHeadersERK12QHttpHeaders',
        self._valueOf(newHeaders),
    )

  @overload(bool)
  def setCachingEnabled(self, canCache: bool) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::setCachingEnabled(bool
    canCache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setCachingEnabled

    Parameters
    ----------

    canCache : bool
      Passed on as it is.
    """
    #  void QNetworkAccessBackend::setCachingEnabled(bool canCache)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend17setCachingEnabledEb', canCache,
    )

  @overload(QNetworkRequest.Attribute, QVariant)
  def setAttribute(
      self,
      attribute: QNetworkRequest.Attribute,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessBackend::setAttribute(QNetworkRequest::Attribute attribute,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setAttribute

    Parameters
    ----------

    attribute : QNetworkRequest.Attribute
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QNetworkAccessBackend::setAttribute(QNetworkRequest::Attribute
    #      attribute, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend12setAttributeEN15QNetworkRequest9'
        'AttributeERK8QVariant',
        attribute.value, self._valueOf(value),
    )

  @overload(QNetworkReplyImplPrivate)
  @overload(NoneType)
  def setReplyPrivate(
      self,
      reply: Optional[QNetworkReplyImplPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessBackend::setReplyPrivate(QNetworkReplyImplPrivate *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setReplyPrivate

    Parameters
    ----------

    reply : Optional[QNetworkReplyImplPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessBackend::setReplyPrivate(QNetworkReplyImplPrivate
    #      *reply)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend15setReplyPrivateEP24QNetworkReply'
        'ImplPrivate',
        self._addressOf(reply),
    )

  @overload(QNetworkAccessManagerPrivate)
  @overload(NoneType)
  def setManagerPrivate(
      self,
      manager: Optional[QNetworkAccessManagerPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessBackend::setManagerPrivate(QNetworkAccessManagerPrivate
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setManagerPrivate

    Parameters
    ----------

    manager : Optional[QNetworkAccessManagerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessBackend::setManagerPrivate(
    #      QNetworkAccessManagerPrivate *manager)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend17setManagerPrivateEP28QNetworkAcc'
        'essManagerPrivate',
        self._addressOf(manager),
    )

  @overload(bool)
  def setSynchronous(self, synchronous: bool) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::setSynchronous(bool
    synchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#setSynchronous

    Parameters
    ----------

    synchronous : bool
      Passed on as it is.
    """
    #  void QNetworkAccessBackend::setSynchronous(bool synchronous)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend14setSynchronousEb', synchronous,
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

  @overload(TargetTypes, SecurityFeatures, IOFeatures)
  def __init__(
      self,
      targetTypes: TargetTypes,
      securityFeatures: SecurityFeatures,
      ioFeatures: IOFeatures,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes,
    SecurityFeatures securityFeatures, IOFeatures ioFeatures)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#QNetworkAccessBackend

    Parameters
    ----------

    targetTypes : TargetTypes
      Passed on as its number.

    securityFeatures : SecurityFeatures
      Passed on as its number.

    ioFeatures : IOFeatures
      Passed on as its number.
    """
    #  QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes,
    #      SecurityFeatures securityFeatures, IOFeatures ioFeatures)
    self._noteCreation(QNetworkAccessBackend, lambda: Rituals.call(
        'ritual_ZN21QNetworkAccessBackendC1E6QFlagsINS_10TargetTypeEES0_INS'
        '_15SecurityFeatureEES0_INS_9IOFeatureEE',
        targetTypes.value, securityFeatures.value, ioFeatures.value,
    ))

  @overload(TargetTypes)
  def __init__(self, targetTypes: TargetTypes) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#QNetworkAccessBackend

    Parameters
    ----------

    targetTypes : TargetTypes
      Passed on as its number.
    """
    #  QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes)
    self._noteCreation(QNetworkAccessBackend, lambda: Rituals.call(
        'ritual_ZN21QNetworkAccessBackendC1E6QFlagsINS_10TargetTypeEE',
        targetTypes.value,
    ))

  @overload(TargetTypes, SecurityFeatures)
  def __init__(
      self,
      targetTypes: TargetTypes,
      securityFeatures: SecurityFeatures,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes,
    SecurityFeatures securityFeatures)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#QNetworkAccessBackend

    Parameters
    ----------

    targetTypes : TargetTypes
      Passed on as its number.

    securityFeatures : SecurityFeatures
      Passed on as its number.
    """
    #  QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes,
    #      SecurityFeatures securityFeatures)
    self._noteCreation(QNetworkAccessBackend, lambda: Rituals.call(
        'ritual_ZN21QNetworkAccessBackendC1E6QFlagsINS_10TargetTypeEES0_INS'
        '_15SecurityFeatureEE',
        targetTypes.value, securityFeatures.value,
    ))

  @overload(TargetTypes, IOFeatures)
  def __init__(
      self,
      targetTypes: TargetTypes,
      ioFeatures: IOFeatures,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes,
    IOFeatures ioFeatures)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#QNetworkAccessBackend

    Parameters
    ----------

    targetTypes : TargetTypes
      Passed on as its number.

    ioFeatures : IOFeatures
      Passed on as its number.
    """
    #  QNetworkAccessBackend::QNetworkAccessBackend(TargetTypes targetTypes,
    #      IOFeatures ioFeatures)
    self._noteCreation(QNetworkAccessBackend, lambda: Rituals.call(
        'ritual_ZN21QNetworkAccessBackendC1E6QFlagsINS_10TargetTypeEES0_INS'
        '_9IOFeatureEE',
        targetTypes.value, ioFeatures.value,
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

  def start(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessBackend::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#start
    """
    #  bool QNetworkAccessBackend::start()
    ritual = 'ritual_ZN21QNetworkAccessBackend5startEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkAccessBackend5startEv'
    return self.uglySide.call(ritual)

  def open(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#open
    """
    #  void QNetworkAccessBackend::open()
    self.uglySide.call('ritual_ZN21QNetworkAccessBackend4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#close
    """
    #  void QNetworkAccessBackend::close()
    self.uglySide.call('ritual_ZN21QNetworkAccessBackend5closeEv')

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::ignoreSslErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#ignoreSslErrors
    """
    #  void QNetworkAccessBackend::ignoreSslErrors()
    ritual = 'ritual_ZN21QNetworkAccessBackend15ignoreSslErrorsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkAccessBackend15ignoreSslErrorsEv'
    self.uglySide.call(ritual)

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::ignoreSslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkAccessBackend::ignoreSslErrors(const QList<QSslError>
    #      &errors)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend15ignoreSslErrorsERK5QListI9QSslEr'
        'rorE',
        self._valueOf(errors),
    )

  def readPointer(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QNetworkAccessBackend::readPointer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#readPointer

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QNetworkAccessBackend::readPointer()
    ritual = 'ritual_ZN21QNetworkAccessBackend11readPointerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkAccessBackend11readPointerEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  @overload(int)
  def advanceReadPointer(self, distance: int) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::advanceReadPointer(qint64
    distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#advanceReadPointer

    Parameters
    ----------

    distance : int
      Passed on as it is.
    """
    #  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
    ritual = 'ritual_ZN21QNetworkAccessBackend18advanceReadPointerEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkAccessBackend18advanceReadPointerEx'
    self.uglySide.call(ritual, distance)

  def wantToRead(self) -> bool:
    """
    Calls Qt's 'bool QNetworkAccessBackend::wantToRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#wantToRead
    """
    #  bool QNetworkAccessBackend::wantToRead()
    ritual = 'ritual_ZN21QNetworkAccessBackend10wantToReadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QNetworkAccessBackend10wantToReadEv'
    return self.uglySide.call(ritual)

  def createUploadByteDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QNetworkAccessBackend::createUploadByteDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#createUploadByteDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QNetworkAccessBackend::createUploadByteDevice()
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend22createUploadByteDeviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def uploadByteDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QNetworkAccessBackend::uploadByteDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#uploadByteDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QNetworkAccessBackend::uploadByteDevice()
    address = self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend16uploadByteDeviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def readyRead(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#readyRead
    """
    #  void QNetworkAccessBackend::readyRead()
    self.uglySide.call('ritual_ZN21QNetworkAccessBackend9readyReadEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#finished
    """
    #  void QNetworkAccessBackend::finished()
    self.uglySide.call('ritual_ZN21QNetworkAccessBackend8finishedEv')

  @overload(QNetworkReply.NetworkError, str)
  def error(
      self,
      code: QNetworkReply.NetworkError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::error(QNetworkReply::NetworkError
    code, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkaccessbackend.html#error

    Parameters
    ----------

    code : QNetworkReply.NetworkError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkAccessBackend::error(QNetworkReply::NetworkError code,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend5errorEN13QNetworkReply12NetworkEr'
        'rorERK7QString',
        code.value, errorString,
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      auth: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *auth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    auth : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessBackend::proxyAuthenticationRequired(const
    #      QNetworkProxy &proxy, QAuthenticator *auth)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend27proxyAuthenticationRequiredERK13'
        'QNetworkProxyP14QAuthenticator',
        self._valueOf(proxy), self._addressOf(auth),
    )

  @overload(QAuthenticator)
  @overload(NoneType)
  def authenticationRequired(self, auth: Optional[QAuthenticator]) -> None:
    """
    Calls Qt's 'void
    QNetworkAccessBackend::authenticationRequired(QAuthenticator *auth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#authenticationRequired

    Parameters
    ----------

    auth : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QNetworkAccessBackend::authenticationRequired(QAuthenticator
    #      *auth)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend22authenticationRequiredEP14QAuthe'
        'nticator',
        self._addressOf(auth),
    )

  def metaDataChanged(self) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::metaDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#metaDataChanged
    """
    #  void QNetworkAccessBackend::metaDataChanged()
    self.uglySide.call('ritual_ZN21QNetworkAccessBackend15metaDataChangedEv')

  @overload(QUrl)
  def redirectionRequested(self, destination: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkAccessBackend::redirectionRequested(const QUrl
    &destination)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessbackend.html#redirectionRequested

    Parameters
    ----------

    destination : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkAccessBackend::redirectionRequested(const QUrl
    #      &destination)
    self.uglySide.call(
        'ritual_ZN21QNetworkAccessBackend20redirectionRequestedERK4QUrl',
        self._valueOf(destination),
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'qint64 QNetworkAccessBackend::read(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNetworkAccessBackend.read' has no cute function yet. Qt's "
        "'qint64 QNetworkAccessBackend::read(char *data, qint64 maxlen)': "
        "names 'char', which has no cute class yet.")
