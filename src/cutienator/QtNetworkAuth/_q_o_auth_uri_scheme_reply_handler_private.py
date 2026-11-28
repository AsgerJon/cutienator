"""
QOAuthUriSchemeReplyHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauthurischemereplyhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QOAuthUriSchemeReplyHandlerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QOAuthOobReplyHandlerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from . import QOAuthUriSchemeReplyHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QOAuthUriSchemeReplyHandlerPrivate(QOAuthOobReplyHandlerPrivate):
  """
  The cute side of Qt's QOAuthUriSchemeReplyHandlerPrivate: a plain Python
  object standing in front of one C++ QOAuthUriSchemeReplyHandlerPrivate.

  It is built on the cute 'QOAuthOobReplyHandlerPrivate', as Qt's
  QOAuthUriSchemeReplyHandlerPrivate is built on Qt's
  QOAuthOobReplyHandlerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOAuthUriSchemeReplyHandlerPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'q_func',
  'hasValidRedirectUrl', '_q_handleRedirectUrl'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOAuthUriSchemeReplyHandler
    *QOAuthUriSchemeReplyHandlerPrivate::q_func() const': takes in Python
    what 'QOAuthUriSchemeReplyHandler
    *QOAuthUriSchemeReplyHandlerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QOAuthUriSchemeReplyHandlerPrivate is created at the first use,
    not by 'QOAuthUriSchemeReplyHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOAuthUriSchemeReplyHandlerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuthUriSchemeReplyHandlerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasValidRedirectUrl(self) -> bool:
    """
    Calls Qt's 'bool
    QOAuthUriSchemeReplyHandlerPrivate::hasValidRedirectUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandlerprivate.html
    """
    #  bool QOAuthUriSchemeReplyHandlerPrivate::hasValidRedirectUrl() const
    return self.uglySide.call(
        'ritual_ZNK34QOAuthUriSchemeReplyHandlerPrivate19hasValidRedirectUr'
        'lEv',
    )

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

  def q_func(self) -> Optional[QOAuthUriSchemeReplyHandler]:
    """
    Calls Qt's 'QOAuthUriSchemeReplyHandler
    *QOAuthUriSchemeReplyHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandlerprivate.html#q_func

    Returns
    -------

    Optional[QOAuthUriSchemeReplyHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuthUriSchemeReplyHandler
    #      *QOAuthUriSchemeReplyHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN34QOAuthUriSchemeReplyHandlerPrivate6q_funcEv',
    )
    from . import QOAuthUriSchemeReplyHandler
    return QOAuthUriSchemeReplyHandler._cuteAt(address)

  @overload(QUrl)
  def _q_handleRedirectUrl(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool
    QOAuthUriSchemeReplyHandlerPrivate::_q_handleRedirectUrl(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthurischemereplyhandlerprivate.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QOAuthUriSchemeReplyHandlerPrivate::_q_handleRedirectUrl(const
    #      QUrl &url)
    return self.uglySide.call(
        'ritual_ZN34QOAuthUriSchemeReplyHandlerPrivate20_q_handleRedirectUr'
        'lERK4QUrl',
        self._valueOf(url),
    )
