"""
qdesigner_internal::DeleteToolBoxPageCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DeleteToolBoxPageCommand to be private: it
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

  from ..QtWidgets import QToolBox
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QToolBox = WAIT['QToolBox']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeleteToolBoxPageCommand(qdesigner_internal.ToolBoxCommand):
  """
  The cute side of Qt's qdesigner_internal::DeleteToolBoxPageCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::DeleteToolBoxPageCommand.

  It is built on the cute 'qdesigner_internal::ToolBoxCommand', as Qt's
  qdesigner_internal::DeleteToolBoxPageCommand is built on Qt's
  qdesigner_internal::ToolBoxCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DeleteToolBoxPageCommand that
  has a ritual and that Python can call so far, 3 names in all: 'init',
  'redo', 'undo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::DeleteToolBoxPageCommand::~DeleteToolBoxPageCommand(
    )': the destructor: Python never removes a C++
    qdesigner_internal::DeleteToolBoxPageCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::DeleteToolBoxPageCommand is created at the
    first use, not by 'qdesigner_internal::DeleteToolBoxPageCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::DeleteToolBoxPageCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DeleteToolBoxPageCommand'

  #  A C++ qdesigner_internal::DeleteToolBoxPageCommand Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_DeleteToolBoxPageCommand'

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

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def __init__(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DeleteToolBoxPageCommand::DeleteToolBoxPageCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletetoolboxpagecommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::DeleteToolBoxPageCommand::
    #      DeleteToolBoxPageCommand(QDesignerFormWindowInterface *formWindow)
    self._noteCreation(DeleteToolBoxPageCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24DeleteToolBoxPageCommandC1EP28QDesi'
        'gnerFormWindowInterface',
        self._addressOf(formWindow),
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

  @overload(QToolBox)
  @overload(NoneType)
  def init(self, toolBox: Optional[QToolBox]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::DeleteToolBoxPageCommand::init(QToolBox *toolBox)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletetoolboxpagecommand.html

    Parameters
    ----------

    toolBox : Optional[QToolBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::DeleteToolBoxPageCommand::init(QToolBox
    #      *toolBox)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24DeleteToolBoxPageCommand4initEP8QTo'
        'olBox',
        self._addressOf(toolBox),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteToolBoxPageCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletetoolboxpagecommand.html
    """
    #  void qdesigner_internal::DeleteToolBoxPageCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal24DeleteToolBoxPageCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24DeleteToolBoxPageCommand4redo'
          'Ev')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteToolBoxPageCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletetoolboxpagecommand.html
    """
    #  void qdesigner_internal::DeleteToolBoxPageCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal24DeleteToolBoxPageCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24DeleteToolBoxPageCommand4undo'
          'Ev')
    self.uglySide.call(ritual)
