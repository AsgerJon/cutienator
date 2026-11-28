"""
QtROExternalIoDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnectionfactories_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtROExternalIoDevice to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtROIoDeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject
  from . import QtROExternalIoDevicePrivate


class QtROExternalIoDevice(QtROIoDeviceBase):
  """
  The cute side of Qt's QtROExternalIoDevice: a plain Python object standing
  in front of one C++ QtROExternalIoDevice.

  It is built on the cute 'QtROIoDeviceBase', as Qt's QtROExternalIoDevice is
  built on Qt's QtROIoDeviceBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtROExternalIoDevice that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'connection',
  'isOpen', 'doClose', 'deviceType', 'd_func'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtROExternalIoDevice::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QtROExternalIoDevice::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QtROExternalIoDevicePrivate *QtROExternalIoDevice::d_func()
    const': takes in Python what 'QtROExternalIoDevicePrivate
    *QtROExternalIoDevice::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 1 leans on
  'QtROExternalIoDevice; 1 leans on 'vtable for QtROExternalIoDevice', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QtROExternalIoDevice is created at the first use, not by
    'QtROExternalIoDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtROExternalIoDevice.
  - Qt tells when it has removed the C++ QtROExternalIoDevice. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtROExternalIoDevice that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROExternalIoDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtROExternalIoDevice::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroexternaliodevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtROExternalIoDevice::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QtROExternalIoDevice10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def connection(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QtROExternalIoDevice::connection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroexternaliodevice.html#connection

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QtROExternalIoDevice::connection() const
    ritual = 'ritual_ZNK20QtROExternalIoDevice10connectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QtROExternalIoDevice10connectionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QtROExternalIoDevice::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtroexternaliodevice.html#isOpen
    """
    #  bool QtROExternalIoDevice::isOpen() const
    ritual = 'ritual_ZNK20QtROExternalIoDevice6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QtROExternalIoDevice6isOpenEv'
    return self.uglySide.call(ritual)

  def deviceType(self) -> str:
    """
    Calls Qt's 'QString QtROExternalIoDevice::deviceType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtroexternaliodevice.html#deviceType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtROExternalIoDevice::deviceType() const
    ritual = 'ritual_ZNK20QtROExternalIoDevice10deviceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QtROExternalIoDevice10deviceTypeEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtROExternalIoDevice::QtROExternalIoDevice(QIODevice *device,
    QObject *parent)': leans on 'vtable for QtROExternalIoDevice', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QtROExternalIoDevice.__init__' has no cute function yet. Qt's "
        "'QtROExternalIoDevice::QtROExternalIoDevice(QIODevice *device, "
        "QObject *parent)': leans on 'vtable for QtROExternalIoDevice', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def doClose(self) -> None:
    """
    Calls Qt's 'void QtROExternalIoDevice::doClose()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroexternaliodevice.html#doClose
    """
    #  void QtROExternalIoDevice::doClose()
    ritual = 'ritual_ZN20QtROExternalIoDevice7doCloseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QtROExternalIoDevice7doCloseEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QtROExternalIoDevicePrivate]:
    """
    Calls Qt's 'QtROExternalIoDevicePrivate *QtROExternalIoDevice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroexternaliodevice.html#d_func

    Returns
    -------

    Optional[QtROExternalIoDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROExternalIoDevicePrivate *QtROExternalIoDevice::d_func()
    address = self.uglySide.call('ritual_ZN20QtROExternalIoDevice6d_funcEv')
    from . import QtROExternalIoDevicePrivate
    return QtROExternalIoDevicePrivate._cuteAt(address)
