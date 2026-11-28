"""
QV4::CompiledData::CompilationUnit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::CompilationUnit to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QQmlPropertyCache, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QUrl
  from . import QQmlType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QQmlType = WAIT['QQmlType']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CompilationUnit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::CompilationUnit: a plain Python
  object standing in front of one C++ QV4::CompiledData::CompilationUnit.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::CompilationUnit that has a ritual
  and that Python can call so far, 32 names in all: 'unitData',
  'setUnitData', 'stringAt', 'fileName', 'finalUrlString',
  'bindingValueAsString', 'bindingValueAsScriptString',
  'bindingValueAsNumber', 'localCacheFilePath', 'importCount', 'importAt',
  'moduleRequests', 'url', 'finalUrl', 'resolvedType', 'rootPropertyCache',
  'objectCount', 'resolvedIndex', 'implicitComponentForObject',
  'inlineComponentId', 'finalizeCompositeType', 'listPropertyAssignBehavior',
  'ignoresFunctionSignature', 'nativeMethodsAcceptThisObjects',
  'valueTypesAreCopied', 'valueTypesAreAddressable',
  'valueTypesAreAssertable', 'componentsAreBound', 'isESModule',
  'isSharedLibrary', 'qmlTypeForComponent', 'metaType'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::CompilationUnit::CompilationUnit(const Unit
    *unitData, const QQmlPrivate::AOTCompiledFunction *aotCompiledFunctions,
    LookupValidationFn validateLookupSignatures, const QString &fileName,
    const QString &finalUrlString)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QV4::CompiledData::CompilationUnit::~CompilationUnit()': the
    destructor: Python never removes a C++
    QV4::CompiledData::CompilationUnit.
  - Qt's 'bool QV4::CompiledData::CompilationUnit::loadFromDisk(const QUrl
    &url, const QDateTime &sourceTimeStamp, qxp::function_ref<QByteArray ()
    const> sourceChecksum, QString *errorString)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QV4::CompiledData::CompilationUnit::saveToDisk(const QUrl
    &unitUrl, qxp::function_ref<QByteArray () const> sourceChecksum, QString
    *errorString) const': takes a type Python has no way to hand over yet.
  - Qt's 'const CompiledObject
    *QV4::CompiledData::CompilationUnit::objectAt(int index) const': gives
    'const CompiledData::Object', which has no cute class yet.
  - Qt's 'bool QV4::CompiledData::CompilationUnit::verifyChecksum(const
    CompiledData::DependentTypesHasher &dependencyHasher) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'FunctionIterator
    QV4::CompiledData::CompilationUnit::objectFunctionsBegin(const
    CompiledObject *object) const': names
    'QV4::CompiledData::CompilationUnit::CompiledObject', which has no cute
    class yet.
  - Qt's 'FunctionIterator
    QV4::CompiledData::CompilationUnit::objectFunctionsEnd(const
    CompiledObject *object) const': names
    'QV4::CompiledData::CompilationUnit::CompiledObject', which has no cute
    class yet.

  What has no ritual
  ------------------

  4 of the 46 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QV4::CompiledData::CompilationUnit is created at the first use,
    not by 'QV4::CompiledData::CompilationUnit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::CompiledData::CompilationUnit.
  - Each name of Qt's QV4::CompiledData::CompilationUnit that has no cute
    function yet, 'loadFromDisk', 'objectAt', 'objectFunctionsBegin',
    'objectFunctionsEnd', 'saveToDisk', 'verifyChecksum', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::CompiledData::CompilationUnit, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ListPropertyAssignBehavior(CuteNum, scoped=True):
    """
    The enum 'QV4::CompiledData::CompilationUnit::ListPropertyAssignBehavior'
    of Qt, with the 3 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    Append = Kee[int](0)
    Replace = Kee[int](1)
    ReplaceIfNotDefault = Kee[int](2)

  #  The classes Qt writes inside QV4::CompiledData::CompilationUnit, each a
  #  class in here as in C++.

  class FunctionIterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QV4::CompiledData::CompilationUnit::FunctionIterator: a plain Python
    object standing in front of one C++
    QV4::CompiledData::CompilationUnit::FunctionIterator.

    C++ hands a QV4::CompiledData::CompilationUnit::FunctionIterator around
    as a copy, so every C++
    QV4::CompiledData::CompilationUnit::FunctionIterator behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's
    QV4::CompiledData::CompilationUnit::FunctionIterator that has a ritual
    and that Python can call so far, 2 names in all: '__eq__', '__ne__'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::CompiledData::CompilationUnit::FunctionIterator::
      FunctionIterator(const CompiledData::Unit *unit, const CompiledObject
      *object, int index)': names
      'QV4::CompiledData::CompilationUnit::CompiledObject', which has no cute
      class yet.
    - Qt's 'const CompiledFunction
      *QV4::CompiledData::CompilationUnit::FunctionIterator::operator->()
      const': an operator Python has no name for.
    - Qt's 'void
      QV4::CompiledData::CompilationUnit::FunctionIterator::operator++()': an
      operator Python has no name for.
    - Qt's 'QV4::CompiledData::CompilationUnit::FunctionIterator::
      ~FunctionIterator()': the destructor: Python removes its C++
      QV4::CompiledData::CompilationUnit::FunctionIterator by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::CompiledData::CompilationUnit::FunctionIterator is created
      at the first use, not by
      'QV4::CompiledData::CompilationUnit::FunctionIterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QV4::CompiledData::CompilationUnit::FunctionIterator back gives a copy
      the ritual made for Python, in a new cute
      QV4::CompiledData::CompilationUnit::FunctionIterator.
    - Each name of Qt's QV4::CompiledData::CompilationUnit::FunctionIterator
      that has no cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::CompiledData::CompilationUnit::FunctionIterator'

    #  Qt's '~QV4::CompiledData::CompilationUnit::FunctionIterator()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QV4::CompiledData::CompilationUnit::FunctionIterator behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV412CompiledData15CompilationUnit16FunctionIteratorD1Ev')

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

    @overload(THIS)
    def __eq__(self, rhs: CompilationUnit.FunctionIterator) -> bool:
      """
      Calls Qt's 'bool
      QV4::CompiledData::CompilationUnit::FunctionIterator::operator==(const
      FunctionIterator &rhs) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compileddata-compilationunit-functioniterator.html

      Parameters
      ----------

      rhs : CompilationUnit.FunctionIterator
        Passed on as a value: Qt reads the C++
        QV4::CompiledData::CompilationUnit::FunctionIterator, which stays
        Python's own.
      """
      #  bool QV4::CompiledData::CompilationUnit::FunctionIterator::
      #      operator==(const FunctionIterator &rhs) const
      return self.uglySide.call(
          'ritual_ZNK3QV412CompiledData15CompilationUnit16FunctionIteratore'
          'qERKS2_',
          self._valueOf(rhs),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __ne__(self, rhs: CompilationUnit.FunctionIterator) -> bool:
      """
      Calls Qt's 'bool
      QV4::CompiledData::CompilationUnit::FunctionIterator::operator!=(const
      FunctionIterator &rhs) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compileddata-compilationunit-functioniterator.html

      Parameters
      ----------

      rhs : CompilationUnit.FunctionIterator
        Passed on as a value: Qt reads the C++
        QV4::CompiledData::CompilationUnit::FunctionIterator, which stays
        Python's own.
      """
      #  bool QV4::CompiledData::CompilationUnit::FunctionIterator::
      #      operator!=(const FunctionIterator &rhs) const
      return self.uglySide.call(
          'ritual_ZNK3QV412CompiledData15CompilationUnit16FunctionIteratorn'
          'eERKS2_',
          self._valueOf(rhs),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QV4::CompiledData::CompilationUnit::FunctionIterator::
      FunctionIterator(const CompiledData::Unit *unit, const CompiledObject
      *object, int index)': names
      'QV4::CompiledData::CompilationUnit::CompiledObject', which has no cute
      class yet.
      """
      raise NotImplementedError(
          "'QV4.CompiledData.CompilationUnit.FunctionIterator.__init__' has "
          "no cute function yet. Qt's "
          "'QV4::CompiledData::CompilationUnit::FunctionIterator::FunctionIt"
          "erator(const CompiledData::Unit *unit, const CompiledObject "
          "*object, int index)': names "
          "'QV4::CompiledData::CompilationUnit::CompiledObject', which has "
          "no cute class yet.")

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

  class IdToObjectMap(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::CompiledData::CompilationUnit::IdToObjectMap:
    a plain Python object standing in front of one C++
    QV4::CompiledData::CompilationUnit::IdToObjectMap.

    C++ hands a QV4::CompiledData::CompilationUnit::IdToObjectMap around as a
    copy, so every C++ QV4::CompiledData::CompilationUnit::IdToObjectMap
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::CompiledData::CompilationUnit::IdToObjectMap
    that has a ritual and that Python can call so far, 3 names in all:
    'insert', 'clear', 'contains'. None can be made from Python: one comes
    out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::CompiledData::CompilationUnit::IdToObjectMap::~IdToObjectMap()':
      the destructor: Python removes its C++
      QV4::CompiledData::CompilationUnit::IdToObjectMap by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::CompiledData::CompilationUnit::IdToObjectMap is created at
      the first use, not by
      'QV4::CompiledData::CompilationUnit::IdToObjectMap(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::CompiledData::CompilationUnit::IdToObjectMap
      back gives a copy the ritual made for Python, in a new cute
      QV4::CompiledData::CompilationUnit::IdToObjectMap.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::CompiledData::CompilationUnit::IdToObjectMap'

    #  Qt's '~QV4::CompiledData::CompilationUnit::IdToObjectMap()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QV4::CompiledData::CompilationUnit::IdToObjectMap behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMapD1Ev')

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

    @overload(int, int)
    def insert(self, a0: int, a1: int) -> None:
      """
      Calls Qt's 'void
      QV4::CompiledData::CompilationUnit::IdToObjectMap::insert(int a0, int
      a1)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compileddata-compilationunit-idtoobjectmap.html

      Parameters
      ----------

      a0 : int
        Passed on as it is.

      a1 : int
        Passed on as it is.
      """
      #  void QV4::CompiledData::CompilationUnit::IdToObjectMap::insert(int
      #      a0, int a1)
      self.uglySide.call(
          'ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMap6inse'
          'rtEii',
          a0, a1,
      )

    def clear(self) -> None:
      """
      Calls Qt's 'void
      QV4::CompiledData::CompilationUnit::IdToObjectMap::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compileddata-compilationunit-idtoobjectmap.html
      """
      #  void QV4::CompiledData::CompilationUnit::IdToObjectMap::clear()
      self.uglySide.call(
          'ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMap5clea'
          'rEv',
      )

    @overload(int)
    def contains(self, a0: int) -> bool:
      """
      Calls Qt's 'bool
      QV4::CompiledData::CompilationUnit::IdToObjectMap::contains(int a0)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-compileddata-compilationunit-idtoobjectmap.html

      Parameters
      ----------

      a0 : int
        Passed on as it is.
      """
      #  bool QV4::CompiledData::CompilationUnit::IdToObjectMap::contains(int
      #      a0)
      return self.uglySide.call(
          'ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMap8cont'
          'ainsEi',
          a0,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUrl)
  def localCacheFilePath(url: QUrl) -> str:
    """
    Calls Qt's 'QString
    QV4::CompiledData::CompilationUnit::localCacheFilePath(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::CompilationUnit::localCacheFilePath(const
    #      QUrl &url)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData15CompilationUnit18localCacheFilePathER'
        'K4QUrl',
        CuteMixin._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::CompilationUnit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def unitData(self) -> Optional[QV4.CompiledData.Unit]:
    """
    Calls Qt's 'const Unit *QV4::CompiledData::CompilationUnit::unitData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#unitData

    Returns
    -------

    Optional[QV4.CompiledData.Unit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Unit *QV4::CompiledData::CompilationUnit::unitData() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit8unitDataEv',
    )
    return QV4.CompiledData.Unit._cuteAt(address)

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QV4::CompiledData::CompilationUnit::stringAt(uint
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::CompilationUnit::stringAt(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit8stringAtEj', index,
    )

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QV4::CompiledData::CompilationUnit::fileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::CompilationUnit::fileName() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit8fileNameEv',
    )

  def finalUrlString(self) -> str:
    """
    Calls Qt's 'QString QV4::CompiledData::CompilationUnit::finalUrlString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::CompilationUnit::finalUrlString() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit14finalUrlStringEv',
    )

  @overload(WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType)
  def bindingValueAsString(
      self,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> str:
    """
    Calls Qt's 'QString
    QV4::CompiledData::CompilationUnit::bindingValueAsString(const
    CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::CompilationUnit::bindingValueAsString(const
    #      CompiledData::Binding *binding) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit20bindingValueAsStrin'
        'gEPKNS0_7BindingE',
        self._addressOf(binding),
    )

  @overload(WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType)
  def bindingValueAsScriptString(
      self,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> str:
    """
    Calls Qt's 'QString
    QV4::CompiledData::CompilationUnit::bindingValueAsScriptString(const
    CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QV4::CompiledData::CompilationUnit::bindingValueAsScriptString(
    #      const CompiledData::Binding *binding) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit26bindingValueAsScrip'
        'tStringEPKNS0_7BindingE',
        self._addressOf(binding),
    )

  @overload(WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType)
  def bindingValueAsNumber(
      self,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> float:
    """
    Calls Qt's 'double
    QV4::CompiledData::CompilationUnit::bindingValueAsNumber(const
    CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QV4::CompiledData::CompilationUnit::bindingValueAsNumber(const
    #      CompiledData::Binding *binding) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit20bindingValueAsNumbe'
        'rEPKNS0_7BindingE',
        self._addressOf(binding),
    )

  def importCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::CompilationUnit::importCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#importCount
    """
    #  int QV4::CompiledData::CompilationUnit::importCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit11importCountEv',
    )

  @overload(int)
  def importAt(self, index: int) -> Optional[QV4.CompiledData.Import]:
    """
    Calls Qt's 'const CompiledData::Import
    *QV4::CompiledData::CompilationUnit::importAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#importAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Import]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const CompiledData::Import
    #      *QV4::CompiledData::CompilationUnit::importAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit8importAtEi', index,
    )
    return QV4.CompiledData.Import._cuteAt(address)

  def moduleRequests(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QV4::CompiledData::CompilationUnit::moduleRequests() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QV4::CompiledData::CompilationUnit::moduleRequests() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit14moduleRequestsEv',
    )
    return QStringList._cuteOwning(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::CompiledData::CompilationUnit::url() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::CompiledData::CompilationUnit::url() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def finalUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::CompiledData::CompilationUnit::finalUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#finalUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::CompiledData::CompilationUnit::finalUrl() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit8finalUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(int)
  def resolvedType(self, id: int) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'ResolvedTypeReference
    *QV4::CompiledData::CompilationUnit::resolvedType(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#resolvedType

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.ResolvedTypeReference]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ResolvedTypeReference
    #      *QV4::CompiledData::CompilationUnit::resolvedType(int id) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit12resolvedTypeEi', id,
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

  @overload(QMetaType)
  def resolvedType(
      self,
      type: QMetaType,
  ) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'ResolvedTypeReference
    *QV4::CompiledData::CompilationUnit::resolvedType(QMetaType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#resolvedType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.ResolvedTypeReference]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ResolvedTypeReference
    #      *QV4::CompiledData::CompilationUnit::resolvedType(QMetaType type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit12resolvedTypeE9QMeta'
        'Type',
        self._valueOf(type),
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

  def rootPropertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QV4::CompiledData::CompilationUnit::rootPropertyCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QV4::CompiledData::CompilationUnit::rootPropertyCache() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit17rootPropertyCacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  def objectCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::CompilationUnit::objectCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#objectCount
    """
    #  int QV4::CompiledData::CompilationUnit::objectCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit11objectCountEv',
    )

  @overload(int)
  def resolvedIndex(self, index: int) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::CompilationUnit::resolvedIndex(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::CompilationUnit::resolvedIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit13resolvedIndexEi',
        index,
    )

  @overload(int)
  def implicitComponentForObject(self, index: int) -> int:
    """
    Calls Qt's 'int
    QV4::CompiledData::CompilationUnit::implicitComponentForObject(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::CompilationUnit::implicitComponentForObject(int
    #      index) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit26implicitComponentFo'
        'rObjectEi',
        index,
    )

  @overload(str)
  def inlineComponentId(self, inlineComponentName: str) -> int:
    """
    Calls Qt's 'int
    QV4::CompiledData::CompilationUnit::inlineComponentId(const QString
    &inlineComponentName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    inlineComponentName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::CompiledData::CompilationUnit::inlineComponentId(const
    #      QString &inlineComponentName) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit17inlineComponentIdER'
        'K7QString',
        inlineComponentName,
    )

  def listPropertyAssignBehavior(self) -> ListPropertyAssignBehavior:
    """
    Calls Qt's 'ListPropertyAssignBehavior
    QV4::CompiledData::CompilationUnit::listPropertyAssignBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Returns
    -------

    ListPropertyAssignBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ListPropertyAssignBehavior(number)' gives.
    """
    #  ListPropertyAssignBehavior
    #      QV4::CompiledData::CompilationUnit::listPropertyAssignBehavior()
    #      const
    return CompilationUnit.ListPropertyAssignBehavior(self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit26listPropertyAssignB'
        'ehaviorEv',
    ))

  def ignoresFunctionSignature(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::CompilationUnit::ignoresFunctionSignature() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::ignoresFunctionSignature()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit24ignoresFunctionSign'
        'atureEv',
    )

  def nativeMethodsAcceptThisObjects(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::CompilationUnit::nativeMethodsAcceptThisObjects()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::
    #      nativeMethodsAcceptThisObjects() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit30nativeMethodsAccept'
        'ThisObjectsEv',
    )

  def valueTypesAreCopied(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::CompilationUnit::valueTypesAreCopied() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::valueTypesAreCopied() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit19valueTypesAreCopied'
        'Ev',
    )

  def valueTypesAreAddressable(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::CompilationUnit::valueTypesAreAddressable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::valueTypesAreAddressable()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit24valueTypesAreAddres'
        'sableEv',
    )

  def valueTypesAreAssertable(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::CompilationUnit::valueTypesAreAssertable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::valueTypesAreAssertable()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit23valueTypesAreAssert'
        'ableEv',
    )

  def componentsAreBound(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::CompilationUnit::componentsAreBound()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::componentsAreBound() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit18componentsAreBoundE'
        'v',
    )

  def isESModule(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::CompilationUnit::isESModule() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#isESModule
    """
    #  bool QV4::CompiledData::CompilationUnit::isESModule() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit10isESModuleEv',
    )

  def isSharedLibrary(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::CompilationUnit::isSharedLibrary()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html
    """
    #  bool QV4::CompiledData::CompilationUnit::isSharedLibrary() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit15isSharedLibraryEv',
    )

  @overload()
  @overload(str)
  def qmlTypeForComponent(self, inlineComponentName: str = '') -> QQmlType:
    """
    Calls Qt's 'QQmlType
    QV4::CompiledData::CompilationUnit::qmlTypeForComponent(const QString
    &inlineComponentName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    inlineComponentName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QV4::CompiledData::CompilationUnit::qmlTypeForComponent(const
    #      QString &inlineComponentName) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit19qmlTypeForComponent'
        'ERK7QString',
        inlineComponentName,
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::CompiledData::CompilationUnit::metaType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::CompiledData::CompilationUnit::metaType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData15CompilationUnit8metaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.CompiledData.Unit'])
  @overload(NoneType)
  @overload(WAIT['QV4.CompiledData.Unit'], WAIT['QV4.CompiledData.QmlUnit'])
  @overload(WAIT['QV4.CompiledData.Unit'], NoneType)
  @overload(NoneType, WAIT['QV4.CompiledData.QmlUnit'])
  @overload(NoneType, NoneType)
  @overload(
      WAIT['QV4.CompiledData.Unit'], WAIT['QV4.CompiledData.QmlUnit'], str,
  )
  @overload(WAIT['QV4.CompiledData.Unit'], NoneType, str)
  @overload(NoneType, WAIT['QV4.CompiledData.QmlUnit'], str)
  @overload(NoneType, NoneType, str)
  @overload(
      WAIT['QV4.CompiledData.Unit'], WAIT['QV4.CompiledData.QmlUnit'], str,
      str,
  )
  @overload(WAIT['QV4.CompiledData.Unit'], NoneType, str, str)
  @overload(NoneType, WAIT['QV4.CompiledData.QmlUnit'], str, str)
  @overload(NoneType, NoneType, str, str)
  def setUnitData(
      self,
      unitData: Optional[QV4.CompiledData.Unit],
      qmlUnit: Optional[QV4.CompiledData.QmlUnit] = None,
      fileName: str = '',
      finalUrlString: str = '',
  ) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::CompilationUnit::setUnitData(const
    Unit *unitData, const QmlUnit *qmlUnit, const QString &fileName, const
    QString &finalUrlString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html#setUnitData

    Parameters
    ----------

    unitData : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qmlUnit : Optional[QV4.CompiledData.QmlUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    finalUrlString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QV4::CompiledData::CompilationUnit::setUnitData(const Unit
    #      *unitData, const QmlUnit *qmlUnit, const QString &fileName, const
    #      QString &finalUrlString)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData15CompilationUnit11setUnitDataEPKNS0_4U'
        'nitEPKNS0_7QmlUnitERK7QStringSA_',
        self._addressOf(unitData), self._addressOf(qmlUnit), fileName,
        finalUrlString,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(WAIT['QV4.CompiledData.Unit'])
  @overload(NoneType)
  @overload(WAIT['QV4.CompiledData.Unit'], str)
  @overload(NoneType, str)
  @overload(WAIT['QV4.CompiledData.Unit'], str, str)
  @overload(NoneType, str, str)
  def __init__(
      self,
      unitData: Optional[QV4.CompiledData.Unit] = None,
      fileName: str = '',
      finalUrlString: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::CompiledData::CompilationUnit::CompilationUnit(const Unit
    *unitData, const QString &fileName, const QString &finalUrlString)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    unitData : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    finalUrlString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QV4::CompiledData::CompilationUnit::CompilationUnit(const Unit
    #      *unitData, const QString &fileName, const QString &finalUrlString)
    self._noteCreation(CompilationUnit, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData15CompilationUnitC1EPKNS0_4UnitERK7QStr'
        'ingS7_',
        self._addressOf(unitData), fileName, finalUrlString,
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

  @overload(QQmlType)
  def finalizeCompositeType(self, type: QQmlType) -> None:
    """
    Calls Qt's 'void
    QV4::CompiledData::CompilationUnit::finalizeCompositeType(const QQmlType
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-compilationunit.html

    Parameters
    ----------

    type : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.
    """
    #  void QV4::CompiledData::CompilationUnit::finalizeCompositeType(const
    #      QQmlType &type)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData15CompilationUnit21finalizeCompositeTyp'
        'eERK8QQmlType',
        self._valueOf(type),
    )

  @staticmethod
  def loadFromDisk(*__, **_) -> Never:
    """
    Qt's 'bool QV4::CompiledData::CompilationUnit::loadFromDisk(const QUrl
    &url, const QDateTime &sourceTimeStamp, qxp::function_ref<QByteArray ()
    const> sourceChecksum, QString *errorString)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.CompilationUnit.loadFromDisk' has no cute "
        "function yet. Qt's 'bool "
        "QV4::CompiledData::CompilationUnit::loadFromDisk(const QUrl &url, "
        "const QDateTime &sourceTimeStamp, qxp::function_ref<QByteArray () "
        "const> sourceChecksum, QString *errorString)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def objectAt(*__, **_) -> Never:
    """
    Qt's 'const CompiledObject
    *QV4::CompiledData::CompilationUnit::objectAt(int index) const': gives
    'const CompiledData::Object', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.CompilationUnit.objectAt' has no cute function "
        "yet. Qt's 'const CompiledObject "
        "*QV4::CompiledData::CompilationUnit::objectAt(int index) const': "
        "gives 'const CompiledData::Object', which has no cute class yet.")

  @staticmethod
  def objectFunctionsBegin(*__, **_) -> Never:
    """
    Qt's 'FunctionIterator
    QV4::CompiledData::CompilationUnit::objectFunctionsBegin(const
    CompiledObject *object) const': names
    'QV4::CompiledData::CompilationUnit::CompiledObject', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.CompilationUnit.objectFunctionsBegin' has no "
        "cute function yet. Qt's 'FunctionIterator "
        "QV4::CompiledData::CompilationUnit::objectFunctionsBegin(const "
        "CompiledObject *object) const': names "
        "'QV4::CompiledData::CompilationUnit::CompiledObject', which has no "
        "cute class yet.")

  @staticmethod
  def objectFunctionsEnd(*__, **_) -> Never:
    """
    Qt's 'FunctionIterator
    QV4::CompiledData::CompilationUnit::objectFunctionsEnd(const
    CompiledObject *object) const': names
    'QV4::CompiledData::CompilationUnit::CompiledObject', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.CompilationUnit.objectFunctionsEnd' has no cute "
        "function yet. Qt's 'FunctionIterator "
        "QV4::CompiledData::CompilationUnit::objectFunctionsEnd(const "
        "CompiledObject *object) const': names "
        "'QV4::CompiledData::CompilationUnit::CompiledObject', which has no "
        "cute class yet.")

  @staticmethod
  def saveToDisk(*__, **_) -> Never:
    """
    Qt's 'bool QV4::CompiledData::CompilationUnit::saveToDisk(const QUrl
    &unitUrl, qxp::function_ref<QByteArray () const> sourceChecksum, QString
    *errorString) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.CompilationUnit.saveToDisk' has no cute function "
        "yet. Qt's 'bool "
        "QV4::CompiledData::CompilationUnit::saveToDisk(const QUrl "
        "&unitUrl, qxp::function_ref<QByteArray () const> sourceChecksum, "
        "QString *errorString) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def verifyChecksum(*__, **_) -> Never:
    """
    Qt's 'bool QV4::CompiledData::CompilationUnit::verifyChecksum(const
    CompiledData::DependentTypesHasher &dependencyHasher) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.CompilationUnit.verifyChecksum' has no cute "
        "function yet. Qt's 'bool "
        "QV4::CompiledData::CompilationUnit::verifyChecksum(const "
        "CompiledData::DependentTypesHasher &dependencyHasher) const': "
        "takes a type Python has no way to hand over yet.")
