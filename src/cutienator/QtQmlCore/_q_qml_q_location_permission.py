"""
QQmlQLocationPermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCore/6.12.0/QtQmlCore/private/qqmlpermissions_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlQLocationPermission to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from ..QtCore import Qt, QLocationPermission, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQmlQLocationPermission(QObject):
  """
  The cute side of Qt's QQmlQLocationPermission: a plain Python object
  standing in front of one C++ QQmlQLocationPermission.

  It is built on the cute 'QObject', as Qt's QQmlQLocationPermission is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlQLocationPermission that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'status',
  'qmlExtendedNamespace', 'availability', 'accuracy'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlQLocationPermission::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlQLocationPermission::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlQLocationPermission::qt_qmlMarker_extendedNamespace()':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 17 functions Qt declares: 4 leans on 'QQmlQLocationPermission; 3
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlQLocationPermission is created at the first use, not by
    'QQmlQLocationPermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlQLocationPermission.
  - Qt tells when it has removed the C++ QQmlQLocationPermission. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlQLocationPermission that has no cute function yet,
    'accuracyChanged', 'availabilityChanged', 'request', 'setAccuracy',
    'setAvailability', 'statusChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQmlQLocationPermission::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlqlocationpermission.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlQLocationPermission::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN23QQmlQLocationPermission20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlQLocationPermission'

  #  A C++ QQmlQLocationPermission Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlQLocationPermission'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlQLocationPermission::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlqlocationpermission.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlQLocationPermission::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlQLocationPermission10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Qt.PermissionStatus:
    """
    Calls Qt's 'Qt::PermissionStatus QQmlQLocationPermission::status()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlqlocationpermission.html#status

    Returns
    -------

    Qt.PermissionStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.PermissionStatus(number)' gives.
    """
    #  Qt::PermissionStatus QQmlQLocationPermission::status() const
    return Qt.PermissionStatus(self.uglySide.call(
        'ritual_ZNK23QQmlQLocationPermission6statusEv',
    ))

  def availability(self) -> QLocationPermission.Availability:
    """
    Calls Qt's 'QLocationPermission::Availability
    QQmlQLocationPermission::availability() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlqlocationpermission.html#availability

    Returns
    -------

    QLocationPermission.Availability
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocationPermission.Availability(number)' gives.
    """
    #  QLocationPermission::Availability
    #      QQmlQLocationPermission::availability() const
    return QLocationPermission.Availability(self.uglySide.call(
        'ritual_ZNK23QQmlQLocationPermission12availabilityEv',
    ))

  def accuracy(self) -> QLocationPermission.Accuracy:
    """
    Calls Qt's 'QLocationPermission::Accuracy
    QQmlQLocationPermission::accuracy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlqlocationpermission.html#accuracy

    Returns
    -------

    QLocationPermission.Accuracy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocationPermission.Accuracy(number)' gives.
    """
    #  QLocationPermission::Accuracy QQmlQLocationPermission::accuracy()
    #      const
    return QLocationPermission.Accuracy(self.uglySide.call(
        'ritual_ZNK23QQmlQLocationPermission8accuracyEv',
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
  def accuracyChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlQLocationPermission::accuracyChanged()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQmlQLocationPermission.accuracyChanged' has no cute function "
        "yet. Qt's 'void QQmlQLocationPermission::accuracyChanged()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def availabilityChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlQLocationPermission::availabilityChanged()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQmlQLocationPermission.availabilityChanged' has no cute function "
        "yet. Qt's 'void QQmlQLocationPermission::availabilityChanged()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def request(*__, **_) -> Never:
    """
    Qt's 'void QQmlQLocationPermission::request()': leans on
    'QQmlQLocationPermission::statusChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlQLocationPermission.request' has no cute function yet. Qt's "
        "'void QQmlQLocationPermission::request()': leans on "
        "'QQmlQLocationPermission::statusChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setAccuracy(*__, **_) -> Never:
    """
    Qt's 'void QQmlQLocationPermission::setAccuracy(const
    QLocationPermission::Accuracy &value)': leans on
    'QQmlQLocationPermission::statusChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlQLocationPermission.setAccuracy' has no cute function yet. "
        "Qt's 'void QQmlQLocationPermission::setAccuracy(const "
        "QLocationPermission::Accuracy &value)': leans on "
        "'QQmlQLocationPermission::statusChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setAvailability(*__, **_) -> Never:
    """
    Qt's 'void QQmlQLocationPermission::setAvailability(const
    QLocationPermission::Availability &value)': leans on
    'QQmlQLocationPermission::statusChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlQLocationPermission.setAvailability' has no cute function "
        "yet. Qt's 'void QQmlQLocationPermission::setAvailability(const "
        "QLocationPermission::Availability &value)': leans on "
        "'QQmlQLocationPermission::statusChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def statusChanged(*__, **_) -> Never:
    """
    Qt's 'void QQmlQLocationPermission::statusChanged()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQmlQLocationPermission.statusChanged' has no cute function yet. "
        "Qt's 'void QQmlQLocationPermission::statusChanged()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
