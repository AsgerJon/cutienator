"""
QV4::ExecutableCompilationUnit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4executablecompilationunit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::ExecutableCompilationUnit to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QQmlPropertyCache, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QUrl
  from . import QQmlPropertyCacheVector, QQmlType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExecutableCompilationUnit(QV4.CompilationUnitRuntimeData):
  """
  The cute side of Qt's QV4::ExecutableCompilationUnit: a plain Python object
  standing in front of one C++ QV4::ExecutableCompilationUnit.

  It is built on the cute 'QV4::CompilationUnitRuntimeData', as Qt's
  QV4::ExecutableCompilationUnit is built on Qt's
  QV4::CompilationUnitRuntimeData, and has everything that class has. Qt's
  QV4::ExecutableCompilationUnit is built on Qt's
  QQmlRefCounted<ExecutableCompilationUnit> as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QV4::ExecutableCompilationUnit that has a ritual and
  that Python can call so far, 45 names in all: 'finalUrlString', 'fileName',
  'url', 'finalUrl', 'propertyCachesPtr', 'rootPropertyCache',
  'resolvedType', 'qmlTypeForComponent', 'metaType', 'inlineComponentId',
  'nativeMethodsAcceptThisObjects', 'ignoresFunctionSignature',
  'valueTypesAreCopied', 'valueTypesAreAddressable',
  'valueTypesAreAssertable', 'componentsAreBound', 'isESModule',
  'objectCount', 'resolvedIndex', 'implicitComponentForObject',
  'templateObjectAt', 'instantiate', 'resolveExport', 'exportedNames',
  'evaluate', 'evaluateModuleRequests', 'mark', 'markObjects',
  'bindingValueAsString', 'bindingValueAsNumber',
  'bindingValueAsScriptString', 'translateFrom', 'module', 'setModule',
  'value', 'setValue', 'unitData', 'stringAt', 'rootFunction', 'populate',
  'clear', 'totalStringCount', 'urlAt', 'createNamedObjectsPerComponent',
  'lookupNameInExportTable'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlRefPointer<QQmlTypeNameCache>
    QV4::ExecutableCompilationUnit::typeNameCache() const': gives a type
    Python has no way to take yet.
  - Qt's 'const CompiledObject *QV4::ExecutableCompilationUnit::objectAt(int
    index) const': gives 'const CompiledData::Object', which has no cute
    class yet.
  - Qt's 'const QList<QQmlRefPointer<QQmlScriptData>>
    *QV4::ExecutableCompilationUnit::dependentScriptsPtr() const': gives
    'QList<QQmlRefPointer<QQmlScriptData>>', which has no cute class yet.
  - Qt's 'const CompiledData::BindingPropertyData
    *QV4::ExecutableCompilationUnit::bindingPropertyDataPerObjectAt(qsizetype
    objectIndex) const': gives 'QList<const QQmlPropertyData *>', which has
    no cute class yet.
  - Qt's 'const QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    &QV4::ExecutableCompilationUnit::baseCompilationUnit() const': gives a
    type Python has no way to take yet.
  - Qt's 'QV4::ExecutableCompilationUnit::ExecutableCompilationUnit(
    QQmlRefPointer<CompiledData::CompilationUnit> &&compilationUnit)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QV4::ExecutableCompilationUnit::~ExecutableCompilationUnit()': the
    destructor: Python never removes a C++ QV4::ExecutableCompilationUnit.
  - Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutableCompilationUnit::create(QQmlRefPointer<CompiledData::
    CompilationUnit> &&compilationUnit, ExecutionEngine *engine)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const Value
    *QV4::ExecutableCompilationUnit::resolveExportRecursively(QV4::String
    *exportName, QList<ResolveSetEntry> *resolveSet) const': names
    'QList<QV4::ExecutableCompilationUnit::ResolveSetEntry>', which has no
    cute class yet.
  - Qt's 'void
    QV4::ExecutableCompilationUnit::getExportedNamesRecursively(QStringList
    *names, QList<const ExecutableCompilationUnit *> *exportNameSet, bool
    includeDefaultExport) const': names 'QStringList', which has no cute
    class yet.

  What has no ritual
  ------------------

  6 of the 62 functions Qt declares: 4 forbidden; 1 a template; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::ExecutableCompilationUnit is created at the first use, not
    by 'QV4::ExecutableCompilationUnit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ExecutableCompilationUnit.
  - Each name of Qt's QV4::ExecutableCompilationUnit that has no cute
    function yet, 'baseCompilationUnit', 'bindingPropertyDataPerObjectAt',
    'create', 'dependentModule', 'dependentScriptsPtr',
    'getExportedNamesRecursively', 'namedObjectsPerComponent', 'objectAt',
    'resolveExportRecursively', 'typeNameCache', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QV4::ExecutableCompilationUnit, each a
  #  class in here as in C++.

  class TranslationDataIndex(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QV4::ExecutableCompilationUnit::TranslationDataIndex: a plain Python
    object standing in front of one C++
    QV4::ExecutableCompilationUnit::TranslationDataIndex.

    C++ hands a QV4::ExecutableCompilationUnit::TranslationDataIndex around
    as a copy, so every C++
    QV4::ExecutableCompilationUnit::TranslationDataIndex behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QV4::ExecutableCompilationUnit::TranslationDataIndex
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::ExecutableCompilationUnit::TranslationDataIndex::
      ~TranslationDataIndex()': the destructor: Python removes its C++
      QV4::ExecutableCompilationUnit::TranslationDataIndex by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::ExecutableCompilationUnit::TranslationDataIndex is created
      at the first use, not by
      'QV4::ExecutableCompilationUnit::TranslationDataIndex(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QV4::ExecutableCompilationUnit::TranslationDataIndex back gives a copy
      the ritual made for Python, in a new cute
      QV4::ExecutableCompilationUnit::TranslationDataIndex.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::ExecutableCompilationUnit::TranslationDataIndex'

    #  Qt's '~QV4::ExecutableCompilationUnit::TranslationDataIndex()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QV4::ExecutableCompilationUnit::TranslationDataIndex behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV425ExecutableCompilationUnit20TranslationDataIndexD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ExecutableCompilationUnit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def finalUrlString(self) -> str:
    """
    Calls Qt's 'QString QV4::ExecutableCompilationUnit::finalUrlString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#finalUrlString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::ExecutableCompilationUnit::finalUrlString() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit14finalUrlStringEv',
    )

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QV4::ExecutableCompilationUnit::fileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::ExecutableCompilationUnit::fileName() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit8fileNameEv',
    )

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::ExecutableCompilationUnit::url() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::ExecutableCompilationUnit::url() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def finalUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::ExecutableCompilationUnit::finalUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#finalUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::ExecutableCompilationUnit::finalUrl() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit8finalUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def rootPropertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QV4::ExecutableCompilationUnit::rootPropertyCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QV4::ExecutableCompilationUnit::rootPropertyCache() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit17rootPropertyCacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(int)
  def resolvedType(self, id: int) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'ResolvedTypeReference
    *QV4::ExecutableCompilationUnit::resolvedType(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#resolvedType

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
    #      *QV4::ExecutableCompilationUnit::resolvedType(int id) const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit12resolvedTypeEi', id,
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

  @overload()
  @overload(str)
  def qmlTypeForComponent(self, inlineComponentName: str = '') -> QQmlType:
    """
    Calls Qt's 'QQmlType
    QV4::ExecutableCompilationUnit::qmlTypeForComponent(const QString
    &inlineComponentName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

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
    #  QQmlType QV4::ExecutableCompilationUnit::qmlTypeForComponent(const
    #      QString &inlineComponentName) const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit19qmlTypeForComponentERK7'
        'QString',
        inlineComponentName,
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::ExecutableCompilationUnit::metaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::ExecutableCompilationUnit::metaType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit8metaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @overload(str)
  def inlineComponentId(self, inlineComponentName: str) -> int:
    """
    Calls Qt's 'int QV4::ExecutableCompilationUnit::inlineComponentId(const
    QString &inlineComponentName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Parameters
    ----------

    inlineComponentName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::ExecutableCompilationUnit::inlineComponentId(const QString
    #      &inlineComponentName) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit17inlineComponentIdERK7QS'
        'tring',
        inlineComponentName,
    )

  def nativeMethodsAcceptThisObjects(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::ExecutableCompilationUnit::nativeMethodsAcceptThisObjects() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  bool QV4::ExecutableCompilationUnit::nativeMethodsAcceptThisObjects()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit30nativeMethodsAcceptThis'
        'ObjectsEv',
    )

  def ignoresFunctionSignature(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::ExecutableCompilationUnit::ignoresFunctionSignature() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  bool QV4::ExecutableCompilationUnit::ignoresFunctionSignature() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit24ignoresFunctionSignatur'
        'eEv',
    )

  def valueTypesAreCopied(self) -> bool:
    """
    Calls Qt's 'bool QV4::ExecutableCompilationUnit::valueTypesAreCopied()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  bool QV4::ExecutableCompilationUnit::valueTypesAreCopied() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit19valueTypesAreCopiedEv',
    )

  def valueTypesAreAddressable(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::ExecutableCompilationUnit::valueTypesAreAddressable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  bool QV4::ExecutableCompilationUnit::valueTypesAreAddressable() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit24valueTypesAreAddressabl'
        'eEv',
    )

  def valueTypesAreAssertable(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::ExecutableCompilationUnit::valueTypesAreAssertable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  bool QV4::ExecutableCompilationUnit::valueTypesAreAssertable() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit23valueTypesAreAssertable'
        'Ev',
    )

  def componentsAreBound(self) -> bool:
    """
    Calls Qt's 'bool QV4::ExecutableCompilationUnit::componentsAreBound()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  bool QV4::ExecutableCompilationUnit::componentsAreBound() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit18componentsAreBoundEv',
    )

  def isESModule(self) -> bool:
    """
    Calls Qt's 'bool QV4::ExecutableCompilationUnit::isESModule() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#isESModule
    """
    #  bool QV4::ExecutableCompilationUnit::isESModule() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit10isESModuleEv',
    )

  def objectCount(self) -> int:
    """
    Calls Qt's 'int QV4::ExecutableCompilationUnit::objectCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#objectCount
    """
    #  int QV4::ExecutableCompilationUnit::objectCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit11objectCountEv',
    )

  @overload(int)
  def resolvedIndex(self, index: int) -> int:
    """
    Calls Qt's 'int QV4::ExecutableCompilationUnit::resolvedIndex(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#resolvedIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QV4::ExecutableCompilationUnit::resolvedIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit13resolvedIndexEi', index,
    )

  @overload(int)
  def implicitComponentForObject(self, index: int) -> int:
    """
    Calls Qt's 'int
    QV4::ExecutableCompilationUnit::implicitComponentForObject(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QV4::ExecutableCompilationUnit::implicitComponentForObject(int
    #      index) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit26implicitComponentForObj'
        'ectEi',
        index,
    )

  @overload(int)
  def templateObjectAt(self, index: int) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutableCompilationUnit::templateObjectAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutableCompilationUnit::templateObjectAt(int
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit16templateObjectAtEi',
        index,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def resolveExport(
      self,
      exportName: Optional[QV4.String],
  ) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value
    *QV4::ExecutableCompilationUnit::resolveExport(QV4::String *exportName)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#resolveExport

    Parameters
    ----------

    exportName : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::ExecutableCompilationUnit::resolveExport(QV4::String
    #      *exportName) const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit13resolveExportEPNS_6Stri'
        'ngE',
        self._addressOf(exportName),
    )
    return QV4.Value._cuteAt(address)

  def exportedNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QV4::ExecutableCompilationUnit::exportedNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#exportedNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QV4::ExecutableCompilationUnit::exportedNames() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit13exportedNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType)
  def bindingValueAsString(
      self,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> str:
    """
    Calls Qt's 'QString
    QV4::ExecutableCompilationUnit::bindingValueAsString(const
    CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

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
    #  QString QV4::ExecutableCompilationUnit::bindingValueAsString(const
    #      CompiledData::Binding *binding) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit20bindingValueAsStringEPK'
        'NS_12CompiledData7BindingE',
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
    QV4::ExecutableCompilationUnit::bindingValueAsNumber(const
    CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Parameters
    ----------

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  double QV4::ExecutableCompilationUnit::bindingValueAsNumber(const
    #      CompiledData::Binding *binding) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit20bindingValueAsNumberEPK'
        'NS_12CompiledData7BindingE',
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
    QV4::ExecutableCompilationUnit::bindingValueAsScriptString(const
    CompiledData::Binding *binding) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

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
    #      QV4::ExecutableCompilationUnit::bindingValueAsScriptString(const
    #      CompiledData::Binding *binding) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit26bindingValueAsScriptStr'
        'ingEPKNS_12CompiledData7BindingE',
        self._addressOf(binding),
    )

  @overload(TranslationDataIndex)
  def translateFrom(self, index: TranslationDataIndex) -> str:
    """
    Calls Qt's 'QString
    QV4::ExecutableCompilationUnit::translateFrom(TranslationDataIndex index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#translateFrom

    Parameters
    ----------

    index : TranslationDataIndex
      Passed on as a value: Qt reads the C++
      QV4::ExecutableCompilationUnit::TranslationDataIndex, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QV4::ExecutableCompilationUnit::translateFrom(TranslationDataIndex
    #      index) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit13translateFromENS0_20Tra'
        'nslationDataIndexE',
        self._valueOf(index),
    )

  def module(self) -> Optional[QV4.Heap.Module]:
    """
    Calls Qt's 'Heap::Module *QV4::ExecutableCompilationUnit::module()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#module

    Returns
    -------

    Optional[QV4.Heap.Module]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Module *QV4::ExecutableCompilationUnit::module() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit6moduleEv',
    )
    return QV4.Heap.Module._cuteAt(address)

  def value(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutableCompilationUnit::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#value
    """
    #  ReturnedValue QV4::ExecutableCompilationUnit::value() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit5valueEv',
    )

  def unitData(self) -> Optional[QV4.CompiledData.Unit]:
    """
    Calls Qt's 'const CompiledData::Unit
    *QV4::ExecutableCompilationUnit::unitData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#unitData

    Returns
    -------

    Optional[QV4.CompiledData.Unit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const CompiledData::Unit *QV4::ExecutableCompilationUnit::unitData()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit8unitDataEv',
    )
    return QV4.CompiledData.Unit._cuteAt(address)

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QV4::ExecutableCompilationUnit::stringAt(uint index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::ExecutableCompilationUnit::stringAt(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit8stringAtEj', index,
    )

  def totalStringCount(self) -> int:
    """
    Calls Qt's 'quint32 QV4::ExecutableCompilationUnit::totalStringCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  quint32 QV4::ExecutableCompilationUnit::totalStringCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit16totalStringCountEv',
    )

  @overload(int)
  def urlAt(self, index: int) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::ExecutableCompilationUnit::urlAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#urlAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::ExecutableCompilationUnit::urlAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit5urlAtEi', index,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(WAIT['QV4.CompiledData.ExportEntry'], int, WAIT['QV4.String'])
  @overload(WAIT['QV4.CompiledData.ExportEntry'], int, NoneType)
  @overload(NoneType, int, WAIT['QV4.String'])
  @overload(NoneType, int, NoneType)
  def lookupNameInExportTable(
      self,
      firstExportEntry: Optional[QV4.CompiledData.ExportEntry],
      tableSize: int,
      name: Optional[QV4.String],
  ) -> Optional[QV4.CompiledData.ExportEntry]:
    """
    Calls Qt's 'const CompiledData::ExportEntry
    *QV4::ExecutableCompilationUnit::lookupNameInExportTable(const
    CompiledData::ExportEntry *firstExportEntry, int tableSize, QV4::String
    *name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Parameters
    ----------

    firstExportEntry : Optional[QV4.CompiledData.ExportEntry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    tableSize : int
      Passed on as it is.

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.CompiledData.ExportEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const CompiledData::ExportEntry
    #      *QV4::ExecutableCompilationUnit::lookupNameInExportTable(const
    #      CompiledData::ExportEntry *firstExportEntry, int tableSize,
    #      QV4::String *name) const
    address = self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit23lookupNameInExportTable'
        'EPKNS_12CompiledData11ExportEntryEiPNS_6StringE',
        self._addressOf(firstExportEntry), tableSize, self._addressOf(name),
    )
    return QV4.CompiledData.ExportEntry._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.Heap.Module'])
  @overload(NoneType)
  def setModule(self, module: Optional[QV4.Heap.Module]) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::setModule(Heap::Module
    *module)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#setModule

    Parameters
    ----------

    module : Optional[QV4.Heap.Module]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutableCompilationUnit::setModule(Heap::Module *module)
    self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit9setModuleEPNS_4Heap6Modul'
        'eE',
        self._addressOf(module),
    )

  @overload(WAIT['QV4.Value'])
  def setValue(self, value: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::setValue(const
    QV4::Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#setValue

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::ExecutableCompilationUnit::setValue(const QV4::Value &value)
    self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit8setValueERKNS_5ValueE',
        self._valueOf(value),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QV4::ExecutableCompilationUnit::ExecutableCompilationUnit()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  QV4::ExecutableCompilationUnit::ExecutableCompilationUnit()
    self._noteCreation(ExecutableCompilationUnit, lambda: Rituals.call(
        'ritual_ZN3QV425ExecutableCompilationUnitC1Ev',
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

  def propertyCachesPtr(self) -> Optional[QQmlPropertyCacheVector]:
    """
    Calls Qt's 'QQmlPropertyCacheVector
    *QV4::ExecutableCompilationUnit::propertyCachesPtr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Returns
    -------

    Optional[QQmlPropertyCacheVector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyCacheVector
    #      *QV4::ExecutableCompilationUnit::propertyCachesPtr()
    address = self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit17propertyCachesPtrEv',
    )
    from . import QQmlPropertyCacheVector
    return QQmlPropertyCacheVector._cuteAt(address)

  def instantiate(self) -> Optional[QV4.Heap.Module]:
    """
    Calls Qt's 'Heap::Module *QV4::ExecutableCompilationUnit::instantiate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#instantiate

    Returns
    -------

    Optional[QV4.Heap.Module]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Module *QV4::ExecutableCompilationUnit::instantiate()
    address = self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit11instantiateEv',
    )
    return QV4.Heap.Module._cuteAt(address)

  def evaluate(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::evaluate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#evaluate
    """
    #  void QV4::ExecutableCompilationUnit::evaluate()
    self.uglySide.call('ritual_ZN3QV425ExecutableCompilationUnit8evaluateEv')

  def evaluateModuleRequests(self) -> None:
    """
    Calls Qt's 'void
    QV4::ExecutableCompilationUnit::evaluateModuleRequests()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html
    """
    #  void QV4::ExecutableCompilationUnit::evaluateModuleRequests()
    self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit22evaluateModuleRequestsEv',
    )

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::mark(MarkStack
    *markStack) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#mark

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutableCompilationUnit::mark(MarkStack *markStack) const
    self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit4markEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def markObjects(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::markObjects(MarkStack
    *markStack) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#markObjects

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutableCompilationUnit::markObjects(MarkStack *markStack)
    #      const
    self.uglySide.call(
        'ritual_ZNK3QV425ExecutableCompilationUnit11markObjectsEPNS_9MarkSt'
        'ackE',
        self._addressOf(markStack),
    )

  def rootFunction(self) -> Optional[QV4.Function]:
    """
    Calls Qt's 'QV4::Function
    *QV4::ExecutableCompilationUnit::rootFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#rootFunction

    Returns
    -------

    Optional[QV4.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Function *QV4::ExecutableCompilationUnit::rootFunction()
    address = self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit12rootFunctionEv',
    )
    return QV4.Function._cuteAt(address)

  def populate(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::populate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#populate
    """
    #  void QV4::ExecutableCompilationUnit::populate()
    self.uglySide.call('ritual_ZN3QV425ExecutableCompilationUnit8populateEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutableCompilationUnit::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html#clear
    """
    #  void QV4::ExecutableCompilationUnit::clear()
    self.uglySide.call('ritual_ZN3QV425ExecutableCompilationUnit5clearEv')

  @overload(int)
  def createNamedObjectsPerComponent(
      self,
      componentObjectIndex: int,
  ) -> QV4.IdentifierHash:
    """
    Calls Qt's 'IdentifierHash
    QV4::ExecutableCompilationUnit::createNamedObjectsPerComponent(int
    componentObjectIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executablecompilationunit.html

    Parameters
    ----------

    componentObjectIndex : int
      Passed on as it is.

    Returns
    -------

    QV4.IdentifierHash
      A new cute QV4::IdentifierHash around the copy Qt gave back. Python
      owns it.
    """
    #  IdentifierHash
    #      QV4::ExecutableCompilationUnit::createNamedObjectsPerComponent(int
    #      componentObjectIndex)
    address = self.uglySide.call(
        'ritual_ZN3QV425ExecutableCompilationUnit30createNamedObjectsPerCom'
        'ponentEi',
        componentObjectIndex,
    )
    return QV4.IdentifierHash._cuteOwning(address)

  @staticmethod
  def baseCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'const QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    &QV4::ExecutableCompilationUnit::baseCompilationUnit() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.baseCompilationUnit' has no cute "
        "function yet. Qt's 'const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&QV4::ExecutableCompilationUnit::baseCompilationUnit() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindingPropertyDataPerObjectAt(*__, **_) -> Never:
    """
    Qt's 'const CompiledData::BindingPropertyData
    *QV4::ExecutableCompilationUnit::bindingPropertyDataPerObjectAt(qsizetype
    objectIndex) const': gives 'QList<const QQmlPropertyData *>', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.bindingPropertyDataPerObjectAt' has "
        "no cute function yet. Qt's 'const "
        "CompiledData::BindingPropertyData "
        "*QV4::ExecutableCompilationUnit::bindingPropertyDataPerObjectAt(qsi"
        "zetype objectIndex) const': gives 'QList<const QQmlPropertyData "
        "*>', which has no cute class yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutableCompilationUnit::create(QQmlRefPointer<CompiledData::
    CompilationUnit> &&compilationUnit, ExecutionEngine *engine)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.create' has no cute function yet. "
        "Qt's 'QQmlRefPointer<ExecutableCompilationUnit> "
        "QV4::ExecutableCompilationUnit::create(QQmlRefPointer<CompiledData:"
        ":CompilationUnit> &&compilationUnit, ExecutionEngine *engine)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def dependentModule(*__, **_) -> Never:
    """
    Qt's 'QV4::ExecutableCompilationUnit::dependentModule': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.dependentModule' has no cute "
        "function yet. Qt's "
        "'QV4::ExecutableCompilationUnit::dependentModule': a template: a "
        "pattern and no single function.")

  @staticmethod
  def dependentScriptsPtr(*__, **_) -> Never:
    """
    Qt's 'const QList<QQmlRefPointer<QQmlScriptData>>
    *QV4::ExecutableCompilationUnit::dependentScriptsPtr() const': gives
    'QList<QQmlRefPointer<QQmlScriptData>>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.dependentScriptsPtr' has no cute "
        "function yet. Qt's 'const QList<QQmlRefPointer<QQmlScriptData>> "
        "*QV4::ExecutableCompilationUnit::dependentScriptsPtr() const': "
        "gives 'QList<QQmlRefPointer<QQmlScriptData>>', which has no cute "
        "class yet.")

  @staticmethod
  def getExportedNamesRecursively(*__, **_) -> Never:
    """
    Qt's 'void
    QV4::ExecutableCompilationUnit::getExportedNamesRecursively(QStringList
    *names, QList<const ExecutableCompilationUnit *> *exportNameSet, bool
    includeDefaultExport) const': names 'QStringList', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.getExportedNamesRecursively' has no "
        "cute function yet. Qt's 'void "
        "QV4::ExecutableCompilationUnit::getExportedNamesRecursively(QString"
        "List *names, QList<const ExecutableCompilationUnit *> "
        "*exportNameSet, bool includeDefaultExport) const': names "
        "'QStringList', which has no cute class yet.")

  @staticmethod
  def namedObjectsPerComponent(*__, **_) -> Never:
    """
    Qt's 'IdentifierHash
    QV4::ExecutableCompilationUnit::namedObjectsPerComponent(int
    componentObjectIndex)': leans on
    'QV4::IdentifierHash::IdentifierHash(QV4::IdentifierHash const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.namedObjectsPerComponent' has no "
        "cute function yet. Qt's 'IdentifierHash "
        "QV4::ExecutableCompilationUnit::namedObjectsPerComponent(int "
        "componentObjectIndex)': leans on "
        "'QV4::IdentifierHash::IdentifierHash(QV4::IdentifierHash const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def objectAt(*__, **_) -> Never:
    """
    Qt's 'const CompiledObject *QV4::ExecutableCompilationUnit::objectAt(int
    index) const': gives 'const CompiledData::Object', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.objectAt' has no cute function yet. "
        "Qt's 'const CompiledObject "
        "*QV4::ExecutableCompilationUnit::objectAt(int index) const': gives "
        "'const CompiledData::Object', which has no cute class yet.")

  @staticmethod
  def resolveExportRecursively(*__, **_) -> Never:
    """
    Qt's 'const Value
    *QV4::ExecutableCompilationUnit::resolveExportRecursively(QV4::String
    *exportName, QList<ResolveSetEntry> *resolveSet) const': names
    'QList<QV4::ExecutableCompilationUnit::ResolveSetEntry>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.resolveExportRecursively' has no "
        "cute function yet. Qt's 'const Value "
        "*QV4::ExecutableCompilationUnit::resolveExportRecursively(QV4::Stri"
        "ng *exportName, QList<ResolveSetEntry> *resolveSet) const': names "
        "'QList<QV4::ExecutableCompilationUnit::ResolveSetEntry>', which "
        "has no cute class yet.")

  @staticmethod
  def typeNameCache(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlTypeNameCache>
    QV4::ExecutableCompilationUnit::typeNameCache() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutableCompilationUnit.typeNameCache' has no cute function "
        "yet. Qt's 'QQmlRefPointer<QQmlTypeNameCache> "
        "QV4::ExecutableCompilationUnit::typeNameCache() const': gives a "
        "type Python has no way to take yet.")
