"""
QtBluetoothPrivate::OrgBluezGattService1Adaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/gattservice1adaptor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezGattService1Adaptor to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtDBus import QDBusObjectPath


class OrgBluezGattService1Adaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtBluetoothPrivate::OrgBluezGattService1Adaptor: a
  plain Python object standing in front of one C++
  QtBluetoothPrivate::OrgBluezGattService1Adaptor.

  What exists
  -----------

  Every function of Qt's QtBluetoothPrivate::OrgBluezGattService1Adaptor that
  has a ritual and that Python can call so far, 5 names in all: 'metaObject',
  'device', 'includes', 'primary', 'uUID'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezGattService1Adaptor::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QtBluetoothPrivate::OrgBluezGattService1Adaptor::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezGattService1Adaptor::
    ~OrgBluezGattService1Adaptor()': the destructor: Python never removes a
    C++ QtBluetoothPrivate::OrgBluezGattService1Adaptor.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezGattService1Adaptor is created at the
    first use, not by 'QtBluetoothPrivate::OrgBluezGattService1Adaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezGattService1Adaptor.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezGattService1Adaptor. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgBluezGattService1Adaptor that
    has no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezGattService1Adaptor'

  #  A C++ QtBluetoothPrivate::OrgBluezGattService1Adaptor Python makes is of
  #  a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezGattService1Adaptor'

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
    *QtBluetoothPrivate::OrgBluezGattService1Adaptor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattservice1adaptor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezGattService1Adaptor::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor10metaO'
        'bjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def device(self) -> QDBusObjectPath:
    """
    Calls Qt's 'QDBusObjectPath
    QtBluetoothPrivate::OrgBluezGattService1Adaptor::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattservice1adaptor.html

    Returns
    -------

    QDBusObjectPath
      A new cute QDBusObjectPath around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusObjectPath
    #      QtBluetoothPrivate::OrgBluezGattService1Adaptor::device() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor6device'
        'Ev',
    )
    from ..QtDBus import QDBusObjectPath
    return QDBusObjectPath._cuteOwning(address)

  def includes(self) -> QList[QDBusObjectPath]:
    """
    Calls Qt's 'QList<QDBusObjectPath>
    QtBluetoothPrivate::OrgBluezGattService1Adaptor::includes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattservice1adaptor.html

    Returns
    -------

    QList[QDBusObjectPath]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDBusObjectPath>
    #      QtBluetoothPrivate::OrgBluezGattService1Adaptor::includes() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor8includ'
        'esEv',
    )
    from ..QtDBus import QDBusObjectPath
    return QList[QDBusObjectPath]._cuteOwning(address)

  def primary(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezGattService1Adaptor::primary() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattservice1adaptor.html
    """
    #  bool QtBluetoothPrivate::OrgBluezGattService1Adaptor::primary() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor7primar'
        'yEv',
    )

  def uUID(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezGattService1Adaptor::uUID() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattservice1adaptor.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezGattService1Adaptor::uUID() const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor4uUIDEv',
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
    Qt's 'QtBluetoothPrivate::OrgBluezGattService1Adaptor::
    OrgBluezGattService1Adaptor(QObject *parent)': leans on
    'QtBluetoothPrivate::OrgBluezGattService1Adaptor::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattService1Adaptor.__init__' has no "
        "cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezGattService1Adaptor::OrgBluezGattServi"
        "ce1Adaptor(QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezGattService1Adaptor::qt_metacall(QMeta"
        "Object::Call, int, void**)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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
