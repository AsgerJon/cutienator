"""
qdesigner_internal::LayoutCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::LayoutCommand to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class LayoutCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::LayoutCommand: a plain Python
  object standing in front of one C++ qdesigner_internal::LayoutCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::LayoutCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::LayoutCommand that has a ritual
  and that Python can call so far, 4 names in all: 'widgets', 'init', 'redo',
  'undo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::LayoutCommand::~LayoutCommand()': the
    destructor: Python never removes a C++ qdesigner_internal::LayoutCommand.

  What to expect
  --------------

  - The C++ qdesigner_internal::LayoutCommand is created at the first use,
    not by 'qdesigner_internal::LayoutCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::LayoutCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::LayoutCommand'

  #  A C++ qdesigner_internal::LayoutCommand Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_LayoutCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def widgets(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList qdesigner_internal::LayoutCommand::widgets()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutcommand.html#widgets

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::LayoutCommand::widgets() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal13LayoutCommand7widgetsEv',
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
    'qdesigner_internal::LayoutCommand::LayoutCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::LayoutCommand::LayoutCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(LayoutCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal13LayoutCommandC1EP28QDesignerFormWin'
        'dowInterface',
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

  @overload(QWidget, QList[QWidget], qdesigner_internal.LayoutInfo.Type)
  @overload(NoneType, QList[QWidget], qdesigner_internal.LayoutInfo.Type)
  @overload(
      QWidget, QList[QWidget], qdesigner_internal.LayoutInfo.Type, QWidget,
  )
  @overload(
      QWidget, QList[QWidget], qdesigner_internal.LayoutInfo.Type, NoneType,
  )
  @overload(
      NoneType, QList[QWidget], qdesigner_internal.LayoutInfo.Type, QWidget,
  )
  @overload(
      NoneType, QList[QWidget], qdesigner_internal.LayoutInfo.Type, NoneType,
  )
  @overload(
      QWidget, QList[QWidget], qdesigner_internal.LayoutInfo.Type, QWidget,
      bool,
  )
  @overload(
      QWidget, QList[QWidget], qdesigner_internal.LayoutInfo.Type, NoneType,
      bool,
  )
  @overload(
      NoneType, QList[QWidget], qdesigner_internal.LayoutInfo.Type, QWidget,
      bool,
  )
  @overload(
      NoneType, QList[QWidget], qdesigner_internal.LayoutInfo.Type, NoneType,
      bool,
  )
  def init(
      self,
      parentWidget: Optional[QWidget],
      widgets: QList[QWidget],
      layoutType: qdesigner_internal.LayoutInfo.Type,
      layoutBase: Optional[QWidget] = None,
      reparentLayoutWidget: bool = True,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutCommand::init(QWidget
    *parentWidget, const QWidgetList &widgets, LayoutInfo::Type layoutType,
    QWidget *layoutBase, bool reparentLayoutWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutcommand.html#init

    Parameters
    ----------

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgets : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    layoutType : qdesigner_internal.LayoutInfo.Type
      Passed on as its number.

    layoutBase : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    reparentLayoutWidget : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void qdesigner_internal::LayoutCommand::init(QWidget *parentWidget,
    #      const QWidgetList &widgets, LayoutInfo::Type layoutType, QWidget
    #      *layoutBase, bool reparentLayoutWidget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal13LayoutCommand4initEP7QWidgetRK5QLis'
        'tIS2_ENS_10LayoutInfo4TypeES2_b',
        self._addressOf(parentWidget), self._valueOf(widgets),
        layoutType.value, self._addressOf(layoutBase), reparentLayoutWidget,
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutcommand.html#redo
    """
    #  void qdesigner_internal::LayoutCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal13LayoutCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal13LayoutCommand4redoEv'
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layoutcommand.html#undo
    """
    #  void qdesigner_internal::LayoutCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal13LayoutCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal13LayoutCommand4undoEv'
    self.uglySide.call(ritual)
