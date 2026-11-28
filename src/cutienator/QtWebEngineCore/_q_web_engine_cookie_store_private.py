"""
QWebEngineCookieStorePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginecookiestore_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineCookieStorePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from ..QtNetwork import QNetworkCookie
  from . import QWebEngineCookieStore
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkCookie = WAIT['QNetworkCookie']
  QUrl = WAIT['QUrl']
  QWebEngineCookieStore = WAIT['QWebEngineCookieStore']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineCookieStorePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineCookieStorePrivate: a plain Python object
  standing in front of one C++ QWebEngineCookieStorePrivate.

  C++ hands a QWebEngineCookieStorePrivate around as a copy, so every C++
  QWebEngineCookieStorePrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineCookieStorePrivate that has a ritual and
  that Python can call so far, 10 names in all: 'q_func',
  'processPendingUserCookies', 'rejectPendingUserCookies', 'setCookie',
  'deleteCookie', 'deleteSessionCookies', 'deleteAllCookies',
  'getAllCookies', 'canAccessCookies', 'onCookieChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWebEngineCookieStore *QWebEngineCookieStorePrivate::q_func()
    const': takes in Python what 'QWebEngineCookieStore
    *QWebEngineCookieStorePrivate::q_func()' takes.
  - Qt's 'QWebEngineCookieStorePrivate::~QWebEngineCookieStorePrivate()': the
    destructor: Python removes its C++ QWebEngineCookieStorePrivate by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QWebEngineCookieStorePrivate is created at the first use, not by
    'QWebEngineCookieStorePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineCookieStorePrivate back gives a copy the
    ritual made for Python, in a new cute QWebEngineCookieStorePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineCookieStorePrivate'

  #  Qt's '~QWebEngineCookieStorePrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineCookieStorePrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QWebEngineCookieStorePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl, QUrl)
  def canAccessCookies(self, firstPartyUrl: QUrl, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QWebEngineCookieStorePrivate::canAccessCookies(const
    QUrl &firstPartyUrl, const QUrl &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#canAccessCookies

    Parameters
    ----------

    firstPartyUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QWebEngineCookieStorePrivate::canAccessCookies(const QUrl
    #      &firstPartyUrl, const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK28QWebEngineCookieStorePrivate16canAccessCookiesERK4QUrl'
        'S2_',
        self._valueOf(firstPartyUrl), self._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkCookie, QUrl)
  def setCookie(self, cookie: QNetworkCookie, origin: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStorePrivate::setCookie(const
    QNetworkCookie &cookie, const QUrl &origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#setCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.

    origin : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineCookieStorePrivate::setCookie(const QNetworkCookie
    #      &cookie, const QUrl &origin)
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate9setCookieERK14QNetworkCook'
        'ieRK4QUrl',
        self._valueOf(cookie), self._valueOf(origin),
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

  @overload(QWebEngineCookieStore)
  @overload(NoneType)
  def __init__(self, q: Optional[QWebEngineCookieStore]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineCookieStorePrivate::QWebEngineCookieStorePrivate(
    QWebEngineCookieStore *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html

    Parameters
    ----------

    q : Optional[QWebEngineCookieStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineCookieStorePrivate::QWebEngineCookieStorePrivate(
    #      QWebEngineCookieStore *q)
    self._noteCreation(QWebEngineCookieStorePrivate, lambda: Rituals.call(
        'ritual_ZN28QWebEngineCookieStorePrivateC1EP21QWebEngineCookieStore',
        self._addressOf(q),
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

  def q_func(self) -> Optional[QWebEngineCookieStore]:
    """
    Calls Qt's 'QWebEngineCookieStore
    *QWebEngineCookieStorePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#q_func

    Returns
    -------

    Optional[QWebEngineCookieStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineCookieStore *QWebEngineCookieStorePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate6q_funcEv',
    )
    from . import QWebEngineCookieStore
    return QWebEngineCookieStore._cuteAt(address)

  def processPendingUserCookies(self) -> None:
    """
    Calls Qt's 'void
    QWebEngineCookieStorePrivate::processPendingUserCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html
    """
    #  void QWebEngineCookieStorePrivate::processPendingUserCookies()
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate25processPendingUserCookies'
        'Ev',
    )

  def rejectPendingUserCookies(self) -> None:
    """
    Calls Qt's 'void
    QWebEngineCookieStorePrivate::rejectPendingUserCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html
    """
    #  void QWebEngineCookieStorePrivate::rejectPendingUserCookies()
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate24rejectPendingUserCookiesE'
        'v',
    )

  @overload(QNetworkCookie, QUrl)
  def deleteCookie(self, cookie: QNetworkCookie, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStorePrivate::deleteCookie(const
    QNetworkCookie &cookie, const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#deleteCookie

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebEngineCookieStorePrivate::deleteCookie(const QNetworkCookie
    #      &cookie, const QUrl &url)
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate12deleteCookieERK14QNetwork'
        'CookieRK4QUrl',
        self._valueOf(cookie), self._valueOf(url),
    )

  def deleteSessionCookies(self) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStorePrivate::deleteSessionCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html
    """
    #  void QWebEngineCookieStorePrivate::deleteSessionCookies()
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate20deleteSessionCookiesEv',
    )

  def deleteAllCookies(self) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStorePrivate::deleteAllCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#deleteAllCookies
    """
    #  void QWebEngineCookieStorePrivate::deleteAllCookies()
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate16deleteAllCookiesEv',
    )

  def getAllCookies(self) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStorePrivate::getAllCookies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#getAllCookies
    """
    #  void QWebEngineCookieStorePrivate::getAllCookies()
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate13getAllCookiesEv',
    )

  @overload(QNetworkCookie, bool)
  def onCookieChanged(self, cookie: QNetworkCookie, removed: bool) -> None:
    """
    Calls Qt's 'void QWebEngineCookieStorePrivate::onCookieChanged(const
    QNetworkCookie &cookie, bool removed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginecookiestoreprivate.html#onCookieChanged

    Parameters
    ----------

    cookie : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.

    removed : bool
      Passed on as it is.
    """
    #  void QWebEngineCookieStorePrivate::onCookieChanged(const
    #      QNetworkCookie &cookie, bool removed)
    self.uglySide.call(
        'ritual_ZN28QWebEngineCookieStorePrivate15onCookieChangedERK14QNetw'
        'orkCookieb',
        self._valueOf(cookie), removed,
    )
