"""
QQmlTypeCompiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTypeCompiler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList
from . import QQmlJS, QV4, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QTypeRevision, QUrl
  from . import QQmlCustomParser, QQmlError, QQmlImports
  from . import QQmlPropertyCacheVector, QQmlType, QQmlTypeLoader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QQmlError = WAIT['QQmlError']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeCompiler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeCompiler: a plain Python object standing in
  front of one C++ QQmlTypeCompiler.

  What exists
  -----------

  Every function of Qt's QQmlTypeCompiler that has a ritual and that Python
  can call so far, 24 names in all: 'tr', 'objectAt', 'objectCount',
  'resolvedIndex', 'implicitComponentForObject', 'stringAt',
  'listPropertyAssignBehavior', 'compilationErrors', 'recordError',
  'registerString', 'registerConstant', 'qmlUnit', 'url', 'typeLoader',
  'imports', 'propertyCaches', 'memoryPool', 'newStringRef', 'stringPool',
  'customParserCache', 'bindingAsString', 'addImport', 'resolvedType',
  'qmlTypeForComponent'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeCompiler::QQmlTypeCompiler(QQmlTypeLoader *typeLoader,
    QQmlTypeData *typeData, QmlIR::Document *document,
    QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache, const
    QV4::CompiledData::DependentTypesHasher &dependencyHasher)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QmlIR::Object *QQmlTypeCompiler::objectAt(int index)': takes in
    Python what 'const QmlIR::Object *QQmlTypeCompiler::objectAt(int index)
    const' takes.
  - Qt's 'QmlIR::PoolList<QmlIR::Function>::Iterator
    QQmlTypeCompiler::objectFunctionsBegin(const QmlIR::Object *object)
    const': gives a type Python has no way to take yet.
  - Qt's 'QmlIR::PoolList<QmlIR::Function>::Iterator
    QQmlTypeCompiler::objectFunctionsEnd(const QmlIR::Object *object) const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const':
    gives 'QList<QmlIR::Object *>', which has no cute class yet.
  - Qt's 'const QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
    const': takes in Python what 'QQmlPropertyCacheVector
    *QQmlTypeCompiler::propertyCaches()' takes.

  What has no ritual
  ------------------

  1 of the 34 functions Qt declares: 1 leans on 'invalidOverride()', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQmlTypeCompiler is created at the first use, not by
    'QQmlTypeCompiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeCompiler.
  - Each name of Qt's QQmlTypeCompiler that has no cute function yet,
    '__init__', 'compile', 'objectFunctionsBegin', 'objectFunctionsEnd',
    'qmlObjects', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQmlTypeCompiler::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeCompiler::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN16QQmlTypeCompiler2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeCompiler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def objectAt(self, index: int) -> Optional[QmlIR.Object]:
    """
    Calls Qt's 'const QmlIR::Object *QQmlTypeCompiler::objectAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#objectAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QmlIR.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QmlIR::Object *QQmlTypeCompiler::objectAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler8objectAtEi', index,
    )
    return QmlIR.Object._cuteAt(address)

  def objectCount(self) -> int:
    """
    Calls Qt's 'int QQmlTypeCompiler::objectCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#objectCount
    """
    #  int QQmlTypeCompiler::objectCount() const
    return self.uglySide.call('ritual_ZNK16QQmlTypeCompiler11objectCountEv')

  @overload(int)
  def resolvedIndex(self, index: int) -> int:
    """
    Calls Qt's 'int QQmlTypeCompiler::resolvedIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#resolvedIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QQmlTypeCompiler::resolvedIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler13resolvedIndexEi', index,
    )

  @overload(int)
  def implicitComponentForObject(self, childIndex: int) -> int:
    """
    Calls Qt's 'int QQmlTypeCompiler::implicitComponentForObject(int
    childIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#implicitComponentForObject

    Parameters
    ----------

    childIndex : int
      Passed on as it is.
    """
    #  int QQmlTypeCompiler::implicitComponentForObject(int childIndex) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler26implicitComponentForObjectEi',
        childIndex,
    )

  @overload(int)
  def stringAt(self, idx: int) -> str:
    """
    Calls Qt's 'QString QQmlTypeCompiler::stringAt(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#stringAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeCompiler::stringAt(int idx) const
    return self.uglySide.call('ritual_ZNK16QQmlTypeCompiler8stringAtEi', idx)

  def listPropertyAssignBehavior(
      self,
  ) -> QmlIR.Pragma.ListPropertyAssignBehaviorValue:
    """
    Calls Qt's 'ListPropertyAssignBehavior
    QQmlTypeCompiler::listPropertyAssignBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#listPropertyAssignBehavior

    Returns
    -------

    QmlIR.Pragma.ListPropertyAssignBehaviorValue
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QmlIR.Pragma.ListPropertyAssignBehaviorValue(number)' gives.
    """
    #  ListPropertyAssignBehavior
    #      QQmlTypeCompiler::listPropertyAssignBehavior() const
    return QmlIR.Pragma.ListPropertyAssignBehaviorValue(self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler26listPropertyAssignBehaviorEv',
    ))

  def compilationErrors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlTypeCompiler::compilationErrors()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#compilationErrors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlTypeCompiler::compilationErrors() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler17compilationErrorsEv',
    )
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  def qmlUnit(self) -> Optional[QV4.CompiledData.Unit]:
    """
    Calls Qt's 'const QV4::CompiledData::Unit *QQmlTypeCompiler::qmlUnit()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#qmlUnit

    Returns
    -------

    Optional[QV4.CompiledData.Unit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QV4::CompiledData::Unit *QQmlTypeCompiler::qmlUnit() const
    address = self.uglySide.call('ritual_ZNK16QQmlTypeCompiler7qmlUnitEv')
    return QV4.CompiledData.Unit._cuteAt(address)

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlTypeCompiler::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlTypeCompiler::url() const
    address = self.uglySide.call('ritual_ZNK16QQmlTypeCompiler3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def typeLoader(self) -> Optional[QQmlTypeLoader]:
    """
    Calls Qt's 'QQmlTypeLoader *QQmlTypeCompiler::typeLoader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#typeLoader

    Returns
    -------

    Optional[QQmlTypeLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoader *QQmlTypeCompiler::typeLoader() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler10typeLoaderEv',
    )
    from . import QQmlTypeLoader
    return QQmlTypeLoader._cuteAt(address)

  def imports(self) -> Optional[QQmlImports]:
    """
    Calls Qt's 'const QQmlImports *QQmlTypeCompiler::imports() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#imports

    Returns
    -------

    Optional[QQmlImports]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlImports *QQmlTypeCompiler::imports() const
    address = self.uglySide.call('ritual_ZNK16QQmlTypeCompiler7importsEv')
    from . import QQmlImports
    return QQmlImports._cuteAt(address)

  def stringPool(self) -> Optional[QV4.Compiler.StringTableGenerator]:
    """
    Calls Qt's 'const QV4::Compiler::StringTableGenerator
    *QQmlTypeCompiler::stringPool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#stringPool

    Returns
    -------

    Optional[QV4.Compiler.StringTableGenerator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QV4::Compiler::StringTableGenerator
    #      *QQmlTypeCompiler::stringPool() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler10stringPoolEv',
    )
    return QV4.Compiler.StringTableGenerator._cuteAt(address)

  def customParserCache(self) -> QHash[int, QQmlCustomParser]:
    """
    Calls Qt's 'const QHash<int, QQmlCustomParser *>
    &QQmlTypeCompiler::customParserCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#customParserCache

    Returns
    -------

    QHash[int, QQmlCustomParser]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  const QHash<int, QQmlCustomParser *>
    #      &QQmlTypeCompiler::customParserCache() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler17customParserCacheEv',
    )
    from . import QQmlCustomParser
    return QHash[int, QQmlCustomParser]._cuteOwning(address)

  @overload(WAIT['QmlIR.Object'], int)
  @overload(NoneType, int)
  def bindingAsString(
      self,
      object: Optional[QmlIR.Object],
      scriptIndex: int,
  ) -> str:
    """
    Calls Qt's 'QString QQmlTypeCompiler::bindingAsString(const QmlIR::Object
    *object, int scriptIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#bindingAsString

    Parameters
    ----------

    object : Optional[QmlIR.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scriptIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeCompiler::bindingAsString(const QmlIR::Object *object,
    #      int scriptIndex) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler15bindingAsStringEPKN5QmlIR6ObjectEi',
        self._addressOf(object), scriptIndex,
    )

  @overload(int)
  def resolvedType(self, id: int) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'QV4::ResolvedTypeReference
    *QQmlTypeCompiler::resolvedType(int id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#resolvedType

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
    #  QV4::ResolvedTypeReference *QQmlTypeCompiler::resolvedType(int id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler12resolvedTypeEi', id,
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

  @overload(QMetaType)
  def resolvedType(
      self,
      type: QMetaType,
  ) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'QV4::ResolvedTypeReference
    *QQmlTypeCompiler::resolvedType(QMetaType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#resolvedType

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
    #  QV4::ResolvedTypeReference *QQmlTypeCompiler::resolvedType(QMetaType
    #      type) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler12resolvedTypeE9QMetaType',
        self._valueOf(type),
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

  @overload()
  @overload(str)
  def qmlTypeForComponent(self, inlineComponentName: str = '') -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlTypeCompiler::qmlTypeForComponent(const QString
    &inlineComponentName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#qmlTypeForComponent

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
    #  QQmlType QQmlTypeCompiler::qmlTypeForComponent(const QString
    #      &inlineComponentName) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlTypeCompiler19qmlTypeForComponentERK7QString',
        inlineComponentName,
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeCompiler::QQmlTypeCompiler(QQmlTypeLoader *typeLoader,
    QQmlTypeData *typeData, QmlIR::Document *document,
    QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache, const
    QV4::CompiledData::DependentTypesHasher &dependencyHasher)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeCompiler.__init__' has no cute function yet. Qt's "
        "'QQmlTypeCompiler::QQmlTypeCompiler(QQmlTypeLoader *typeLoader, "
        "QQmlTypeData *typeData, QmlIR::Document *document, "
        "QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache, "
        "const QV4::CompiledData::DependentTypesHasher &dependencyHasher)': "
        "takes a type Python has no way to hand over yet.")

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

  @overload(WAIT['QV4.CompiledData.Location'], str)
  def recordError(
      self,
      location: QV4.CompiledData.Location,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeCompiler::recordError(const
    QV4::CompiledData::Location &location, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#recordError

    Parameters
    ----------

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypeCompiler::recordError(const QV4::CompiledData::Location
    #      &location, const QString &description)
    self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler11recordErrorERKN3QV412CompiledData8Loc'
        'ationERK7QString',
        self._valueOf(location), description,
    )

  @overload(WAIT['QQmlJS.DiagnosticMessage'])
  def recordError(self, message: QQmlJS.DiagnosticMessage) -> None:
    """
    Calls Qt's 'void QQmlTypeCompiler::recordError(const
    QQmlJS::DiagnosticMessage &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#recordError

    Parameters
    ----------

    message : QQmlJS.DiagnosticMessage
      Passed on as a value: Qt reads the C++ QQmlJS::DiagnosticMessage, which
      stays Python's own.
    """
    #  void QQmlTypeCompiler::recordError(const QQmlJS::DiagnosticMessage
    #      &message)
    self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler11recordErrorERKN6QQmlJS17DiagnosticMes'
        'sageE',
        self._valueOf(message),
    )

  @overload(QQmlError)
  def recordError(self, e: QQmlError) -> None:
    """
    Calls Qt's 'void QQmlTypeCompiler::recordError(const QQmlError &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#recordError

    Parameters
    ----------

    e : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  void QQmlTypeCompiler::recordError(const QQmlError &e)
    self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler11recordErrorERK9QQmlError',
        self._valueOf(e),
    )

  @overload(str)
  def registerString(self, str: str) -> int:
    """
    Calls Qt's 'int QQmlTypeCompiler::registerString(const QString &str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#registerString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QQmlTypeCompiler::registerString(const QString &str)
    return self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler14registerStringERK7QString', str,
    )

  @overload(int)
  def registerConstant(self, v: int) -> int:
    """
    Calls Qt's 'int QQmlTypeCompiler::registerConstant(QV4::ReturnedValue
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#registerConstant

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  int QQmlTypeCompiler::registerConstant(QV4::ReturnedValue v)
    return self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler16registerConstantEy', v,
    )

  def propertyCaches(self) -> Optional[QQmlPropertyCacheVector]:
    """
    Calls Qt's 'QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypecompiler.html#propertyCaches

    Returns
    -------

    Optional[QQmlPropertyCacheVector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
    address = self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler14propertyCachesEv',
    )
    from . import QQmlPropertyCacheVector
    return QQmlPropertyCacheVector._cuteAt(address)

  def memoryPool(self) -> Optional[QQmlJS.MemoryPool]:
    """
    Calls Qt's 'QQmlJS::MemoryPool *QQmlTypeCompiler::memoryPool()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#memoryPool

    Returns
    -------

    Optional[QQmlJS.MemoryPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJS::MemoryPool *QQmlTypeCompiler::memoryPool()
    address = self.uglySide.call('ritual_ZN16QQmlTypeCompiler10memoryPoolEv')
    return QQmlJS.MemoryPool._cuteAt(address)

  @overload(str)
  def newStringRef(self, string: str) -> str:
    """
    Calls Qt's 'QStringView QQmlTypeCompiler::newStringRef(const QString
    &string)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#newStringRef

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QQmlTypeCompiler::newStringRef(const QString &string)
    return self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler12newStringRefERK7QString', string,
    )

  @overload(str, str, QTypeRevision)
  def addImport(
      self,
      module: str,
      qualifier: str,
      version: QTypeRevision,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeCompiler::addImport(const QString &module, const
    QString &qualifier, QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypecompiler.html#addImport

    Parameters
    ----------

    module : str
      Passed on as it is: a QString is made of it for the call.

    qualifier : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlTypeCompiler::addImport(const QString &module, const QString
    #      &qualifier, QTypeRevision version)
    self.uglySide.call(
        'ritual_ZN16QQmlTypeCompiler9addImportERK7QStringS2_13QTypeRevision',
        module, qualifier, self._valueOf(version),
    )

  @staticmethod
  def compile(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QQmlTypeCompiler::compile()': leans on 'invalidOverride()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlTypeCompiler.compile' has no cute function yet. Qt's "
        "'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QQmlTypeCompiler::compile()': leans on 'invalidOverride()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def objectFunctionsBegin(*__, **_) -> Never:
    """
    Qt's 'QmlIR::PoolList<QmlIR::Function>::Iterator
    QQmlTypeCompiler::objectFunctionsBegin(const QmlIR::Object *object)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeCompiler.objectFunctionsBegin' has no cute function yet. "
        "Qt's 'QmlIR::PoolList<QmlIR::Function>::Iterator "
        "QQmlTypeCompiler::objectFunctionsBegin(const QmlIR::Object "
        "*object) const': gives a type Python has no way to take yet.")

  @staticmethod
  def objectFunctionsEnd(*__, **_) -> Never:
    """
    Qt's 'QmlIR::PoolList<QmlIR::Function>::Iterator
    QQmlTypeCompiler::objectFunctionsEnd(const QmlIR::Object *object) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeCompiler.objectFunctionsEnd' has no cute function yet. "
        "Qt's 'QmlIR::PoolList<QmlIR::Function>::Iterator "
        "QQmlTypeCompiler::objectFunctionsEnd(const QmlIR::Object *object) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def qmlObjects(*__, **_) -> Never:
    """
    Qt's 'QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const':
    gives 'QList<QmlIR::Object *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlTypeCompiler.qmlObjects' has no cute function yet. Qt's "
        "'QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const': "
        "gives 'QList<QmlIR::Object *>', which has no cute class yet.")
