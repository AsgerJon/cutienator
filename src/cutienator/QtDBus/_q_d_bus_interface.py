"""
QDBusInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDBusAbstractInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDBusConnection, QDBusInterfacePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']
  QDBusInterfacePrivate = WAIT['QDBusInterfacePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusInterface(QDBusAbstractInterface):
  """
  The cute side of Qt's QDBusInterface: a plain Python object standing in
  front of one C++ QDBusInterface.

  It is built on the cute 'QDBusAbstractInterface', as Qt's QDBusInterface is
  built on Qt's QDBusAbstractInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusInterface that has a ritual and that Python can
  call so far, 2 names in all: 'metaObject', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusInterface::~QDBusInterface()': the destructor: Python never
    removes a C++ QDBusInterface.
  - Qt's 'void *QDBusInterface::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDBusInterface::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QDBusInterfacePrivate *QDBusInterface::d_func() const': takes
    in Python what 'QDBusInterfacePrivate *QDBusInterface::d_func()' takes.

  What to expect
  --------------

  - The C++ QDBusInterface is created at the first use, not by
    'QDBusInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusInterface.
  - Qt tells when it has removed the C++ QDBusInterface. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusInterface'

  #  A C++ QDBusInterface Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusInterface::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusInterface::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QDBusInterface10metaObjectEv')
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

  @overload(QDBusInterfacePrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QDBusInterfacePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDBusInterface::QDBusInterface(QDBusInterfacePrivate *p)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusinterface.html#QDBusInterface

    Parameters
    ----------

    p : Optional[QDBusInterfacePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusInterface::QDBusInterface(QDBusInterfacePrivate *p)
    self._noteCreation(QDBusInterface, lambda: Rituals.call(
        'ritual_ZN14QDBusInterfaceC1EP21QDBusInterfacePrivate',
        self._addressOf(p),
    ))

  @overload(str, str, str, QDBusConnection)
  @overload(str, str, str, QDBusConnection, QObject)
  @overload(str, str, str, QDBusConnection, NoneType)
  def __init__(
      self,
      service: str,
      path: str,
      interface: str,
      connection: QDBusConnection,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDBusInterface::QDBusInterface(const
    QString &service, const QString &path, const QString &interface, const
    QDBusConnection &connection, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusinterface.html#QDBusInterface

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    path : str
      Passed on as it is: a QString is made of it for the call.

    interface : str
      Passed on as it is: a QString is made of it for the call.

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusInterface::QDBusInterface(const QString &service, const QString
    #      &path, const QString &interface, const QDBusConnection
    #      &connection, QObject *parent)
    self._noteCreation(QDBusInterface, lambda: Rituals.call(
        'ritual_ZN14QDBusInterfaceC1ERK7QStringS2_S2_RK15QDBusConnectionP7Q'
        'Object',
        service, path, interface, self._valueOf(connection),
        self._addressOf(parent, 'QObject'),
    ))

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

  def d_func(self) -> Optional[QDBusInterfacePrivate]:
    """
    Calls Qt's 'QDBusInterfacePrivate *QDBusInterface::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusinterface.html#d_func

    Returns
    -------

    Optional[QDBusInterfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusInterfacePrivate *QDBusInterface::d_func()
    address = self.uglySide.call('ritual_ZN14QDBusInterface6d_funcEv')
    from . import QDBusInterfacePrivate
    return QDBusInterfacePrivate._cuteAt(address)
