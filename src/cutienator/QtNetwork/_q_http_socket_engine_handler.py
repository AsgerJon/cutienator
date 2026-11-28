"""
QHttpSocketEngineHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpSocketEngineHandler to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractSocket, QSocketEngineHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QAbstractSocketEngine, QNetworkProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkProxy = WAIT['QNetworkProxy']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpSocketEngineHandler(QSocketEngineHandler):
  """
  The cute side of Qt's QHttpSocketEngineHandler: a plain Python object
  standing in front of one C++ QHttpSocketEngineHandler.

  It is built on the cute 'QSocketEngineHandler', as Qt's
  QHttpSocketEngineHandler is built on Qt's QSocketEngineHandler, and has
  everything that class has.

  C++ hands a QHttpSocketEngineHandler around as a copy, so every C++
  QHttpSocketEngineHandler behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpSocketEngineHandler that has a ritual and that
  Python can call so far, 1 name in all: 'createSocketEngine'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpSocketEngineHandler::~QHttpSocketEngineHandler()': the
    destructor: Python removes its C++ QHttpSocketEngineHandler by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QHttpSocketEngineHandler is created at the first use, not by
    'QHttpSocketEngineHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpSocketEngineHandler back gives a copy the ritual
    made for Python, in a new cute QHttpSocketEngineHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpSocketEngineHandler'

  #  A C++ QHttpSocketEngineHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpSocketEngineHandler'

  #  Qt's '~QHttpSocketEngineHandler()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpSocketEngineHandler behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QHttpSocketEngineHandlerD1Ev'

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

  @overload(QAbstractSocket.SocketType, QNetworkProxy, QObject)
  @overload(QAbstractSocket.SocketType, QNetworkProxy, NoneType)
  def createSocketEngine(
      self,
      socketType: QAbstractSocket.SocketType,
      a1: QNetworkProxy,
      parent: Optional[QObject],
  ) -> Optional[QAbstractSocketEngine]:
    """
    Calls Qt's 'QAbstractSocketEngine
    *QHttpSocketEngineHandler::createSocketEngine(QAbstractSocket::SocketType
    socketType, const QNetworkProxy &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketenginehandler.html#createSocketEngine

    Parameters
    ----------

    socketType : QAbstractSocket.SocketType
      Passed on as its number.

    a1 : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractSocketEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSocketEngine
    #      *QHttpSocketEngineHandler::createSocketEngine(QAbstractSocket::
    #      SocketType socketType, const QNetworkProxy &a1, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN24QHttpSocketEngineHandler18createSocketEngineEN15QAbstra'
        'ctSocket10SocketTypeERK13QNetworkProxyP7QObject',
        socketType.value, self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QAbstractSocketEngine
    return QAbstractSocketEngine._cuteAt(address)

  @overload(int, QObject)
  @overload(int, NoneType)
  def createSocketEngine(
      self,
      socketDescripter: int,
      parent: Optional[QObject],
  ) -> Optional[QAbstractSocketEngine]:
    """
    Calls Qt's 'QAbstractSocketEngine
    *QHttpSocketEngineHandler::createSocketEngine(qintptr socketDescripter,
    QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpsocketenginehandler.html#createSocketEngine

    Parameters
    ----------

    socketDescripter : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractSocketEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSocketEngine
    #      *QHttpSocketEngineHandler::createSocketEngine(qintptr
    #      socketDescripter, QObject *parent)
    ritual = (
        'ritual_ZN24QHttpSocketEngineHandler18createSocketEngineExP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QHttpSocketEngineHandler18createSocketEngineExP7Q'
          'Object')
    address = self.uglySide.call(
        ritual, socketDescripter, self._addressOf(parent, 'QObject'),
    )
    from . import QAbstractSocketEngine
    return QAbstractSocketEngine._cuteAt(address)
