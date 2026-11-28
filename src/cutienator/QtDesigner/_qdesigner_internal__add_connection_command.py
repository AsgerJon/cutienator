"""
qdesigner_internal::AddConnectionCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::AddConnectionCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AddConnectionCommand(qdesigner_internal.CECommand):
  """
  The cute side of Qt's qdesigner_internal::AddConnectionCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::AddConnectionCommand.

  It is built on the cute 'qdesigner_internal::CECommand', as Qt's
  qdesigner_internal::AddConnectionCommand is built on Qt's
  qdesigner_internal::CECommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::AddConnectionCommand that has a
  ritual and that Python can call so far, 2 names in all: 'redo', 'undo'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::AddConnectionCommand is created at the first
    use, not by 'qdesigner_internal::AddConnectionCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::AddConnectionCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::AddConnectionCommand'

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

  @overload(
      WAIT['qdesigner_internal.ConnectionEdit'],
      WAIT['qdesigner_internal.Connection'],
  )
  @overload(WAIT['qdesigner_internal.ConnectionEdit'], NoneType)
  @overload(NoneType, WAIT['qdesigner_internal.Connection'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      edit: Optional[qdesigner_internal.ConnectionEdit],
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::AddConnectionCommand::AddConnectionCommand(
    ConnectionEdit *edit, Connection *con)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addconnectioncommand.html

    Parameters
    ----------

    edit : Optional[qdesigner_internal.ConnectionEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::AddConnectionCommand::AddConnectionCommand(
    #      ConnectionEdit *edit, Connection *con)
    self._noteCreation(AddConnectionCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20AddConnectionCommandC1EPNS_14Connec'
        'tionEditEPNS_10ConnectionE',
        self._addressOf(edit), self._addressOf(con),
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

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AddConnectionCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addconnectioncommand.html#redo
    """
    #  void qdesigner_internal::AddConnectionCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal20AddConnectionCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20AddConnectionCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AddConnectionCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addconnectioncommand.html#undo
    """
    #  void qdesigner_internal::AddConnectionCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal20AddConnectionCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20AddConnectionCommand4undoEv')
    self.uglySide.call(ritual)
