"""
QNetworkAccessAuthenticationManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessauthenticationmanager_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QNetworkAccessAuthenticationManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QNetworkAccessAuthenticationManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkAccessAuthenticationManager: a plain Python
  object standing in front of one C++ QNetworkAccessAuthenticationManager.

  What exists
  -----------

  No function of Qt's QNetworkAccessAuthenticationManager yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  6 of the 6 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'vtable for QNetworkAccessCache', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken; 1 leans on
  'QNetworkAccessCache.

  What to expect
  --------------

  - The C++ QNetworkAccessAuthenticationManager is created at the first use,
    not by 'QNetworkAccessAuthenticationManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessAuthenticationManager.
  - Each name of Qt's QNetworkAccessAuthenticationManager that has no cute
    function yet, '__init__', 'cacheCredentials', 'cacheProxyCredentials',
    'clearCache', 'fetchCachedCredentials', 'fetchCachedProxyCredentials',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessAuthenticationManager'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNetworkAccessAuthenticationManager::
    QNetworkAccessAuthenticationManager()': leans on 'vtable for
    QNetworkAccessCache', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessAuthenticationManager.__init__' has no cute "
        "function yet. Qt's "
        "'QNetworkAccessAuthenticationManager::QNetworkAccessAuthenticationM"
        "anager()': leans on 'vtable for QNetworkAccessCache', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @staticmethod
  def cacheCredentials(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessAuthenticationManager::cacheCredentials(const
    QUrl &url, const QAuthenticator *auth)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: unknown
    type name 'QNetworkAuthenticationCache'; did you mean
    'QNetworkAuthenticationCredential'?.
    """
    raise NotImplementedError(
        "'QNetworkAccessAuthenticationManager.cacheCredentials' has no cute "
        "function yet. Qt's 'void "
        "QNetworkAccessAuthenticationManager::cacheCredentials(const QUrl "
        "&url, const QAuthenticator *auth)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: unknown type name 'QNetworkAuthenticationCache'; did you "
        "mean 'QNetworkAuthenticationCredential'?.")

  @staticmethod
  def cacheProxyCredentials(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkAccessAuthenticationManager::cacheProxyCredentials(const
    QNetworkProxy &proxy, const QAuthenticator *auth)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'QNetworkAuthenticationCache'; did you mean
    'QNetworkAuthenticationCredential'?.
    """
    raise NotImplementedError(
        "'QNetworkAccessAuthenticationManager.cacheProxyCredentials' has no "
        "cute function yet. Qt's 'void "
        "QNetworkAccessAuthenticationManager::cacheProxyCredentials(const "
        "QNetworkProxy &proxy, const QAuthenticator *auth)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name "
        "'QNetworkAuthenticationCache'; did you mean "
        "'QNetworkAuthenticationCredential'?.")

  @staticmethod
  def clearCache(*__, **_) -> Never:
    """
    Qt's 'void QNetworkAccessAuthenticationManager::clearCache()': leans on
    'QNetworkAccessCache::clear()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkAccessAuthenticationManager.clearCache' has no cute "
        "function yet. Qt's 'void "
        "QNetworkAccessAuthenticationManager::clearCache()': leans on "
        "'QNetworkAccessCache::clear()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def fetchCachedCredentials(*__, **_) -> Never:
    """
    Qt's 'QNetworkAuthenticationCredential
    QNetworkAccessAuthenticationManager::fetchCachedCredentials(const QUrl
    &url, const QAuthenticator *auth)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'authenticationKey'.
    """
    raise NotImplementedError(
        "'QNetworkAccessAuthenticationManager.fetchCachedCredentials' has "
        "no cute function yet. Qt's 'QNetworkAuthenticationCredential "
        "QNetworkAccessAuthenticationManager::fetchCachedCredentials(const "
        "QUrl &url, const QAuthenticator *auth)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'authenticationKey'.")

  @staticmethod
  def fetchCachedProxyCredentials(*__, **_) -> Never:
    """
    Qt's 'QNetworkAuthenticationCredential
    QNetworkAccessAuthenticationManager::fetchCachedProxyCredentials(const
    QNetworkProxy &proxy, const QAuthenticator *auth)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'proxyAuthenticationKey'.
    """
    raise NotImplementedError(
        "'QNetworkAccessAuthenticationManager.fetchCachedProxyCredentials' "
        "has no cute function yet. Qt's 'QNetworkAuthenticationCredential "
        "QNetworkAccessAuthenticationManager::fetchCachedProxyCredentials(co"
        "nst QNetworkProxy &proxy, const QAuthenticator *auth)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'proxyAuthenticationKey'.")
