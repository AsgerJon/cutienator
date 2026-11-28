"""
qdesigner_internal::ActionInsertionCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ActionInsertionCommand to be private: it
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

  from ..QtGui import QAction
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ActionInsertionCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ActionInsertionCommand: a plain
  Python object standing in front of one C++
  qdesigner_internal::ActionInsertionCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ActionInsertionCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionInsertionCommand that has
  a ritual and that Python can call so far, 1 name in all: 'init'. It can be
  made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionInsertionCommand is created at the
    first use, not by 'qdesigner_internal::ActionInsertionCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ActionInsertionCommand.
  - Each name of Qt's qdesigner_internal::ActionInsertionCommand that has no
    cute function yet, 'insertAction', 'removeAction', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ActionInsertionCommand'

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

  @overload(str, QDesignerFormWindowInterface)
  @overload(str, NoneType)
  def __init__(
      self,
      text: str,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ActionInsertionCommand::ActionInsertionCommand(const
    QString &text, QDesignerFormWindowInterface *formWindow)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioninsertioncommand.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ActionInsertionCommand::
    #      ActionInsertionCommand(const QString &text,
    #      QDesignerFormWindowInterface *formWindow)
    self._noteCreation(ActionInsertionCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22ActionInsertionCommandC1ERK7QString'
        'P28QDesignerFormWindowInterface',
        text, self._addressOf(formWindow),
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

  @overload(QWidget, QAction)
  @overload(QWidget, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  @overload(QWidget, QAction, QAction)
  @overload(QWidget, QAction, NoneType)
  @overload(QWidget, NoneType, QAction)
  @overload(QWidget, NoneType, NoneType)
  @overload(NoneType, QAction, QAction)
  @overload(NoneType, QAction, NoneType)
  @overload(NoneType, NoneType, QAction)
  @overload(NoneType, NoneType, NoneType)
  @overload(QWidget, QAction, QAction, bool)
  @overload(QWidget, QAction, NoneType, bool)
  @overload(QWidget, NoneType, QAction, bool)
  @overload(QWidget, NoneType, NoneType, bool)
  @overload(NoneType, QAction, QAction, bool)
  @overload(NoneType, QAction, NoneType, bool)
  @overload(NoneType, NoneType, QAction, bool)
  @overload(NoneType, NoneType, NoneType, bool)
  def init(
      self,
      parentWidget: Optional[QWidget],
      action: Optional[QAction],
      beforeAction: Optional[QAction] = None,
      update: bool = True,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionInsertionCommand::init(QWidget
    *parentWidget, QAction *action, QAction *beforeAction, bool update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioninsertioncommand.html

    Parameters
    ----------

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    beforeAction : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void qdesigner_internal::ActionInsertionCommand::init(QWidget
    #      *parentWidget, QAction *action, QAction *beforeAction, bool
    #      update)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22ActionInsertionCommand4initEP7QWidg'
        'etP7QActionS4_b',
        self._addressOf(parentWidget), self._addressOf(action),
        self._addressOf(beforeAction), update,
    )

  @staticmethod
  def insertAction(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::ActionInsertionCommand::insertAction()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'PropertyHelper'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ActionInsertionCommand.insertAction' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::ActionInsertionCommand::insertAction()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'PropertyHelper'.")

  @staticmethod
  def removeAction(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::ActionInsertionCommand::removeAction()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'PropertyHelper'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ActionInsertionCommand.removeAction' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::ActionInsertionCommand::removeAction()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'PropertyHelper'.")
