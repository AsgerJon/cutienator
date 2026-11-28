"""
Qt3DInput::Input::MouseDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::MouseDevice to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MouseDevice(Qt3DInput.QAbstractPhysicalDeviceBackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::MouseDevice: a plain Python object
  standing in front of one C++ Qt3DInput::Input::MouseDevice.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDeviceBackendNode', as
  Qt's Qt3DInput::Input::MouseDevice is built on Qt's
  Qt3DInput::QAbstractPhysicalDeviceBackendNode, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::MouseDevice that has a ritual and
  that Python can call so far, 11 names in all: 'setInputHandler',
  'inputHandler', 'axisValue', 'isButtonPressed', 'resetMouseAxisState',
  'mouseState', 'previousPos', 'wasPressed', 'sensitivity',
  'updateAxesContinuously', 'syncFromFrontEnd'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::Input::MouseDevice::~MouseDevice()': the destructor:
    Python never removes a C++ Qt3DInput::Input::MouseDevice.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::MouseDevice is created at the first use, not by
    'Qt3DInput::Input::MouseDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::MouseDevice.
  - Each name of Qt's Qt3DInput::Input::MouseDevice that has no cute function
    yet, 'updateMouseEvent', 'updateWheelEvent', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside Qt3DInput::Input::MouseDevice, each a class
  #  in here as in C++.

  class MouseState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DInput::Input::MouseDevice::MouseState: a plain
    Python object standing in front of one C++
    Qt3DInput::Input::MouseDevice::MouseState.

    C++ hands a Qt3DInput::Input::MouseDevice::MouseState around as a copy,
    so every C++ Qt3DInput::Input::MouseDevice::MouseState behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DInput::Input::MouseDevice::MouseState yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DInput::Input::MouseDevice::MouseState::~MouseState()': the
      destructor: Python removes its C++
      Qt3DInput::Input::MouseDevice::MouseState by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ Qt3DInput::Input::MouseDevice::MouseState is created at the
      first use, not by 'Qt3DInput::Input::MouseDevice::MouseState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DInput::Input::MouseDevice::MouseState back
      gives a copy the ritual made for Python, in a new cute
      Qt3DInput::Input::MouseDevice::MouseState.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DInput::Input::MouseDevice::MouseState'

    #  Qt's '~Qt3DInput::Input::MouseDevice::MouseState()'. Naming it makes
    #  this a value class: Python owns every C++
    #  Qt3DInput::Input::MouseDevice::MouseState behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN9Qt3DInput5Input11MouseDevice10MouseStateD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DInput::Input::MouseDevice::MouseState::MouseState()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3dinput-input-mousedevice-mousestate.html
      """
      #  Qt3DInput::Input::MouseDevice::MouseState::MouseState()
      self._noteCreation(MouseDevice.MouseState, lambda: Rituals.call(
          'ritual_ZN9Qt3DInput5Input11MouseDevice10MouseStateC1Ev',
      ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::MouseDevice'

  #  A C++ Qt3DInput::Input::MouseDevice Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_Input_MouseDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def inputHandler(self) -> Optional[Qt3DInput.Input.InputHandler]:
    """
    Calls Qt's 'InputHandler *Qt3DInput::Input::MouseDevice::inputHandler()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#inputHandler

    Returns
    -------

    Optional[Qt3DInput.Input.InputHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InputHandler *Qt3DInput::Input::MouseDevice::inputHandler() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11MouseDevice12inputHandlerEv',
    )
    return Qt3DInput.Input.InputHandler._cuteAt(address)

  @overload(int)
  def axisValue(self, axisIdentifier: int) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::MouseDevice::axisValue(int
    axisIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#axisValue

    Parameters
    ----------

    axisIdentifier : int
      Passed on as it is.
    """
    #  float Qt3DInput::Input::MouseDevice::axisValue(int axisIdentifier)
    #      const
    ritual = 'ritual_ZNK9Qt3DInput5Input11MouseDevice9axisValueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9Qt3DInput5Input11MouseDevice9axisValueEi'
    return self.uglySide.call(ritual, axisIdentifier)

  @overload(int)
  def isButtonPressed(self, buttonIdentifier: int) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::MouseDevice::isButtonPressed(int
    buttonIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#isButtonPressed

    Parameters
    ----------

    buttonIdentifier : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::MouseDevice::isButtonPressed(int
    #      buttonIdentifier) const
    ritual = 'ritual_ZNK9Qt3DInput5Input11MouseDevice15isButtonPressedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input11MouseDevice15isButtonPressedEi')
    return self.uglySide.call(ritual, buttonIdentifier)

  def mouseState(self) -> MouseState:
    """
    Calls Qt's 'MouseState Qt3DInput::Input::MouseDevice::mouseState()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#mouseState

    Returns
    -------

    MouseState
      A new cute Qt3DInput::Input::MouseDevice::MouseState around the copy Qt
      gave back. Python owns it.
    """
    #  MouseState Qt3DInput::Input::MouseDevice::mouseState() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11MouseDevice10mouseStateEv',
    )
    return Qt3DInput.Input.MouseDevice.MouseState._cuteOwning(address)

  def previousPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF Qt3DInput::Input::MouseDevice::previousPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#previousPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF Qt3DInput::Input::MouseDevice::previousPos() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11MouseDevice11previousPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def wasPressed(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::MouseDevice::wasPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#wasPressed
    """
    #  bool Qt3DInput::Input::MouseDevice::wasPressed() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11MouseDevice10wasPressedEv',
    )

  def sensitivity(self) -> float:
    """
    Calls Qt's 'float Qt3DInput::Input::MouseDevice::sensitivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#sensitivity
    """
    #  float Qt3DInput::Input::MouseDevice::sensitivity() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11MouseDevice11sensitivityEv',
    )

  def updateAxesContinuously(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::MouseDevice::updateAxesContinuously()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html
    """
    #  bool Qt3DInput::Input::MouseDevice::updateAxesContinuously() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input11MouseDevice22updateAxesContinuouslyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.Input.InputHandler'])
  @overload(NoneType)
  def setInputHandler(
      self,
      handler: Optional[Qt3DInput.Input.InputHandler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::MouseDevice::setInputHandler(InputHandler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#setInputHandler

    Parameters
    ----------

    handler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::MouseDevice::setInputHandler(InputHandler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input11MouseDevice15setInputHandlerEPNS0_12Inp'
        'utHandlerE',
        self._addressOf(handler),
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
    'Qt3DInput::Input::MouseDevice::MouseDevice()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#MouseDevice
    """
    #  Qt3DInput::Input::MouseDevice::MouseDevice()
    self._noteCreation(MouseDevice, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input11MouseDeviceC1Ev',
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

  def resetMouseAxisState(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::MouseDevice::resetMouseAxisState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html
    """
    #  void Qt3DInput::Input::MouseDevice::resetMouseAxisState()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input11MouseDevice19resetMouseAxisStateEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::MouseDevice::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-mousedevice.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::MouseDevice::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input11MouseDevice16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input11MouseDevice16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def updateMouseEvent(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::MouseDevice::updateMouseEvent(::QMouseEvent
    *events)': the compiler refuses its ritual as it would be written here:
    cannot initialize a parameter of type '::QMouseEvent *' with an lvalue of
    type '::Qt3DInput::QMouseEvent *'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.MouseDevice.updateMouseEvent' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::MouseDevice::updateMouseEvent(::QMouseEvent "
        "*events)': the compiler refuses its ritual as it would be written "
        "here: cannot initialize a parameter of type '::QMouseEvent *' with "
        "an lvalue of type '::Qt3DInput::QMouseEvent *'.")

  @staticmethod
  def updateWheelEvent(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::MouseDevice::updateWheelEvent(::QWheelEvent
    *events)': the compiler refuses its ritual as it would be written here:
    cannot initialize a parameter of type '::QWheelEvent *' with an lvalue of
    type '::Qt3DInput::QWheelEvent *'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.MouseDevice.updateWheelEvent' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::MouseDevice::updateWheelEvent(::QWheelEvent "
        "*events)': the compiler refuses its ritual as it would be written "
        "here: cannot initialize a parameter of type '::QWheelEvent *' with "
        "an lvalue of type '::Qt3DInput::QWheelEvent *'.")
