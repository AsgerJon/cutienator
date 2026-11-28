"""
QOAuth2AuthorizationCodeFlowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QOAuth2AuthorizationCodeFlowPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMap
from . import QAbstractOAuth2Private

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QUrl, QVariant
  from ..QtNetwork import QAuthenticator, QNetworkAccessManager
  from ..QtNetwork import QNetworkReply
  from . import QOAuth2AuthorizationCodeFlow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QNetworkAccessManager = WAIT['QNetworkAccessManager']
  QNetworkReply = WAIT['QNetworkReply']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuth2AuthorizationCodeFlowPrivate(QAbstractOAuth2Private):
  """
  The cute side of Qt's QOAuth2AuthorizationCodeFlowPrivate: a plain Python
  object standing in front of one C++ QOAuth2AuthorizationCodeFlowPrivate.

  It is built on the cute 'QAbstractOAuth2Private', as Qt's
  QOAuth2AuthorizationCodeFlowPrivate is built on Qt's
  QAbstractOAuth2Private, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuth2AuthorizationCodeFlowPrivate that has a
  ritual and that Python can call so far, 4 names in all: 'q_func',
  '_q_handleCallback', '_q_authenticate', 'createPKCEChallenge'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOAuth2AuthorizationCodeFlow
    *QOAuth2AuthorizationCodeFlowPrivate::q_func() const': takes in Python
    what 'QOAuth2AuthorizationCodeFlow
    *QOAuth2AuthorizationCodeFlowPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QOAuth2AuthorizationCodeFlowPrivate is created at the first use,
    not by 'QOAuth2AuthorizationCodeFlowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuth2AuthorizationCodeFlowPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth2AuthorizationCodeFlowPrivate'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl, QUrl, str)
  @overload(QUrl, QUrl, str, QNetworkAccessManager)
  @overload(QUrl, QUrl, str, NoneType)
  def __init__(
      self,
      authorizationUrl: QUrl,
      accessTokenUrl: QUrl,
      clientIdentifier: str,
      manager: Optional[QNetworkAccessManager] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QOAuth2AuthorizationCodeFlowPrivate::
    QOAuth2AuthorizationCodeFlowPrivate(const QUrl &authorizationUrl, const
    QUrl &accessTokenUrl, const QString &clientIdentifier,
    QNetworkAccessManager *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflowprivate.html

    Parameters
    ----------

    authorizationUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    accessTokenUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    clientIdentifier : str
      Passed on as it is: a QString is made of it for the call.

    manager : Optional[QNetworkAccessManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOAuth2AuthorizationCodeFlowPrivate::
    #      QOAuth2AuthorizationCodeFlowPrivate(const QUrl &authorizationUrl,
    #      const QUrl &accessTokenUrl, const QString &clientIdentifier,
    #      QNetworkAccessManager *manager)
    self._noteCreation(
        QOAuth2AuthorizationCodeFlowPrivate, lambda: Rituals.call(
            'ritual_ZN35QOAuth2AuthorizationCodeFlowPrivateC1ERK4QUrlS2_RK7'
            'QStringP21QNetworkAccessManager',
            self._valueOf(authorizationUrl), self._valueOf(accessTokenUrl),
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

  def q_func(self) -> Optional[QOAuth2AuthorizationCodeFlow]:
    """
    Calls Qt's 'QOAuth2AuthorizationCodeFlow
    *QOAuth2AuthorizationCodeFlowPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflowprivate.html#q_func

    Returns
    -------

    Optional[QOAuth2AuthorizationCodeFlow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuth2AuthorizationCodeFlow
    #      *QOAuth2AuthorizationCodeFlowPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate6q_funcEv',
    )
    from . import QOAuth2AuthorizationCodeFlow
    return QOAuth2AuthorizationCodeFlow._cuteAt(address)

  @overload(QMap[str, QVariant])
  def _q_handleCallback(self, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void
    QOAuth2AuthorizationCodeFlowPrivate::_q_handleCallback(const QVariantMap
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflowprivate.html

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QOAuth2AuthorizationCodeFlowPrivate::_q_handleCallback(const
    #      QVariantMap &data)
    self.uglySide.call(
        'ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate17_q_handleCallbackE'
        'RK4QMapI7QString8QVariantE',
        self._valueOf(data),
    )

  @overload(QNetworkReply, QAuthenticator)
  @overload(QNetworkReply, NoneType)
  @overload(NoneType, QAuthenticator)
  @overload(NoneType, NoneType)
  def _q_authenticate(
      self,
      reply: Optional[QNetworkReply],
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QOAuth2AuthorizationCodeFlowPrivate::_q_authenticate(QNetworkReply
    *reply, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflowprivate.html

    Parameters
    ----------

    reply : Optional[QNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QOAuth2AuthorizationCodeFlowPrivate::_q_authenticate(QNetworkReply
    #      *reply, QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate15_q_authenticateEP1'
        '3QNetworkReplyP14QAuthenticator',
        self._addressOf(reply), self._addressOf(authenticator),
    )

  def createPKCEChallenge(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QOAuth2AuthorizationCodeFlowPrivate::createPKCEChallenge()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth2authorizationcodeflowprivate.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth2AuthorizationCodeFlowPrivate::createPKCEChallenge()
    address = self.uglySide.call(
        'ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate19createPKCEChalleng'
        'eEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)
