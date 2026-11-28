"""
QXdgNotificationInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qxdgnotificationproxy_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QXdgNotificationInterface to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QXdgNotificationInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXdgNotificationInterface: a plain Python object
  standing in front of one C++ QXdgNotificationInterface.

  What exists
  -----------

  Every function of Qt's QXdgNotificationInterface that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject',
  'staticInterfaceName', 'ActionInvoked', 'NotificationClosed'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QXdgNotificationInterface::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QXdgNotificationInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QXdgNotificationInterface::~QXdgNotificationInterface()': the
    destructor: Python never removes a C++ QXdgNotificationInterface.
  - Qt's 'QDBusPendingReply<>
    QXdgNotificationInterface::closeNotification(uint id)': gives a type
    Python has no way to take yet.
  - Qt's 'QDBusPendingReply<QStringList>
    QXdgNotificationInterface::getCapabilities()': gives a type Python has no
    way to take yet.
  - Qt's 'QDBusPendingReply<QString, QString, QString, QString>
    QXdgNotificationInterface::getServerInformation()': gives a type Python
    has no way to take yet.
  - Qt's 'QDBusReply<QString>
    QXdgNotificationInterface::getServerInformation(QString &vendor, QString
    &version, QString &specVersion)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QDBusPendingReply<uint> QXdgNotificationInterface::notify(const
    QString &appName, uint replacesId, const QString &appIcon, const QString
    &summary, const QString &body, const QStringList &actions, const
    QVariantMap &hints, int timeout)': gives a type Python has no way to take
    yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 leans on
  'QXdgNotificationInterface.

  What to expect
  --------------

  - The C++ QXdgNotificationInterface is created at the first use, not by
    'QXdgNotificationInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXdgNotificationInterface.
  - Qt tells when it has removed the C++ QXdgNotificationInterface. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QXdgNotificationInterface that has no cute function
    yet, '__init__', 'closeNotification', 'getCapabilities',
    'getServerInformation', 'notify', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def staticInterfaceName() -> Optional[str]:
    """
    Calls Qt's 'const char
    *QXdgNotificationInterface::staticInterfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxdgnotificationinterface.html#staticInterfaceName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QXdgNotificationInterface::staticInterfaceName()
    chars = Rituals.call(
        'ritual_ZN25QXdgNotificationInterface19staticInterfaceNameEv',
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXdgNotificationInterface'

  #  A C++ QXdgNotificationInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXdgNotificationInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QXdgNotificationInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxdgnotificationinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QXdgNotificationInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QXdgNotificationInterface10metaObjectEv',
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
    Qt's 'QXdgNotificationInterface::QXdgNotificationInterface(const QString
    &service, const QString &path, const QDBusConnection &connection, QObject
    *parent)': leans on
    'QXdgNotificationInterface::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QXdgNotificationInterface.__init__' has no cute function yet. "
        "Qt's 'QXdgNotificationInterface::QXdgNotificationInterface(const "
        "QString &service, const QString &path, const QDBusConnection "
        "&connection, QObject *parent)': leans on "
        "'QXdgNotificationInterface::qt_metacall(QMetaObject::Call, int, "
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

  @overload(int, str)
  def ActionInvoked(self, id: int, action_key: str) -> None:
    """
    Calls Qt's 'void QXdgNotificationInterface::ActionInvoked(uint id, const
    QString &action_key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxdgnotificationinterface.html#ActionInvoked

    Parameters
    ----------

    id : int
      Passed on as it is.

    action_key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXdgNotificationInterface::ActionInvoked(uint id, const QString
    #      &action_key)
    self.uglySide.call(
        'ritual_ZN25QXdgNotificationInterface13ActionInvokedEjRK7QString',
        id, action_key,
    )

  @overload(int, int)
  def NotificationClosed(self, id: int, reason: int) -> None:
    """
    Calls Qt's 'void QXdgNotificationInterface::NotificationClosed(uint id,
    uint reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxdgnotificationinterface.html#NotificationClosed

    Parameters
    ----------

    id : int
      Passed on as it is.

    reason : int
      Passed on as it is.
    """
    #  void QXdgNotificationInterface::NotificationClosed(uint id, uint
    #      reason)
    self.uglySide.call(
        'ritual_ZN25QXdgNotificationInterface18NotificationClosedEjj',
        id, reason,
    )

  @staticmethod
  def closeNotification(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<>
    QXdgNotificationInterface::closeNotification(uint id)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXdgNotificationInterface.closeNotification' has no cute function "
        "yet. Qt's 'QDBusPendingReply<> "
        "QXdgNotificationInterface::closeNotification(uint id)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def getCapabilities(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<QStringList>
    QXdgNotificationInterface::getCapabilities()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QXdgNotificationInterface.getCapabilities' has no cute function "
        "yet. Qt's 'QDBusPendingReply<QStringList> "
        "QXdgNotificationInterface::getCapabilities()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def getServerInformation(*__, **_) -> Never:
    """
    - Qt's 'QDBusPendingReply<QString, QString, QString, QString>
      QXdgNotificationInterface::getServerInformation()': gives a type Python
      has no way to take yet.
    - Qt's 'QDBusReply<QString>
      QXdgNotificationInterface::getServerInformation(QString &vendor,
      QString &version, QString &specVersion)': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QXdgNotificationInterface.getServerInformation' has no cute "
        "function yet. Qt's 'QDBusPendingReply<QString, QString, QString, "
        "QString> QXdgNotificationInterface::getServerInformation()': gives "
        "a type Python has no way to take yet. Qt's 'QDBusReply<QString> "
        "QXdgNotificationInterface::getServerInformation(QString &vendor, "
        "QString &version, QString &specVersion)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def notify(*__, **_) -> Never:
    """
    Qt's 'QDBusPendingReply<uint> QXdgNotificationInterface::notify(const
    QString &appName, uint replacesId, const QString &appIcon, const QString
    &summary, const QString &body, const QStringList &actions, const
    QVariantMap &hints, int timeout)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QXdgNotificationInterface.notify' has no cute function yet. Qt's "
        "'QDBusPendingReply<uint> QXdgNotificationInterface::notify(const "
        "QString &appName, uint replacesId, const QString &appIcon, const "
        "QString &summary, const QString &body, const QStringList &actions, "
        "const QVariantMap &hints, int timeout)': gives a type Python has "
        "no way to take yet.")
