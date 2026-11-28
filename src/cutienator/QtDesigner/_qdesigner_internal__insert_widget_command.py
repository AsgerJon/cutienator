"""
qdesigner_internal::InsertWidgetCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::InsertWidgetCommand to be private: it
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


class InsertWidgetCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::InsertWidgetCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::InsertWidgetCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::InsertWidgetCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::InsertWidgetCommand that has a
  ritual and that Python can call so far, 4 names in all: 'init', 'redo',
  'undo', 'refreshBuddyLabels'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::InsertWidgetCommand::~InsertWidgetCommand()':
    the destructor: Python never removes a C++
    qdesigner_internal::InsertWidgetCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::InsertWidgetCommand is created at the first
    use, not by 'qdesigner_internal::InsertWidgetCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::InsertWidgetCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::InsertWidgetCommand'

  #  A C++ qdesigner_internal::InsertWidgetCommand Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_InsertWidgetCommand'

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
    'qdesigner_internal::InsertWidgetCommand::InsertWidgetCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertwidgetcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::InsertWidgetCommand::InsertWidgetCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(InsertWidgetCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19InsertWidgetCommandC1EP28QDesignerF'
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
  @overload(QWidget, bool)
  @overload(NoneType, bool)
  @overload(QWidget, bool, int)
  @overload(NoneType, bool, int)
  @overload(QWidget, bool, int, int)
  @overload(NoneType, bool, int, int)
  def init(
      self,
      widget: Optional[QWidget],
      already_in_form: bool = False,
      layoutRow: int = -1,
      layoutColumn: int = -1,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::InsertWidgetCommand::init(QWidget
    *widget, bool already_in_form, int layoutRow, int layoutColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertwidgetcommand.html#init

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    already_in_form : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    layoutRow : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    layoutColumn : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void qdesigner_internal::InsertWidgetCommand::init(QWidget *widget,
    #      bool already_in_form, int layoutRow, int layoutColumn)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19InsertWidgetCommand4initEP7QWidgetb'
        'ii',
        self._addressOf(widget), already_in_form, layoutRow, layoutColumn,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::InsertWidgetCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertwidgetcommand.html#redo
    """
    #  void qdesigner_internal::InsertWidgetCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal19InsertWidgetCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19InsertWidgetCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::InsertWidgetCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertwidgetcommand.html#undo
    """
    #  void qdesigner_internal::InsertWidgetCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal19InsertWidgetCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19InsertWidgetCommand4undoEv')
    self.uglySide.call(ritual)

  def refreshBuddyLabels(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::InsertWidgetCommand::refreshBuddyLabels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-insertwidgetcommand.html
    """
    #  void qdesigner_internal::InsertWidgetCommand::refreshBuddyLabels()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19InsertWidgetCommand18refreshBuddyLa'
        'belsEv',
    )
