"""
QBluetoothServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothserver_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBluetoothServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBluetoothServer


class QBluetoothServerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothServerPrivate: a plain Python object
  standing in front of one C++ QBluetoothServerPrivate.

  What exists
  -----------

  Every function of Qt's QBluetoothServerPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', '_q_newConnection'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBluetoothServer *QBluetoothServerPrivate::q_func() const':
    takes in Python what 'QBluetoothServer
    *QBluetoothServerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  5 of the 8 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'vtable for QBluetoothSocketPrivateBluez', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QBluetoothServerPrivate is created at the first use, not by
    'QBluetoothServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothServerPrivate.
  - Each name of Qt's QBluetoothServerPrivate that has no cute function yet,
    '__init__', 'createSocketForServer', 'setSocketSecurityLevel',
    'socketSecurityLevel', holds a function that raises
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
  __qt_class__ = 'QBluetoothServerPrivate'

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
    Qt's 'QBluetoothServerPrivate::QBluetoothServerPrivate(
    QBluetoothServiceInfo::Protocol serverType, QBluetoothServer *parent)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QBluetoothServerPrivate.__init__' has no cute function yet. Qt's "
        "'QBluetoothServerPrivate::QBluetoothServerPrivate(QBluetoothService"
        "Info::Protocol serverType, QBluetoothServer *parent)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

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

  def q_func(self) -> Optional[QBluetoothServer]:
    """
    Calls Qt's 'QBluetoothServer *QBluetoothServerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserverprivate.html#q_func

    Returns
    -------

    Optional[QBluetoothServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothServer *QBluetoothServerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QBluetoothServerPrivate6q_funcEv',
    )
    from . import QBluetoothServer
    return QBluetoothServer._cuteAt(address)

  def _q_newConnection(self) -> None:
    """
    Calls Qt's 'void QBluetoothServerPrivate::_q_newConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserverprivate.html#_q_newConnection
    """
    #  void QBluetoothServerPrivate::_q_newConnection()
    self.uglySide.call(
        'ritual_ZN23QBluetoothServerPrivate16_q_newConnectionEv',
    )

  @staticmethod
  def createSocketForServer(*__, **_) -> Never:
    """
    Qt's 'QBluetoothSocket
    *QBluetoothServerPrivate::createSocketForServer(QBluetoothServiceInfo::
    Protocol socketType)': leans on 'vtable for
    QBluetoothSocketPrivateBluez', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServerPrivate.createSocketForServer' has no cute "
        "function yet. Qt's 'QBluetoothSocket "
        "*QBluetoothServerPrivate::createSocketForServer(QBluetoothServiceIn"
        "fo::Protocol socketType)': leans on 'vtable for "
        "QBluetoothSocketPrivateBluez', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSocketSecurityLevel(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServerPrivate::setSocketSecurityLevel(QBluetooth::SecurityFlags
    requestedSecLevel, int *errnoCode)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QBluetoothServerPrivate.setSocketSecurityLevel' has no cute "
        "function yet. Qt's 'void "
        "QBluetoothServerPrivate::setSocketSecurityLevel(QBluetooth::Securit"
        "yFlags requestedSecLevel, int *errnoCode)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def socketSecurityLevel(*__, **_) -> Never:
    """
    Qt's 'QBluetooth::SecurityFlags
    QBluetoothServerPrivate::socketSecurityLevel() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: variable has incomplete type 'struct bt_security'.
    """
    raise NotImplementedError(
        "'QBluetoothServerPrivate.socketSecurityLevel' has no cute function "
        "yet. Qt's 'QBluetooth::SecurityFlags "
        "QBluetoothServerPrivate::socketSecurityLevel() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: variable has incomplete type 'struct "
        "bt_security'.")
