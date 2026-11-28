"""
qdesigner_internal::InsertActionIntoCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::InsertActionIntoCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class InsertActionIntoCommand(qdesigner_internal.ActionInsertionCommand):
  """
  The cute side of Qt's qdesigner_internal::InsertActionIntoCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::InsertActionIntoCommand.

  It is built on the cute 'qdesigner_internal::ActionInsertionCommand', as
  Qt's qdesigner_internal::InsertActionIntoCommand is built on Qt's
  qdesigner_internal::ActionInsertionCommand, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::InsertActionIntoCommand that has
  a ritual and that Python can call so far, 2 names in all: 'redo', 'undo'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on 'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::InsertActionIntoCommand is created at the
    first use, not by 'qdesigner_internal::InsertActionIntoCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::InsertActionIntoCommand.
  - Each name of Qt's qdesigner_internal::InsertActionIntoCommand that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::InsertActionIntoCommand'

  #  A C++ qdesigner_internal::InsertActionIntoCommand Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_InsertActionIntoCommand'

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
    'qdesigner_internal::InsertActionIntoCommand::InsertActionIntoCommand(
    QDesignerFormWindowInterface *formWindow)': leans on
    'qdesigner_internal::ActionInsertionCommand::insertAction()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.InsertActionIntoCommand.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::InsertActionIntoCommand::InsertActionIntoComma"
        "nd(QDesignerFormWindowInterface *formWindow)': leans on "
        "'qdesigner_internal::ActionInsertionCommand::insertAction()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void qdesigner_internal::InsertActionIntoCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertactionintocommand.html
    """
    #  void qdesigner_internal::InsertActionIntoCommand::redo()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23InsertActionIntoCommand4redoEv',
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::InsertActionIntoCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertactionintocommand.html
    """
    #  void qdesigner_internal::InsertActionIntoCommand::undo()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23InsertActionIntoCommand4undoEv',
    )
