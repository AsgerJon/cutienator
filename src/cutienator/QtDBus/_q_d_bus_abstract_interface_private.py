"""
QDBusAbstractInterfacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusabstractinterface_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDBusAbstractInterfacePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaProperty, QVariant
  from . import QDBusAbstractInterface, QDBusConnection
  from . import QDBusConnectionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']
  QMetaProperty = WAIT['QMetaProperty']
  QVariant = WAIT['QVariant']


class QDBusAbstractInterfacePrivate(QObjectPrivate):
  """
  The cute side of Qt's QDBusAbstractInterfacePrivate: a plain Python object
  standing in front of one C++ QDBusAbstractInterfacePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QDBusAbstractInterfacePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusAbstractInterfacePrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'canMakeCalls',
  'setProperty', 'connectionPrivate', '_q_serviceOwnerChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDBusAbstractInterface
    *QDBusAbstractInterfacePrivate::q_func() const': takes in Python what
    'QDBusAbstractInterface *QDBusAbstractInterfacePrivate::q_func()' takes.
  - Qt's 'QDBusAbstractInterfacePrivate::~QDBusAbstractInterfacePrivate()':
    the destructor: Python never removes a C++ QDBusAbstractInterfacePrivate.
  - Qt's 'bool QDBusAbstractInterfacePrivate::property(const QMetaProperty
    &mp, void *returnValuePtr) const': names 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 1 leans on 'QDBusConnectionPrivate; 1
  leans on 'qdbus_resolve_me(char const*)', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QDBusAbstractInterfacePrivate is created at the first use, not by
    'QDBusAbstractInterfacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusAbstractInterfacePrivate.
  - Each name of Qt's QDBusAbstractInterfacePrivate that has no cute function
    yet, 'finishDisconnectNotify', 'initOwnerTracking', 'property', holds a
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
  __qt_class__ = 'QDBusAbstractInterfacePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canMakeCalls(self) -> bool:
    """
    Calls Qt's 'bool QDBusAbstractInterfacePrivate::canMakeCalls() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfaceprivate.html#canMakeCalls
    """
    #  bool QDBusAbstractInterfacePrivate::canMakeCalls() const
    return self.uglySide.call(
        'ritual_ZNK29QDBusAbstractInterfacePrivate12canMakeCallsEv',
    )

  def connectionPrivate(self) -> Optional[QDBusConnectionPrivate]:
    """
    Calls Qt's 'QDBusConnectionPrivate
    *QDBusAbstractInterfacePrivate::connectionPrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfaceprivate.html

    Returns
    -------

    Optional[QDBusConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusConnectionPrivate
    #      *QDBusAbstractInterfacePrivate::connectionPrivate() const
    address = self.uglySide.call(
        'ritual_ZNK29QDBusAbstractInterfacePrivate17connectionPrivateEv',
    )
    from . import QDBusConnectionPrivate
    return QDBusConnectionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMetaProperty, QVariant)
  def setProperty(self, mp: QMetaProperty, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QDBusAbstractInterfacePrivate::setProperty(const
    QMetaProperty &mp, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfaceprivate.html#setProperty

    Parameters
    ----------

    mp : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QDBusAbstractInterfacePrivate::setProperty(const QMetaProperty
    #      &mp, const QVariant &value)
    return self.uglySide.call(
        'ritual_ZN29QDBusAbstractInterfacePrivate11setPropertyERK13QMetaPro'
        'pertyRK8QVariant',
        self._valueOf(mp), self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str, str, QDBusConnection, bool)
  def __init__(
      self,
      serv: str,
      p: str,
      iface: str,
      con: QDBusConnection,
      dynamic: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDBusAbstractInterfacePrivate::QDBusAbstractInterfacePrivate(const
    QString &serv, const QString &p, const QString &iface, const
    QDBusConnection &con, bool dynamic)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfaceprivate.html

    Parameters
    ----------

    serv : str
      Passed on as it is: a QString is made of it for the call.

    p : str
      Passed on as it is: a QString is made of it for the call.

    iface : str
      Passed on as it is: a QString is made of it for the call.

    con : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    dynamic : bool
      Passed on as it is.
    """
    #  QDBusAbstractInterfacePrivate::QDBusAbstractInterfacePrivate(const
    #      QString &serv, const QString &p, const QString &iface, const
    #      QDBusConnection &con, bool dynamic)
    self._noteCreation(QDBusAbstractInterfacePrivate, lambda: Rituals.call(
        'ritual_ZN29QDBusAbstractInterfacePrivateC1ERK7QStringS2_S2_RK15QDB'
        'usConnectionb',
        serv, p, iface, self._valueOf(con), dynamic,
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

  def q_func(self) -> Optional[QDBusAbstractInterface]:
    """
    Calls Qt's 'QDBusAbstractInterface
    *QDBusAbstractInterfacePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfaceprivate.html#q_func

    Returns
    -------

    Optional[QDBusAbstractInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusAbstractInterface *QDBusAbstractInterfacePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QDBusAbstractInterfacePrivate6q_funcEv',
    )
    from . import QDBusAbstractInterface
    return QDBusAbstractInterface._cuteAt(address)

  @overload(str, str, str)
  def _q_serviceOwnerChanged(
      self,
      name: str,
      oldOwner: str,
      newOwner: str,
  ) -> None:
    """
    Calls Qt's 'void
    QDBusAbstractInterfacePrivate::_q_serviceOwnerChanged(const QString
    &name, const QString &oldOwner, const QString &newOwner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusabstractinterfaceprivate.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    oldOwner : str
      Passed on as it is: a QString is made of it for the call.

    newOwner : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusAbstractInterfacePrivate::_q_serviceOwnerChanged(const
    #      QString &name, const QString &oldOwner, const QString &newOwner)
    self.uglySide.call(
        'ritual_ZN29QDBusAbstractInterfacePrivate22_q_serviceOwnerChangedER'
        'K7QStringS2_S2_',
        name, oldOwner, newOwner,
    )

  @staticmethod
  def finishDisconnectNotify(*__, **_) -> Never:
    """
    Qt's 'void QDBusAbstractInterfacePrivate::finishDisconnectNotify(
    QDBusAbstractInterface *iface, int signalId)': leans on
    'QDBusConnectionPrivate::disconnectRelay(QString const&, QString const&,
    QString const&, QDBusAbstractInterface*, QMetaMethod const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusAbstractInterfacePrivate.finishDisconnectNotify' has no cute "
        "function yet. Qt's 'void "
        "QDBusAbstractInterfacePrivate::finishDisconnectNotify(QDBusAbstract"
        "Interface *iface, int signalId)': leans on "
        "'QDBusConnectionPrivate::disconnectRelay(QString const&, QString "
        "const&, QString const&, QDBusAbstractInterface*, QMetaMethod "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def initOwnerTracking(*__, **_) -> Never:
    """
    Qt's 'void QDBusAbstractInterfacePrivate::initOwnerTracking()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusAbstractInterfacePrivate.initOwnerTracking' has no cute "
        "function yet. Qt's 'void "
        "QDBusAbstractInterfacePrivate::initOwnerTracking()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def property(*__, **_) -> Never:
    """
    Qt's 'bool QDBusAbstractInterfacePrivate::property(const QMetaProperty
    &mp, void *returnValuePtr) const': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDBusAbstractInterfacePrivate.property' has no cute function yet. "
        "Qt's 'bool QDBusAbstractInterfacePrivate::property(const "
        "QMetaProperty &mp, void *returnValuePtr) const': names 'void', "
        "which has no cute class yet.")
