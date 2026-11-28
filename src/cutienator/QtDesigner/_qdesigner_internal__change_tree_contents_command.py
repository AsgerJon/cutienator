"""
qdesigner_internal::ChangeTreeContentsCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeTreeContentsCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QTreeWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QTreeWidget = WAIT['QTreeWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeTreeContentsCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeTreeContentsCommand: a
  plain Python object standing in front of one C++
  qdesigner_internal::ChangeTreeContentsCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeTreeContentsCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeTreeContentsCommand that
  has a ritual and that Python can call so far, 3 names in all: 'init',
  'redo', 'undo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeTreeContentsCommand is created at the
    first use, not by 'qdesigner_internal::ChangeTreeContentsCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ChangeTreeContentsCommand.
  """

  #  The enums Qt writes inside
  #  qdesigner_internal::ChangeTreeContentsCommand, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ApplyIconStrategy(CuteNum):
    """
    The enum
    'qdesigner_internal::ChangeTreeContentsCommand::ApplyIconStrategy' of Qt,
    with the 2 names Qt gives in it.
    """

    SetIconStrategy = Kee[int](0)
    ResetIconStrategy = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ChangeTreeContentsCommand'

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
    'qdesigner_internal::ChangeTreeContentsCommand::
    ChangeTreeContentsCommand(QDesignerFormWindowInterface *formWindow)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetreecontentscommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ChangeTreeContentsCommand::
    #      ChangeTreeContentsCommand(QDesignerFormWindowInterface
    #      *formWindow)
    self._noteCreation(ChangeTreeContentsCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal25ChangeTreeContentsCommandC1EP28QDes'
        'ignerFormWindowInterface',
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

  @overload(
      QTreeWidget, WAIT['qdesigner_internal.TreeWidgetContents'],
      WAIT['qdesigner_internal.TreeWidgetContents'],
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.TreeWidgetContents'],
      WAIT['qdesigner_internal.TreeWidgetContents'],
  )
  def init(
      self,
      treeWidget: Optional[QTreeWidget],
      oldState: qdesigner_internal.TreeWidgetContents,
      newState: qdesigner_internal.TreeWidgetContents,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeTreeContentsCommand::init(QTreeWidget
    *treeWidget, const TreeWidgetContents &oldState, const TreeWidgetContents
    &newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetreecontentscommand.html

    Parameters
    ----------

    treeWidget : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldState : qdesigner_internal.TreeWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TreeWidgetContents, which stays Python's own.

    newState : qdesigner_internal.TreeWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TreeWidgetContents, which stays Python's own.
    """
    #  void qdesigner_internal::ChangeTreeContentsCommand::init(QTreeWidget
    #      *treeWidget, const TreeWidgetContents &oldState, const
    #      TreeWidgetContents &newState)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ChangeTreeContentsCommand4initEP11Q'
        'TreeWidgetRKNS_18TreeWidgetContentsES5_',
        self._addressOf(treeWidget), self._valueOf(oldState),
        self._valueOf(newState),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeTreeContentsCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetreecontentscommand.html
    """
    #  void qdesigner_internal::ChangeTreeContentsCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal25ChangeTreeContentsCommand4redoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal25ChangeTreeContentsCommand4red'
          'oEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeTreeContentsCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetreecontentscommand.html
    """
    #  void qdesigner_internal::ChangeTreeContentsCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal25ChangeTreeContentsCommand4undoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal25ChangeTreeContentsCommand4und'
          'oEv')
    self.uglySide.call(ritual)
