"""
QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/objectmanageradaptor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
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


class OrgFreedesktopDBusObjectManagerAdaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor: a plain Python
  object standing in front of one C++
  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor.

  What exists
  -----------

  Every function of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor that has a
  ritual and that Python can call so far, 2 names in all: 'metaObject',
  'InterfacesRemoved'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    ~OrgFreedesktopDBusObjectManagerAdaptor()': the destructor: Python never
    removes a C++ QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor.
  - Qt's 'void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    InterfacesAdded(const QDBusObjectPath &object_path, InterfaceList
    interfaces_and_properties)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate; 1 leans on
  'qRegisterNormalizedMetaType_ManagedObjectList(QByteArray const&)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor is
    created at the first use, not by
    'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor that has no
    cute function yet, 'GetManagedObjects', 'InterfacesAdded', '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor'

  #  A C++ QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptor'

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
    *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbusobjectmanageradaptor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAda'
        'ptor10metaObjectEv',
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
    Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    OrgFreedesktopDBusObjectManagerAdaptor(QObject *parent)': leans on
    'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusObjectManagerAdaptor.__init__"
        "' has no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::OrgFre"
        "edesktopDBusObjectManagerAdaptor(QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::qt_met"
        "acall(QMetaObject::Call, int, void**)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
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
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    InterfacesRemoved(const QDBusObjectPath &object_path, const QStringList
    &interfaces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbusobjectmanageradaptor.html

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
    #  void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    #      InterfacesRemoved(const QDBusObjectPath &object_path, const
    #      QStringList &interfaces)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdap'
        'tor17InterfacesRemovedERK15QDBusObjectPathRK5QListI7QStringE',
        self._valueOf(object_path), self._valueOf(interfaces),
    )

  @staticmethod
  def GetManagedObjects(*__, **_) -> Never:
    """
    Qt's 'ManagedObjectList
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    GetManagedObjects()': leans on
    'qRegisterNormalizedMetaType_ManagedObjectList(QByteArray const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusObjectManagerAdaptor.GetManag"
        "edObjects' has no cute function yet. Qt's 'ManagedObjectList "
        "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::GetMana"
        "gedObjects()': leans on "
        "'qRegisterNormalizedMetaType_ManagedObjectList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def InterfacesAdded(*__, **_) -> Never:
    """
    Qt's 'void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::
    InterfacesAdded(const QDBusObjectPath &object_path, InterfaceList
    interfaces_and_properties)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusObjectManagerAdaptor.Interfac"
        "esAdded' has no cute function yet. Qt's 'void "
        "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::Interfa"
        "cesAdded(const QDBusObjectPath &object_path, InterfaceList "
        "interfaces_and_properties)': takes a type Python has no way to "
        "hand over yet.")
