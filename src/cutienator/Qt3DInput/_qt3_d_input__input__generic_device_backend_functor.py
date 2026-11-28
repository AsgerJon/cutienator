"""
Qt3DInput::Input::GenericDeviceBackendFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DInput::Input::GenericDeviceBackendFunctor to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
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


class GenericDeviceBackendFunctor(Qt3DCore.QBackendNodeMapper):
  """
  The cute side of Qt's Qt3DInput::Input::GenericDeviceBackendFunctor: a
  plain Python object standing in front of one C++
  Qt3DInput::Input::GenericDeviceBackendFunctor.

  It is built on the cute 'Qt3DCore::QBackendNodeMapper', as Qt's
  Qt3DInput::Input::GenericDeviceBackendFunctor is built on Qt's
  Qt3DCore::QBackendNodeMapper, and has everything that class has.

  C++ hands a Qt3DInput::Input::GenericDeviceBackendFunctor around as a copy,
  so every C++ Qt3DInput::Input::GenericDeviceBackendFunctor behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::GenericDeviceBackendFunctor that
  has a ritual and that Python can call so far, 3 names in all: 'create',
  'get', 'destroy'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::Input::GenericDeviceBackendFunctor::
    ~GenericDeviceBackendFunctor()': the destructor: Python removes its C++
    Qt3DInput::Input::GenericDeviceBackendFunctor by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::GenericDeviceBackendFunctor is created at the
    first use, not by 'Qt3DInput::Input::GenericDeviceBackendFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DInput::Input::GenericDeviceBackendFunctor back
    gives a copy the ritual made for Python, in a new cute
    Qt3DInput::Input::GenericDeviceBackendFunctor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::GenericDeviceBackendFunctor'

  #  Qt's '~Qt3DInput::Input::GenericDeviceBackendFunctor()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DInput::Input::GenericDeviceBackendFunctor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN9Qt3DInput5Input27GenericDeviceBackendFunctorD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def create(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'Qt3DCore::QBackendNode
    *Qt3DInput::Input::GenericDeviceBackendFunctor::create(Qt3DCore::QNodeId
    id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendfunctor.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QBackendNode
    #      *Qt3DInput::Input::GenericDeviceBackendFunctor::create(Qt3DCore::
    #      QNodeId id) const
    ritual = (
        'ritual_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor6createEN8Q'
        't3DCore7QNodeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor6crea'
          'teEN8Qt3DCore7QNodeIdE')
    address = self.uglySide.call(ritual, self._valueOf(id))
    return Qt3DCore.QBackendNode._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def get(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'Qt3DCore::QBackendNode
    *Qt3DInput::Input::GenericDeviceBackendFunctor::get(Qt3DCore::QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendfunctor.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QBackendNode
    #      *Qt3DInput::Input::GenericDeviceBackendFunctor::get(Qt3DCore::
    #      QNodeId id) const
    ritual = (
        'ritual_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor3getEN8Qt3D'
        'Core7QNodeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor3getE'
          'N8Qt3DCore7QNodeIdE')
    address = self.uglySide.call(ritual, self._valueOf(id))
    return Qt3DCore.QBackendNode._cuteAt(address)

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

  @overload(
      WAIT['Qt3DInput.QInputAspect'], WAIT['Qt3DInput.Input.InputHandler'],
  )
  @overload(WAIT['Qt3DInput.QInputAspect'], NoneType)
  @overload(NoneType, WAIT['Qt3DInput.Input.InputHandler'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      inputaspect: Optional[Qt3DInput.QInputAspect],
      handler: Optional[Qt3DInput.Input.InputHandler],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::Input::GenericDeviceBackendFunctor::
    GenericDeviceBackendFunctor(QInputAspect *inputaspect, InputHandler
    *handler)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendfunctor.html

    Parameters
    ----------

    inputaspect : Optional[Qt3DInput.QInputAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    handler : Optional[Qt3DInput.Input.InputHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DInput::Input::GenericDeviceBackendFunctor::
    #      GenericDeviceBackendFunctor(QInputAspect *inputaspect,
    #      InputHandler *handler)
    self._noteCreation(GenericDeviceBackendFunctor, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input27GenericDeviceBackendFunctorC1EPNS_12QIn'
        'putAspectEPNS0_12InputHandlerE',
        self._addressOf(inputaspect), self._addressOf(handler),
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
  def destroy(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::GenericDeviceBackendFunctor::destroy(Qt3DCore::QNodeId
    id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendfunctor.html

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DInput::Input::GenericDeviceBackendFunctor::destroy(Qt3DCore::
    #      QNodeId id) const
    ritual = (
        'ritual_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor7destroyEN8'
        'Qt3DCore7QNodeIdE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor7dest'
          'royEN8Qt3DCore7QNodeIdE')
    self.uglySide.call(ritual, self._valueOf(id))
