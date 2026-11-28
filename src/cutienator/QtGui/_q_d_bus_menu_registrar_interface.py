"""
QDBusMenuRegistrarInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusmenuregistrarproxy_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDBusMenuRegistrarInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QDBusMenuRegistrarInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMenuRegistrarInterface: a plain Python object
  standing in front of one C++ QDBusMenuRegistrarInterface.

  What exists
  -----------

  Every function of Qt's QDBusMenuRegistrarInterface that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject',
  'staticInterfaceName'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusMenuRegistrarInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDBusMenuRegistrarInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusMenuRegistrarInterface::~QDBusMenuRegistrarInterface()': the
    destructor: Python never removes a C++ QDBusMenuRegistrarInterface.
  - Qt's 'QDBusPendingReply<QString, QDBusObjectPath>
    QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId)': gives a
    type Python has no way to take yet.
  - Qt's 'QDBusReply<QString>
    QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId,
    QDBusObjectPath &menuObjectPath)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QDBusPendingReply<>
    QDBusMenuRegistrarInterface::RegisterWindow(uint windowId, const
    QDBusObjectPath &menuObjectPath)': gives a type Python has no way to take
    yet.
  - Qt's 'QDBusPendingReply<>
    QDBusMenuRegistrarInterface::UnregisterWindow(uint windowId)': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QDBusMenuRegistrarInterface.

  What to expect
  --------------

  - The C++ QDBusMenuRegistrarInterface is created at the first use, not by
    'QDBusMenuRegistrarInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusMenuRegistrarInterface.
  - Qt tells when it has removed the C++ QDBusMenuRegistrarInterface. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusMenuRegistrarInterface that has no cute function
    yet, 'GetMenuForWindow', 'RegisterWindow', 'UnregisterWindow',
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
    *QDBusMenuRegistrarInterface::staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuregistrarinterface.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QDBusMenuRegistrarInterface::staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN27QDBusMenuRegistrarInterface19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMenuRegistrarInterface'

  #  A C++ QDBusMenuRegistrarInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusMenuRegistrarInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusMenuRegistrarInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuregistrarinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusMenuRegistrarInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDBusMenuRegistrarInterface10metaObjectEv',
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
    Qt's 'QDBusMenuRegistrarInterface::QDBusMenuRegistrarInterface(const
    QString &service, const QString &path, const QDBusConnection &connection,
    QObject *parent)': leans on
    'QDBusMenuRegistrarInterface::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMenuRegistrarInterface.__init__' has no cute function yet. "
        "Qt's "
        "'QDBusMenuRegistrarInterface::QDBusMenuRegistrarInterface(const "
        "QString &service, const QString &path, const QDBusConnection "
        "&connection, QObject *parent)': leans on "
        "'QDBusMenuRegistrarInterface::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
  def GetMenuForWindow(*__, **_) -> Never:
    """
    - Qt's 'QDBusPendingReply<QString, QDBusObjectPath>
      QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId)': gives a
      type Python has no way to take yet.
    - Qt's 'QDBusReply<QString>
      QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId,
      QDBusObjectPath &menuObjectPath)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QDBusMenuRegistrarInterface.GetMenuForWindow' has no cute "
        "function yet. Qt's 'QDBusPendingReply<QString, QDBusObjectPath> "
        "QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId)': "
        "gives a type Python has no way to take yet. Qt's "
        "'QDBusReply<QString> "
        "QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId, "
        "QDBusObjectPath &menuObjectPath)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def RegisterWindow(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QDBusMenuRegistrarInterface::RegisterWindow(uint windowId, const
    QDBusObjectPath &menuObjectPath)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QDBusMenuRegistrarInterface.RegisterWindow' has no cute function "
        "yet. Qt's 'QDBusPendingReply<> "
        "QDBusMenuRegistrarInterface::RegisterWindow(uint windowId, const "
        "QDBusObjectPath &menuObjectPath)': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def UnregisterWindow(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QDBusMenuRegistrarInterface::UnregisterWindow(uint windowId)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusMenuRegistrarInterface.UnregisterWindow' has no cute "
        "function yet. Qt's 'QDBusPendingReply<> "
        "QDBusMenuRegistrarInterface::UnregisterWindow(uint windowId)': "
        "gives a type Python has no way to take yet.")
