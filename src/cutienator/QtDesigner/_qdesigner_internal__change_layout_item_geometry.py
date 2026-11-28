"""
qdesigner_internal::ChangeLayoutItemGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeLayoutItemGeometry to be private: it
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

  from ..QtCore import QRect
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeLayoutItemGeometry(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeLayoutItemGeometry: a plain
  Python object standing in front of one C++
  qdesigner_internal::ChangeLayoutItemGeometry.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeLayoutItemGeometry is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeLayoutItemGeometry that
  has a ritual and that Python can call so far, 4 names in all: 'init',
  'redo', 'undo', 'changeItemPosition'. It can be made from Python, in 1 way;
  see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeLayoutItemGeometry is created at the
    first use, not by 'qdesigner_internal::ChangeLayoutItemGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ChangeLayoutItemGeometry.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ChangeLayoutItemGeometry'

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
    'qdesigner_internal::ChangeLayoutItemGeometry::ChangeLayoutItemGeometry(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelayoutitemgeometry.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ChangeLayoutItemGeometry::
    #      ChangeLayoutItemGeometry(QDesignerFormWindowInterface *formWindow)
    self._noteCreation(ChangeLayoutItemGeometry, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometryC1EP28QDesi'
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

  @overload(QWidget, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  def init(
      self,
      widget: Optional[QWidget],
      row: int,
      column: int,
      rowspan: int,
      colspan: int,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeLayoutItemGeometry::init(QWidget *widget, int
    row, int column, int rowspan, int colspan)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelayoutitemgeometry.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    rowspan : int
      Passed on as it is.

    colspan : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ChangeLayoutItemGeometry::init(QWidget
    #      *widget, int row, int column, int rowspan, int colspan)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry4initEP7QWi'
        'dgetiiii',
        self._addressOf(widget), row, column, rowspan, colspan,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeLayoutItemGeometry::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelayoutitemgeometry.html
    """
    #  void qdesigner_internal::ChangeLayoutItemGeometry::redo()
    ritual = 'ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24ChangeLayoutItemGeometry4redo'
          'Ev')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeLayoutItemGeometry::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelayoutitemgeometry.html
    """
    #  void qdesigner_internal::ChangeLayoutItemGeometry::undo()
    ritual = 'ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal24ChangeLayoutItemGeometry4undo'
          'Ev')
    self.uglySide.call(ritual)

  @overload(QRect)
  def changeItemPosition(self, g: QRect) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeLayoutItemGeometry::changeItemPosition(const
    QRect &g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelayoutitemgeometry.html

    Parameters
    ----------

    g : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void qdesigner_internal::ChangeLayoutItemGeometry::changeItemPosition(
    #      const QRect &g)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24ChangeLayoutItemGeometry18changeIte'
        'mPositionERK5QRect',
        self._valueOf(g),
    )
