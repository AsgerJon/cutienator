"""
qdesigner_internal::RaiseWidgetCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::RaiseWidgetCommand to be private: it declares
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


class RaiseWidgetCommand(qdesigner_internal.ChangeZOrderCommand):
  """
  The cute side of Qt's qdesigner_internal::RaiseWidgetCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::RaiseWidgetCommand.

  It is built on the cute 'qdesigner_internal::ChangeZOrderCommand', as Qt's
  qdesigner_internal::RaiseWidgetCommand is built on Qt's
  qdesigner_internal::ChangeZOrderCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::RaiseWidgetCommand that has a
  ritual and that Python can call so far, 3 names in all: 'init',
  'reorderWidget', 'reorder'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::RaiseWidgetCommand is created at the first
    use, not by 'qdesigner_internal::RaiseWidgetCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::RaiseWidgetCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::RaiseWidgetCommand'

  #  A C++ qdesigner_internal::RaiseWidgetCommand Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_RaiseWidgetCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QWidget], QWidget)
  @overload(QList[QWidget], NoneType)
  def reorderWidget(
      self,
      list: QList[QWidget],
      widget: Optional[QWidget],
  ) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::RaiseWidgetCommand::reorderWidget(const QWidgetList
    &list, QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-raisewidgetcommand.html

    Parameters
    ----------

    list : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList
    #      qdesigner_internal::RaiseWidgetCommand::reorderWidget(const
    #      QWidgetList &list, QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18RaiseWidgetCommand13reorderWidgetE'
        'RK5QListIP7QWidgetES3_',
        self._valueOf(list), self._addressOf(widget),
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
    'qdesigner_internal::RaiseWidgetCommand::RaiseWidgetCommand(
    QDesignerFormWindowInterface *formWindow)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-raisewidgetcommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::RaiseWidgetCommand::RaiseWidgetCommand(
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(RaiseWidgetCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18RaiseWidgetCommandC1EP28QDesignerFo'
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

  @overload(QWidget)
  @overload(NoneType)
  def init(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::RaiseWidgetCommand::init(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-raisewidgetcommand.html#init

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::RaiseWidgetCommand::init(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18RaiseWidgetCommand4initEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def reorder(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::RaiseWidgetCommand::reorder(QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-raisewidgetcommand.html#reorder

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::RaiseWidgetCommand::reorder(QWidget *widget)
    #      const
    ritual = (
        'ritual_ZNK18qdesigner_internal18RaiseWidgetCommand7reorderEP7QWidg'
        'et')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal18RaiseWidgetCommand7reorderEP'
          '7QWidget')
    self.uglySide.call(ritual, self._addressOf(widget))
