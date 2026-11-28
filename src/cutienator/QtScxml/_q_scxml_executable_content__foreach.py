"""
QScxmlExecutableContent::Foreach binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::Foreach to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Foreach(QScxmlExecutableContent.Instruction):
  """
  The cute side of Qt's QScxmlExecutableContent::Foreach: a plain Python
  object standing in front of one C++ QScxmlExecutableContent::Foreach.

  It is built on the cute 'QScxmlExecutableContent::Instruction', as Qt's
  QScxmlExecutableContent::Foreach is built on Qt's
  QScxmlExecutableContent::Instruction, and has everything that class has.

  C++ hands a QScxmlExecutableContent::Foreach around as a copy, so every C++
  QScxmlExecutableContent::Foreach behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QScxmlExecutableContent::Foreach that has a ritual
  and that Python can call so far, 2 names in all: 'kind', 'size'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const InstructionId *QScxmlExecutableContent::Foreach::blockstart()
    const': gives 'int', which has no cute class yet.
  - Qt's 'QScxmlExecutableContent::Foreach::~Foreach()': the destructor:
    Python removes its C++ QScxmlExecutableContent::Foreach by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::Foreach is created at the first use, not
    by 'QScxmlExecutableContent::Foreach(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::Foreach back gives a copy
    the ritual made for Python, in a new cute
    QScxmlExecutableContent::Foreach.
  - Each name of Qt's QScxmlExecutableContent::Foreach that has no cute
    function yet, 'blockstart', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def kind() -> QScxmlExecutableContent.Instruction.InstructionType:
    """
    Calls Qt's 'InstructionType QScxmlExecutableContent::Foreach::kind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-foreach.html#kind

    Returns
    -------

    QScxmlExecutableContent.Instruction.InstructionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QScxmlExecutableContent.Instruction.InstructionType(number)' gives.
    """
    #  InstructionType QScxmlExecutableContent::Foreach::kind()
    return QScxmlExecutableContent.Instruction.InstructionType(Rituals.call(
        'ritual_ZN23QScxmlExecutableContent7Foreach4kindEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutableContent::Foreach'

  #  Qt's '~QScxmlExecutableContent::Foreach()'. Naming it makes this a value
  #  class: Python owns every C++ QScxmlExecutableContent::Foreach behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QScxmlExecutableContent7ForeachD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::Foreach::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-foreach.html#size
    """
    #  int QScxmlExecutableContent::Foreach::size() const
    return self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent7Foreach4sizeEv',
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
  def blockstart(*__, **_) -> Never:
    """
    Qt's 'const InstructionId *QScxmlExecutableContent::Foreach::blockstart()
    const': gives 'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QScxmlExecutableContent.Foreach.blockstart' has no cute function "
        "yet. Qt's 'const InstructionId "
        "*QScxmlExecutableContent::Foreach::blockstart() const': gives "
        "'int', which has no cute class yet.")
