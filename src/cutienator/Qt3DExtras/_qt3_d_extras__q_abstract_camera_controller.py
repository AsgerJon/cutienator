"""
Qt3DExtras::QAbstractCameraController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qabstractcameracontroller.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DInput import Qt3DInput
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractCameraController(Qt3DCore.QEntity):
  """
  The cute side of Qt's Qt3DExtras::QAbstractCameraController: a plain Python
  object standing in front of one C++ Qt3DExtras::QAbstractCameraController.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's
  Qt3DExtras::QAbstractCameraController is built on Qt's Qt3DCore::QEntity,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QAbstractCameraController that has a
  ritual and that Python can call so far, 21 names in all: 'metaObject',
  'tr', 'camera', 'linearSpeed', 'lookSpeed', 'acceleration', 'deceleration',
  'setCamera', 'setLinearSpeed', 'setLookSpeed', 'setAcceleration',
  'setDeceleration', 'cameraChanged', 'linearSpeedChanged',
  'lookSpeedChanged', 'accelerationChanged', 'decelerationChanged',
  'keyboardDevice', 'mouseDevice', 'moveCamera', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QAbstractCameraController::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QAbstractCameraController::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DExtras::QAbstractCameraController::~QAbstractCameraController()':
    the destructor: Python never removes a C++
    Qt3DExtras::QAbstractCameraController.
  - Qt's 'Qt3DExtras::QAbstractCameraController::QAbstractCameraController(
    QAbstractCameraControllerPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QAbstractCameraControllerPrivate
    *Qt3DExtras::QAbstractCameraController::d_func() const': takes in Python
    what 'QAbstractCameraControllerPrivate
    *Qt3DExtras::QAbstractCameraController::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QAbstractCameraController is created at the first
    use, not by 'Qt3DExtras::QAbstractCameraController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QAbstractCameraController.
  - Qt tells when it has removed the C++
    Qt3DExtras::QAbstractCameraController. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The classes Qt writes inside Qt3DExtras::QAbstractCameraController, each
  #  a class in here as in C++.

  class InputState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DExtras::QAbstractCameraController::InputState:
    a plain Python object standing in front of one C++
    Qt3DExtras::QAbstractCameraController::InputState.

    C++ hands a Qt3DExtras::QAbstractCameraController::InputState around as a
    copy, so every C++ Qt3DExtras::QAbstractCameraController::InputState
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DExtras::QAbstractCameraController::InputState
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DExtras::QAbstractCameraController::InputState::~InputState()': the
      destructor: Python removes its C++
      Qt3DExtras::QAbstractCameraController::InputState by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DExtras::QAbstractCameraController::InputState is created at
      the first use, not by
      'Qt3DExtras::QAbstractCameraController::InputState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DExtras::QAbstractCameraController::InputState
      back gives a copy the ritual made for Python, in a new cute
      Qt3DExtras::QAbstractCameraController::InputState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DExtras::QAbstractCameraController::InputState'

    #  Qt's '~Qt3DExtras::QAbstractCameraController::InputState()'. Naming it
    #  makes this a value class: Python owns every C++
    #  Qt3DExtras::QAbstractCameraController::InputState behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DExtras25QAbstractCameraController10InputStateD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString Qt3DExtras::QAbstractCameraController::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html#tr

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
    #  QString Qt3DExtras::QAbstractCameraController::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QAbstractCameraController'

  #  A C++ Qt3DExtras::QAbstractCameraController Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QAbstractCameraController'

  #  The functions Qt calls itself that Qt3DExtras::QAbstractCameraController
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'moveCamera': (
          ('_ZN10Qt3DExtras25QAbstractCameraController10moveCameraERKNS0_10'
           'InputStateEf',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'Qt3DExtras:Qt3DExtras.QAbstractCameraController.InputState'),
               ('float', 'number', ''),
           )),
      ),
  }

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
    *Qt3DExtras::QAbstractCameraController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QAbstractCameraController::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def camera(self) -> Optional[Qt3DRender.QCamera]:
    """
    Calls Qt's 'Qt3DRender::QCamera
    *Qt3DExtras::QAbstractCameraController::camera() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html#camera

    Returns
    -------

    Optional[Qt3DRender.QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QCamera *Qt3DExtras::QAbstractCameraController::camera()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController6cameraEv',
    )
    return Qt3DRender.QCamera._cuteAt(address)

  def linearSpeed(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QAbstractCameraController::linearSpeed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  float Qt3DExtras::QAbstractCameraController::linearSpeed() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController11linearSpeedEv',
    )

  def lookSpeed(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QAbstractCameraController::lookSpeed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  float Qt3DExtras::QAbstractCameraController::lookSpeed() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController9lookSpeedEv',
    )

  def acceleration(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QAbstractCameraController::acceleration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  float Qt3DExtras::QAbstractCameraController::acceleration() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController12accelerationEv',
    )

  def deceleration(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QAbstractCameraController::deceleration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  float Qt3DExtras::QAbstractCameraController::deceleration() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController12decelerationEv',
    )

  def keyboardDevice(self) -> Optional[Qt3DInput.QKeyboardDevice]:
    """
    Calls Qt's 'Qt3DInput::QKeyboardDevice
    *Qt3DExtras::QAbstractCameraController::keyboardDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Returns
    -------

    Optional[Qt3DInput.QKeyboardDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DInput::QKeyboardDevice
    #      *Qt3DExtras::QAbstractCameraController::keyboardDevice() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController14keyboardDeviceE'
        'v',
    )
    return Qt3DInput.QKeyboardDevice._cuteAt(address)

  def mouseDevice(self) -> Optional[Qt3DInput.QMouseDevice]:
    """
    Calls Qt's 'Qt3DInput::QMouseDevice
    *Qt3DExtras::QAbstractCameraController::mouseDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Returns
    -------

    Optional[Qt3DInput.QMouseDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DInput::QMouseDevice
    #      *Qt3DExtras::QAbstractCameraController::mouseDevice() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QAbstractCameraController11mouseDeviceEv',
    )
    return Qt3DInput.QMouseDevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QCamera'])
  @overload(NoneType)
  def setCamera(self, camera: Optional[Qt3DRender.QCamera]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::setCamera(Qt3DRender::QCamera
    *camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    camera : Optional[Qt3DRender.QCamera]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QAbstractCameraController::setCamera(Qt3DRender::
    #      QCamera *camera)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController9setCameraEPN10Qt3'
        'DRender7QCameraE',
        self._addressOf(camera),
    )

  @overload(float)
  def setLinearSpeed(self, linearSpeed: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::setLinearSpeed(float
    linearSpeed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    linearSpeed : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::setLinearSpeed(float
    #      linearSpeed)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController14setLinearSpeedEf',
        linearSpeed,
    )

  @overload(float)
  def setLookSpeed(self, lookSpeed: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::setLookSpeed(float lookSpeed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    lookSpeed : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::setLookSpeed(float
    #      lookSpeed)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController12setLookSpeedEf',
        lookSpeed,
    )

  @overload(float)
  def setAcceleration(self, acceleration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::setAcceleration(float
    acceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    acceleration : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::setAcceleration(float
    #      acceleration)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController15setAccelerationE'
        'f',
        acceleration,
    )

  @overload(float)
  def setDeceleration(self, deceleration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::setDeceleration(float
    deceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    deceleration : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::setDeceleration(float
    #      deceleration)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController15setDecelerationE'
        'f',
        deceleration,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QAbstractCameraController::QAbstractCameraController(
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QAbstractCameraController::QAbstractCameraController(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QAbstractCameraController, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraControllerC1EPN8Qt3DCore5QNo'
        'deE',
        self._addressOf(parent),
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

  def cameraChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QAbstractCameraController::cameraChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  void Qt3DExtras::QAbstractCameraController::cameraChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController13cameraChangedEv',
    )

  def linearSpeedChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::linearSpeedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  void Qt3DExtras::QAbstractCameraController::linearSpeedChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController18linearSpeedChang'
        'edEv',
    )

  def lookSpeedChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::lookSpeedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html
    """
    #  void Qt3DExtras::QAbstractCameraController::lookSpeedChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController16lookSpeedChanged'
        'Ev',
    )

  @overload(float)
  def accelerationChanged(self, acceleration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::accelerationChanged(float
    acceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    acceleration : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::accelerationChanged(float
    #      acceleration)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController19accelerationChan'
        'gedEf',
        acceleration,
    )

  @overload(float)
  def decelerationChanged(self, deceleration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractCameraController::decelerationChanged(float
    deceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    deceleration : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::decelerationChanged(float
    #      deceleration)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController19decelerationChan'
        'gedEf',
        deceleration,
    )

  @overload(InputState, float)
  def moveCamera(self, state: InputState, dt: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QAbstractCameraController::moveCamera(const
    InputState &state, float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html

    Parameters
    ----------

    state : InputState
      Passed on as a value: Qt reads the C++
      Qt3DExtras::QAbstractCameraController::InputState, which stays Python's
      own.

    dt : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractCameraController::moveCamera(const
    #      InputState &state, float dt)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController10moveCameraERKNS0'
        '_10InputStateEf',
        self._valueOf(state), dt,
    )

  def d_func(self) -> Optional[Qt3DExtras.QAbstractCameraControllerPrivate]:
    """
    Calls Qt's 'QAbstractCameraControllerPrivate
    *Qt3DExtras::QAbstractCameraController::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractcameracontroller.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QAbstractCameraControllerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractCameraControllerPrivate
    #      *Qt3DExtras::QAbstractCameraController::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QAbstractCameraController6d_funcEv',
    )
    return Qt3DExtras.QAbstractCameraControllerPrivate._cuteAt(address)
