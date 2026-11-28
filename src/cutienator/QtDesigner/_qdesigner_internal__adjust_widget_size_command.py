"""
qdesigner_internal::AdjustWidgetSizeCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::AdjustWidgetSizeCommand to be private: it
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


class AdjustWidgetSizeCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::AdjustWidgetSizeCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::AdjustWidgetSizeCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::AdjustWidgetSizeCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::AdjustWidgetSizeCommand that has
  a ritual and that Python can call so far, 5 names in all: 'init', 'redo',
  'undo', 'widgetForAdjust', 'updatePropertyEditor'. It can be made from
  Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::AdjustWidgetSizeCommand is created at the
    first use, not by 'qdesigner_internal::AdjustWidgetSizeCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::AdjustWidgetSizeCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::AdjustWidgetSizeCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def widgetForAdjust(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::AdjustWidgetSizeCommand::widgetForAdjust() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-adjustwidgetsizecommand.html

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget
    #      *qdesigner_internal::AdjustWidgetSizeCommand::widgetForAdjust()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23AdjustWidgetSizeCommand15widgetFor'
        'AdjustEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

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
    'qdesigner_internal::AdjustWidgetSizeCommand::AdjustWidgetSizeCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-adjustwidgetsizecommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::AdjustWidgetSizeCommand::
    #      AdjustWidgetSizeCommand(QDesignerFormWindowInterface *formWindow)
    self._noteCreation(AdjustWidgetSizeCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommandC1EP28QDesig'
        'nerFormWindowInterface',
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
  def init(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::AdjustWidgetSizeCommand::init(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-adjustwidgetsizecommand.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::AdjustWidgetSizeCommand::init(QWidget
    #      *widget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommand4initEP7QWid'
        'get',
        self._addressOf(widget),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AdjustWidgetSizeCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-adjustwidgetsizecommand.html
    """
    #  void qdesigner_internal::AdjustWidgetSizeCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal23AdjustWidgetSizeCommand4redoE'
          'v')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::AdjustWidgetSizeCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-adjustwidgetsizecommand.html
    """
    #  void qdesigner_internal::AdjustWidgetSizeCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal23AdjustWidgetSizeCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal23AdjustWidgetSizeCommand4undoE'
          'v')
    self.uglySide.call(ritual)

  def updatePropertyEditor(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::AdjustWidgetSizeCommand::updatePropertyEditor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-adjustwidgetsizecommand.html
    """
    #  void
    #      qdesigner_internal::AdjustWidgetSizeCommand::updatePropertyEditor(
    #      ) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23AdjustWidgetSizeCommand20updatePro'
        'pertyEditorEv',
    )
