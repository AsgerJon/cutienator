"""
qdesigner_internal::QDesignerFormWindowCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formwindowcommand_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerFormWindowCommand to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QUndoCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
  from . import QDesignerPropertySheetExtension
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormWindowCommand(QUndoCommand):
  """
  The cute side of Qt's qdesigner_internal::QDesignerFormWindowCommand: a
  plain Python object standing in front of one C++
  qdesigner_internal::QDesignerFormWindowCommand.

  It is built on the cute 'QUndoCommand', as Qt's
  qdesigner_internal::QDesignerFormWindowCommand is built on Qt's
  QUndoCommand, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerFormWindowCommand that
  has a ritual and that Python can call so far, 8 names in all: 'undo',
  'redo', 'updateBuddies', 'formWindow', 'core', 'propertySheet',
  'cheapUpdate', 'selectUnmanagedObject'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerFormWindowCommand is created at the
    first use, not by 'qdesigner_internal::QDesignerFormWindowCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::QDesignerFormWindowCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerFormWindowInterface, str, str)
  @overload(NoneType, str, str)
  def updateBuddies(
      form: Optional[QDesignerFormWindowInterface],
      old_name: str,
      new_name: str,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormWindowCommand::updateBuddies(
    QDesignerFormWindowInterface *form, const QString &old_name, const
    QString &new_name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html

    Parameters
    ----------

    form : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    old_name : str
      Passed on as it is: a QString is made of it for the call.

    new_name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::QDesignerFormWindowCommand::updateBuddies(
    #      QDesignerFormWindowInterface *form, const QString &old_name, const
    #      QString &new_name)
    Rituals.call(
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand13updateB'
        'uddiesEP28QDesignerFormWindowInterfaceRK7QStringS5_',
        CuteMixin._addressOf(form), old_name, new_name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerFormWindowCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::QDesignerFormWindowCommand::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::QDesignerFormWindowCommand::formWindow()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal26QDesignerFormWindowCommand10formWi'
        'ndowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::QDesignerFormWindowCommand::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *qdesigner_internal::QDesignerFormWindowCommand::core() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal26QDesignerFormWindowCommand4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def propertySheet(
      self,
      object: Optional[QObject],
  ) -> Optional[QDesignerPropertySheetExtension]:
    """
    Calls Qt's 'QDesignerPropertySheetExtension
    *qdesigner_internal::QDesignerFormWindowCommand::propertySheet(QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerPropertySheetExtension]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerPropertySheetExtension
    #      *qdesigner_internal::QDesignerFormWindowCommand::propertySheet(
    #      QObject *object) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal26QDesignerFormWindowCommand13proper'
        'tySheetEP7QObject',
        self._addressOf(object, 'QObject'),
    )
    from . import QDesignerPropertySheetExtension
    return QDesignerPropertySheetExtension._cuteAt(address)

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
  @overload(str, QDesignerFormWindowInterface, QUndoCommand)
  @overload(str, QDesignerFormWindowInterface, NoneType)
  @overload(str, NoneType, QUndoCommand)
  @overload(str, NoneType, NoneType)
  def __init__(
      self,
      description: str,
      formWindow: Optional[QDesignerFormWindowInterface],
      parent: Optional[QUndoCommand] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerFormWindowCommand::
    QDesignerFormWindowCommand(const QString &description,
    QDesignerFormWindowInterface *formWindow, QUndoCommand *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QUndoCommand]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::QDesignerFormWindowCommand::
    #      QDesignerFormWindowCommand(const QString &description,
    #      QDesignerFormWindowInterface *formWindow, QUndoCommand *parent)
    self._noteCreation(QDesignerFormWindowCommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowCommandC1ERK7QSt'
        'ringP28QDesignerFormWindowInterfaceP12QUndoCommand',
        description, self._addressOf(formWindow), self._addressOf(parent),
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

  def undo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerFormWindowCommand::undo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html
    """
    #  void qdesigner_internal::QDesignerFormWindowCommand::undo()
    ritual = (
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand4undoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal26QDesignerFormWindowCommand4un'
          'doEv')
    self.uglySide.call(ritual)

  def redo(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerFormWindowCommand::redo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html
    """
    #  void qdesigner_internal::QDesignerFormWindowCommand::redo()
    ritual = (
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand4redoEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal26QDesignerFormWindowCommand4re'
          'doEv')
    self.uglySide.call(ritual)

  def cheapUpdate(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormWindowCommand::cheapUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html
    """
    #  void qdesigner_internal::QDesignerFormWindowCommand::cheapUpdate()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand11cheapUp'
        'dateEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def selectUnmanagedObject(
      self,
      unmanagedObject: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormWindowCommand::selectUnmanagedObject(
    QObject *unmanagedObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowcommand.html

    Parameters
    ----------

    unmanagedObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerFormWindowCommand::
    #      selectUnmanagedObject(QObject *unmanagedObject)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowCommand21selectU'
        'nmanagedObjectEP7QObject',
        self._addressOf(unmanagedObject, 'QObject'),
    )
