"""
QQuick3DXrHandInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrhandinput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrHandInput to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion, QVector3D


class QQuick3DXrHandInput(QObject):
  """
  The cute side of Qt's QQuick3DXrHandInput: a plain Python object standing
  in front of one C++ QQuick3DXrHandInput.

  It is built on the cute 'QObject', as Qt's QQuick3DXrHandInput is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrHandInput that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'isActive',
  'jointPositions', 'jointRotations', 'pokePosition', 'isHandTrackingActive',
  'isActiveChanged', 'poseSpaceChanged', 'posePositionChanged',
  'poseRotationChanged', 'jointPositionsChanged', 'jointRotationsChanged',
  'jointDataUpdated', 'pokePositionChanged', 'isHandTrackingChanged'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrHandInput::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrHandInput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 25 functions Qt declares: 4 leans on 'QQuick3DXrHandInput; 2 not a
  gap; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file; 1 leans on 'vtable for
  QQuick3DXrHandInput', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuick3DXrHandInput is created at the first use, not by
    'QQuick3DXrHandInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrHandInput.
  - Qt tells when it has removed the C++ QQuick3DXrHandInput. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrHandInput that has no cute function yet,
    '__init__', 'setIsActive', 'setIsHandTrackingActive',
    'setJointPositionsAndRotations', 'setPokePosition', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrHandInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrHandInput::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrHandInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrHandInput::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrhandinput.html#isActive
    """
    #  bool QQuick3DXrHandInput::isActive() const
    return self.uglySide.call('ritual_ZNK19QQuick3DXrHandInput8isActiveEv')

  def jointPositions(self) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D> QQuick3DXrHandInput::jointPositions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#jointPositions

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> QQuick3DXrHandInput::jointPositions() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandInput14jointPositionsEv',
    )
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def jointRotations(self) -> QList[QQuaternion]:
    """
    Calls Qt's 'QList<QQuaternion> QQuick3DXrHandInput::jointRotations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#jointRotations

    Returns
    -------

    QList[QQuaternion]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuaternion> QQuick3DXrHandInput::jointRotations() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandInput14jointRotationsEv',
    )
    from ..QtGui import QQuaternion
    return QList[QQuaternion]._cuteOwning(address)

  def pokePosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DXrHandInput::pokePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#pokePosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DXrHandInput::pokePosition() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandInput12pokePositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isHandTrackingActive(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrHandInput::isHandTrackingActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#isHandTrackingActive
    """
    #  bool QQuick3DXrHandInput::isHandTrackingActive() const
    return self.uglySide.call(
        'ritual_ZNK19QQuick3DXrHandInput20isHandTrackingActiveEv',
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
    Qt's 'QQuick3DXrHandInput::QQuick3DXrHandInput(QObject *parent)': leans
    on 'vtable for QQuick3DXrHandInput', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandInput.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrHandInput::QQuick3DXrHandInput(QObject *parent)': leans "
        "on 'vtable for QQuick3DXrHandInput', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def isActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::isActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#isActiveChanged
    """
    #  void QQuick3DXrHandInput::isActiveChanged()
    self.uglySide.call('ritual_ZN19QQuick3DXrHandInput15isActiveChangedEv')

  def poseSpaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::poseSpaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#poseSpaceChanged
    """
    #  void QQuick3DXrHandInput::poseSpaceChanged()
    self.uglySide.call('ritual_ZN19QQuick3DXrHandInput16poseSpaceChangedEv')

  def posePositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::posePositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#posePositionChanged
    """
    #  void QQuick3DXrHandInput::posePositionChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandInput19posePositionChangedEv',
    )

  def poseRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::poseRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#poseRotationChanged
    """
    #  void QQuick3DXrHandInput::poseRotationChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandInput19poseRotationChangedEv',
    )

  def jointPositionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::jointPositionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#jointPositionsChanged
    """
    #  void QQuick3DXrHandInput::jointPositionsChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandInput21jointPositionsChangedEv',
    )

  def jointRotationsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::jointRotationsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#jointRotationsChanged
    """
    #  void QQuick3DXrHandInput::jointRotationsChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandInput21jointRotationsChangedEv',
    )

  def jointDataUpdated(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::jointDataUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#jointDataUpdated
    """
    #  void QQuick3DXrHandInput::jointDataUpdated()
    self.uglySide.call('ritual_ZN19QQuick3DXrHandInput16jointDataUpdatedEv')

  def pokePositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::pokePositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#pokePositionChanged
    """
    #  void QQuick3DXrHandInput::pokePositionChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandInput19pokePositionChangedEv',
    )

  def isHandTrackingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrHandInput::isHandTrackingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrhandinput.html#isHandTrackingChanged
    """
    #  void QQuick3DXrHandInput::isHandTrackingChanged()
    self.uglySide.call(
        'ritual_ZN19QQuick3DXrHandInput21isHandTrackingChangedEv',
    )

  @staticmethod
  def setIsActive(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHandInput::setIsActive(bool isActive)': leans on
    'QQuick3DXrHandInput::isActiveChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandInput.setIsActive' has no cute function yet. Qt's "
        "'void QQuick3DXrHandInput::setIsActive(bool isActive)': leans on "
        "'QQuick3DXrHandInput::isActiveChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setIsHandTrackingActive(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHandInput::setIsHandTrackingActive(bool
    newIsHandTracking)': leans on
    'QQuick3DXrHandInput::isHandTrackingChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandInput.setIsHandTrackingActive' has no cute function "
        "yet. Qt's 'void QQuick3DXrHandInput::setIsHandTrackingActive(bool "
        "newIsHandTracking)': leans on "
        "'QQuick3DXrHandInput::isHandTrackingChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setJointPositionsAndRotations(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHandInput::setJointPositionsAndRotations(const
    QList<QVector3D> &newJointPositions, const QList<QQuaternion>
    &newJointRotations)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: incomplete type
    'QQuick3DXrInputManagerPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandInput.setJointPositionsAndRotations' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrHandInput::setJointPositionsAndRotations(const "
        "QList<QVector3D> &newJointPositions, const QList<QQuaternion> "
        "&newJointRotations)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: "
        "incomplete type 'QQuick3DXrInputManagerPrivate' named in nested "
        "name specifier.")

  @staticmethod
  def setPokePosition(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrHandInput::setPokePosition(const QVector3D
    &newPokePosition)': leans on
    'QQuick3DXrHandInput::pokePositionChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrHandInput.setPokePosition' has no cute function yet. "
        "Qt's 'void QQuick3DXrHandInput::setPokePosition(const QVector3D "
        "&newPokePosition)': leans on "
        "'QQuick3DXrHandInput::pokePositionChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
