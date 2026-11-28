"""
QSslServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSslServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QTcpServerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSslServer, QSslSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslSocket = WAIT['QSslSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSslServerPrivate(QTcpServerPrivate):
  """
  The cute side of Qt's QSslServerPrivate: a plain Python object standing in
  front of one C++ QSslServerPrivate.

  It is built on the cute 'QTcpServerPrivate', as Qt's QSslServerPrivate is
  built on Qt's QTcpServerPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSslServerPrivate that has a ritual and that Python
  can call so far, 6 names in all: 'q_func', 'checkClientHelloAndContinue',
  'initializeHandshakeProcess', 'removeSocketData',
  'handleHandshakeTimedOut', 'totalPendingConnections'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSslServer *QSslServerPrivate::q_func() const': takes in
    Python what 'QSslServer *QSslServerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QSslServerPrivate is created at the first use, not by
    'QSslServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSslServerPrivate.
  """

  #  The classes Qt writes inside QSslServerPrivate, each a class in here as
  #  in C++.

  class SocketData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSslServerPrivate::SocketData: a plain Python
    object standing in front of one C++ QSslServerPrivate::SocketData.

    C++ hands a QSslServerPrivate::SocketData around as a copy, so every C++
    QSslServerPrivate::SocketData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSslServerPrivate::SocketData that has a ritual
    and that Python can call so far, 1 name in all: 'disconnectSignals'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSslServerPrivate::SocketData::SocketData(QMetaObject::Connection
      readyRead, QMetaObject::Connection destroyed, std::shared_ptr<QTimer>
      &&timer)': takes a type Python has no way to hand over yet.
    - Qt's 'QSslServerPrivate::SocketData::~SocketData()': the destructor:
      Python removes its C++ QSslServerPrivate::SocketData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSslServerPrivate::SocketData is created at the first use, not
      by 'QSslServerPrivate::SocketData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSslServerPrivate::SocketData back gives a copy the
      ritual made for Python, in a new cute QSslServerPrivate::SocketData.
    - Each name of Qt's QSslServerPrivate::SocketData that has no cute
      function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSslServerPrivate::SocketData'

    #  Qt's '~QSslServerPrivate::SocketData()'. Naming it makes this a value
    #  class: Python owns every C++ QSslServerPrivate::SocketData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QSslServerPrivate10SocketDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QSslServerPrivate::SocketData::SocketData(QMetaObject::Connection
      readyRead, QMetaObject::Connection destroyed, std::shared_ptr<QTimer>
      &&timer)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QSslServerPrivate.SocketData.__init__' has no cute function "
          "yet. Qt's "
          "'QSslServerPrivate::SocketData::SocketData(QMetaObject::Connectio"
          "n readyRead, QMetaObject::Connection destroyed, "
          "std::shared_ptr<QTimer> &&timer)': takes a type Python has no "
          "way to hand over yet.")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def disconnectSignals(self) -> None:
      """
      Calls Qt's 'void QSslServerPrivate::SocketData::disconnectSignals()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsslserverprivate-socketdata.html
      """
      #  void QSslServerPrivate::SocketData::disconnectSignals()
      self.uglySide.call(
          'ritual_ZN17QSslServerPrivate10SocketData17disconnectSignalsEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslServerPrivate'

  #  A C++ QSslServerPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSslServerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def totalPendingConnections(self) -> int:
    """
    Calls Qt's 'int QSslServerPrivate::totalPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserverprivate.html#totalPendingConnections
    """
    #  int QSslServerPrivate::totalPendingConnections() const
    ritual = 'ritual_ZNK17QSslServerPrivate23totalPendingConnectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSslServerPrivate23totalPendingConnectionsEv'
    return self.uglySide.call(ritual)

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
    Notes what was given, for Qt's 'QSslServerPrivate::QSslServerPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserverprivate.html#QSslServerPrivate
    """
    #  QSslServerPrivate::QSslServerPrivate()
    self._noteCreation(QSslServerPrivate, lambda: Rituals.call(
        'ritual_ZN17QSslServerPrivateC1Ev',
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

  def q_func(self) -> Optional[QSslServer]:
    """
    Calls Qt's 'QSslServer *QSslServerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsslserverprivate.html#q_func

    Returns
    -------

    Optional[QSslServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSslServer *QSslServerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QSslServerPrivate6q_funcEv')
    from . import QSslServer
    return QSslServer._cuteAt(address)

  def checkClientHelloAndContinue(self) -> None:
    """
    Calls Qt's 'void QSslServerPrivate::checkClientHelloAndContinue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserverprivate.html#checkClientHelloAndContinue
    """
    #  void QSslServerPrivate::checkClientHelloAndContinue()
    self.uglySide.call(
        'ritual_ZN17QSslServerPrivate27checkClientHelloAndContinueEv',
    )

  @overload(QSslSocket)
  @overload(NoneType)
  def initializeHandshakeProcess(self, socket: Optional[QSslSocket]) -> None:
    """
    Calls Qt's 'void QSslServerPrivate::initializeHandshakeProcess(QSslSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserverprivate.html#initializeHandshakeProcess

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslServerPrivate::initializeHandshakeProcess(QSslSocket *socket)
    self.uglySide.call(
        'ritual_ZN17QSslServerPrivate26initializeHandshakeProcessEP10QSslSo'
        'cket',
        self._addressOf(socket),
    )

  @overload(int)
  def removeSocketData(self, socket: int) -> None:
    """
    Calls Qt's 'void QSslServerPrivate::removeSocketData(quintptr socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserverprivate.html#removeSocketData

    Parameters
    ----------

    socket : int
      Passed on as it is.
    """
    #  void QSslServerPrivate::removeSocketData(quintptr socket)
    self.uglySide.call(
        'ritual_ZN17QSslServerPrivate16removeSocketDataEy', socket,
    )

  @overload(QSslSocket)
  @overload(NoneType)
  def handleHandshakeTimedOut(self, socket: Optional[QSslSocket]) -> None:
    """
    Calls Qt's 'void QSslServerPrivate::handleHandshakeTimedOut(QSslSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslserverprivate.html#handleHandshakeTimedOut

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSslServerPrivate::handleHandshakeTimedOut(QSslSocket *socket)
    self.uglySide.call(
        'ritual_ZN17QSslServerPrivate23handleHandshakeTimedOutEP10QSslSocke'
        't',
        self._addressOf(socket),
    )
