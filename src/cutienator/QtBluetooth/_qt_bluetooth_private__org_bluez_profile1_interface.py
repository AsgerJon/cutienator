"""
QtBluetoothPrivate::OrgBluezProfile1Interface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/profile1_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezProfile1Interface to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class OrgBluezProfile1Interface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtBluetoothPrivate::OrgBluezProfile1Interface: a
  plain Python object standing in front of one C++
  QtBluetoothPrivate::OrgBluezProfile1Interface.

  What exists
  -----------

  Every function of Qt's QtBluetoothPrivate::OrgBluezProfile1Interface that
  has a ritual and that Python can call so far, 3 names in all: 'metaObject',
  'staticInterfaceName', 'Release'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezProfile1Interface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezProfile1Interface::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezProfile1Interface::
    ~OrgBluezProfile1Interface()': the destructor: Python never removes a C++
    QtBluetoothPrivate::OrgBluezProfile1Interface.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezProfile1Interface::NewConnection(const
    QDBusObjectPath &in0, const QDBusUnixFileDescriptor &in1, const
    QVariantMap &in2)': gives a type Python has no way to take yet.
  - Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezProfile1Interface::RequestDisconnection(const
    QDBusObjectPath &in0)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezProfile1Interface is created at the
    first use, not by 'QtBluetoothPrivate::OrgBluezProfile1Interface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezProfile1Interface.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezProfile1Interface. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgBluezProfile1Interface that has
    no cute function yet, 'NewConnection', 'RequestDisconnection',
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QtBluetoothPrivate::OrgBluezProfile1Interface::staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezprofile1interface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QtBluetoothPrivate::OrgBluezProfile1Interface::
    #      staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface19staticIn'
        'terfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezProfile1Interface'

  #  A C++ QtBluetoothPrivate::OrgBluezProfile1Interface Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezProfile1Interface'

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
    *QtBluetoothPrivate::OrgBluezProfile1Interface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezprofile1interface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezProfile1Interface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate25OrgBluezProfile1Interface10metaObj'
        'ectEv',
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
    Qt's 'QtBluetoothPrivate::OrgBluezProfile1Interface::
    OrgBluezProfile1Interface(const QString &service, const QString &path,
    const QDBusConnection &connection, QObject *parent)': leans on
    'QtBluetoothPrivate::OrgBluezProfile1Interface::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezProfile1Interface.__init__' has no "
        "cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezProfile1Interface::OrgBluezProfile1Int"
        "erface(const QString &service, const QString &path, const "
        "QDBusConnection &connection, QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezProfile1Interface::qt_metacall(QMetaOb"
        "ject::Call, int, void**)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezProfile1Interface::Release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezprofile1interface.html
    """
    #  void QtBluetoothPrivate::OrgBluezProfile1Interface::Release()
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface7ReleaseEv',
    )

  @staticmethod
  def NewConnection(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezProfile1Interface::NewConnection(const
    QDBusObjectPath &in0, const QDBusUnixFileDescriptor &in1, const
    QVariantMap &in2)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezProfile1Interface.NewConnection' has "
        "no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezProfile1Interface::NewConnection(const "
        "QDBusObjectPath &in0, const QDBusUnixFileDescriptor &in1, const "
        "QVariantMap &in2)': gives a type Python has no way to take yet.")

  @staticmethod
  def RequestDisconnection(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QtBluetoothPrivate::OrgBluezProfile1Interface::RequestDisconnection(const
    QDBusObjectPath &in0)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezProfile1Interface.RequestDisconnection'"
        " has no cute function yet. Qt's 'QDBusPendingReply<> "
        "QtBluetoothPrivate::OrgBluezProfile1Interface::RequestDisconnection"
        "(const QDBusObjectPath &in0)': gives a type Python has no way to "
        "take yet.")
