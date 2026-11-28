"""
QScxmlExecutableContent::If binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::If to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..occult import Rituals
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class If(QScxmlExecutableContent.Instruction):
  """
  The cute side of Qt's QScxmlExecutableContent::If: a plain Python object
  standing in front of one C++ QScxmlExecutableContent::If.

  It is built on the cute 'QScxmlExecutableContent::Instruction', as Qt's
  QScxmlExecutableContent::If is built on Qt's
  QScxmlExecutableContent::Instruction, and has everything that class has.

  C++ hands a QScxmlExecutableContent::If around as a copy, so every C++
  QScxmlExecutableContent::If behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QScxmlExecutableContent::If that has a ritual and
  that Python can call so far, 3 names in all: 'blocks', 'kind', 'size'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlExecutableContent::If::~If()': the destructor: Python removes
    its C++ QScxmlExecutableContent::If by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::If is created at the first use, not by
    'QScxmlExecutableContent::If(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::If back gives a copy the
    ritual made for Python, in a new cute QScxmlExecutableContent::If.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def kind() -> QScxmlExecutableContent.Instruction.InstructionType:
    """
    Calls Qt's 'InstructionType QScxmlExecutableContent::If::kind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-if.html#kind

    Returns
    -------

    QScxmlExecutableContent.Instruction.InstructionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QScxmlExecutableContent.Instruction.InstructionType(number)' gives.
    """
    #  InstructionType QScxmlExecutableContent::If::kind()
    return QScxmlExecutableContent.Instruction.InstructionType(Rituals.call(
        'ritual_ZN23QScxmlExecutableContent2If4kindEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutableContent::If'

  #  Qt's '~QScxmlExecutableContent::If()'. Naming it makes this a value
  #  class: Python owns every C++ QScxmlExecutableContent::If behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QScxmlExecutableContent2IfD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def blocks(self) -> Optional[QScxmlExecutableContent.InstructionSequences]:
    """
    Calls Qt's 'const InstructionSequences
    *QScxmlExecutableContent::If::blocks() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-if.html#blocks

    Returns
    -------

    Optional[QScxmlExecutableContent.InstructionSequences]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const InstructionSequences *QScxmlExecutableContent::If::blocks()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent2If6blocksEv',
    )
    return QScxmlExecutableContent.InstructionSequences._cuteAt(address)

  def size(self) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::If::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-if.html#size
    """
    #  int QScxmlExecutableContent::If::size() const
    return self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent2If4sizeEv',
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
