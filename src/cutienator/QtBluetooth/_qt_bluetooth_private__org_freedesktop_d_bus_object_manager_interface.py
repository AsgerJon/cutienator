"""
QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/objectmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface to
#  be private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtDBus import QDBusObjectPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusObjectPath = WAIT['QDBusObjectPath']


class OrgFreedesktopDBusObjectManagerInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface: a plain
  Python object standing in front of one C++
  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface.

  What exists
  -----------

  Every function of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface that has a
  ritual and that Python can call so far, 3 names in all: 'metaObject',
  'staticInterfaceName', 'InterfacesRemoved'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    qt_metacast(const char *a0)': one of Qt's own inner workings.
  - Qt's 'int QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    qt_metacall(QMetaObject::Call a0, int a1, void **a2)': one of Qt's own
    inner workings.
  - Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    ~OrgFreedesktopDBusObjectManagerInterface()': the destructor: Python
    never removes a C++
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface.
  - Qt's 'void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    InterfacesAdded(const QDBusObjectPath &object_path, InterfaceList
    interfaces_and_properties)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate; 1 leans on
  'qRegisterNormalizedMetaType_ManagedObjectList(QByteArray const&)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface is
    created at the first use, not by
    'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface that has no
    cute function yet, 'GetManagedObjects', 'InterfacesAdded', '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbusobjectmanagerinterface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInte'
        'rface19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface'

  #  A C++ QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface
  #  Python makes is of a C++ class of ours, in which Python can take
  #  functions over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbusobjectmanagerinterface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInt'
        'erface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    OrgFreedesktopDBusObjectManagerInterface(const QString &service, const
    QString &path, const QDBusConnection &connection, QObject *parent)':
    leans on 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    qt_metacall(QMetaObject::Call, int, void**)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusObjectManagerInterface.__init"
        "__' has no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::OrgF"
        "reedesktopDBusObjectManagerInterface(const QString &service, const "
        "QString &path, const QDBusConnection &connection, QObject "
        "*parent)': leans on "
        "'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::qt_m"
        "etacall(QMetaObject::Call, int, void**)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QDBusObjectPath, QStringList)
  def InterfacesRemoved(
      self,
      object_path: QDBusObjectPath,
      interfaces: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    InterfacesRemoved(const QDBusObjectPath &object_path, const QStringList
    &interfaces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbusobjectmanagerinterface.html

    Parameters
    ----------

    object_path : QDBusObjectPath
      Passed on as a value: Qt reads the C++ QDBusObjectPath, which stays
      Python's own.

    interfaces : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    #      InterfacesRemoved(const QDBusObjectPath &object_path, const
    #      QStringList &interfaces)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInte'
        'rface17InterfacesRemovedERK15QDBusObjectPathRK5QListI7QStringE',
        self._valueOf(object_path), self._valueOf(interfaces),
    )

  @staticmethod
  def GetManagedObjects(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<ManagedObjectList>
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    GetManagedObjects()': leans on
    'qRegisterNormalizedMetaType_ManagedObjectList(QByteArray const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusObjectManagerInterface.GetMan"
        "agedObjects' has no cute function yet. Qt's "
        "'QDBusPendingReply<ManagedObjectList> "
        "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::GetMa"
        "nagedObjects()': leans on "
        "'qRegisterNormalizedMetaType_ManagedObjectList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def InterfacesAdded(*__, **_) -> Never:
    """
    Qt's 'void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::
    InterfacesAdded(const QDBusObjectPath &object_path, InterfaceList
    interfaces_and_properties)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusObjectManagerInterface.Interf"
        "acesAdded' has no cute function yet. Qt's 'void "
        "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::Inter"
        "facesAdded(const QDBusObjectPath &object_path, InterfaceList "
        "interfaces_and_properties)': takes a type Python has no way to "
        "hand over yet.")
