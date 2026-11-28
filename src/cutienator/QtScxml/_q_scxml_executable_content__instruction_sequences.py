"""
QScxmlExecutableContent::InstructionSequences binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::InstructionSequences to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..occult import Rituals
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class InstructionSequences(QScxmlExecutableContent.Instruction):
  """
  The cute side of Qt's QScxmlExecutableContent::InstructionSequences: a
  plain Python object standing in front of one C++
  QScxmlExecutableContent::InstructionSequences.

  It is built on the cute 'QScxmlExecutableContent::Instruction', as Qt's
  QScxmlExecutableContent::InstructionSequences is built on Qt's
  QScxmlExecutableContent::Instruction, and has everything that class has.

  C++ hands a QScxmlExecutableContent::InstructionSequences around as a copy,
  so every C++ QScxmlExecutableContent::InstructionSequences behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScxmlExecutableContent::InstructionSequences that
  has a ritual and that Python can call so far, 3 names in all: 'kind',
  'sequences', 'size'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const InstructionId
    *QScxmlExecutableContent::InstructionSequences::at(int pos) const': gives
    'int', which has no cute class yet.
  - Qt's
    'QScxmlExecutableContent::InstructionSequences::~InstructionSequences()':
    the destructor: Python removes its C++
    QScxmlExecutableContent::InstructionSequences by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::InstructionSequences is created at the
    first use, not by 'QScxmlExecutableContent::InstructionSequences(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::InstructionSequences back
    gives a copy the ritual made for Python, in a new cute
    QScxmlExecutableContent::InstructionSequences.
  - Each name of Qt's QScxmlExecutableContent::InstructionSequences that has
    no cute function yet, 'at', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def kind() -> QScxmlExecutableContent.Instruction.InstructionType:
    """
    Calls Qt's 'InstructionType
    QScxmlExecutableContent::InstructionSequences::kind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-instructionsequences.html

    Returns
    -------

    QScxmlExecutableContent.Instruction.InstructionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QScxmlExecutableContent.Instruction.InstructionType(number)' gives.
    """
    #  InstructionType QScxmlExecutableContent::InstructionSequences::kind()
    return QScxmlExecutableContent.Instruction.InstructionType(Rituals.call(
        'ritual_ZN23QScxmlExecutableContent20InstructionSequences4kindEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutableContent::InstructionSequences'

  #  Qt's '~QScxmlExecutableContent::InstructionSequences()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QScxmlExecutableContent::InstructionSequences behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN23QScxmlExecutableContent20InstructionSequencesD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sequences(
      self,
  ) -> Optional[QScxmlExecutableContent.InstructionSequence]:
    """
    Calls Qt's 'const InstructionSequence
    *QScxmlExecutableContent::InstructionSequences::sequences() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-instructionsequences.html

    Returns
    -------

    Optional[QScxmlExecutableContent.InstructionSequence]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const InstructionSequence
    #      *QScxmlExecutableContent::InstructionSequences::sequences() const
    address = self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent20InstructionSequences9sequence'
        'sEv',
    )
    return QScxmlExecutableContent.InstructionSequence._cuteAt(address)

  def size(self) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::InstructionSequences::size()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-instructionsequences.html
    """
    #  int QScxmlExecutableContent::InstructionSequences::size() const
    return self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent20InstructionSequences4sizeEv',
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

  @staticmethod
  def at(*__, **_) -> Never:
    """
    Qt's 'const InstructionId
    *QScxmlExecutableContent::InstructionSequences::at(int pos) const': gives
    'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScxmlExecutableContent.InstructionSequences.at' has no cute "
        "function yet. Qt's 'const InstructionId "
        "*QScxmlExecutableContent::InstructionSequences::at(int pos) "
        "const': gives 'int', which has no cute class yet.")
