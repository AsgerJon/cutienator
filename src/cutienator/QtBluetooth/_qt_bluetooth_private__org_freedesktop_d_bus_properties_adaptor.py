"""
QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/propertiesadaptor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtDBus import QDBusVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusVariant = WAIT['QDBusVariant']
  QVariant = WAIT['QVariant']


class OrgFreedesktopDBusPropertiesAdaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor: a plain Python
  object standing in front of one C++
  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor.

  What exists
  -----------

  Every function of Qt's
  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'Get',
  'GetAll', 'Set', 'PropertiesChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacast(
    const char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::
    ~OrgFreedesktopDBusPropertiesAdaptor()': the destructor: Python never
    removes a C++ QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor is
    created at the first use, not by
    'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor
    that has no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor'

  #  A C++ QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor Python
  #  makes is of a C++ class of ours, in which Python can take functions
  #  over. This ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor'

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
    *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesadaptor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::
    #      metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdapto'
        'r10metaObjectEv',
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
    Qt's 'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::
    OrgFreedesktopDBusPropertiesAdaptor(QObject *parent)': leans on
    'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgFreedesktopDBusPropertiesAdaptor.__init__' "
        "has no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::OrgFreede"
        "sktopDBusPropertiesAdaptor(QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metaca"
        "ll(QMetaObject::Call, int, void**)', which Qt's source does not "
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

  @overload(str, str)
  def Get(self, interface: str, name: str) -> QDBusVariant:
    """
    Calls Qt's 'QDBusVariant
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Get(const
    QString &interface, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesadaptor.html

    Parameters
    ----------

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDBusVariant
      A new cute QDBusVariant around the copy Qt gave back. Python owns it.
    """
    #  QDBusVariant
    #      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Get(const
    #      QString &interface, const QString &name)
    address = self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor'
        '3GetERK7QStringS3_',
        interface, name,
    )
    from ..QtDBus import QDBusVariant
    return QDBusVariant._cuteOwning(address)

  @overload(str)
  def GetAll(self, interface: str) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::GetAll(const
    QString &interface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesadaptor.html

    Parameters
    ----------

    interface : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap
    #      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::GetAll(
    #      const QString &interface)
    address = self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor'
        '6GetAllERK7QString',
        interface,
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(str, str, QDBusVariant)
  def Set(self, interface: str, name: str, value: QDBusVariant) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Set(const
    QString &interface, const QString &name, const QDBusVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesadaptor.html

    Parameters
    ----------

    interface : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QDBusVariant
      Passed on as a value: Qt reads the C++ QDBusVariant, which stays
      Python's own.
    """
    #  void
    #      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Set(const
    #      QString &interface, const QString &name, const QDBusVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor'
        '3SetERK7QStringS3_RK12QDBusVariant',
        interface, name, self._valueOf(value),
    )

  @overload(str, QMap[str, QVariant], QStringList)
  def PropertiesChanged(
      self,
      interface: str,
      changed_properties: QMap[str, QVariant],
      invalidated_properties: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::
    PropertiesChanged(const QString &interface, const QVariantMap
    &changed_properties, const QStringList &invalidated_properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgfreedesktopdbuspropertiesadaptor.html

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
    """
    #  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::
    #      PropertiesChanged(const QString &interface, const QVariantMap
    #      &changed_properties, const QStringList &invalidated_properties)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor'
        '17PropertiesChangedERK7QStringRK4QMapIS1_8QVariantERK5QListIS1_E',
        interface, self._valueOf(changed_properties),
        self._valueOf(invalidated_properties),
    )
