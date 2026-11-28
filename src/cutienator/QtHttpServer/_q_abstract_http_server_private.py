"""
QAbstractHttpServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qabstracthttpserver_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAbstractHttpServerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractHttpServer


class QAbstractHttpServerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractHttpServerPrivate: a plain Python object
  standing in front of one C++ QAbstractHttpServerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QAbstractHttpServerPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractHttpServerPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func',
  'restartHeartbeatTimer'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractHttpServer *QAbstractHttpServerPrivate::q_func()
    const': takes in Python what 'QAbstractHttpServer
    *QAbstractHttpServerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  9 of the 13 functions Qt declares: 3 leans on
  'QHttpServerHttp1ProtocolHandler; 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'LessHostAddress; 1 leans on 'QHttpServerHttp2ProtocolHandler; 1 leans on
  'QAbstractHttpServerPrivate.

  What to expect
  --------------

  - The C++ QAbstractHttpServerPrivate is created at the first use, not by
    'QAbstractHttpServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractHttpServerPrivate.
  - Each name of Qt's QAbstractHttpServerPrivate that has no cute function
    yet, 'createHttp1Handler', 'createHttp2Handler', 'handleNewConnections',
    'handleNewLocalConnections', 'handleStartedEncryptionHandshake',
    'hasTooManyConnections', 'socketDisconnected', 'updateSocketCounter',
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
  __qt_class__ = 'QAbstractHttpServerPrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractHttpServerPrivate::QAbstractHttpServerPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserverprivate.html
    """
    #  QAbstractHttpServerPrivate::QAbstractHttpServerPrivate()
    self._noteCreation(QAbstractHttpServerPrivate, lambda: Rituals.call(
        'ritual_ZN26QAbstractHttpServerPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractHttpServer]:
    """
    Calls Qt's 'QAbstractHttpServer *QAbstractHttpServerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserverprivate.html#q_func

    Returns
    -------

    Optional[QAbstractHttpServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractHttpServer *QAbstractHttpServerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QAbstractHttpServerPrivate6q_funcEv',
    )
    from . import QAbstractHttpServer
    return QAbstractHttpServer._cuteAt(address)

  def restartHeartbeatTimer(self) -> None:
    """
    Calls Qt's 'void QAbstractHttpServerPrivate::restartHeartbeatTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracthttpserverprivate.html
    """
    #  void QAbstractHttpServerPrivate::restartHeartbeatTimer()
    self.uglySide.call(
        'ritual_ZN26QAbstractHttpServerPrivate21restartHeartbeatTimerEv',
    )

  @staticmethod
  def createHttp1Handler(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServerPrivate::createHttp1Handler(QIODevice
    *socket)': leans on 'QHttpServerHttp1ProtocolHandler::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.createHttp1Handler' has no cute "
        "function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::createHttp1Handler(QIODevice "
        "*socket)': leans on "
        "'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def createHttp2Handler(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServerPrivate::createHttp2Handler(QIODevice
    *socket)': leans on 'QHttpServerHttp2ProtocolHandler::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.createHttp2Handler' has no cute "
        "function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::createHttp2Handler(QIODevice "
        "*socket)': leans on "
        "'QHttpServerHttp2ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleNewConnections(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServerPrivate::handleNewConnections()': leans on
    'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.handleNewConnections' has no cute "
        "function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::handleNewConnections()': leans on "
        "'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleNewLocalConnections(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServerPrivate::handleNewLocalConnections()':
    leans on 'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.handleNewLocalConnections' has no cute "
        "function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::handleNewLocalConnections()': leans on "
        "'QHttpServerHttp1ProtocolHandler::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def handleStartedEncryptionHandshake(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractHttpServerPrivate::handleStartedEncryptionHandshake(QSslSocket
    *socket)': leans on
    'QAbstractHttpServerPrivate::hasTooManyConnections(QIODevice*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.handleStartedEncryptionHandshake' has "
        "no cute function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::handleStartedEncryptionHandshake(QSslSo"
        "cket *socket)': leans on "
        "'QAbstractHttpServerPrivate::hasTooManyConnections(QIODevice*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def hasTooManyConnections(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractHttpServerPrivate::hasTooManyConnections(QIODevice
    *socket)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'lcHttpServer';
    did you mean 'QHttpServer'?.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.hasTooManyConnections' has no cute "
        "function yet. Qt's 'bool "
        "QAbstractHttpServerPrivate::hasTooManyConnections(QIODevice "
        "*socket)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'lcHttpServer'; did you mean 'QHttpServer'?.")

  @staticmethod
  def socketDisconnected(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServerPrivate::socketDisconnected()': leans on
    'LessHostAddress::operator()(QHostAddress const&, QHostAddress const&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.socketDisconnected' has no cute "
        "function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::socketDisconnected()': leans on "
        "'LessHostAddress::operator()(QHostAddress const&, QHostAddress "
        "const&) const', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateSocketCounter(*__, **_) -> Never:
    """
    Qt's 'void QAbstractHttpServerPrivate::updateSocketCounter(QIODevice
    *socket)': leans on 'LessHostAddress::operator()(QHostAddress const&,
    QHostAddress const&) const', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.updateSocketCounter' has no cute "
        "function yet. Qt's 'void "
        "QAbstractHttpServerPrivate::updateSocketCounter(QIODevice "
        "*socket)': leans on 'LessHostAddress::operator()(QHostAddress "
        "const&, QHostAddress const&) const', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def verifyThreadAffinity(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractHttpServerPrivate::verifyThreadAffinity(const QObject
    *contextObject) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'lcHttpServer'; did you mean 'QHttpServer'?.
    """
    raise NotImplementedError(
        "'QAbstractHttpServerPrivate.verifyThreadAffinity' has no cute "
        "function yet. Qt's 'bool "
        "QAbstractHttpServerPrivate::verifyThreadAffinity(const QObject "
        "*contextObject) const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: unknown "
        "type name 'lcHttpServer'; did you mean 'QHttpServer'?.")
