"""
Qt3DInput::Input::PhysicalDeviceProxyManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/inputmanagers_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DInput::Input::PhysicalDeviceProxyManager to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class PhysicalDeviceProxyManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DInput::Input::PhysicalDeviceProxyManager: a plain
  Python object standing in front of one C++
  Qt3DInput::Input::PhysicalDeviceProxyManager.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::PhysicalDeviceProxyManager that
  has a ritual and that Python can call so far, 1 name in all:
  'addPendingProxyToLoad'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::PhysicalDeviceProxyManager::takePendingProxiesToLoad(
    )': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::PhysicalDeviceProxyManager is created at the
    first use, not by 'Qt3DInput::Input::PhysicalDeviceProxyManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DInput::Input::PhysicalDeviceProxyManager.
  - Each name of Qt's Qt3DInput::Input::PhysicalDeviceProxyManager that has
    no cute function yet, 'takePendingProxiesToLoad', holds a function that
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
  __qt_class__ = 'Qt3DInput::Input::PhysicalDeviceProxyManager'

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
    'Qt3DInput::Input::PhysicalDeviceProxyManager::
    PhysicalDeviceProxyManager()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxymanager.html
    """
    #  Qt3DInput::Input::PhysicalDeviceProxyManager::
    #      PhysicalDeviceProxyManager()
    self._noteCreation(PhysicalDeviceProxyManager, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input26PhysicalDeviceProxyManagerC1Ev',
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

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addPendingProxyToLoad(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::PhysicalDeviceProxyManager::addPendingProxyToLoad(
    Qt3DCore::QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxymanager.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DInput::Input::PhysicalDeviceProxyManager::
    #      addPendingProxyToLoad(Qt3DCore::QNodeId id)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input26PhysicalDeviceProxyManager21addPendingP'
        'roxyToLoadEN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
    )

  @staticmethod
  def takePendingProxiesToLoad(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DInput::Input::PhysicalDeviceProxyManager::takePendingProxiesToLoad(
    )': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.PhysicalDeviceProxyManager.takePendingProxiesToLoa"
        "d' has no cute function yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DInput::Input::PhysicalDeviceProxyManager::takePendingProxiesToL"
        "oad()': gives a type Python has no way to take yet.")
