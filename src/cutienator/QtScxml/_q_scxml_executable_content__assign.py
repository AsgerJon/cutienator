"""
QScxmlExecutableContent::Assign binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::Assign to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from . import QScxmlExecutableContent


class Assign(QScxmlExecutableContent.Instruction):
  """
  The cute side of Qt's QScxmlExecutableContent::Assign: a plain Python
  object standing in front of one C++ QScxmlExecutableContent::Assign.

  It is built on the cute 'QScxmlExecutableContent::Instruction', as Qt's
  QScxmlExecutableContent::Assign is built on Qt's
  QScxmlExecutableContent::Instruction, and has everything that class has.

  C++ hands a QScxmlExecutableContent::Assign around as a copy, so every C++
  QScxmlExecutableContent::Assign behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QScxmlExecutableContent::Assign that has a ritual
  and that Python can call so far, 2 names in all: 'kind', 'size'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlExecutableContent::Assign::~Assign()': the destructor: Python
    removes its C++ QScxmlExecutableContent::Assign by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::Assign is created at the first use, not
    by 'QScxmlExecutableContent::Assign(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::Assign back gives a copy the
    ritual made for Python, in a new cute QScxmlExecutableContent::Assign.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def kind() -> QScxmlExecutableContent.Instruction.InstructionType:
    """
    Calls Qt's 'InstructionType QScxmlExecutableContent::Assign::kind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-assign.html#kind

    Returns
    -------

    QScxmlExecutableContent.Instruction.InstructionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QScxmlExecutableContent.Instruction.InstructionType(number)' gives.
    """
    #  InstructionType QScxmlExecutableContent::Assign::kind()
    return QScxmlExecutableContent.Instruction.InstructionType(Rituals.call(
        'ritual_ZN23QScxmlExecutableContent6Assign4kindEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutableContent::Assign'

  #  Qt's '~QScxmlExecutableContent::Assign()'. Naming it makes this a value
  #  class: Python owns every C++ QScxmlExecutableContent::Assign behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QScxmlExecutableContent6AssignD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::Assign::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-assign.html#size
    """
    #  int QScxmlExecutableContent::Assign::size() const
    return self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent6Assign4sizeEv',
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
