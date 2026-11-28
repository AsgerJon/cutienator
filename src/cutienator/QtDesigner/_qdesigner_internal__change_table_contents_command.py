"""
qdesigner_internal::ChangeTableContentsCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeTableContentsCommand to be private: it
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

  from ..QtWidgets import QTableWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QTableWidget = WAIT['QTableWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeTableContentsCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeTableContentsCommand: a
  plain Python object standing in front of one C++
  qdesigner_internal::ChangeTableContentsCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeTableContentsCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeTableContentsCommand that
  has a ritual and that Python can call so far, 3 names in all: 'init',
  'redo', 'undo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeTableContentsCommand is created at the
    first use, not by 'qdesigner_internal::ChangeTableContentsCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ChangeTableContentsCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ChangeTableContentsCommand'

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
    'qdesigner_internal::ChangeTableContentsCommand::
    ChangeTableContentsCommand(QDesignerFormWindowInterface *formWindow)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetablecontentscommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ChangeTableContentsCommand::
    #      ChangeTableContentsCommand(QDesignerFormWindowInterface
    #      *formWindow)
    self._noteCreation(ChangeTableContentsCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal26ChangeTableContentsCommandC1EP28QDe'
        'signerFormWindowInterface',
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

  @overload(
      QTableWidget, WAIT['qdesigner_internal.TableWidgetContents'],
      WAIT['qdesigner_internal.TableWidgetContents'],
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.TableWidgetContents'],
      WAIT['qdesigner_internal.TableWidgetContents'],
  )
  def init(
      self,
      tableWidget: Optional[QTableWidget],
      oldCont: qdesigner_internal.TableWidgetContents,
      newCont: qdesigner_internal.TableWidgetContents,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeTableContentsCommand::init(QTableWidget
    *tableWidget, const TableWidgetContents &oldCont, const
    TableWidgetContents &newCont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetablecontentscommand.html

    Parameters
    ----------

    tableWidget : Optional[QTableWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldCont : qdesigner_internal.TableWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TableWidgetContents, which stays Python's own.

    newCont : qdesigner_internal.TableWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TableWidgetContents, which stays Python's own.
    """
    #  void qdesigner_internal::ChangeTableContentsCommand::init(QTableWidget
    #      *tableWidget, const TableWidgetContents &oldCont, const
    #      TableWidgetContents &newCont)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal26ChangeTableContentsCommand4initEP12'
        'QTableWidgetRKNS_19TableWidgetContentsES5_',
        self._addressOf(tableWidget), self._valueOf(oldCont),
        self._valueOf(newCont),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeTableContentsCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetablecontentscommand.html
    """
    #  void qdesigner_internal::ChangeTableContentsCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal26ChangeTableContentsCommand4redoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal26ChangeTableContentsCommand4re'
          'doEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeTableContentsCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changetablecontentscommand.html
    """
    #  void qdesigner_internal::ChangeTableContentsCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal26ChangeTableContentsCommand4undoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal26ChangeTableContentsCommand4un'
          'doEv')
    self.uglySide.call(ritual)
