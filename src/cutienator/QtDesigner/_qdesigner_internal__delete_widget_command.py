"""
qdesigner_internal::DeleteWidgetCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DeleteWidgetCommand to be private: it
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


class DeleteWidgetCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::DeleteWidgetCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::DeleteWidgetCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::DeleteWidgetCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DeleteWidgetCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'redo',
  'undo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::DeleteWidgetCommand::~DeleteWidgetCommand()':
    the destructor: Python never removes a C++
    qdesigner_internal::DeleteWidgetCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::DeleteWidgetCommand is created at the first
    use, not by 'qdesigner_internal::DeleteWidgetCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::DeleteWidgetCommand.
  """

  #  The enums Qt writes inside qdesigner_internal::DeleteWidgetCommand, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DeleteFlags(CuteNum):
    """
    The enum 'qdesigner_internal::DeleteWidgetCommand::DeleteFlags' of Qt,
    with the 2 names Qt gives in it.
    """

    DoNotUnmanage = Kee[int](1)
    DoNotSimplifyLayout = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DeleteWidgetCommand'

  #  A C++ qdesigner_internal::DeleteWidgetCommand Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_DeleteWidgetCommand'

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
    'qdesigner_internal::DeleteWidgetCommand::DeleteWidgetCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletewidgetcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::DeleteWidgetCommand::DeleteWidgetCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(DeleteWidgetCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19DeleteWidgetCommandC1EP28QDesignerF'
        'ormWindowInterface',
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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, int)
  @overload(NoneType, int)
  def init(self, widget: Optional[QWidget], flags: int = 0) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteWidgetCommand::init(QWidget
    *widget, unsigned int flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletewidgetcommand.html#init

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void qdesigner_internal::DeleteWidgetCommand::init(QWidget *widget,
    #      unsigned int flags)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19DeleteWidgetCommand4initEP7QWidgetj',
        self._addressOf(widget), flags,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteWidgetCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletewidgetcommand.html#redo
    """
    #  void qdesigner_internal::DeleteWidgetCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal19DeleteWidgetCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19DeleteWidgetCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DeleteWidgetCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-deletewidgetcommand.html#undo
    """
    #  void qdesigner_internal::DeleteWidgetCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal19DeleteWidgetCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19DeleteWidgetCommand4undoEv')
    self.uglySide.call(ritual)
