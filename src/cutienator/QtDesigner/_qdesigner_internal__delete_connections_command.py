"""
qdesigner_internal::DeleteConnectionsCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DeleteConnectionsCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DeleteConnectionsCommand(qdesigner_internal.CECommand):
  """
  The cute side of Qt's qdesigner_internal::DeleteConnectionsCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::DeleteConnectionsCommand.

  It is built on the cute 'qdesigner_internal::CECommand', as Qt's
  qdesigner_internal::DeleteConnectionsCommand is built on Qt's
  qdesigner_internal::CECommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DeleteConnectionsCommand that
  has a ritual and that Python can call so far, 2 names in all: 'redo',
  'undo'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::DeleteConnectionsCommand::DeleteConnectionsCommand(
    ConnectionEdit *edit, const ConnectionList &con_list)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::DeleteConnectionsCommand is created at the
    first use, not by 'qdesigner_internal::DeleteConnectionsCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::DeleteConnectionsCommand.
  - Each name of Qt's qdesigner_internal::DeleteConnectionsCommand that has
    no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::DeleteConnectionsCommand'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'qdesigner_internal::DeleteConnectionsCommand::DeleteConnectionsCommand(
    ConnectionEdit *edit, const ConnectionList &con_list)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DeleteConnectionsCommand.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::DeleteConnectionsCommand::DeleteConnectionsCom"
        "mand(ConnectionEdit *edit, const ConnectionList &con_list)': takes "
        "a type Python has no way to hand over yet.")

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
    Calls Qt's 'void qdesigner_internal::DeleteConnectionsCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deleteconnectionscommand.html
    """
    #  void qdesigner_internal::DeleteConnectionsCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal24DeleteConnectionsCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24DeleteConnectionsCommand4redo'
          'Ev')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteConnectionsCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deleteconnectionscommand.html
    """
    #  void qdesigner_internal::DeleteConnectionsCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal24DeleteConnectionsCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24DeleteConnectionsCommand4undo'
          'Ev')
    self.uglySide.call(ritual)
