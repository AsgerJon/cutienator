"""
qdesigner_internal::RemoveActionCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::RemoveActionCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RemoveActionCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::RemoveActionCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::RemoveActionCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::RemoveActionCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::RemoveActionCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'redo',
  'undo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::RemoveActionCommand is created at the first
    use, not by 'qdesigner_internal::RemoveActionCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::RemoveActionCommand.
  """

  #  The classes Qt writes inside qdesigner_internal::RemoveActionCommand,
  #  each a class in here as in C++.

  class ActionDataItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    qdesigner_internal::RemoveActionCommand::ActionDataItem: a plain Python
    object standing in front of one C++
    qdesigner_internal::RemoveActionCommand::ActionDataItem.

    C++ hands a qdesigner_internal::RemoveActionCommand::ActionDataItem
    around as a copy, so every C++
    qdesigner_internal::RemoveActionCommand::ActionDataItem behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    qdesigner_internal::RemoveActionCommand::ActionDataItem yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'qdesigner_internal::RemoveActionCommand::ActionDataItem::
      ~ActionDataItem()': the destructor: Python removes its C++
      qdesigner_internal::RemoveActionCommand::ActionDataItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ qdesigner_internal::RemoveActionCommand::ActionDataItem is
      created at the first use, not by
      'qdesigner_internal::RemoveActionCommand::ActionDataItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      qdesigner_internal::RemoveActionCommand::ActionDataItem back gives a
      copy the ritual made for Python, in a new cute
      qdesigner_internal::RemoveActionCommand::ActionDataItem.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QAction = WAIT['QAction']
      QWidget = WAIT['QWidget']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'qdesigner_internal::RemoveActionCommand::ActionDataItem'

    #  Qt's '~qdesigner_internal::RemoveActionCommand::ActionDataItem()'.
    #  Naming it makes this a value class: Python owns every C++
    #  qdesigner_internal::RemoveActionCommand::ActionDataItem behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18qdesigner_internal19RemoveActionCommand14ActionDataItemD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(QAction)
    @overload(NoneType)
    @overload(QAction, QWidget)
    @overload(QAction, NoneType)
    @overload(NoneType, QWidget)
    @overload(NoneType, NoneType)
    def __init__(
        self,
        _before: Optional[QAction] = None,
        _widget: Optional[QWidget] = None,
    ) -> None:
      """
      Notes what was given, for Qt's
      'qdesigner_internal::RemoveActionCommand::ActionDataItem::
      ActionDataItem(QAction *_before, QWidget *_widget)', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-removeactioncommand-actiondataitem.html

      Parameters
      ----------

      _before : Optional[QAction]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.

      _widget : Optional[QWidget]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.
      """
      #  qdesigner_internal::RemoveActionCommand::ActionDataItem::
      #      ActionDataItem(QAction *_before, QWidget *_widget)
      self._noteCreation(
          RemoveActionCommand.ActionDataItem, lambda: Rituals.call(
              'ritual_ZN18qdesigner_internal19RemoveActionCommand14ActionDa'
              'taItemC1EP7QActionP7QWidget',
              self._addressOf(_before), self._addressOf(_widget),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::RemoveActionCommand'

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
    'qdesigner_internal::RemoveActionCommand::RemoveActionCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-removeactioncommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::RemoveActionCommand::RemoveActionCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(RemoveActionCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19RemoveActionCommandC1EP28QDesignerF'
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

  @overload(QAction)
  @overload(NoneType)
  def init(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::RemoveActionCommand::init(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-removeactioncommand.html#init

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::RemoveActionCommand::init(QAction *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19RemoveActionCommand4initEP7QAction',
        self._addressOf(action),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::RemoveActionCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-removeactioncommand.html#redo
    """
    #  void qdesigner_internal::RemoveActionCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal19RemoveActionCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19RemoveActionCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::RemoveActionCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-removeactioncommand.html#undo
    """
    #  void qdesigner_internal::RemoveActionCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal19RemoveActionCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19RemoveActionCommand4undoEv')
    self.uglySide.call(ritual)
