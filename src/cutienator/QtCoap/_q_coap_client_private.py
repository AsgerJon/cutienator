"""
QCoapClientPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapclient_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCoapClientPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCoapClient, QCoapConnection, QCoapProtocol
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCoapConnection = WAIT['QCoapConnection']
  QCoapProtocol = WAIT['QCoapProtocol']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapClientPrivate(QObjectPrivate):
  """
  The cute side of Qt's QCoapClientPrivate: a plain Python object standing in
  front of one C++ QCoapClientPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QCoapClientPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapClientPrivate that has a ritual and that Python
  can call so far, 1 name in all: 'q_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapClientPrivate::~QCoapClientPrivate()': the destructor: Python
    never removes a C++ QCoapClientPrivate.
  - Qt's 'const QCoapClient *QCoapClientPrivate::q_func() const': takes in
    Python what 'QCoapClient *QCoapClientPrivate::q_func()' takes.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 2 leans on 'QCoapClientPrivate; 1 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 1 leans on 'QCoapConnection.

  What to expect
  --------------

  - The C++ QCoapClientPrivate is created at the first use, not by
    'QCoapClientPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapClientPrivate.
  - Each name of Qt's QCoapClientPrivate that has no cute function yet,
    'send', 'sendDiscovery', 'sendRequest', 'setConnection', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapClientPrivate'

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

  @overload(QCoapProtocol, QCoapConnection)
  @overload(QCoapProtocol, NoneType)
  @overload(NoneType, QCoapConnection)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      protocol: Optional[QCoapProtocol],
      connection: Optional[QCoapConnection],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCoapClientPrivate::QCoapClientPrivate(QCoapProtocol *protocol,
    QCoapConnection *connection)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapclientprivate.html#QCoapClientPrivate

    Parameters
    ----------

    protocol : Optional[QCoapProtocol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    connection : Optional[QCoapConnection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCoapClientPrivate::QCoapClientPrivate(QCoapProtocol *protocol,
    #      QCoapConnection *connection)
    self._noteCreation(QCoapClientPrivate, lambda: Rituals.call(
        'ritual_ZN18QCoapClientPrivateC1EP13QCoapProtocolP15QCoapConnection',
        self._addressOf(protocol), self._addressOf(connection),
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

  def q_func(self) -> Optional[QCoapClient]:
    """
    Calls Qt's 'QCoapClient *QCoapClientPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapclientprivate.html#q_func

    Returns
    -------

    Optional[QCoapClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapClient *QCoapClientPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QCoapClientPrivate6q_funcEv')
    from . import QCoapClient
    return QCoapClient._cuteAt(address)

  @staticmethod
  def send(*__, **_) -> Never:
    """
    Qt's 'bool QCoapClientPrivate::send(QCoapReply *reply)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'lcCoapClient'; did you mean 'QCoapClient'?.
    """
    raise NotImplementedError(
        "'QCoapClientPrivate.send' has no cute function yet. Qt's 'bool "
        "QCoapClientPrivate::send(QCoapReply *reply)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'lcCoapClient'; did you mean "
        "'QCoapClient'?.")

  @staticmethod
  def sendDiscovery(*__, **_) -> Never:
    """
    Qt's 'QCoapResourceDiscoveryReply
    *QCoapClientPrivate::sendDiscovery(const QCoapRequest &request)': leans
    on 'QCoapClientPrivate::send(QCoapReply*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapClientPrivate.sendDiscovery' has no cute function yet. Qt's "
        "'QCoapResourceDiscoveryReply "
        "*QCoapClientPrivate::sendDiscovery(const QCoapRequest &request)': "
        "leans on 'QCoapClientPrivate::send(QCoapReply*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def sendRequest(*__, **_) -> Never:
    """
    Qt's 'QCoapReply *QCoapClientPrivate::sendRequest(const QCoapRequest
    &request)': leans on 'QCoapClientPrivate::send(QCoapReply*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCoapClientPrivate.sendRequest' has no cute function yet. Qt's "
        "'QCoapReply *QCoapClientPrivate::sendRequest(const QCoapRequest "
        "&request)': leans on 'QCoapClientPrivate::send(QCoapReply*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setConnection(*__, **_) -> Never:
    """
    Qt's 'void QCoapClientPrivate::setConnection(QCoapConnection
    *customConnection)': leans on 'QCoapConnection::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCoapClientPrivate.setConnection' has no cute function yet. Qt's "
        "'void QCoapClientPrivate::setConnection(QCoapConnection "
        "*customConnection)': leans on 'QCoapConnection::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
