"""
Qt3DInput::Input::PhysicalDeviceProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/physicaldeviceproxy_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DInput::Input::PhysicalDeviceProxy to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PhysicalDeviceProxy(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::PhysicalDeviceProxy: a plain Python
  object standing in front of one C++ Qt3DInput::Input::PhysicalDeviceProxy.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::PhysicalDeviceProxy is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::PhysicalDeviceProxy that has a
  ritual and that Python can call so far, 7 names in all: 'cleanup',
  'deviceName', 'setManager', 'manager', 'setDevice', 'physicalDeviceId',
  'syncFromFrontEnd'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::PhysicalDeviceProxy is created at the first
    use, not by 'Qt3DInput::Input::PhysicalDeviceProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::PhysicalDeviceProxy.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::PhysicalDeviceProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def deviceName(self) -> str:
    """
    Calls Qt's 'QString Qt3DInput::Input::PhysicalDeviceProxy::deviceName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DInput::Input::PhysicalDeviceProxy::deviceName() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input19PhysicalDeviceProxy10deviceNameEv',
    )

  def manager(self) -> Optional[Qt3DInput.Input.PhysicalDeviceProxyManager]:
    """
    Calls Qt's 'PhysicalDeviceProxyManager
    *Qt3DInput::Input::PhysicalDeviceProxy::manager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html#manager

    Returns
    -------

    Optional[Qt3DInput.Input.PhysicalDeviceProxyManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PhysicalDeviceProxyManager
    #      *Qt3DInput::Input::PhysicalDeviceProxy::manager() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input19PhysicalDeviceProxy7managerEv',
    )
    return Qt3DInput.Input.PhysicalDeviceProxyManager._cuteAt(address)

  def physicalDeviceId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DInput::Input::PhysicalDeviceProxy::physicalDeviceId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DInput::Input::PhysicalDeviceProxy::physicalDeviceId() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input19PhysicalDeviceProxy16physicalDeviceIdE'
        'v',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.Input.PhysicalDeviceProxyManager'])
  @overload(NoneType)
  def setManager(
      self,
      manager: Optional[Qt3DInput.Input.PhysicalDeviceProxyManager],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::PhysicalDeviceProxy::setManager(
    PhysicalDeviceProxyManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html

    Parameters
    ----------

    manager : Optional[Qt3DInput.Input.PhysicalDeviceProxyManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::PhysicalDeviceProxy::setManager(
    #      PhysicalDeviceProxyManager *manager)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy10setManagerEPNS0_26'
        'PhysicalDeviceProxyManagerE',
        self._addressOf(manager),
    )

  @overload(WAIT['Qt3DInput.QAbstractPhysicalDevice'])
  @overload(NoneType)
  def setDevice(
      self,
      device: Optional[Qt3DInput.QAbstractPhysicalDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::PhysicalDeviceProxy::setDevice(QAbstractPhysicalDevice
    *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html#setDevice

    Parameters
    ----------

    device : Optional[Qt3DInput.QAbstractPhysicalDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::Input::PhysicalDeviceProxy::setDevice(
    #      QAbstractPhysicalDevice *device)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy9setDeviceEPNS_23QAb'
        'stractPhysicalDeviceE',
        self._addressOf(device),
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
    'Qt3DInput::Input::PhysicalDeviceProxy::PhysicalDeviceProxy()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html
    """
    #  Qt3DInput::Input::PhysicalDeviceProxy::PhysicalDeviceProxy()
    self._noteCreation(PhysicalDeviceProxy, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxyC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::PhysicalDeviceProxy::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html#cleanup
    """
    #  void Qt3DInput::Input::PhysicalDeviceProxy::cleanup()
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::PhysicalDeviceProxy::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-physicaldeviceproxy.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::PhysicalDeviceProxy::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy16syncFromFrontEndEP'
        'KN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input19PhysicalDeviceProxy16syncFromFron'
          'tEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
