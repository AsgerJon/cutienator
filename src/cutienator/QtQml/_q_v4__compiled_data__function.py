"""
QV4::CompiledData::Function binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Function to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class Function(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Function: a plain Python object
  standing in front of one C++ QV4::CompiledData::Function.

  C++ hands a QV4::CompiledData::Function around as a copy, so every C++
  QV4::CompiledData::Function behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Function that has a ritual and
  that Python can call so far, 9 names in all:
  'lineAndStatementNumberOffset', 'labelInfosOffset', 'formalsTable',
  'lineAndStatementNumberTable', 'formalsBegin', 'formalsEnd', 'code',
  'calculateSize', 'align'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const quint32_le *QV4::CompiledData::Function::localsTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'const quint32_le *QV4::CompiledData::Function::labelInfoTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'QV4::CompiledData::Function::~Function()': the destructor: Python
    removes its C++ QV4::CompiledData::Function by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Function is created at the first use, not by
    'QV4::CompiledData::Function(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Function back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::Function.
  - Each name of Qt's QV4::CompiledData::Function that has no cute function
    yet, 'labelInfoTable', 'localsTable', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::CompiledData::Function, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flags(CuteNum):
    """
    The enum 'QV4::CompiledData::Function::Flags' of Qt, with the 4 names Qt
    gives in it.
    """

    IsStrict = Kee[int](1)
    IsArrowFunction = Kee[int](2)
    IsGenerator = Kee[int](4)
    IsClosureWrapper = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int, int, int, int)
  def calculateSize(
      nFormals: int,
      nLocals: int,
      nLinesAndStatements: int,
      labelInfoSize: int,
      codeSize: int,
  ) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Function::calculateSize(int nFormals,
    int nLocals, int nLinesAndStatements, int labelInfoSize, int codeSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#calculateSize

    Parameters
    ----------

    nFormals : int
      Passed on as it is.

    nLocals : int
      Passed on as it is.

    nLinesAndStatements : int
      Passed on as it is.

    labelInfoSize : int
      Passed on as it is.

    codeSize : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::Function::calculateSize(int nFormals, int
    #      nLocals, int nLinesAndStatements, int labelInfoSize, int codeSize)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData8Function13calculateSizeEiiiii',
        nFormals, nLocals, nLinesAndStatements, labelInfoSize, codeSize,
    )

  @staticmethod
  @overload(int)
  def align(a: int) -> int:
    """
    Calls Qt's 'size_t QV4::CompiledData::Function::align(size_t a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#align

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  size_t QV4::CompiledData::Function::align(size_t a)
    return Rituals.call('ritual_ZN3QV412CompiledData8Function5alignEm', a)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Function'

  #  Qt's '~QV4::CompiledData::Function()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::Function behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData8FunctionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lineAndStatementNumberOffset(self) -> int:
    """
    Calls Qt's 'size_t
    QV4::CompiledData::Function::lineAndStatementNumberOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html
    """
    #  size_t QV4::CompiledData::Function::lineAndStatementNumberOffset()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function28lineAndStatementNumberOffse'
        'tEv',
    )

  def labelInfosOffset(self) -> int:
    """
    Calls Qt's 'size_t QV4::CompiledData::Function::labelInfosOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#labelInfosOffset
    """
    #  size_t QV4::CompiledData::Function::labelInfosOffset() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function16labelInfosOffsetEv',
    )

  def formalsTable(self) -> Optional[QV4.CompiledData.Parameter]:
    """
    Calls Qt's 'const Parameter *QV4::CompiledData::Function::formalsTable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#formalsTable

    Returns
    -------

    Optional[QV4.CompiledData.Parameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Parameter *QV4::CompiledData::Function::formalsTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function12formalsTableEv',
    )
    return QV4.CompiledData.Parameter._cuteAt(address)

  def lineAndStatementNumberTable(
      self,
  ) -> Optional[QV4.CompiledData.CodeOffsetToLineAndStatement]:
    """
    Calls Qt's 'const CodeOffsetToLineAndStatement
    *QV4::CompiledData::Function::lineAndStatementNumberTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html

    Returns
    -------

    Optional[QV4.CompiledData.CodeOffsetToLineAndStatement]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const CodeOffsetToLineAndStatement
    #      *QV4::CompiledData::Function::lineAndStatementNumberTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function27lineAndStatementNumberTable'
        'Ev',
    )
    return QV4.CompiledData.CodeOffsetToLineAndStatement._cuteAt(address)

  def formalsBegin(self) -> Optional[QV4.CompiledData.Parameter]:
    """
    Calls Qt's 'const Parameter *QV4::CompiledData::Function::formalsBegin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#formalsBegin

    Returns
    -------

    Optional[QV4.CompiledData.Parameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Parameter *QV4::CompiledData::Function::formalsBegin() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function12formalsBeginEv',
    )
    return QV4.CompiledData.Parameter._cuteAt(address)

  def formalsEnd(self) -> Optional[QV4.CompiledData.Parameter]:
    """
    Calls Qt's 'const Parameter *QV4::CompiledData::Function::formalsEnd()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#formalsEnd

    Returns
    -------

    Optional[QV4.CompiledData.Parameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Parameter *QV4::CompiledData::Function::formalsEnd() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function10formalsEndEv',
    )
    return QV4.CompiledData.Parameter._cuteAt(address)

  def code(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QV4::CompiledData::Function::code() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-function.html#code

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::CompiledData::Function::code() const
    chars = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Function4codeEv',
    )
    return None if chars is None else chars.decode()

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
  def labelInfoTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Function::labelInfoTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Function.labelInfoTable' has no cute function "
        "yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Function::labelInfoTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")

  @staticmethod
  def localsTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Function::localsTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Function.localsTable' has no cute function yet. "
        "Qt's 'const quint32_le *QV4::CompiledData::Function::localsTable() "
        "const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned "
        "int>>', which has no cute class yet.")
