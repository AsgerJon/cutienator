"""
QV4::Compiler::JSUnitGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Compiler::JSUnitGenerator to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QQmlJS, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JSUnitGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Compiler::JSUnitGenerator: a plain Python object
  standing in front of one C++ QV4::Compiler::JSUnitGenerator.

  C++ hands a QV4::Compiler::JSUnitGenerator around as a copy, so every C++
  QV4::Compiler::JSUnitGenerator behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::JSUnitGenerator that has a ritual and
  that Python can call so far, 19 names in all: 'generateUnitChecksum',
  'registerString', 'getStringId', 'hasStringId', 'stringForIndex',
  'registerGetterLookup', 'registerSetterLookup',
  'registerGlobalGetterLookup', 'registerQmlContextPropertyGetterLookup',
  'lookupNameIndex', 'lookupName', 'registerRegExp', 'registerConstant',
  'constant', 'registerJSClass', 'jsClassSize', 'jsClassMember',
  'registerTranslation', 'generateUnit'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Compiler::JSUnitGenerator::writeFunction(char *f, Context
    *irFunction) const': names 'char', which has no cute class yet.
  - Qt's 'void QV4::Compiler::JSUnitGenerator::writeClass(char *f, const
    Class &c)': names 'char', which has no cute class yet.
  - Qt's 'void QV4::Compiler::JSUnitGenerator::writeTemplateObject(char *f,
    const TemplateObject &o)': names 'char', which has no cute class yet.
  - Qt's 'void QV4::Compiler::JSUnitGenerator::writeBlock(char *f, Context
    *irBlock) const': names 'char', which has no cute class yet.
  - Qt's 'CompiledData::Unit
    QV4::Compiler::JSUnitGenerator::generateHeader(GeneratorOption option,
    quint32_le *functionOffsets, uint *jsClassDataOffset)': names
    'quint32_le', which has no cute class yet.
  - Qt's 'QV4::Compiler::JSUnitGenerator::~JSUnitGenerator()': the
    destructor: Python removes its C++ QV4::Compiler::JSUnitGenerator by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Compiler::JSUnitGenerator is created at the first use, not
    by 'QV4::Compiler::JSUnitGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::JSUnitGenerator back gives a copy the
    ritual made for Python, in a new cute QV4::Compiler::JSUnitGenerator.
  - Each name of Qt's QV4::Compiler::JSUnitGenerator that has no cute
    function yet, 'generateHeader', 'writeBlock', 'writeClass',
    'writeFunction', 'writeTemplateObject', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Compiler::JSUnitGenerator, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class GeneratorOption(CuteNum):
    """
    The enum 'QV4::Compiler::JSUnitGenerator::GeneratorOption' of Qt, with
    the 2 names Qt gives in it.
    """

    GenerateWithStringTable = Kee[int](0)
    GenerateWithoutStringTable = Kee[int](1)

  class LookupMode(CuteNum):
    """
    The enum 'QV4::Compiler::JSUnitGenerator::LookupMode' of Qt, with the 2
    names Qt gives in it.
    """

    LookupForStorage = Kee[int](0)
    LookupForCall = Kee[int](1)

  #  The classes Qt writes inside QV4::Compiler::JSUnitGenerator, each a
  #  class in here as in C++.

  class MemberInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Compiler::JSUnitGenerator::MemberInfo: a plain
    Python object standing in front of one C++
    QV4::Compiler::JSUnitGenerator::MemberInfo.

    C++ hands a QV4::Compiler::JSUnitGenerator::MemberInfo around as a copy,
    so every C++ QV4::Compiler::JSUnitGenerator::MemberInfo behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QV4::Compiler::JSUnitGenerator::MemberInfo yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Compiler::JSUnitGenerator::MemberInfo::~MemberInfo()': the
      destructor: Python removes its C++
      QV4::Compiler::JSUnitGenerator::MemberInfo by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::Compiler::JSUnitGenerator::MemberInfo is created at the
      first use, not by 'QV4::Compiler::JSUnitGenerator::MemberInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Compiler::JSUnitGenerator::MemberInfo back
      gives a copy the ritual made for Python, in a new cute
      QV4::Compiler::JSUnitGenerator::MemberInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Compiler::JSUnitGenerator::MemberInfo'

    #  Qt's '~QV4::Compiler::JSUnitGenerator::MemberInfo()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::Compiler::JSUnitGenerator::MemberInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV48Compiler15JSUnitGenerator10MemberInfoD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.CompiledData.Unit'])
  @overload(NoneType)
  def generateUnitChecksum(unit: Optional[QV4.CompiledData.Unit]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::JSUnitGenerator::generateUnitChecksum(CompiledData::Unit
    *unit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    unit : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::JSUnitGenerator::generateUnitChecksum(
    #      CompiledData::Unit *unit)
    Rituals.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator20generateUnitChecksumEPNS_'
        '12CompiledData4UnitE',
        CuteMixin._addressOf(unit),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::JSUnitGenerator'

  #  Qt's '~QV4::Compiler::JSUnitGenerator()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::Compiler::JSUnitGenerator behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler15JSUnitGeneratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def getStringId(self, string: str) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::getStringId(const QString
    &string) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#getStringId

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::Compiler::JSUnitGenerator::getStringId(const QString &string)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator11getStringIdERK7QString',
        string,
    )

  @overload(str)
  def hasStringId(self, string: str) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::JSUnitGenerator::hasStringId(const
    QString &string) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#hasStringId

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::Compiler::JSUnitGenerator::hasStringId(const QString
    #      &string) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator11hasStringIdERK7QString',
        string,
    )

  @overload(int)
  def stringForIndex(self, index: int) -> str:
    """
    Calls Qt's 'QString QV4::Compiler::JSUnitGenerator::stringForIndex(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#stringForIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::JSUnitGenerator::stringForIndex(int index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator14stringForIndexEi', index,
    )

  @overload(int)
  def lookupNameIndex(self, index: int) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::lookupNameIndex(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#lookupNameIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QV4::Compiler::JSUnitGenerator::lookupNameIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator15lookupNameIndexEi', index,
    )

  @overload(int)
  def lookupName(self, index: int) -> str:
    """
    Calls Qt's 'QString QV4::Compiler::JSUnitGenerator::lookupName(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#lookupName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::JSUnitGenerator::lookupName(int index) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator10lookupNameEi', index,
    )

  @overload(int)
  def constant(self, idx: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Compiler::JSUnitGenerator::constant(int
    idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#constant

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::Compiler::JSUnitGenerator::constant(int idx) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator8constantEi', idx,
    )

  @overload(int)
  def jsClassSize(self, jsClassId: int) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::jsClassSize(int
    jsClassId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#jsClassSize

    Parameters
    ----------

    jsClassId : int
      Passed on as it is.
    """
    #  int QV4::Compiler::JSUnitGenerator::jsClassSize(int jsClassId) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator11jsClassSizeEi', jsClassId,
    )

  @overload(int, int)
  def jsClassMember(self, jsClassId: int, member: int) -> str:
    """
    Calls Qt's 'QString QV4::Compiler::JSUnitGenerator::jsClassMember(int
    jsClassId, int member) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#jsClassMember

    Parameters
    ----------

    jsClassId : int
      Passed on as it is.

    member : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::JSUnitGenerator::jsClassMember(int jsClassId,
    #      int member) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler15JSUnitGenerator13jsClassMemberEii',
        jsClassId, member,
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

  @overload(WAIT['QV4.Compiler.Module'])
  @overload(NoneType)
  def __init__(self, module: Optional[QV4.Compiler.Module]) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Compiler::JSUnitGenerator::JSUnitGenerator(Module *module)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#JSUnitGenerator

    Parameters
    ----------

    module : Optional[QV4.Compiler.Module]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Compiler::JSUnitGenerator::JSUnitGenerator(Module *module)
    self._noteCreation(JSUnitGenerator, lambda: Rituals.call(
        'ritual_ZN3QV48Compiler15JSUnitGeneratorC1EPNS0_6ModuleE',
        self._addressOf(module),
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

  @overload(str)
  def registerString(self, str: str) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::registerString(const
    QString &str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#registerString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerString(const QString &str)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator14registerStringERK7QString',
        str,
    )

  @overload(str, LookupMode)
  def registerGetterLookup(self, name: str, mode: LookupMode) -> int:
    """
    Calls Qt's 'int
    QV4::Compiler::JSUnitGenerator::registerGetterLookup(const QString &name,
    LookupMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    mode : LookupMode
      Passed on as its number.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerGetterLookup(const QString
    #      &name, LookupMode mode)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator20registerGetterLookupERK7Q'
        'StringNS1_10LookupModeE',
        name, mode.value,
    )

  @overload(int, LookupMode)
  def registerGetterLookup(self, nameIndex: int, mode: LookupMode) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::registerGetterLookup(int
    nameIndex, LookupMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    mode : LookupMode
      Passed on as its number.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerGetterLookup(int
    #      nameIndex, LookupMode mode)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator20registerGetterLookupEiNS1'
        '_10LookupModeE',
        nameIndex, mode.value,
    )

  @overload(str)
  def registerSetterLookup(self, name: str) -> int:
    """
    Calls Qt's 'int
    QV4::Compiler::JSUnitGenerator::registerSetterLookup(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerSetterLookup(const QString
    #      &name)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator20registerSetterLookupERK7Q'
        'String',
        name,
    )

  @overload(int)
  def registerSetterLookup(self, nameIndex: int) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::registerSetterLookup(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerSetterLookup(int
    #      nameIndex)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator20registerSetterLookupEi',
        nameIndex,
    )

  @overload(int, LookupMode)
  def registerGlobalGetterLookup(
      self,
      nameIndex: int,
      mode: LookupMode,
  ) -> int:
    """
    Calls Qt's 'int
    QV4::Compiler::JSUnitGenerator::registerGlobalGetterLookup(int nameIndex,
    LookupMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    mode : LookupMode
      Passed on as its number.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerGlobalGetterLookup(int
    #      nameIndex, LookupMode mode)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator26registerGlobalGetterLooku'
        'pEiNS1_10LookupModeE',
        nameIndex, mode.value,
    )

  @overload(int, LookupMode)
  def registerQmlContextPropertyGetterLookup(
      self,
      nameIndex: int,
      mode: LookupMode,
  ) -> int:
    """
    Calls Qt's 'int
    QV4::Compiler::JSUnitGenerator::registerQmlContextPropertyGetterLookup(
    int nameIndex, LookupMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    mode : LookupMode
      Passed on as its number.
    """
    #  int QV4::Compiler::JSUnitGenerator::
    #      registerQmlContextPropertyGetterLookup(int nameIndex, LookupMode
    #      mode)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator38registerQmlContextPropert'
        'yGetterLookupEiNS1_10LookupModeE',
        nameIndex, mode.value,
    )

  @overload(WAIT['QQmlJS.AST.RegExpLiteral'])
  @overload(NoneType)
  def registerRegExp(
      self,
      regexp: Optional[QQmlJS.AST.RegExpLiteral],
  ) -> int:
    """
    Calls Qt's 'int
    QV4::Compiler::JSUnitGenerator::registerRegExp(QQmlJS::AST::RegExpLiteral
    *regexp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#registerRegExp

    Parameters
    ----------

    regexp : Optional[QQmlJS.AST.RegExpLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerRegExp(QQmlJS::AST::
    #      RegExpLiteral *regexp)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator14registerRegExpEPN6QQmlJS3'
        'AST13RegExpLiteralE',
        self._addressOf(regexp),
    )

  @overload(int)
  def registerConstant(self, v: int) -> int:
    """
    Calls Qt's 'int
    QV4::Compiler::JSUnitGenerator::registerConstant(ReturnedValue v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#registerConstant

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerConstant(ReturnedValue v)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator16registerConstantEy', v,
    )

  @overload(QStringList)
  def registerJSClass(self, members: QStringList) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::registerJSClass(const
    QStringList &members)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#registerJSClass

    Parameters
    ----------

    members : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerJSClass(const QStringList
    #      &members)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator15registerJSClassERK5QListI'
        '7QStringE',
        self._valueOf(members),
    )

  @overload(WAIT['QV4.CompiledData.TranslationData'])
  def registerTranslation(
      self,
      translation: QV4.CompiledData.TranslationData,
  ) -> int:
    """
    Calls Qt's 'int QV4::Compiler::JSUnitGenerator::registerTranslation(const
    CompiledData::TranslationData &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html

    Parameters
    ----------

    translation : QV4.CompiledData.TranslationData
      Passed on as a value: Qt reads the C++
      QV4::CompiledData::TranslationData, which stays Python's own.
    """
    #  int QV4::Compiler::JSUnitGenerator::registerTranslation(const
    #      CompiledData::TranslationData &translation)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator19registerTranslationERKNS_'
        '12CompiledData15TranslationDataE',
        self._valueOf(translation),
    )

  @overload()
  @overload(GeneratorOption)
  def generateUnit(
      self,
      option: GeneratorOption = GeneratorOption.GenerateWithStringTable,
  ) -> Optional[QV4.CompiledData.Unit]:
    """
    Calls Qt's 'QV4::CompiledData::Unit
    *QV4::Compiler::JSUnitGenerator::generateUnit(GeneratorOption option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-jsunitgenerator.html#generateUnit

    Parameters
    ----------

    option : GeneratorOption
      Passed on as its number. May be left out, as in Qt: it is then
      GeneratorOption.GenerateWithStringTable.

    Returns
    -------

    Optional[QV4.CompiledData.Unit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::CompiledData::Unit
    #      *QV4::Compiler::JSUnitGenerator::generateUnit(GeneratorOption
    #      option)
    address = self.uglySide.call(
        'ritual_ZN3QV48Compiler15JSUnitGenerator12generateUnitENS1_15Genera'
        'torOptionE',
        option.value,
    )
    return QV4.CompiledData.Unit._cuteAt(address)

  @staticmethod
  def generateHeader(*__, **_) -> Never:
    """
    Qt's 'CompiledData::Unit
    QV4::Compiler::JSUnitGenerator::generateHeader(GeneratorOption option,
    quint32_le *functionOffsets, uint *jsClassDataOffset)': names
    'quint32_le', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.JSUnitGenerator.generateHeader' has no cute function "
        "yet. Qt's 'CompiledData::Unit "
        "QV4::Compiler::JSUnitGenerator::generateHeader(GeneratorOption "
        "option, quint32_le *functionOffsets, uint *jsClassDataOffset)': "
        "names 'quint32_le', which has no cute class yet.")

  @staticmethod
  def writeBlock(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::JSUnitGenerator::writeBlock(char *f, Context
    *irBlock) const': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.JSUnitGenerator.writeBlock' has no cute function "
        "yet. Qt's 'void QV4::Compiler::JSUnitGenerator::writeBlock(char "
        "*f, Context *irBlock) const': names 'char', which has no cute "
        "class yet.")

  @staticmethod
  def writeClass(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::JSUnitGenerator::writeClass(char *f, const
    Class &c)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.JSUnitGenerator.writeClass' has no cute function "
        "yet. Qt's 'void QV4::Compiler::JSUnitGenerator::writeClass(char "
        "*f, const Class &c)': names 'char', which has no cute class yet.")

  @staticmethod
  def writeFunction(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::JSUnitGenerator::writeFunction(char *f, Context
    *irFunction) const': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.JSUnitGenerator.writeFunction' has no cute function "
        "yet. Qt's 'void QV4::Compiler::JSUnitGenerator::writeFunction(char "
        "*f, Context *irFunction) const': names 'char', which has no cute "
        "class yet.")

  @staticmethod
  def writeTemplateObject(*__, **_) -> Never:
    """
    Qt's 'void QV4::Compiler::JSUnitGenerator::writeTemplateObject(char *f,
    const TemplateObject &o)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Compiler.JSUnitGenerator.writeTemplateObject' has no cute "
        "function yet. Qt's 'void "
        "QV4::Compiler::JSUnitGenerator::writeTemplateObject(char *f, const "
        "TemplateObject &o)': names 'char', which has no cute class yet.")
