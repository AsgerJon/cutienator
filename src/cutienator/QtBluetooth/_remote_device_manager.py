"""
RemoteDeviceManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/remotedevicemanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means RemoteDeviceManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class RemoteDeviceManager(QObject):
  """
  The cute side of Qt's RemoteDeviceManager: a plain Python object standing
  in front of one C++ RemoteDeviceManager.

  It is built on the cute 'QObject', as Qt's RemoteDeviceManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's RemoteDeviceManager that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'isJobInProgress',
  'finished', 'runQueue', 'prepareNextJob'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *RemoteDeviceManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int RemoteDeviceManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'RemoteDeviceManager.

  What to expect
  --------------

  - The C++ RemoteDeviceManager is created at the first use, not by
    'RemoteDeviceManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ RemoteDeviceManager.
  - Qt tells when it has removed the C++ RemoteDeviceManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's RemoteDeviceManager that has no cute function yet,
    '__init__', 'disconnectDevice', 'scheduleJob', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside RemoteDeviceManager, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class JobType(CuteNum, scoped=True):
    """
    The enum 'RemoteDeviceManager::JobType' of Qt, with the 1 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    JobDisconnectDevice = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'RemoteDeviceManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *RemoteDeviceManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/remotedevicemanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *RemoteDeviceManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19RemoteDeviceManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isJobInProgress(self) -> bool:
    """
    Calls Qt's 'bool RemoteDeviceManager::isJobInProgress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/remotedevicemanager.html#isJobInProgress
    """
    #  bool RemoteDeviceManager::isJobInProgress() const
    return self.uglySide.call(
        'ritual_ZNK19RemoteDeviceManager15isJobInProgressEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'RemoteDeviceManager::RemoteDeviceManager(const QBluetoothAddress
    &localAddress, QObject *parent)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'RemoteDeviceManager.__init__' has no cute function yet. Qt's "
        "'RemoteDeviceManager::RemoteDeviceManager(const QBluetoothAddress "
        "&localAddress, QObject *parent)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'QT_BT_BLUEZ'.")

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

  def finished(self) -> None:
    """
    Calls Qt's 'void RemoteDeviceManager::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/remotedevicemanager.html#finished
    """
    #  void RemoteDeviceManager::finished()
    self.uglySide.call('ritual_ZN19RemoteDeviceManager8finishedEv')

  def runQueue(self) -> None:
    """
    Calls Qt's 'void RemoteDeviceManager::runQueue()'.

    Qt's own words: https://doc.qt.io/qt-6/remotedevicemanager.html#runQueue
    """
    #  void RemoteDeviceManager::runQueue()
    self.uglySide.call('ritual_ZN19RemoteDeviceManager8runQueueEv')

  def prepareNextJob(self) -> None:
    """
    Calls Qt's 'void RemoteDeviceManager::prepareNextJob()'.

    Qt's own words:
    https://doc.qt.io/qt-6/remotedevicemanager.html#prepareNextJob
    """
    #  void RemoteDeviceManager::prepareNextJob()
    self.uglySide.call('ritual_ZN19RemoteDeviceManager14prepareNextJobEv')

  @staticmethod
  def disconnectDevice(*__, **_) -> Never:
    """
    Qt's 'void RemoteDeviceManager::disconnectDevice(const QBluetoothAddress
    &remote)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name
    'OrgFreedesktopDBusObjectManagerInterface'; did you mean
    'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface'?.
    """
    raise NotImplementedError(
        "'RemoteDeviceManager.disconnectDevice' has no cute function yet. "
        "Qt's 'void RemoteDeviceManager::disconnectDevice(const "
        "QBluetoothAddress &remote)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'OrgFreedesktopDBusObjectManagerInterface'; did "
        "you mean "
        "'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface'?.")

  @staticmethod
  def scheduleJob(*__, **_) -> Never:
    """
    Qt's 'bool RemoteDeviceManager::scheduleJob(JobType job, const
    QList<QBluetoothAddress> &remoteDevices)': leans on
    'RemoteDeviceManager::disconnectDevice(QBluetoothAddress const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'RemoteDeviceManager.scheduleJob' has no cute function yet. Qt's "
        "'bool RemoteDeviceManager::scheduleJob(JobType job, const "
        "QList<QBluetoothAddress> &remoteDevices)': leans on "
        "'RemoteDeviceManager::disconnectDevice(QBluetoothAddress const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
