"""
QAbstractPhysicsBody binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qabstractphysicsbody_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstractPhysicsBody to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QAbstractPhysicsNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QPhysicsMaterial


class QAbstractPhysicsBody(QAbstractPhysicsNode):
  """
  The cute side of Qt's QAbstractPhysicsBody: a plain Python object standing
  in front of one C++ QAbstractPhysicsBody.

  It is built on the cute 'QAbstractPhysicsNode', as Qt's
  QAbstractPhysicsBody is built on Qt's QAbstractPhysicsNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractPhysicsBody that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'physicsMaterial',
  'simulationEnabled', 'physicsMaterialChanged', 'simulationEnabledChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractPhysicsBody::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractPhysicsBody::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QAbstractPhysicsBody::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 3 leans on 'QAbstractPhysicsBody; 2 not
  a gap; 1 the class is abstract, so C++ cannot make one, and the C++ class
  of ours does not fill in every function it leaves open.

  What to expect
  --------------

  - The C++ QAbstractPhysicsBody is created at the first use, not by
    'QAbstractPhysicsBody(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractPhysicsBody.
  - Qt tells when it has removed the C++ QAbstractPhysicsBody. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractPhysicsBody that has no cute function yet,
    '__init__', 'setPhysicsMaterial', 'setSimulationEnabled', holds a
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
  __qt_class__ = 'QAbstractPhysicsBody'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractPhysicsBody::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsbody.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractPhysicsBody::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsBody10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def physicsMaterial(self) -> Optional[QPhysicsMaterial]:
    """
    Calls Qt's 'QPhysicsMaterial *QAbstractPhysicsBody::physicsMaterial()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsbody.html#physicsMaterial

    Returns
    -------

    Optional[QPhysicsMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPhysicsMaterial *QAbstractPhysicsBody::physicsMaterial() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsBody15physicsMaterialEv',
    )
    from . import QPhysicsMaterial
    return QPhysicsMaterial._cuteAt(address)

  def simulationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAbstractPhysicsBody::simulationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsbody.html#simulationEnabled
    """
    #  bool QAbstractPhysicsBody::simulationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK20QAbstractPhysicsBody17simulationEnabledEv',
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
    Qt's 'QAbstractPhysicsBody::QAbstractPhysicsBody()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsBody.__init__' has no cute function yet. Qt's "
        "'QAbstractPhysicsBody::QAbstractPhysicsBody()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def physicsMaterialChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsBody::physicsMaterialChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsbody.html#physicsMaterialChanged
    """
    #  void QAbstractPhysicsBody::physicsMaterialChanged()
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsBody22physicsMaterialChangedEv',
    )

  def simulationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractPhysicsBody::simulationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractphysicsbody.html#simulationEnabledChanged
    """
    #  void QAbstractPhysicsBody::simulationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN20QAbstractPhysicsBody24simulationEnabledChangedEv',
    )

  @staticmethod
  def setPhysicsMaterial(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsBody::setPhysicsMaterial(QPhysicsMaterial
    *newPhysicsMaterial)': leans on
    'QAbstractPhysicsBody::physicsMaterialChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsBody.setPhysicsMaterial' has no cute function "
        "yet. Qt's 'void "
        "QAbstractPhysicsBody::setPhysicsMaterial(QPhysicsMaterial "
        "*newPhysicsMaterial)': leans on "
        "'QAbstractPhysicsBody::physicsMaterialChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setSimulationEnabled(*__, **_) -> Never:
    """
    Qt's 'void QAbstractPhysicsBody::setSimulationEnabled(bool
    newSimulationEnabled)': leans on
    'QAbstractPhysicsBody::simulationEnabledChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QAbstractPhysicsBody.setSimulationEnabled' has no cute function "
        "yet. Qt's 'void QAbstractPhysicsBody::setSimulationEnabled(bool "
        "newSimulationEnabled)': leans on "
        "'QAbstractPhysicsBody::simulationEnabledChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
