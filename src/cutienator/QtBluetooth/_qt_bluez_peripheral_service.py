"""
QtBluezPeripheralService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralobjects_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluezPeripheralService to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtBluezPeripheralGattObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QtBluezPeripheralService(QtBluezPeripheralGattObject):
  """
  The cute side of Qt's QtBluezPeripheralService: a plain Python object
  standing in front of one C++ QtBluezPeripheralService.

  It is built on the cute 'QtBluezPeripheralGattObject', as Qt's
  QtBluezPeripheralService is built on Qt's QtBluezPeripheralGattObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtBluezPeripheralService that has a ritual and that
  Python can call so far, 1 name in all: 'metaObject'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtBluezPeripheralService::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QtBluezPeripheralService::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'InterfaceList QtBluezPeripheralService::properties() const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QtBluezPeripheralService.

  What to expect
  --------------

  - The C++ QtBluezPeripheralService is created at the first use, not by
    'QtBluezPeripheralService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtBluezPeripheralService.
  - Qt tells when it has removed the C++ QtBluezPeripheralService. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluezPeripheralService that has no cute function yet,
    '__init__', 'addIncludedService', holds a function that raises
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
  __qt_class__ = 'QtBluezPeripheralService'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtBluezPeripheralService::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluezperipheralservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtBluezPeripheralService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QtBluezPeripheralService10metaObjectEv',
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
    Qt's 'QtBluezPeripheralService::QtBluezPeripheralService(const
    QLowEnergyServiceData &serviceData, const QString &applicationPath,
    quint16 ordinal, QLowEnergyHandle handle, QObject *parent)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: unknown type name 'OrgBluezGattService1Adaptor'; did you
    mean 'QtBluetoothPrivate::OrgBluezGattService1Adaptor'?.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralService.__init__' has no cute function yet. Qt's "
        "'QtBluezPeripheralService::QtBluezPeripheralService(const "
        "QLowEnergyServiceData &serviceData, const QString "
        "&applicationPath, quint16 ordinal, QLowEnergyHandle handle, "
        "QObject *parent)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: unknown type "
        "name 'OrgBluezGattService1Adaptor'; did you mean "
        "'QtBluetoothPrivate::OrgBluezGattService1Adaptor'?.")

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

  @staticmethod
  def addIncludedService(*__, **_) -> Never:
    """
    Qt's 'void QtBluezPeripheralService::addIncludedService(const QString
    &objectPath)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QtBluezPeripheralService.addIncludedService' has no cute function "
        "yet. Qt's 'void QtBluezPeripheralService::addIncludedService(const "
        "QString &objectPath)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QT_BT_BLUEZ'.")
