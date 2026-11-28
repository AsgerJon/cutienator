"""
QTextUndoCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextUndoCommand to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute


class QTextUndoCommand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextUndoCommand: a plain Python object standing in
  front of one C++ QTextUndoCommand.

  C++ hands a QTextUndoCommand around as a copy, so every C++
  QTextUndoCommand behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextUndoCommand that has a ritual and that Python
  can call so far, 1 name in all: 'tryMerge'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextUndoCommand::~QTextUndoCommand()': the destructor: Python
    removes its C++ QTextUndoCommand by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextUndoCommand is created at the first use, not by
    'QTextUndoCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextUndoCommand back gives a copy the ritual made
    for Python, in a new cute QTextUndoCommand.
  """

  #  The enums Qt writes inside QTextUndoCommand, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Command(CuteNum):
    """
    The enum 'QTextUndoCommand::Command' of Qt, with the 11 names Qt gives in
    it.
    """

    Inserted = Kee[int](0)
    Removed = Kee[int](1)
    CharFormatChanged = Kee[int](2)
    BlockFormatChanged = Kee[int](3)
    BlockInserted = Kee[int](4)
    BlockRemoved = Kee[int](5)
    BlockAdded = Kee[int](6)
    BlockDeleted = Kee[int](7)
    GroupFormatChange = Kee[int](8)
    CursorMoved = Kee[int](9)
    Custom = Kee[int](256)

  class Operation(CuteNum):
    """
    The enum 'QTextUndoCommand::Operation' of Qt, with the 2 names Qt gives
    in it.
    """

    KeepCursor = Kee[int](0)
    MoveCursor = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextUndoCommand'

  #  Qt's '~QTextUndoCommand()'. Naming it makes this a value class: Python
  #  owns every C++ QTextUndoCommand behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTextUndoCommandD1Ev'

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

  @overload(THIS)
  def tryMerge(self, other: QTextUndoCommand) -> bool:
    """
    Calls Qt's 'bool QTextUndoCommand::tryMerge(const QTextUndoCommand
    &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextundocommand.html#tryMerge

    Parameters
    ----------

    other : QTextUndoCommand
      Passed on as a value: Qt reads the C++ QTextUndoCommand, which stays
      Python's own.
    """
    #  bool QTextUndoCommand::tryMerge(const QTextUndoCommand &other)
    return self.uglySide.call(
        'ritual_ZN16QTextUndoCommand8tryMergeERKS_', self._valueOf(other),
    )
