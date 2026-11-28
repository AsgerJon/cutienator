"""
qdesigner_internal::ChangeCurrentPageCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeCurrentPageCommand to be private: it
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
  from . import QDesignerContainerExtension, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeCurrentPageCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeCurrentPageCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::ChangeCurrentPageCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeCurrentPageCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeCurrentPageCommand that
  has a ritual and that Python can call so far, 4 names in all:
  'containerExtension', 'init', 'redo', 'undo'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::ChangeCurrentPageCommand::~ChangeCurrentPageCommand(
    )': the destructor: Python never removes a C++
    qdesigner_internal::ChangeCurrentPageCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeCurrentPageCommand is created at the
    first use, not by 'qdesigner_internal::ChangeCurrentPageCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ChangeCurrentPageCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ChangeCurrentPageCommand'

  #  A C++ qdesigner_internal::ChangeCurrentPageCommand Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_ChangeCurrentPageCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def containerExtension(self) -> Optional[QDesignerContainerExtension]:
    """
    Calls Qt's 'QDesignerContainerExtension
    *qdesigner_internal::ChangeCurrentPageCommand::containerExtension()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changecurrentpagecommand.html

    Returns
    -------

    Optional[QDesignerContainerExtension]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerContainerExtension
    #      *qdesigner_internal::ChangeCurrentPageCommand::containerExtension(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24ChangeCurrentPageCommand18containe'
        'rExtensionEv',
    )
    from . import QDesignerContainerExtension
    return QDesignerContainerExtension._cuteAt(address)

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
    'qdesigner_internal::ChangeCurrentPageCommand::ChangeCurrentPageCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changecurrentpagecommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ChangeCurrentPageCommand::
    #      ChangeCurrentPageCommand(QDesignerFormWindowInterface *formWindow)
    self._noteCreation(ChangeCurrentPageCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24ChangeCurrentPageCommandC1EP28QDesi'
        'gnerFormWindowInterface',
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

  @overload(QWidget, int)
  @overload(NoneType, int)
  def init(self, containerWidget: Optional[QWidget], newIndex: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeCurrentPageCommand::init(QWidget
    *containerWidget, int newIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changecurrentpagecommand.html

    Parameters
    ----------

    containerWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newIndex : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ChangeCurrentPageCommand::init(QWidget
    #      *containerWidget, int newIndex)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24ChangeCurrentPageCommand4initEP7QWi'
        'dgeti',
        self._addressOf(containerWidget), newIndex,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeCurrentPageCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changecurrentpagecommand.html
    """
    #  void qdesigner_internal::ChangeCurrentPageCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal24ChangeCurrentPageCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24ChangeCurrentPageCommand4redo'
          'Ev')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeCurrentPageCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changecurrentpagecommand.html
    """
    #  void qdesigner_internal::ChangeCurrentPageCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal24ChangeCurrentPageCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24ChangeCurrentPageCommand4undo'
          'Ev')
    self.uglySide.call(ritual)
