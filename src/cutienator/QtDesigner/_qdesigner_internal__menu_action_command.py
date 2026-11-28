"""
qdesigner_internal::MenuActionCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::MenuActionCommand to be private: it declares
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

  from ..QtGui import QAction
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MenuActionCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::MenuActionCommand: a plain Python
  object standing in front of one C++ qdesigner_internal::MenuActionCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::MenuActionCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::MenuActionCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init',
  'insertMenu', 'removeMenu'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::MenuActionCommand is created at the first
    use, not by 'qdesigner_internal::MenuActionCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::MenuActionCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::MenuActionCommand'

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

  @overload(str, QDesignerFormWindowInterface)
  @overload(str, NoneType)
  def __init__(
      self,
      text: str,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::MenuActionCommand::MenuActionCommand(const QString
    &text, QDesignerFormWindowInterface *formWindow)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-menuactioncommand.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::MenuActionCommand::MenuActionCommand(const QString
    #      &text, QDesignerFormWindowInterface *formWindow)
    self._noteCreation(MenuActionCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17MenuActionCommandC1ERK7QStringP28QD'
        'esignerFormWindowInterface',
        text, self._addressOf(formWindow),
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

  @overload(QAction, QAction, QWidget, QWidget)
  @overload(QAction, QAction, QWidget, NoneType)
  @overload(QAction, QAction, NoneType, QWidget)
  @overload(QAction, QAction, NoneType, NoneType)
  @overload(QAction, NoneType, QWidget, QWidget)
  @overload(QAction, NoneType, QWidget, NoneType)
  @overload(QAction, NoneType, NoneType, QWidget)
  @overload(QAction, NoneType, NoneType, NoneType)
  @overload(NoneType, QAction, QWidget, QWidget)
  @overload(NoneType, QAction, QWidget, NoneType)
  @overload(NoneType, QAction, NoneType, QWidget)
  @overload(NoneType, QAction, NoneType, NoneType)
  @overload(NoneType, NoneType, QWidget, QWidget)
  @overload(NoneType, NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType, NoneType)
  def init(
      self,
      action: Optional[QAction],
      actionBefore: Optional[QAction],
      associatedWidget: Optional[QWidget],
      objectToSelect: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MenuActionCommand::init(QAction
    *action, QAction *actionBefore, QWidget *associatedWidget, QWidget
    *objectToSelect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-menuactioncommand.html#init

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    actionBefore : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    associatedWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectToSelect : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::MenuActionCommand::init(QAction *action,
    #      QAction *actionBefore, QWidget *associatedWidget, QWidget
    #      *objectToSelect)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17MenuActionCommand4initEP7QActionS2_'
        'P7QWidgetS4_',
        self._addressOf(action), self._addressOf(actionBefore),
        self._addressOf(associatedWidget), self._addressOf(objectToSelect),
    )

  def insertMenu(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MenuActionCommand::insertMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-menuactioncommand.html
    """
    #  void qdesigner_internal::MenuActionCommand::insertMenu()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17MenuActionCommand10insertMenuEv',
    )

  def removeMenu(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MenuActionCommand::removeMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-menuactioncommand.html
    """
    #  void qdesigner_internal::MenuActionCommand::removeMenu()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17MenuActionCommand10removeMenuEv',
    )
