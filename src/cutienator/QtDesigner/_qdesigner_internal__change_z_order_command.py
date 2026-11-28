"""
qdesigner_internal::ChangeZOrderCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeZOrderCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeZOrderCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeZOrderCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::ChangeZOrderCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeZOrderCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeZOrderCommand that has a
  ritual and that Python can call so far, 5 names in all: 'init', 'redo',
  'undo', 'reorderWidget', 'reorder'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeZOrderCommand is created at the first
    use, not by 'qdesigner_internal::ChangeZOrderCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ChangeZOrderCommand.
  - Each name of Qt's qdesigner_internal::ChangeZOrderCommand that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::ChangeZOrderCommand'

  #  The functions Qt calls itself that
  #  qdesigner_internal::ChangeZOrderCommand is the first to declare and that
  #  cannot be handed to Python yet, each as Qt declares it. A class of a
  #  program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'reorderWidget': (
          'QWidgetList '
          'qdesigner_internal::ChangeZOrderCommand::reorderWidget(const '
          'QWidgetList &, QWidget *) const',
      ),
  }

  #  The functions Qt calls itself that
  #  qdesigner_internal::ChangeZOrderCommand is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'reorder': (
          ('_ZNK18qdesigner_internal19ChangeZOrderCommand7reorderEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
  }

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
    qdesigner_internal::ChangeZOrderCommand::reorderWidget(const QWidgetList
    &list, QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changezordercommand.html

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
    #      qdesigner_internal::ChangeZOrderCommand::reorderWidget(const
    #      QWidgetList &list, QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19ChangeZOrderCommand13reorderWidget'
        'ERK5QListIP7QWidgetES3_',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::ChangeZOrderCommand::ChangeZOrderCommand(
    QDesignerFormWindowInterface *formWindow)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ChangeZOrderCommand.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::ChangeZOrderCommand::ChangeZOrderCommand(QDesi"
        "gnerFormWindowInterface *formWindow)': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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
    Calls Qt's 'void qdesigner_internal::ChangeZOrderCommand::init(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changezordercommand.html#init

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ChangeZOrderCommand::init(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19ChangeZOrderCommand4initEP7QWidget',
        self._addressOf(widget),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeZOrderCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changezordercommand.html#redo
    """
    #  void qdesigner_internal::ChangeZOrderCommand::redo()
    ritual = 'ritual_ZN18qdesigner_internal19ChangeZOrderCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19ChangeZOrderCommand4redoEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeZOrderCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changezordercommand.html#undo
    """
    #  void qdesigner_internal::ChangeZOrderCommand::undo()
    ritual = 'ritual_ZN18qdesigner_internal19ChangeZOrderCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal19ChangeZOrderCommand4undoEv')
    self.uglySide.call(ritual)

  @overload(QWidget)
  @overload(NoneType)
  def reorder(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeZOrderCommand::reorder(QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changezordercommand.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ChangeZOrderCommand::reorder(QWidget *widget)
    #      const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19ChangeZOrderCommand7reorderEP7QWid'
        'get',
        self._addressOf(widget),
    )
