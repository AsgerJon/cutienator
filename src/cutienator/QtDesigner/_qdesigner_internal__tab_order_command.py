"""
qdesigner_internal::TabOrderCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::TabOrderCommand to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
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


class TabOrderCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::TabOrderCommand: a plain Python
  object standing in front of one C++ qdesigner_internal::TabOrderCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::TabOrderCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::TabOrderCommand that has a
  ritual and that Python can call so far, 5 names in all: 'init',
  'oldTabOrder', 'newTabOrder', 'redo', 'undo'. It can be made from Python,
  in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::TabOrderCommand is created at the first use,
    not by 'qdesigner_internal::TabOrderCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::TabOrderCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::TabOrderCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def oldTabOrder(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::TabOrderCommand::oldTabOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tabordercommand.html

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::TabOrderCommand::oldTabOrder() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal15TabOrderCommand11oldTabOrderEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  def newTabOrder(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::TabOrderCommand::newTabOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tabordercommand.html

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::TabOrderCommand::newTabOrder() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal15TabOrderCommand11newTabOrderEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

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
    'qdesigner_internal::TabOrderCommand::TabOrderCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tabordercommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::TabOrderCommand::TabOrderCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(TabOrderCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal15TabOrderCommandC1EP28QDesignerFormW'
        'indowInterface',
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

  @overload(QList[QWidget])
  def init(self, newTabOrder: QList[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TabOrderCommand::init(const
    QWidgetList &newTabOrder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tabordercommand.html#init

    Parameters
    ----------

    newTabOrder : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::TabOrderCommand::init(const QWidgetList
    #      &newTabOrder)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15TabOrderCommand4initERK5QListIP7QWi'
        'dgetE',
        self._valueOf(newTabOrder),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TabOrderCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tabordercommand.html#redo
    """
    #  void qdesigner_internal::TabOrderCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal15TabOrderCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal15TabOrderCommand4redoEv'
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TabOrderCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-tabordercommand.html#undo
    """
    #  void qdesigner_internal::TabOrderCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal15TabOrderCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal15TabOrderCommand4undoEv'
    self.uglySide.call(ritual)
