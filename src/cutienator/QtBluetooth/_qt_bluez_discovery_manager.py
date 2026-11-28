"""
QtBluezDiscoveryManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/bluez5_helper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtBluezDiscoveryManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtDBus import QDBusMessage, QDBusObjectPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMessage = WAIT['QDBusMessage']
  QDBusObjectPath = WAIT['QDBusObjectPath']
  QVariant = WAIT['QVariant']


class QtBluezDiscoveryManager(QObject):
  """
  The cute side of Qt's QtBluezDiscoveryManager: a plain Python object
  standing in front of one C++ QtBluezDiscoveryManager.

  It is built on the cute 'QObject', as Qt's QtBluezDiscoveryManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtBluezDiscoveryManager that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject',
  'discoveryInterrupted', 'InterfacesRemoved', 'PropertiesChanged'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtBluezDiscoveryManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QtBluezDiscoveryManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 15 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QtBluezDiscoveryManager.

  What to expect
  --------------

  - The C++ QtBluezDiscoveryManager is created at the first use, not by
    'QtBluezDiscoveryManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtBluezDiscoveryManager.
  - Qt tells when it has removed the C++ QtBluezDiscoveryManager. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluezDiscoveryManager that has no cute function yet,
    '__init__', 'instance', 'registerDiscoveryInterest',
    'removeAdapterFromMonitoring', 'unregisterDiscoveryInterest', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluezDiscoveryManager'

  #  A C++ QtBluezDiscoveryManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluezDiscoveryManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtBluezDiscoveryManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezdiscoverymanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtBluezDiscoveryManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QtBluezDiscoveryManager10metaObjectEv',
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
    Qt's 'QtBluezDiscoveryManager::QtBluezDiscoveryManager(QObject *parent)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezDiscoveryManager.__init__' has no cute function yet. Qt's "
        "'QtBluezDiscoveryManager::QtBluezDiscoveryManager(QObject "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QT_BT_BLUEZ'.")

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

  @overload(str)
  def discoveryInterrupted(self, adapterPath: str) -> None:
    """
    Calls Qt's 'void QtBluezDiscoveryManager::discoveryInterrupted(const
    QString &adapterPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezdiscoverymanager.html#discoveryInterrupted

    Parameters
    ----------

    adapterPath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtBluezDiscoveryManager::discoveryInterrupted(const QString
    #      &adapterPath)
    self.uglySide.call(
        'ritual_ZN23QtBluezDiscoveryManager20discoveryInterruptedERK7QStrin'
        'g',
        adapterPath,
    )

  @overload(QDBusObjectPath, QStringList)
  def InterfacesRemoved(
      self,
      object_path: QDBusObjectPath,
      interfaces: QStringList,
  ) -> None:
    """
    Calls Qt's 'void QtBluezDiscoveryManager::InterfacesRemoved(const
    QDBusObjectPath &object_path, const QStringList &interfaces)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezdiscoverymanager.html#InterfacesRemoved

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
    #  void QtBluezDiscoveryManager::InterfacesRemoved(const QDBusObjectPath
    #      &object_path, const QStringList &interfaces)
    self.uglySide.call(
        'ritual_ZN23QtBluezDiscoveryManager17InterfacesRemovedERK15QDBusObj'
        'ectPathRK5QListI7QStringE',
        self._valueOf(object_path), self._valueOf(interfaces),
    )

  @overload(str, QMap[str, QVariant], QStringList, QDBusMessage)
  def PropertiesChanged(
      self,
      interface: str,
      changed_properties: QMap[str, QVariant],
      invalidated_properties: QStringList,
      msg: QDBusMessage,
  ) -> None:
    """
    Calls Qt's 'void QtBluezDiscoveryManager::PropertiesChanged(const QString
    &interface, const QVariantMap &changed_properties, const QStringList
    &invalidated_properties, const QDBusMessage &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezdiscoverymanager.html#PropertiesChanged

    Parameters
    ----------

    interface : str
      Passed on as it is: a QString is made of it for the call.

    changed_properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    invalidated_properties : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QtBluezDiscoveryManager::PropertiesChanged(const QString
    #      &interface, const QVariantMap &changed_properties, const
    #      QStringList &invalidated_properties, const QDBusMessage &msg)
    self.uglySide.call(
        'ritual_ZN23QtBluezDiscoveryManager17PropertiesChangedERK7QStringRK'
        '4QMapIS0_8QVariantERK5QListIS0_ERK12QDBusMessage',
        interface, self._valueOf(changed_properties),
        self._valueOf(invalidated_properties), self._valueOf(msg),
    )

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QtBluezDiscoveryManager *QtBluezDiscoveryManager::instance()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'discoveryManager'.
    """
    raise NotImplementedError(
        "'QtBluezDiscoveryManager.instance' has no cute function yet. Qt's "
        "'QtBluezDiscoveryManager *QtBluezDiscoveryManager::instance()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'discoveryManager'.")

  @staticmethod
  def registerDiscoveryInterest(*__, **_) -> Never:
    """
    Qt's 'bool QtBluezDiscoveryManager::registerDiscoveryInterest(const
    QString &adapterPath)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QtBluezDiscoveryManagerPrivate'.
    """
    raise NotImplementedError(
        "'QtBluezDiscoveryManager.registerDiscoveryInterest' has no cute "
        "function yet. Qt's 'bool "
        "QtBluezDiscoveryManager::registerDiscoveryInterest(const QString "
        "&adapterPath)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QtBluezDiscoveryManagerPrivate'.")

  @staticmethod
  def removeAdapterFromMonitoring(*__, **_) -> Never:
    """
    Qt's 'void QtBluezDiscoveryManager::removeAdapterFromMonitoring(const
    QString &dbusPath)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'AdapterData'.
    """
    raise NotImplementedError(
        "'QtBluezDiscoveryManager.removeAdapterFromMonitoring' has no cute "
        "function yet. Qt's 'void "
        "QtBluezDiscoveryManager::removeAdapterFromMonitoring(const QString "
        "&dbusPath)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'AdapterData'.")

  @staticmethod
  def unregisterDiscoveryInterest(*__, **_) -> Never:
    """
    Qt's 'void QtBluezDiscoveryManager::unregisterDiscoveryInterest(const
    QString &adapterPath)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QtBluezDiscoveryManagerPrivate'.
    """
    raise NotImplementedError(
        "'QtBluezDiscoveryManager.unregisterDiscoveryInterest' has no cute "
        "function yet. Qt's 'void "
        "QtBluezDiscoveryManager::unregisterDiscoveryInterest(const QString "
        "&adapterPath)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QtBluezDiscoveryManagerPrivate'.")
