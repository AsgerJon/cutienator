"""
qdesigner_internal::CreateSubmenuCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::CreateSubmenuCommand to be private: it
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

  from ..QtCore import QObject
  from ..QtGui import QAction
  from . import QDesignerFormWindowInterface, QDesignerMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QDesignerMenu = WAIT['QDesignerMenu']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CreateSubmenuCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::CreateSubmenuCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::CreateSubmenuCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::CreateSubmenuCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::CreateSubmenuCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'redo',
  'undo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::CreateSubmenuCommand is created at the first
    use, not by 'qdesigner_internal::CreateSubmenuCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::CreateSubmenuCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::CreateSubmenuCommand'

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
    'qdesigner_internal::CreateSubmenuCommand::CreateSubmenuCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-createsubmenucommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::CreateSubmenuCommand::CreateSubmenuCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(CreateSubmenuCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20CreateSubmenuCommandC1EP28QDesigner'
        'FormWindowInterface',
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

  @overload(QDesignerMenu, QAction)
  @overload(QDesignerMenu, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  @overload(QDesignerMenu, QAction, QObject)
  @overload(QDesignerMenu, QAction, NoneType)
  @overload(QDesignerMenu, NoneType, QObject)
  @overload(QDesignerMenu, NoneType, NoneType)
  @overload(NoneType, QAction, QObject)
  @overload(NoneType, QAction, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def init(
      self,
      menu: Optional[QDesignerMenu],
      action: Optional[QAction],
      m_objectToSelect: Optional[QObject] = None,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::CreateSubmenuCommand::init(QDesignerMenu *menu,
    QAction *action, QObject *m_objectToSelect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-createsubmenucommand.html#init

    Parameters
    ----------

    menu : Optional[QDesignerMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m_objectToSelect : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void qdesigner_internal::CreateSubmenuCommand::init(QDesignerMenu
    #      *menu, QAction *action, QObject *m_objectToSelect)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20CreateSubmenuCommand4initEP13QDesig'
        'nerMenuP7QActionP7QObject',
        self._addressOf(menu), self._addressOf(action),
        self._addressOf(m_objectToSelect, 'QObject'),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CreateSubmenuCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-createsubmenucommand.html#redo
    """
    #  void qdesigner_internal::CreateSubmenuCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal20CreateSubmenuCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20CreateSubmenuCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CreateSubmenuCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-createsubmenucommand.html#undo
    """
    #  void qdesigner_internal::CreateSubmenuCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal20CreateSubmenuCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20CreateSubmenuCommand4undoEv')
    self.uglySide.call(ritual)
