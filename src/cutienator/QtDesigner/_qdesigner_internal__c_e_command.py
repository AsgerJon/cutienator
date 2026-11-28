"""
qdesigner_internal::CECommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::CECommand to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QUndoCommand
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CECommand(QUndoCommand, qdesigner_internal.CETypes):
  """
  The cute side of Qt's qdesigner_internal::CECommand: a plain Python object
  standing in front of one C++ qdesigner_internal::CECommand.

  It is built on the cute 'QUndoCommand', as Qt's
  qdesigner_internal::CECommand is built on Qt's QUndoCommand, and has
  everything that class has. It is built on the cute
  'qdesigner_internal::CETypes' as well, as Qt's
  qdesigner_internal::CECommand is built on Qt's qdesigner_internal::CETypes
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::CECommand that has a ritual and
  that Python can call so far, 2 names in all: 'mergeWith', 'edit'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::CECommand is created at the first use, not by
    'qdesigner_internal::CECommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::CECommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::CECommand'

  #  Qt's qdesigner_internal::CECommand is built on more than one class. The
  #  part of a C++ qdesigner_internal::CECommand that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'qdesigner_internal::CETypes':
          'ritual_cast_qdesigner_internal_CECommand_qdesigner_internal_CETypes',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def edit(self) -> Optional[qdesigner_internal.ConnectionEdit]:
    """
    Calls Qt's 'ConnectionEdit *qdesigner_internal::CECommand::edit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-cecommand.html#edit

    Returns
    -------

    Optional[qdesigner_internal.ConnectionEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ConnectionEdit *qdesigner_internal::CECommand::edit() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9CECommand4editEv',
    )
    return qdesigner_internal.ConnectionEdit._cuteAt(address)

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

  @overload(WAIT['qdesigner_internal.ConnectionEdit'])
  @overload(NoneType)
  def __init__(
      self,
      edit: Optional[qdesigner_internal.ConnectionEdit],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::CECommand::CECommand(ConnectionEdit *edit)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-cecommand.html#CECommand

    Parameters
    ----------

    edit : Optional[qdesigner_internal.ConnectionEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::CECommand::CECommand(ConnectionEdit *edit)
    self._noteCreation(CECommand, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal9CECommandC1EPNS_14ConnectionEditE',
        self._addressOf(edit),
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

  @overload(QUndoCommand)
  @overload(NoneType)
  def mergeWith(self, a0: Optional[QUndoCommand]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::CECommand::mergeWith(const
    QUndoCommand *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-cecommand.html#mergeWith

    Parameters
    ----------

    a0 : Optional[QUndoCommand]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::CECommand::mergeWith(const QUndoCommand *a0)
    ritual = (
        'ritual_ZN18qdesigner_internal9CECommand9mergeWithEPK12QUndoCommand')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal9CECommand9mergeWithEPK12QUndoC'
          'ommand')
    return self.uglySide.call(ritual, self._addressOf(a0))
