"""
Qt3DInput::Input::InputHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/inputhandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::InputHandler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InputHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DInput::Input::InputHandler: a plain Python object
  standing in front of one C++ Qt3DInput::Input::InputHandler.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::InputHandler that has a ritual and
  that Python can call so far, 24 names in all: 'setScene',
  'keyboardDeviceManager', 'keyboardInputManager', 'mouseDeviceManager',
  'mouseInputManager', 'axisManager', 'axisAccumulatorManager',
  'actionManager', 'axisSettingManager', 'actionInputManager',
  'analogAxisInputManager', 'buttonAxisInputManager', 'inputChordManager',
  'inputSequenceManager', 'logicalDeviceManager',
  'genericDeviceBackendNodeManager', 'physicalDeviceProxyManager',
  'inputSettings', 'resetMouseAxisState', 'addInputDeviceIntegration',
  'setInputSettings', 'updateEventSource', 'setEventFilterService',
  'lookupActionInput'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DInput::Input::InputHandler::appendKeyboardDevice(HKeyboardDevice
    device)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DInput::Input::InputHandler::removeKeyboardDevice(HKeyboardDevice
    device)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DInput::Input::InputHandler::appendMouseDevice(HMouseDevice
    device)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DInput::Input::InputHandler::removeMouseDevice(HMouseDevice
    device)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DInput::Input::InputHandler::appendGenericDevice(
    HGenericDeviceBackendNode device)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void Qt3DInput::Input::InputHandler::removeGenericDevice(
    HGenericDeviceBackendNode device)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<Qt3DInput::QInputDeviceIntegration *>
    Qt3DInput::Input::InputHandler::inputDeviceIntegrations() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 36 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'vtable for Qt3DInput.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::InputHandler is created at the first use, not
    by 'Qt3DInput::Input::InputHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::InputHandler.
  - Each name of Qt's Qt3DInput::Input::InputHandler that has no cute
    function yet, '__init__', 'appendGenericDevice', 'appendKeyboardDevice',
    'appendMouseDevice', 'createPhysicalDevice', 'inputDeviceIntegrations',
    'registerEventFilters', 'removeGenericDevice', 'removeKeyboardDevice',
    'removeMouseDevice', 'unregisterEventFilters', holds a function that
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
  __qt_class__ = 'Qt3DInput::Input::InputHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def keyboardDeviceManager(
      self,
  ) -> Optional[Qt3DInput.Input.KeyboardDeviceManager]:
    """
    Calls Qt's 'KeyboardDeviceManager
    *Qt3DInput::Input::InputHandler::keyboardDeviceManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.KeyboardDeviceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  KeyboardDeviceManager
    #      *Qt3DInput::Input::InputHandler::keyboardDeviceManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler21keyboardDeviceManagerEv',
    )
    return Qt3DInput.Input.KeyboardDeviceManager._cuteAt(address)

  def keyboardInputManager(
      self,
  ) -> Optional[Qt3DInput.Input.KeyboardInputManager]:
    """
    Calls Qt's 'KeyboardInputManager
    *Qt3DInput::Input::InputHandler::keyboardInputManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.KeyboardInputManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  KeyboardInputManager
    #      *Qt3DInput::Input::InputHandler::keyboardInputManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler20keyboardInputManagerEv',
    )
    return Qt3DInput.Input.KeyboardInputManager._cuteAt(address)

  def mouseDeviceManager(
      self,
  ) -> Optional[Qt3DInput.Input.MouseDeviceManager]:
    """
    Calls Qt's 'MouseDeviceManager
    *Qt3DInput::Input::InputHandler::mouseDeviceManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.MouseDeviceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MouseDeviceManager
    #      *Qt3DInput::Input::InputHandler::mouseDeviceManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler18mouseDeviceManagerEv',
    )
    return Qt3DInput.Input.MouseDeviceManager._cuteAt(address)

  def mouseInputManager(self) -> Optional[Qt3DInput.Input.MouseInputManager]:
    """
    Calls Qt's 'MouseInputManager
    *Qt3DInput::Input::InputHandler::mouseInputManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.MouseInputManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MouseInputManager *Qt3DInput::Input::InputHandler::mouseInputManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler17mouseInputManagerEv',
    )
    return Qt3DInput.Input.MouseInputManager._cuteAt(address)

  def axisManager(self) -> Optional[Qt3DInput.Input.AxisManager]:
    """
    Calls Qt's 'AxisManager *Qt3DInput::Input::InputHandler::axisManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html#axisManager

    Returns
    -------

    Optional[Qt3DInput.Input.AxisManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AxisManager *Qt3DInput::Input::InputHandler::axisManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler11axisManagerEv',
    )
    return Qt3DInput.Input.AxisManager._cuteAt(address)

  def axisAccumulatorManager(
      self,
  ) -> Optional[Qt3DInput.Input.AxisAccumulatorManager]:
    """
    Calls Qt's 'AxisAccumulatorManager
    *Qt3DInput::Input::InputHandler::axisAccumulatorManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.AxisAccumulatorManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AxisAccumulatorManager
    #      *Qt3DInput::Input::InputHandler::axisAccumulatorManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler22axisAccumulatorManagerEv',
    )
    return Qt3DInput.Input.AxisAccumulatorManager._cuteAt(address)

  def actionManager(self) -> Optional[Qt3DInput.Input.ActionManager]:
    """
    Calls Qt's 'ActionManager
    *Qt3DInput::Input::InputHandler::actionManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html#actionManager

    Returns
    -------

    Optional[Qt3DInput.Input.ActionManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ActionManager *Qt3DInput::Input::InputHandler::actionManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler13actionManagerEv',
    )
    return Qt3DInput.Input.ActionManager._cuteAt(address)

  def axisSettingManager(
      self,
  ) -> Optional[Qt3DInput.Input.AxisSettingManager]:
    """
    Calls Qt's 'AxisSettingManager
    *Qt3DInput::Input::InputHandler::axisSettingManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.AxisSettingManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AxisSettingManager
    #      *Qt3DInput::Input::InputHandler::axisSettingManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler18axisSettingManagerEv',
    )
    return Qt3DInput.Input.AxisSettingManager._cuteAt(address)

  def actionInputManager(
      self,
  ) -> Optional[Qt3DInput.Input.ActionInputManager]:
    """
    Calls Qt's 'ActionInputManager
    *Qt3DInput::Input::InputHandler::actionInputManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.ActionInputManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ActionInputManager
    #      *Qt3DInput::Input::InputHandler::actionInputManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler18actionInputManagerEv',
    )
    return Qt3DInput.Input.ActionInputManager._cuteAt(address)

  def analogAxisInputManager(
      self,
  ) -> Optional[Qt3DInput.Input.AnalogAxisInputManager]:
    """
    Calls Qt's 'AnalogAxisInputManager
    *Qt3DInput::Input::InputHandler::analogAxisInputManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.AnalogAxisInputManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AnalogAxisInputManager
    #      *Qt3DInput::Input::InputHandler::analogAxisInputManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler22analogAxisInputManagerEv',
    )
    return Qt3DInput.Input.AnalogAxisInputManager._cuteAt(address)

  def buttonAxisInputManager(
      self,
  ) -> Optional[Qt3DInput.Input.ButtonAxisInputManager]:
    """
    Calls Qt's 'ButtonAxisInputManager
    *Qt3DInput::Input::InputHandler::buttonAxisInputManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.ButtonAxisInputManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ButtonAxisInputManager
    #      *Qt3DInput::Input::InputHandler::buttonAxisInputManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler22buttonAxisInputManagerEv',
    )
    return Qt3DInput.Input.ButtonAxisInputManager._cuteAt(address)

  def inputChordManager(self) -> Optional[Qt3DInput.Input.InputChordManager]:
    """
    Calls Qt's 'InputChordManager
    *Qt3DInput::Input::InputHandler::inputChordManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.InputChordManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InputChordManager *Qt3DInput::Input::InputHandler::inputChordManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler17inputChordManagerEv',
    )
    return Qt3DInput.Input.InputChordManager._cuteAt(address)

  def inputSequenceManager(
      self,
  ) -> Optional[Qt3DInput.Input.InputSequenceManager]:
    """
    Calls Qt's 'InputSequenceManager
    *Qt3DInput::Input::InputHandler::inputSequenceManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.InputSequenceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InputSequenceManager
    #      *Qt3DInput::Input::InputHandler::inputSequenceManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler20inputSequenceManagerEv',
    )
    return Qt3DInput.Input.InputSequenceManager._cuteAt(address)

  def logicalDeviceManager(
      self,
  ) -> Optional[Qt3DInput.Input.LogicalDeviceManager]:
    """
    Calls Qt's 'LogicalDeviceManager
    *Qt3DInput::Input::InputHandler::logicalDeviceManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.LogicalDeviceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LogicalDeviceManager
    #      *Qt3DInput::Input::InputHandler::logicalDeviceManager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler20logicalDeviceManagerEv',
    )
    return Qt3DInput.Input.LogicalDeviceManager._cuteAt(address)

  def genericDeviceBackendNodeManager(
      self,
  ) -> Optional[Qt3DInput.Input.GenericDeviceBackendNodeManager]:
    """
    Calls Qt's 'GenericDeviceBackendNodeManager
    *Qt3DInput::Input::InputHandler::genericDeviceBackendNodeManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.GenericDeviceBackendNodeManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  GenericDeviceBackendNodeManager
    #      *Qt3DInput::Input::InputHandler::genericDeviceBackendNodeManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler31genericDeviceBackendNode'
        'ManagerEv',
    )
    return Qt3DInput.Input.GenericDeviceBackendNodeManager._cuteAt(address)

  def physicalDeviceProxyManager(
      self,
  ) -> Optional[Qt3DInput.Input.PhysicalDeviceProxyManager]:
    """
    Calls Qt's 'PhysicalDeviceProxyManager
    *Qt3DInput::Input::InputHandler::physicalDeviceProxyManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Returns
    -------

    Optional[Qt3DInput.Input.PhysicalDeviceProxyManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PhysicalDeviceProxyManager
    #      *Qt3DInput::Input::InputHandler::physicalDeviceProxyManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler26physicalDeviceProxyManag'
        'erEv',
    )
    return Qt3DInput.Input.PhysicalDeviceProxyManager._cuteAt(address)

  def inputSettings(self) -> Optional[Qt3DInput.Input.InputSettings]:
    """
    Calls Qt's 'InputSettings
    *Qt3DInput::Input::InputHandler::inputSettings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html#inputSettings

    Returns
    -------

    Optional[Qt3DInput.Input.InputSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  InputSettings *Qt3DInput::Input::InputHandler::inputSettings() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler13inputSettingsEv',
    )
    return Qt3DInput.Input.InputSettings._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupActionInput(
      self,
      id: Qt3DCore.QNodeId,
  ) -> Optional[Qt3DInput.Input.AbstractActionInput]:
    """
    Calls Qt's 'AbstractActionInput
    *Qt3DInput::Input::InputHandler::lookupActionInput(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DInput.Input.AbstractActionInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractActionInput
    #      *Qt3DInput::Input::InputHandler::lookupActionInput(Qt3DCore::
    #      QNodeId id) const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input12InputHandler17lookupActionInputEN8Qt3D'
        'Core7QNodeIdE',
        self._valueOf(id),
    )
    return Qt3DInput.Input.AbstractActionInput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QScene'])
  @overload(NoneType)
  def setScene(self, scene: Optional[Qt3DCore.QScene]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::InputHandler::setScene(Qt3DCore::QScene *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html#setScene

    Parameters
    ----------

    scene : Optional[Qt3DCore.QScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::InputHandler::setScene(Qt3DCore::QScene *scene)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input12InputHandler8setSceneEPN8Qt3DCore6QScen'
        'eE',
        self._addressOf(scene),
    )

  @overload(WAIT['Qt3DInput.Input.InputSettings'])
  @overload(NoneType)
  def setInputSettings(
      self,
      settings: Optional[Qt3DInput.Input.InputSettings],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::InputHandler::setInputSettings(InputSettings
    *settings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html#setInputSettings

    Parameters
    ----------

    settings : Optional[Qt3DInput.Input.InputSettings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::InputHandler::setInputSettings(InputSettings
    #      *settings)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input12InputHandler16setInputSettingsEPNS0_13I'
        'nputSettingsE',
        self._addressOf(settings),
    )

  @overload(WAIT['Qt3DCore.QEventFilterService'])
  @overload(NoneType)
  def setEventFilterService(
      self,
      service: Optional[Qt3DCore.QEventFilterService],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::InputHandler::setEventFilterService(Qt3DCore::
    QEventFilterService *service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Parameters
    ----------

    service : Optional[Qt3DCore.QEventFilterService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::InputHandler::setEventFilterService(Qt3DCore::
    #      QEventFilterService *service)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input12InputHandler21setEventFilterServiceEPN8'
        'Qt3DCore19QEventFilterServiceE',
        self._addressOf(service),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DInput::Input::InputHandler::InputHandler()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'InternalEventFilter'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.__init__' has no cute function yet. "
        "Qt's 'Qt3DInput::Input::InputHandler::InputHandler()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'InternalEventFilter'.")

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
    Calls Qt's 'void Qt3DInput::Input::InputHandler::resetMouseAxisState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html
    """
    #  void Qt3DInput::Input::InputHandler::resetMouseAxisState()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input12InputHandler19resetMouseAxisStateEv',
    )

  @overload(WAIT['Qt3DInput.QInputDeviceIntegration'])
  @overload(NoneType)
  def addInputDeviceIntegration(
      self,
      inputIntegration: Optional[Qt3DInput.QInputDeviceIntegration],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::InputHandler::addInputDeviceIntegration(
    QInputDeviceIntegration *inputIntegration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html

    Parameters
    ----------

    inputIntegration : Optional[Qt3DInput.QInputDeviceIntegration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::InputHandler::addInputDeviceIntegration(
    #      QInputDeviceIntegration *inputIntegration)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input12InputHandler25addInputDeviceIntegration'
        'EPNS_23QInputDeviceIntegrationE',
        self._addressOf(inputIntegration),
    )

  def updateEventSource(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::InputHandler::updateEventSource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-inputhandler.html
    """
    #  void Qt3DInput::Input::InputHandler::updateEventSource()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input12InputHandler17updateEventSourceEv',
    )

  @staticmethod
  def appendGenericDevice(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::InputHandler::appendGenericDevice(
    HGenericDeviceBackendNode device)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.appendGenericDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::appendGenericDevice(HGenericDeviceB"
        "ackendNode device)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def appendKeyboardDevice(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DInput::Input::InputHandler::appendKeyboardDevice(HKeyboardDevice
    device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.appendKeyboardDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::appendKeyboardDevice(HKeyboardDevic"
        "e device)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def appendMouseDevice(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::InputHandler::appendMouseDevice(HMouseDevice
    device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.appendMouseDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::appendMouseDevice(HMouseDevice "
        "device)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createPhysicalDevice(*__, **_) -> Never:
    """
    Qt's 'QAbstractPhysicalDevice
    *Qt3DInput::Input::InputHandler::createPhysicalDevice(const QString
    &name)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name
    'QAbstractPhysicalDevice'; did you mean
    'Qt3DInput::QAbstractPhysicalDevice'?.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.createPhysicalDevice' has no cute "
        "function yet. Qt's 'QAbstractPhysicalDevice "
        "*Qt3DInput::Input::InputHandler::createPhysicalDevice(const "
        "QString &name)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'QAbstractPhysicalDevice'; did you mean "
        "'Qt3DInput::QAbstractPhysicalDevice'?.")

  @staticmethod
  def inputDeviceIntegrations(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DInput::QInputDeviceIntegration *>
    Qt3DInput::Input::InputHandler::inputDeviceIntegrations() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.inputDeviceIntegrations' has no cute "
        "function yet. Qt's 'QList<Qt3DInput::QInputDeviceIntegration *> "
        "Qt3DInput::Input::InputHandler::inputDeviceIntegrations() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def registerEventFilters(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::InputHandler::registerEventFilters()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: cannot initialize a parameter of type 'QObject *'
    with an lvalue of type 'InternalEventFilter *'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.registerEventFilters' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::registerEventFilters()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: cannot initialize a parameter of type "
        "'QObject *' with an lvalue of type 'InternalEventFilter *'.")

  @staticmethod
  def removeGenericDevice(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::InputHandler::removeGenericDevice(
    HGenericDeviceBackendNode device)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.removeGenericDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::removeGenericDevice(HGenericDeviceB"
        "ackendNode device)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def removeKeyboardDevice(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DInput::Input::InputHandler::removeKeyboardDevice(HKeyboardDevice
    device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.removeKeyboardDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::removeKeyboardDevice(HKeyboardDevic"
        "e device)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def removeMouseDevice(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::InputHandler::removeMouseDevice(HMouseDevice
    device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.removeMouseDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::removeMouseDevice(HMouseDevice "
        "device)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def unregisterEventFilters(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::InputHandler::unregisterEventFilters()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: cannot initialize a parameter of type
    'QObject *' with an lvalue of type 'InternalEventFilter *'.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.InputHandler.unregisterEventFilters' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::InputHandler::unregisterEventFilters()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: cannot initialize a parameter of type "
        "'QObject *' with an lvalue of type 'InternalEventFilter *'.")
