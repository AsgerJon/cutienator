"""
QObjectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QObjectPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QList, QObjectData, QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBindingStatus, QMetaMethod, QMetaProperty, QObject
  from . import QThreadData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBindingStatus = WAIT['QBindingStatus']
  QMetaMethod = WAIT['QMetaMethod']
  QMetaProperty = WAIT['QMetaProperty']
  QObject = WAIT['QObject']
  QThreadData = WAIT['QThreadData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectPrivate(QObjectData):
  """
  The cute side of Qt's QObjectPrivate: a plain Python object standing in
  front of one C++ QObjectPrivate.

  It is built on the cute 'QObjectData', as Qt's QObjectPrivate is built on
  Qt's QObjectData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QObjectPrivate that has a ritual and that Python can
  call so far, 20 names in all: 'q_func', 'ensureExtraData',
  'setObjectNameWithoutBindings', 'deleteChildren', 'clearBindingStorage',
  'setParent_helper', 'moveToThread_helper', 'setThreadData_helper',
  'receiverList', 'ensureConnectionData', 'addConnection', 'get',
  'deleteInOwnThread', 'isSignalConnected', 'maybeSignalConnected',
  'isDeclarativeSignalConnected', 'connectNotify', 'disconnectNotify',
  'reinitBindingStorageAfterThreadMove', 'getPropertyAdaptorSlotObject'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QObject *QObjectPrivate::q_func() const': takes in Python
    what 'QObject *QObjectPrivate::q_func()' takes.
  - Qt's 'QObjectPrivate::QObjectPrivate(decltype(QObjectPrivateVersion)
    version)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
  - Qt's 'QObjectPrivate::~QObjectPrivate()': the destructor: Python never
    removes a C++ QObjectPrivate.
  - Qt's 'const QObjectPrivate *QObjectPrivate::get(const QObject *o)': takes
    in Python what 'QObjectPrivate *QObjectPrivate::get(QObject *o)' takes.
  - Qt's 'int QObjectPrivate::signalIndex(const char *signalName, const
    QMetaObject **meta) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QMetaObject::Connection QObjectPrivate::connectImpl(const QObject
    *sender, int signal_index, const QObject *receiver, void **slot,
    QtPrivate::QSlotObjectBase *slotObj, int type, const int *types, const
    QMetaObject *senderMetaObject)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QMetaObject::Connection QObjectPrivate::connect(const QObject
    *sender, int signal_index, QtPrivate::QSlotObjectBase *slotObj,
    Qt::ConnectionType type)': names 'QtPrivate::QSlotObjectBase', which has
    no cute class yet.
  - Qt's 'QMetaObject::Connection QObjectPrivate::connect(const QObject
    *sender, int signal_index, const QObject *receiver,
    QtPrivate::QSlotObjectBase *slotObj, Qt::ConnectionType type)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
  - Qt's 'bool QObjectPrivate::disconnect(const QObject *sender, int
    signal_index, void **slot)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QObjectPrivate::disconnect(const QObject *sender, int
    signal_index, const QObject *receiver, void **slot)': takes a type Python
    has no way to hand over yet.
  - Qt's 'std::string QObjectPrivate::flagsForDumping() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QObjectPrivate::writeToDebugStream(QDebug &a0) const': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 35 functions Qt declares: 2 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QObjectPrivate is created at the first use, not by
    'QObjectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QObjectPrivate.
  - Each name of Qt's QObjectPrivate that has no cute function yet,
    '__init__', 'connect', 'connectImpl', 'disconnect', 'flagsForDumping',
    'removeConnection', 'signalIndex', 'writeToDebugStream', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QObjectPrivate, each a class in here as in
  #  C++.

  class Connection(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::Connection: a plain Python object
    standing in front of one C++ QObjectPrivate::Connection.

    What exists
    -----------

    Every function of Qt's QObjectPrivate::Connection that has a ritual and
    that Python can call so far, 3 names in all: 'method', 'ref',
    'freeSlotObject'. It can be made from Python, in 1 way; see '__init__'.

    What has no ritual
    ------------------

    2 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file; 1 leans on
    'QObjectPrivate.

    What to expect
    --------------

    - The C++ QObjectPrivate::Connection is created at the first use, not by
      'QObjectPrivate::Connection(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QObjectPrivate::Connection.
    - Each name of Qt's QObjectPrivate::Connection that has no cute function
      yet, 'deref', holds a function that raises 'NotImplementedError', and
      its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::Connection'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def method(self) -> int:
      """
      Calls Qt's 'int QObjectPrivate::Connection::method() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-connection.html#method
      """
      #  int QObjectPrivate::Connection::method() const
      return self.uglySide.call(
          'ritual_ZNK14QObjectPrivate10Connection6methodEv',
      )

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QObjectPrivate::Connection::Connection()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-connection.html#Connection
      """
      #  QObjectPrivate::Connection::Connection()
      self._noteCreation(QObjectPrivate.Connection, lambda: Rituals.call(
          'ritual_ZN14QObjectPrivate10ConnectionC1Ev',
      ))

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

    def ref(self) -> None:
      """
      Calls Qt's 'void QObjectPrivate::Connection::ref()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-connection.html#ref
      """
      #  void QObjectPrivate::Connection::ref()
      self.uglySide.call('ritual_ZN14QObjectPrivate10Connection3refEv')

    def freeSlotObject(self) -> None:
      """
      Calls Qt's 'void QObjectPrivate::Connection::freeSlotObject()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-connection.html#freeSlotObject
      """
      #  void QObjectPrivate::Connection::freeSlotObject()
      self.uglySide.call(
          'ritual_ZN14QObjectPrivate10Connection14freeSlotObjectEv',
      )

    @staticmethod
    def deref(*__, **_) -> Never:
      """
      Qt's 'void QObjectPrivate::Connection::deref()': leans on
      'QObjectPrivate::Connection::~Connection()', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
      """
      raise NotImplementedError(
          "'QObjectPrivate.Connection.deref' has no cute function yet. Qt's "
          "'void QObjectPrivate::Connection::deref()': leans on "
          "'QObjectPrivate::Connection::~Connection()', which Qt's source "
          "does not mark for use from outside Qt and has no code for that "
          "could be taken.")

  class ConnectionData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::ConnectionData: a plain Python
    object standing in front of one C++ QObjectPrivate::ConnectionData.

    What exists
    -----------

    Every function of Qt's QObjectPrivate::ConnectionData that has a ritual
    and that Python can call so far, 2 names in all: 'resizeSignalVector',
    'signalVectorCount'. None can be made from Python: one comes out of a
    function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'ConnectionList
      &QObjectPrivate::ConnectionData::connectionsForSignal(int signal)':
      gives a type Python has no way to take yet.

    What has no ritual
    ------------------

    5 of the 8 functions Qt declares: 3 leans on 'QObjectPrivate; 1 Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file; 1 leans on 'QThreadData.

    What to expect
    --------------

    - The C++ QObjectPrivate::ConnectionData is created at the first use, not
      by 'QObjectPrivate::ConnectionData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QObjectPrivate::ConnectionData.
    - Each name of Qt's QObjectPrivate::ConnectionData that has no cute
      function yet, 'cleanOrphanedConnections',
      'cleanOrphanedConnectionsImpl', 'connectionsForSignal',
      'deleteOrphaned', 'removeConnection', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The enums Qt writes inside QObjectPrivate::ConnectionData, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class LockPolicy(CuteNum):
      """
      The enum 'QObjectPrivate::ConnectionData::LockPolicy' of Qt, with the 2
      names Qt gives in it.
      """

      NeedToLock = Kee[int](0)
      AlreadyLockedAndTemporarilyReleasingLock = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::ConnectionData'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def signalVectorCount(self) -> int:
      """
      Calls Qt's 'int QObjectPrivate::ConnectionData::signalVectorCount()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-connectiondata.html
      """
      #  int QObjectPrivate::ConnectionData::signalVectorCount() const
      return self.uglySide.call(
          'ritual_ZNK14QObjectPrivate14ConnectionData17signalVectorCountEv',
      )

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

    @overload(int)
    def resizeSignalVector(self, size: int) -> None:
      """
      Calls Qt's 'void
      QObjectPrivate::ConnectionData::resizeSignalVector(size_t size)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-connectiondata.html

      Parameters
      ----------

      size : int
        Passed on as it is.
      """
      #  void QObjectPrivate::ConnectionData::resizeSignalVector(size_t size)
      self.uglySide.call(
          'ritual_ZN14QObjectPrivate14ConnectionData18resizeSignalVectorEm',
          size,
      )

    @staticmethod
    def cleanOrphanedConnections(*__, **_) -> Never:
      """
      Qt's 'void
      QObjectPrivate::ConnectionData::cleanOrphanedConnections(QObject
      *sender, LockPolicy lockPolicy)': leans on
      'QObjectPrivate::ConnectionData::cleanOrphanedConnectionsImpl(QObject*,
      QObjectPrivate::ConnectionData::LockPolicy)', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
      """
      raise NotImplementedError(
          "'QObjectPrivate.ConnectionData.cleanOrphanedConnections' has no "
          "cute function yet. Qt's 'void "
          "QObjectPrivate::ConnectionData::cleanOrphanedConnections(QObject "
          "*sender, LockPolicy lockPolicy)': leans on "
          "'QObjectPrivate::ConnectionData::cleanOrphanedConnectionsImpl(QOb"
          "ject*, QObjectPrivate::ConnectionData::LockPolicy)', which Qt's "
          "source does not mark for use from outside Qt and has no code for "
          "that could be taken.")

    @staticmethod
    def cleanOrphanedConnectionsImpl(*__, **_) -> Never:
      """
      Qt's 'void
      QObjectPrivate::ConnectionData::cleanOrphanedConnectionsImpl(QObject
      *sender, LockPolicy lockPolicy)': Qt's library has no name for it, and
      its code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'signalSlotLock'.
      """
      raise NotImplementedError(
          "'QObjectPrivate.ConnectionData.cleanOrphanedConnectionsImpl' has "
          "no cute function yet. Qt's 'void "
          "QObjectPrivate::ConnectionData::cleanOrphanedConnectionsImpl(QObj"
          "ect *sender, LockPolicy lockPolicy)': Qt's library has no name "
          "for it, and its code in Qt's source does not compile apart from "
          "its file: use of undeclared identifier 'signalSlotLock'.")

    @staticmethod
    def connectionsForSignal(*__, **_) -> Never:
      """
      Qt's 'ConnectionList
      &QObjectPrivate::ConnectionData::connectionsForSignal(int signal)':
      gives a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QObjectPrivate.ConnectionData.connectionsForSignal' has no cute "
          "function yet. Qt's 'ConnectionList "
          "&QObjectPrivate::ConnectionData::connectionsForSignal(int "
          "signal)': gives a type Python has no way to take yet.")

    @staticmethod
    def deleteOrphaned(*__, **_) -> Never:
      """
      Qt's 'void
      QObjectPrivate::ConnectionData::deleteOrphaned(TaggedSignalVector o)':
      leans on 'QObjectPrivate::Connection::~Connection()', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
      """
      raise NotImplementedError(
          "'QObjectPrivate.ConnectionData.deleteOrphaned' has no cute "
          "function yet. Qt's 'void "
          "QObjectPrivate::ConnectionData::deleteOrphaned(TaggedSignalVector"
          " o)': leans on 'QObjectPrivate::Connection::~Connection()', "
          "which Qt's source does not mark for use from outside Qt and has "
          "no code for that could be taken.")

    @staticmethod
    def removeConnection(*__, **_) -> Never:
      """
      Qt's 'void QObjectPrivate::ConnectionData::removeConnection(Connection
      *c)': leans on 'QThreadData::clearCurrentThreadData()', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
      """
      raise NotImplementedError(
          "'QObjectPrivate.ConnectionData.removeConnection' has no cute "
          "function yet. Qt's 'void "
          "QObjectPrivate::ConnectionData::removeConnection(Connection "
          "*c)': leans on 'QThreadData::clearCurrentThreadData()', which "
          "Qt's source does not mark for use from outside Qt and has no "
          "code for that could be taken.")

  class ConnectionList(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::ConnectionList: a plain Python
    object standing in front of one C++ QObjectPrivate::ConnectionList.

    C++ hands a QObjectPrivate::ConnectionList around as a copy, so every C++
    QObjectPrivate::ConnectionList behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QObjectPrivate::ConnectionList yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QObjectPrivate::ConnectionList::~ConnectionList()': the
      destructor: Python removes its C++ QObjectPrivate::ConnectionList by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QObjectPrivate::ConnectionList is created at the first use, not
      by 'QObjectPrivate::ConnectionList(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QObjectPrivate::ConnectionList back gives a copy
      the ritual made for Python, in a new cute
      QObjectPrivate::ConnectionList.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::ConnectionList'

    #  Qt's '~QObjectPrivate::ConnectionList()'. Naming it makes this a value
    #  class: Python owns every C++ QObjectPrivate::ConnectionList behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QObjectPrivate14ConnectionListD1Ev'

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

  class ConnectionOrSignalVector(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::ConnectionOrSignalVector: a plain
    Python object standing in front of one C++
    QObjectPrivate::ConnectionOrSignalVector.

    C++ hands a QObjectPrivate::ConnectionOrSignalVector around as a copy, so
    every C++ QObjectPrivate::ConnectionOrSignalVector behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QObjectPrivate::ConnectionOrSignalVector yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QObjectPrivate::ConnectionOrSignalVector::~ConnectionOrSignalVector(
      )': the destructor: Python removes its C++
      QObjectPrivate::ConnectionOrSignalVector by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QObjectPrivate::ConnectionOrSignalVector is created at the
      first use, not by 'QObjectPrivate::ConnectionOrSignalVector(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QObjectPrivate::ConnectionOrSignalVector back gives
      a copy the ritual made for Python, in a new cute
      QObjectPrivate::ConnectionOrSignalVector.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::ConnectionOrSignalVector'

    #  Qt's '~QObjectPrivate::ConnectionOrSignalVector()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QObjectPrivate::ConnectionOrSignalVector behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN14QObjectPrivate24ConnectionOrSignalVectorD1Ev')

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

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::ExtraData: a plain Python object
    standing in front of one C++ QObjectPrivate::ExtraData.

    C++ hands a QObjectPrivate::ExtraData around as a copy, so every C++
    QObjectPrivate::ExtraData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QObjectPrivate::ExtraData that has a ritual and
    that Python can call so far, 3 names in all: 'setObjectNameForwarder',
    'nameChangedForwarder', '_qt_property_objectName_offset'. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QObjectPrivate::ExtraData::~ExtraData()': the destructor: Python
      removes its C++ QObjectPrivate::ExtraData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QObjectPrivate::ExtraData is created at the first use, not by
      'QObjectPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QObjectPrivate::ExtraData back gives a copy the
      ritual made for Python, in a new cute QObjectPrivate::ExtraData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QObjectPrivate = WAIT['QObjectPrivate']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def _qt_property_objectName_offset() -> int:
      """
      Calls Qt's 'size_t
      QObjectPrivate::ExtraData::_qt_property_objectName_offset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-extradata.html
      """
      #  size_t QObjectPrivate::ExtraData::_qt_property_objectName_offset()
      return Rituals.call(
          'ritual_ZN14QObjectPrivate9ExtraData30_qt_property_objectName_off'
          'setEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::ExtraData'

    #  Qt's '~QObjectPrivate::ExtraData()'. Naming it makes this a value
    #  class: Python owns every C++ QObjectPrivate::ExtraData behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QObjectPrivate9ExtraDataD1Ev'

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

    @overload(str)
    def setObjectNameForwarder(self, name: str) -> None:
      """
      Calls Qt's 'void
      QObjectPrivate::ExtraData::setObjectNameForwarder(const QString
      &name)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-extradata.html

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QObjectPrivate::ExtraData::setObjectNameForwarder(const QString
      #      &name)
      self.uglySide.call(
          'ritual_ZN14QObjectPrivate9ExtraData22setObjectNameForwarderERK7Q'
          'String',
          name,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QObjectPrivate)
    @overload(NoneType)
    def __init__(self, ptr: Optional[QObjectPrivate]) -> None:
      """
      Notes what was given, for Qt's
      'QObjectPrivate::ExtraData::ExtraData(QObjectPrivate *ptr)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-extradata.html#ExtraData

      Parameters
      ----------

      ptr : Optional[QObjectPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QObjectPrivate::ExtraData::ExtraData(QObjectPrivate *ptr)
      self._noteCreation(QObjectPrivate.ExtraData, lambda: Rituals.call(
          'ritual_ZN14QObjectPrivate9ExtraDataC1EPS_',
          self._addressOf(ptr, 'QObjectPrivate'),
      ))

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

    @overload(str)
    def nameChangedForwarder(self, name: str) -> None:
      """
      Calls Qt's 'void QObjectPrivate::ExtraData::nameChangedForwarder(const
      QString &name)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-extradata.html

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QObjectPrivate::ExtraData::nameChangedForwarder(const QString
      #      &name)
      self.uglySide.call(
          'ritual_ZN14QObjectPrivate9ExtraData20nameChangedForwarderERK7QSt'
          'ring',
          name,
      )

  class Sender(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::Sender: a plain Python object
    standing in front of one C++ QObjectPrivate::Sender.

    C++ hands a QObjectPrivate::Sender around as a copy, so every C++
    QObjectPrivate::Sender behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QObjectPrivate::Sender that has a ritual and that
    Python can call so far, 1 name in all: 'receiverDeleted'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QObjectPrivate::Sender::Sender(QObject *receiver, QObject
      *sender, int signal, ConnectionData *receiverConnections)': names
      'QObjectPrivate::ConnectionData', which stands beside this class inside
      'QObjectPrivate' and cannot be named from here.
    - Qt's 'QObjectPrivate::Sender::~Sender()': the destructor: Python
      removes its C++ QObjectPrivate::Sender by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QObjectPrivate::Sender is created at the first use, not by
      'QObjectPrivate::Sender(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QObjectPrivate::Sender back gives a copy the ritual
      made for Python, in a new cute QObjectPrivate::Sender.
    - Each name of Qt's QObjectPrivate::Sender that has no cute function yet,
      '__init__', holds a function that raises 'NotImplementedError', and its
      docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::Sender'

    #  Qt's '~QObjectPrivate::Sender()'. Naming it makes this a value class:
    #  Python owns every C++ QObjectPrivate::Sender behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QObjectPrivate6SenderD1Ev'

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
      Qt's 'QObjectPrivate::Sender::Sender(QObject *receiver, QObject
      *sender, int signal, ConnectionData *receiverConnections)': names
      'QObjectPrivate::ConnectionData', which stands beside this class inside
      'QObjectPrivate' and cannot be named from here.
      """
      raise NotImplementedError(
          "'QObjectPrivate.Sender.__init__' has no cute function yet. Qt's "
          "'QObjectPrivate::Sender::Sender(QObject *receiver, QObject "
          "*sender, int signal, ConnectionData *receiverConnections)': "
          "names 'QObjectPrivate::ConnectionData', which stands beside this "
          "class inside 'QObjectPrivate' and cannot be named from here.")

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

    def receiverDeleted(self) -> None:
      """
      Calls Qt's 'void QObjectPrivate::Sender::receiverDeleted()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-sender.html#receiverDeleted
      """
      #  void QObjectPrivate::Sender::receiverDeleted()
      self.uglySide.call(
          'ritual_ZN14QObjectPrivate6Sender15receiverDeletedEv',
      )

  class SignalVector(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::SignalVector: a plain Python object
    standing in front of one C++ QObjectPrivate::SignalVector.

    C++ hands a QObjectPrivate::SignalVector around as a copy, so every C++
    QObjectPrivate::SignalVector behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QObjectPrivate::SignalVector that has a ritual and
    that Python can call so far, 1 name in all: 'count'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'ConnectionList &QObjectPrivate::SignalVector::at(int i)': gives a
      type Python has no way to take yet.
    - Qt's 'const ConnectionList &QObjectPrivate::SignalVector::at(int i)
      const': gives 'QObjectPrivate::ConnectionList', which stands beside
      this class inside 'QObjectPrivate' and cannot be named from here.
    - Qt's 'QObjectPrivate::SignalVector::~SignalVector()': the destructor:
      Python removes its C++ QObjectPrivate::SignalVector by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QObjectPrivate::SignalVector is created at the first use, not
      by 'QObjectPrivate::SignalVector(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QObjectPrivate::SignalVector back gives a copy the
      ritual made for Python, in a new cute QObjectPrivate::SignalVector.
    - Each name of Qt's QObjectPrivate::SignalVector that has no cute
      function yet, 'at', holds a function that raises 'NotImplementedError',
      and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::SignalVector'

    #  Qt's '~QObjectPrivate::SignalVector()'. Naming it makes this a value
    #  class: Python owns every C++ QObjectPrivate::SignalVector behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QObjectPrivate12SignalVectorD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def count(self) -> int:
      """
      Calls Qt's 'int QObjectPrivate::SignalVector::count() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-signalvector.html#count
      """
      #  int QObjectPrivate::SignalVector::count() const
      return self.uglySide.call(
          'ritual_ZNK14QObjectPrivate12SignalVector5countEv',
      )

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

    @staticmethod
    def at(*__, **_) -> Never:
      """
      - Qt's 'ConnectionList &QObjectPrivate::SignalVector::at(int i)': gives
        a type Python has no way to take yet.
      - Qt's 'const ConnectionList &QObjectPrivate::SignalVector::at(int i)
        const': gives 'QObjectPrivate::ConnectionList', which stands beside
        this class inside 'QObjectPrivate' and cannot be named from here.
      """
      raise NotImplementedError(
          "'QObjectPrivate.SignalVector.at' has no cute function yet. Qt's "
          "'ConnectionList &QObjectPrivate::SignalVector::at(int i)': gives "
          "a type Python has no way to take yet. Qt's 'const ConnectionList "
          "&QObjectPrivate::SignalVector::at(int i) const': gives "
          "'QObjectPrivate::ConnectionList', which stands beside this class "
          "inside 'QObjectPrivate' and cannot be named from here.")

  class TaggedSignalVector(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QObjectPrivate::TaggedSignalVector: a plain Python
    object standing in front of one C++ QObjectPrivate::TaggedSignalVector.

    C++ hands a QObjectPrivate::TaggedSignalVector around as a copy, so every
    C++ QObjectPrivate::TaggedSignalVector behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QObjectPrivate::TaggedSignalVector yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QObjectPrivate::TaggedSignalVector::TaggedSignalVector(std::nullptr_t
      a0)': takes in Python what
      'QObjectPrivate::TaggedSignalVector::TaggedSignalVector()' takes.
    - Qt's 'QObjectPrivate::TaggedSignalVector::TaggedSignalVector(Connection
      *v)': names 'QObjectPrivate::Connection', which stands beside this
      class inside 'QObjectPrivate' and cannot be named from here.
    - Qt's
      'QObjectPrivate::TaggedSignalVector::TaggedSignalVector(SignalVector
      *v)': names 'QObjectPrivate::SignalVector', which stands beside this
      class inside 'QObjectPrivate' and cannot be named from here.
    - Qt's 'SignalVector *QObjectPrivate::TaggedSignalVector::operator
      QObjectPrivate::SignalVector *() const': an operator Python has no name
      for.
    - Qt's 'Connection *QObjectPrivate::TaggedSignalVector::operator
      QObjectPrivate::Connection *() const': an operator Python has no name
      for.
    - Qt's 'uintptr_t QObjectPrivate::TaggedSignalVector::operator unsigned
      long() const': an operator Python has no name for.
    - Qt's 'QObjectPrivate::TaggedSignalVector::~TaggedSignalVector()': the
      destructor: Python removes its C++ QObjectPrivate::TaggedSignalVector
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QObjectPrivate::TaggedSignalVector is created at the first use,
      not by 'QObjectPrivate::TaggedSignalVector(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QObjectPrivate::TaggedSignalVector back gives a
      copy the ritual made for Python, in a new cute
      QObjectPrivate::TaggedSignalVector.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QObjectPrivate::TaggedSignalVector'

    #  Qt's '~QObjectPrivate::TaggedSignalVector()'. Naming it makes this a
    #  value class: Python owns every C++ QObjectPrivate::TaggedSignalVector
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QObjectPrivate18TaggedSignalVectorD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QObjectPrivate::TaggedSignalVector::TaggedSignalVector()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qobjectprivate-taggedsignalvector.html
      """
      #  QObjectPrivate::TaggedSignalVector::TaggedSignalVector()
      self._noteCreation(
          QObjectPrivate.TaggedSignalVector, lambda: Rituals.call(
              'ritual_ZN14QObjectPrivate18TaggedSignalVectorC1Ev',
          ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def get(o: Optional[QObject]) -> Optional[QObjectPrivate]:
    """
    Calls Qt's 'QObjectPrivate *QObjectPrivate::get(QObject *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectprivate.html#get

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObjectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectPrivate *QObjectPrivate::get(QObject *o)
    address = Rituals.call(
        'ritual_ZN14QObjectPrivate3getEP7QObject',
        CuteMixin._addressOf(o, 'QObject'),
    )
    return QObjectPrivate._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def deleteInOwnThread(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectPrivate::deleteInOwnThread(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#deleteInOwnThread

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectPrivate::deleteInOwnThread(QObject *object)
    Rituals.call(
        'ritual_ZN14QObjectPrivate17deleteInOwnThreadEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QObjectPrivate'

  #  The functions Qt calls itself that QObjectPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'flagsForDumping': (
          'std::string QObjectPrivate::flagsForDumping() const',
      ),
      'writeToDebugStream': (
          'void QObjectPrivate::writeToDebugStream(QDebug &) const',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(NoneType)
  def receiverList(self, signal: Optional[str]) -> QList[QObject]:
    """
    Calls Qt's 'QObjectList QObjectPrivate::receiverList(const char *signal)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectprivate.html#receiverList

    Parameters
    ----------

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QObjectList QObjectPrivate::receiverList(const char *signal) const
    address = self._callAs(
        'QObjectPrivate', 'ritual_ZNK14QObjectPrivate12receiverListEPKc',
        self._bytesOf(signal),
    )
    from . import QObject
    return QList[QObject]._cuteOwning(address)

  @overload(int)
  @overload(int, bool)
  def isSignalConnected(
      self,
      signalIdx: int,
      checkDeclarative: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QObjectPrivate::isSignalConnected(uint signalIdx, bool
    checkDeclarative) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#isSignalConnected

    Parameters
    ----------

    signalIdx : int
      Passed on as it is.

    checkDeclarative : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QObjectPrivate::isSignalConnected(uint signalIdx, bool
    #      checkDeclarative) const
    return self._callAs(
        'QObjectPrivate', 'ritual_ZNK14QObjectPrivate17isSignalConnectedEjb',
        signalIdx, checkDeclarative,
    )

  @overload(int)
  def maybeSignalConnected(self, signalIndex: int) -> bool:
    """
    Calls Qt's 'bool QObjectPrivate::maybeSignalConnected(uint signalIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#maybeSignalConnected

    Parameters
    ----------

    signalIndex : int
      Passed on as it is.
    """
    #  bool QObjectPrivate::maybeSignalConnected(uint signalIndex) const
    return self._callAs(
        'QObjectPrivate',
        'ritual_ZNK14QObjectPrivate20maybeSignalConnectedEj',
        signalIndex,
    )

  @overload(int)
  def isDeclarativeSignalConnected(self, signalIdx: int) -> bool:
    """
    Calls Qt's 'bool QObjectPrivate::isDeclarativeSignalConnected(uint
    signalIdx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#isDeclarativeSignalConnected

    Parameters
    ----------

    signalIdx : int
      Passed on as it is.
    """
    #  bool QObjectPrivate::isDeclarativeSignalConnected(uint signalIdx)
    #      const
    return self._callAs(
        'QObjectPrivate',
        'ritual_ZNK14QObjectPrivate28isDeclarativeSignalConnectedEj',
        signalIdx,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setObjectNameWithoutBindings(self, name: str) -> None:
    """
    Calls Qt's 'void QObjectPrivate::setObjectNameWithoutBindings(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#setObjectNameWithoutBindings

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QObjectPrivate::setObjectNameWithoutBindings(const QString &name)
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate28setObjectNameWithoutBindingsERK7QString',
        name,
    )

  @overload(QObject)
  @overload(NoneType)
  def setParent_helper(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectPrivate::setParent_helper(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#setParent_helper

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectPrivate::setParent_helper(QObject *a0)
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate16setParent_helperEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(QThreadData, QThreadData, QBindingStatus)
  @overload(QThreadData, QThreadData, NoneType)
  @overload(QThreadData, NoneType, QBindingStatus)
  @overload(QThreadData, NoneType, NoneType)
  @overload(NoneType, QThreadData, QBindingStatus)
  @overload(NoneType, QThreadData, NoneType)
  @overload(NoneType, NoneType, QBindingStatus)
  @overload(NoneType, NoneType, NoneType)
  def setThreadData_helper(
      self,
      currentData: Optional[QThreadData],
      targetData: Optional[QThreadData],
      status: Optional[QBindingStatus],
  ) -> None:
    """
    Calls Qt's 'void QObjectPrivate::setThreadData_helper(QThreadData
    *currentData, QThreadData *targetData, QBindingStatus *status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#setThreadData_helper

    Parameters
    ----------

    currentData : Optional[QThreadData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetData : Optional[QThreadData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    status : Optional[QBindingStatus]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectPrivate::setThreadData_helper(QThreadData *currentData,
    #      QThreadData *targetData, QBindingStatus *status)
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate20setThreadData_helperEP11QThreadDataS1_P'
        '14QBindingStatus',
        self._addressOf(currentData), self._addressOf(targetData),
        self._addressOf(status),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QObjectPrivate::QObjectPrivate(decltype(QObjectPrivateVersion)
    version)': names the enum 'QtPrivate_6_12_0', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QObjectPrivate.__init__' has no cute function yet. Qt's "
        "'QObjectPrivate::QObjectPrivate(decltype(QObjectPrivateVersion) "
        "version)': names the enum 'QtPrivate_6_12_0', whose class cannot "
        "be named here.")

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

  def q_func(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QObjectPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectprivate.html#q_func

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QObjectPrivate::q_func()
    address = self._callAs(
        'QObjectPrivate', 'ritual_ZN14QObjectPrivate6q_funcEv',
    )
    from . import QObject
    return QObject._cuteAt(address)

  def ensureExtraData(self) -> None:
    """
    Calls Qt's 'void QObjectPrivate::ensureExtraData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#ensureExtraData
    """
    #  void QObjectPrivate::ensureExtraData()
    self._callAs(
        'QObjectPrivate', 'ritual_ZN14QObjectPrivate15ensureExtraDataEv',
    )

  def deleteChildren(self) -> None:
    """
    Calls Qt's 'void QObjectPrivate::deleteChildren()'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectprivate.html#deleteChildren
    """
    #  void QObjectPrivate::deleteChildren()
    self._callAs(
        'QObjectPrivate', 'ritual_ZN14QObjectPrivate14deleteChildrenEv',
    )

  def clearBindingStorage(self) -> None:
    """
    Calls Qt's 'void QObjectPrivate::clearBindingStorage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#clearBindingStorage
    """
    #  void QObjectPrivate::clearBindingStorage()
    self._callAs(
        'QObjectPrivate', 'ritual_ZN14QObjectPrivate19clearBindingStorageEv',
    )

  def moveToThread_helper(self) -> None:
    """
    Calls Qt's 'void QObjectPrivate::moveToThread_helper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#moveToThread_helper
    """
    #  void QObjectPrivate::moveToThread_helper()
    self._callAs(
        'QObjectPrivate', 'ritual_ZN14QObjectPrivate19moveToThread_helperEv',
    )

  def ensureConnectionData(self) -> None:
    """
    Calls Qt's 'void QObjectPrivate::ensureConnectionData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#ensureConnectionData
    """
    #  void QObjectPrivate::ensureConnectionData()
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate20ensureConnectionDataEv',
    )

  @overload(int, Connection)
  @overload(int, NoneType)
  def addConnection(self, signal: int, c: Optional[Connection]) -> None:
    """
    Calls Qt's 'void QObjectPrivate::addConnection(int signal, Connection
    *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectprivate.html#addConnection

    Parameters
    ----------

    signal : int
      Passed on as it is.

    c : Optional[Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectPrivate::addConnection(int signal, Connection *c)
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate13addConnectionEiPNS_10ConnectionE',
        signal, self._addressOf(c),
    )

  @overload(QMetaMethod)
  def connectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QObjectPrivate::connectNotify(const QMetaMethod
    &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectprivate.html#connectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QObjectPrivate::connectNotify(const QMetaMethod &signal)
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate13connectNotifyERK11QMetaMethod',
        self._valueOf(signal),
    )

  @overload(QMetaMethod)
  def disconnectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QObjectPrivate::disconnectNotify(const QMetaMethod
    &signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#disconnectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QObjectPrivate::disconnectNotify(const QMetaMethod &signal)
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate16disconnectNotifyERK11QMetaMethod',
        self._valueOf(signal),
    )

  def reinitBindingStorageAfterThreadMove(self) -> None:
    """
    Calls Qt's 'void QObjectPrivate::reinitBindingStorageAfterThreadMove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html
    """
    #  void QObjectPrivate::reinitBindingStorageAfterThreadMove()
    self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate35reinitBindingStorageAfterThreadMoveEv',
    )

  @overload(QMetaProperty)
  def getPropertyAdaptorSlotObject(
      self,
      property: QMetaProperty,
  ) -> Optional[QtPrivate.QPropertyAdaptorSlotObject]:
    """
    Calls Qt's 'QtPrivate::QPropertyAdaptorSlotObject
    *QObjectPrivate::getPropertyAdaptorSlotObject(const QMetaProperty
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectprivate.html#getPropertyAdaptorSlotObject

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    Returns
    -------

    Optional[QtPrivate.QPropertyAdaptorSlotObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtPrivate::QPropertyAdaptorSlotObject
    #      *QObjectPrivate::getPropertyAdaptorSlotObject(const QMetaProperty
    #      &property)
    address = self._callAs(
        'QObjectPrivate',
        'ritual_ZN14QObjectPrivate28getPropertyAdaptorSlotObjectERK13QMetaP'
        'roperty',
        self._valueOf(property),
    )
    return QtPrivate.QPropertyAdaptorSlotObject._cuteAt(address)

  @staticmethod
  def connect(*__, **_) -> Never:
    """
    - Qt's 'QMetaObject::Connection QObjectPrivate::connect(const QObject
      *sender, int signal_index, QtPrivate::QSlotObjectBase *slotObj,
      Qt::ConnectionType type)': names 'QtPrivate::QSlotObjectBase', which
      has no cute class yet.
    - Qt's 'QMetaObject::Connection QObjectPrivate::connect(const QObject
      *sender, int signal_index, const QObject *receiver,
      QtPrivate::QSlotObjectBase *slotObj, Qt::ConnectionType type)': names
      'QtPrivate::QSlotObjectBase', which has no cute class yet.
    - Qt's 'QObjectPrivate::connect': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QObjectPrivate.connect' has no cute function yet. Qt's "
        "'QMetaObject::Connection QObjectPrivate::connect(const QObject "
        "*sender, int signal_index, QtPrivate::QSlotObjectBase *slotObj, "
        "Qt::ConnectionType type)': names 'QtPrivate::QSlotObjectBase', "
        "which has no cute class yet. Qt's 'QMetaObject::Connection "
        "QObjectPrivate::connect(const QObject *sender, int signal_index, "
        "const QObject *receiver, QtPrivate::QSlotObjectBase *slotObj, "
        "Qt::ConnectionType type)': names 'QtPrivate::QSlotObjectBase', "
        "which has no cute class yet. Qt's 'QObjectPrivate::connect': a "
        "template: a pattern and no single function.")

  @staticmethod
  def connectImpl(*__, **_) -> Never:
    """
    Qt's 'QMetaObject::Connection QObjectPrivate::connectImpl(const QObject
    *sender, int signal_index, const QObject *receiver, void **slot,
    QtPrivate::QSlotObjectBase *slotObj, int type, const int *types, const
    QMetaObject *senderMetaObject)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QObjectPrivate.connectImpl' has no cute function yet. Qt's "
        "'QMetaObject::Connection QObjectPrivate::connectImpl(const QObject "
        "*sender, int signal_index, const QObject *receiver, void **slot, "
        "QtPrivate::QSlotObjectBase *slotObj, int type, const int *types, "
        "const QMetaObject *senderMetaObject)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def disconnect(*__, **_) -> Never:
    """
    - Qt's 'bool QObjectPrivate::disconnect(const QObject *sender, int
      signal_index, void **slot)': takes a type Python has no way to hand
      over yet.
    - Qt's 'bool QObjectPrivate::disconnect(const QObject *sender, int
      signal_index, const QObject *receiver, void **slot)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QObjectPrivate::disconnect': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QObjectPrivate.disconnect' has no cute function yet. Qt's 'bool "
        "QObjectPrivate::disconnect(const QObject *sender, int "
        "signal_index, void **slot)': takes a type Python has no way to "
        "hand over yet. Qt's 'bool QObjectPrivate::disconnect(const QObject "
        "*sender, int signal_index, const QObject *receiver, void **slot)': "
        "takes a type Python has no way to hand over yet. Qt's "
        "'QObjectPrivate::disconnect': a template: a pattern and no single "
        "function.")

  @staticmethod
  def flagsForDumping(*__, **_) -> Never:
    """
    Qt's 'std::string QObjectPrivate::flagsForDumping() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QObjectPrivate.flagsForDumping' has no cute function yet. Qt's "
        "'std::string QObjectPrivate::flagsForDumping() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def removeConnection(*__, **_) -> Never:
    """
    Qt's 'bool QObjectPrivate::removeConnection(Connection *c)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'signalSlotLock'.
    """
    raise NotImplementedError(
        "'QObjectPrivate.removeConnection' has no cute function yet. Qt's "
        "'bool QObjectPrivate::removeConnection(Connection *c)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'signalSlotLock'.")

  @staticmethod
  def signalIndex(*__, **_) -> Never:
    """
    Qt's 'int QObjectPrivate::signalIndex(const char *signalName, const
    QMetaObject **meta) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QObjectPrivate.signalIndex' has no cute function yet. Qt's 'int "
        "QObjectPrivate::signalIndex(const char *signalName, const "
        "QMetaObject **meta) const': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def writeToDebugStream(*__, **_) -> Never:
    """
    Qt's 'void QObjectPrivate::writeToDebugStream(QDebug &a0) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QObjectPrivate.writeToDebugStream' has no cute function yet. Qt's "
        "'void QObjectPrivate::writeToDebugStream(QDebug &a0) const': takes "
        "a type Python has no way to hand over yet.")
