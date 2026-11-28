"""
qdesigner_internal::AddToolBarCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::AddToolBarCommand to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QMainWindow
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QMainWindow = WAIT['QMainWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AddToolBarCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::AddToolBarCommand: a plain Python
  object standing in front of one C++ qdesigner_internal::AddToolBarCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::AddToolBarCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::AddToolBarCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'undo',
  'redo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::AddToolBarCommand is created at the first
    use, not by 'qdesigner_internal::AddToolBarCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::AddToolBarCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::AddToolBarCommand'

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
    'qdesigner_internal::AddToolBarCommand::AddToolBarCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addtoolbarcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::AddToolBarCommand::AddToolBarCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(AddToolBarCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17AddToolBarCommandC1EP28QDesignerFor'
        'mWindowInterface',
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

  @overload(QMainWindow, Qt.ToolBarArea)
  @overload(NoneType, Qt.ToolBarArea)
  def init(
      self,
      mainWindow: Optional[QMainWindow],
      area: Qt.ToolBarArea,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AddToolBarCommand::init(QMainWindow
    *mainWindow, Qt::ToolBarArea area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addtoolbarcommand.html#init

    Parameters
    ----------

    mainWindow : Optional[QMainWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    area : Qt.ToolBarArea
      Passed on as its number.
    """
    #  void qdesigner_internal::AddToolBarCommand::init(QMainWindow
    #      *mainWindow, Qt::ToolBarArea area)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17AddToolBarCommand4initEP11QMainWind'
        'owN2Qt11ToolBarAreaE',
        self._addressOf(mainWindow), area.value,
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AddToolBarCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addtoolbarcommand.html#undo
    """
    #  void qdesigner_internal::AddToolBarCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal17AddToolBarCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal17AddToolBarCommand4undoEv'
    self.uglySide.call(ritual)

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AddToolBarCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addtoolbarcommand.html#redo
    """
    #  void qdesigner_internal::AddToolBarCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal17AddToolBarCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal17AddToolBarCommand4redoEv'
    self.uglySide.call(ritual)
