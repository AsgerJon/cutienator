"""
QSocks5PasswordAuthenticator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSocks5PasswordAuthenticator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSocks5Authenticator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSocks5PasswordAuthenticator(QSocks5Authenticator):
  """
  The cute side of Qt's QSocks5PasswordAuthenticator: a plain Python object
  standing in front of one C++ QSocks5PasswordAuthenticator.

  It is built on the cute 'QSocks5Authenticator', as Qt's
  QSocks5PasswordAuthenticator is built on Qt's QSocks5Authenticator, and has
  everything that class has.

  C++ hands a QSocks5PasswordAuthenticator around as a copy, so every C++
  QSocks5PasswordAuthenticator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSocks5PasswordAuthenticator that has a ritual and
  that Python can call so far, 1 name in all: 'errorString'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'char QSocks5PasswordAuthenticator::methodId()': gives a single
    letter as C has it.
  - Qt's 'bool QSocks5PasswordAuthenticator::beginAuthenticate(QTcpSocket
    *socket, bool *completed)': takes a number to change where it is.
  - Qt's 'bool QSocks5PasswordAuthenticator::continueAuthenticate(QTcpSocket
    *socket, bool *completed)': takes a number to change where it is.
  - Qt's 'QSocks5PasswordAuthenticator::~QSocks5PasswordAuthenticator()': the
    destructor: Python removes its C++ QSocks5PasswordAuthenticator by it,
    and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'QSocks5PasswordAuthenticator.

  What to expect
  --------------

  - The C++ QSocks5PasswordAuthenticator is created at the first use, not by
    'QSocks5PasswordAuthenticator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSocks5PasswordAuthenticator back gives a copy the
    ritual made for Python, in a new cute QSocks5PasswordAuthenticator.
  - Each name of Qt's QSocks5PasswordAuthenticator that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSocks5PasswordAuthenticator'

  #  Qt's '~QSocks5PasswordAuthenticator()'. Naming it makes this a value
  #  class: Python owns every C++ QSocks5PasswordAuthenticator behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QSocks5PasswordAuthenticatorD1Ev'

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
    Qt's 'QSocks5PasswordAuthenticator::QSocks5PasswordAuthenticator(const
    QString &userName, const QString &password)': leans on
    'QSocks5PasswordAuthenticator::continueAuthenticate(QTcpSocket*, bool*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSocks5PasswordAuthenticator.__init__' has no cute function yet. "
        "Qt's "
        "'QSocks5PasswordAuthenticator::QSocks5PasswordAuthenticator(const "
        "QString &userName, const QString &password)': leans on "
        "'QSocks5PasswordAuthenticator::continueAuthenticate(QTcpSocket*, "
        "bool*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSocks5PasswordAuthenticator::errorString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5passwordauthenticator.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSocks5PasswordAuthenticator::errorString()
    ritual = 'ritual_ZN28QSocks5PasswordAuthenticator11errorStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QSocks5PasswordAuthenticator11errorStringEv'
    return self.uglySide.call(ritual)
