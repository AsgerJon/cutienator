"""
qdesigner_internal::DeleteStatusBarCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DeleteStatusBarCommand to be private: it
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

  from ..QtWidgets import QStatusBar
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QStatusBar = WAIT['QStatusBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeleteStatusBarCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::DeleteStatusBarCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::DeleteStatusBarCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::DeleteStatusBarCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DeleteStatusBarCommand that has
  a ritual and that Python can call so far, 3 names in all: 'init', 'undo',
  'redo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::DeleteStatusBarCommand is created at the
    first use, not by 'qdesigner_internal::DeleteStatusBarCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::DeleteStatusBarCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DeleteStatusBarCommand'

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
    'qdesigner_internal::DeleteStatusBarCommand::DeleteStatusBarCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletestatusbarcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::DeleteStatusBarCommand::
    #      DeleteStatusBarCommand(QDesignerFormWindowInterface *formWindow)
    self._noteCreation(DeleteStatusBarCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22DeleteStatusBarCommandC1EP28QDesign'
        'erFormWindowInterface',
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

  @overload(QStatusBar)
  @overload(NoneType)
  def init(self, statusBar: Optional[QStatusBar]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::DeleteStatusBarCommand::init(QStatusBar *statusBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletestatusbarcommand.html

    Parameters
    ----------

    statusBar : Optional[QStatusBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::DeleteStatusBarCommand::init(QStatusBar
    #      *statusBar)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22DeleteStatusBarCommand4initEP10QSta'
        'tusBar',
        self._addressOf(statusBar),
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteStatusBarCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletestatusbarcommand.html
    """
    #  void qdesigner_internal::DeleteStatusBarCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal22DeleteStatusBarCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal22DeleteStatusBarCommand4undoEv')
    self.uglySide.call(ritual)

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteStatusBarCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletestatusbarcommand.html
    """
    #  void qdesigner_internal::DeleteStatusBarCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal22DeleteStatusBarCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal22DeleteStatusBarCommand4redoEv')
    self.uglySide.call(ritual)
