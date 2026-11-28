"""
QOAuth2DeviceAuthorizationFlow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/qoauth2deviceauthorizationflow.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractOAuth2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QEvent, QMetaObject, QUrl
  from ..QtNetwork import QNetworkAccessManager
  from . import QOAuth2DeviceAuthorizationFlowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QEvent = WAIT['QEvent']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuth2DeviceAuthorizationFlow(QAbstractOAuth2):
  """
  The cute side of Qt's QOAuth2DeviceAuthorizationFlow: a plain Python object
  standing in front of one C++ QOAuth2DeviceAuthorizationFlow.

  It is built on the cute 'QAbstractOAuth2', as Qt's
  QOAuth2DeviceAuthorizationFlow is built on Qt's QAbstractOAuth2, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuth2DeviceAuthorizationFlow that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject', 'tr',
  'userCode', 'verificationUrl', 'completeVerificationUrl', 'isPolling',
  'userCodeExpirationAt', 'grant', 'startTokenPolling', 'stopTokenPolling',
  'authorizeWithUserCode', 'userCodeChanged', 'verificationUrlChanged',
  'completeVerificationUrlChanged', 'pollingChanged',
  'userCodeExpirationAtChanged', 'event', 'refreshTokensImplementation',
  'd_func'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOAuth2DeviceAuthorizationFlow::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QOAuth2DeviceAuthorizationFlow::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOAuth2DeviceAuthorizationFlow::~QOAuth2DeviceAuthorizationFlow()':
    the destructor: Python never removes a C++
    QOAuth2DeviceAuthorizationFlow.
  - Qt's 'const QOAuth2DeviceAuthorizationFlowPrivate
    *QOAuth2DeviceAuthorizationFlow::d_func() const': takes in Python what
    'QOAuth2DeviceAuthorizationFlowPrivate
    *QOAuth2DeviceAuthorizationFlow::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QOAuth2DeviceAuthorizationFlow is created at the first use, not
    by 'QOAuth2DeviceAuthorizationFlow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuth2DeviceAuthorizationFlow.
  - Qt tells when it has removed the C++ QOAuth2DeviceAuthorizationFlow.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QOAuth2DeviceAuthorizationFlow::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#tr

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
    #  QString QOAuth2DeviceAuthorizationFlow::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth2DeviceAuthorizationFlow'

  #  A C++ QOAuth2DeviceAuthorizationFlow Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOAuth2DeviceAuthorizationFlow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QOAuth2DeviceAuthorizationFlow::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOAuth2DeviceAuthorizationFlow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QOAuth2DeviceAuthorizationFlow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def userCode(self) -> str:
    """
    Calls Qt's 'QString QOAuth2DeviceAuthorizationFlow::userCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#userCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuth2DeviceAuthorizationFlow::userCode() const
    return self.uglySide.call(
        'ritual_ZNK30QOAuth2DeviceAuthorizationFlow8userCodeEv',
    )

  def verificationUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QOAuth2DeviceAuthorizationFlow::verificationUrl()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuth2DeviceAuthorizationFlow::verificationUrl() const
    address = self.uglySide.call(
        'ritual_ZNK30QOAuth2DeviceAuthorizationFlow15verificationUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def completeVerificationUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl
    QOAuth2DeviceAuthorizationFlow::completeVerificationUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QOAuth2DeviceAuthorizationFlow::completeVerificationUrl() const
    address = self.uglySide.call(
        'ritual_ZNK30QOAuth2DeviceAuthorizationFlow23completeVerificationUr'
        'lEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isPolling(self) -> bool:
    """
    Calls Qt's 'bool QOAuth2DeviceAuthorizationFlow::isPolling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#isPolling
    """
    #  bool QOAuth2DeviceAuthorizationFlow::isPolling() const
    return self.uglySide.call(
        'ritual_ZNK30QOAuth2DeviceAuthorizationFlow9isPollingEv',
    )

  def userCodeExpirationAt(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime
    QOAuth2DeviceAuthorizationFlow::userCodeExpirationAt() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QOAuth2DeviceAuthorizationFlow::userCodeExpirationAt() const
    address = self.uglySide.call(
        'ritual_ZNK30QOAuth2DeviceAuthorizationFlow20userCodeExpirationAtEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html
    """
    #  QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow()
    self._noteCreation(QOAuth2DeviceAuthorizationFlow, lambda: Rituals.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlowC1Ev',
    ))

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
    'QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow(
    QNetworkAccessManager *manager, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow(
    #      QNetworkAccessManager *manager, QObject *parent)
    self._noteCreation(QOAuth2DeviceAuthorizationFlow, lambda: Rituals.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlowC1EP21QNetworkAccessManag'
        'erP7QObject',
        self._addressOf(manager), self._addressOf(parent, 'QObject'),
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow(QObject
    #      *parent)
    self._noteCreation(QOAuth2DeviceAuthorizationFlow, lambda: Rituals.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlowC1EP7QObject',
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
    Calls Qt's 'void QOAuth2DeviceAuthorizationFlow::grant()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#grant
    """
    #  void QOAuth2DeviceAuthorizationFlow::grant()
    ritual = 'ritual_ZN30QOAuth2DeviceAuthorizationFlow5grantEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QOAuth2DeviceAuthorizationFlow5grantEv'
    self.uglySide.call(ritual)

  def startTokenPolling(self) -> bool:
    """
    Calls Qt's 'bool QOAuth2DeviceAuthorizationFlow::startTokenPolling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html
    """
    #  bool QOAuth2DeviceAuthorizationFlow::startTokenPolling()
    return self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow17startTokenPollingEv',
    )

  def stopTokenPolling(self) -> None:
    """
    Calls Qt's 'void QOAuth2DeviceAuthorizationFlow::stopTokenPolling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html
    """
    #  void QOAuth2DeviceAuthorizationFlow::stopTokenPolling()
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow16stopTokenPollingEv',
    )

  @overload(QUrl, str, QUrl)
  def authorizeWithUserCode(
      self,
      verificationUrl: QUrl,
      userCode: str,
      completeVerificationUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlow::authorizeWithUserCode(const QUrl
    &verificationUrl, const QString &userCode, const QUrl
    &completeVerificationUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    verificationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    userCode : str
      Passed on as it is: a QString is made of it for the call.

    completeVerificationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth2DeviceAuthorizationFlow::authorizeWithUserCode(const QUrl
    #      &verificationUrl, const QString &userCode, const QUrl
    #      &completeVerificationUrl)
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow21authorizeWithUserCodeER'
        'K4QUrlRK7QStringS2_',
        self._valueOf(verificationUrl), userCode,
        self._valueOf(completeVerificationUrl),
    )

  @overload(str)
  def userCodeChanged(self, userCode: str) -> None:
    """
    Calls Qt's 'void QOAuth2DeviceAuthorizationFlow::userCodeChanged(const
    QString &userCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    userCode : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOAuth2DeviceAuthorizationFlow::userCodeChanged(const QString
    #      &userCode)
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow15userCodeChangedERK7QStr'
        'ing',
        userCode,
    )

  @overload(QUrl)
  def verificationUrlChanged(self, verificationUrl: QUrl) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlow::verificationUrlChanged(const QUrl
    &verificationUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    verificationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth2DeviceAuthorizationFlow::verificationUrlChanged(const QUrl
    #      &verificationUrl)
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow22verificationUrlChangedE'
        'RK4QUrl',
        self._valueOf(verificationUrl),
    )

  @overload(QUrl)
  def completeVerificationUrlChanged(
      self,
      completeVerificationUrl: QUrl,
  ) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlow::completeVerificationUrlChanged(const QUrl
    &completeVerificationUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    completeVerificationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuth2DeviceAuthorizationFlow::completeVerificationUrlChanged(
    #      const QUrl &completeVerificationUrl)
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow30completeVerificationUrl'
        'ChangedERK4QUrl',
        self._valueOf(completeVerificationUrl),
    )

  @overload(bool)
  def pollingChanged(self, polling: bool) -> None:
    """
    Calls Qt's 'void QOAuth2DeviceAuthorizationFlow::pollingChanged(bool
    polling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#pollingChanged

    Parameters
    ----------

    polling : bool
      Passed on as it is.
    """
    #  void QOAuth2DeviceAuthorizationFlow::pollingChanged(bool polling)
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow14pollingChangedEb',
        polling,
    )

  @overload(QDateTime)
  def userCodeExpirationAtChanged(self, expiration: QDateTime) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlow::userCodeExpirationAtChanged(const
    QDateTime &expiration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html

    Parameters
    ----------

    expiration : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QOAuth2DeviceAuthorizationFlow::userCodeExpirationAtChanged(const
    #      QDateTime &expiration)
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow27userCodeExpirationAtCha'
        'ngedERK9QDateTime',
        self._valueOf(expiration),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QOAuth2DeviceAuthorizationFlow::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOAuth2DeviceAuthorizationFlow::event(QEvent *event)
    ritual = 'ritual_ZN30QOAuth2DeviceAuthorizationFlow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QOAuth2DeviceAuthorizationFlow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def refreshTokensImplementation(self) -> None:
    """
    Calls Qt's 'void
    QOAuth2DeviceAuthorizationFlow::refreshTokensImplementation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html
    """
    #  void QOAuth2DeviceAuthorizationFlow::refreshTokensImplementation()
    self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow27refreshTokensImplementa'
        'tionEv',
    )

  def d_func(self) -> Optional[QOAuth2DeviceAuthorizationFlowPrivate]:
    """
    Calls Qt's 'QOAuth2DeviceAuthorizationFlowPrivate
    *QOAuth2DeviceAuthorizationFlow::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2deviceauthorizationflow.html#d_func

    Returns
    -------

    Optional[QOAuth2DeviceAuthorizationFlowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuth2DeviceAuthorizationFlowPrivate
    #      *QOAuth2DeviceAuthorizationFlow::d_func()
    address = self.uglySide.call(
        'ritual_ZN30QOAuth2DeviceAuthorizationFlow6d_funcEv',
    )
    from . import QOAuth2DeviceAuthorizationFlowPrivate
    return QOAuth2DeviceAuthorizationFlowPrivate._cuteAt(address)
