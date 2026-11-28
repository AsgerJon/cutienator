"""
QHttpServerRouterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrouter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpServerRouterPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractHttpServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractHttpServer = WAIT['QAbstractHttpServer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpServerRouterPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerRouterPrivate: a plain Python object
  standing in front of one C++ QHttpServerRouterPrivate.

  C++ hands a QHttpServerRouterPrivate around as a copy, so every C++
  QHttpServerRouterPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QHttpServerRouterPrivate yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpServerRouterPrivate::~QHttpServerRouterPrivate()': the
    destructor: Python removes its C++ QHttpServerRouterPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QHttpServerRouterPrivate is created at the first use, not by
    'QHttpServerRouterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerRouterPrivate back gives a copy the ritual
    made for Python, in a new cute QHttpServerRouterPrivate.
  - Each name of Qt's QHttpServerRouterPrivate that has no cute function yet,
    'verifyThreadAffinity', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerRouterPrivate'

  #  Qt's '~QHttpServerRouterPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpServerRouterPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QHttpServerRouterPrivateD1Ev'

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

  @overload(QAbstractHttpServer)
  @overload(NoneType)
  def __init__(self, server: Optional[QAbstractHttpServer]) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRouterPrivate::QHttpServerRouterPrivate(QAbstractHttpServer
    *server)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrouterprivate.html

    Parameters
    ----------

    server : Optional[QAbstractHttpServer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QHttpServerRouterPrivate::QHttpServerRouterPrivate(QAbstractHttpServer
    #      *server)
    self._noteCreation(QHttpServerRouterPrivate, lambda: Rituals.call(
        'ritual_ZN24QHttpServerRouterPrivateC1EP19QAbstractHttpServer',
        self._addressOf(server),
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

  @staticmethod
  def verifyThreadAffinity(*__, **_) -> Never:
    """
    Qt's 'bool QHttpServerRouterPrivate::verifyThreadAffinity(const QObject
    *contextObject) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'lcRouter'.
    """
    raise NotImplementedError(
        "'QHttpServerRouterPrivate.verifyThreadAffinity' has no cute "
        "function yet. Qt's 'bool "
        "QHttpServerRouterPrivate::verifyThreadAffinity(const QObject "
        "*contextObject) const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'lcRouter'.")
