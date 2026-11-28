"""
qdesigner_internal::AddContainerWidgetPageCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::AddContainerWidgetPageCommand to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AddContainerWidgetPageCommand(qdesigner_internal.ContainerWidgetCommand):
  """
  The cute side of Qt's qdesigner_internal::AddContainerWidgetPageCommand: a
  plain Python object standing in front of one C++
  qdesigner_internal::AddContainerWidgetPageCommand.

  It is built on the cute 'qdesigner_internal::ContainerWidgetCommand', as
  Qt's qdesigner_internal::AddContainerWidgetPageCommand is built on Qt's
  qdesigner_internal::ContainerWidgetCommand, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::AddContainerWidgetPageCommand
  that has a ritual and that Python can call so far, 3 names in all: 'init',
  'redo', 'undo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::AddContainerWidgetPageCommand::
    ~AddContainerWidgetPageCommand()': the destructor: Python never removes a
    C++ qdesigner_internal::AddContainerWidgetPageCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::AddContainerWidgetPageCommand is created at
    the first use, not by
    'qdesigner_internal::AddContainerWidgetPageCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::AddContainerWidgetPageCommand.
  """

  #  The enums Qt writes inside
  #  qdesigner_internal::AddContainerWidgetPageCommand, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class InsertionMode(CuteNum):
    """
    The enum
    'qdesigner_internal::AddContainerWidgetPageCommand::InsertionMode' of Qt,
    with the 2 names Qt gives in it.
    """

    InsertBefore = Kee[int](0)
    InsertAfter = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::AddContainerWidgetPageCommand'

  #  A C++ qdesigner_internal::AddContainerWidgetPageCommand Python makes is
  #  of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_AddContainerWidgetPageCommand'

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
    'qdesigner_internal::AddContainerWidgetPageCommand::
    AddContainerWidgetPageCommand(QDesignerFormWindowInterface *formWindow)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addcontainerwidgetpagecommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::AddContainerWidgetPageCommand::
    #      AddContainerWidgetPageCommand(QDesignerFormWindowInterface
    #      *formWindow)
    self._noteCreation(AddContainerWidgetPageCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal29AddContainerWidgetPageCommandC1EP28'
        'QDesignerFormWindowInterface',
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

  @overload(QWidget, qdesigner_internal.ContainerType, InsertionMode)
  @overload(NoneType, qdesigner_internal.ContainerType, InsertionMode)
  def init(
      self,
      containerWidget: Optional[QWidget],
      ct: qdesigner_internal.ContainerType,
      mode: InsertionMode,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::AddContainerWidgetPageCommand::init(QWidget
    *containerWidget, ContainerType ct, InsertionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addcontainerwidgetpagecommand.html

    Parameters
    ----------

    containerWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ct : qdesigner_internal.ContainerType
      Passed on as its number.

    mode : InsertionMode
      Passed on as its number.
    """
    #  void qdesigner_internal::AddContainerWidgetPageCommand::init(QWidget
    #      *containerWidget, ContainerType ct, InsertionMode mode)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal29AddContainerWidgetPageCommand4initE'
        'P7QWidgetNS_13ContainerTypeENS0_13InsertionModeE',
        self._addressOf(containerWidget), ct.value, mode.value,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::AddContainerWidgetPageCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addcontainerwidgetpagecommand.html
    """
    #  void qdesigner_internal::AddContainerWidgetPageCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal29AddContainerWidgetPageCommand4redoE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal29AddContainerWidgetPageCommand'
          '4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::AddContainerWidgetPageCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-addcontainerwidgetpagecommand.html
    """
    #  void qdesigner_internal::AddContainerWidgetPageCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal29AddContainerWidgetPageCommand4undoE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal29AddContainerWidgetPageCommand'
          '4undoEv')
    self.uglySide.call(ritual)
