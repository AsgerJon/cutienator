"""
QOAuth2DeviceAuthorizationFlowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QOAuth2DeviceAuthorizationFlowPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractOAuth, QAbstractOAuth2Private

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QUrl
  from ..QtNetwork import QNetworkAccessManager, QRestAccessManager
  from . import QOAuth2DeviceAuthorizationFlow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuth2DeviceAuthorizationFlowPrivate(QAbstractOAuth2Private):
  """
  The cute side of Qt's QOAuth2DeviceAuthorizationFlowPrivate: a plain Python
  object standing in front of one C++ QOAuth2DeviceAuthorizationFlowPrivate.

  It is built on the cute 'QAbstractOAuth2Private', as Qt's
  QOAuth2DeviceAuthorizationFlowPrivate is built on Qt's
  QAbstractOAuth2Private, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuth2DeviceAuthorizationFlowPrivate that has a
  ritual and that Python can call so far, 11 names in all: 'q_func',
  'tokenAcquisitionFailed', 'setUserCode', 'setVerificationUrl',
  'setVerificationUrlComplete', 'setUserCodeExpiration', 'stopTokenPolling',
  'isNextPollAfterExpiration', 'resetCurrentTokenReply',
  'resetCurrentAuthorizationReply', 'network'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOAuth2DeviceAuthorizationFlow
    *QOAuth2DeviceAuthorizationFlowPrivate::q_func() const': takes in Python
    what 'QOAuth2DeviceAuthorizationFlow
    *QOAuth2DeviceAuthorizationFlowPrivate::q_func()' takes.
  - Qt's 'QOAuth2DeviceAuthorizationFlowPrivate::
    ~QOAuth2DeviceAuthorizationFlowPrivate()': the destructor: Python never
    removes a C++ QOAuth2DeviceAuthorizationFlowPrivate.

  What has no ritual
  ------------------

  7 of the 21 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QAbstractOAuth2Private.

  What to expect
  --------------

  - The C++ QOAuth2DeviceAuthorizationFlowPrivate is created at the first
    use, not by 'QOAuth2DeviceAuthorizationFlowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuth2DeviceAuthorizationFlowPrivate.
  - Each name of Qt's QOAuth2DeviceAuthorizationFlowPrivate that has no cute
    function yet, 'authorizationReplyFinished', 'handleTokenErrorResponse',
    'handleTokenSuccessResponse', 'pollTokens', 'reset', 'startTokenPolling',
    'tokenReplyFinished', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth2DeviceAuthorizationFlowPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNextPollAfterExpiration(self) -> bool:
    """
    Calls Qt's 'bool
    QOAuth2DeviceAuthorizationFlowPrivate::isNextPollAfterExpiration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html
    """
    #  bool
    #      QOAuth2DeviceAuthorizationFlowPrivate::isNextPollAfterExpiration()
    #      const
    return self.uglySide.call(
        'ritual_ZNK37QOAuth2DeviceAuthorizationFlowPrivate25isNextPollAfter'
        'ExpirationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setUserCode(self, code: str) -> None:
    """
    Calls Qt's 'void QOAuth2DeviceAuthorizationFlowPrivate::setUserCode(const
    QString &code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth2DeviceAuthorizationFlowPrivate::setUserCode(const QString
    #      &code)
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate11setUserCodeERK7Q'
        'String',
        code,
    )

  @overload(QUrl)
  def setVerificationUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrl(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrl(const
    #      QUrl &url)
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate18setVerificationU'
        'rlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QUrl)
  def setVerificationUrlComplete(self, url: QUrl) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrlComplete(const
    QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void
    #      QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrlComplete(
    #      const QUrl &url)
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate26setVerificationU'
        'rlCompleteERK4QUrl',
        self._valueOf(url),
    )

  @overload(QDateTime)
  def setUserCodeExpiration(self, expiration: QDateTime) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::setUserCodeExpiration(const
    QDateTime &expiration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html

    Parameters
    ----------

    expiration : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void
    #      QOAuth2DeviceAuthorizationFlowPrivate::setUserCodeExpiration(const
    #      QDateTime &expiration)
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate21setUserCodeExpir'
        'ationERK9QDateTime',
        self._valueOf(expiration),
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
  @overload(QNetworkAccessManager)
  @overload(NoneType)
  def __init__(
      self,
      manager: Optional[QNetworkAccessManager] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QOAuth2DeviceAuthorizationFlowPrivate::
    QOAuth2DeviceAuthorizationFlowPrivate(QNetworkAccessManager *manager)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2DeviceAuthorizationFlowPrivate::
    #      QOAuth2DeviceAuthorizationFlowPrivate(QNetworkAccessManager
    #      *manager)
    self._noteCreation(
        QOAuth2DeviceAuthorizationFlowPrivate, lambda: Rituals.call(
            'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivateC1EP21QNetwork'
            'AccessManager',
            self._addressOf(manager),
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

  def q_func(self) -> Optional[QOAuth2DeviceAuthorizationFlow]:
    """
    Calls Qt's 'QOAuth2DeviceAuthorizationFlow
    *QOAuth2DeviceAuthorizationFlowPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html#q_func

    Returns
    -------

    Optional[QOAuth2DeviceAuthorizationFlow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuth2DeviceAuthorizationFlow
    #      *QOAuth2DeviceAuthorizationFlowPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate6q_funcEv',
    )
    from . import QOAuth2DeviceAuthorizationFlow
    return QOAuth2DeviceAuthorizationFlow._cuteAt(address)

  @overload(QAbstractOAuth.Error)
  @overload(QAbstractOAuth.Error, str)
  def tokenAcquisitionFailed(
      self,
      error: QAbstractOAuth.Error,
      errorString: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::tokenAcquisitionFailed(
    QAbstractOAuth::Error error, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html

    Parameters
    ----------

    error : QAbstractOAuth.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QOAuth2DeviceAuthorizationFlowPrivate::tokenAcquisitionFailed(
    #      QAbstractOAuth::Error error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate22tokenAcquisition'
        'FailedEN14QAbstractOAuth5ErrorERK7QString',
        error.value, errorString,
    )

  def stopTokenPolling(self) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::stopTokenPolling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html
    """
    #  void QOAuth2DeviceAuthorizationFlowPrivate::stopTokenPolling()
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate16stopTokenPolling'
        'Ev',
    )

  def resetCurrentTokenReply(self) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentTokenReply()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html
    """
    #  void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentTokenReply()
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate22resetCurrentToke'
        'nReplyEv',
    )

  def resetCurrentAuthorizationReply(self) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentAuthorizationReply()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html
    """
    #  void QOAuth2DeviceAuthorizationFlowPrivate::
    #      resetCurrentAuthorizationReply()
    self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate30resetCurrentAuth'
        'orizationReplyEv',
    )

  def network(self) -> Optional[QRestAccessManager]:
    """
    Calls Qt's 'QRestAccessManager
    *QOAuth2DeviceAuthorizationFlowPrivate::network()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflowprivate.html#network

    Returns
    -------

    Optional[QRestAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRestAccessManager *QOAuth2DeviceAuthorizationFlowPrivate::network()
    address = self.uglySide.call(
        'ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate7networkEv',
    )
    from ..QtNetwork import QRestAccessManager
    return QRestAccessManager._cuteAt(address)

  @staticmethod
  def authorizationReplyFinished(*__, **_) -> Never:
    """
    Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::authorizationReplyFinished(
    QRestReply &reply)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'Error'.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.authorizationReplyFinished' "
        "has no cute function yet. Qt's 'void "
        "QOAuth2DeviceAuthorizationFlowPrivate::authorizationReplyFinished(Q"
        "RestReply &reply)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'Error'.")

  @staticmethod
  def handleTokenErrorResponse(*__, **_) -> Never:
    """
    Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::handleTokenErrorResponse(const
    QJsonObject &data)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: no matching literal
    operator for call to 'operator""ms' with argument of type 'unsigned long
    long' or 'const char *', and no matching literal operator template.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.handleTokenErrorResponse' "
        "has no cute function yet. Qt's 'void "
        "QOAuth2DeviceAuthorizationFlowPrivate::handleTokenErrorResponse(con"
        "st QJsonObject &data)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: no "
        "matching literal operator for call to 'operator\"\"ms' with "
        "argument of type 'unsigned long long' or 'const char *', and no "
        "matching literal operator template.")

  @staticmethod
  def handleTokenSuccessResponse(*__, **_) -> Never:
    """
    Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::handleTokenSuccessResponse(const
    QJsonObject &data)': leans on
    'QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.handleTokenSuccessResponse' "
        "has no cute function yet. Qt's 'void "
        "QOAuth2DeviceAuthorizationFlowPrivate::handleTokenSuccessResponse(c"
        "onst QJsonObject &data)': leans on "
        "'QAbstractOAuth2Private::warnOnInvalidScopeToken(QStringView)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def pollTokens(*__, **_) -> Never:
    """
    Qt's 'void QOAuth2DeviceAuthorizationFlowPrivate::pollTokens()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'Error'.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.pollTokens' has no cute "
        "function yet. Qt's 'void "
        "QOAuth2DeviceAuthorizationFlowPrivate::pollTokens()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'Error'.")

  @staticmethod
  def reset(*__, **_) -> Never:
    """
    Qt's 'void QOAuth2DeviceAuthorizationFlowPrivate::reset()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'Status'; did you mean
    'QAbstractOAuth2::Status'?.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.reset' has no cute function "
        "yet. Qt's 'void QOAuth2DeviceAuthorizationFlowPrivate::reset()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'Status'; did you mean 'QAbstractOAuth2::Status'?.")

  @staticmethod
  def startTokenPolling(*__, **_) -> Never:
    """
    Qt's 'bool QOAuth2DeviceAuthorizationFlowPrivate::startTokenPolling()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'Error'.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.startTokenPolling' has no "
        "cute function yet. Qt's 'bool "
        "QOAuth2DeviceAuthorizationFlowPrivate::startTokenPolling()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'Error'.")

  @staticmethod
  def tokenReplyFinished(*__, **_) -> Never:
    """
    Qt's 'void
    QOAuth2DeviceAuthorizationFlowPrivate::tokenReplyFinished(QRestReply
    &reply)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'Error'.
    """
    raise NotImplementedError(
        "'QOAuth2DeviceAuthorizationFlowPrivate.tokenReplyFinished' has no "
        "cute function yet. Qt's 'void "
        "QOAuth2DeviceAuthorizationFlowPrivate::tokenReplyFinished(QRestRepl"
        "y &reply)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'Error'.")
