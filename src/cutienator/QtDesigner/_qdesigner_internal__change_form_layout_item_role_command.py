"""
qdesigner_internal::ChangeFormLayoutItemRoleCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeFormLayoutItemRoleCommand to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QFormLayout, QWidget
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeFormLayoutItemRoleCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeFormLayoutItemRoleCommand:
  a plain Python object standing in front of one C++
  qdesigner_internal::ChangeFormLayoutItemRoleCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeFormLayoutItemRoleCommand is built on
  Qt's qdesigner_internal::QDesignerFormWindowCommand, and has everything
  that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeFormLayoutItemRoleCommand
  that has a ritual and that Python can call so far, 7 names in all: 'init',
  'redo', 'undo', 'possibleOperations', 'managedFormLayoutOf',
  'reverseOperation', 'doOperation'. It can be made from Python, in 1 way;
  see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeFormLayoutItemRoleCommand is created at
    the first use, not by
    'qdesigner_internal::ChangeFormLayoutItemRoleCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ChangeFormLayoutItemRoleCommand.
  """

  #  The enums Qt writes inside
  #  qdesigner_internal::ChangeFormLayoutItemRoleCommand, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Operation(CuteNum):
    """
    The enum 'qdesigner_internal::ChangeFormLayoutItemRoleCommand::Operation'
    of Qt, with the 4 names Qt gives in it.
    """

    SpanningToLabel = Kee[int](1)
    SpanningToField = Kee[int](2)
    LabelToSpanning = Kee[int](4)
    FieldToSpanning = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def possibleOperations(
      core: Optional[QDesignerFormEditorInterface],
      w: Optional[QWidget],
  ) -> int:
    """
    Calls Qt's 'unsigned int
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::possibleOperations(
    QDesignerFormEditorInterface *core, QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  unsigned int qdesigner_internal::ChangeFormLayoutItemRoleCommand::
    #      possibleOperations(QDesignerFormEditorInterface *core, QWidget *w)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand18po'
        'ssibleOperationsEP28QDesignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(w),
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def managedFormLayoutOf(
      core: Optional[QDesignerFormEditorInterface],
      w: Optional[QWidget],
  ) -> Optional[QFormLayout]:
    """
    Calls Qt's 'QFormLayout
    *qdesigner_internal::ChangeFormLayoutItemRoleCommand::
    managedFormLayoutOf(QDesignerFormEditorInterface *core, QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QFormLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFormLayout *qdesigner_internal::ChangeFormLayoutItemRoleCommand::
    #      managedFormLayoutOf(QDesignerFormEditorInterface *core, QWidget
    #      *w)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand19ma'
        'nagedFormLayoutOfEP28QDesignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(w),
    )
    from ..QtWidgets import QFormLayout
    return QFormLayout._cuteAt(address)

  @staticmethod
  @overload(Operation)
  def reverseOperation(op: Operation) -> Operation:
    """
    Calls Qt's 'Operation
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::reverseOperation(
    Operation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html

    Parameters
    ----------

    op : Operation
      Passed on as its number.

    Returns
    -------

    Operation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operation(number)' gives.
    """
    #  Operation qdesigner_internal::ChangeFormLayoutItemRoleCommand::
    #      reverseOperation(Operation op)
    return ChangeFormLayoutItemRoleCommand.Operation(Rituals.call(
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand16re'
        'verseOperationENS0_9OperationE',
        op.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ChangeFormLayoutItemRoleCommand'

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
    'qdesigner_internal::ChangeFormLayoutItemRoleCommand::
    ChangeFormLayoutItemRoleCommand(QDesignerFormWindowInterface
    *formWindow)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ChangeFormLayoutItemRoleCommand::
    #      ChangeFormLayoutItemRoleCommand(QDesignerFormWindowInterface
    #      *formWindow)
    self._noteCreation(ChangeFormLayoutItemRoleCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommandC1EP'
        '28QDesignerFormWindowInterface',
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

  @overload(QWidget, Operation)
  @overload(NoneType, Operation)
  def init(self, widget: Optional[QWidget], op: Operation) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::init(QWidget
    *widget, Operation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    op : Operation
      Passed on as its number.
    """
    #  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::init(QWidget
    #      *widget, Operation op)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4ini'
        'tEP7QWidgetNS0_9OperationE',
        self._addressOf(widget), op.value,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html
    """
    #  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4red'
        'oEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal31ChangeFormLayoutItemRoleComma'
          'nd4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html
    """
    #  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand4und'
        'oEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal31ChangeFormLayoutItemRoleComma'
          'nd4undoEv')
    self.uglySide.call(ritual)

  @overload(Operation)
  def doOperation(self, op: Operation) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeFormLayoutItemRoleCommand::doOperation(
    Operation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changeformlayoutitemrolecommand.html

    Parameters
    ----------

    op : Operation
      Passed on as its number.
    """
    #  void qdesigner_internal::ChangeFormLayoutItemRoleCommand::doOperation(
    #      Operation op)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal31ChangeFormLayoutItemRoleCommand11do'
        'OperationENS0_9OperationE',
        op.value,
    )
