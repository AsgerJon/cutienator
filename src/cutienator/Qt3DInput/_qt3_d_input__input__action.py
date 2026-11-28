"""
Qt3DInput::Input::Action binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/action_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DInput::Input::Action to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class Action(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::Input::Action: a plain Python object
  standing in front of one C++ Qt3DInput::Input::Action.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::Input::Action is built on Qt's Qt3DInput::Input::BackendNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::Input::Action that has a ritual and that
  Python can call so far, 4 names in all: 'cleanup', 'actionTriggered',
  'setActionTriggered', 'syncFromFrontEnd'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Qt3DCore::QNodeId> Qt3DInput::Input::Action::inputs() const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DInput::Input::Action is created at the first use, not by
    'Qt3DInput::Input::Action(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::Input::Action.
  - Each name of Qt's Qt3DInput::Input::Action that has no cute function yet,
    'inputs', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::Input::Action'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def actionTriggered(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::Input::Action::actionTriggered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-action.html#actionTriggered
    """
    #  bool Qt3DInput::Input::Action::actionTriggered() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput5Input6Action15actionTriggeredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActionTriggered(self, actionTriggered: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::Action::setActionTriggered(bool
    actionTriggered)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-action.html#setActionTriggered

    Parameters
    ----------

    actionTriggered : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::Action::setActionTriggered(bool
    #      actionTriggered)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput5Input6Action18setActionTriggeredEb',
        actionTriggered,
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
    Notes what was given, for Qt's 'Qt3DInput::Input::Action::Action()',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-input-action.html#Action
    """
    #  Qt3DInput::Input::Action::Action()
    self._noteCreation(Action, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput5Input6ActionC1Ev',
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
    Calls Qt's 'void Qt3DInput::Input::Action::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-action.html#cleanup
    """
    #  void Qt3DInput::Input::Action::cleanup()
    self.uglySide.call('ritual_ZN9Qt3DInput5Input6Action7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::Input::Action::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-input-action.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::Input::Action::syncFromFrontEnd(const Qt3DCore::QNode
    #      *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput5Input6Action16syncFromFrontEndEPKN8Qt3DCore5QN'
        'odeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput5Input6Action16syncFromFrontEndEPKN8Qt3DC'
          'ore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def inputs(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId> Qt3DInput::Input::Action::inputs() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.Input.Action.inputs' has no cute function yet. Qt's "
        "'QList<Qt3DCore::QNodeId> Qt3DInput::Input::Action::inputs() "
        "const': gives a type Python has no way to take yet.")
