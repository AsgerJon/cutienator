"""
QQuickWebEngineAuthenticationDialogRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineAuthenticationDialogRequest to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineAuthenticationDialogRequest(QObject):
  """
  The cute side of Qt's QQuickWebEngineAuthenticationDialogRequest: a plain
  Python object standing in front of one C++
  QQuickWebEngineAuthenticationDialogRequest.

  It is built on the cute 'QObject', as Qt's
  QQuickWebEngineAuthenticationDialogRequest is built on Qt's QObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineAuthenticationDialogRequest that has
  a ritual and that Python can call so far, 10 names in all: 'metaObject',
  'tr', 'url', 'realm', 'proxyHost', 'type', 'isAccepted', 'setAccepted',
  'dialogAccept', 'dialogReject'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineAuthenticationDialogRequest::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickWebEngineAuthenticationDialogRequest::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickWebEngineAuthenticationDialogRequest::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QQuickWebEngineAuthenticationDialogRequest::
    ~QQuickWebEngineAuthenticationDialogRequest()': the destructor: Python
    never removes a C++ QQuickWebEngineAuthenticationDialogRequest.
  - Qt's 'QQuickWebEngineAuthenticationDialogRequest::
    QQuickWebEngineAuthenticationDialogRequest(
    QSharedPointer<QtWebEngineCore::AuthenticationDialogController>
    controller, QObject *parent)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineAuthenticationDialogRequest is created at the
    first use, not by 'QQuickWebEngineAuthenticationDialogRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineAuthenticationDialogRequest.
  - Qt tells when it has removed the C++
    QQuickWebEngineAuthenticationDialogRequest. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickWebEngineAuthenticationDialogRequest that has no
    cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebEngineAuthenticationDialogRequest,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class AuthenticationType(CuteNum):
    """
    The enum 'QQuickWebEngineAuthenticationDialogRequest::AuthenticationType'
    of Qt, with the 2 names Qt gives in it.
    """

    AuthenticationTypeHTTP = Kee[int](0)
    AuthenticationTypeProxy = Kee[int](1)

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineAuthenticationDialogRequest::QmlIsUncreatable'
    of Qt, with the 1 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    yes = Kee[int](1)

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
    Calls Qt's 'QString QQuickWebEngineAuthenticationDialogRequest::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html#tr

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
    #  QString QQuickWebEngineAuthenticationDialogRequest::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN42QQuickWebEngineAuthenticationDialogRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineAuthenticationDialogRequest'

  #  A C++ QQuickWebEngineAuthenticationDialogRequest Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineAuthenticationDialogRequest'

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
    *QQuickWebEngineAuthenticationDialogRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickWebEngineAuthenticationDialogRequest::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest10metaObject'
        'Ev',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWebEngineAuthenticationDialogRequest::url()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWebEngineAuthenticationDialogRequest::url() const
    address = self.uglySide.call(
        'ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def realm(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineAuthenticationDialogRequest::realm()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineAuthenticationDialogRequest::realm() const
    return self.uglySide.call(
        'ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest5realmEv',
    )

  def proxyHost(self) -> str:
    """
    Calls Qt's 'QString
    QQuickWebEngineAuthenticationDialogRequest::proxyHost() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineAuthenticationDialogRequest::proxyHost() const
    return self.uglySide.call(
        'ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest9proxyHostEv',
    )

  def type(self) -> AuthenticationType:
    """
    Calls Qt's 'AuthenticationType
    QQuickWebEngineAuthenticationDialogRequest::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Returns
    -------

    AuthenticationType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AuthenticationType(number)' gives.
    """
    #  AuthenticationType QQuickWebEngineAuthenticationDialogRequest::type()
    #      const
    return QQuickWebEngineAuthenticationDialogRequest.AuthenticationType(
        self.uglySide.call(
            'ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest4typeEv',
        ))

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineAuthenticationDialogRequest::isAccepted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html
    """
    #  bool QQuickWebEngineAuthenticationDialogRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK42QQuickWebEngineAuthenticationDialogRequest10isAccepted'
        'Ev',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineAuthenticationDialogRequest::setAccepted(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineAuthenticationDialogRequest::setAccepted(bool
    #      accepted)
    self.uglySide.call(
        'ritual_ZN42QQuickWebEngineAuthenticationDialogRequest11setAccepted'
        'Eb',
        accepted,
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
    Qt's 'QQuickWebEngineAuthenticationDialogRequest::
    QQuickWebEngineAuthenticationDialogRequest(
    QSharedPointer<QtWebEngineCore::AuthenticationDialogController>
    controller, QObject *parent)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineAuthenticationDialogRequest.__init__' has no cute "
        "function yet. Qt's "
        "'QQuickWebEngineAuthenticationDialogRequest::QQuickWebEngineAuthent"
        "icationDialogRequest(QSharedPointer<QtWebEngineCore::Authentication"
        "DialogController> controller, QObject *parent)': takes a type "
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

  @overload(str, str)
  def dialogAccept(self, user: str, password: str) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineAuthenticationDialogRequest::dialogAccept(const QString
    &user, const QString &password)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html

    Parameters
    ----------

    user : str
      Passed on as it is: a QString is made of it for the call.

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWebEngineAuthenticationDialogRequest::dialogAccept(const
    #      QString &user, const QString &password)
    self.uglySide.call(
        'ritual_ZN42QQuickWebEngineAuthenticationDialogRequest12dialogAccep'
        'tERK7QStringS2_',
        user, password,
    )

  def dialogReject(self) -> None:
    """
    Calls Qt's 'void
    QQuickWebEngineAuthenticationDialogRequest::dialogReject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineauthenticationdialogrequest.html
    """
    #  void QQuickWebEngineAuthenticationDialogRequest::dialogReject()
    self.uglySide.call(
        'ritual_ZN42QQuickWebEngineAuthenticationDialogRequest12dialogRejec'
        'tEv',
    )
