"""
QSocketEngineHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSocketEngineHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QSocketEngineHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSocketEngineHandler: a plain Python object standing
  in front of one C++ QSocketEngineHandler.

  What exists
  -----------

  Every function of Qt's QSocketEngineHandler that has a ritual and that
  Python can call so far, 1 name in all: 'createSocketEngine'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSocketEngineHandler::~QSocketEngineHandler()': the destructor:
    Python never removes a C++ QSocketEngineHandler.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSocketEngineHandler is created at the first use, not by
    'QSocketEngineHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSocketEngineHandler.
  - Each name of Qt's QSocketEngineHandler that has no cute function yet,
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
  __qt_class__ = 'QSocketEngineHandler'

  #  A C++ QSocketEngineHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSocketEngineHandler'

  #  The functions Qt calls itself that QSocketEngineHandler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createSocketEngine': (
          ('_ZN20QSocketEngineHandler18createSocketEngineEN15QAbstractSocke'
           't10SocketTypeERK13QNetworkProxyP7QObject',
           ('address', 'address', 'QtNetwork:QAbstractSocketEngine'),
           (
               ('int', 'enum', 'QtNetwork:QAbstractSocket.SocketType'),
               ('address', 'value', 'QtNetwork:QNetworkProxy'),
               ('address', 'address', 'QtCore:QObject'),
           )),
          ('_ZN20QSocketEngineHandler18createSocketEngineExP7QObject',
           ('address', 'address', 'QtNetwork:QAbstractSocketEngine'),
           (
               ('long long', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
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
    Qt's 'QSocketEngineHandler::QSocketEngineHandler()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'socketHandlers'.
    """
    raise NotImplementedError(
        "'QSocketEngineHandler.__init__' has no cute function yet. Qt's "
        "'QSocketEngineHandler::QSocketEngineHandler()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'socketHandlers'.")

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
    *QSocketEngineHandler::createSocketEngine(QAbstractSocket::SocketType
    socketType, const QNetworkProxy &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocketenginehandler.html#createSocketEngine

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
    #      *QSocketEngineHandler::createSocketEngine(QAbstractSocket::
    #      SocketType socketType, const QNetworkProxy &a1, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN20QSocketEngineHandler18createSocketEngineEN15QAbstractSo'
        'cket10SocketTypeERK13QNetworkProxyP7QObject',
        socketType.value, self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QAbstractSocketEngine
    return QAbstractSocketEngine._cuteAt(address)

  @overload(int, QObject)
  @overload(int, NoneType)
  def createSocketEngine(
      self,
      socketDescriptor: int,
      parent: Optional[QObject],
  ) -> Optional[QAbstractSocketEngine]:
    """
    Calls Qt's 'QAbstractSocketEngine
    *QSocketEngineHandler::createSocketEngine(qintptr socketDescriptor,
    QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocketenginehandler.html#createSocketEngine

    Parameters
    ----------

    socketDescriptor : int
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
    #      *QSocketEngineHandler::createSocketEngine(qintptr
    #      socketDescriptor, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN20QSocketEngineHandler18createSocketEngineExP7QObject',
        socketDescriptor, self._addressOf(parent, 'QObject'),
    )
    from . import QAbstractSocketEngine
    return QAbstractSocketEngine._cuteAt(address)
