"""
qdesigner_internal::PromoteToCustomWidgetCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PromoteToCustomWidgetCommand to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PromoteToCustomWidgetCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::PromoteToCustomWidgetCommand: a
  plain Python object standing in front of one C++
  qdesigner_internal::PromoteToCustomWidgetCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::PromoteToCustomWidgetCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PromoteToCustomWidgetCommand
  that has a ritual and that Python can call so far, 3 names in all: 'redo',
  'undo', 'updateSelection'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void qdesigner_internal::PromoteToCustomWidgetCommand::init(const
    WidgetPointerList &widgets, const QString &customClassName)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::PromoteToCustomWidgetCommand is created at
    the first use, not by
    'qdesigner_internal::PromoteToCustomWidgetCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::PromoteToCustomWidgetCommand.
  - Each name of Qt's qdesigner_internal::PromoteToCustomWidgetCommand that
    has no cute function yet, 'init', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::PromoteToCustomWidgetCommand'

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
    'qdesigner_internal::PromoteToCustomWidgetCommand::
    PromoteToCustomWidgetCommand(QDesignerFormWindowInterface *formWindow)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotetocustomwidgetcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::PromoteToCustomWidgetCommand::
    #      PromoteToCustomWidgetCommand(QDesignerFormWindowInterface
    #      *formWindow)
    self._noteCreation(PromoteToCustomWidgetCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommandC1EP28Q'
        'DesignerFormWindowInterface',
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

  def redo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromoteToCustomWidgetCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotetocustomwidgetcommand.html
    """
    #  void qdesigner_internal::PromoteToCustomWidgetCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4redoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4'
          'redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromoteToCustomWidgetCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotetocustomwidgetcommand.html
    """
    #  void qdesigner_internal::PromoteToCustomWidgetCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4undoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal28PromoteToCustomWidgetCommand4'
          'undoEv')
    self.uglySide.call(ritual)

  def updateSelection(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromoteToCustomWidgetCommand::updateSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotetocustomwidgetcommand.html
    """
    #  void
    #      qdesigner_internal::PromoteToCustomWidgetCommand::updateSelection(
    #      )
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal28PromoteToCustomWidgetCommand15updat'
        'eSelectionEv',
    )

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::PromoteToCustomWidgetCommand::init(const
    WidgetPointerList &widgets, const QString &customClassName)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromoteToCustomWidgetCommand.init' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::PromoteToCustomWidgetCommand::init(const "
        "WidgetPointerList &widgets, const QString &customClassName)': "
        "takes a type Python has no way to hand over yet.")
