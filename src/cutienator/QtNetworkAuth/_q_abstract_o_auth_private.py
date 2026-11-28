"""
QAbstractOAuthPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractOAuthPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObjectPrivate
from . import QAbstractOAuth

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl, QVariant
  from ..QtNetwork import QNetworkAccessManager, QNetworkRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkRequest = WAIT['QNetworkRequest']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractOAuthPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractOAuthPrivate: a plain Python object standing
  in front of one C++ QAbstractOAuthPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstractOAuthPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractOAuthPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'q_func', 'networkAccessManager',
  'setStatus', 'generateRandomBase64String', 'setExtraTokens',
  'convertParameters', 'addContentTypeHeaders'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractOAuth *QAbstractOAuthPrivate::q_func() const': takes
    in Python what 'QAbstractOAuth *QAbstractOAuthPrivate::q_func()' takes.
  - Qt's 'QAbstractOAuthPrivate::~QAbstractOAuthPrivate()': the destructor:
    Python never removes a C++ QAbstractOAuthPrivate.
  - Qt's 'QUrlQuery QAbstractOAuthPrivate::createQuery(const
    QMultiMap<QString, QVariant> &parameters)': takes a type Python has no
    way to hand over yet.

  What to expect
  --------------

  - The C++ QAbstractOAuthPrivate is created at the first use, not by
    'QAbstractOAuthPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractOAuthPrivate.
  - Each name of Qt's QAbstractOAuthPrivate that has no cute function yet,
    'createQuery', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def generateRandomBase64String(length: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QAbstractOAuthPrivate::generateRandomBase64String(quint8 length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html

    Parameters
    ----------

    length : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAbstractOAuthPrivate::generateRandomBase64String(quint8
    #      length)
    address = Rituals.call(
        'ritual_ZN21QAbstractOAuthPrivate26generateRandomBase64StringEh',
        length,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractOAuthPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractOAuth.Status)
  def setStatus(self, status: QAbstractOAuth.Status) -> None:
    """
    Calls Qt's 'void QAbstractOAuthPrivate::setStatus(QAbstractOAuth::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html#setStatus

    Parameters
    ----------

    status : QAbstractOAuth.Status
      Passed on as its number.
    """
    #  void QAbstractOAuthPrivate::setStatus(QAbstractOAuth::Status status)
    self.uglySide.call(
        'ritual_ZN21QAbstractOAuthPrivate9setStatusEN14QAbstractOAuth6Statu'
        'sE',
        status.value,
    )

  @overload(QMap[str, QVariant])
  def setExtraTokens(self, tokens: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QAbstractOAuthPrivate::setExtraTokens(const QVariantMap
    &tokens)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html#setExtraTokens

    Parameters
    ----------

    tokens : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QAbstractOAuthPrivate::setExtraTokens(const QVariantMap &tokens)
    self.uglySide.call(
        'ritual_ZN21QAbstractOAuthPrivate14setExtraTokensERK4QMapI7QString8'
        'QVariantE',
        self._valueOf(tokens),
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

  @overload(str, QUrl, str, QNetworkAccessManager)
  @overload(str, QUrl, str, NoneType)
  @overload(NoneType, QUrl, str, QNetworkAccessManager)
  @overload(NoneType, QUrl, str, NoneType)
  def __init__(
      self,
      loggingCategory: Optional[str],
      authorizationUrl: QUrl,
      clientIdentifier: str,
      manager: Optional[QNetworkAccessManager],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractOAuthPrivate::QAbstractOAuthPrivate(const char
    *loggingCategory, const QUrl &authorizationUrl, const QString
    &clientIdentifier, QNetworkAccessManager *manager)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html#QAbstractOAuthPrivate

    Parameters
    ----------

    loggingCategory : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    authorizationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractOAuthPrivate::QAbstractOAuthPrivate(const char
    #      *loggingCategory, const QUrl &authorizationUrl, const QString
    #      &clientIdentifier, QNetworkAccessManager *manager)
    self._noteCreation(QAbstractOAuthPrivate, lambda: Rituals.call(
        'ritual_ZN21QAbstractOAuthPrivateC1EPKcRK4QUrlRK7QStringP21QNetwork'
        'AccessManager',
        self._bytesOf(loggingCategory), self._valueOf(authorizationUrl),
        clientIdentifier, self._addressOf(manager),
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

  def q_func(self) -> Optional[QAbstractOAuth]:
    """
    Calls Qt's 'QAbstractOAuth *QAbstractOAuthPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractoauthprivate.html#q_func

    Returns
    -------

    Optional[QAbstractOAuth]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractOAuth *QAbstractOAuthPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QAbstractOAuthPrivate6q_funcEv')
    return QAbstractOAuth._cuteAt(address)

  def networkAccessManager(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager
    *QAbstractOAuthPrivate::networkAccessManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html#networkAccessManager

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QAbstractOAuthPrivate::networkAccessManager()
    address = self.uglySide.call(
        'ritual_ZN21QAbstractOAuthPrivate20networkAccessManagerEv',
    )
    from ..QtNetwork import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

  @overload(QMap[str, QVariant])
  def convertParameters(self, parameters: QMap[str, QVariant]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QAbstractOAuthPrivate::convertParameters(const
    QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html#convertParameters

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAbstractOAuthPrivate::convertParameters(const QVariantMap
    #      &parameters)
    address = self.uglySide.call(
        'ritual_ZN21QAbstractOAuthPrivate17convertParametersERK4QMapI7QStri'
        'ng8QVariantE',
        self._valueOf(parameters),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QNetworkRequest)
  @overload(NoneType)
  def addContentTypeHeaders(
      self,
      request: Optional[QNetworkRequest],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractOAuthPrivate::addContentTypeHeaders(QNetworkRequest *request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractoauthprivate.html#addContentTypeHeaders

    Parameters
    ----------

    request : Optional[QNetworkRequest]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractOAuthPrivate::addContentTypeHeaders(QNetworkRequest
    #      *request)
    self.uglySide.call(
        'ritual_ZN21QAbstractOAuthPrivate21addContentTypeHeadersEP15QNetwor'
        'kRequest',
        self._addressOf(request),
    )

  @staticmethod
  def createQuery(*__, **_) -> Never:
    """
    Qt's 'QUrlQuery QAbstractOAuthPrivate::createQuery(const
    QMultiMap<QString, QVariant> &parameters)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractOAuthPrivate.createQuery' has no cute function yet. Qt's "
        "'QUrlQuery QAbstractOAuthPrivate::createQuery(const "
        "QMultiMap<QString, QVariant> &parameters)': takes a type Python "
        "has no way to hand over yet.")
