"""
QOAuth1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qoauth1.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from ..QtNetwork import QNetworkAccessManager
from . import QAbstractOAuth

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
  from ..QtNetwork import QNetworkReply, QNetworkRequest
  from . import QOAuth1Private
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNetworkRequest = WAIT['QNetworkRequest']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuth1(QAbstractOAuth):
  """
  The cute side of Qt's QOAuth1: a plain Python object standing in front of
  one C++ QOAuth1.

  It is built on the cute 'QAbstractOAuth', as Qt's QOAuth1 is built on Qt's
  QAbstractOAuth, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuth1 that has a ritual and that Python can call
  so far, 32 names in all: 'metaObject', 'tr', 'clientSharedSecret',
  'setClientSharedSecret', 'setClientCredentials', 'tokenSecret',
  'setTokenSecret', 'setTokenCredentials', 'temporaryCredentialsUrl',
  'setTemporaryCredentialsUrl', 'tokenCredentialsUrl',
  'setTokenCredentialsUrl', 'signatureMethod', 'setSignatureMethod',
  'prepareRequest', 'head', 'get', 'post', 'put', 'deleteResource', 'grant',
  'continueGrantWithVerifier', 'signatureMethodChanged',
  'clientSharedSecretChanged', 'tokenSecretChanged',
  'temporaryCredentialsUrlChanged', 'tokenCredentialsUrlChanged',
  'requestTemporaryCredentials', 'setup', 'nonce',
  'generateAuthorizationHeader', 'd_func'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOAuth1::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QOAuth1::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'std::pair<QString, QString> QOAuth1::clientCredentials() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QOAuth1::setClientCredentials(const std::pair<QString,
    QString> &clientCredentials)': takes a type Python has no way to hand
    over yet.
  - Qt's 'std::pair<QString, QString> QOAuth1::tokenCredentials() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QOAuth1::setTokenCredentials(const std::pair<QString, QString>
    &tokenCredentials)': takes a type Python has no way to hand over yet.
  - Qt's 'QNetworkReply
    *QOAuth1::requestTokenCredentials(QNetworkAccessManager::Operation
    operation, const QUrl &url, const std::pair<QString, QString>
    &temporaryToken, const QVariantMap &parameters)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QOAuth1Private *QOAuth1::d_func() const': takes in Python
    what 'QOAuth1Private *QOAuth1::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 48 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOAuth1 is created at the first use, not by 'QOAuth1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuth1.
  - Qt tells when it has removed the C++ QOAuth1. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QOAuth1 that has no cute function yet,
    'clientCredentials', 'requestTokenCredentials', 'tokenCredentials', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOAuth1, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class SignatureMethod(CuteNum, scoped=True):
    """
    The enum 'QOAuth1::SignatureMethod' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Hmac_Sha1 = Kee[int](0)
    Rsa_Sha1 = Kee[int](1)
    PlainText = Kee[int](2)

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
    Calls Qt's 'QString QOAuth1::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#tr

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
    #  QString QOAuth1::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QOAuth12trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def nonce() -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1::nonce()'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#nonce

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1::nonce()
    address = Rituals.call('ritual_ZN7QOAuth15nonceEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QMap[str, QVariant])
  def generateAuthorizationHeader(
      oauthParams: QMap[str, QVariant],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1::generateAuthorizationHeader(const
    QVariantMap &oauthParams)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#generateAuthorizationHeader

    Parameters
    ----------

    oauthParams : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1::generateAuthorizationHeader(const QVariantMap
    #      &oauthParams)
    address = Rituals.call(
        'ritual_ZN7QOAuth127generateAuthorizationHeaderERK4QMapI7QString8QV'
        'ariantE',
        CuteMixin._valueOf(oauthParams),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth1'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOAuth1::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOAuth1::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QOAuth110metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def clientSharedSecret(self) -> str:
    """
    Calls Qt's 'QString QOAuth1::clientSharedSecret() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#clientSharedSecret

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuth1::clientSharedSecret() const
    return self.uglySide.call('ritual_ZNK7QOAuth118clientSharedSecretEv')

  def tokenSecret(self) -> str:
    """
    Calls Qt's 'QString QOAuth1::tokenSecret() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#tokenSecret

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuth1::tokenSecret() const
    return self.uglySide.call('ritual_ZNK7QOAuth111tokenSecretEv')

  def temporaryCredentialsUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QOAuth1::temporaryCredentialsUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#temporaryCredentialsUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuth1::temporaryCredentialsUrl() const
    address = self.uglySide.call(
        'ritual_ZNK7QOAuth123temporaryCredentialsUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def tokenCredentialsUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QOAuth1::tokenCredentialsUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#tokenCredentialsUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuth1::tokenCredentialsUrl() const
    address = self.uglySide.call('ritual_ZNK7QOAuth119tokenCredentialsUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def signatureMethod(self) -> SignatureMethod:
    """
    Calls Qt's 'SignatureMethod QOAuth1::signatureMethod() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#signatureMethod

    Returns
    -------

    SignatureMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SignatureMethod(number)'
      gives.
    """
    #  SignatureMethod QOAuth1::signatureMethod() const
    return QOAuth1.SignatureMethod(self.uglySide.call(
        'ritual_ZNK7QOAuth115signatureMethodEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setClientSharedSecret(self, clientSharedSecret: str) -> None:
    """
    Calls Qt's 'void QOAuth1::setClientSharedSecret(const QString
    &clientSharedSecret)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setClientSharedSecret

    Parameters
    ----------

    clientSharedSecret : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::setClientSharedSecret(const QString &clientSharedSecret)
    self.uglySide.call(
        'ritual_ZN7QOAuth121setClientSharedSecretERK7QString',
        clientSharedSecret,
    )

  @overload(str, str)
  def setClientCredentials(
      self,
      clientIdentifier: str,
      clientSharedSecret: str,
  ) -> None:
    """
    Calls Qt's 'void QOAuth1::setClientCredentials(const QString
    &clientIdentifier, const QString &clientSharedSecret)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setClientCredentials

    Parameters
    ----------

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.

    clientSharedSecret : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::setClientCredentials(const QString &clientIdentifier,
    #      const QString &clientSharedSecret)
    self.uglySide.call(
        'ritual_ZN7QOAuth120setClientCredentialsERK7QStringS2_',
        clientIdentifier, clientSharedSecret,
    )

  @overload(str)
  def setTokenSecret(self, tokenSecret: str) -> None:
    """
    Calls Qt's 'void QOAuth1::setTokenSecret(const QString &tokenSecret)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setTokenSecret

    Parameters
    ----------

    tokenSecret : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::setTokenSecret(const QString &tokenSecret)
    self.uglySide.call(
        'ritual_ZN7QOAuth114setTokenSecretERK7QString', tokenSecret,
    )

  @overload(str, str)
  def setTokenCredentials(self, token: str, tokenSecret: str) -> None:
    """
    Calls Qt's 'void QOAuth1::setTokenCredentials(const QString &token, const
    QString &tokenSecret)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setTokenCredentials

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.

    tokenSecret : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::setTokenCredentials(const QString &token, const QString
    #      &tokenSecret)
    self.uglySide.call(
        'ritual_ZN7QOAuth119setTokenCredentialsERK7QStringS2_',
        token, tokenSecret,
    )

  @overload(QUrl)
  def setTemporaryCredentialsUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QOAuth1::setTemporaryCredentialsUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#setTemporaryCredentialsUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth1::setTemporaryCredentialsUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN7QOAuth126setTemporaryCredentialsUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QUrl)
  def setTokenCredentialsUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QOAuth1::setTokenCredentialsUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#setTokenCredentialsUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth1::setTokenCredentialsUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN7QOAuth122setTokenCredentialsUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(SignatureMethod)
  def setSignatureMethod(self, value: SignatureMethod) -> None:
    """
    Calls Qt's 'void QOAuth1::setSignatureMethod(SignatureMethod value)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setSignatureMethod

    Parameters
    ----------

    value : SignatureMethod
      Passed on as its number.
    """
    #  void QOAuth1::setSignatureMethod(SignatureMethod value)
    self.uglySide.call(
        'ritual_ZN7QOAuth118setSignatureMethodENS_15SignatureMethodE',
        value.value,
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

  @overload(QNetworkAccessManager)
  @overload(QNetworkAccessManager, QObject)
  @overload(QNetworkAccessManager, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QOAuth1::QOAuth1(QNetworkAccessManager
    *manager, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#QOAuth1

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth1::QOAuth1(QNetworkAccessManager *manager, QObject *parent)
    self._noteCreation(QOAuth1, lambda: Rituals.call(
        'ritual_ZN7QOAuth1C1EP21QNetworkAccessManagerP7QObject',
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QOAuth1::QOAuth1(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#QOAuth1

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth1::QOAuth1(QObject *parent)
    self._noteCreation(QOAuth1, lambda: Rituals.call(
        'ritual_ZN7QOAuth1C1EP7QObject', self._addressOf(parent, 'QObject'),
    ))

  @overload(str, str, QNetworkAccessManager)
  @overload(str, str, NoneType)
  @overload(str, str, QNetworkAccessManager, QObject)
  @overload(str, str, QNetworkAccessManager, NoneType)
  @overload(str, str, NoneType, QObject)
  @overload(str, str, NoneType, NoneType)
  def __init__(
      self,
      clientIdentifier: str,
      clientSharedSecret: str,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QOAuth1::QOAuth1(const QString
    &clientIdentifier, const QString &clientSharedSecret,
    QNetworkAccessManager *manager, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#QOAuth1

    Parameters
    ----------

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.

    clientSharedSecret : str
      Passed on as it is: a QString is made of it for the call.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth1::QOAuth1(const QString &clientIdentifier, const QString
    #      &clientSharedSecret, QNetworkAccessManager *manager, QObject
    #      *parent)
    self._noteCreation(QOAuth1, lambda: Rituals.call(
        'ritual_ZN7QOAuth1C1ERK7QStringS2_P21QNetworkAccessManagerP7QObject',
        clientIdentifier, clientSharedSecret, self._addressOf(manager),
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

  @overload(QNetworkRequest, QByteArray)
  @overload(NoneType, QByteArray)
  @overload(QNetworkRequest, QByteArray, QByteArray)
  @overload(NoneType, QByteArray, QByteArray)
  def prepareRequest(
      self,
      request: Optional[QNetworkRequest],
      verb: QByteArray,
      body: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QOAuth1::prepareRequest(QNetworkRequest *request, const
    QByteArray &verb, const QByteArray &body)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#prepareRequest

    Parameters
    ----------

    request : Optional[QNetworkRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    verb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    body : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QOAuth1::prepareRequest(QNetworkRequest *request, const
    #      QByteArray &verb, const QByteArray &body)
    if body is None:
      from ..QtCore import QByteArray
      body = QByteArray()
    ritual = (
        'ritual_ZN7QOAuth114prepareRequestEP15QNetworkRequestRK10QByteArray'
        'S4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QOAuth114prepareRequestEP15QNetworkRequestRK10QByt'
          'eArrayS4_')
    self.uglySide.call(
        ritual,
        self._addressOf(request), self._valueOf(verb), self._valueOf(body),
    )

  @overload(QUrl, QMap[str, QVariant])
  def head(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QOAuth1::head(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#head

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QOAuth1::head(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN7QOAuth14headERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def get(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QOAuth1::get(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#get

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QOAuth1::get(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN7QOAuth13getERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def post(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QOAuth1::post(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#post

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QOAuth1::post(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN7QOAuth14postERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def put(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QOAuth1::put(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#put

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QOAuth1::put(const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN7QOAuth13putERK4QUrlRK4QMapI7QString8QVariantE',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(QUrl, QMap[str, QVariant])
  def deleteResource(
      self,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply *QOAuth1::deleteResource(const QUrl &url, const
    QVariantMap &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#deleteResource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply *QOAuth1::deleteResource(const QUrl &url, const
    #      QVariantMap &parameters)
    address = self.uglySide.call(
        'ritual_ZN7QOAuth114deleteResourceERK4QUrlRK4QMapI7QString8QVariant'
        'E',
        self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  def grant(self) -> None:
    """
    Calls Qt's 'void QOAuth1::grant()'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#grant
    """
    #  void QOAuth1::grant()
    ritual = 'ritual_ZN7QOAuth15grantEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QOAuth15grantEv'
    self.uglySide.call(ritual)

  @overload(str)
  def continueGrantWithVerifier(self, verifier: str) -> None:
    """
    Calls Qt's 'void QOAuth1::continueGrantWithVerifier(const QString
    &verifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#continueGrantWithVerifier

    Parameters
    ----------

    verifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::continueGrantWithVerifier(const QString &verifier)
    self.uglySide.call(
        'ritual_ZN7QOAuth125continueGrantWithVerifierERK7QString', verifier,
    )

  @overload(SignatureMethod)
  def signatureMethodChanged(self, method: SignatureMethod) -> None:
    """
    Calls Qt's 'void QOAuth1::signatureMethodChanged(QOAuth1::SignatureMethod
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#signatureMethodChanged

    Parameters
    ----------

    method : SignatureMethod
      Passed on as its number.
    """
    #  void QOAuth1::signatureMethodChanged(QOAuth1::SignatureMethod method)
    self.uglySide.call(
        'ritual_ZN7QOAuth122signatureMethodChangedENS_15SignatureMethodE',
        method.value,
    )

  @overload(str)
  def clientSharedSecretChanged(self, credential: str) -> None:
    """
    Calls Qt's 'void QOAuth1::clientSharedSecretChanged(const QString
    &credential)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#clientSharedSecretChanged

    Parameters
    ----------

    credential : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::clientSharedSecretChanged(const QString &credential)
    self.uglySide.call(
        'ritual_ZN7QOAuth125clientSharedSecretChangedERK7QString',
        credential,
    )

  @overload(str)
  def tokenSecretChanged(self, token: str) -> None:
    """
    Calls Qt's 'void QOAuth1::tokenSecretChanged(const QString &token)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#tokenSecretChanged

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth1::tokenSecretChanged(const QString &token)
    self.uglySide.call(
        'ritual_ZN7QOAuth118tokenSecretChangedERK7QString', token,
    )

  @overload(QUrl)
  def temporaryCredentialsUrlChanged(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QOAuth1::temporaryCredentialsUrlChanged(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#temporaryCredentialsUrlChanged

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth1::temporaryCredentialsUrlChanged(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN7QOAuth130temporaryCredentialsUrlChangedERK4QUrl',
        self._valueOf(url),
    )

  @overload(QUrl)
  def tokenCredentialsUrlChanged(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QOAuth1::tokenCredentialsUrlChanged(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#tokenCredentialsUrlChanged

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth1::tokenCredentialsUrlChanged(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN7QOAuth126tokenCredentialsUrlChangedERK4QUrl',
        self._valueOf(url),
    )

  @overload(QNetworkAccessManager.Operation, QUrl, QMap[str, QVariant])
  def requestTemporaryCredentials(
      self,
      operation: QNetworkAccessManager.Operation,
      url: QUrl,
      parameters: QMap[str, QVariant],
  ) -> Optional[QNetworkReply]:
    """
    Calls Qt's 'QNetworkReply
    *QOAuth1::requestTemporaryCredentials(QNetworkAccessManager::Operation
    operation, const QUrl &url, const QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1.html#requestTemporaryCredentials

    Parameters
    ----------

    operation : QNetworkAccessManager.Operation
      Passed on as its number.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReply
    #      *QOAuth1::requestTemporaryCredentials(QNetworkAccessManager::
    #      Operation operation, const QUrl &url, const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN7QOAuth127requestTemporaryCredentialsEN21QNetworkAccessMa'
        'nager9OperationERK4QUrlRK4QMapI7QString8QVariantE',
        operation.value, self._valueOf(url), self._valueOf(parameters),
    )
    from ..QtNetwork import QNetworkReply
    return QNetworkReply._cuteAt(address)

  @overload(
      QNetworkRequest, QMap[str, QVariant], QNetworkAccessManager.Operation,
  )
  @overload(NoneType, QMap[str, QVariant], QNetworkAccessManager.Operation)
  def setup(
      self,
      request: Optional[QNetworkRequest],
      signingParameters: QMap[str, QVariant],
      operation: QNetworkAccessManager.Operation,
  ) -> None:
    """
    Calls Qt's 'void QOAuth1::setup(QNetworkRequest *request, const
    QVariantMap &signingParameters, QNetworkAccessManager::Operation
    operation)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setup

    Parameters
    ----------

    request : Optional[QNetworkRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signingParameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operation : QNetworkAccessManager.Operation
      Passed on as its number.
    """
    #  void QOAuth1::setup(QNetworkRequest *request, const QVariantMap
    #      &signingParameters, QNetworkAccessManager::Operation operation)
    self.uglySide.call(
        'ritual_ZN7QOAuth15setupEP15QNetworkRequestRK4QMapI7QString8QVarian'
        'tEN21QNetworkAccessManager9OperationE',
        self._addressOf(request), self._valueOf(signingParameters),
        operation.value,
    )

  @overload(QNetworkRequest, QMap[str, QVariant], QByteArray)
  @overload(NoneType, QMap[str, QVariant], QByteArray)
  def setup(
      self,
      request: Optional[QNetworkRequest],
      signingParameters: QMap[str, QVariant],
      operationVerb: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QOAuth1::setup(QNetworkRequest *request, const
    QVariantMap &signingParameters, const QByteArray &operationVerb)'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#setup

    Parameters
    ----------

    request : Optional[QNetworkRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signingParameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    operationVerb : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QOAuth1::setup(QNetworkRequest *request, const QVariantMap
    #      &signingParameters, const QByteArray &operationVerb)
    self.uglySide.call(
        'ritual_ZN7QOAuth15setupEP15QNetworkRequestRK4QMapI7QString8QVarian'
        'tERK10QByteArray',
        self._addressOf(request), self._valueOf(signingParameters),
        self._valueOf(operationVerb),
    )

  def d_func(self) -> Optional[QOAuth1Private]:
    """
    Calls Qt's 'QOAuth1Private *QOAuth1::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qoauth1.html#d_func

    Returns
    -------

    Optional[QOAuth1Private]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuth1Private *QOAuth1::d_func()
    address = self.uglySide.call('ritual_ZN7QOAuth16d_funcEv')
    from . import QOAuth1Private
    return QOAuth1Private._cuteAt(address)

  @staticmethod
  def clientCredentials(*__, **_) -> Never:
    """
    Qt's 'std::pair<QString, QString> QOAuth1::clientCredentials() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOAuth1.clientCredentials' has no cute function yet. Qt's "
        "'std::pair<QString, QString> QOAuth1::clientCredentials() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def requestTokenCredentials(*__, **_) -> Never:
    """
    Qt's 'QNetworkReply
    *QOAuth1::requestTokenCredentials(QNetworkAccessManager::Operation
    operation, const QUrl &url, const std::pair<QString, QString>
    &temporaryToken, const QVariantMap &parameters)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOAuth1.requestTokenCredentials' has no cute function yet. Qt's "
        "'QNetworkReply "
        "*QOAuth1::requestTokenCredentials(QNetworkAccessManager::Operation "
        "operation, const QUrl &url, const std::pair<QString, QString> "
        "&temporaryToken, const QVariantMap &parameters)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def tokenCredentials(*__, **_) -> Never:
    """
    Qt's 'std::pair<QString, QString> QOAuth1::tokenCredentials() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOAuth1.tokenCredentials' has no cute function yet. Qt's "
        "'std::pair<QString, QString> QOAuth1::tokenCredentials() const': "
        "gives a type Python has no way to take yet.")
