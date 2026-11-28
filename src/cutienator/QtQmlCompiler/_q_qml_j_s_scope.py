"""
QQmlJSScope binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSScope to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList, QStringList
from ..QtQml import QQmlJS
from . import QQmlSA, QQmlJSMetaMethod

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QTypeRevision
  from . import QQmlJSAnnotation, QQmlJSMetaEnum, QQmlJSMetaProperty
  from . import QQmlJSMetaPropertyBinding
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSAnnotation = WAIT['QQmlJSAnnotation']
  QQmlJSMetaEnum = WAIT['QQmlJSMetaEnum']
  QQmlJSMetaProperty = WAIT['QQmlJSMetaProperty']
  QQmlJSMetaPropertyBinding = WAIT['QQmlJSMetaPropertyBinding']


class QQmlJSScope(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSScope: a plain Python object standing in front
  of one C++ QQmlJSScope.

  What exists
  -----------

  Every function of Qt's QQmlJSScope that has a ritual and that Python can
  call so far, 136 names in all: 'insertJSIdentifier', 'scopeType',
  'setScopeType', 'addOwnMethod', 'ownMethods', 'hasOwnMethod', 'hasMethod',
  'methods', 'addOwnEnumeration', 'ownEnumerations', 'ownEnumeration',
  'hasOwnEnumeration', 'hasEnumeration', 'hasEnumerationKey',
  'hasOwnEnumerationKey', 'enumeration', 'enumerations', 'setAnnotations',
  'annotations', 'filePath', 'setFilePath', 'lineNumber', 'setLineNumber',
  'resolvedFilePath', 'setResolvedFilePath', 'lineNumberInResolvedFile',
  'setLineNumberInResolvedFile', 'internalName', 'setInternalName',
  'augmentedInternalName', 'prettyName', 'componentRootStatus', 'setAliases',
  'aliases', 'setInterfaceNames', 'interfaceNames', 'hasInterface',
  'hasOwnInterface', 'setOwnDeferredNames', 'ownDeferredNames',
  'setOwnImmediateNames', 'ownImmediateNames', 'isNameDeferred',
  'setBaseTypeName', 'baseTypeName', 'baseTypeRevision', 'moduleName',
  'ownModuleName', 'setOwnModuleName', 'clearBaseType', 'setBaseTypeError',
  'baseTypeError', 'addOwnProperty', 'ownProperties', 'ownProperty',
  'hasOwnProperty', 'hasProperty', 'property', 'properties',
  'setPropertyLocallyRequired', 'isPropertyRequired',
  'isPropertyLocallyRequired', 'addOwnPropertyBinding',
  'ownPropertyBindingsInQmlIROrder', 'hasOwnPropertyBindings',
  'hasPropertyBindings', 'propertyBindings', 'isResolved', 'isFullyResolved',
  'ownDefaultPropertyName', 'setOwnDefaultPropertyName',
  'defaultPropertyName', 'ownParentPropertyName', 'setOwnParentPropertyName',
  'parentPropertyName', 'ownAttachedTypeName', 'setOwnAttachedTypeName',
  'attachedTypeName', 'extensionTypeName', 'setExtensionTypeName',
  'extensionType', 'elementTypeName', 'setElementTypeName',
  'addOwnRuntimeFunctionIndex', 'ownRuntimeFunctionIndex', 'isComposite',
  'setIsComposite', 'isJavaScriptBuiltin', 'setIsJavaScriptBuiltin',
  'isOpaqueType', 'setIsTypeOpaque', 'isScript', 'setIsScript',
  'hasCustomParser', 'setHasCustomParser', 'isArrayScope', 'setIsArrayScope',
  'isInlineComponent', 'setIsInlineComponent',
  'isWrappedInImplicitComponent', 'setIsWrappedInImplicitComponent',
  'isAssignedToUnknownProperty', 'setAssignedToUnknownProperty',
  'extensionIsJavaScript', 'setExtensionIsJavaScript',
  'extensionIsNamespace', 'setExtensionIsNamespace', 'isListProperty',
  'setIsListProperty', 'isSingleton', 'setIsSingleton',
  'enforcesScopedEnums', 'setEnforcesScopedEnumsFlag', 'isCreatable',
  'setCreatableFlag', 'isStructured', 'setStructuredFlag',
  'isFileRootComponent', 'setIsRootFileComponentFlag', 'isSelfExtension',
  'setIsSelfExtension', 'setAccessSemantics', 'accessSemantics',
  'isReferenceType', 'isValueType', 'setInlineComponentName',
  'setSourceLocation', 'sourceLocation', 'setIdSourceLocation',
  'idSourceLocation', 'isInCustomParserParent', 'sizeofQQmlSAElement',
  'addOwnPropertyBindingInQmlIROrder', 'hasEnforcesScopedEnumsFlag',
  'hasCreatableFlag', 'hasStructuredFlag'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSScope::Ptr QQmlJSScope::create()': gives a type Python has no
    way to take yet.
  - Qt's 'const QQmlJSScope::Ptr &QQmlJSScope::resetForReparse(const
    QQmlJSScope::Ptr &scope)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::findCurrentQMLScope(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlJSScope::Ptr QQmlJSScope::parentScope()': gives a type Python
    has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::parentScope() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QQmlJSScope::reparent(const QQmlJSScope::Ptr &parentScope,
    const QQmlJSScope::Ptr &childScope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QHash<QString, JavaScriptIdentifier>
    QQmlJSScope::ownJSIdentifiers() const': gives a type Python has no way to
    take yet.
  - Qt's 'QMultiHash<QString, QQmlJSMetaMethod> QQmlJSScope::ownMethods()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::baseType() const': gives a type
    Python has no way to take yet.
  - Qt's 'QMultiHash<QString, QQmlJSMetaPropertyBinding>
    QQmlJSScope::ownPropertyBindings() const': gives a type Python has no way
    to take yet.
  - Qt's 'std::pair<QMultiHash<QString,
    QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString,
    QQmlJSMetaPropertyBinding>::const_iterator>
    QQmlJSScope::ownPropertyBindings(const QString &name) const': gives a
    type Python has no way to take yet.
  - Qt's 'AnnotatedScope QQmlJSScope::ownerOfProperty(const
    QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type Python
    has no way to hand over yet.
  - Qt's 'AnnotatedScope QQmlJSScope::ownerOfMethod(const
    QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type Python
    has no way to hand over yet.
  - Qt's 'AnnotatedScope QQmlJSScope::ownerOfEnum(const QQmlJSScope::ConstPtr
    &self_, const QString &name)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::ownAttachedType() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::attachedType() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::elementType() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::listType() const': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlJSScope::Ptr QQmlJSScope::listType()': gives a type Python has
    no way to take yet.
  - Qt's 'std::optional<JavaScriptIdentifier> QQmlJSScope::jsIdentifier(const
    QString &id) const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<JavaScriptIdentifier>
    QQmlJSScope::ownJSIdentifier(const QString &id) const': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlJS::ChildScopesIterator QQmlJSScope::childScopesBegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJS::ChildScopesIterator QQmlJSScope::childScopesEnd() const':
    gives a type Python has no way to take yet.
  - Qt's 'std::optional<QString> QQmlJSScope::inlineComponentName() const':
    gives a type Python has no way to take yet.
  - Qt's 'InlineComponentOrDocumentRootName
    QQmlJSScope::enclosingInlineComponentName() const': gives a type Python
    has no way to take yet.
  - Qt's 'QList<QQmlJSScope::Ptr> QQmlJSScope::childScopes()': gives a type
    Python has no way to take yet.
  - Qt's 'QList<QQmlJSScope::ConstPtr> QQmlJSScope::childScopes() const':
    gives a type Python has no way to take yet.
  - Qt's 'QTypeRevision QQmlJSScope::resolveTypes(const Ptr &self_, const
    QQmlJS::ContextualTypes &contextualTypes, QSet<QString> *usedTypes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSScope::resolveNonEnumTypes(const QQmlJSScope::Ptr
    &self_, const QQmlJS::ContextualTypes &contextualTypes, QSet<QString>
    *usedTypes)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSScope::resolveEnums(const QQmlJSScope::Ptr &self_, const
    QQmlJS::ContextualTypes &contextualTypes, QSet<QString> *usedTypes)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSScope::resolveList(const QQmlJSScope::Ptr &self_, const
    QQmlJSScope::ConstPtr &arrayType)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlJSScope::resolveGroup(const QQmlJSScope::Ptr &self_, const
    QQmlJSScope::ConstPtr &baseType, const QQmlJS::ContextualTypes
    &contextualTypes, QSet<QString> *usedTypes)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::nonCompositeBaseType(const
    QQmlJSScope::ConstPtr &type)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QQmlJSScope::isSameType(const QQmlJSScope::ConstPtr
    &otherScope) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSScope::inherits(const QQmlJSScope::ConstPtr &base)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSScope::canAssign(const QQmlJSScope::ConstPtr &derived)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlSA::Element QQmlJSScope::createQQmlSAElement(const ConstPtr
    &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlSA::Element QQmlJSScope::createQQmlSAElement(ConstPtr &&a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQmlJSScope::ConstPtr &QQmlJSScope::scope(const
    QQmlSA::Element &a0)': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::QQmlJSScope(QQmlJSScope &&a0)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQmlJSScope &QQmlJSScope::operator=(QQmlJSScope &&a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlJSScope::QQmlJSScope(const QQmlJSScope &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlJSScope &QQmlJSScope::operator=(const QQmlJSScope &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QTypeRevision QQmlJSScope::resolveType(const QQmlJSScope::Ptr
    &self_, const QQmlJS::ContextualTypes &contextualTypes, QSet<QString>
    *usedTypes)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSScope::updateChildScope(const QQmlJSScope::Ptr
    &childScope, const QQmlJSScope::Ptr &self_, const QQmlJS::ContextualTypes
    &contextualTypes, QSet<QString> *usedTypes)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 188 functions Qt declares: 3 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlJSScope is created at the first use, not by
    'QQmlJSScope(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSScope.
  - Each name of Qt's QQmlJSScope that has no cute function yet,
    'attachedType', 'baseType', 'canAssign', 'childScopes',
    'childScopesBegin', 'childScopesEnd', 'create', 'createQQmlSAElement',
    'elementType', 'enclosingInlineComponentName', 'findCurrentQMLScope',
    'findType', 'inherits', 'inlineComponentName', 'isSameType',
    'jsIdentifier', 'listType', 'mutableOwnMethodsRange',
    'nonCompositeBaseRevision', 'nonCompositeBaseType', 'ownAttachedType',
    'ownJSIdentifier', 'ownJSIdentifiers', 'ownPropertyBindings',
    'ownerOfEnum', 'ownerOfMethod', 'ownerOfProperty', 'parentScope',
    'reparent', 'resetForReparse', 'resolveEnums', 'resolveGroup',
    'resolveList', 'resolveNonEnumTypes', 'resolveType', 'resolveTypes',
    'scope', 'updateChildScope', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSScope, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class BindingTargetSpecifier(CuteNum):
    """
    The enum 'QQmlJSScope::BindingTargetSpecifier' of Qt, with the 3 names Qt
    gives in it.
    """

    SimplePropertyTarget = Kee[int](0)
    ListPropertyTarget = Kee[int](1)
    UnnamedPropertyTarget = Kee[int](2)

  class ExtensionKind(CuteNum):
    """
    The enum 'QQmlJSScope::ExtensionKind' of Qt, with the 4 names Qt gives in
    it.
    """

    NotExtension = Kee[int](0)
    ExtensionType = Kee[int](1)
    ExtensionJavaScript = Kee[int](2)
    ExtensionNamespace = Kee[int](3)

  class Flag(CuteFlags):
    """
    The flags enum 'QQmlJSScope::Flag' of Qt, with the 19 names Qt gives in
    it. Qt names the type of its combinations 'QQmlJSScope::Flags'.
    """

    Creatable = 0x1
    Composite = 0x2
    JavaScriptBuiltin = 0x4
    Singleton = 0x8
    Script = 0x10
    CustomParser = 0x20
    Array = 0x40
    InlineComponent = 0x80
    WrappedInImplicitComponent = 0x100
    HasBaseTypeError = 0x200
    ExtensionIsNamespace = 0x400
    IsListProperty = 0x800
    Structured = 0x1000
    ExtensionIsJavaScript = 0x2000
    EnforcesScopedEnums = 0x4000
    FileRootComponent = 0x8000
    AssignedToUnknownProperty = 0x10000
    IsSelfExtension = 0x20000
    IsOpaque = 0x40000

  Flags = Flag

  class IsComponentRoot(CuteNum, scoped=True):
    """
    The enum 'QQmlJSScope::IsComponentRoot' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)
    Maybe = Kee[int](2)

  #  The classes Qt writes inside QQmlJSScope, each a class in here as in
  #  C++.

  class AnnotatedScope(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSScope::AnnotatedScope: a plain Python object
    standing in front of one C++ QQmlJSScope::AnnotatedScope.

    C++ hands a QQmlJSScope::AnnotatedScope around as a copy, so every C++
    QQmlJSScope::AnnotatedScope behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlJSScope::AnnotatedScope yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSScope::AnnotatedScope::~AnnotatedScope()': the destructor:
      Python removes its C++ QQmlJSScope::AnnotatedScope by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlJSScope::AnnotatedScope is created at the first use, not by
      'QQmlJSScope::AnnotatedScope(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSScope::AnnotatedScope back gives a copy the
      ritual made for Python, in a new cute QQmlJSScope::AnnotatedScope.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSScope::AnnotatedScope'

    #  Qt's '~QQmlJSScope::AnnotatedScope()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSScope::AnnotatedScope behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QQmlJSScope14AnnotatedScopeD1Ev'

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

  class JavaScriptIdentifier(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSScope::JavaScriptIdentifier: a plain Python
    object standing in front of one C++ QQmlJSScope::JavaScriptIdentifier.

    C++ hands a QQmlJSScope::JavaScriptIdentifier around as a copy, so every
    C++ QQmlJSScope::JavaScriptIdentifier behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQmlJSScope::JavaScriptIdentifier yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSScope::JavaScriptIdentifier::~JavaScriptIdentifier()': the
      destructor: Python removes its C++ QQmlJSScope::JavaScriptIdentifier by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlJSScope::JavaScriptIdentifier is created at the first use,
      not by 'QQmlJSScope::JavaScriptIdentifier(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSScope::JavaScriptIdentifier back gives a copy
      the ritual made for Python, in a new cute
      QQmlJSScope::JavaScriptIdentifier.
    """

    #  The enums Qt writes inside QQmlJSScope::JavaScriptIdentifier, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class Kind(CuteNum):
      """
      The enum 'QQmlJSScope::JavaScriptIdentifier::Kind' of Qt, with the 4
      names Qt gives in it.
      """

      Parameter = Kee[int](0)
      FunctionScoped = Kee[int](1)
      LexicalScoped = Kee[int](2)
      Injected = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSScope::JavaScriptIdentifier'

    #  Qt's '~QQmlJSScope::JavaScriptIdentifier()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlJSScope::JavaScriptIdentifier
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QQmlJSScope20JavaScriptIdentifierD1Ev'

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
  @overload(str)
  def prettyName(name: str) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::prettyName(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#prettyName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::prettyName(QAnyStringView name)
    return Rituals.call(
        'ritual_ZN11QQmlJSScope10prettyNameE14QAnyStringView', name,
    )

  @staticmethod
  def sizeofQQmlSAElement() -> int:
    """
    Calls Qt's 'qsizetype QQmlJSScope::sizeofQQmlSAElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#sizeofQQmlSAElement
    """
    #  qsizetype QQmlJSScope::sizeofQQmlSAElement()
    return Rituals.call('ritual_ZN11QQmlJSScope19sizeofQQmlSAElementEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSScope'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scopeType(self) -> QQmlSA.ScopeType:
    """
    Calls Qt's 'ScopeType QQmlJSScope::scopeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#scopeType

    Returns
    -------

    QQmlSA.ScopeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QQmlSA.ScopeType(number)'
      gives.
    """
    #  ScopeType QQmlJSScope::scopeType() const
    return QQmlSA.ScopeType(self.uglySide.call(
        'ritual_ZNK11QQmlJSScope9scopeTypeEv',
    ))

  @overload(str)
  def ownMethods(self, name: str) -> QList[QQmlJSMetaMethod]:
    """
    Calls Qt's 'QList<QQmlJSMetaMethod> QQmlJSScope::ownMethods(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownMethods

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QQmlJSMetaMethod]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaMethod> QQmlJSScope::ownMethods(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope10ownMethodsERK7QString', name,
    )
    return QList[QQmlJSMetaMethod]._cuteOwning(address)

  @overload(str)
  def hasOwnMethod(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasOwnMethod(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasOwnMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasOwnMethod(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope12hasOwnMethodERK7QString', name,
    )

  @overload(str)
  def hasMethod(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasMethod(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasMethod(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope9hasMethodERK7QString', name,
    )

  @overload()
  def methods(self) -> QHash[str, QQmlJSMetaMethod]:
    """
    Calls Qt's 'QHash<QString, QQmlJSMetaMethod> QQmlJSScope::methods()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#methods

    Returns
    -------

    QHash[str, QQmlJSMetaMethod]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QQmlJSMetaMethod> QQmlJSScope::methods() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope7methodsEv')
    return QHash[str, QQmlJSMetaMethod]._cuteOwning(address)

  @overload(str)
  def methods(self, name: str) -> QList[QQmlJSMetaMethod]:
    """
    Calls Qt's 'QList<QQmlJSMetaMethod> QQmlJSScope::methods(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#methods

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QQmlJSMetaMethod]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaMethod> QQmlJSScope::methods(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope7methodsERK7QString', name,
    )
    return QList[QQmlJSMetaMethod]._cuteOwning(address)

  @overload(str, QQmlSA.MethodType)
  def methods(
      self,
      name: str,
      type: QQmlSA.MethodType,
  ) -> QList[QQmlJSMetaMethod]:
    """
    Calls Qt's 'QList<QQmlJSMetaMethod> QQmlJSScope::methods(const QString
    &name, QQmlJSMetaMethodType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#methods

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    type : QQmlSA.MethodType
      Passed on as its number.

    Returns
    -------

    QList[QQmlJSMetaMethod]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaMethod> QQmlJSScope::methods(const QString &name,
    #      QQmlJSMetaMethodType type) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope7methodsERK7QStringN6QQmlSA10MethodTypeE',
        name, type.value,
    )
    return QList[QQmlJSMetaMethod]._cuteOwning(address)

  def ownEnumerations(self) -> QHash[str, QQmlJSMetaEnum]:
    """
    Calls Qt's 'QHash<QString, QQmlJSMetaEnum> QQmlJSScope::ownEnumerations()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownEnumerations

    Returns
    -------

    QHash[str, QQmlJSMetaEnum]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QQmlJSMetaEnum> QQmlJSScope::ownEnumerations() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope15ownEnumerationsEv',
    )
    from . import QQmlJSMetaEnum
    return QHash[str, QQmlJSMetaEnum]._cuteOwning(address)

  @overload(str)
  def ownEnumeration(self, name: str) -> QQmlJSMetaEnum:
    """
    Calls Qt's 'QQmlJSMetaEnum QQmlJSScope::ownEnumeration(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownEnumeration

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJSMetaEnum
      A new cute QQmlJSMetaEnum around the copy Qt gave back. Python owns it.
    """
    #  QQmlJSMetaEnum QQmlJSScope::ownEnumeration(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope14ownEnumerationERK7QString', name,
    )
    from . import QQmlJSMetaEnum
    return QQmlJSMetaEnum._cuteOwning(address)

  @overload(str)
  def hasOwnEnumeration(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasOwnEnumeration(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasOwnEnumeration

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasOwnEnumeration(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope17hasOwnEnumerationERK7QString', name,
    )

  @overload(str)
  def hasEnumeration(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasEnumeration(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasEnumeration

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasEnumeration(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope14hasEnumerationERK7QString', name,
    )

  @overload(str)
  def hasEnumerationKey(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasEnumerationKey(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasEnumerationKey

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasEnumerationKey(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope17hasEnumerationKeyERK7QString', name,
    )

  @overload(str)
  def hasOwnEnumerationKey(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasOwnEnumerationKey(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#hasOwnEnumerationKey

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasOwnEnumerationKey(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope20hasOwnEnumerationKeyERK7QString', name,
    )

  @overload(str)
  def enumeration(self, name: str) -> QQmlJSMetaEnum:
    """
    Calls Qt's 'QQmlJSMetaEnum QQmlJSScope::enumeration(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#enumeration

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJSMetaEnum
      A new cute QQmlJSMetaEnum around the copy Qt gave back. Python owns it.
    """
    #  QQmlJSMetaEnum QQmlJSScope::enumeration(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope11enumerationERK7QString', name,
    )
    from . import QQmlJSMetaEnum
    return QQmlJSMetaEnum._cuteOwning(address)

  def enumerations(self) -> QHash[str, QQmlJSMetaEnum]:
    """
    Calls Qt's 'QHash<QString, QQmlJSMetaEnum> QQmlJSScope::enumerations()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#enumerations

    Returns
    -------

    QHash[str, QQmlJSMetaEnum]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QQmlJSMetaEnum> QQmlJSScope::enumerations() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope12enumerationsEv')
    from . import QQmlJSMetaEnum
    return QHash[str, QQmlJSMetaEnum]._cuteOwning(address)

  def annotations(self) -> QList[QQmlJSAnnotation]:
    """
    Calls Qt's 'const QList<QQmlJSAnnotation> &QQmlJSScope::annotations()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#annotations

    Returns
    -------

    QList[QQmlJSAnnotation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QQmlJSAnnotation> &QQmlJSScope::annotations() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope11annotationsEv')
    from . import QQmlJSAnnotation
    return QList[QQmlJSAnnotation]._cuteOwning(address)

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::filePath() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope8filePathEv')

  def lineNumber(self) -> int:
    """
    Calls Qt's 'quint32 QQmlJSScope::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#lineNumber
    """
    #  quint32 QQmlJSScope::lineNumber() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope10lineNumberEv')

  def resolvedFilePath(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::resolvedFilePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#resolvedFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::resolvedFilePath() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope16resolvedFilePathEv')

  def lineNumberInResolvedFile(self) -> int:
    """
    Calls Qt's 'quint32 QQmlJSScope::lineNumberInResolvedFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#lineNumberInResolvedFile
    """
    #  quint32 QQmlJSScope::lineNumberInResolvedFile() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope24lineNumberInResolvedFileEv',
    )

  def internalName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::internalName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#internalName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::internalName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope12internalNameEv')

  def augmentedInternalName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::augmentedInternalName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#augmentedInternalName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::augmentedInternalName() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope21augmentedInternalNameEv',
    )

  def componentRootStatus(self) -> IsComponentRoot:
    """
    Calls Qt's 'IsComponentRoot QQmlJSScope::componentRootStatus() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#componentRootStatus

    Returns
    -------

    IsComponentRoot
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'IsComponentRoot(number)'
      gives.
    """
    #  IsComponentRoot QQmlJSScope::componentRootStatus() const
    return QQmlJSScope.IsComponentRoot(self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19componentRootStatusEv',
    ))

  def aliases(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSScope::aliases() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#aliases

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSScope::aliases() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope7aliasesEv')
    return QStringList._cuteOwning(address)

  def interfaceNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSScope::interfaceNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#interfaceNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSScope::interfaceNames() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope14interfaceNamesEv')
    return QStringList._cuteOwning(address)

  @overload(str)
  def hasInterface(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasInterface(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasInterface

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasInterface(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope12hasInterfaceERK7QString', name,
    )

  @overload(str)
  def hasOwnInterface(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasOwnInterface(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasOwnInterface

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasOwnInterface(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope15hasOwnInterfaceERK7QString', name,
    )

  def ownDeferredNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSScope::ownDeferredNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownDeferredNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSScope::ownDeferredNames() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope16ownDeferredNamesEv',
    )
    return QStringList._cuteOwning(address)

  def ownImmediateNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSScope::ownImmediateNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownImmediateNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSScope::ownImmediateNames() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope17ownImmediateNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def isNameDeferred(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isNameDeferred(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isNameDeferred

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::isNameDeferred(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope14isNameDeferredERK7QString', name,
    )

  def baseTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::baseTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#baseTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::baseTypeName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope12baseTypeNameEv')

  def baseTypeRevision(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlJSScope::baseTypeRevision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#baseTypeRevision

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlJSScope::baseTypeRevision() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope16baseTypeRevisionEv',
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def moduleName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::moduleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#moduleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::moduleName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope10moduleNameEv')

  def ownModuleName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::ownModuleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownModuleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::ownModuleName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope13ownModuleNameEv')

  def baseTypeError(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::baseTypeError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#baseTypeError

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::baseTypeError() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope13baseTypeErrorEv')

  def ownProperties(self) -> QHash[str, QQmlJSMetaProperty]:
    """
    Calls Qt's 'QHash<QString, QQmlJSMetaProperty>
    QQmlJSScope::ownProperties() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownProperties

    Returns
    -------

    QHash[str, QQmlJSMetaProperty]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QQmlJSMetaProperty> QQmlJSScope::ownProperties() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope13ownPropertiesEv')
    from . import QQmlJSMetaProperty
    return QHash[str, QQmlJSMetaProperty]._cuteOwning(address)

  @overload(str)
  def ownProperty(self, name: str) -> QQmlJSMetaProperty:
    """
    Calls Qt's 'QQmlJSMetaProperty QQmlJSScope::ownProperty(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#ownProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJSMetaProperty
      A new cute QQmlJSMetaProperty around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaProperty QQmlJSScope::ownProperty(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope11ownPropertyERK7QString', name,
    )
    from . import QQmlJSMetaProperty
    return QQmlJSMetaProperty._cuteOwning(address)

  @overload(str)
  def hasOwnProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasOwnProperty(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasOwnProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasOwnProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope14hasOwnPropertyERK7QString', name,
    )

  @overload(str)
  def hasProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasProperty(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope11hasPropertyERK7QString', name,
    )

  @overload(str)
  def property(self, name: str) -> QQmlJSMetaProperty:
    """
    Calls Qt's 'QQmlJSMetaProperty QQmlJSScope::property(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#property

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlJSMetaProperty
      A new cute QQmlJSMetaProperty around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaProperty QQmlJSScope::property(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope8propertyERK7QString', name,
    )
    from . import QQmlJSMetaProperty
    return QQmlJSMetaProperty._cuteOwning(address)

  def properties(self) -> QHash[str, QQmlJSMetaProperty]:
    """
    Calls Qt's 'QHash<QString, QQmlJSMetaProperty> QQmlJSScope::properties()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#properties

    Returns
    -------

    QHash[str, QQmlJSMetaProperty]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<QString, QQmlJSMetaProperty> QQmlJSScope::properties() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope10propertiesEv')
    from . import QQmlJSMetaProperty
    return QHash[str, QQmlJSMetaProperty]._cuteOwning(address)

  @overload(str)
  def isPropertyRequired(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isPropertyRequired(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isPropertyRequired

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::isPropertyRequired(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope18isPropertyRequiredERK7QString', name,
    )

  @overload(str)
  def isPropertyLocallyRequired(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isPropertyLocallyRequired(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isPropertyLocallyRequired

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::isPropertyLocallyRequired(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope25isPropertyLocallyRequiredERK7QString',
        name,
    )

  def ownPropertyBindingsInQmlIROrder(
      self,
  ) -> QList[QQmlJSMetaPropertyBinding]:
    """
    Calls Qt's 'QList<QQmlJSMetaPropertyBinding>
    QQmlJSScope::ownPropertyBindingsInQmlIROrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#ownPropertyBindingsInQmlIROrder

    Returns
    -------

    QList[QQmlJSMetaPropertyBinding]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaPropertyBinding>
    #      QQmlJSScope::ownPropertyBindingsInQmlIROrder() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope31ownPropertyBindingsInQmlIROrderEv',
    )
    from . import QQmlJSMetaPropertyBinding
    return QList[QQmlJSMetaPropertyBinding]._cuteOwning(address)

  @overload(str)
  def hasOwnPropertyBindings(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasOwnPropertyBindings(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#hasOwnPropertyBindings

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasOwnPropertyBindings(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope22hasOwnPropertyBindingsERK7QString', name,
    )

  @overload(str)
  def hasPropertyBindings(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasPropertyBindings(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#hasPropertyBindings

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScope::hasPropertyBindings(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19hasPropertyBindingsERK7QString', name,
    )

  @overload(str)
  def propertyBindings(self, name: str) -> QList[QQmlJSMetaPropertyBinding]:
    """
    Calls Qt's 'QList<QQmlJSMetaPropertyBinding>
    QQmlJSScope::propertyBindings(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#propertyBindings

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QQmlJSMetaPropertyBinding]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaPropertyBinding> QQmlJSScope::propertyBindings(const
    #      QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope16propertyBindingsERK7QString', name,
    )
    from . import QQmlJSMetaPropertyBinding
    return QList[QQmlJSMetaPropertyBinding]._cuteOwning(address)

  def isResolved(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isResolved() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isResolved
    """
    #  bool QQmlJSScope::isResolved() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope10isResolvedEv')

  def isFullyResolved(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isFullyResolved() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isFullyResolved
    """
    #  bool QQmlJSScope::isFullyResolved() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope15isFullyResolvedEv')

  def ownDefaultPropertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::ownDefaultPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#ownDefaultPropertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::ownDefaultPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope22ownDefaultPropertyNameEv',
    )

  def defaultPropertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::defaultPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#defaultPropertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::defaultPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19defaultPropertyNameEv',
    )

  def ownParentPropertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::ownParentPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#ownParentPropertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::ownParentPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope21ownParentPropertyNameEv',
    )

  def parentPropertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::parentPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#parentPropertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::parentPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope18parentPropertyNameEv',
    )

  def ownAttachedTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::ownAttachedTypeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#ownAttachedTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::ownAttachedTypeName() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19ownAttachedTypeNameEv',
    )

  def attachedTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::attachedTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#attachedTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::attachedTypeName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope16attachedTypeNameEv')

  def extensionTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::extensionTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#extensionTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::extensionTypeName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope17extensionTypeNameEv')

  def extensionType(self) -> AnnotatedScope:
    """
    Calls Qt's 'AnnotatedScope QQmlJSScope::extensionType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#extensionType

    Returns
    -------

    AnnotatedScope
      A new cute QQmlJSScope::AnnotatedScope around the copy Qt gave back.
      Python owns it.
    """
    #  AnnotatedScope QQmlJSScope::extensionType() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope13extensionTypeEv')
    return QQmlJSScope.AnnotatedScope._cuteOwning(address)

  def elementTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSScope::elementTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#elementTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSScope::elementTypeName() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope15elementTypeNameEv')

  @overload(QQmlJSMetaMethod.RelativeFunctionIndex)
  def ownRuntimeFunctionIndex(
      self,
      index: QQmlJSMetaMethod.RelativeFunctionIndex,
  ) -> QQmlJSMetaMethod.AbsoluteFunctionIndex:
    """
    Calls Qt's 'QQmlJSMetaMethod::AbsoluteFunctionIndex
    QQmlJSScope::ownRuntimeFunctionIndex(QQmlJSMetaMethod::
    RelativeFunctionIndex index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#ownRuntimeFunctionIndex

    Parameters
    ----------

    index : QQmlJSMetaMethod.RelativeFunctionIndex
      Passed on as its number.

    Returns
    -------

    QQmlJSMetaMethod.AbsoluteFunctionIndex
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlJSMetaMethod.AbsoluteFunctionIndex(number)' gives.
    """
    #  QQmlJSMetaMethod::AbsoluteFunctionIndex
    #      QQmlJSScope::ownRuntimeFunctionIndex(QQmlJSMetaMethod::
    #      RelativeFunctionIndex index) const
    return QQmlJSMetaMethod.AbsoluteFunctionIndex(self.uglySide.call(
        'ritual_ZNK11QQmlJSScope23ownRuntimeFunctionIndexEN16QQmlJSMetaMeth'
        'od21RelativeFunctionIndexE',
        index.value,
    ))

  def isComposite(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isComposite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isComposite
    """
    #  bool QQmlJSScope::isComposite() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope11isCompositeEv')

  def isJavaScriptBuiltin(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isJavaScriptBuiltin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isJavaScriptBuiltin
    """
    #  bool QQmlJSScope::isJavaScriptBuiltin() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19isJavaScriptBuiltinEv',
    )

  def isOpaqueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isOpaqueType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isOpaqueType
    """
    #  bool QQmlJSScope::isOpaqueType() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope12isOpaqueTypeEv')

  def isScript(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isScript() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isScript
    """
    #  bool QQmlJSScope::isScript() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope8isScriptEv')

  def hasCustomParser(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasCustomParser() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasCustomParser
    """
    #  bool QQmlJSScope::hasCustomParser() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope15hasCustomParserEv')

  def isArrayScope(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isArrayScope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isArrayScope
    """
    #  bool QQmlJSScope::isArrayScope() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope12isArrayScopeEv')

  def isInlineComponent(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isInlineComponent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isInlineComponent
    """
    #  bool QQmlJSScope::isInlineComponent() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope17isInlineComponentEv')

  def isWrappedInImplicitComponent(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isWrappedInImplicitComponent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isWrappedInImplicitComponent
    """
    #  bool QQmlJSScope::isWrappedInImplicitComponent() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope28isWrappedInImplicitComponentEv',
    )

  def isAssignedToUnknownProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isAssignedToUnknownProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isAssignedToUnknownProperty
    """
    #  bool QQmlJSScope::isAssignedToUnknownProperty() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope27isAssignedToUnknownPropertyEv',
    )

  def extensionIsJavaScript(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::extensionIsJavaScript() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#extensionIsJavaScript
    """
    #  bool QQmlJSScope::extensionIsJavaScript() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope21extensionIsJavaScriptEv',
    )

  def extensionIsNamespace(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::extensionIsNamespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#extensionIsNamespace
    """
    #  bool QQmlJSScope::extensionIsNamespace() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope20extensionIsNamespaceEv',
    )

  def isListProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isListProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isListProperty
    """
    #  bool QQmlJSScope::isListProperty() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope14isListPropertyEv')

  def isSingleton(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isSingleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isSingleton
    """
    #  bool QQmlJSScope::isSingleton() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope11isSingletonEv')

  def enforcesScopedEnums(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::enforcesScopedEnums() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#enforcesScopedEnums
    """
    #  bool QQmlJSScope::enforcesScopedEnums() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19enforcesScopedEnumsEv',
    )

  def isCreatable(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isCreatable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isCreatable
    """
    #  bool QQmlJSScope::isCreatable() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope11isCreatableEv')

  def isStructured(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isStructured() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isStructured
    """
    #  bool QQmlJSScope::isStructured() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope12isStructuredEv')

  def isFileRootComponent(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isFileRootComponent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isFileRootComponent
    """
    #  bool QQmlJSScope::isFileRootComponent() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope19isFileRootComponentEv',
    )

  def isSelfExtension(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isSelfExtension() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isSelfExtension
    """
    #  bool QQmlJSScope::isSelfExtension() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope15isSelfExtensionEv')

  def accessSemantics(self) -> QQmlSA.AccessSemantics:
    """
    Calls Qt's 'AccessSemantics QQmlJSScope::accessSemantics() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#accessSemantics

    Returns
    -------

    QQmlSA.AccessSemantics
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.AccessSemantics(number)' gives.
    """
    #  AccessSemantics QQmlJSScope::accessSemantics() const
    return QQmlSA.AccessSemantics(self.uglySide.call(
        'ritual_ZNK11QQmlJSScope15accessSemanticsEv',
    ))

  def isReferenceType(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isReferenceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isReferenceType
    """
    #  bool QQmlJSScope::isReferenceType() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope15isReferenceTypeEv')

  def isValueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isValueType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#isValueType
    """
    #  bool QQmlJSScope::isValueType() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope11isValueTypeEv')

  def sourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation QQmlJSScope::sourceLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#sourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSScope::sourceLocation() const
    address = self.uglySide.call('ritual_ZNK11QQmlJSScope14sourceLocationEv')
    return QQmlJS.SourceLocation._cuteOwning(address)

  def idSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation QQmlJSScope::idSourceLocation()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#idSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSScope::idSourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlJSScope16idSourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isInCustomParserParent(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::isInCustomParserParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#isInCustomParserParent
    """
    #  bool QQmlJSScope::isInCustomParserParent() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope22isInCustomParserParentEv',
    )

  def hasEnforcesScopedEnumsFlag(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasEnforcesScopedEnumsFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#hasEnforcesScopedEnumsFlag
    """
    #  bool QQmlJSScope::hasEnforcesScopedEnumsFlag() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlJSScope26hasEnforcesScopedEnumsFlagEv',
    )

  def hasCreatableFlag(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasCreatableFlag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasCreatableFlag
    """
    #  bool QQmlJSScope::hasCreatableFlag() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope16hasCreatableFlagEv')

  def hasStructuredFlag(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScope::hasStructuredFlag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#hasStructuredFlag
    """
    #  bool QQmlJSScope::hasStructuredFlag() const
    return self.uglySide.call('ritual_ZNK11QQmlJSScope17hasStructuredFlagEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlSA.ScopeType)
  def setScopeType(self, type: QQmlSA.ScopeType) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setScopeType(ScopeType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setScopeType

    Parameters
    ----------

    type : QQmlSA.ScopeType
      Passed on as its number.
    """
    #  void QQmlJSScope::setScopeType(ScopeType type)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope12setScopeTypeEN6QQmlSA9ScopeTypeE',
        type.value,
    )

  @overload(QList[QQmlJSAnnotation])
  def setAnnotations(self, annotations: QList[QQmlJSAnnotation]) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setAnnotations(const
    QList<QQmlJSAnnotation> &annotations)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setAnnotations

    Parameters
    ----------

    annotations : QList[QQmlJSAnnotation]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSScope::setAnnotations(const QList<QQmlJSAnnotation>
    #      &annotations)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope14setAnnotationsERK5QListI16QQmlJSAnnotation'
        'E',
        self._valueOf(annotations),
    )

  @overload(str)
  def setFilePath(self, file: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setFilePath(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setFilePath

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setFilePath(const QString &file)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope11setFilePathERK7QString', file,
    )

  @overload(int)
  def setLineNumber(self, lineNumber: int) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setLineNumber(quint32 lineNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setLineNumber

    Parameters
    ----------

    lineNumber : int
      Passed on as it is.
    """
    #  void QQmlJSScope::setLineNumber(quint32 lineNumber)
    self.uglySide.call('ritual_ZN11QQmlJSScope13setLineNumberEj', lineNumber)

  @overload(str)
  def setResolvedFilePath(self, file: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setResolvedFilePath(const QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setResolvedFilePath

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setResolvedFilePath(const QString &file)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope19setResolvedFilePathERK7QString', file,
    )

  @overload(int)
  def setLineNumberInResolvedFile(self, lineNumber: int) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setLineNumberInResolvedFile(quint32
    lineNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setLineNumberInResolvedFile

    Parameters
    ----------

    lineNumber : int
      Passed on as it is.
    """
    #  void QQmlJSScope::setLineNumberInResolvedFile(quint32 lineNumber)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope27setLineNumberInResolvedFileEj', lineNumber,
    )

  @overload(str)
  def setInternalName(self, internalName: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setInternalName(const QString
    &internalName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setInternalName

    Parameters
    ----------

    internalName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setInternalName(const QString &internalName)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope15setInternalNameERK7QString', internalName,
    )

  @overload(QStringList)
  def setAliases(self, aliases: QStringList) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setAliases(const QStringList &aliases)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setAliases

    Parameters
    ----------

    aliases : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSScope::setAliases(const QStringList &aliases)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope10setAliasesERK5QListI7QStringE',
        self._valueOf(aliases),
    )

  @overload(QStringList)
  def setInterfaceNames(self, interfaces: QStringList) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setInterfaceNames(const QStringList
    &interfaces)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setInterfaceNames

    Parameters
    ----------

    interfaces : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSScope::setInterfaceNames(const QStringList &interfaces)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope17setInterfaceNamesERK5QListI7QStringE',
        self._valueOf(interfaces),
    )

  @overload(QStringList)
  def setOwnDeferredNames(self, names: QStringList) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setOwnDeferredNames(const QStringList
    &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setOwnDeferredNames

    Parameters
    ----------

    names : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSScope::setOwnDeferredNames(const QStringList &names)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope19setOwnDeferredNamesERK5QListI7QStringE',
        self._valueOf(names),
    )

  @overload(QStringList)
  def setOwnImmediateNames(self, names: QStringList) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setOwnImmediateNames(const QStringList
    &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setOwnImmediateNames

    Parameters
    ----------

    names : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSScope::setOwnImmediateNames(const QStringList &names)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope20setOwnImmediateNamesERK5QListI7QStringE',
        self._valueOf(names),
    )

  @overload(str)
  def setBaseTypeName(self, baseTypeName: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setBaseTypeName(const QString
    &baseTypeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setBaseTypeName

    Parameters
    ----------

    baseTypeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setBaseTypeName(const QString &baseTypeName)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope15setBaseTypeNameERK7QString', baseTypeName,
    )

  @overload(str)
  def setOwnModuleName(self, moduleName: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setOwnModuleName(const QString
    &moduleName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setOwnModuleName

    Parameters
    ----------

    moduleName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setOwnModuleName(const QString &moduleName)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope16setOwnModuleNameERK7QString', moduleName,
    )

  @overload(str)
  def setBaseTypeError(self, baseTypeError: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setBaseTypeError(const QString
    &baseTypeError)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setBaseTypeError

    Parameters
    ----------

    baseTypeError : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setBaseTypeError(const QString &baseTypeError)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope16setBaseTypeErrorERK7QString', baseTypeError,
    )

  @overload(str, bool)
  def setPropertyLocallyRequired(self, name: str, isRequired: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setPropertyLocallyRequired(const QString
    &name, bool isRequired)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setPropertyLocallyRequired

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    isRequired : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setPropertyLocallyRequired(const QString &name, bool
    #      isRequired)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope26setPropertyLocallyRequiredERK7QStringb',
        name, isRequired,
    )

  @overload(str)
  def setOwnDefaultPropertyName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setOwnDefaultPropertyName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setOwnDefaultPropertyName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setOwnDefaultPropertyName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope25setOwnDefaultPropertyNameERK7QString', name,
    )

  @overload(str)
  def setOwnParentPropertyName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setOwnParentPropertyName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setOwnParentPropertyName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setOwnParentPropertyName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope24setOwnParentPropertyNameERK7QString', name,
    )

  @overload(str)
  def setOwnAttachedTypeName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setOwnAttachedTypeName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setOwnAttachedTypeName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setOwnAttachedTypeName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope22setOwnAttachedTypeNameERK7QString', name,
    )

  @overload(str)
  def setExtensionTypeName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setExtensionTypeName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setExtensionTypeName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setExtensionTypeName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope20setExtensionTypeNameERK7QString', name,
    )

  @overload(str)
  def setElementTypeName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setElementTypeName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setElementTypeName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setElementTypeName(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope18setElementTypeNameERK7QString', name,
    )

  @overload(bool)
  def setIsComposite(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsComposite(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setIsComposite

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsComposite(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope14setIsCompositeEb', v)

  @overload(bool)
  def setIsJavaScriptBuiltin(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsJavaScriptBuiltin(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setIsJavaScriptBuiltin

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsJavaScriptBuiltin(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope22setIsJavaScriptBuiltinEb', v)

  @overload(bool)
  def setIsTypeOpaque(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsTypeOpaque(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setIsTypeOpaque

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsTypeOpaque(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope15setIsTypeOpaqueEb', v)

  @overload(bool)
  def setIsScript(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsScript(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setIsScript

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsScript(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope11setIsScriptEb', v)

  @overload(bool)
  def setHasCustomParser(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setHasCustomParser(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setHasCustomParser

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setHasCustomParser(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope18setHasCustomParserEb', v)

  @overload(bool)
  def setIsArrayScope(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsArrayScope(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setIsArrayScope

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsArrayScope(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope15setIsArrayScopeEb', v)

  @overload(bool)
  def setIsInlineComponent(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsInlineComponent(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setIsInlineComponent

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsInlineComponent(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope20setIsInlineComponentEb', v)

  @overload(bool)
  def setIsWrappedInImplicitComponent(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsWrappedInImplicitComponent(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setIsWrappedInImplicitComponent

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsWrappedInImplicitComponent(bool v)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope31setIsWrappedInImplicitComponentEb', v,
    )

  @overload(bool)
  def setAssignedToUnknownProperty(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setAssignedToUnknownProperty(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setAssignedToUnknownProperty

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setAssignedToUnknownProperty(bool v)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope28setAssignedToUnknownPropertyEb', v,
    )

  @overload(bool)
  def setExtensionIsJavaScript(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setExtensionIsJavaScript(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setExtensionIsJavaScript

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setExtensionIsJavaScript(bool v)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope24setExtensionIsJavaScriptEb', v,
    )

  @overload(bool)
  def setExtensionIsNamespace(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setExtensionIsNamespace(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setExtensionIsNamespace

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setExtensionIsNamespace(bool v)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope23setExtensionIsNamespaceEb', v,
    )

  @overload(bool)
  def setIsListProperty(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsListProperty(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setIsListProperty

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsListProperty(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope17setIsListPropertyEb', v)

  @overload(bool)
  def setIsSingleton(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsSingleton(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setIsSingleton

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsSingleton(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope14setIsSingletonEb', v)

  @overload(bool)
  def setEnforcesScopedEnumsFlag(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setEnforcesScopedEnumsFlag(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setEnforcesScopedEnumsFlag

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setEnforcesScopedEnumsFlag(bool v)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope26setEnforcesScopedEnumsFlagEb', v,
    )

  @overload(bool)
  def setCreatableFlag(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setCreatableFlag(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setCreatableFlag

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setCreatableFlag(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope16setCreatableFlagEb', v)

  @overload(bool)
  def setStructuredFlag(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setStructuredFlag(bool v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setStructuredFlag

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setStructuredFlag(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope17setStructuredFlagEb', v)

  @overload(bool)
  def setIsRootFileComponentFlag(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsRootFileComponentFlag(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setIsRootFileComponentFlag

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsRootFileComponentFlag(bool v)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope26setIsRootFileComponentFlagEb', v,
    )

  @overload(bool)
  def setIsSelfExtension(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIsSelfExtension(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setIsSelfExtension

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJSScope::setIsSelfExtension(bool v)
    self.uglySide.call('ritual_ZN11QQmlJSScope18setIsSelfExtensionEb', v)

  @overload(QQmlSA.AccessSemantics)
  def setAccessSemantics(self, semantics: QQmlSA.AccessSemantics) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setAccessSemantics(AccessSemantics
    semantics)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setAccessSemantics

    Parameters
    ----------

    semantics : QQmlSA.AccessSemantics
      Passed on as its number.
    """
    #  void QQmlJSScope::setAccessSemantics(AccessSemantics semantics)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope18setAccessSemanticsEN6QQmlSA15AccessSemanti'
        'csE',
        semantics.value,
    )

  @overload(str)
  def setInlineComponentName(self, inlineComponentName: str) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setInlineComponentName(const QString
    &inlineComponentName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setInlineComponentName

    Parameters
    ----------

    inlineComponentName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSScope::setInlineComponentName(const QString
    #      &inlineComponentName)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope22setInlineComponentNameERK7QString',
        inlineComponentName,
    )

  @overload(WAIT['QQmlJS.SourceLocation'])
  def setSourceLocation(self, sourceLocation: QQmlJS.SourceLocation) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setSourceLocation(const
    QQmlJS::SourceLocation &sourceLocation)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#setSourceLocation

    Parameters
    ----------

    sourceLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSScope::setSourceLocation(const QQmlJS::SourceLocation
    #      &sourceLocation)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope17setSourceLocationERKN6QQmlJS14SourceLocati'
        'onE',
        self._valueOf(sourceLocation),
    )

  @overload(WAIT['QQmlJS.SourceLocation'])
  def setIdSourceLocation(
      self,
      sourceLocation: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSScope::setIdSourceLocation(const
    QQmlJS::SourceLocation &sourceLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#setIdSourceLocation

    Parameters
    ----------

    sourceLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSScope::setIdSourceLocation(const QQmlJS::SourceLocation
    #      &sourceLocation)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope19setIdSourceLocationERKN6QQmlJS14SourceLoca'
        'tionE',
        self._valueOf(sourceLocation),
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

  @overload(str)
  def __init__(self, internalName: str) -> None:
    """
    Notes what was given, for Qt's 'QQmlJSScope::QQmlJSScope(const QString
    &internalName)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#QQmlJSScope

    Parameters
    ----------

    internalName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJSScope::QQmlJSScope(const QString &internalName)
    self._noteCreation(QQmlJSScope, lambda: Rituals.call(
        'ritual_ZN11QQmlJSScopeC1ERK7QString', internalName,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlJSScope::QQmlJSScope()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#QQmlJSScope
    """
    #  QQmlJSScope::QQmlJSScope()
    self._noteCreation(QQmlJSScope, lambda: Rituals.call(
        'ritual_ZN11QQmlJSScopeC1Ev',
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

  @overload(str, JavaScriptIdentifier)
  def insertJSIdentifier(
      self,
      name: str,
      identifier: JavaScriptIdentifier,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSScope::insertJSIdentifier(const QString &name,
    const JavaScriptIdentifier &identifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#insertJSIdentifier

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    identifier : JavaScriptIdentifier
      Passed on as a value: Qt reads the C++
      QQmlJSScope::JavaScriptIdentifier, which stays Python's own.
    """
    #  void QQmlJSScope::insertJSIdentifier(const QString &name, const
    #      JavaScriptIdentifier &identifier)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope18insertJSIdentifierERK7QStringRKNS_20JavaSc'
        'riptIdentifierE',
        name, self._valueOf(identifier),
    )

  @overload(QQmlJSMetaMethod)
  def addOwnMethod(self, method: QQmlJSMetaMethod) -> None:
    """
    Calls Qt's 'void QQmlJSScope::addOwnMethod(const QQmlJSMetaMethod
    &method)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#addOwnMethod

    Parameters
    ----------

    method : QQmlJSMetaMethod
      Passed on as a value: Qt reads the C++ QQmlJSMetaMethod, which stays
      Python's own.
    """
    #  void QQmlJSScope::addOwnMethod(const QQmlJSMetaMethod &method)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope12addOwnMethodERK16QQmlJSMetaMethod',
        self._valueOf(method),
    )

  @overload(QQmlJSMetaEnum)
  def addOwnEnumeration(self, enumeration: QQmlJSMetaEnum) -> None:
    """
    Calls Qt's 'void QQmlJSScope::addOwnEnumeration(const QQmlJSMetaEnum
    &enumeration)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#addOwnEnumeration

    Parameters
    ----------

    enumeration : QQmlJSMetaEnum
      Passed on as a value: Qt reads the C++ QQmlJSMetaEnum, which stays
      Python's own.
    """
    #  void QQmlJSScope::addOwnEnumeration(const QQmlJSMetaEnum &enumeration)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope17addOwnEnumerationERK14QQmlJSMetaEnum',
        self._valueOf(enumeration),
    )

  def clearBaseType(self) -> None:
    """
    Calls Qt's 'void QQmlJSScope::clearBaseType()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#clearBaseType
    """
    #  void QQmlJSScope::clearBaseType()
    self.uglySide.call('ritual_ZN11QQmlJSScope13clearBaseTypeEv')

  @overload(QQmlJSMetaProperty)
  def addOwnProperty(self, prop: QQmlJSMetaProperty) -> None:
    """
    Calls Qt's 'void QQmlJSScope::addOwnProperty(const QQmlJSMetaProperty
    &prop)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscope.html#addOwnProperty

    Parameters
    ----------

    prop : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.
    """
    #  void QQmlJSScope::addOwnProperty(const QQmlJSMetaProperty &prop)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope14addOwnPropertyERK18QQmlJSMetaProperty',
        self._valueOf(prop),
    )

  @overload(QQmlJSMetaPropertyBinding)
  @overload(QQmlJSMetaPropertyBinding, BindingTargetSpecifier)
  def addOwnPropertyBinding(
      self,
      binding: QQmlJSMetaPropertyBinding,
      specifier: BindingTargetSpecifier = (
          BindingTargetSpecifier.SimplePropertyTarget),
  ) -> None:
    """
    Calls Qt's 'void QQmlJSScope::addOwnPropertyBinding(const
    QQmlJSMetaPropertyBinding &binding, BindingTargetSpecifier specifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#addOwnPropertyBinding

    Parameters
    ----------

    binding : QQmlJSMetaPropertyBinding
      Passed on as a value: Qt reads the C++ QQmlJSMetaPropertyBinding, which
      stays Python's own.

    specifier : BindingTargetSpecifier
      Passed on as its number. May be left out, as in Qt: it is then
      BindingTargetSpecifier.SimplePropertyTarget.
    """
    #  void QQmlJSScope::addOwnPropertyBinding(const
    #      QQmlJSMetaPropertyBinding &binding, BindingTargetSpecifier
    #      specifier)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope21addOwnPropertyBindingERK25QQmlJSMetaProper'
        'tyBindingNS_22BindingTargetSpecifierE',
        self._valueOf(binding), specifier.value,
    )

  @overload(QQmlJSMetaMethod.AbsoluteFunctionIndex)
  def addOwnRuntimeFunctionIndex(
      self,
      index: QQmlJSMetaMethod.AbsoluteFunctionIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSScope::addOwnRuntimeFunctionIndex(QQmlJSMetaMethod::
    AbsoluteFunctionIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#addOwnRuntimeFunctionIndex

    Parameters
    ----------

    index : QQmlJSMetaMethod.AbsoluteFunctionIndex
      Passed on as its number.
    """
    #  void QQmlJSScope::addOwnRuntimeFunctionIndex(QQmlJSMetaMethod::
    #      AbsoluteFunctionIndex index)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope26addOwnRuntimeFunctionIndexEN16QQmlJSMetaMe'
        'thod21AbsoluteFunctionIndexE',
        index.value,
    )

  @overload(QQmlJSMetaPropertyBinding, BindingTargetSpecifier)
  def addOwnPropertyBindingInQmlIROrder(
      self,
      binding: QQmlJSMetaPropertyBinding,
      specifier: BindingTargetSpecifier,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSScope::addOwnPropertyBindingInQmlIROrder(const
    QQmlJSMetaPropertyBinding &binding, BindingTargetSpecifier specifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscope.html#addOwnPropertyBindingInQmlIROrder

    Parameters
    ----------

    binding : QQmlJSMetaPropertyBinding
      Passed on as a value: Qt reads the C++ QQmlJSMetaPropertyBinding, which
      stays Python's own.

    specifier : BindingTargetSpecifier
      Passed on as its number.
    """
    #  void QQmlJSScope::addOwnPropertyBindingInQmlIROrder(const
    #      QQmlJSMetaPropertyBinding &binding, BindingTargetSpecifier
    #      specifier)
    self.uglySide.call(
        'ritual_ZN11QQmlJSScope33addOwnPropertyBindingInQmlIROrderERK25QQml'
        'JSMetaPropertyBindingNS_22BindingTargetSpecifierE',
        self._valueOf(binding), specifier.value,
    )

  @staticmethod
  def attachedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::attachedType() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.attachedType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::attachedType() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def baseType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::baseType() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.baseType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::baseType() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def canAssign(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSScope::canAssign(const QQmlJSScope::ConstPtr &derived)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.canAssign' has no cute function yet. Qt's 'bool "
        "QQmlJSScope::canAssign(const QQmlJSScope::ConstPtr &derived) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def childScopes(*__, **_) -> Never:
    """
    - Qt's 'QList<QQmlJSScope::Ptr> QQmlJSScope::childScopes()': gives a type
      Python has no way to take yet.
    - Qt's 'QList<QQmlJSScope::ConstPtr> QQmlJSScope::childScopes() const':
      gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.childScopes' has no cute function yet. Qt's "
        "'QList<QQmlJSScope::Ptr> QQmlJSScope::childScopes()': gives a type "
        "Python has no way to take yet. Qt's 'QList<QQmlJSScope::ConstPtr> "
        "QQmlJSScope::childScopes() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def childScopesBegin(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::ChildScopesIterator QQmlJSScope::childScopesBegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.childScopesBegin' has no cute function yet. Qt's "
        "'QQmlJS::ChildScopesIterator QQmlJSScope::childScopesBegin() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def childScopesEnd(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::ChildScopesIterator QQmlJSScope::childScopesEnd() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.childScopesEnd' has no cute function yet. Qt's "
        "'QQmlJS::ChildScopesIterator QQmlJSScope::childScopesEnd() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::Ptr QQmlJSScope::create()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.create' has no cute function yet. Qt's "
        "'QQmlJSScope::Ptr QQmlJSScope::create()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def createQQmlSAElement(*__, **_) -> Never:
    """
    - Qt's 'QQmlSA::Element QQmlJSScope::createQQmlSAElement(const ConstPtr
      &a0)': takes a type Python has no way to hand over yet.
    - Qt's 'QQmlSA::Element QQmlJSScope::createQQmlSAElement(ConstPtr &&a0)':
      takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.createQQmlSAElement' has no cute function yet. Qt's "
        "'QQmlSA::Element QQmlJSScope::createQQmlSAElement(const ConstPtr "
        "&a0)': takes a type Python has no way to hand over yet. Qt's "
        "'QQmlSA::Element QQmlJSScope::createQQmlSAElement(ConstPtr &&a0)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def elementType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::elementType() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.elementType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::elementType() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def enclosingInlineComponentName(*__, **_) -> Never:
    """
    Qt's 'InlineComponentOrDocumentRootName
    QQmlJSScope::enclosingInlineComponentName() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.enclosingInlineComponentName' has no cute function "
        "yet. Qt's 'InlineComponentOrDocumentRootName "
        "QQmlJSScope::enclosingInlineComponentName() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def findCurrentQMLScope(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::findCurrentQMLScope(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.findCurrentQMLScope' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::findCurrentQMLScope(const "
        "QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def findType(*__, **_) -> Never:
    """
    Qt's 'ImportedScope<QQmlJSScope::ConstPtr> QQmlJSScope::findType(const
    QString &name, const QQmlJS::ContextualTypes &contextualTypes,
    QSet<QString> *usedTypes)': the compiler refuses its ritual as it would
    be written here: no template named 'ImportedScope'; did you mean
    'QQmlJS::ImportedScope'?.
    """
    raise NotImplementedError(
        "'QQmlJSScope.findType' has no cute function yet. Qt's "
        "'ImportedScope<QQmlJSScope::ConstPtr> QQmlJSScope::findType(const "
        "QString &name, const QQmlJS::ContextualTypes &contextualTypes, "
        "QSet<QString> *usedTypes)': the compiler refuses its ritual as it "
        "would be written here: no template named 'ImportedScope'; did you "
        "mean 'QQmlJS::ImportedScope'?.")

  @staticmethod
  def inherits(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSScope::inherits(const QQmlJSScope::ConstPtr &base)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.inherits' has no cute function yet. Qt's 'bool "
        "QQmlJSScope::inherits(const QQmlJSScope::ConstPtr &base) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def inlineComponentName(*__, **_) -> Never:
    """
    Qt's 'std::optional<QString> QQmlJSScope::inlineComponentName() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.inlineComponentName' has no cute function yet. Qt's "
        "'std::optional<QString> QQmlJSScope::inlineComponentName() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def isSameType(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSScope::isSameType(const QQmlJSScope::ConstPtr
    &otherScope) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.isSameType' has no cute function yet. Qt's 'bool "
        "QQmlJSScope::isSameType(const QQmlJSScope::ConstPtr &otherScope) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def jsIdentifier(*__, **_) -> Never:
    """
    Qt's 'std::optional<JavaScriptIdentifier> QQmlJSScope::jsIdentifier(const
    QString &id) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.jsIdentifier' has no cute function yet. Qt's "
        "'std::optional<JavaScriptIdentifier> "
        "QQmlJSScope::jsIdentifier(const QString &id) const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def listType(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::listType() const': gives a
      type Python has no way to take yet.
    - Qt's 'QQmlJSScope::Ptr QQmlJSScope::listType()': gives a type Python
      has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.listType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::listType() const': gives a "
        "type Python has no way to take yet. Qt's 'QQmlJSScope::Ptr "
        "QQmlJSScope::listType()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def mutableOwnMethodsRange(*__, **_) -> Never:
    """
    Qt's 'QMultiHashRange<QString, QQmlJSMetaMethod>
    QQmlJSScope::mutableOwnMethodsRange(const QString &name)': the compiler
    refuses its ritual as it would be written here: no template named
    'QMultiHashRange'; did you mean 'QMultiHash'?.
    """
    raise NotImplementedError(
        "'QQmlJSScope.mutableOwnMethodsRange' has no cute function yet. "
        "Qt's 'QMultiHashRange<QString, QQmlJSMetaMethod> "
        "QQmlJSScope::mutableOwnMethodsRange(const QString &name)': the "
        "compiler refuses its ritual as it would be written here: no "
        "template named 'QMultiHashRange'; did you mean 'QMultiHash'?.")

  @staticmethod
  def nonCompositeBaseRevision(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlJSScope::nonCompositeBaseRevision(const
    ImportedScope<QQmlJSScope::ConstPtr> &scope)': the compiler refuses its
    ritual as it would be written here: no template named 'ImportedScope';
    did you mean 'QQmlJS::ImportedScope'?.
    """
    raise NotImplementedError(
        "'QQmlJSScope.nonCompositeBaseRevision' has no cute function yet. "
        "Qt's 'QTypeRevision QQmlJSScope::nonCompositeBaseRevision(const "
        "ImportedScope<QQmlJSScope::ConstPtr> &scope)': the compiler "
        "refuses its ritual as it would be written here: no template named "
        "'ImportedScope'; did you mean 'QQmlJS::ImportedScope'?.")

  @staticmethod
  def nonCompositeBaseType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::nonCompositeBaseType(const
    QQmlJSScope::ConstPtr &type)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.nonCompositeBaseType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::nonCompositeBaseType(const "
        "QQmlJSScope::ConstPtr &type)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def ownAttachedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::ownAttachedType() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownAttachedType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScope::ownAttachedType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def ownJSIdentifier(*__, **_) -> Never:
    """
    Qt's 'std::optional<JavaScriptIdentifier>
    QQmlJSScope::ownJSIdentifier(const QString &id) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownJSIdentifier' has no cute function yet. Qt's "
        "'std::optional<JavaScriptIdentifier> "
        "QQmlJSScope::ownJSIdentifier(const QString &id) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def ownJSIdentifiers(*__, **_) -> Never:
    """
    Qt's 'QHash<QString, JavaScriptIdentifier>
    QQmlJSScope::ownJSIdentifiers() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownJSIdentifiers' has no cute function yet. Qt's "
        "'QHash<QString, JavaScriptIdentifier> "
        "QQmlJSScope::ownJSIdentifiers() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def ownPropertyBindings(*__, **_) -> Never:
    """
    - Qt's 'QMultiHash<QString, QQmlJSMetaPropertyBinding>
      QQmlJSScope::ownPropertyBindings() const': gives a type Python has no
      way to take yet.
    - Qt's 'std::pair<QMultiHash<QString,
      QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString,
      QQmlJSMetaPropertyBinding>::const_iterator>
      QQmlJSScope::ownPropertyBindings(const QString &name) const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownPropertyBindings' has no cute function yet. Qt's "
        "'QMultiHash<QString, QQmlJSMetaPropertyBinding> "
        "QQmlJSScope::ownPropertyBindings() const': gives a type Python has "
        "no way to take yet. Qt's 'std::pair<QMultiHash<QString, "
        "QQmlJSMetaPropertyBinding>::const_iterator, QMultiHash<QString, "
        "QQmlJSMetaPropertyBinding>::const_iterator> "
        "QQmlJSScope::ownPropertyBindings(const QString &name) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def ownerOfEnum(*__, **_) -> Never:
    """
    Qt's 'AnnotatedScope QQmlJSScope::ownerOfEnum(const QQmlJSScope::ConstPtr
    &self_, const QString &name)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownerOfEnum' has no cute function yet. Qt's "
        "'AnnotatedScope QQmlJSScope::ownerOfEnum(const "
        "QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def ownerOfMethod(*__, **_) -> Never:
    """
    Qt's 'AnnotatedScope QQmlJSScope::ownerOfMethod(const
    QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownerOfMethod' has no cute function yet. Qt's "
        "'AnnotatedScope QQmlJSScope::ownerOfMethod(const "
        "QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def ownerOfProperty(*__, **_) -> Never:
    """
    Qt's 'AnnotatedScope QQmlJSScope::ownerOfProperty(const
    QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.ownerOfProperty' has no cute function yet. Qt's "
        "'AnnotatedScope QQmlJSScope::ownerOfProperty(const "
        "QQmlJSScope::ConstPtr &self_, const QString &name)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def parentScope(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSScope::Ptr QQmlJSScope::parentScope()': gives a type Python
      has no way to take yet.
    - Qt's 'QQmlJSScope::ConstPtr QQmlJSScope::parentScope() const': gives a
      type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.parentScope' has no cute function yet. Qt's "
        "'QQmlJSScope::Ptr QQmlJSScope::parentScope()': gives a type Python "
        "has no way to take yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSScope::parentScope() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def reparent(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScope::reparent(const QQmlJSScope::Ptr &parentScope,
    const QQmlJSScope::Ptr &childScope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.reparent' has no cute function yet. Qt's 'void "
        "QQmlJSScope::reparent(const QQmlJSScope::Ptr &parentScope, const "
        "QQmlJSScope::Ptr &childScope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def resetForReparse(*__, **_) -> Never:
    """
    Qt's 'const QQmlJSScope::Ptr &QQmlJSScope::resetForReparse(const
    QQmlJSScope::Ptr &scope)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resetForReparse' has no cute function yet. Qt's "
        "'const QQmlJSScope::Ptr &QQmlJSScope::resetForReparse(const "
        "QQmlJSScope::Ptr &scope)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def resolveEnums(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScope::resolveEnums(const QQmlJSScope::Ptr &self_, const
    QQmlJS::ContextualTypes &contextualTypes, QSet<QString> *usedTypes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resolveEnums' has no cute function yet. Qt's 'void "
        "QQmlJSScope::resolveEnums(const QQmlJSScope::Ptr &self_, const "
        "QQmlJS::ContextualTypes &contextualTypes, QSet<QString> "
        "*usedTypes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def resolveGroup(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScope::resolveGroup(const QQmlJSScope::Ptr &self_, const
    QQmlJSScope::ConstPtr &baseType, const QQmlJS::ContextualTypes
    &contextualTypes, QSet<QString> *usedTypes)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resolveGroup' has no cute function yet. Qt's 'void "
        "QQmlJSScope::resolveGroup(const QQmlJSScope::Ptr &self_, const "
        "QQmlJSScope::ConstPtr &baseType, const QQmlJS::ContextualTypes "
        "&contextualTypes, QSet<QString> *usedTypes)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def resolveList(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScope::resolveList(const QQmlJSScope::Ptr &self_, const
    QQmlJSScope::ConstPtr &arrayType)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resolveList' has no cute function yet. Qt's 'void "
        "QQmlJSScope::resolveList(const QQmlJSScope::Ptr &self_, const "
        "QQmlJSScope::ConstPtr &arrayType)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def resolveNonEnumTypes(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScope::resolveNonEnumTypes(const QQmlJSScope::Ptr
    &self_, const QQmlJS::ContextualTypes &contextualTypes, QSet<QString>
    *usedTypes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resolveNonEnumTypes' has no cute function yet. Qt's "
        "'void QQmlJSScope::resolveNonEnumTypes(const QQmlJSScope::Ptr "
        "&self_, const QQmlJS::ContextualTypes &contextualTypes, "
        "QSet<QString> *usedTypes)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def resolveType(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlJSScope::resolveType(const QQmlJSScope::Ptr
    &self_, const QQmlJS::ContextualTypes &contextualTypes, QSet<QString>
    *usedTypes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resolveType' has no cute function yet. Qt's "
        "'QTypeRevision QQmlJSScope::resolveType(const QQmlJSScope::Ptr "
        "&self_, const QQmlJS::ContextualTypes &contextualTypes, "
        "QSet<QString> *usedTypes)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def resolveTypes(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlJSScope::resolveTypes(const Ptr &self_, const
    QQmlJS::ContextualTypes &contextualTypes, QSet<QString> *usedTypes)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.resolveTypes' has no cute function yet. Qt's "
        "'QTypeRevision QQmlJSScope::resolveTypes(const Ptr &self_, const "
        "QQmlJS::ContextualTypes &contextualTypes, QSet<QString> "
        "*usedTypes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def scope(*__, **_) -> Never:
    """
    Qt's 'const QQmlJSScope::ConstPtr &QQmlJSScope::scope(const
    QQmlSA::Element &a0)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.scope' has no cute function yet. Qt's 'const "
        "QQmlJSScope::ConstPtr &QQmlJSScope::scope(const QQmlSA::Element "
        "&a0)': gives a type Python has no way to take yet.")

  @staticmethod
  def updateChildScope(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScope::updateChildScope(const QQmlJSScope::Ptr
    &childScope, const QQmlJSScope::Ptr &self_, const QQmlJS::ContextualTypes
    &contextualTypes, QSet<QString> *usedTypes)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScope.updateChildScope' has no cute function yet. Qt's "
        "'void QQmlJSScope::updateChildScope(const QQmlJSScope::Ptr "
        "&childScope, const QQmlJSScope::Ptr &self_, const "
        "QQmlJS::ContextualTypes &contextualTypes, QSet<QString> "
        "*usedTypes)': takes a type Python has no way to hand over yet.")
