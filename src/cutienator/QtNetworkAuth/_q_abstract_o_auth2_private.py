"""
QAbstractOAuth2Private binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth2_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractOAuth2Private to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap
from . import QAbstractOAuth, QAbstractOAuthPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QLatin1String, QObject, QUrl, QVariant
  from . import QAbstractOAuth2
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QLatin1String = WAIT['QLatin1String']
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOAuth2Private(QAbstractOAuthPrivate):
  """
  The cute side of Qt's QAbstractOAuth2Private: a plain Python object
  standing in front of one C++ QAbstractOAuth2Private.

  It is built on the cute 'QAbstractOAuthPrivate', as Qt's
  QAbstractOAuth2Private is built on Qt's QAbstractOAuthPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractOAuth2Private that has a ritual and that
  Python can call so far, 12 names in all: 'q_func', 'setExpiresAt',
  'generateRandomState', 'generateNonce', 'authorizationShouldIncludeNonce',
  'setIdToken', '_q_tokenRequestFailed', 'handleRfcErrorResponseIfPresent',
  'createRefreshRequestAndBody', 'logAuthorizationStageWarning',
  'logTokenStageWarning', 'verifyThreadAffinity'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractOAuth2 *QAbstractOAuth2Private::q_func() const':
    takes in Python what 'QAbstractOAuth2 *QAbstractOAuth2Private::q_func()'
    takes.
  - Qt's 'QAbstractOAuth2Private::QAbstractOAuth2Private(const
    std::pair<QString, QString> &clientCredentials, const QUrl
    &authorizationUrl, QNetworkAccessManager *manager)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QAbstractOAuth2Private::~QAbstractOAuth2Private()': the destructor:
    Python never removes a C++ QAbstractOAuth2Private.
  - Qt's 'void QAbstractOAuth2Private::setGrantedScopeTokens(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QString QAbstractOAuth2Private::joinedScope(const QSet<QByteArray>
    &scopeTokens)': takes a type Python has no way to hand over yet.
  - Qt's 'QNetworkRequest QAbstractOAuth2Private::createRequest(QUrl url,
    const QVariantMap *parameters)': names 'QVariantMap', which has no cute
    class yet.
  - Qt's 'void
    QAbstractOAuth2Private::callNetworkRequestModifier(QNetworkRequest
    &request, QAbstractOAuth::Stage stage)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  7 of the 27 functions Qt declares: 4 leans on 'QAbstractOAuth2Private; 3
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QAbstractOAuth2Private is created at the first use, not by
    'QAbstractOAuth2Private(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractOAuth2Private.
  - Each name of Qt's QAbstractOAuth2Private that has no cute function yet,
    '__init__', '_q_tokenRequestFinished', 'callNetworkRequestModifier',
    'checkRequestedScopeTokenValid', 'checkRequestedScopeTokensValid',
    'createRequest', 'initializeRefreshHandling', 'joinedScope',
    'setGrantedScopeTokens', 'splitScope', 'updateRefreshTimer',
    'warnOnInvalidScopeToken', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QAbstractOAuth2Private, each a class in
  #  here as in C++.

  class CallerInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractOAuth2Private::CallerInfo: a plain Python
    object standing in front of one C++ QAbstractOAuth2Private::CallerInfo.

    What exists
    -----------

    No function of Qt's QAbstractOAuth2Private::CallerInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What to expect
    --------------

    - The C++ QAbstractOAuth2Private::CallerInfo is created at the first use,
      not by 'QAbstractOAuth2Private::CallerInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QAbstractOAuth2Private::CallerInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractOAuth2Private::CallerInfo'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class RequestAndBody(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAbstractOAuth2Private::RequestAndBody: a plain
    Python object standing in front of one C++
    QAbstractOAuth2Private::RequestAndBody.

    C++ hands a QAbstractOAuth2Private::RequestAndBody around as a copy, so
    every C++ QAbstractOAuth2Private::RequestAndBody behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QAbstractOAuth2Private::RequestAndBody yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAbstractOAuth2Private::RequestAndBody::~RequestAndBody()': the
      destructor: Python removes its C++
      QAbstractOAuth2Private::RequestAndBody by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QAbstractOAuth2Private::RequestAndBody is created at the first
      use, not by 'QAbstractOAuth2Private::RequestAndBody(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAbstractOAuth2Private::RequestAndBody back gives a
      copy the ritual made for Python, in a new cute
      QAbstractOAuth2Private::RequestAndBody.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAbstractOAuth2Private::RequestAndBody'

    #  Qt's '~QAbstractOAuth2Private::RequestAndBody()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QAbstractOAuth2Private::RequestAndBody behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QAbstractOAuth2Private14RequestAndBodyD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def generateRandomState() -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2Private::generateRandomState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#generateRandomState

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2Private::generateRandomState()
    return Rituals.call(
        'ritual_ZN22QAbstractOAuth2Private19generateRandomStateEv',
    )

  @staticmethod
  def generateNonce() -> str:
    """
    Calls Qt's 'QString QAbstractOAuth2Private::generateNonce()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#generateNonce

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractOAuth2Private::generateNonce()
    return Rituals.call('ritual_ZN22QAbstractOAuth2Private13generateNonceEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOAuth2Private'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def authorizationShouldIncludeNonce(self) -> bool:
    """
    Calls Qt's 'bool
    QAbstractOAuth2Private::authorizationShouldIncludeNonce() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html
    """
    #  bool QAbstractOAuth2Private::authorizationShouldIncludeNonce() const
    return self.uglySide.call(
        'ritual_ZNK22QAbstractOAuth2Private31authorizationShouldIncludeNonc'
        'eEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setExpiresAt(self, expiration: QDateTime) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2Private::setExpiresAt(const QDateTime
    &expiration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#setExpiresAt

    Parameters
    ----------

    expiration : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QAbstractOAuth2Private::setExpiresAt(const QDateTime &expiration)
    self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private12setExpiresAtERK9QDateTime',
        self._valueOf(expiration),
    )

  @overload(str)
  def setIdToken(self, token: str) -> None:
    """
    Calls Qt's 'void QAbstractOAuth2Private::setIdToken(const QString
    &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#setIdToken

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2Private::setIdToken(const QString &token)
    self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private10setIdTokenERK7QString', token,
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
    Qt's 'QAbstractOAuth2Private::QAbstractOAuth2Private(const
    std::pair<QString, QString> &clientCredentials, const QUrl
    &authorizationUrl, QNetworkAccessManager *manager)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.__init__' has no cute function yet. Qt's "
        "'QAbstractOAuth2Private::QAbstractOAuth2Private(const "
        "std::pair<QString, QString> &clientCredentials, const QUrl "
        "&authorizationUrl, QNetworkAccessManager *manager)': takes a type "
        "Python has no way to hand over yet.")

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

  def q_func(self) -> Optional[QAbstractOAuth2]:
    """
    Calls Qt's 'QAbstractOAuth2 *QAbstractOAuth2Private::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauth2private.html#q_func

    Returns
    -------

    Optional[QAbstractOAuth2]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOAuth2 *QAbstractOAuth2Private::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private6q_funcEv',
    )
    from . import QAbstractOAuth2
    return QAbstractOAuth2._cuteAt(address)

  @overload(QAbstractOAuth.Error, str)
  def _q_tokenRequestFailed(
      self,
      error: QAbstractOAuth.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuth2Private::_q_tokenRequestFailed(QAbstractOAuth::Error
    error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#_q_tokenRequestFailed

    Parameters
    ----------

    error : QAbstractOAuth.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractOAuth2Private::_q_tokenRequestFailed(QAbstractOAuth::
    #      Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private21_q_tokenRequestFailedEN14QAbstr'
        'actOAuth5ErrorERK7QString',
        error.value, errorString,
    )

  @overload(QMap[str, QVariant])
  def handleRfcErrorResponseIfPresent(
      self,
      data: QMap[str, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractOAuth2Private::handleRfcErrorResponseIfPresent(const QVariantMap
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QAbstractOAuth2Private::handleRfcErrorResponseIfPresent(const
    #      QVariantMap &data)
    return self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private31handleRfcErrorResponseIfPresent'
        'ERK4QMapI7QString8QVariantE',
        self._valueOf(data),
    )

  @overload(QUrl)
  def createRefreshRequestAndBody(self, url: QUrl) -> RequestAndBody:
    """
    Calls Qt's 'RequestAndBody
    QAbstractOAuth2Private::createRefreshRequestAndBody(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    RequestAndBody
      A new cute QAbstractOAuth2Private::RequestAndBody around the copy Qt
      gave back. Python owns it.
    """
    #  RequestAndBody
    #      QAbstractOAuth2Private::createRefreshRequestAndBody(const QUrl
    #      &url)
    address = self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private27createRefreshRequestAndBodyERK4'
        'QUrl',
        self._valueOf(url),
    )
    return QAbstractOAuth2Private.RequestAndBody._cuteOwning(address)

  @overload(QLatin1String)
  def logAuthorizationStageWarning(self, message: QLatin1String) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuth2Private::logAuthorizationStageWarning(QLatin1StringView
    message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html

    Parameters
    ----------

    message : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QAbstractOAuth2Private::logAuthorizationStageWarning(
    #      QLatin1StringView message)
    self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private28logAuthorizationStageWarningE13'
        'QLatin1String',
        self._valueOf(message),
    )

  @overload(QLatin1String, int)
  def logAuthorizationStageWarning(
      self,
      message: QLatin1String,
      detail: int,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuth2Private::logAuthorizationStageWarning(QLatin1StringView
    message, int detail)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html

    Parameters
    ----------

    message : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    detail : int
      Passed on as it is.
    """
    #  void QAbstractOAuth2Private::logAuthorizationStageWarning(
    #      QLatin1StringView message, int detail)
    self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private28logAuthorizationStageWarningE13'
        'QLatin1Stringi',
        self._valueOf(message), detail,
    )

  @overload(QLatin1String)
  def logTokenStageWarning(self, message: QLatin1String) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuth2Private::logTokenStageWarning(QLatin1StringView message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#logTokenStageWarning

    Parameters
    ----------

    message : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QAbstractOAuth2Private::logTokenStageWarning(QLatin1StringView
    #      message)
    self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private20logTokenStageWarningE13QLatin1S'
        'tring',
        self._valueOf(message),
    )

  @overload(QObject)
  @overload(NoneType)
  def verifyThreadAffinity(self, contextObject: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QAbstractOAuth2Private::verifyThreadAffinity(const
    QObject *contextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauth2private.html#verifyThreadAffinity

    Parameters
    ----------

    contextObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractOAuth2Private::verifyThreadAffinity(const QObject
    #      *contextObject)
    return self.uglySide.call(
        'ritual_ZN22QAbstractOAuth2Private20verifyThreadAffinityEPK7QObject',
        self._addressOf(contextObject, 'QObject'),
    )

  @staticmethod
  def _q_tokenRequestFinished(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2Private::_q_tokenRequestFinished(const
    QVariantMap &values)': leans on
    'QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private._q_tokenRequestFinished' has no cute "
        "function yet. Qt's 'void "
        "QAbstractOAuth2Private::_q_tokenRequestFinished(const QVariantMap "
        "&values)': leans on "
        "'QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def callNetworkRequestModifier(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractOAuth2Private::callNetworkRequestModifier(QNetworkRequest
    &request, QAbstractOAuth::Stage stage)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.callNetworkRequestModifier' has no cute "
        "function yet. Qt's 'void "
        "QAbstractOAuth2Private::callNetworkRequestModifier(QNetworkRequest "
        "&request, QAbstractOAuth::Stage stage)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def checkRequestedScopeTokenValid(*__, **_) -> Never:
    """
    Qt's 'bool
    QAbstractOAuth2Private::checkRequestedScopeTokenValid(QByteArrayView
    token)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'lcOAuth2Validation'.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.checkRequestedScopeTokenValid' has no cute "
        "function yet. Qt's 'bool "
        "QAbstractOAuth2Private::checkRequestedScopeTokenValid(QByteArrayVie"
        "w token)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'lcOAuth2Validation'.")

  @staticmethod
  def checkRequestedScopeTokensValid(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractOAuth2Private::checkRequestedScopeTokensValid(const
    QSet<QByteArray> &tokens)': leans on
    'QAbstractOAuth2Private::checkRequestedScopeTokenValid(QByteArrayView)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.checkRequestedScopeTokensValid' has no "
        "cute function yet. Qt's 'bool "
        "QAbstractOAuth2Private::checkRequestedScopeTokensValid(const "
        "QSet<QByteArray> &tokens)': leans on "
        "'QAbstractOAuth2Private::checkRequestedScopeTokenValid(QByteArrayVi"
        "ew)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def createRequest(*__, **_) -> Never:
    """
    Qt's 'QNetworkRequest QAbstractOAuth2Private::createRequest(QUrl url,
    const QVariantMap *parameters)': names 'QVariantMap', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.createRequest' has no cute function yet. "
        "Qt's 'QNetworkRequest QAbstractOAuth2Private::createRequest(QUrl "
        "url, const QVariantMap *parameters)': names 'QVariantMap', which "
        "has no cute class yet.")

  @staticmethod
  def initializeRefreshHandling(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2Private::initializeRefreshHandling()': leans on
    'QAbstractOAuth2Private::updateRefreshTimer(bool)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.initializeRefreshHandling' has no cute "
        "function yet. Qt's 'void "
        "QAbstractOAuth2Private::initializeRefreshHandling()': leans on "
        "'QAbstractOAuth2Private::updateRefreshTimer(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def joinedScope(*__, **_) -> Never:
    """
    Qt's 'QString QAbstractOAuth2Private::joinedScope(const QSet<QByteArray>
    &scopeTokens)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.joinedScope' has no cute function yet. "
        "Qt's 'QString QAbstractOAuth2Private::joinedScope(const "
        "QSet<QByteArray> &scopeTokens)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setGrantedScopeTokens(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2Private::setGrantedScopeTokens(const
    QSet<QByteArray> &tokens)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.setGrantedScopeTokens' has no cute "
        "function yet. Qt's 'void "
        "QAbstractOAuth2Private::setGrantedScopeTokens(const "
        "QSet<QByteArray> &tokens)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def splitScope(*__, **_) -> Never:
    """
    Qt's 'QSet<QByteArray> QAbstractOAuth2Private::splitScope(QStringView
    scope)': leans on
    'QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.splitScope' has no cute function yet. Qt's "
        "'QSet<QByteArray> QAbstractOAuth2Private::splitScope(QStringView "
        "scope)': leans on "
        "'QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def updateRefreshTimer(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2Private::updateRefreshTimer(bool
    clientSideUpdate)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: no matching literal operator
    for call to 'operator""s' with argument of type 'unsigned long long' or
    'const char *', and no matching literal operator template.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.updateRefreshTimer' has no cute function "
        "yet. Qt's 'void QAbstractOAuth2Private::updateRefreshTimer(bool "
        "clientSideUpdate)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: no matching "
        "literal operator for call to 'operator\"\"s' with argument of type "
        "'unsigned long long' or 'const char *', and no matching literal "
        "operator template.")

  @staticmethod
  def warnOnInvalidScopeToken(*__, **_) -> Never:
    """
    Qt's 'void QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView
    token)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'lcOAuth2Validation'.
    """
    raise NotImplementedError(
        "'QAbstractOAuth2Private.warnOnInvalidScopeToken' has no cute "
        "function yet. Qt's 'void "
        "QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView "
        "token)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'lcOAuth2Validation'.")
