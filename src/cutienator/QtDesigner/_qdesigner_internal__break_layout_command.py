"""
qdesigner_internal::BreakLayoutCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::BreakLayoutCommand to be private: it declares
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


class BreakLayoutCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::BreakLayoutCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::BreakLayoutCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::BreakLayoutCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::BreakLayoutCommand that has a
  ritual and that Python can call so far, 6 names in all: 'widgets', 'init',
  'redo', 'undo', 'layoutProperties', 'propertyMask'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::BreakLayoutCommand::~BreakLayoutCommand()': the
    destructor: Python never removes a C++
    qdesigner_internal::BreakLayoutCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::BreakLayoutCommand is created at the first
    use, not by 'qdesigner_internal::BreakLayoutCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::BreakLayoutCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::BreakLayoutCommand'

  #  A C++ qdesigner_internal::BreakLayoutCommand Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_BreakLayoutCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def widgets(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList qdesigner_internal::BreakLayoutCommand::widgets()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html#widgets

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::BreakLayoutCommand::widgets() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18BreakLayoutCommand7widgetsEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  def layoutProperties(
      self,
  ) -> Optional[qdesigner_internal.LayoutProperties]:
    """
    Calls Qt's 'const LayoutProperties
    *qdesigner_internal::BreakLayoutCommand::layoutProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html

    Returns
    -------

    Optional[qdesigner_internal.LayoutProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const LayoutProperties
    #      *qdesigner_internal::BreakLayoutCommand::layoutProperties() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18BreakLayoutCommand16layoutProperti'
        'esEv',
    )
    return qdesigner_internal.LayoutProperties._cuteAt(address)

  def propertyMask(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::BreakLayoutCommand::propertyMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html
    """
    #  int qdesigner_internal::BreakLayoutCommand::propertyMask() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18BreakLayoutCommand12propertyMaskEv',
    )

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
    'qdesigner_internal::BreakLayoutCommand::BreakLayoutCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::BreakLayoutCommand::BreakLayoutCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(BreakLayoutCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18BreakLayoutCommandC1EP28QDesignerFo'
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

  @overload(QList[QWidget], QWidget)
  @overload(QList[QWidget], NoneType)
  @overload(QList[QWidget], QWidget, bool)
  @overload(QList[QWidget], NoneType, bool)
  def init(
      self,
      widgets: QList[QWidget],
      layoutBase: Optional[QWidget],
      reparentLayoutWidget: bool = True,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::BreakLayoutCommand::init(const
    QWidgetList &widgets, QWidget *layoutBase, bool reparentLayoutWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html#init

    Parameters
    ----------

    widgets : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    layoutBase : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reparentLayoutWidget : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void qdesigner_internal::BreakLayoutCommand::init(const QWidgetList
    #      &widgets, QWidget *layoutBase, bool reparentLayoutWidget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18BreakLayoutCommand4initERK5QListIP7'
        'QWidgetES3_b',
        self._valueOf(widgets), self._addressOf(layoutBase),
        reparentLayoutWidget,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::BreakLayoutCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html#redo
    """
    #  void qdesigner_internal::BreakLayoutCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal18BreakLayoutCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal18BreakLayoutCommand4redoEv'
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::BreakLayoutCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-breaklayoutcommand.html#undo
    """
    #  void qdesigner_internal::BreakLayoutCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal18BreakLayoutCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal18BreakLayoutCommand4undoEv'
    self.uglySide.call(ritual)
