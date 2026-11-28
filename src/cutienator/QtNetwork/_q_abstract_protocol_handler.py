"""
QAbstractProtocolHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qabstractprotocolhandler_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAbstractProtocolHandler to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QHttpNetworkConnectionChannel, QHttpNetworkReply
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttpNetworkConnectionChannel = WAIT['QHttpNetworkConnectionChannel']
  QHttpNetworkReply = WAIT['QHttpNetworkReply']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractProtocolHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractProtocolHandler: a plain Python object
  standing in front of one C++ QAbstractProtocolHandler.

  What exists
  -----------

  Every function of Qt's QAbstractProtocolHandler that has a ritual and that
  Python can call so far, 5 names in all: '_q_receiveReply', '_q_readyRead',
  'sendRequest', 'tryRemoveReply', 'setReply'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractProtocolHandler::~QAbstractProtocolHandler()': the
    destructor: Python never removes a C++ QAbstractProtocolHandler.

  What to expect
  --------------

  - The C++ QAbstractProtocolHandler is created at the first use, not by
    'QAbstractProtocolHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractProtocolHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractProtocolHandler'

  #  A C++ QAbstractProtocolHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractProtocolHandler'

  #  The functions Qt calls itself that QAbstractProtocolHandler is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      '_q_receiveReply': (
          ('_ZN24QAbstractProtocolHandler15_q_receiveReplyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      '_q_readyRead': (
          ('_ZN24QAbstractProtocolHandler12_q_readyReadEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'sendRequest': (
          ('_ZN24QAbstractProtocolHandler11sendRequestEv',
           ('bool', 'number', ''),
           ()),
      ),
      'tryRemoveReply': (
          ('_ZN24QAbstractProtocolHandler14tryRemoveReplyEP17QHttpNetworkRe'
           'ply',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QHttpNetworkReply'),
           )),
      ),
  }

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

  @overload(QHttpNetworkReply)
  @overload(NoneType)
  def setReply(self, reply: Optional[QHttpNetworkReply]) -> None:
    """
    Calls Qt's 'void QAbstractProtocolHandler::setReply(QHttpNetworkReply
    *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotocolhandler.html#setReply

    Parameters
    ----------

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
    self._callAs(
        'QAbstractProtocolHandler',
        'ritual_ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply',
        self._addressOf(reply),
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

  @overload(QHttpNetworkConnectionChannel)
  @overload(NoneType)
  def __init__(
      self,
      channel: Optional[QHttpNetworkConnectionChannel],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractProtocolHandler::QAbstractProtocolHandler(
    QHttpNetworkConnectionChannel *channel)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotocolhandler.html

    Parameters
    ----------

    channel : Optional[QHttpNetworkConnectionChannel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractProtocolHandler::QAbstractProtocolHandler(
    #      QHttpNetworkConnectionChannel *channel)
    self._noteCreation(QAbstractProtocolHandler, lambda: Rituals.call(
        'ritual_ZN24QAbstractProtocolHandlerC1EP29QHttpNetworkConnectionCha'
        'nnel',
        self._addressOf(channel),
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

  def _q_receiveReply(self) -> None:
    """
    Calls Qt's 'void QAbstractProtocolHandler::_q_receiveReply()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotocolhandler.html#_q_receiveReply
    """
    #  void QAbstractProtocolHandler::_q_receiveReply()
    self._callAs(
        'QAbstractProtocolHandler',
        'ritual_ZN24QAbstractProtocolHandler15_q_receiveReplyEv',
    )

  def _q_readyRead(self) -> None:
    """
    Calls Qt's 'void QAbstractProtocolHandler::_q_readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotocolhandler.html#_q_readyRead
    """
    #  void QAbstractProtocolHandler::_q_readyRead()
    self._callAs(
        'QAbstractProtocolHandler',
        'ritual_ZN24QAbstractProtocolHandler12_q_readyReadEv',
    )

  def sendRequest(self) -> bool:
    """
    Calls Qt's 'bool QAbstractProtocolHandler::sendRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotocolhandler.html#sendRequest
    """
    #  bool QAbstractProtocolHandler::sendRequest()
    return self._callAs(
        'QAbstractProtocolHandler',
        'ritual_ZN24QAbstractProtocolHandler11sendRequestEv',
    )

  @overload(QHttpNetworkReply)
  @overload(NoneType)
  def tryRemoveReply(self, reply: Optional[QHttpNetworkReply]) -> bool:
    """
    Calls Qt's 'bool
    QAbstractProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotocolhandler.html#tryRemoveReply

    Parameters
    ----------

    reply : Optional[QHttpNetworkReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractProtocolHandler::tryRemoveReply(QHttpNetworkReply
    #      *reply)
    ritual = (
        'ritual_ZN24QAbstractProtocolHandler14tryRemoveReplyEP17QHttpNetwor'
        'kReply')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractProtocolHandler14tryRemoveReplyEP17QHttp'
          'NetworkReply')
    return self._callAs(
        'QAbstractProtocolHandler', ritual, self._addressOf(reply),
    )
