"""
Qt3DInput::Input::GenericDeviceBackendNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DInput::Input::GenericDeviceBackendNode to be private: it
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GenericDeviceBackendNode(Qt3DInput.QAbstractPhysicalDeviceBackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::GenericDeviceBackendNode: a plain
  Python object standing in front of one C++
  Qt3DInput::Input::GenericDeviceBackendNode.

  It is built on the cute 'Qt3DInput::QAbstractPhysicalDeviceBackendNode', as
  Qt's Qt3DInput::Input::GenericDeviceBackendNode is built on Qt's
  Qt3DInput::QAbstractPhysicalDeviceBackendNode, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::GenericDeviceBackendNode that has
  a ritual and that Python can call so far, 4 names in all:
  'syncFromFrontEnd', 'cleanup', 'axisValue', 'isButtonPressed'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DInput::Input::GenericDeviceBackendNode::~GenericDeviceBackendNode(
    )': the destructor: Python never removes a C++
    Qt3DInput::Input::GenericDeviceBackendNode.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::GenericDeviceBackendNode is created at the
    first use, not by 'Qt3DInput::Input::GenericDeviceBackendNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::GenericDeviceBackendNode.
  - Each name of Qt's Qt3DInput::Input::GenericDeviceBackendNode that has no
    cute function yet, 'updateEvents', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::GenericDeviceBackendNode'

  #  A C++ Qt3DInput::Input::GenericDeviceBackendNode Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_Input_GenericDeviceBackendNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def axisValue(self, axisIdentifier: int) -> float:
    """
    Calls Qt's 'float
    Qt3DInput::Input::GenericDeviceBackendNode::axisValue(int axisIdentifier)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendnode.html

    Parameters
    ----------

    axisIdentifier : int
      Passed on as it is.
    """
    #  float Qt3DInput::Input::GenericDeviceBackendNode::axisValue(int
    #      axisIdentifier) const
    ritual = (
        'ritual_ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisValueEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisVal'
          'ueEi')
    return self.uglySide.call(ritual, axisIdentifier)

  @overload(int)
  def isButtonPressed(self, buttonIdentifier: int) -> bool:
    """
    Calls Qt's 'bool
    Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(int
    buttonIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendnode.html

    Parameters
    ----------

    buttonIdentifier : int
      Passed on as it is.
    """
    #  bool Qt3DInput::Input::GenericDeviceBackendNode::isButtonPressed(int
    #      buttonIdentifier) const
    ritual = (
        'ritual_ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButtonPres'
        'sedEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButt'
          'onPressedEi')
    return self.uglySide.call(ritual, buttonIdentifier)

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
  @overload(Qt3DCore.QBackendNode.Mode)
  def __init__(
      self,
      mode: Qt3DCore.QBackendNode.Mode = (
          Qt3DCore.QBackendNode.Mode.ReadWrite),
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::Input::GenericDeviceBackendNode::GenericDeviceBackendNode(
    QBackendNode::Mode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendnode.html

    Parameters
    ----------

    mode : Qt3DCore.QBackendNode.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt3DCore.QBackendNode.Mode.ReadWrite.
    """
    #  Qt3DInput::Input::GenericDeviceBackendNode::
    #      GenericDeviceBackendNode(QBackendNode::Mode mode)
    self._noteCreation(GenericDeviceBackendNode, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNodeC1EN8Qt3DCore12'
        'QBackendNode4ModeE',
        mode.value,
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendnode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void
    #      Qt3DInput::Input::GenericDeviceBackendNode::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFromFront'
        'EndEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFro'
          'mFrontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::GenericDeviceBackendNode::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-genericdevicebackendnode.html
    """
    #  void Qt3DInput::Input::GenericDeviceBackendNode::cleanup()
    ritual = 'ritual_ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupE'
          'v')
    self.uglySide.call(ritual)

  @staticmethod
  def updateEvents(*__, **_) -> Never:
    """
    Qt's 'void Qt3DInput::Input::GenericDeviceBackendNode::updateEvents()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.GenericDeviceBackendNode.updateEvents' has no "
        "cute function yet. Qt's 'void "
        "Qt3DInput::Input::GenericDeviceBackendNode::updateEvents()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
