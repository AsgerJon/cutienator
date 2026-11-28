"""
QHttpProtocolHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpprotocolhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpProtocolHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QAbstractProtocolHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QHttpProtocolHandler(QAbstractProtocolHandler):
  """
  The cute side of Qt's QHttpProtocolHandler: a plain Python object standing
  in front of one C++ QHttpProtocolHandler.

  It is built on the cute 'QAbstractProtocolHandler', as Qt's
  QHttpProtocolHandler is built on Qt's QAbstractProtocolHandler, and has
  everything that class has.

  C++ hands a QHttpProtocolHandler around as a copy, so every C++
  QHttpProtocolHandler behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpProtocolHandler that has a ritual and that
  Python can call so far, 3 names in all: '_q_receiveReply', '_q_readyRead',
  'sendRequest'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpProtocolHandler::~QHttpProtocolHandler()': the destructor:
    Python removes its C++ QHttpProtocolHandler by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'Http2.

  What to expect
  --------------

  - The C++ QHttpProtocolHandler is created at the first use, not by
    'QHttpProtocolHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpProtocolHandler back gives a copy the ritual
    made for Python, in a new cute QHttpProtocolHandler.
  - Each name of Qt's QHttpProtocolHandler that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpProtocolHandler'

  #  Qt's '~QHttpProtocolHandler()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpProtocolHandler behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QHttpProtocolHandlerD1Ev'

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
    Qt's
    'QHttpProtocolHandler::QHttpProtocolHandler(QHttpNetworkConnectionChannel
    *channel)': leans on 'Http2::is_protocol_upgraded(QHttpNetworkReply
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpProtocolHandler.__init__' has no cute function yet. Qt's "
        "'QHttpProtocolHandler::QHttpProtocolHandler(QHttpNetworkConnectionC"
        "hannel *channel)': leans on "
        "'Http2::is_protocol_upgraded(QHttpNetworkReply const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void QHttpProtocolHandler::_q_receiveReply()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpprotocolhandler.html#_q_receiveReply
    """
    #  void QHttpProtocolHandler::_q_receiveReply()
    self.uglySide.call('ritual_ZN20QHttpProtocolHandler15_q_receiveReplyEv')

  def _q_readyRead(self) -> None:
    """
    Calls Qt's 'void QHttpProtocolHandler::_q_readyRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpprotocolhandler.html#_q_readyRead
    """
    #  void QHttpProtocolHandler::_q_readyRead()
    self.uglySide.call('ritual_ZN20QHttpProtocolHandler12_q_readyReadEv')

  def sendRequest(self) -> bool:
    """
    Calls Qt's 'bool QHttpProtocolHandler::sendRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpprotocolhandler.html#sendRequest
    """
    #  bool QHttpProtocolHandler::sendRequest()
    return self.uglySide.call(
        'ritual_ZN20QHttpProtocolHandler11sendRequestEv',
    )
