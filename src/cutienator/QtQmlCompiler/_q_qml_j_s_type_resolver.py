"""
QQmlJSTypeResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstyperesolver_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSTypeResolver to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from ..QtQml import QQmlJS, QSOperator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSImporter, QQmlJSLogger, QQmlJSRegisterContent
  from . import QQmlJSRegisterContentPool, QQmlJSScopesById
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSImporter = WAIT['QQmlJSImporter']
  QQmlJSRegisterContent = WAIT['QQmlJSRegisterContent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSTypeResolver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSTypeResolver: a plain Python object standing in
  front of one C++ QQmlJSTypeResolver.

  What exists
  -----------

  Every function of Qt's QQmlJSTypeResolver that has a ritual and that Python
  can call so far, 35 names in all: 'registerContentPool', 'logger',
  'setParentMode', 'parentMode', 'setCloneMode', 'cloneMode',
  'jsGlobalObjectContent', 'isPrefix', 'seenModuleQualifiers', 'objectsById',
  'canCallJSFunctions', 'canAddressValueTypes', 'isPrimitive', 'isNumeric',
  'isIntegral', 'canHoldUndefined', 'isOptionalType', 'canConvertFromTo',
  'original', 'shadowed', 'extractNonVoidFromOptionalType',
  'typeForBinaryOperation', 'typeForArithmeticUnaryOperation', 'merge',
  'clearMergeCache', 'memberType', 'elementType', 'iteratorPointer',
  'convert', 'adjustTrackedType', 'generalizeType', 'memberEnumType',
  'checkEnums', 'lengthProperty', 'registerContentForName'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJSTypeResolver::init(QQmlJSImportVisitor *visitor,
    QQmlJS::AST::Node *program)': names 'QQmlJS::AST::Node', which has no
    cute class yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::voidType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::emptyType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::nullType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::realType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::floatType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int8Type() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint8Type() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int16Type() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint16Type() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int32Type() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint32Type() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int64Type() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint64Type() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::sizeType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::boolType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringListType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::byteArrayType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::urlType() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateTimeType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::timeType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::regexpType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantListType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantMapType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::varType() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qmlPropertyMapType()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsValueType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsPrimitiveType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::listPropertyType()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::metaObjectType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::functionType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsGlobalObject() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectListType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::arrayPrototype() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::forInIteratorPtr()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::forOfIteratorPtr()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qQmlScriptStringType()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::mathObject() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::consoleObject() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::typeForConst(QV4::ReturnedValue rv) const': gives a
    type Python has no way to take yet.
  - Qt's 'const QHash<QString, QQmlJS::ContextualType>
    &QQmlJSTypeResolver::importedTypes() const': gives a type Python has no
    way to take yet.
  - Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString>
    &QQmlJSTypeResolver::importedNames() const': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForName(const QString
    &name) const': gives a type Python has no way to take yet.
  - Qt's 'QString QQmlJSTypeResolver::nameForType(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopeForLocation(const
    QV4::CompiledData::Location &location) const': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::typeFromAST(QQmlJS::AST::Type *type) const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForId(const
    QQmlJSScope::ConstPtr &scope, const QString &name,
    QQmlJSScopesByIdOptions options) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopedType(const
    QQmlJSScope::ConstPtr &scope, const QString &name,
    QQmlJSScopesByIdOptions options) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'const QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler>
    &QQmlJSTypeResolver::signalHandlers() const': gives a type Python has no
    way to take yet.
  - Qt's 'bool QQmlJSTypeResolver::isPrimitive(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::isNumeric(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::isIntegral(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::isSignedInteger(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::isUnsignedInteger(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::isNativeArrayIndex(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::canHold(const QQmlJSScope::ConstPtr
    &container, const QQmlJSScope::ConstPtr &contained) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::canPopulate(const QQmlJSScope::ConstPtr
    &type, const QQmlJSScope::ConstPtr &argument, bool *isExtension) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::canConvertFromTo(const
    QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::areEquivalentLists(const
    QQmlJSScope::ConstPtr &a, const QQmlJSScope::ConstPtr &b) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::isTriviallyCopyable(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::inherits(const QQmlJSScope::ConstPtr
    &derived, const QQmlJSScope::ConstPtr &base) const': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::genericType(const
    QQmlJSScope::ConstPtr &type, ComponentIsGeneric allowComponent) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::storedType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::originalContainedType(QQmlJSRegisterContent
    container) const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::merge(const
    QQmlJSScope::ConstPtr &a, const QQmlJSScope::ConstPtr &b) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QQmlJSMetaMethod QQmlJSTypeResolver::selectConstructor(const
    QQmlJSScope::ConstPtr &type, const QQmlJSScope::ConstPtr &argument, bool
    *isExtension) const': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::literalType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::operationType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::namedType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::syntheticType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::scopedType(QQmlJSRegisterContent scope, const QString
    &name, int lookupIndex, QQmlJSScopesByIdOptions options) const': names
    the enum 'QQmlJSScopesByIdOption', whose class cannot be named here.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::returnType(const
    QQmlJSMetaMethod &method, const QQmlJSScope::ConstPtr &returnType,
    QQmlJSRegisterContent scope) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::extensionType(const
    QQmlJSScope::ConstPtr &extension, QQmlJSRegisterContent base) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::baseType(const
    QQmlJSScope::ConstPtr &base, QQmlJSRegisterContent derived) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::parentScope(const
    QQmlJSScope::ConstPtr &parent, QQmlJSRegisterContent child) const': takes
    a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::convert(QQmlJSRegisterContent from, const
    QQmlJSScope::ConstPtr &to) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent
    tracked, const QQmlJSScope::ConstPtr &conversion) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlJSTypeResolver::adjustOriginalType(QQmlJSRegisterContent
    tracked, const QQmlJSScope::ConstPtr &conversion) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QQmlJSTypeResolver::canPrimitivelyConvertFromTo(const
    QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::containedTypeForName(const QString &name) const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::resolveParentProperty(const QString &name, const
    QQmlJSScope::ConstPtr &base, const QQmlJSScope::ConstPtr &propType)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlJSTypeResolver is created at the first use, not by
    'QQmlJSTypeResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSTypeResolver.
  - Each name of Qt's QQmlJSTypeResolver that has no cute function yet,
    'adjustOriginalType', 'areEquivalentLists', 'arrayPrototype', 'baseType',
    'boolType', 'byteArrayType', 'canHold', 'canPopulate',
    'canPrimitivelyConvertFromTo', 'consoleObject', 'containedTypeForName',
    'dateTimeType', 'dateType', 'emptyType', 'extensionType', 'floatType',
    'forInIteratorPtr', 'forOfIteratorPtr', 'functionType', 'genericType',
    'importedNames', 'importedTypes', 'inherits', 'init', 'int16Type',
    'int32Type', 'int64Type', 'int8Type', 'isNativeArrayIndex',
    'isSignedInteger', 'isTriviallyCopyable', 'isUnsignedInteger',
    'jsGlobalObject', 'jsPrimitiveType', 'jsValueType', 'listPropertyType',
    'literalType', 'mathObject', 'metaObjectType', 'nameForType',
    'namedType', 'nullType', 'operationType', 'originalContainedType',
    'parentScope', 'qObjectListType', 'qObjectType', 'qQmlScriptStringType',
    'qmlPropertyMapType', 'realType', 'regexpType', 'resolveParentProperty',
    'returnType', 'scopeForLocation', 'scopedType', 'selectConstructor',
    'signalHandlers', 'sizeType', 'storedType', 'stringListType',
    'stringType', 'syntheticType', 'timeType', 'typeForConst', 'typeForId',
    'typeForName', 'typeFromAST', 'uint16Type', 'uint32Type', 'uint64Type',
    'uint8Type', 'urlType', 'varType', 'variantListType', 'variantMapType',
    'voidType', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQmlJSTypeResolver, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CloneMode(CuteNum):
    """
    The enum 'QQmlJSTypeResolver::CloneMode' of Qt, with the 2 names Qt gives
    in it.
    """

    CloneTypes = Kee[int](0)
    DoNotCloneTypes = Kee[int](1)

  class ComponentIsGeneric(CuteNum, scoped=True):
    """
    The enum 'QQmlJSTypeResolver::ComponentIsGeneric' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class ParentMode(CuteNum):
    """
    The enum 'QQmlJSTypeResolver::ParentMode' of Qt, with the 2 names Qt
    gives in it.
    """

    UseDocumentParent = Kee[int](0)
    UseParentProperty = Kee[int](1)

  class UnaryOperator(CuteNum, scoped=True):
    """
    The enum 'QQmlJSTypeResolver::UnaryOperator' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Not = Kee[int](0)
    Plus = Kee[int](1)
    Minus = Kee[int](2)
    Increment = Kee[int](3)
    Decrement = Kee[int](4)
    Complement = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSTypeResolver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def registerContentPool(self) -> Optional[QQmlJSRegisterContentPool]:
    """
    Calls Qt's 'QQmlJSRegisterContentPool
    *QQmlJSTypeResolver::registerContentPool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#registerContentPool

    Returns
    -------

    Optional[QQmlJSRegisterContentPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJSRegisterContentPool *QQmlJSTypeResolver::registerContentPool()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver19registerContentPoolEv',
    )
    from . import QQmlJSRegisterContentPool
    return QQmlJSRegisterContentPool._cuteAt(address)

  def logger(self) -> Optional[QQmlJSLogger]:
    """
    Calls Qt's 'QQmlJSLogger *QQmlJSTypeResolver::logger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#logger

    Returns
    -------

    Optional[QQmlJSLogger]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJSLogger *QQmlJSTypeResolver::logger() const
    address = self.uglySide.call('ritual_ZNK18QQmlJSTypeResolver6loggerEv')
    from . import QQmlJSLogger
    return QQmlJSLogger._cuteAt(address)

  def parentMode(self) -> ParentMode:
    """
    Calls Qt's 'ParentMode QQmlJSTypeResolver::parentMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#parentMode

    Returns
    -------

    ParentMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ParentMode(number)'
      gives.
    """
    #  ParentMode QQmlJSTypeResolver::parentMode() const
    return QQmlJSTypeResolver.ParentMode(self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver10parentModeEv',
    ))

  def cloneMode(self) -> CloneMode:
    """
    Calls Qt's 'CloneMode QQmlJSTypeResolver::cloneMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#cloneMode

    Returns
    -------

    CloneMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CloneMode(number)' gives.
    """
    #  CloneMode QQmlJSTypeResolver::cloneMode() const
    return QQmlJSTypeResolver.CloneMode(self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver9cloneModeEv',
    ))

  def jsGlobalObjectContent(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::jsGlobalObjectContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#jsGlobalObjectContent

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSTypeResolver::jsGlobalObjectContent()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver21jsGlobalObjectContentEv',
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(str)
  def isPrefix(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::isPrefix(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#isPrefix

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSTypeResolver::isPrefix(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver8isPrefixERK7QString', name,
    )

  def seenModuleQualifiers(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSTypeResolver::seenModuleQualifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#seenModuleQualifiers

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSTypeResolver::seenModuleQualifiers() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver20seenModuleQualifiersEv',
    )
    return QStringList._cuteOwning(address)

  def objectsById(self) -> QQmlJSScopesById:
    """
    Calls Qt's 'const QQmlJSScopesById &QQmlJSTypeResolver::objectsById()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#objectsById

    Returns
    -------

    QQmlJSScopesById
      A new cute QQmlJSScopesById around the copy Qt gave back. Python owns
      it.
    """
    #  const QQmlJSScopesById &QQmlJSTypeResolver::objectsById() const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver11objectsByIdEv',
    )
    from . import QQmlJSScopesById
    return QQmlJSScopesById._cuteOwning(address)

  def canCallJSFunctions(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::canCallJSFunctions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#canCallJSFunctions
    """
    #  bool QQmlJSTypeResolver::canCallJSFunctions() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver18canCallJSFunctionsEv',
    )

  def canAddressValueTypes(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::canAddressValueTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#canAddressValueTypes
    """
    #  bool QQmlJSTypeResolver::canAddressValueTypes() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver20canAddressValueTypesEv',
    )

  @overload(QQmlJSRegisterContent)
  def isPrimitive(self, type: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::isPrimitive(QQmlJSRegisterContent
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#isPrimitive

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::isPrimitive(QQmlJSRegisterContent type) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver11isPrimitiveE21QQmlJSRegisterConten'
        't',
        self._valueOf(type),
    )

  @overload(QQmlJSRegisterContent)
  def isNumeric(self, type: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::isNumeric(QQmlJSRegisterContent
    type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#isNumeric

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::isNumeric(QQmlJSRegisterContent type) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver9isNumericE21QQmlJSRegisterContent',
        self._valueOf(type),
    )

  @overload(QQmlJSRegisterContent)
  def isIntegral(self, type: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::isIntegral(QQmlJSRegisterContent
    type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#isIntegral

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::isIntegral(QQmlJSRegisterContent type) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver10isIntegralE21QQmlJSRegisterContent',
        self._valueOf(type),
    )

  @overload(QQmlJSRegisterContent)
  def canHoldUndefined(self, content: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypeResolver::canHoldUndefined(QQmlJSRegisterContent content)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#canHoldUndefined

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::canHoldUndefined(QQmlJSRegisterContent
    #      content) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver16canHoldUndefinedE21QQmlJSRegisterC'
        'ontent',
        self._valueOf(content),
    )

  @overload(QQmlJSRegisterContent)
  def isOptionalType(self, content: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::isOptionalType(QQmlJSRegisterContent
    content) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#isOptionalType

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::isOptionalType(QQmlJSRegisterContent content)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver14isOptionalTypeE21QQmlJSRegisterCon'
        'tent',
        self._valueOf(content),
    )

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent)
  def canConvertFromTo(
      self,
      from_: QQmlJSRegisterContent,
      to: QQmlJSRegisterContent,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypeResolver::canConvertFromTo(QQmlJSRegisterContent from,
    QQmlJSRegisterContent to) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#canConvertFromTo

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    to : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::canConvertFromTo(QQmlJSRegisterContent from,
    #      QQmlJSRegisterContent to) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver16canConvertFromToE21QQmlJSRegisterC'
        'ontentS0_',
        self._valueOf(from_), self._valueOf(to),
    )

  @overload(QQmlJSRegisterContent)
  def original(self, type: QQmlJSRegisterContent) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::original(QQmlJSRegisterContent type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#original

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::original(QQmlJSRegisterContent type) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver8originalE21QQmlJSRegisterContent',
        self._valueOf(type),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent)
  def shadowed(self, type: QQmlJSRegisterContent) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::shadowed(QQmlJSRegisterContent type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#shadowed

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::shadowed(QQmlJSRegisterContent type) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver8shadowedE21QQmlJSRegisterContent',
        self._valueOf(type),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent)
  def extractNonVoidFromOptionalType(
      self,
      content: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::extractNonVoidFromOptionalType(QQmlJSRegisterContent
    content) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::extractNonVoidFromOptionalType(
    #      QQmlJSRegisterContent content) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver30extractNonVoidFromOptionalTypeE21Q'
        'QmlJSRegisterContent',
        self._valueOf(content),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QSOperator.Op, QQmlJSRegisterContent, QQmlJSRegisterContent)
  def typeForBinaryOperation(
      self,
      oper: QSOperator.Op,
      left: QQmlJSRegisterContent,
      right: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::typeForBinaryOperation(QSOperator::Op oper,
    QQmlJSRegisterContent left, QQmlJSRegisterContent right) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#typeForBinaryOperation

    Parameters
    ----------

    oper : QSOperator.Op
      Passed on as its number.

    left : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    right : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::typeForBinaryOperation(QSOperator::Op oper,
    #      QQmlJSRegisterContent left, QQmlJSRegisterContent right) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver22typeForBinaryOperationEN10QSOperat'
        'or2OpE21QQmlJSRegisterContentS2_',
        oper.value, self._valueOf(left), self._valueOf(right),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(UnaryOperator, QQmlJSRegisterContent)
  def typeForArithmeticUnaryOperation(
      self,
      op: UnaryOperator,
      operand: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::typeForArithmeticUnaryOperation(UnaryOperator op,
    QQmlJSRegisterContent operand) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html

    Parameters
    ----------

    op : UnaryOperator
      Passed on as its number.

    operand : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::typeForArithmeticUnaryOperation(UnaryOperator
    #      op, QQmlJSRegisterContent operand) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver31typeForArithmeticUnaryOperationENS'
        '_13UnaryOperatorE21QQmlJSRegisterContent',
        op.value, self._valueOf(operand),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent)
  def merge(
      self,
      a: QQmlJSRegisterContent,
      b: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::merge(QQmlJSRegisterContent a, QQmlJSRegisterContent
    b) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#merge

    Parameters
    ----------

    a : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    b : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSTypeResolver::merge(QQmlJSRegisterContent
    #      a, QQmlJSRegisterContent b) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver5mergeE21QQmlJSRegisterContentS0_',
        self._valueOf(a), self._valueOf(b),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, str, int)
  def memberType(
      self,
      type: QQmlJSRegisterContent,
      name: str,
      lookupIndex: int,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::memberType(QQmlJSRegisterContent type, const QString
    &name, int lookupIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#memberType

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    lookupIndex : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::memberType(QQmlJSRegisterContent type, const
    #      QString &name, int lookupIndex) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver10memberTypeE21QQmlJSRegisterContent'
        'RK7QStringi',
        self._valueOf(type), name, lookupIndex,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, str, int, int)
  def memberType(
      self,
      type: QQmlJSRegisterContent,
      name: str,
      baseLookupIndex: int,
      resultLookupIndex: int,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::memberType(QQmlJSRegisterContent type, const QString
    &name, int baseLookupIndex, int resultLookupIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#memberType

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    baseLookupIndex : int
      Passed on as it is.

    resultLookupIndex : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::memberType(QQmlJSRegisterContent type, const
    #      QString &name, int baseLookupIndex, int resultLookupIndex) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver10memberTypeE21QQmlJSRegisterContent'
        'RK7QStringii',
        self._valueOf(type), name, baseLookupIndex, resultLookupIndex,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent)
  def elementType(
      self,
      list: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::elementType(QQmlJSRegisterContent list) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#elementType

    Parameters
    ----------

    list : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::elementType(QQmlJSRegisterContent list) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver11elementTypeE21QQmlJSRegisterConten'
        't',
        self._valueOf(list),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, QQmlJS.AST.ForEachType, int)
  def iteratorPointer(
      self,
      listType: QQmlJSRegisterContent,
      type: QQmlJS.AST.ForEachType,
      lookupIndex: int,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::iteratorPointer(QQmlJSRegisterContent listType,
    QQmlJS::AST::ForEachType type, int lookupIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#iteratorPointer

    Parameters
    ----------

    listType : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    type : QQmlJS.AST.ForEachType
      Passed on as its number.

    lookupIndex : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::iteratorPointer(QQmlJSRegisterContent
    #      listType, QQmlJS::AST::ForEachType type, int lookupIndex) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver15iteratorPointerE21QQmlJSRegisterCo'
        'ntentN6QQmlJS3AST11ForEachTypeEi',
        self._valueOf(listType), type.value, lookupIndex,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent)
  def convert(
      self,
      from_: QQmlJSRegisterContent,
      to: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::convert(QQmlJSRegisterContent from,
    QQmlJSRegisterContent to) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#convert

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    to : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::convert(QQmlJSRegisterContent from,
    #      QQmlJSRegisterContent to) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver7convertE21QQmlJSRegisterContentS0_',
        self._valueOf(from_), self._valueOf(to),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent)
  def adjustTrackedType(
      self,
      tracked: QQmlJSRegisterContent,
      conversion: QQmlJSRegisterContent,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent tracked,
    QQmlJSRegisterContent conversion) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#adjustTrackedType

    Parameters
    ----------

    tracked : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    conversion : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent
    #      tracked, QQmlJSRegisterContent conversion) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver17adjustTrackedTypeE21QQmlJSRegister'
        'ContentS0_',
        self._valueOf(tracked), self._valueOf(conversion),
    )

  @overload(QQmlJSRegisterContent, QList[QQmlJSRegisterContent])
  def adjustTrackedType(
      self,
      tracked: QQmlJSRegisterContent,
      conversions: QList[QQmlJSRegisterContent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent tracked,
    const QList<QQmlJSRegisterContent> &conversions) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#adjustTrackedType

    Parameters
    ----------

    tracked : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    conversions : QList[QQmlJSRegisterContent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent
    #      tracked, const QList<QQmlJSRegisterContent> &conversions) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver17adjustTrackedTypeE21QQmlJSRegister'
        'ContentRK5QListIS0_E',
        self._valueOf(tracked), self._valueOf(conversions),
    )

  @overload(QQmlJSRegisterContent, str)
  def memberEnumType(
      self,
      type: QQmlJSRegisterContent,
      name: str,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::memberEnumType(QQmlJSRegisterContent type, const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#memberEnumType

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypeResolver::memberEnumType(QQmlJSRegisterContent type,
    #      const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver14memberEnumTypeE21QQmlJSRegisterCon'
        'tentRK7QString',
        self._valueOf(type), name,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent, str, QQmlJSRegisterContent)
  @overload(QQmlJSRegisterContent, str, NoneType)
  def checkEnums(
      self,
      scope: QQmlJSRegisterContent,
      name: str,
      result: Optional[QQmlJSRegisterContent],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypeResolver::checkEnums(QQmlJSRegisterContent
    scope, const QString &name, QQmlJSRegisterContent *result) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstyperesolver.html#checkEnums

    Parameters
    ----------

    scope : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    result : Optional[QQmlJSRegisterContent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSTypeResolver::checkEnums(QQmlJSRegisterContent scope, const
    #      QString &name, QQmlJSRegisterContent *result) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver10checkEnumsE21QQmlJSRegisterContent'
        'RK7QStringPS0_',
        self._valueOf(scope), name, self._addressOf(result),
    )

  @overload(bool, QQmlJSRegisterContent)
  def lengthProperty(
      self,
      isWritable: bool,
      scope: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::lengthProperty(bool
    isWritable, QQmlJSRegisterContent scope) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#lengthProperty

    Parameters
    ----------

    isWritable : bool
      Passed on as it is.

    scope : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSTypeResolver::lengthProperty(bool
    #      isWritable, QQmlJSRegisterContent scope) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver14lengthPropertyEb21QQmlJSRegisterCo'
        'ntent',
        isWritable, self._valueOf(scope),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(str)
  @overload(str, QQmlJSRegisterContent)
  def registerContentForName(
      self,
      name: str,
      scopeType: Optional[QQmlJSRegisterContent] = None,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypeResolver::registerContentForName(const QString &name,
    QQmlJSRegisterContent scopeType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#registerContentForName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    scopeType : Optional[QQmlJSRegisterContent]
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own. May be left out, as in Qt: a new
      'QQmlJSRegisterContent()' is then passed on.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSTypeResolver::registerContentForName(const
    #      QString &name, QQmlJSRegisterContent scopeType) const
    if scopeType is None:
      from . import QQmlJSRegisterContent
      scopeType = QQmlJSRegisterContent()
    address = self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver22registerContentForNameERK7QString2'
        '1QQmlJSRegisterContent',
        name, self._valueOf(scopeType),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ParentMode)
  def setParentMode(self, mode: ParentMode) -> None:
    """
    Calls Qt's 'void QQmlJSTypeResolver::setParentMode(ParentMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#setParentMode

    Parameters
    ----------

    mode : ParentMode
      Passed on as its number.
    """
    #  void QQmlJSTypeResolver::setParentMode(ParentMode mode)
    self.uglySide.call(
        'ritual_ZN18QQmlJSTypeResolver13setParentModeENS_10ParentModeE',
        mode.value,
    )

  @overload(CloneMode)
  def setCloneMode(self, mode: CloneMode) -> None:
    """
    Calls Qt's 'void QQmlJSTypeResolver::setCloneMode(CloneMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#setCloneMode

    Parameters
    ----------

    mode : CloneMode
      Passed on as its number.
    """
    #  void QQmlJSTypeResolver::setCloneMode(CloneMode mode)
    self.uglySide.call(
        'ritual_ZN18QQmlJSTypeResolver12setCloneModeENS_9CloneModeE',
        mode.value,
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

  @overload(QQmlJSImporter)
  @overload(NoneType)
  def __init__(self, importer: Optional[QQmlJSImporter]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSTypeResolver::QQmlJSTypeResolver(QQmlJSImporter *importer)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#QQmlJSTypeResolver

    Parameters
    ----------

    importer : Optional[QQmlJSImporter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJSTypeResolver::QQmlJSTypeResolver(QQmlJSImporter *importer)
    self._noteCreation(QQmlJSTypeResolver, lambda: Rituals.call(
        'ritual_ZN18QQmlJSTypeResolverC1EP14QQmlJSImporter',
        self._addressOf(importer),
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

  def clearMergeCache(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypeResolver::clearMergeCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#clearMergeCache
    """
    #  void QQmlJSTypeResolver::clearMergeCache() const
    self.uglySide.call('ritual_ZNK18QQmlJSTypeResolver15clearMergeCacheEv')

  @overload(QQmlJSRegisterContent)
  def generalizeType(self, type: QQmlJSRegisterContent) -> None:
    """
    Calls Qt's 'void QQmlJSTypeResolver::generalizeType(QQmlJSRegisterContent
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstyperesolver.html#generalizeType

    Parameters
    ----------

    type : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypeResolver::generalizeType(QQmlJSRegisterContent type)
    #      const
    self.uglySide.call(
        'ritual_ZNK18QQmlJSTypeResolver14generalizeTypeE21QQmlJSRegisterCon'
        'tent',
        self._valueOf(type),
    )

  @staticmethod
  def adjustOriginalType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSTypeResolver::adjustOriginalType(QQmlJSRegisterContent
    tracked, const QQmlJSScope::ConstPtr &conversion) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.adjustOriginalType' has no cute function yet. "
        "Qt's 'void "
        "QQmlJSTypeResolver::adjustOriginalType(QQmlJSRegisterContent "
        "tracked, const QQmlJSScope::ConstPtr &conversion) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def areEquivalentLists(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::areEquivalentLists(const
    QQmlJSScope::ConstPtr &a, const QQmlJSScope::ConstPtr &b) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.areEquivalentLists' has no cute function yet. "
        "Qt's 'bool QQmlJSTypeResolver::areEquivalentLists(const "
        "QQmlJSScope::ConstPtr &a, const QQmlJSScope::ConstPtr &b) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def arrayPrototype(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::arrayPrototype() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.arrayPrototype' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::arrayPrototype() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def baseType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::baseType(const
    QQmlJSScope::ConstPtr &base, QQmlJSRegisterContent derived) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.baseType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::baseType(const "
        "QQmlJSScope::ConstPtr &base, QQmlJSRegisterContent derived) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def boolType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::boolType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.boolType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::boolType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def byteArrayType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::byteArrayType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.byteArrayType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::byteArrayType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def canHold(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::canHold(const QQmlJSScope::ConstPtr
    &container, const QQmlJSScope::ConstPtr &contained) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.canHold' has no cute function yet. Qt's 'bool "
        "QQmlJSTypeResolver::canHold(const QQmlJSScope::ConstPtr "
        "&container, const QQmlJSScope::ConstPtr &contained) const': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def canPopulate(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::canPopulate(const QQmlJSScope::ConstPtr
    &type, const QQmlJSScope::ConstPtr &argument, bool *isExtension) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.canPopulate' has no cute function yet. Qt's "
        "'bool QQmlJSTypeResolver::canPopulate(const QQmlJSScope::ConstPtr "
        "&type, const QQmlJSScope::ConstPtr &argument, bool *isExtension) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def canPrimitivelyConvertFromTo(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::canPrimitivelyConvertFromTo(const
    QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.canPrimitivelyConvertFromTo' has no cute "
        "function yet. Qt's 'bool "
        "QQmlJSTypeResolver::canPrimitivelyConvertFromTo(const "
        "QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def consoleObject(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::consoleObject() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.consoleObject' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::consoleObject() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def containedTypeForName(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::containedTypeForName(const QString &name) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.containedTypeForName' has no cute function "
        "yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::containedTypeForName(const QString &name) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def dateTimeType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateTimeType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.dateTimeType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateTimeType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def dateType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.dateType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def emptyType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::emptyType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.emptyType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::emptyType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def extensionType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::extensionType(const
    QQmlJSScope::ConstPtr &extension, QQmlJSRegisterContent base) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.extensionType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::extensionType(const "
        "QQmlJSScope::ConstPtr &extension, QQmlJSRegisterContent base) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def floatType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::floatType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.floatType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::floatType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def forInIteratorPtr(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::forInIteratorPtr()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.forInIteratorPtr' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::forInIteratorPtr() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def forOfIteratorPtr(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::forOfIteratorPtr()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.forOfIteratorPtr' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::forOfIteratorPtr() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def functionType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::functionType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.functionType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::functionType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def genericType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::genericType(const
    QQmlJSScope::ConstPtr &type, ComponentIsGeneric allowComponent) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.genericType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::genericType(const "
        "QQmlJSScope::ConstPtr &type, ComponentIsGeneric allowComponent) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def importedNames(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString>
    &QQmlJSTypeResolver::importedNames() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.importedNames' has no cute function yet. Qt's "
        "'const QMultiHash<QQmlJSScope::ConstPtr, QString> "
        "&QQmlJSTypeResolver::importedNames() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def importedTypes(*__, **_) -> Never:
    """
    Qt's 'const QHash<QString, QQmlJS::ContextualType>
    &QQmlJSTypeResolver::importedTypes() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.importedTypes' has no cute function yet. Qt's "
        "'const QHash<QString, QQmlJS::ContextualType> "
        "&QQmlJSTypeResolver::importedTypes() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def inherits(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::inherits(const QQmlJSScope::ConstPtr
    &derived, const QQmlJSScope::ConstPtr &base) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.inherits' has no cute function yet. Qt's 'bool "
        "QQmlJSTypeResolver::inherits(const QQmlJSScope::ConstPtr &derived, "
        "const QQmlJSScope::ConstPtr &base) const': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSTypeResolver::init(QQmlJSImportVisitor *visitor,
    QQmlJS::AST::Node *program)': names 'QQmlJS::AST::Node', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.init' has no cute function yet. Qt's 'void "
        "QQmlJSTypeResolver::init(QQmlJSImportVisitor *visitor, "
        "QQmlJS::AST::Node *program)': names 'QQmlJS::AST::Node', which has "
        "no cute class yet.")

  @staticmethod
  def int16Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int16Type() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.int16Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int16Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def int32Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int32Type() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.int32Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int32Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def int64Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int64Type() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.int64Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int64Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def int8Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int8Type() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.int8Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::int8Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def isNativeArrayIndex(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::isNativeArrayIndex(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.isNativeArrayIndex' has no cute function yet. "
        "Qt's 'bool QQmlJSTypeResolver::isNativeArrayIndex(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def isSignedInteger(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::isSignedInteger(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.isSignedInteger' has no cute function yet. "
        "Qt's 'bool QQmlJSTypeResolver::isSignedInteger(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def isTriviallyCopyable(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::isTriviallyCopyable(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.isTriviallyCopyable' has no cute function yet. "
        "Qt's 'bool QQmlJSTypeResolver::isTriviallyCopyable(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def isUnsignedInteger(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypeResolver::isUnsignedInteger(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.isUnsignedInteger' has no cute function yet. "
        "Qt's 'bool QQmlJSTypeResolver::isUnsignedInteger(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def jsGlobalObject(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsGlobalObject() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.jsGlobalObject' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsGlobalObject() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def jsPrimitiveType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsPrimitiveType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.jsPrimitiveType' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsPrimitiveType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def jsValueType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsValueType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.jsValueType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsValueType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def listPropertyType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::listPropertyType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.listPropertyType' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::listPropertyType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def literalType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::literalType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.literalType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::literalType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def mathObject(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::mathObject() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.mathObject' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::mathObject() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def metaObjectType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::metaObjectType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.metaObjectType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::metaObjectType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def nameForType(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSTypeResolver::nameForType(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.nameForType' has no cute function yet. Qt's "
        "'QString QQmlJSTypeResolver::nameForType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def namedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::namedType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.namedType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::namedType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def nullType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::nullType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.nullType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::nullType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def operationType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::operationType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.operationType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::operationType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def originalContainedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::originalContainedType(QQmlJSRegisterContent
    container) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.originalContainedType' has no cute function "
        "yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::originalContainedType(QQmlJSRegisterContent "
        "container) const': gives a type Python has no way to take yet.")

  @staticmethod
  def parentScope(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::parentScope(const
    QQmlJSScope::ConstPtr &parent, QQmlJSRegisterContent child) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.parentScope' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::parentScope(const "
        "QQmlJSScope::ConstPtr &parent, QQmlJSRegisterContent child) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def qObjectListType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectListType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.qObjectListType' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectListType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def qObjectType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.qObjectType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def qQmlScriptStringType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qQmlScriptStringType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.qQmlScriptStringType' has no cute function "
        "yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::qQmlScriptStringType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def qmlPropertyMapType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::qmlPropertyMapType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.qmlPropertyMapType' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::qmlPropertyMapType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def realType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::realType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.realType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::realType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def regexpType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::regexpType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.regexpType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::regexpType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def resolveParentProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::resolveParentProperty(const QString &name, const
    QQmlJSScope::ConstPtr &base, const QQmlJSScope::ConstPtr &propType)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.resolveParentProperty' has no cute function "
        "yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::resolveParentProperty(const QString &name, "
        "const QQmlJSScope::ConstPtr &base, const QQmlJSScope::ConstPtr "
        "&propType) const': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def returnType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::returnType(const
    QQmlJSMetaMethod &method, const QQmlJSScope::ConstPtr &returnType,
    QQmlJSRegisterContent scope) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.returnType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::returnType(const "
        "QQmlJSMetaMethod &method, const QQmlJSScope::ConstPtr &returnType, "
        "QQmlJSRegisterContent scope) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def scopeForLocation(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopeForLocation(const
    QV4::CompiledData::Location &location) const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.scopeForLocation' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::scopeForLocation(const "
        "QV4::CompiledData::Location &location) const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def scopedType(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopedType(const
      QQmlJSScope::ConstPtr &scope, const QString &name,
      QQmlJSScopesByIdOptions options) const': takes a type Python has no way
      to hand over yet.
    - Qt's 'QQmlJSRegisterContent
      QQmlJSTypeResolver::scopedType(QQmlJSRegisterContent scope, const
      QString &name, int lookupIndex, QQmlJSScopesByIdOptions options)
      const': names the enum 'QQmlJSScopesByIdOption', whose class cannot be
      named here.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.scopedType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopedType(const "
        "QQmlJSScope::ConstPtr &scope, const QString &name, "
        "QQmlJSScopesByIdOptions options) const': takes a type Python has "
        "no way to hand over yet. Qt's 'QQmlJSRegisterContent "
        "QQmlJSTypeResolver::scopedType(QQmlJSRegisterContent scope, const "
        "QString &name, int lookupIndex, QQmlJSScopesByIdOptions options) "
        "const': names the enum 'QQmlJSScopesByIdOption', whose class "
        "cannot be named here.")

  @staticmethod
  def selectConstructor(*__, **_) -> Never:
    """
    Qt's 'QQmlJSMetaMethod QQmlJSTypeResolver::selectConstructor(const
    QQmlJSScope::ConstPtr &type, const QQmlJSScope::ConstPtr &argument, bool
    *isExtension) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.selectConstructor' has no cute function yet. "
        "Qt's 'QQmlJSMetaMethod QQmlJSTypeResolver::selectConstructor(const "
        "QQmlJSScope::ConstPtr &type, const QQmlJSScope::ConstPtr "
        "&argument, bool *isExtension) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def signalHandlers(*__, **_) -> Never:
    """
    Qt's 'const QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler>
    &QQmlJSTypeResolver::signalHandlers() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.signalHandlers' has no cute function yet. Qt's "
        "'const QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler> "
        "&QQmlJSTypeResolver::signalHandlers() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def sizeType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::sizeType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.sizeType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::sizeType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def storedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::storedType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.storedType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::storedType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def stringListType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringListType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.stringListType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringListType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def stringType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.stringType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def syntheticType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSTypeResolver::syntheticType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.syntheticType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSTypeResolver::syntheticType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def timeType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::timeType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.timeType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::timeType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def typeForConst(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::typeForConst(QV4::ReturnedValue rv) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.typeForConst' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::typeForConst(QV4::ReturnedValue rv) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def typeForId(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForId(const
    QQmlJSScope::ConstPtr &scope, const QString &name,
    QQmlJSScopesByIdOptions options) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.typeForId' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForId(const "
        "QQmlJSScope::ConstPtr &scope, const QString &name, "
        "QQmlJSScopesByIdOptions options) const': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def typeForName(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForName(const QString
    &name) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.typeForName' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForName(const "
        "QString &name) const': gives a type Python has no way to take yet.")

  @staticmethod
  def typeFromAST(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr
    QQmlJSTypeResolver::typeFromAST(QQmlJS::AST::Type *type) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.typeFromAST' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr "
        "QQmlJSTypeResolver::typeFromAST(QQmlJS::AST::Type *type) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def uint16Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint16Type() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.uint16Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint16Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def uint32Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint32Type() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.uint32Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint32Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def uint64Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint64Type() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.uint64Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint64Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def uint8Type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint8Type() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.uint8Type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint8Type() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def urlType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::urlType() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.urlType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::urlType() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def varType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::varType() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.varType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::varType() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def variantListType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantListType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.variantListType' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantListType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def variantMapType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantMapType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.variantMapType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantMapType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def voidType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSTypeResolver::voidType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypeResolver.voidType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSTypeResolver::voidType() const': "
        "gives a type Python has no way to take yet.")
