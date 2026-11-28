"""
QOAuth2AuthorizationCodeFlow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qoauth2authorizationcodeflow.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractOAuth2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtNetwork import QNetworkAccessManager
  from . import QOAuth2AuthorizationCodeFlowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuth2AuthorizationCodeFlow(QAbstractOAuth2):
  """
  The cute side of Qt's QOAuth2AuthorizationCodeFlow: a plain Python object
  standing in front of one C++ QOAuth2AuthorizationCodeFlow.

  It is built on the cute 'QAbstractOAuth2', as Qt's
  QOAuth2AuthorizationCodeFlow is built on Qt's QAbstractOAuth2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuth2AuthorizationCodeFlow that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'accessTokenUrl', 'setAccessTokenUrl', 'setPkceMethod', 'pkceMethod',
  'grant', 'refreshAccessToken', 'refreshTokensImplementation',
  'requestAccessToken', 'accessTokenUrlChanged', 'd_func'. It can be made
  from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOAuth2AuthorizationCodeFlow::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QOAuth2AuthorizationCodeFlow::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOAuth2AuthorizationCodeFlow::~QOAuth2AuthorizationCodeFlow()': the
    destructor: Python never removes a C++ QOAuth2AuthorizationCodeFlow.
  - Qt's 'QUrl QOAuth2AuthorizationCodeFlow::buildAuthenticateUrl(const
    QMultiMap<QString, QVariant> &parameters)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QOAuth2AuthorizationCodeFlow::resourceOwnerAuthorization(const
    QUrl &url, const QMultiMap<QString, QVariant> &parameters)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QOAuth2AuthorizationCodeFlowPrivate
    *QOAuth2AuthorizationCodeFlow::d_func() const': takes in Python what
    'QOAuth2AuthorizationCodeFlowPrivate
    *QOAuth2AuthorizationCodeFlow::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOAuth2AuthorizationCodeFlow is created at the first use, not by
    'QOAuth2AuthorizationCodeFlow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuth2AuthorizationCodeFlow.
  - Qt tells when it has removed the C++ QOAuth2AuthorizationCodeFlow. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOAuth2AuthorizationCodeFlow that has no cute function
    yet, 'buildAuthenticateUrl', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOAuth2AuthorizationCodeFlow, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class PkceMethod(CuteNum, scoped=True):
    """
    The enum 'QOAuth2AuthorizationCodeFlow::PkceMethod' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    S256 = Kee[int](0)
    Plain = Kee[int](1)
    NULL = Kee[int](255)

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
    Calls Qt's 'QString QOAuth2AuthorizationCodeFlow::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#tr

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
    #  QString QOAuth2AuthorizationCodeFlow::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth2AuthorizationCodeFlow'

  #  A C++ QOAuth2AuthorizationCodeFlow Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOAuth2AuthorizationCodeFlow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOAuth2AuthorizationCodeFlow::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOAuth2AuthorizationCodeFlow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QOAuth2AuthorizationCodeFlow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def accessTokenUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QOAuth2AuthorizationCodeFlow::accessTokenUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#accessTokenUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuth2AuthorizationCodeFlow::accessTokenUrl() const
    address = self.uglySide.call(
        'ritual_ZNK28QOAuth2AuthorizationCodeFlow14accessTokenUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def pkceMethod(self) -> PkceMethod:
    """
    Calls Qt's 'PkceMethod QOAuth2AuthorizationCodeFlow::pkceMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#pkceMethod

    Returns
    -------

    PkceMethod
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PkceMethod(number)'
      gives.
    """
    #  PkceMethod QOAuth2AuthorizationCodeFlow::pkceMethod() const
    return QOAuth2AuthorizationCodeFlow.PkceMethod(self.uglySide.call(
        'ritual_ZNK28QOAuth2AuthorizationCodeFlow10pkceMethodEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setAccessTokenUrl(self, accessTokenUrl: QUrl) -> None:
    """
    Calls Qt's 'void QOAuth2AuthorizationCodeFlow::setAccessTokenUrl(const
    QUrl &accessTokenUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    accessTokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth2AuthorizationCodeFlow::setAccessTokenUrl(const QUrl
    #      &accessTokenUrl)
    self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow17setAccessTokenUrlERK4QUrl',
        self._valueOf(accessTokenUrl),
    )

  @overload(PkceMethod)
  @overload(PkceMethod, int)
  def setPkceMethod(self, method: PkceMethod, length: int = 43) -> None:
    """
    Calls Qt's 'void QOAuth2AuthorizationCodeFlow::setPkceMethod(PkceMethod
    method, qsizetype length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#setPkceMethod

    Parameters
    ----------

    method : PkceMethod
      Passed on as its number.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then 43.
    """
    #  void QOAuth2AuthorizationCodeFlow::setPkceMethod(PkceMethod method,
    #      qsizetype length)
    self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow13setPkceMethodENS_10PkceMe'
        'thodEx',
        method.value, length,
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
    Notes what was given, for Qt's
    'QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(
    QNetworkAccessManager *manager, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(
    #      QNetworkAccessManager *manager, QObject *parent)
    self._noteCreation(QOAuth2AuthorizationCodeFlow, lambda: Rituals.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlowC1EP21QNetworkAccessManager'
        'P7QObject',
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(QObject
    #      *parent)
    self._noteCreation(QOAuth2AuthorizationCodeFlow, lambda: Rituals.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlowC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QNetworkAccessManager)
  @overload(str, NoneType)
  @overload(str, QNetworkAccessManager, QObject)
  @overload(str, QNetworkAccessManager, NoneType)
  @overload(str, NoneType, QObject)
  @overload(str, NoneType, NoneType)
  def __init__(
      self,
      clientIdentifier: str,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QString
    &clientIdentifier, QNetworkAccessManager *manager, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const
    #      QString &clientIdentifier, QNetworkAccessManager *manager, QObject
    #      *parent)
    self._noteCreation(QOAuth2AuthorizationCodeFlow, lambda: Rituals.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlowC1ERK7QStringP21QNetworkAcc'
        'essManagerP7QObject',
        clientIdentifier, self._addressOf(manager), self._addressOf(parent,
        'QObject'),
    ))

  @overload(QUrl, QUrl, QNetworkAccessManager)
  @overload(QUrl, QUrl, NoneType)
  @overload(QUrl, QUrl, QNetworkAccessManager, QObject)
  @overload(QUrl, QUrl, QNetworkAccessManager, NoneType)
  @overload(QUrl, QUrl, NoneType, QObject)
  @overload(QUrl, QUrl, NoneType, NoneType)
  def __init__(
      self,
      authorizationUrl: QUrl,
      accessTokenUrl: QUrl,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QUrl
    &authorizationUrl, const QUrl &accessTokenUrl, QNetworkAccessManager
    *manager, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    authorizationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    accessTokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QUrl
    #      &authorizationUrl, const QUrl &accessTokenUrl,
    #      QNetworkAccessManager *manager, QObject *parent)
    self._noteCreation(QOAuth2AuthorizationCodeFlow, lambda: Rituals.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlowC1ERK4QUrlS2_P21QNetworkAcc'
        'essManagerP7QObject',
        self._valueOf(authorizationUrl), self._valueOf(accessTokenUrl),
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QUrl, QUrl, QNetworkAccessManager)
  @overload(str, QUrl, QUrl, NoneType)
  @overload(str, QUrl, QUrl, QNetworkAccessManager, QObject)
  @overload(str, QUrl, QUrl, QNetworkAccessManager, NoneType)
  @overload(str, QUrl, QUrl, NoneType, QObject)
  @overload(str, QUrl, QUrl, NoneType, NoneType)
  def __init__(
      self,
      clientIdentifier: str,
      authorizationUrl: QUrl,
      accessTokenUrl: QUrl,
      manager: Optional[QNetworkAccessManager],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QString
    &clientIdentifier, const QUrl &authorizationUrl, const QUrl
    &accessTokenUrl, QNetworkAccessManager *manager, QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.

    authorizationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    accessTokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const
    #      QString &clientIdentifier, const QUrl &authorizationUrl, const
    #      QUrl &accessTokenUrl, QNetworkAccessManager *manager, QObject
    #      *parent)
    self._noteCreation(QOAuth2AuthorizationCodeFlow, lambda: Rituals.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlowC1ERK7QStringRK4QUrlS5_P21Q'
        'NetworkAccessManagerP7QObject',
        clientIdentifier, self._valueOf(authorizationUrl),
        self._valueOf(accessTokenUrl), self._addressOf(manager),
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

  def grant(self) -> None:
    """
    Calls Qt's 'void QOAuth2AuthorizationCodeFlow::grant()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#grant
    """
    #  void QOAuth2AuthorizationCodeFlow::grant()
    ritual = 'ritual_ZN28QOAuth2AuthorizationCodeFlow5grantEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QOAuth2AuthorizationCodeFlow5grantEv'
    self.uglySide.call(ritual)

  def refreshAccessToken(self) -> None:
    """
    Calls Qt's 'void QOAuth2AuthorizationCodeFlow::refreshAccessToken()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html
    """
    #  void QOAuth2AuthorizationCodeFlow::refreshAccessToken()
    self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow18refreshAccessTokenEv',
    )

  def refreshTokensImplementation(self) -> None:
    """
    Calls Qt's 'void
    QOAuth2AuthorizationCodeFlow::refreshTokensImplementation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html
    """
    #  void QOAuth2AuthorizationCodeFlow::refreshTokensImplementation()
    self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow27refreshTokensImplementati'
        'onEv',
    )

  @overload(str)
  def requestAccessToken(self, code: str) -> None:
    """
    Calls Qt's 'void QOAuth2AuthorizationCodeFlow::requestAccessToken(const
    QString &code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth2AuthorizationCodeFlow::requestAccessToken(const QString
    #      &code)
    self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow18requestAccessTokenERK7QSt'
        'ring',
        code,
    )

  @overload(QUrl)
  def accessTokenUrlChanged(self, accessTokenUrl: QUrl) -> None:
    """
    Calls Qt's 'void
    QOAuth2AuthorizationCodeFlow::accessTokenUrlChanged(const QUrl
    &accessTokenUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html

    Parameters
    ----------

    accessTokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth2AuthorizationCodeFlow::accessTokenUrlChanged(const QUrl
    #      &accessTokenUrl)
    self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow21accessTokenUrlChangedERK4'
        'QUrl',
        self._valueOf(accessTokenUrl),
    )

  def d_func(self) -> Optional[QOAuth2AuthorizationCodeFlowPrivate]:
    """
    Calls Qt's 'QOAuth2AuthorizationCodeFlowPrivate
    *QOAuth2AuthorizationCodeFlow::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflow.html#d_func

    Returns
    -------

    Optional[QOAuth2AuthorizationCodeFlowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuth2AuthorizationCodeFlowPrivate
    #      *QOAuth2AuthorizationCodeFlow::d_func()
    address = self.uglySide.call(
        'ritual_ZN28QOAuth2AuthorizationCodeFlow6d_funcEv',
    )
    from . import QOAuth2AuthorizationCodeFlowPrivate
    return QOAuth2AuthorizationCodeFlowPrivate._cuteAt(address)

  @staticmethod
  def buildAuthenticateUrl(*__, **_) -> Never:
    """
    Qt's 'QUrl QOAuth2AuthorizationCodeFlow::buildAuthenticateUrl(const
    QMultiMap<QString, QVariant> &parameters)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QOAuth2AuthorizationCodeFlow.buildAuthenticateUrl' has no cute "
        "function yet. Qt's 'QUrl "
        "QOAuth2AuthorizationCodeFlow::buildAuthenticateUrl(const "
        "QMultiMap<QString, QVariant> &parameters)': takes a type Python "
        "has no way to hand over yet.")
