"""
QQmlBluetoothPermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCore/6.12.0/QtQmlCore/private/qqmlpermissions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlBluetoothPermission to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from ..QtCore import Qt, QBluetoothPermission, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQmlBluetoothPermission(QObject):
  """
  The cute side of Qt's QQmlBluetoothPermission: a plain Python object
  standing in front of one C++ QQmlBluetoothPermission.

  It is built on the cute 'QObject', as Qt's QQmlBluetoothPermission is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlBluetoothPermission that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'status',
  'qmlExtendedNamespace', 'communicationModes'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlBluetoothPermission::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlBluetoothPermission::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlBluetoothPermission::qt_qmlMarker_extendedNamespace()':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 3 leans on 'QQmlBluetoothPermission; 2
  not a gap; 2 cannot be called and cannot be called through the meta-object
  and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlBluetoothPermission is created at the first use, not by
    'QQmlBluetoothPermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlBluetoothPermission.
  - Qt tells when it has removed the C++ QQmlBluetoothPermission. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlBluetoothPermission that has no cute function yet,
    'communicationModesChanged', 'request', 'setCommunicationModes',
    'statusChanged', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQmlBluetoothPermission::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbluetoothpermission.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlBluetoothPermission::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN23QQmlBluetoothPermission20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBluetoothPermission'

  #  A C++ QQmlBluetoothPermission Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlBluetoothPermission'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlBluetoothPermission::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbluetoothpermission.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlBluetoothPermission::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlBluetoothPermission10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Qt.PermissionStatus:
    """
    Calls Qt's 'Qt::PermissionStatus QQmlBluetoothPermission::status()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbluetoothpermission.html#status

    Returns
    -------

    Qt.PermissionStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.PermissionStatus(number)' gives.
    """
    #  Qt::PermissionStatus QQmlBluetoothPermission::status() const
    return Qt.PermissionStatus(self.uglySide.call(
        'ritual_ZNK23QQmlBluetoothPermission6statusEv',
    ))

  def communicationModes(self) -> QBluetoothPermission.CommunicationModes:
    """
    Calls Qt's 'QBluetoothPermission::CommunicationModes
    QQmlBluetoothPermission::communicationModes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbluetoothpermission.html#communicationModes

    Returns
    -------

    QBluetoothPermission.CommunicationModes
      The value standing for the combination Qt gave back.
    """
    #  QBluetoothPermission::CommunicationModes
    #      QQmlBluetoothPermission::communicationModes() const
    return QBluetoothPermission.CommunicationModes(self.uglySide.call(
        'ritual_ZNK23QQmlBluetoothPermission18communicationModesEv',
    ))

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
  def communicationModesChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlBluetoothPermission::communicationModesChanged()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQmlBluetoothPermission.communicationModesChanged' has no cute "
        "function yet. Qt's 'void "
        "QQmlBluetoothPermission::communicationModesChanged()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def request(*__, **_) -> Never:
    """
    Qt's 'void QQmlBluetoothPermission::request()': leans on
    'QQmlBluetoothPermission::statusChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlBluetoothPermission.request' has no cute function yet. Qt's "
        "'void QQmlBluetoothPermission::request()': leans on "
        "'QQmlBluetoothPermission::statusChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setCommunicationModes(*__, **_) -> Never:
    """
    Qt's 'void QQmlBluetoothPermission::setCommunicationModes(const
    QBluetoothPermission::CommunicationModes &value)': leans on
    'QQmlBluetoothPermission::statusChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlBluetoothPermission.setCommunicationModes' has no cute "
        "function yet. Qt's 'void "
        "QQmlBluetoothPermission::setCommunicationModes(const "
        "QBluetoothPermission::CommunicationModes &value)': leans on "
        "'QQmlBluetoothPermission::statusChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def statusChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlBluetoothPermission::statusChanged()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQmlBluetoothPermission.statusChanged' has no cute function yet. "
        "Qt's 'void QQmlBluetoothPermission::statusChanged()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
