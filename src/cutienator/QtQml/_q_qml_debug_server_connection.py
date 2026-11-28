"""
QQmlDebugServerConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugserverconnection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDebugServerConnection to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlDebugServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDebugServer = WAIT['QQmlDebugServer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDebugServerConnection(QObject):
  """
  The cute side of Qt's QQmlDebugServerConnection: a plain Python object
  standing in front of one C++ QQmlDebugServerConnection.

  It is built on the cute 'QObject', as Qt's QQmlDebugServerConnection is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDebugServerConnection that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'setServer',
  'setPortRange', 'setFileName', 'isConnected', 'disconnect',
  'waitForConnection', 'flush'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlDebugServerConnection::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlDebugServerConnection::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlDebugServerConnection::~QQmlDebugServerConnection()': the
    destructor: Python never removes a C++ QQmlDebugServerConnection.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlDebugServerConnection is created at the first use, not by
    'QQmlDebugServerConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDebugServerConnection.
  - Qt tells when it has removed the C++ QQmlDebugServerConnection. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQmlDebugServerConnection::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldebugserverconnection.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDebugServerConnection::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQmlDebugServerConnection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDebugServerConnection'

  #  A C++ QQmlDebugServerConnection Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDebugServerConnection'

  #  The functions Qt calls itself that QQmlDebugServerConnection is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setServer': (
          ('_ZN25QQmlDebugServerConnection9setServerEP15QQmlDebugServer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QQmlDebugServer'),
           )),
      ),
      'setPortRange': (
          ('_ZN25QQmlDebugServerConnection12setPortRangeEiibRK7QString',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('bool', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'setFileName': (
          ('_ZN25QQmlDebugServerConnection11setFileNameERK7QStringb',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'isConnected': (
          ('_ZNK25QQmlDebugServerConnection11isConnectedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'disconnect': (
          ('_ZN25QQmlDebugServerConnection10disconnectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'waitForConnection': (
          ('_ZN25QQmlDebugServerConnection17waitForConnectionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'flush': (
          ('_ZN25QQmlDebugServerConnection5flushEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlDebugServerConnection::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlDebugServerConnection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlDebugServerConnection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isConnected(self) -> bool:
    """
    Calls Qt's 'bool QQmlDebugServerConnection::isConnected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#isConnected
    """
    #  bool QQmlDebugServerConnection::isConnected() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlDebugServerConnection11isConnectedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlDebugServer)
  @overload(NoneType)
  def setServer(self, server: Optional[QQmlDebugServer]) -> None:
    """
    Calls Qt's 'void QQmlDebugServerConnection::setServer(QQmlDebugServer
    *server)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#setServer

    Parameters
    ----------

    server : Optional[QQmlDebugServer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDebugServerConnection::setServer(QQmlDebugServer *server)
    self.uglySide.call(
        'ritual_ZN25QQmlDebugServerConnection9setServerEP15QQmlDebugServer',
        self._addressOf(server),
    )

  @overload(int, int, bool, str)
  def setPortRange(
      self,
      portFrom: int,
      portTo: int,
      block: bool,
      hostaddress: str,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlDebugServerConnection::setPortRange(int portFrom,
    int portTo, bool block, const QString &hostaddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#setPortRange

    Parameters
    ----------

    portFrom : int
      Passed on as it is.

    portTo : int
      Passed on as it is.

    block : bool
      Passed on as it is.

    hostaddress : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlDebugServerConnection::setPortRange(int portFrom, int portTo,
    #      bool block, const QString &hostaddress)
    return self.uglySide.call(
        'ritual_ZN25QQmlDebugServerConnection12setPortRangeEiibRK7QString',
        portFrom, portTo, block, hostaddress,
    )

  @overload(str, bool)
  def setFileName(self, fileName: str, block: bool) -> bool:
    """
    Calls Qt's 'bool QQmlDebugServerConnection::setFileName(const QString
    &fileName, bool block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    block : bool
      Passed on as it is.
    """
    #  bool QQmlDebugServerConnection::setFileName(const QString &fileName,
    #      bool block)
    return self.uglySide.call(
        'ritual_ZN25QQmlDebugServerConnection11setFileNameERK7QStringb',
        fileName, block,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDebugServerConnection::QQmlDebugServerConnection(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlDebugServerConnection::QQmlDebugServerConnection(QObject *parent)
    self._noteCreation(QQmlDebugServerConnection, lambda: Rituals.call(
        'ritual_ZN25QQmlDebugServerConnectionC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def disconnect(self) -> None:
    """
    Calls Qt's 'void QQmlDebugServerConnection::disconnect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#disconnect
    """
    #  void QQmlDebugServerConnection::disconnect()
    self.uglySide.call('ritual_ZN25QQmlDebugServerConnection10disconnectEv')

  def waitForConnection(self) -> None:
    """
    Calls Qt's 'void QQmlDebugServerConnection::waitForConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#waitForConnection
    """
    #  void QQmlDebugServerConnection::waitForConnection()
    self.uglySide.call(
        'ritual_ZN25QQmlDebugServerConnection17waitForConnectionEv',
    )

  def flush(self) -> None:
    """
    Calls Qt's 'void QQmlDebugServerConnection::flush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugserverconnection.html#flush
    """
    #  void QQmlDebugServerConnection::flush()
    self.uglySide.call('ritual_ZN25QQmlDebugServerConnection5flushEv')
