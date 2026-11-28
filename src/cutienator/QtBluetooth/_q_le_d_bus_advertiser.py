"""
QLeDBusAdvertiser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qleadvertiser_bluezdbus_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QLeDBusAdvertiser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QLeDBusAdvertiser(QObject):
  """
  The cute side of Qt's QLeDBusAdvertiser: a plain Python object standing in
  front of one C++ QLeDBusAdvertiser.

  It is built on the cute 'QObject', as Qt's QLeDBusAdvertiser is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLeDBusAdvertiser that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'Release', 'errorOccurred'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLeDBusAdvertiser::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QLeDBusAdvertiser::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QLeDBusAdvertiser::~QLeDBusAdvertiser()': the destructor: Python
    never removes a C++ QLeDBusAdvertiser.

  What has no ritual
  ------------------

  9 of the 15 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QLeDBusAdvertiser.

  What to expect
  --------------

  - The C++ QLeDBusAdvertiser is created at the first use, not by
    'QLeDBusAdvertiser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLeDBusAdvertiser.
  - Qt tells when it has removed the C++ QLeDBusAdvertiser. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLeDBusAdvertiser that has no cute function yet,
    '__init__', 'setAdvertisementDataForDBus', 'setAdvertisingParamsForDBus',
    'setDataForDBus', 'startAdvertising', 'stopAdvertising', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLeDBusAdvertiser'

  #  A C++ QLeDBusAdvertiser Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLeDBusAdvertiser'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLeDBusAdvertiser::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qledbusadvertiser.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLeDBusAdvertiser::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QLeDBusAdvertiser10metaObjectEv',
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
    Qt's 'QLeDBusAdvertiser::QLeDBusAdvertiser(const
    QLowEnergyAdvertisingParameters &params, const QLowEnergyAdvertisingData
    &advertisingData, const QLowEnergyAdvertisingData &scanResponseData,
    const QString &hostAdapterPath, QObject *parent)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'sanitizeNameForDBus'.
    """
    raise NotImplementedError(
        "'QLeDBusAdvertiser.__init__' has no cute function yet. Qt's "
        "'QLeDBusAdvertiser::QLeDBusAdvertiser(const "
        "QLowEnergyAdvertisingParameters &params, const "
        "QLowEnergyAdvertisingData &advertisingData, const "
        "QLowEnergyAdvertisingData &scanResponseData, const QString "
        "&hostAdapterPath, QObject *parent)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'sanitizeNameForDBus'.")

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

  def Release(self) -> None:
    """
    Calls Qt's 'void QLeDBusAdvertiser::Release()'.

    Qt's own words: https://doc.qt.io/qt-6/qledbusadvertiser.html#Release
    """
    #  void QLeDBusAdvertiser::Release()
    self.uglySide.call('ritual_ZN17QLeDBusAdvertiser7ReleaseEv')

  def errorOccurred(self) -> None:
    """
    Calls Qt's 'void QLeDBusAdvertiser::errorOccurred()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qledbusadvertiser.html#errorOccurred
    """
    #  void QLeDBusAdvertiser::errorOccurred()
    self.uglySide.call('ritual_ZN17QLeDBusAdvertiser13errorOccurredEv')

  @staticmethod
  def setAdvertisementDataForDBus(*__, **_) -> Never:
    """
    Qt's 'void QLeDBusAdvertiser::setAdvertisementDataForDBus()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface'.
    """
    raise NotImplementedError(
        "'QLeDBusAdvertiser.setAdvertisementDataForDBus' has no cute "
        "function yet. Qt's 'void "
        "QLeDBusAdvertiser::setAdvertisementDataForDBus()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface'.")

  @staticmethod
  def setAdvertisingParamsForDBus(*__, **_) -> Never:
    """
    Qt's 'void QLeDBusAdvertiser::setAdvertisingParamsForDBus()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLeDBusAdvertiser.setAdvertisingParamsForDBus' has no cute "
        "function yet. Qt's 'void "
        "QLeDBusAdvertiser::setAdvertisingParamsForDBus()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def setDataForDBus(*__, **_) -> Never:
    """
    Qt's 'void QLeDBusAdvertiser::setDataForDBus()': leans on
    'QLeDBusAdvertiser::setAdvertisementDataForDBus()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QLeDBusAdvertiser.setDataForDBus' has no cute function yet. Qt's "
        "'void QLeDBusAdvertiser::setDataForDBus()': leans on "
        "'QLeDBusAdvertiser::setAdvertisementDataForDBus()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def startAdvertising(*__, **_) -> Never:
    """
    Qt's 'void QLeDBusAdvertiser::startAdvertising()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLeDBusAdvertiser.startAdvertising' has no cute function yet. "
        "Qt's 'void QLeDBusAdvertiser::startAdvertising()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def stopAdvertising(*__, **_) -> Never:
    """
    Qt's 'void QLeDBusAdvertiser::stopAdvertising()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QLeDBusAdvertiser.stopAdvertising' has no cute function yet. Qt's "
        "'void QLeDBusAdvertiser::stopAdvertising()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")
