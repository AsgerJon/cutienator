"""
QQuick3DXrController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcontroller_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrController to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion, QVector3D
  from . import QQuick3DXrHandInput

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrController(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DXrController: a plain Python object standing
  in front of one C++ QQuick3DXrController.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DXrController is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrController that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr', 'controller',
  'setController', 'handInput', 'poseSpace', 'setPoseSpace', 'pokePosition',
  'jointPositions', 'jointRotations', 'isActive', 'controllerChanged',
  'actionMapperChanged', 'poseSpaceChanged', 'pokePositionChanged',
  'jointPositionsChanged', 'jointRotationsChanged', 'jointDataUpdated',
  'isActiveChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrController::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrController is created at the first use, not by
    'QQuick3DXrController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrController.
  - Qt tells when it has removed the C++ QQuick3DXrController. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DXrController, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Controller(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrController::Controller' of Qt, with the 8 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    LeftController = Kee[int](0)
    RightController = Kee[int](1)
    UnknownController = Kee[int](2)
    LeftHand = Kee[int](0)
    RightHand = Kee[int](1)
    ControllerLeft = Kee[int](0)
    ControllerRight = Kee[int](1)
    ControllerNone = Kee[int](2)

  class HandPoseSpace(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrController::HandPoseSpace' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    GripPose = Kee[int](0)
    AimPose = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuick3DXrController::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrcontroller.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DXrController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuick3DXrController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def controller(self) -> Controller:
    """
    Calls Qt's 'Controller QQuick3DXrController::controller() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#controller

    Returns
    -------

    Controller
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Controller(number)'
      gives.
    """
    #  Controller QQuick3DXrController::controller() const
    return QQuick3DXrController.Controller(self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController10controllerEv',
    ))

  def handInput(self) -> Optional[QQuick3DXrHandInput]:
    """
    Calls Qt's 'QQuick3DXrHandInput *QQuick3DXrController::handInput()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#handInput

    Returns
    -------

    Optional[QQuick3DXrHandInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrHandInput *QQuick3DXrController::handInput() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController9handInputEv',
    )
    from . import QQuick3DXrHandInput
    return QQuick3DXrHandInput._cuteAt(address)

  def poseSpace(self) -> HandPoseSpace:
    """
    Calls Qt's 'HandPoseSpace QQuick3DXrController::poseSpace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#poseSpace

    Returns
    -------

    HandPoseSpace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandPoseSpace(number)'
      gives.
    """
    #  HandPoseSpace QQuick3DXrController::poseSpace() const
    return QQuick3DXrController.HandPoseSpace(self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController9poseSpaceEv',
    ))

  def pokePosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DXrController::pokePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#pokePosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DXrController::pokePosition() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController12pokePositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def jointPositions(self) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D> QQuick3DXrController::jointPositions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#jointPositions

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> QQuick3DXrController::jointPositions() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController14jointPositionsEv',
    )
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def jointRotations(self) -> QList[QQuaternion]:
    """
    Calls Qt's 'QList<QQuaternion> QQuick3DXrController::jointRotations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#jointRotations

    Returns
    -------

    QList[QQuaternion]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuaternion> QQuick3DXrController::jointRotations() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DXrController14jointRotationsEv',
    )
    from ..QtGui import QQuaternion
    return QList[QQuaternion]._cuteOwning(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrController::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrcontroller.html#isActive
    """
    #  bool QQuick3DXrController::isActive() const
    return self.uglySide.call('ritual_ZNK20QQuick3DXrController8isActiveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Controller)
  def setController(self, newController: Controller) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::setController(Controller
    newController)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#setController

    Parameters
    ----------

    newController : Controller
      Passed on as its number.
    """
    #  void QQuick3DXrController::setController(Controller newController)
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController13setControllerENS_10ControllerE',
        newController.value,
    )

  @overload(HandPoseSpace)
  def setPoseSpace(self, newPoseSpace: HandPoseSpace) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::setPoseSpace(HandPoseSpace
    newPoseSpace)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#setPoseSpace

    Parameters
    ----------

    newPoseSpace : HandPoseSpace
      Passed on as its number.
    """
    #  void QQuick3DXrController::setPoseSpace(HandPoseSpace newPoseSpace)
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController12setPoseSpaceENS_13HandPoseSpaceE',
        newPoseSpace.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DXrController::QQuick3DXrController()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#QQuick3DXrController
    """
    #  QQuick3DXrController::QQuick3DXrController()
    self._noteCreation(QQuick3DXrController, lambda: Rituals.call(
        'ritual_ZN20QQuick3DXrControllerC1Ev',
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

  def controllerChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::controllerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#controllerChanged
    """
    #  void QQuick3DXrController::controllerChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController17controllerChangedEv',
    )

  def actionMapperChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::actionMapperChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#actionMapperChanged
    """
    #  void QQuick3DXrController::actionMapperChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController19actionMapperChangedEv',
    )

  def poseSpaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::poseSpaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#poseSpaceChanged
    """
    #  void QQuick3DXrController::poseSpaceChanged()
    self.uglySide.call('ritual_ZN20QQuick3DXrController16poseSpaceChangedEv')

  def pokePositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::pokePositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#pokePositionChanged
    """
    #  void QQuick3DXrController::pokePositionChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController19pokePositionChangedEv',
    )

  def jointPositionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::jointPositionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#jointPositionsChanged
    """
    #  void QQuick3DXrController::jointPositionsChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController21jointPositionsChangedEv',
    )

  def jointRotationsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::jointRotationsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#jointRotationsChanged
    """
    #  void QQuick3DXrController::jointRotationsChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DXrController21jointRotationsChangedEv',
    )

  def jointDataUpdated(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::jointDataUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#jointDataUpdated
    """
    #  void QQuick3DXrController::jointDataUpdated()
    self.uglySide.call('ritual_ZN20QQuick3DXrController16jointDataUpdatedEv')

  def isActiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrController::isActiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrcontroller.html#isActiveChanged
    """
    #  void QQuick3DXrController::isActiveChanged()
    self.uglySide.call('ritual_ZN20QQuick3DXrController15isActiveChangedEv')
