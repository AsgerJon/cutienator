"""
QScxmlExecutableContent::Send binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlExecutableContent::Send to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QScxmlExecutableContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Send(QScxmlExecutableContent.Instruction):
  """
  The cute side of Qt's QScxmlExecutableContent::Send: a plain Python object
  standing in front of one C++ QScxmlExecutableContent::Send.

  It is built on the cute 'QScxmlExecutableContent::Instruction', as Qt's
  QScxmlExecutableContent::Send is built on Qt's
  QScxmlExecutableContent::Instruction, and has everything that class has.

  C++ hands a QScxmlExecutableContent::Send around as a copy, so every C++
  QScxmlExecutableContent::Send behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QScxmlExecutableContent::Send that has a ritual and
  that Python can call so far, 4 names in all: 'kind', 'paramsOffset',
  'size', 'calculateExtraSize'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlExecutableContent::Send::~Send()': the destructor: Python
    removes its C++ QScxmlExecutableContent::Send by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QScxmlExecutableContent::Send is created at the first use, not by
    'QScxmlExecutableContent::Send(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlExecutableContent::Send back gives a copy the
    ritual made for Python, in a new cute QScxmlExecutableContent::Send.
  - Each name of Qt's QScxmlExecutableContent::Send that has no cute function
    yet, 'params', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def kind() -> QScxmlExecutableContent.Instruction.InstructionType:
    """
    Calls Qt's 'InstructionType QScxmlExecutableContent::Send::kind()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-send.html#kind

    Returns
    -------

    QScxmlExecutableContent.Instruction.InstructionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QScxmlExecutableContent.Instruction.InstructionType(number)' gives.
    """
    #  InstructionType QScxmlExecutableContent::Send::kind()
    return QScxmlExecutableContent.Instruction.InstructionType(Rituals.call(
        'ritual_ZN23QScxmlExecutableContent4Send4kindEv',
    ))

  @staticmethod
  @overload(int, int)
  def calculateExtraSize(paramCount: int, nameCount: int) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::Send::calculateExtraSize(int
    paramCount, int nameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-send.html

    Parameters
    ----------

    paramCount : int
      Passed on as it is.

    nameCount : int
      Passed on as it is.
    """
    #  int QScxmlExecutableContent::Send::calculateExtraSize(int paramCount,
    #      int nameCount)
    return Rituals.call(
        'ritual_ZN23QScxmlExecutableContent4Send18calculateExtraSizeEii',
        paramCount, nameCount,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlExecutableContent::Send'

  #  Qt's '~QScxmlExecutableContent::Send()'. Naming it makes this a value
  #  class: Python owns every C++ QScxmlExecutableContent::Send behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QScxmlExecutableContent4SendD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def paramsOffset(self) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::Send::paramsOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-send.html#paramsOffset
    """
    #  int QScxmlExecutableContent::Send::paramsOffset() const
    return self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent4Send12paramsOffsetEv',
    )

  def size(self) -> int:
    """
    Calls Qt's 'int QScxmlExecutableContent::Send::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlexecutablecontent-send.html#size
    """
    #  int QScxmlExecutableContent::Send::size() const
    return self.uglySide.call(
        'ritual_ZNK23QScxmlExecutableContent4Send4sizeEv',
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
  def params(*__, **_) -> Never:
    """
    - Qt's 'const Array<ParameterInfo>
      *QScxmlExecutableContent::Send::params() const': the compiler refuses
      its ritual as it would be written here: no template named 'Array'; did
      you mean 'QScxmlExecutableContent::Array'?.
    - Qt's 'Array<ParameterInfo> *QScxmlExecutableContent::Send::params()':
      the compiler refuses its ritual as it would be written here: no
      template named 'Array'; did you mean 'QScxmlExecutableContent::Array'?.
    """
    raise NotImplementedError(
        "'QScxmlExecutableContent.Send.params' has no cute function yet. "
        "Qt's 'const Array<ParameterInfo> "
        "*QScxmlExecutableContent::Send::params() const': the compiler "
        "refuses its ritual as it would be written here: no template named "
        "'Array'; did you mean 'QScxmlExecutableContent::Array'?. Qt's "
        "'Array<ParameterInfo> *QScxmlExecutableContent::Send::params()': "
        "the compiler refuses its ritual as it would be written here: no "
        "template named 'Array'; did you mean "
        "'QScxmlExecutableContent::Array'?.")
