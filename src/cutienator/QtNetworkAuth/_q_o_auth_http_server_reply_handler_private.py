"""
QOAuthHttpServerReplyHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QOAuthHttpServerReplyHandlerPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from ..QtNetwork import QHostAddress, QTcpSocket
  from . import QOAuthHttpServerReplyHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QOAuthHttpServerReplyHandler = WAIT['QOAuthHttpServerReplyHandler']
  QTcpSocket = WAIT['QTcpSocket']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOAuthHttpServerReplyHandlerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOAuthHttpServerReplyHandlerPrivate: a plain Python
  object standing in front of one C++ QOAuthHttpServerReplyHandlerPrivate.

  C++ hands a QOAuthHttpServerReplyHandlerPrivate around as a copy, so every
  C++ QOAuthHttpServerReplyHandlerPrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QOAuthHttpServerReplyHandlerPrivate that has a
  ritual and that Python can call so far, 8 names in all: 'q_func',
  'callback', 'callbackHost', '_q_clientConnected', '_q_readData',
  '_q_answerClient', 'initializeLocalServer', 'listen'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOAuthHttpServerReplyHandler
    *QOAuthHttpServerReplyHandlerPrivate::q_func() const': takes in Python
    what 'QOAuthHttpServerReplyHandler
    *QOAuthHttpServerReplyHandlerPrivate::q_func()' takes.
  - Qt's 'QOAuthHttpServerReplyHandlerPrivate::
    ~QOAuthHttpServerReplyHandlerPrivate()': the destructor: Python removes
    its C++ QOAuthHttpServerReplyHandlerPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOAuthHttpServerReplyHandlerPrivate is created at the first use,
    not by 'QOAuthHttpServerReplyHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOAuthHttpServerReplyHandlerPrivate back gives a copy
    the ritual made for Python, in a new cute
    QOAuthHttpServerReplyHandlerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuthHttpServerReplyHandlerPrivate'

  #  Qt's '~QOAuthHttpServerReplyHandlerPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QOAuthHttpServerReplyHandlerPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN35QOAuthHttpServerReplyHandlerPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def callback(self) -> str:
    """
    Calls Qt's 'QString QOAuthHttpServerReplyHandlerPrivate::callback()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html#callback

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthHttpServerReplyHandlerPrivate::callback() const
    return self.uglySide.call(
        'ritual_ZNK35QOAuthHttpServerReplyHandlerPrivate8callbackEv',
    )

  def callbackHost(self) -> str:
    """
    Calls Qt's 'QString QOAuthHttpServerReplyHandlerPrivate::callbackHost()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOAuthHttpServerReplyHandlerPrivate::callbackHost() const
    return self.uglySide.call(
        'ritual_ZNK35QOAuthHttpServerReplyHandlerPrivate12callbackHostEv',
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

  @overload(QOAuthHttpServerReplyHandler)
  @overload(NoneType)
  def __init__(self, p: Optional[QOAuthHttpServerReplyHandler]) -> None:
    """
    Notes what was given, for Qt's 'QOAuthHttpServerReplyHandlerPrivate::
    QOAuthHttpServerReplyHandlerPrivate(QOAuthHttpServerReplyHandler *p)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html

    Parameters
    ----------

    p : Optional[QOAuthHttpServerReplyHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOAuthHttpServerReplyHandlerPrivate::
    #      QOAuthHttpServerReplyHandlerPrivate(QOAuthHttpServerReplyHandler
    #      *p)
    self._noteCreation(
        QOAuthHttpServerReplyHandlerPrivate, lambda: Rituals.call(
            'ritual_ZN35QOAuthHttpServerReplyHandlerPrivateC1EP28QOAuthHttp'
            'ServerReplyHandler',
            self._addressOf(p),
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

  def q_func(self) -> Optional[QOAuthHttpServerReplyHandler]:
    """
    Calls Qt's 'QOAuthHttpServerReplyHandler
    *QOAuthHttpServerReplyHandlerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html#q_func

    Returns
    -------

    Optional[QOAuthHttpServerReplyHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOAuthHttpServerReplyHandler
    #      *QOAuthHttpServerReplyHandlerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN35QOAuthHttpServerReplyHandlerPrivate6q_funcEv',
    )
    from . import QOAuthHttpServerReplyHandler
    return QOAuthHttpServerReplyHandler._cuteAt(address)

  def _q_clientConnected(self) -> None:
    """
    Calls Qt's 'void
    QOAuthHttpServerReplyHandlerPrivate::_q_clientConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html
    """
    #  void QOAuthHttpServerReplyHandlerPrivate::_q_clientConnected()
    self.uglySide.call(
        'ritual_ZN35QOAuthHttpServerReplyHandlerPrivate18_q_clientConnected'
        'Ev',
    )

  @overload(QTcpSocket)
  @overload(NoneType)
  def _q_readData(self, socket: Optional[QTcpSocket]) -> None:
    """
    Calls Qt's 'void
    QOAuthHttpServerReplyHandlerPrivate::_q_readData(QTcpSocket *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html

    Parameters
    ----------

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOAuthHttpServerReplyHandlerPrivate::_q_readData(QTcpSocket
    #      *socket)
    self.uglySide.call(
        'ritual_ZN35QOAuthHttpServerReplyHandlerPrivate11_q_readDataEP10QTc'
        'pSocket',
        self._addressOf(socket),
    )

  @overload(QTcpSocket, QUrl)
  @overload(NoneType, QUrl)
  def _q_answerClient(self, socket: Optional[QTcpSocket], url: QUrl) -> None:
    """
    Calls Qt's 'void
    QOAuthHttpServerReplyHandlerPrivate::_q_answerClient(QTcpSocket *socket,
    const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html

    Parameters
    ----------

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QOAuthHttpServerReplyHandlerPrivate::_q_answerClient(QTcpSocket
    #      *socket, const QUrl &url)
    self.uglySide.call(
        'ritual_ZN35QOAuthHttpServerReplyHandlerPrivate15_q_answerClientEP1'
        '0QTcpSocketRK4QUrl',
        self._addressOf(socket), self._valueOf(url),
    )

  def initializeLocalServer(self) -> None:
    """
    Calls Qt's 'void
    QOAuthHttpServerReplyHandlerPrivate::initializeLocalServer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html
    """
    #  void QOAuthHttpServerReplyHandlerPrivate::initializeLocalServer()
    self.uglySide.call(
        'ritual_ZN35QOAuthHttpServerReplyHandlerPrivate21initializeLocalSer'
        'verEv',
    )

  @overload(QHostAddress, int)
  def listen(self, address: QHostAddress, port: int) -> bool:
    """
    Calls Qt's 'bool QOAuthHttpServerReplyHandlerPrivate::listen(const
    QHostAddress &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauthhttpserverreplyhandlerprivate.html#listen

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QOAuthHttpServerReplyHandlerPrivate::listen(const QHostAddress
    #      &address, quint16 port)
    return self.uglySide.call(
        'ritual_ZN35QOAuthHttpServerReplyHandlerPrivate6listenERK12QHostAdd'
        'resst',
        self._valueOf(address), port,
    )
