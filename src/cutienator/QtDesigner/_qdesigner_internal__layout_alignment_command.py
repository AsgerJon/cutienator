"""
qdesigner_internal::LayoutAlignmentCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command2_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::LayoutAlignmentCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtWidgets import QWidget
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


class LayoutAlignmentCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::LayoutAlignmentCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::LayoutAlignmentCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::LayoutAlignmentCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::LayoutAlignmentCommand that has
  a ritual and that Python can call so far, 4 names in all: 'init', 'redo',
  'undo', 'applyAlignment'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt::Alignment
    qdesigner_internal::LayoutAlignmentCommand::alignmentOf(const
    QDesignerFormEditorInterface *core, QWidget *w, bool *enabled)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ qdesigner_internal::LayoutAlignmentCommand is created at the
    first use, not by 'qdesigner_internal::LayoutAlignmentCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::LayoutAlignmentCommand.
  - Each name of Qt's qdesigner_internal::LayoutAlignmentCommand that has no
    cute function yet, 'alignmentOf', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget, Qt.Alignment)
  @overload(QDesignerFormEditorInterface, NoneType, Qt.Alignment)
  @overload(NoneType, QWidget, Qt.Alignment)
  @overload(NoneType, NoneType, Qt.Alignment)
  def applyAlignment(
      core: Optional[QDesignerFormEditorInterface],
      w: Optional[QWidget],
      a: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::LayoutAlignmentCommand::applyAlignment(const
    QDesignerFormEditorInterface *core, QWidget *w, Qt::Alignment a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutalignmentcommand.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a : Qt.Alignment
      Passed on as its number.
    """
    #  void qdesigner_internal::LayoutAlignmentCommand::applyAlignment(const
    #      QDesignerFormEditorInterface *core, QWidget *w, Qt::Alignment a)
    Rituals.call(
        'ritual_ZN18qdesigner_internal22LayoutAlignmentCommand14applyAlignm'
        'entEPK28QDesignerFormEditorInterfaceP7QWidget6QFlagsIN2Qt13Alignme'
        'ntFlagEE',
        CuteMixin._addressOf(core), CuteMixin._addressOf(w), a.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::LayoutAlignmentCommand'

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
    'qdesigner_internal::LayoutAlignmentCommand::LayoutAlignmentCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutalignmentcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::LayoutAlignmentCommand::
    #      LayoutAlignmentCommand(QDesignerFormWindowInterface *formWindow)
    self._noteCreation(LayoutAlignmentCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22LayoutAlignmentCommandC1EP28QDesign'
        'erFormWindowInterface',
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

  @overload(QWidget, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def init(self, w: Optional[QWidget], alignment: Qt.Alignment) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::LayoutAlignmentCommand::init(QWidget
    *w, Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutalignmentcommand.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  bool qdesigner_internal::LayoutAlignmentCommand::init(QWidget *w,
    #      Qt::Alignment alignment)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal22LayoutAlignmentCommand4initEP7QWidg'
        'et6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(w), alignment.value,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutAlignmentCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutalignmentcommand.html
    """
    #  void qdesigner_internal::LayoutAlignmentCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal22LayoutAlignmentCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal22LayoutAlignmentCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutAlignmentCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutalignmentcommand.html
    """
    #  void qdesigner_internal::LayoutAlignmentCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal22LayoutAlignmentCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal22LayoutAlignmentCommand4undoEv')
    self.uglySide.call(ritual)

  @staticmethod
  def alignmentOf(*__, **_) -> Never:
    """
    Qt's 'Qt::Alignment
    qdesigner_internal::LayoutAlignmentCommand::alignmentOf(const
    QDesignerFormEditorInterface *core, QWidget *w, bool *enabled)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.LayoutAlignmentCommand.alignmentOf' has no "
        "cute function yet. Qt's 'Qt::Alignment "
        "qdesigner_internal::LayoutAlignmentCommand::alignmentOf(const "
        "QDesignerFormEditorInterface *core, QWidget *w, bool *enabled)': "
        "takes a number to change where it is.")
