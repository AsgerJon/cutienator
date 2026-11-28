"""
qdesigner_internal::MoveTabPageCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::MoveTabPageCommand to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QIcon
  from ..QtWidgets import QTabWidget, QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QIcon = WAIT['QIcon']
  QTabWidget = WAIT['QTabWidget']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MoveTabPageCommand(qdesigner_internal.TabWidgetCommand):
  """
  The cute side of Qt's qdesigner_internal::MoveTabPageCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::MoveTabPageCommand.

  It is built on the cute 'qdesigner_internal::TabWidgetCommand', as Qt's
  qdesigner_internal::MoveTabPageCommand is built on Qt's
  qdesigner_internal::TabWidgetCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::MoveTabPageCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'redo',
  'undo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::MoveTabPageCommand::~MoveTabPageCommand()': the
    destructor: Python never removes a C++
    qdesigner_internal::MoveTabPageCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::MoveTabPageCommand is created at the first
    use, not by 'qdesigner_internal::MoveTabPageCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::MoveTabPageCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::MoveTabPageCommand'

  #  A C++ qdesigner_internal::MoveTabPageCommand Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_MoveTabPageCommand'

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
    'qdesigner_internal::MoveTabPageCommand::MoveTabPageCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-movetabpagecommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::MoveTabPageCommand::MoveTabPageCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(MoveTabPageCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18MoveTabPageCommandC1EP28QDesignerFo'
        'rmWindowInterface',
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

  @overload(QTabWidget, QWidget, QIcon, str, int, int)
  @overload(QTabWidget, NoneType, QIcon, str, int, int)
  @overload(NoneType, QWidget, QIcon, str, int, int)
  @overload(NoneType, NoneType, QIcon, str, int, int)
  def init(
      self,
      tabWidget: Optional[QTabWidget],
      page: Optional[QWidget],
      icon: QIcon,
      label: str,
      index: int,
      newIndex: int,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MoveTabPageCommand::init(QTabWidget
    *tabWidget, QWidget *page, const QIcon &icon, const QString &label, int
    index, int newIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-movetabpagecommand.html#init

    Parameters
    ----------

    tabWidget : Optional[QTabWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    page : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    label : str
      Passed on as it is: a QString is made of it for the call.

    index : int
      Passed on as it is.

    newIndex : int
      Passed on as it is.
    """
    #  void qdesigner_internal::MoveTabPageCommand::init(QTabWidget
    #      *tabWidget, QWidget *page, const QIcon &icon, const QString
    #      &label, int index, int newIndex)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18MoveTabPageCommand4initEP10QTabWidg'
        'etP7QWidgetRK5QIconRK7QStringii',
        self._addressOf(tabWidget), self._addressOf(page),
        self._valueOf(icon), label, index, newIndex,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MoveTabPageCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-movetabpagecommand.html#redo
    """
    #  void qdesigner_internal::MoveTabPageCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal18MoveTabPageCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal18MoveTabPageCommand4redoEv'
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MoveTabPageCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-movetabpagecommand.html#undo
    """
    #  void qdesigner_internal::MoveTabPageCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal18MoveTabPageCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal18MoveTabPageCommand4undoEv'
    self.uglySide.call(ritual)
