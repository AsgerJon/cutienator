"""
qdesigner_internal::ChangeListContentsCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ChangeListContentsCommand to be private: it
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

  from ..QtWidgets import QComboBox, QListWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QComboBox = WAIT['QComboBox']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QListWidget = WAIT['QListWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChangeListContentsCommand(qdesigner_internal.QDesignerFormWindowCommand):
  """
  The cute side of Qt's qdesigner_internal::ChangeListContentsCommand: a
  plain Python object standing in front of one C++
  qdesigner_internal::ChangeListContentsCommand.

  It is built on the cute 'qdesigner_internal::QDesignerFormWindowCommand',
  as Qt's qdesigner_internal::ChangeListContentsCommand is built on Qt's
  qdesigner_internal::QDesignerFormWindowCommand, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ChangeListContentsCommand that
  has a ritual and that Python can call so far, 3 names in all: 'init',
  'redo', 'undo'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::ChangeListContentsCommand is created at the
    first use, not by 'qdesigner_internal::ChangeListContentsCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ChangeListContentsCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ChangeListContentsCommand'

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
    'qdesigner_internal::ChangeListContentsCommand::
    ChangeListContentsCommand(QDesignerFormWindowInterface *formWindow)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelistcontentscommand.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ChangeListContentsCommand::
    #      ChangeListContentsCommand(QDesignerFormWindowInterface
    #      *formWindow)
    self._noteCreation(ChangeListContentsCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal25ChangeListContentsCommandC1EP28QDes'
        'ignerFormWindowInterface',
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
      QListWidget, WAIT['qdesigner_internal.ListContents'],
      WAIT['qdesigner_internal.ListContents'],
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.ListContents'],
      WAIT['qdesigner_internal.ListContents'],
  )
  def init(
      self,
      listWidget: Optional[QListWidget],
      oldItems: qdesigner_internal.ListContents,
      items: qdesigner_internal.ListContents,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeListContentsCommand::init(QListWidget
    *listWidget, const ListContents &oldItems, const ListContents &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelistcontentscommand.html

    Parameters
    ----------

    listWidget : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItems : qdesigner_internal.ListContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::ListContents, which stays Python's own.

    items : qdesigner_internal.ListContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::ListContents, which stays Python's own.
    """
    #  void qdesigner_internal::ChangeListContentsCommand::init(QListWidget
    #      *listWidget, const ListContents &oldItems, const ListContents
    #      &items)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ChangeListContentsCommand4initEP11Q'
        'ListWidgetRKNS_12ListContentsES5_',
        self._addressOf(listWidget), self._valueOf(oldItems),
        self._valueOf(items),
    )

  @overload(
      QComboBox, WAIT['qdesigner_internal.ListContents'],
      WAIT['qdesigner_internal.ListContents'],
  )
  def init(
      self,
      comboBox: Optional[QComboBox],
      oldItems: qdesigner_internal.ListContents,
      items: qdesigner_internal.ListContents,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ChangeListContentsCommand::init(QComboBox *comboBox,
    const ListContents &oldItems, const ListContents &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelistcontentscommand.html

    Parameters
    ----------

    comboBox : Optional[QComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItems : qdesigner_internal.ListContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::ListContents, which stays Python's own.

    items : qdesigner_internal.ListContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::ListContents, which stays Python's own.
    """
    #  void qdesigner_internal::ChangeListContentsCommand::init(QComboBox
    #      *comboBox, const ListContents &oldItems, const ListContents
    #      &items)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ChangeListContentsCommand4initEP9QC'
        'omboBoxRKNS_12ListContentsES5_',
        self._addressOf(comboBox), self._valueOf(oldItems),
        self._valueOf(items),
    )

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeListContentsCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelistcontentscommand.html
    """
    #  void qdesigner_internal::ChangeListContentsCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal25ChangeListContentsCommand4redoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal25ChangeListContentsCommand4red'
          'oEv')
    self.uglySide.call(ritual)

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ChangeListContentsCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-changelistcontentscommand.html
    """
    #  void qdesigner_internal::ChangeListContentsCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal25ChangeListContentsCommand4undoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal25ChangeListContentsCommand4und'
          'oEv')
    self.uglySide.call(ritual)
