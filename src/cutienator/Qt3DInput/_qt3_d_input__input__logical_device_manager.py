"""
Qt3DInput::Input::LogicalDeviceManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/inputmanagers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::LogicalDeviceManager to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class LogicalDeviceManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DInput::Input::LogicalDeviceManager: a plain
  Python object standing in front of one C++
  Qt3DInput::Input::LogicalDeviceManager.

  What exists
  -----------

  No function of Qt's Qt3DInput::Input::LogicalDeviceManager yet. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<HLogicalDevice>
    Qt3DInput::Input::LogicalDeviceManager::activeDevices() const': gives a
    type Python has no way to take yet.
  - Qt's 'void
    Qt3DInput::Input::LogicalDeviceManager::addActiveDevice(HLogicalDevice
    device)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DInput::Input::LogicalDeviceManager::removeActiveDevice(HLogicalDevice
    device)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::LogicalDeviceManager is created at the first
    use, not by 'Qt3DInput::Input::LogicalDeviceManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::LogicalDeviceManager.
  - Each name of Qt's Qt3DInput::Input::LogicalDeviceManager that has no cute
    function yet, 'activeDevices', 'addActiveDevice', 'removeActiveDevice',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::LogicalDeviceManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::Input::LogicalDeviceManager::LogicalDeviceManager()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-logicaldevicemanager.html
    """
    #  Qt3DInput::Input::LogicalDeviceManager::LogicalDeviceManager()
    self._noteCreation(LogicalDeviceManager, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input20LogicalDeviceManagerC1Ev',
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

  @staticmethod
  def activeDevices(*__, **_) -> Never:
    """
    Qt's 'QList<HLogicalDevice>
    Qt3DInput::Input::LogicalDeviceManager::activeDevices() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.LogicalDeviceManager.activeDevices' has no cute "
        "function yet. Qt's 'QList<HLogicalDevice> "
        "Qt3DInput::Input::LogicalDeviceManager::activeDevices() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def addActiveDevice(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DInput::Input::LogicalDeviceManager::addActiveDevice(HLogicalDevice
    device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.LogicalDeviceManager.addActiveDevice' has no cute "
        "function yet. Qt's 'void "
        "Qt3DInput::Input::LogicalDeviceManager::addActiveDevice(HLogicalDev"
        "ice device)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def removeActiveDevice(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DInput::Input::LogicalDeviceManager::removeActiveDevice(HLogicalDevice
    device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.LogicalDeviceManager.removeActiveDevice' has no "
        "cute function yet. Qt's 'void "
        "Qt3DInput::Input::LogicalDeviceManager::removeActiveDevice(HLogical"
        "Device device)': takes a type Python has no way to hand over yet.")
