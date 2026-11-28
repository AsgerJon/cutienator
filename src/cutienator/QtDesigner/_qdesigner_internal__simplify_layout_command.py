"""
qdesigner_internal::SimplifyLayoutCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::SimplifyLayoutCommand to be private: it
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
  from typing import Never, Optional

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


class SimplifyLayoutCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::SimplifyLayoutCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::SimplifyLayoutCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::SimplifyLayoutCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::SimplifyLayoutCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'redo',
  'undo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::SimplifyLayoutCommand::~SimplifyLayoutCommand()':
    the destructor: Python never removes a C++
    qdesigner_internal::SimplifyLayoutCommand.
  - Qt's 'bool qdesigner_internal::SimplifyLayoutCommand::canSimplify(
    QDesignerFormEditorInterface *core, const QWidget *w, int *layoutType)':
    takes a number to change where it is.

  What to expect
  --------------

  - The C++ qdesigner_internal::SimplifyLayoutCommand is created at the first
    use, not by 'qdesigner_internal::SimplifyLayoutCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::SimplifyLayoutCommand.
  - Each name of Qt's qdesigner_internal::SimplifyLayoutCommand that has no
    cute function yet, 'canSimplify', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::SimplifyLayoutCommand'

  #  A C++ qdesigner_internal::SimplifyLayoutCommand Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_SimplifyLayoutCommand'

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
    'qdesigner_internal::SimplifyLayoutCommand::SimplifyLayoutCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-simplifylayoutcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::SimplifyLayoutCommand::SimplifyLayoutCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(SimplifyLayoutCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal21SimplifyLayoutCommandC1EP28QDesigne'
        'rFormWindowInterface',
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
  def init(self, layoutBase: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::SimplifyLayoutCommand::init(QWidget
    *layoutBase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-simplifylayoutcommand.html#init

    Parameters
    ----------

    layoutBase : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::SimplifyLayoutCommand::init(QWidget
    #      *layoutBase)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal21SimplifyLayoutCommand4initEP7QWidge'
        't',
        self._addressOf(layoutBase),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SimplifyLayoutCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-simplifylayoutcommand.html#redo
    """
    #  void qdesigner_internal::SimplifyLayoutCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal21SimplifyLayoutCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal21SimplifyLayoutCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SimplifyLayoutCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-simplifylayoutcommand.html#undo
    """
    #  void qdesigner_internal::SimplifyLayoutCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal21SimplifyLayoutCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal21SimplifyLayoutCommand4undoEv')
    self.uglySide.call(ritual)

  @staticmethod
  def canSimplify(*__, **_) -> Never:
    """
    Qt's 'bool qdesigner_internal::SimplifyLayoutCommand::canSimplify(
    QDesignerFormEditorInterface *core, const QWidget *w, int *layoutType)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SimplifyLayoutCommand.canSimplify' has no cute "
        "function yet. Qt's 'bool "
        "qdesigner_internal::SimplifyLayoutCommand::canSimplify(QDesignerFor"
        "mEditorInterface *core, const QWidget *w, int *layoutType)': takes "
        "a number to change where it is.")
