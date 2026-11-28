"""
QV4::ExecutionEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4engine_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::ExecutionEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QMap, QStringList
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDate, QDateTime, QMetaType, QMutex
  from ..QtCore import QObject, QRegularExpression, QTime, QUrl, QVariant
  from . import QJSEngine, QQmlDelayedCallQueue, QQmlEngine, QQmlError
  from ..QtNetwork import QNetworkAccessManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QJSEngine = WAIT['QJSEngine']
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']
  QRegularExpression = WAIT['QRegularExpression']
  QTime = WAIT['QTime']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExecutionEngine(QV4.EngineBase):
  """
  The cute side of Qt's QV4::ExecutionEngine: a plain Python object standing
  in front of one C++ QV4::ExecutionEngine.

  It is built on the cute 'QV4::EngineBase', as Qt's QV4::ExecutionEngine is
  built on Qt's QV4::EngineBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ExecutionEngine that has a ritual and that
  Python can call so far, 222 names in all: 'jsAlloca', 'jsEngine',
  'qmlEngine', 'rootContext', 'scriptContext', 'setScriptContext',
  'objectCtor', 'stringCtor', 'symbolCtor', 'numberCtor', 'booleanCtor',
  'arrayCtor', 'functionCtor', 'generatorFunctionCtor', 'dateCtor',
  'regExpCtor', 'errorCtor', 'evalErrorCtor', 'rangeErrorCtor',
  'referenceErrorCtor', 'syntaxErrorCtor', 'typeErrorCtor', 'uRIErrorCtor',
  'sharedArrayBufferCtor', 'promiseCtor', 'arrayBufferCtor', 'dataViewCtor',
  'weakSetCtor', 'setCtor', 'weakMapCtor', 'mapCtor',
  'intrinsicTypedArrayCtor', 'urlCtor', 'urlSearchParamsCtor',
  'getSymbolSpecies', 'objectPrototype', 'symbolPrototype', 'arrayPrototype',
  'arrayProtoValues', 'propertyListPrototype', 'stringPrototype',
  'numberPrototype', 'booleanPrototype', 'datePrototype',
  'functionPrototype', 'generatorPrototype', 'regExpPrototype',
  'errorPrototype', 'evalErrorPrototype', 'rangeErrorPrototype',
  'referenceErrorPrototype', 'syntaxErrorPrototype', 'typeErrorPrototype',
  'uRIErrorPrototype', 'promisePrototype', 'variantPrototype',
  'variantAssociationPrototype', 'sequencePrototype',
  'sharedArrayBufferPrototype', 'arrayBufferPrototype', 'dataViewPrototype',
  'weakSetPrototype', 'setPrototype', 'weakMapPrototype', 'mapPrototype',
  'intrinsicTypedArrayPrototype', 'valueTypeWrapperPrototype',
  'signalHandlerPrototype', 'typeWrapperPrototype', 'iteratorPrototype',
  'forInIteratorPrototype', 'setIteratorPrototype', 'mapIteratorPrototype',
  'arrayIteratorPrototype', 'stringIteratorPrototype', 'urlPrototype',
  'urlSearchParamsPrototype', 'evalFunction', 'getStackFunction', 'thrower',
  'getNetworkAccessManager', 'id_empty', 'id_undefined', 'id_null',
  'id_true', 'id_false', 'id_boolean', 'id_number', 'id_string',
  'id_default', 'id_symbol', 'id_object', 'id_function', 'id_length',
  'id_prototype', 'id_constructor', 'id_arguments', 'id_caller', 'id_callee',
  'id_this', 'id___proto__', 'id_enumerable', 'id_configurable',
  'id_writable', 'id_value', 'id_get', 'id_set', 'id_eval', 'id_uintMax',
  'id_name', 'id_index', 'id_input', 'id_toString', 'id_toLocaleString',
  'id_destroy', 'id_valueOf', 'id_byteLength', 'id_byteOffset', 'id_buffer',
  'id_lastIndex', 'id_next', 'id_done', 'id_return', 'id_throw', 'id_global',
  'id_ignoreCase', 'id_multiline', 'id_unicode', 'id_sticky', 'id_source',
  'id_flags', 'symbol_hasInstance', 'symbol_isConcatSpreadable',
  'symbol_iterator', 'symbol_match', 'symbol_replace', 'symbol_search',
  'symbol_species', 'symbol_split', 'symbol_toPrimitive',
  'symbol_toStringTag', 'symbol_unscopables', 'symbol_revokableProxy',
  'debugger', 'profiler', 'setDebugger', 'setProfiler', 'setPreviewing',
  'newProtoId', 'newObject', 'newString', 'newIdentifier', 'newStringObject',
  'newSymbolObject', 'newNumberObject', 'newBooleanObject', 'newArrayObject',
  'newArrayBuffer', 'newDateObject', 'newRegExpObject', 'newUrlObject',
  'newUrlSearchParamsObject', 'newErrorObject', 'newSyntaxErrorObject',
  'newReferenceErrorObject', 'newTypeErrorObject', 'newRangeErrorObject',
  'newURIErrorObject', 'newEvalErrorObject', 'newPromiseObject',
  'getPromiseReactionHandler', 'newForInIteratorObject',
  'newSetIteratorObject', 'newMapIteratorObject', 'newArrayIteratorObject',
  'qmlContext', 'qmlScopeObject', 'resolvedUrl', 'markObjects',
  'initRootContext', 'newClass', 'throwError', 'throwSyntaxError',
  'throwTypeError', 'throwReferenceError', 'throwRangeError',
  'throwURIError', 'throwUnimplemented', 'catchExceptionAsQmlError',
  'amendException', 'toVariant', 'toVariantLossy', 'fromVariant',
  'variantMapFromJS', 'variantHashFromJS', 'maxJSStackSize',
  'maxGCStackSize', 'safeForAllocLength', 'global_', 'initQmlGlobalObject',
  'initializeGlobal', 'createQtObject', 'freezeObject', 'lockObject',
  'setupXmlHttpRequestExtension', 'setQmlEngine', 'resetQmlEngine',
  'delayedCallQueue', 'startTimer', 'consoleCountHelper',
  'registrationMutex', 'registerExtension', 'setExtensionData',
  'extensionData', 'trimCompilationUnits', 'trimCompilationUnitsForUrl',
  'diskCacheOptions', 'callInContext', 'setMaxCallDepth', 'maxCallDepth',
  'initializeStaticMembers', 'hasJsStackOverflow'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ExecutionEngine::~ExecutionEngine()': the destructor: Python
    never removes a C++ QV4::ExecutionEngine.
  - Qt's 'Heap::InternalClass *QV4::ExecutionEngine::newInternalClass(const
    VTable *vtable, Object *prototype)': names 'QV4::VTable', which has no
    cute class yet.
  - Qt's 'Heap::Object *QV4::ExecutionEngine::newVariantObject(const
    QMetaType type, const void *data)': names 'void', which has no cute class
    yet.
  - Qt's 'StackTrace QV4::ExecutionEngine::stackTrace(int frameLimit) const':
    gives a type Python has no way to take yet.
  - Qt's 'ReturnedValue QV4::ExecutionEngine::catchException(StackTrace
    *trace)': names 'QV4::StackTrace', which has no cute class yet.
  - Qt's 'bool QV4::ExecutionEngine::metaTypeFromJS(const Value &value,
    QMetaType type, void *data)': names 'void', which has no cute class yet.
  - Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::metaTypeToJS(QMetaType
    type, const void *data)': names 'void', which has no cute class yet.
  - Qt's 'void *QV4::ExecutionEngine::xmlHttpRequestData() const': gives
    'void', which has no cute class yet.
  - Qt's 'qint64 QV4::ExecutionEngine::stopTimer(const QString &timerName,
    bool *wasRunning)': takes a number to change where it is.
  - Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutionEngine::compilationUnitForUrl(const QUrl &url) const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutionEngine::executableCompilationUnit(QQmlRefPointer<QV4::
    CompiledData::CompilationUnit> &&unit)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutionEngine::insertCompilationUnit(QQmlRefPointer<QV4::
    CompiledData::CompilationUnit> &&unit)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QMultiHash<QUrl, QQmlRefPointer<ExecutableCompilationUnit>>
    QV4::ExecutionEngine::compilationUnits() const': gives a type Python has
    no way to take yet.
  - Qt's 'Module QV4::ExecutionEngine::registerNativeModule(const QUrl &url,
    const QV4::Value &value)': gives a type Python has no way to take yet.
  - Qt's 'Module QV4::ExecutionEngine::moduleForUrl(const QUrl &_url, const
    ExecutableCompilationUnit *referrer)': gives a type Python has no way to
    take yet.
  - Qt's 'void QV4::ExecutionEngine::callInContext(QV4::Function *function,
    QObject *self_, QV4::ExecutionContext *ctxt, int argc, void **args,
    QMetaType *types)': takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::fromData(QMetaType type,
    const void *ptr, Heap::Object *parent, int property, uint flags)': names
    'void', which has no cute class yet.
  - Qt's 'bool QV4::ExecutionEngine::inStack(const void *current) const':
    names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  10 of the 276 functions Qt declares: 4 a template; 4 leans on 'QV4; 2 the
  compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QV4::ExecutionEngine is created at the first use, not by
    'QV4::ExecutionEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ExecutionEngine.
  - Each name of Qt's QV4::ExecutionEngine that has no cute function yet,
    'callingQmlContext', 'canJIT', 'catchException', 'checkStackLimits',
    'compilationUnitForUrl', 'compilationUnits', 'createPrimitive',
    'currentContext', 'executableCompilationUnit', 'fromData',
    'hasCppStackOverflow', 'hasStackOverflow', 'inStack',
    'insertCompilationUnit', 'metaTypeFromJS', 'metaTypeToJS',
    'moduleForUrl', 'newInternalClass', 'newVariantObject',
    'registerNativeModule', 'setCppStackProperties', 'stackTrace',
    'stopTimer', 'typeLoader', 'xmlHttpRequestData', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::ExecutionEngine, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DiskCache(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QV4::ExecutionEngine::DiskCache' of Qt, with the 8 names
    Qt gives in it. Qt names the type of its combinations
    'QV4::ExecutionEngine::DiskCacheOptions'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    Disabled = 0x0
    AotByteCode = 0x1
    AotNative = 0x2
    QmlcRead = 0x4
    QmlcWrite = 0x8
    Aot = 0x3
    Qmlc = 0xc
    Enabled = 0xf

  DiskCacheOptions = DiskCache

  class JSObjects(CuteNum):
    """
    The enum 'QV4::ExecutionEngine::JSObjects' of Qt, with the 78 names Qt
    gives in it.
    """

    RootContext = Kee[int](0)
    ScriptContext = Kee[int](1)
    IntegerNull = Kee[int](2)
    ObjectProto = Kee[int](3)
    SymbolProto = Kee[int](4)
    ArrayProto = Kee[int](5)
    ArrayProtoValues = Kee[int](6)
    PropertyListProto = Kee[int](7)
    StringProto = Kee[int](8)
    NumberProto = Kee[int](9)
    BooleanProto = Kee[int](10)
    DateProto = Kee[int](11)
    FunctionProto = Kee[int](12)
    GeneratorProto = Kee[int](13)
    RegExpProto = Kee[int](14)
    ErrorProto = Kee[int](15)
    EvalErrorProto = Kee[int](16)
    RangeErrorProto = Kee[int](17)
    ReferenceErrorProto = Kee[int](18)
    SyntaxErrorProto = Kee[int](19)
    TypeErrorProto = Kee[int](20)
    URIErrorProto = Kee[int](21)
    PromiseProto = Kee[int](22)
    VariantProto = Kee[int](23)
    VariantAssociationProto = Kee[int](24)
    SequenceProto = Kee[int](25)
    SharedArrayBufferProto = Kee[int](26)
    ArrayBufferProto = Kee[int](27)
    DataViewProto = Kee[int](28)
    WeakSetProto = Kee[int](29)
    SetProto = Kee[int](30)
    WeakMapProto = Kee[int](31)
    MapProto = Kee[int](32)
    IntrinsicTypedArrayProto = Kee[int](33)
    ValueTypeProto = Kee[int](34)
    TypeWrapperProto = Kee[int](35)
    SignalHandlerProto = Kee[int](36)
    IteratorProto = Kee[int](37)
    ForInIteratorProto = Kee[int](38)
    SetIteratorProto = Kee[int](39)
    MapIteratorProto = Kee[int](40)
    ArrayIteratorProto = Kee[int](41)
    StringIteratorProto = Kee[int](42)
    UrlProto = Kee[int](43)
    UrlSearchParamsProto = Kee[int](44)
    Object_Ctor = Kee[int](45)
    String_Ctor = Kee[int](46)
    Symbol_Ctor = Kee[int](47)
    Number_Ctor = Kee[int](48)
    Boolean_Ctor = Kee[int](49)
    Array_Ctor = Kee[int](50)
    Function_Ctor = Kee[int](51)
    GeneratorFunction_Ctor = Kee[int](52)
    Date_Ctor = Kee[int](53)
    RegExp_Ctor = Kee[int](54)
    Error_Ctor = Kee[int](55)
    EvalError_Ctor = Kee[int](56)
    RangeError_Ctor = Kee[int](57)
    ReferenceError_Ctor = Kee[int](58)
    SyntaxError_Ctor = Kee[int](59)
    TypeError_Ctor = Kee[int](60)
    URIError_Ctor = Kee[int](61)
    SharedArrayBuffer_Ctor = Kee[int](62)
    Promise_Ctor = Kee[int](63)
    ArrayBuffer_Ctor = Kee[int](64)
    DataView_Ctor = Kee[int](65)
    WeakSet_Ctor = Kee[int](66)
    Set_Ctor = Kee[int](67)
    WeakMap_Ctor = Kee[int](68)
    Map_Ctor = Kee[int](69)
    IntrinsicTypedArray_Ctor = Kee[int](70)
    Url_Ctor = Kee[int](71)
    UrlSearchParams_Ctor = Kee[int](72)
    GetSymbolSpecies = Kee[int](73)
    Eval_Function = Kee[int](74)
    GetStack_Function = Kee[int](75)
    ThrowerObject = Kee[int](76)
    NJSObjects = Kee[int](77)

  class JSStrings(CuteNum):
    """
    The enum 'QV4::ExecutionEngine::JSStrings' of Qt, with the 51 names Qt
    gives in it.
    """

    String_Empty = Kee[int](0)
    String_undefined = Kee[int](1)
    String_null = Kee[int](2)
    String_true = Kee[int](3)
    String_false = Kee[int](4)
    String_boolean = Kee[int](5)
    String_number = Kee[int](6)
    String_string = Kee[int](7)
    String_default = Kee[int](8)
    String_symbol = Kee[int](9)
    String_object = Kee[int](10)
    String_function = Kee[int](11)
    String_length = Kee[int](12)
    String_prototype = Kee[int](13)
    String_constructor = Kee[int](14)
    String_arguments = Kee[int](15)
    String_caller = Kee[int](16)
    String_callee = Kee[int](17)
    String_this = Kee[int](18)
    String___proto__ = Kee[int](19)
    String_enumerable = Kee[int](20)
    String_configurable = Kee[int](21)
    String_writable = Kee[int](22)
    String_value = Kee[int](23)
    String_get = Kee[int](24)
    String_set = Kee[int](25)
    String_eval = Kee[int](26)
    String_uintMax = Kee[int](27)
    String_name = Kee[int](28)
    String_index = Kee[int](29)
    String_input = Kee[int](30)
    String_toString = Kee[int](31)
    String_toLocaleString = Kee[int](32)
    String_destroy = Kee[int](33)
    String_valueOf = Kee[int](34)
    String_byteLength = Kee[int](35)
    String_byteOffset = Kee[int](36)
    String_buffer = Kee[int](37)
    String_lastIndex = Kee[int](38)
    String_next = Kee[int](39)
    String_done = Kee[int](40)
    String_return = Kee[int](41)
    String_throw = Kee[int](42)
    String_global = Kee[int](43)
    String_ignoreCase = Kee[int](44)
    String_multiline = Kee[int](45)
    String_unicode = Kee[int](46)
    String_sticky = Kee[int](47)
    String_source = Kee[int](48)
    String_flags = Kee[int](49)
    NJSStrings = Kee[int](50)

  class JSSymbols(CuteNum):
    """
    The enum 'QV4::ExecutionEngine::JSSymbols' of Qt, with the 13 names Qt
    gives in it.
    """

    Symbol_hasInstance = Kee[int](0)
    Symbol_isConcatSpreadable = Kee[int](1)
    Symbol_iterator = Kee[int](2)
    Symbol_match = Kee[int](3)
    Symbol_replace = Kee[int](4)
    Symbol_search = Kee[int](5)
    Symbol_species = Kee[int](6)
    Symbol_split = Kee[int](7)
    Symbol_toPrimitive = Kee[int](8)
    Symbol_toStringTag = Kee[int](9)
    Symbol_unscopables = Kee[int](10)
    Symbol_revokableProxy = Kee[int](11)
    NJSSymbols = Kee[int](12)

  #  The classes Qt writes inside QV4::ExecutionEngine, each a class in here
  #  as in C++.

  class Deletable(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::ExecutionEngine::Deletable: a plain Python
    object standing in front of one C++ QV4::ExecutionEngine::Deletable.

    C++ hands a QV4::ExecutionEngine::Deletable around as a copy, so every
    C++ QV4::ExecutionEngine::Deletable behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QV4::ExecutionEngine::Deletable yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::ExecutionEngine::Deletable::~Deletable()': the destructor:
      Python removes its C++ QV4::ExecutionEngine::Deletable by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QV4::ExecutionEngine::Deletable is created at the first use,
      not by 'QV4::ExecutionEngine::Deletable(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::ExecutionEngine::Deletable back gives a copy
      the ritual made for Python, in a new cute
      QV4::ExecutionEngine::Deletable.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::ExecutionEngine::Deletable'

    #  Qt's '~QV4::ExecutionEngine::Deletable()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::ExecutionEngine::Deletable
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV415ExecutionEngine9DeletableD1Ev'

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

  class ScarceResourceData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::ExecutionEngine::ScarceResourceData: a plain
    Python object standing in front of one C++
    QV4::ExecutionEngine::ScarceResourceData.

    C++ hands a QV4::ExecutionEngine::ScarceResourceData around as a copy, so
    every C++ QV4::ExecutionEngine::ScarceResourceData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QV4::ExecutionEngine::ScarceResourceData yet. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QV4::ExecutionEngine::ScarceResourceData::ScarceResourceData(const
      QMetaType type, const void *data)': names 'void', which has no cute
      class yet.
    - Qt's 'QV4::ExecutionEngine::ScarceResourceData::~ScarceResourceData()':
      the destructor: Python removes its C++
      QV4::ExecutionEngine::ScarceResourceData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::ExecutionEngine::ScarceResourceData is created at the
      first use, not by 'QV4::ExecutionEngine::ScarceResourceData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::ExecutionEngine::ScarceResourceData back gives
      a copy the ritual made for Python, in a new cute
      QV4::ExecutionEngine::ScarceResourceData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::ExecutionEngine::ScarceResourceData'

    #  Qt's '~QV4::ExecutionEngine::ScarceResourceData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QV4::ExecutionEngine::ScarceResourceData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN3QV415ExecutionEngine18ScarceResourceDataD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QV4::ExecutionEngine::ScarceResourceData::ScarceResourceData()', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-executionengine-scarceresourcedata.html
      """
      #  QV4::ExecutionEngine::ScarceResourceData::ScarceResourceData()
      self._noteCreation(
          ExecutionEngine.ScarceResourceData, lambda: Rituals.call(
              'ritual_ZN3QV415ExecutionEngine18ScarceResourceDataC1Ev',
          ))

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
  @overload(bool)
  def setPreviewing(enabled: bool) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setPreviewing(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setPreviewing

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QV4::ExecutionEngine::setPreviewing(bool enabled)
    Rituals.call('ritual_ZN3QV415ExecutionEngine13setPreviewingEb', enabled)

  @staticmethod
  @overload(WAIT['QV4.Heap.ExecutionContext'])
  @overload(NoneType)
  def qmlContext(
      ctx: Optional[QV4.Heap.ExecutionContext],
  ) -> Optional[QV4.Heap.ExecutionContext]:
    """
    Calls Qt's 'Heap::ExecutionContext
    *QV4::ExecutionEngine::qmlContext(Heap::ExecutionContext *ctx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#qmlContext

    Parameters
    ----------

    ctx : Optional[QV4.Heap.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ExecutionContext
    #      *QV4::ExecutionEngine::qmlContext(Heap::ExecutionContext *ctx)
    address = Rituals.call(
        'ritual_ZN3QV415ExecutionEngine10qmlContextEPNS_4Heap16ExecutionCon'
        'textE',
        CuteMixin._addressOf(ctx),
    )
    return QV4.Heap.ExecutionContext._cuteAt(address)

  @overload()
  def qmlContext(self) -> Optional[QV4.Heap.QmlContext]:
    """
    Calls Qt's 'Heap::QmlContext *QV4::ExecutionEngine::qmlContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#qmlContext

    Returns
    -------

    Optional[QV4.Heap.QmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::QmlContext *QV4::ExecutionEngine::qmlContext() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10qmlContextEv',
    )
    return QV4.Heap.QmlContext._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Value'], QMetaType)
  @overload(WAIT['QV4.Value'], QMetaType, bool)
  def toVariant(
      value: QV4.Value,
      typeHint: QMetaType,
      createJSValueForObjectsAndSymbols: bool = True,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::ExecutionEngine::toVariant(const QV4::Value
    &value, QMetaType typeHint, bool createJSValueForObjectsAndSymbols)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#toVariant

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    typeHint : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    createJSValueForObjectsAndSymbols : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::ExecutionEngine::toVariant(const QV4::Value &value,
    #      QMetaType typeHint, bool createJSValueForObjectsAndSymbols)
    address = Rituals.call(
        'ritual_ZN3QV415ExecutionEngine9toVariantERKNS_5ValueE9QMetaTypeb',
        CuteMixin._valueOf(value), CuteMixin._valueOf(typeHint),
        createJSValueForObjectsAndSymbols,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.Value'])
  def toVariantLossy(value: QV4.Value) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::ExecutionEngine::toVariantLossy(const
    QV4::Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#toVariantLossy

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::ExecutionEngine::toVariantLossy(const QV4::Value &value)
    address = Rituals.call(
        'ritual_ZN3QV415ExecutionEngine14toVariantLossyERKNS_5ValueE',
        CuteMixin._valueOf(value),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def variantMapFromJS(o: Optional[QV4.Object]) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QV4::ExecutionEngine::variantMapFromJS(const
    QV4::Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#variantMapFromJS

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QV4::ExecutionEngine::variantMapFromJS(const QV4::Object
    #      *o)
    address = Rituals.call(
        'ritual_ZN3QV415ExecutionEngine16variantMapFromJSEPKNS_6ObjectE',
        CuteMixin._addressOf(o),
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def variantHashFromJS(o: Optional[QV4.Object]) -> QHash[str, QVariant]:
    """
    Calls Qt's 'QVariantHash QV4::ExecutionEngine::variantHashFromJS(const
    QV4::Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#variantHashFromJS

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QHash[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantHash QV4::ExecutionEngine::variantHashFromJS(const QV4::Object
    #      *o)
    address = Rituals.call(
        'ritual_ZN3QV415ExecutionEngine17variantHashFromJSEPKNS_6ObjectE',
        CuteMixin._addressOf(o),
    )
    from ..QtCore import QVariant
    return QHash[str, QVariant]._cuteOwning(address)

  @staticmethod
  def registrationMutex() -> Optional[QMutex]:
    """
    Calls Qt's 'QMutex *QV4::ExecutionEngine::registrationMutex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#registrationMutex

    Returns
    -------

    Optional[QMutex]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMutex *QV4::ExecutionEngine::registrationMutex()
    address = Rituals.call(
        'ritual_ZN3QV415ExecutionEngine17registrationMutexEv',
    )
    from ..QtCore import QMutex
    return QMutex._cuteAt(address)

  @staticmethod
  def registerExtension() -> int:
    """
    Calls Qt's 'int QV4::ExecutionEngine::registerExtension()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#registerExtension
    """
    #  int QV4::ExecutionEngine::registerExtension()
    return Rituals.call(
        'ritual_ZN3QV415ExecutionEngine17registerExtensionEv',
    )

  @staticmethod
  @overload(int)
  def setMaxCallDepth(maxCallDepth: int) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setMaxCallDepth(int
    maxCallDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setMaxCallDepth

    Parameters
    ----------

    maxCallDepth : int
      Passed on as it is.
    """
    #  void QV4::ExecutionEngine::setMaxCallDepth(int maxCallDepth)
    Rituals.call(
        'ritual_ZN3QV415ExecutionEngine15setMaxCallDepthEi', maxCallDepth,
    )

  @staticmethod
  def maxCallDepth() -> int:
    """
    Calls Qt's 'int QV4::ExecutionEngine::maxCallDepth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#maxCallDepth
    """
    #  int QV4::ExecutionEngine::maxCallDepth()
    return Rituals.call('ritual_ZN3QV415ExecutionEngine12maxCallDepthEv')

  @staticmethod
  def initializeStaticMembers() -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::initializeStaticMembers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#initializeStaticMembers
    """
    #  void QV4::ExecutionEngine::initializeStaticMembers()
    Rituals.call('ritual_ZN3QV415ExecutionEngine23initializeStaticMembersEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ExecutionEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def jsEngine(self) -> Optional[QJSEngine]:
    """
    Calls Qt's 'QJSEngine *QV4::ExecutionEngine::jsEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#jsEngine

    Returns
    -------

    Optional[QJSEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJSEngine *QV4::ExecutionEngine::jsEngine() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8jsEngineEv',
    )
    from . import QJSEngine
    return QJSEngine._cuteAt(address)

  def qmlEngine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QV4::ExecutionEngine::qmlEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#qmlEngine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QV4::ExecutionEngine::qmlEngine() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9qmlEngineEv',
    )
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def rootContext(self) -> Optional[QV4.ExecutionContext]:
    """
    Calls Qt's 'ExecutionContext *QV4::ExecutionEngine::rootContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#rootContext

    Returns
    -------

    Optional[QV4.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionContext *QV4::ExecutionEngine::rootContext() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11rootContextEv',
    )
    return QV4.ExecutionContext._cuteAt(address)

  def scriptContext(self) -> Optional[QV4.ExecutionContext]:
    """
    Calls Qt's 'ExecutionContext *QV4::ExecutionEngine::scriptContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#scriptContext

    Returns
    -------

    Optional[QV4.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionContext *QV4::ExecutionEngine::scriptContext() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13scriptContextEv',
    )
    return QV4.ExecutionContext._cuteAt(address)

  def objectCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::objectCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#objectCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::objectCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10objectCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def stringCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::stringCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#stringCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::stringCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10stringCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def symbolCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::symbolCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbolCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::symbolCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10symbolCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def numberCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::numberCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#numberCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::numberCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10numberCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def booleanCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::booleanCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#booleanCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::booleanCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11booleanCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def arrayCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::arrayCtor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#arrayCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::arrayCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9arrayCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def functionCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::functionCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#functionCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::functionCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12functionCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def generatorFunctionCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::generatorFunctionCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#generatorFunctionCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::generatorFunctionCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine21generatorFunctionCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def dateCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::dateCtor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#dateCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::dateCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8dateCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def regExpCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::regExpCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#regExpCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::regExpCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10regExpCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def errorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::errorCtor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#errorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::errorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9errorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def evalErrorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::evalErrorCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#evalErrorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::evalErrorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13evalErrorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def rangeErrorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::rangeErrorCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#rangeErrorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::rangeErrorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14rangeErrorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def referenceErrorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::referenceErrorCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#referenceErrorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::referenceErrorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18referenceErrorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def syntaxErrorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::syntaxErrorCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#syntaxErrorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::syntaxErrorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15syntaxErrorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def typeErrorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::typeErrorCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#typeErrorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::typeErrorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13typeErrorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def uRIErrorCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::uRIErrorCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#uRIErrorCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::uRIErrorCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12uRIErrorCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def sharedArrayBufferCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::sharedArrayBufferCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#sharedArrayBufferCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::sharedArrayBufferCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine21sharedArrayBufferCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def promiseCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::promiseCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#promiseCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::promiseCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11promiseCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def arrayBufferCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::arrayBufferCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#arrayBufferCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::arrayBufferCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15arrayBufferCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def dataViewCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::dataViewCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#dataViewCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::dataViewCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12dataViewCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def weakSetCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::weakSetCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#weakSetCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::weakSetCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11weakSetCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def weakMapCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::weakMapCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#weakMapCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::weakMapCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11weakMapCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def mapCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::mapCtor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#mapCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::mapCtor() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7mapCtorEv')
    return QV4.FunctionObject._cuteAt(address)

  def intrinsicTypedArrayCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject
    *QV4::ExecutionEngine::intrinsicTypedArrayCtor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#intrinsicTypedArrayCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::intrinsicTypedArrayCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine23intrinsicTypedArrayCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def urlCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::urlCtor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#urlCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::urlCtor() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7urlCtorEv')
    return QV4.FunctionObject._cuteAt(address)

  def urlSearchParamsCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::urlSearchParamsCtor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#urlSearchParamsCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::urlSearchParamsCtor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine19urlSearchParamsCtorEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def getSymbolSpecies(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::getSymbolSpecies()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#getSymbolSpecies

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::getSymbolSpecies() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16getSymbolSpeciesEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def objectPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::objectPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#objectPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::objectPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15objectPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def symbolPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::symbolPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbolPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::symbolPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15symbolPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def arrayPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::arrayPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#arrayPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::arrayPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14arrayPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def arrayProtoValues(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::arrayProtoValues() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#arrayProtoValues

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::arrayProtoValues() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16arrayProtoValuesEv',
    )
    return QV4.Object._cuteAt(address)

  def propertyListPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::propertyListPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#propertyListPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::propertyListPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine21propertyListPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def stringPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::stringPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#stringPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::stringPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15stringPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def numberPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::numberPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#numberPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::numberPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15numberPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def booleanPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::booleanPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#booleanPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::booleanPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16booleanPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def datePrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::datePrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#datePrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::datePrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13datePrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def functionPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::functionPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#functionPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::functionPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine17functionPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def generatorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::generatorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#generatorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::generatorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18generatorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def regExpPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::regExpPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#regExpPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::regExpPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15regExpPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def errorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::errorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#errorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::errorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14errorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def evalErrorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::evalErrorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#evalErrorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::evalErrorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18evalErrorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def rangeErrorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::rangeErrorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#rangeErrorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::rangeErrorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine19rangeErrorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def referenceErrorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::referenceErrorPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#referenceErrorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::referenceErrorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine23referenceErrorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def syntaxErrorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::syntaxErrorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#syntaxErrorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::syntaxErrorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine20syntaxErrorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def typeErrorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::typeErrorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#typeErrorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::typeErrorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18typeErrorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def uRIErrorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::uRIErrorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#uRIErrorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::uRIErrorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine17uRIErrorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def promisePrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::promisePrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#promisePrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::promisePrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16promisePrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def variantPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::variantPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#variantPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::variantPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16variantPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def variantAssociationPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::variantAssociationPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::variantAssociationPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine27variantAssociationPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def sequencePrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::sequencePrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#sequencePrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::sequencePrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine17sequencePrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def sharedArrayBufferPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::sharedArrayBufferPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::sharedArrayBufferPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine26sharedArrayBufferPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def arrayBufferPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::arrayBufferPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#arrayBufferPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::arrayBufferPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine20arrayBufferPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def dataViewPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::dataViewPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#dataViewPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::dataViewPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine17dataViewPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def weakSetPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::weakSetPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#weakSetPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::weakSetPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16weakSetPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def weakMapPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::weakMapPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#weakMapPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::weakMapPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16weakMapPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def mapPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::mapPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#mapPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::mapPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12mapPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def intrinsicTypedArrayPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::intrinsicTypedArrayPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::intrinsicTypedArrayPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine28intrinsicTypedArrayPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def valueTypeWrapperPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::valueTypeWrapperPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#valueTypeWrapperPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::valueTypeWrapperPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine25valueTypeWrapperPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def signalHandlerPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::signalHandlerPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#signalHandlerPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::signalHandlerPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine22signalHandlerPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def typeWrapperPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::typeWrapperPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#typeWrapperPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::typeWrapperPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine20typeWrapperPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def iteratorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::iteratorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#iteratorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::iteratorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine17iteratorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def forInIteratorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::forInIteratorPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#forInIteratorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::forInIteratorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine22forInIteratorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def mapIteratorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::mapIteratorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#mapIteratorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::mapIteratorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine20mapIteratorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def arrayIteratorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::arrayIteratorPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#arrayIteratorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::arrayIteratorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine22arrayIteratorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def stringIteratorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::stringIteratorPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#stringIteratorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::stringIteratorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine23stringIteratorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def urlPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::urlPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#urlPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::urlPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12urlPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def urlSearchParamsPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::urlSearchParamsPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#urlSearchParamsPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::urlSearchParamsPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine24urlSearchParamsPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def evalFunction(self) -> Optional[QV4.EvalFunction]:
    """
    Calls Qt's 'EvalFunction *QV4::ExecutionEngine::evalFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#evalFunction

    Returns
    -------

    Optional[QV4.EvalFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EvalFunction *QV4::ExecutionEngine::evalFunction() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12evalFunctionEv',
    )
    return QV4.EvalFunction._cuteAt(address)

  def getStackFunction(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::getStackFunction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#getStackFunction

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::getStackFunction() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16getStackFunctionEv',
    )
    return QV4.FunctionObject._cuteAt(address)

  def thrower(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::thrower() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#thrower

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::thrower() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7throwerEv')
    return QV4.FunctionObject._cuteAt(address)

  def id_empty(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_empty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_empty

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_empty() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_emptyEv',
    )
    return QV4.String._cuteAt(address)

  def id_undefined(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_undefined() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_undefined

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_undefined() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12id_undefinedEv',
    )
    return QV4.String._cuteAt(address)

  def id_null(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_null() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_null

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_null() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_nullEv')
    return QV4.String._cuteAt(address)

  def id_true(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_true() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_true

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_true() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_trueEv')
    return QV4.String._cuteAt(address)

  def id_false(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_false() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_false

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_false() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_falseEv',
    )
    return QV4.String._cuteAt(address)

  def id_boolean(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_boolean() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_boolean

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_boolean() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10id_booleanEv',
    )
    return QV4.String._cuteAt(address)

  def id_number(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_number() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_number

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_number() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_numberEv',
    )
    return QV4.String._cuteAt(address)

  def id_string(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_string() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_string

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_string() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_stringEv',
    )
    return QV4.String._cuteAt(address)

  def id_default(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_default() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_default

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_default() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10id_defaultEv',
    )
    return QV4.String._cuteAt(address)

  def id_symbol(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_symbol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_symbol

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_symbol() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_symbolEv',
    )
    return QV4.String._cuteAt(address)

  def id_object(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_object

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_object() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_objectEv',
    )
    return QV4.String._cuteAt(address)

  def id_function(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_function() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_function

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_function() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11id_functionEv',
    )
    return QV4.String._cuteAt(address)

  def id_length(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_length

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_length() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_lengthEv',
    )
    return QV4.String._cuteAt(address)

  def id_prototype(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_prototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_prototype

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_prototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12id_prototypeEv',
    )
    return QV4.String._cuteAt(address)

  def id_constructor(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_constructor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_constructor

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_constructor() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14id_constructorEv',
    )
    return QV4.String._cuteAt(address)

  def id_arguments(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_arguments() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_arguments

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_arguments() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12id_argumentsEv',
    )
    return QV4.String._cuteAt(address)

  def id_caller(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_caller() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_caller

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_caller() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_callerEv',
    )
    return QV4.String._cuteAt(address)

  def id_callee(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_callee() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_callee

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_callee() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_calleeEv',
    )
    return QV4.String._cuteAt(address)

  def id_this(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_this() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_this

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_this() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_thisEv')
    return QV4.String._cuteAt(address)

  def id___proto__(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id___proto__() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id___proto__

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id___proto__() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12id___proto__Ev',
    )
    return QV4.String._cuteAt(address)

  def id_enumerable(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_enumerable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_enumerable

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_enumerable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13id_enumerableEv',
    )
    return QV4.String._cuteAt(address)

  def id_configurable(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_configurable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_configurable

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_configurable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15id_configurableEv',
    )
    return QV4.String._cuteAt(address)

  def id_writable(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_writable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_writable

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_writable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11id_writableEv',
    )
    return QV4.String._cuteAt(address)

  def id_value(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_value

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_value() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_valueEv',
    )
    return QV4.String._cuteAt(address)

  def id_get(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_get() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_get

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_get() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine6id_getEv')
    return QV4.String._cuteAt(address)

  def id_set(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_set() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_set

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_set() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine6id_setEv')
    return QV4.String._cuteAt(address)

  def id_eval(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_eval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_eval

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_eval() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_evalEv')
    return QV4.String._cuteAt(address)

  def id_uintMax(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_uintMax() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_uintMax

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_uintMax() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10id_uintMaxEv',
    )
    return QV4.String._cuteAt(address)

  def id_name(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_name

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_name() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_nameEv')
    return QV4.String._cuteAt(address)

  def id_index(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_index

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_index() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_indexEv',
    )
    return QV4.String._cuteAt(address)

  def id_input(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_input() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_input

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_input() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_inputEv',
    )
    return QV4.String._cuteAt(address)

  def id_toString(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_toString

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_toString() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine11id_toStringEv',
    )
    return QV4.String._cuteAt(address)

  def id_toLocaleString(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_toLocaleString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_toLocaleString

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_toLocaleString() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine17id_toLocaleStringEv',
    )
    return QV4.String._cuteAt(address)

  def id_destroy(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_destroy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_destroy

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_destroy() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10id_destroyEv',
    )
    return QV4.String._cuteAt(address)

  def id_valueOf(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_valueOf() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_valueOf

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_valueOf() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10id_valueOfEv',
    )
    return QV4.String._cuteAt(address)

  def id_byteLength(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_byteLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_byteLength

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_byteLength() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13id_byteLengthEv',
    )
    return QV4.String._cuteAt(address)

  def id_byteOffset(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_byteOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_byteOffset

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_byteOffset() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13id_byteOffsetEv',
    )
    return QV4.String._cuteAt(address)

  def id_buffer(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_buffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_buffer

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_buffer() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_bufferEv',
    )
    return QV4.String._cuteAt(address)

  def id_lastIndex(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_lastIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_lastIndex

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_lastIndex() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12id_lastIndexEv',
    )
    return QV4.String._cuteAt(address)

  def id_next(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_next() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_next

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_next() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_nextEv')
    return QV4.String._cuteAt(address)

  def id_done(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_done() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_done

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_done() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7id_doneEv')
    return QV4.String._cuteAt(address)

  def id_return(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_return() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_return

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_return() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_returnEv',
    )
    return QV4.String._cuteAt(address)

  def id_throw(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_throw() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_throw

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_throw() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_throwEv',
    )
    return QV4.String._cuteAt(address)

  def id_global(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_global() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_global

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_global() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_globalEv',
    )
    return QV4.String._cuteAt(address)

  def id_ignoreCase(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_ignoreCase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_ignoreCase

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_ignoreCase() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13id_ignoreCaseEv',
    )
    return QV4.String._cuteAt(address)

  def id_multiline(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_multiline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_multiline

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_multiline() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12id_multilineEv',
    )
    return QV4.String._cuteAt(address)

  def id_unicode(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_unicode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#id_unicode

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_unicode() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine10id_unicodeEv',
    )
    return QV4.String._cuteAt(address)

  def id_sticky(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_sticky() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_sticky

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_sticky() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_stickyEv',
    )
    return QV4.String._cuteAt(address)

  def id_source(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_source

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_source() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine9id_sourceEv',
    )
    return QV4.String._cuteAt(address)

  def id_flags(self) -> Optional[QV4.String]:
    """
    Calls Qt's 'String *QV4::ExecutionEngine::id_flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#id_flags

    Returns
    -------

    Optional[QV4.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  String *QV4::ExecutionEngine::id_flags() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8id_flagsEv',
    )
    return QV4.String._cuteAt(address)

  def symbol_hasInstance(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_hasInstance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_hasInstance

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_hasInstance() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18symbol_hasInstanceEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_isConcatSpreadable(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_isConcatSpreadable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_isConcatSpreadable

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_isConcatSpreadable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine25symbol_isConcatSpreadableEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_iterator(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_iterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_iterator

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_iterator() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine15symbol_iteratorEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_match(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_match() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_match

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_match() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12symbol_matchEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_replace(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_replace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_replace

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_replace() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14symbol_replaceEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_search(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_search() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_search

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_search() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13symbol_searchEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_species(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_species() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_species

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_species() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14symbol_speciesEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_split(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_split() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_split

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_split() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12symbol_splitEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_toPrimitive(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_toPrimitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_toPrimitive

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_toPrimitive() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18symbol_toPrimitiveEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_toStringTag(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_toStringTag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_toStringTag

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_toStringTag() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18symbol_toStringTagEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_unscopables(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_unscopables() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_unscopables

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_unscopables() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18symbol_unscopablesEv',
    )
    return QV4.Symbol._cuteAt(address)

  def symbol_revokableProxy(self) -> Optional[QV4.Symbol]:
    """
    Calls Qt's 'Symbol *QV4::ExecutionEngine::symbol_revokableProxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#symbol_revokableProxy

    Returns
    -------

    Optional[QV4.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Symbol *QV4::ExecutionEngine::symbol_revokableProxy() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine21symbol_revokableProxyEv',
    )
    return QV4.Symbol._cuteAt(address)

  def debugger(self) -> Optional[QV4.Debugging.Debugger]:
    """
    Calls Qt's 'QV4::Debugging::Debugger *QV4::ExecutionEngine::debugger()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#debugger

    Returns
    -------

    Optional[QV4.Debugging.Debugger]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Debugging::Debugger *QV4::ExecutionEngine::debugger() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8debuggerEv',
    )
    return QV4.Debugging.Debugger._cuteAt(address)

  def profiler(self) -> Optional[QV4.Profiling.Profiler]:
    """
    Calls Qt's 'QV4::Profiling::Profiler *QV4::ExecutionEngine::profiler()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#profiler

    Returns
    -------

    Optional[QV4.Profiling.Profiler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Profiling::Profiler *QV4::ExecutionEngine::profiler() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine8profilerEv',
    )
    return QV4.Profiling.Profiler._cuteAt(address)

  def qmlScopeObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::ExecutionEngine::qmlScopeObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#qmlScopeObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::ExecutionEngine::qmlScopeObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14qmlScopeObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def maxJSStackSize(self) -> int:
    """
    Calls Qt's 'int QV4::ExecutionEngine::maxJSStackSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#maxJSStackSize
    """
    #  int QV4::ExecutionEngine::maxJSStackSize() const
    return self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14maxJSStackSizeEv',
    )

  def maxGCStackSize(self) -> int:
    """
    Calls Qt's 'int QV4::ExecutionEngine::maxGCStackSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#maxGCStackSize
    """
    #  int QV4::ExecutionEngine::maxGCStackSize() const
    return self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine14maxGCStackSizeEv',
    )

  @overload(int)
  def extensionData(self, index: int) -> Optional[Deletable]:
    """
    Calls Qt's 'Deletable *QV4::ExecutionEngine::extensionData(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#extensionData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[Deletable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Deletable *QV4::ExecutionEngine::extensionData(int index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine13extensionDataEi', index,
    )
    return QV4.ExecutionEngine.Deletable._cuteAt(address)

  def diskCacheOptions(self) -> DiskCacheOptions:
    """
    Calls Qt's 'DiskCacheOptions QV4::ExecutionEngine::diskCacheOptions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#diskCacheOptions

    Returns
    -------

    DiskCacheOptions
      The value standing for the combination Qt gave back.
    """
    #  DiskCacheOptions QV4::ExecutionEngine::diskCacheOptions() const
    return ExecutionEngine.DiskCacheOptions(self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine16diskCacheOptionsEv',
    ))

  def hasJsStackOverflow(self) -> bool:
    """
    Calls Qt's 'bool QV4::ExecutionEngine::hasJsStackOverflow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#hasJsStackOverflow
    """
    #  bool QV4::ExecutionEngine::hasJsStackOverflow() const
    return self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine18hasJsStackOverflowEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setScriptContext(self, c: int) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setScriptContext(ReturnedValue
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setScriptContext

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QV4::ExecutionEngine::setScriptContext(ReturnedValue c)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16setScriptContextEy', c,
    )

  def setCtor(self) -> Optional[QV4.FunctionObject]:
    """
    Calls Qt's 'FunctionObject *QV4::ExecutionEngine::setCtor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#setCtor

    Returns
    -------

    Optional[QV4.FunctionObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionObject *QV4::ExecutionEngine::setCtor() const
    address = self.uglySide.call('ritual_ZNK3QV415ExecutionEngine7setCtorEv')
    return QV4.FunctionObject._cuteAt(address)

  def setPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::setPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::setPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine12setPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  def setIteratorPrototype(self) -> Optional[QV4.Object]:
    """
    Calls Qt's 'Object *QV4::ExecutionEngine::setIteratorPrototype() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setIteratorPrototype

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::ExecutionEngine::setIteratorPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ExecutionEngine20setIteratorPrototypeEv',
    )
    return QV4.Object._cuteAt(address)

  @overload(WAIT['QV4.Debugging.Debugger'])
  @overload(NoneType)
  def setDebugger(self, debugger: Optional[QV4.Debugging.Debugger]) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setDebugger(Debugging::Debugger
    *debugger)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setDebugger

    Parameters
    ----------

    debugger : Optional[QV4.Debugging.Debugger]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutionEngine::setDebugger(Debugging::Debugger *debugger)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine11setDebuggerEPNS_9Debugging8Debugge'
        'rE',
        self._addressOf(debugger),
    )

  @overload(WAIT['QV4.Profiling.Profiler'])
  @overload(NoneType)
  def setProfiler(self, profiler: Optional[QV4.Profiling.Profiler]) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setProfiler(Profiling::Profiler
    *profiler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setProfiler

    Parameters
    ----------

    profiler : Optional[QV4.Profiling.Profiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutionEngine::setProfiler(Profiling::Profiler *profiler)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine11setProfilerEPNS_9Profiling8Profile'
        'rE',
        self._addressOf(profiler),
    )

  @overload(QQmlEngine)
  @overload(NoneType)
  def setQmlEngine(self, engine: Optional[QQmlEngine]) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setQmlEngine(QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setQmlEngine

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutionEngine::setQmlEngine(QQmlEngine *engine)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine12setQmlEngineEP10QQmlEngine',
        self._addressOf(engine),
    )

  @overload(int, Deletable)
  @overload(int, NoneType)
  def setExtensionData(self, a0: int, a1: Optional[Deletable]) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setExtensionData(int a0, Deletable
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#setExtensionData

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[Deletable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutionEngine::setExtensionData(int a0, Deletable *a1)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16setExtensionDataEiPNS0_9DeletableE',
        a0, self._addressOf(a1),
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
  @overload(QJSEngine)
  @overload(NoneType)
  def __init__(self, jsEngine: Optional[QJSEngine] = None) -> None:
    """
    Notes what was given, for Qt's
    'QV4::ExecutionEngine::ExecutionEngine(QJSEngine *jsEngine)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#ExecutionEngine

    Parameters
    ----------

    jsEngine : Optional[QJSEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QV4::ExecutionEngine::ExecutionEngine(QJSEngine *jsEngine)
    self._noteCreation(ExecutionEngine, lambda: Rituals.call(
        'ritual_ZN3QV415ExecutionEngineC1EP9QJSEngine',
        self._addressOf(jsEngine),
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

  @overload(int)
  def jsAlloca(self, nValues: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::ExecutionEngine::jsAlloca(int nValues)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#jsAlloca

    Parameters
    ----------

    nValues : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::ExecutionEngine::jsAlloca(int nValues)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine8jsAllocaEi', nValues,
    )
    return QV4.Value._cuteAt(address)

  def getNetworkAccessManager(self) -> Optional[QNetworkAccessManager]:
    """
    Calls Qt's 'QNetworkAccessManager
    *QV4::ExecutionEngine::getNetworkAccessManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#getNetworkAccessManager

    Returns
    -------

    Optional[QNetworkAccessManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessManager *QV4::ExecutionEngine::getNetworkAccessManager()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine23getNetworkAccessManagerEv',
    )
    from ..QtNetwork import QNetworkAccessManager
    return QNetworkAccessManager._cuteAt(address)

  def newProtoId(self) -> int:
    """
    Calls Qt's 'quintptr QV4::ExecutionEngine::newProtoId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newProtoId
    """
    #  quintptr QV4::ExecutionEngine::newProtoId()
    return self.uglySide.call('ritual_ZN3QV415ExecutionEngine10newProtoIdEv')

  @overload()
  def newObject(self) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newObject()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#newObject

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newObject()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine9newObjectEv',
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.Heap.InternalClass'])
  @overload(NoneType)
  def newObject(
      self,
      internalClass: Optional[QV4.Heap.InternalClass],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newObject(Heap::InternalClass *internalClass)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#newObject

    Parameters
    ----------

    internalClass : Optional[QV4.Heap.InternalClass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newObject(Heap::InternalClass
    #      *internalClass)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine9newObjectEPNS_4Heap13InternalClassE',
        self._addressOf(internalClass),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(int)
  def newString(self, c: int) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::ExecutionEngine::newString(char16_t c)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#newString

    Parameters
    ----------

    c : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::ExecutionEngine::newString(char16_t c)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine9newStringEDs', c,
    )
    return QV4.Heap.String._cuteAt(address)

  @overload()
  @overload(str)
  def newString(self, s: str = '') -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::ExecutionEngine::newString(const QString
    &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#newString

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::ExecutionEngine::newString(const QString &s)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine9newStringERK7QString', s,
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(str)
  def newIdentifier(self, text: str) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::ExecutionEngine::newIdentifier(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newIdentifier

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::ExecutionEngine::newIdentifier(const QString &text)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13newIdentifierERK7QString', text,
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def newStringObject(
      self,
      string: Optional[QV4.String],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newStringObject(const
    String *string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newStringObject

    Parameters
    ----------

    string : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newStringObject(const String
    #      *string)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15newStringObjectEPKNS_6StringE',
        self._addressOf(string),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.Symbol'])
  @overload(NoneType)
  def newSymbolObject(
      self,
      symbol: Optional[QV4.Symbol],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newSymbolObject(const
    Symbol *symbol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newSymbolObject

    Parameters
    ----------

    symbol : Optional[QV4.Symbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newSymbolObject(const Symbol
    #      *symbol)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15newSymbolObjectEPKNS_6SymbolE',
        self._addressOf(symbol),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(float)
  def newNumberObject(self, value: float) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newNumberObject(double
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newNumberObject

    Parameters
    ----------

    value : float
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newNumberObject(double value)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15newNumberObjectEd', value,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(bool)
  def newBooleanObject(self, b: bool) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newBooleanObject(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newBooleanObject

    Parameters
    ----------

    b : bool
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newBooleanObject(bool b)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16newBooleanObjectEb', b,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload()
  @overload(int)
  def newArrayObject(self, count: int = 0) -> Optional[QV4.Heap.ArrayObject]:
    """
    Calls Qt's 'Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayObject

    Parameters
    ----------

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QV4.Heap.ArrayObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(int count)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newArrayObjectEi', count,
    )
    return QV4.Heap.ArrayObject._cuteAt(address)

  @overload(WAIT['QV4.Value'], int)
  @overload(NoneType, int)
  def newArrayObject(
      self,
      values: Optional[QV4.Value],
      length: int,
  ) -> Optional[QV4.Heap.ArrayObject]:
    """
    Calls Qt's 'Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(const
    Value *values, int length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayObject

    Parameters
    ----------

    values : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.ArrayObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(const Value
    #      *values, int length)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newArrayObjectEPKNS_5ValueEi',
        self._addressOf(values), length,
    )
    return QV4.Heap.ArrayObject._cuteAt(address)

  @overload(QStringList)
  def newArrayObject(
      self,
      list: QStringList,
  ) -> Optional[QV4.Heap.ArrayObject]:
    """
    Calls Qt's 'Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(const
    QStringList &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayObject

    Parameters
    ----------

    list : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QV4.Heap.ArrayObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(const
    #      QStringList &list)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newArrayObjectERK5QListI7QStringE',
        self._valueOf(list),
    )
    return QV4.Heap.ArrayObject._cuteAt(address)

  @overload(WAIT['QV4.Heap.InternalClass'])
  @overload(NoneType)
  def newArrayObject(
      self,
      ic: Optional[QV4.Heap.InternalClass],
  ) -> Optional[QV4.Heap.ArrayObject]:
    """
    Calls Qt's 'Heap::ArrayObject
    *QV4::ExecutionEngine::newArrayObject(Heap::InternalClass *ic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayObject

    Parameters
    ----------

    ic : Optional[QV4.Heap.InternalClass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.ArrayObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayObject
    #      *QV4::ExecutionEngine::newArrayObject(Heap::InternalClass *ic)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newArrayObjectEPNS_4Heap13Internal'
        'ClassE',
        self._addressOf(ic),
    )
    return QV4.Heap.ArrayObject._cuteAt(address)

  @overload(QByteArray)
  def newArrayBuffer(
      self,
      array: QByteArray,
  ) -> Optional[QV4.Heap.ArrayBuffer]:
    """
    Calls Qt's 'Heap::ArrayBuffer *QV4::ExecutionEngine::newArrayBuffer(const
    QByteArray &array)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayBuffer

    Parameters
    ----------

    array : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.ArrayBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayBuffer *QV4::ExecutionEngine::newArrayBuffer(const
    #      QByteArray &array)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newArrayBufferERK10QByteArray',
        self._valueOf(array),
    )
    return QV4.Heap.ArrayBuffer._cuteAt(address)

  @overload(int)
  def newArrayBuffer(self, length: int) -> Optional[QV4.Heap.ArrayBuffer]:
    """
    Calls Qt's 'Heap::ArrayBuffer
    *QV4::ExecutionEngine::newArrayBuffer(size_t length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayBuffer

    Parameters
    ----------

    length : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.ArrayBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayBuffer *QV4::ExecutionEngine::newArrayBuffer(size_t length)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newArrayBufferEm', length,
    )
    return QV4.Heap.ArrayBuffer._cuteAt(address)

  @overload(float)
  def newDateObject(self, dateTime: float) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'Heap::DateObject *QV4::ExecutionEngine::newDateObject(double
    dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newDateObject

    Parameters
    ----------

    dateTime : float
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::DateObject *QV4::ExecutionEngine::newDateObject(double dateTime)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13newDateObjectEd', dateTime,
    )
    return QV4.Heap.DateObject._cuteAt(address)

  @overload(QDateTime)
  def newDateObject(
      self,
      dateTime: QDateTime,
  ) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'Heap::DateObject *QV4::ExecutionEngine::newDateObject(const
    QDateTime &dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newDateObject

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::DateObject *QV4::ExecutionEngine::newDateObject(const QDateTime
    #      &dateTime)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13newDateObjectERK9QDateTime',
        self._valueOf(dateTime),
    )
    return QV4.Heap.DateObject._cuteAt(address)

  @overload(QDate, WAIT['QV4.Heap.Object'], int, int)
  @overload(QDate, NoneType, int, int)
  def newDateObject(
      self,
      date: QDate,
      parent: Optional[QV4.Heap.Object],
      index: int,
      flags: int,
  ) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'Heap::DateObject *QV4::ExecutionEngine::newDateObject(QDate
    date, Heap::Object *parent, int index, uint flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newDateObject

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    parent : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    flags : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::DateObject *QV4::ExecutionEngine::newDateObject(QDate date,
    #      Heap::Object *parent, int index, uint flags)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13newDateObjectE5QDatePNS_4Heap6Obje'
        'ctEij',
        self._valueOf(date), self._addressOf(parent), index, flags,
    )
    return QV4.Heap.DateObject._cuteAt(address)

  @overload(QTime, WAIT['QV4.Heap.Object'], int, int)
  @overload(QTime, NoneType, int, int)
  def newDateObject(
      self,
      time: QTime,
      parent: Optional[QV4.Heap.Object],
      index: int,
      flags: int,
  ) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'Heap::DateObject *QV4::ExecutionEngine::newDateObject(QTime
    time, Heap::Object *parent, int index, uint flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newDateObject

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    parent : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    flags : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::DateObject *QV4::ExecutionEngine::newDateObject(QTime time,
    #      Heap::Object *parent, int index, uint flags)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13newDateObjectE5QTimePNS_4Heap6Obje'
        'ctEij',
        self._valueOf(time), self._addressOf(parent), index, flags,
    )
    return QV4.Heap.DateObject._cuteAt(address)

  @overload(QDateTime, WAIT['QV4.Heap.Object'], int, int)
  @overload(QDateTime, NoneType, int, int)
  def newDateObject(
      self,
      dateTime: QDateTime,
      parent: Optional[QV4.Heap.Object],
      index: int,
      flags: int,
  ) -> Optional[QV4.Heap.DateObject]:
    """
    Calls Qt's 'Heap::DateObject
    *QV4::ExecutionEngine::newDateObject(QDateTime dateTime, Heap::Object
    *parent, int index, uint flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newDateObject

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    parent : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    flags : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.DateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::DateObject *QV4::ExecutionEngine::newDateObject(QDateTime
    #      dateTime, Heap::Object *parent, int index, uint flags)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13newDateObjectE9QDateTimePNS_4Heap6'
        'ObjectEij',
        self._valueOf(dateTime), self._addressOf(parent), index, flags,
    )
    return QV4.Heap.DateObject._cuteAt(address)

  @overload(str, int)
  def newRegExpObject(
      self,
      pattern: str,
      flags: int,
  ) -> Optional[QV4.Heap.RegExpObject]:
    """
    Calls Qt's 'Heap::RegExpObject
    *QV4::ExecutionEngine::newRegExpObject(const QString &pattern, int
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newRegExpObject

    Parameters
    ----------

    pattern : str
      Passed on as it is: a QString is made of it for the call.

    flags : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.RegExpObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::RegExpObject *QV4::ExecutionEngine::newRegExpObject(const
    #      QString &pattern, int flags)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15newRegExpObjectERK7QStringi',
        pattern, flags,
    )
    return QV4.Heap.RegExpObject._cuteAt(address)

  @overload(QRegularExpression)
  def newRegExpObject(
      self,
      re: QRegularExpression,
  ) -> Optional[QV4.Heap.RegExpObject]:
    """
    Calls Qt's 'Heap::RegExpObject
    *QV4::ExecutionEngine::newRegExpObject(const QRegularExpression &re)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newRegExpObject

    Parameters
    ----------

    re : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.Heap.RegExpObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::RegExpObject *QV4::ExecutionEngine::newRegExpObject(const
    #      QRegularExpression &re)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15newRegExpObjectERK18QRegularExpres'
        'sion',
        self._valueOf(re),
    )
    return QV4.Heap.RegExpObject._cuteAt(address)

  @overload()
  def newUrlObject(self) -> Optional[QV4.Heap.UrlObject]:
    """
    Calls Qt's 'Heap::UrlObject *QV4::ExecutionEngine::newUrlObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newUrlObject

    Returns
    -------

    Optional[QV4.Heap.UrlObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::UrlObject *QV4::ExecutionEngine::newUrlObject()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine12newUrlObjectEv',
    )
    return QV4.Heap.UrlObject._cuteAt(address)

  @overload(QUrl)
  def newUrlObject(self, url: QUrl) -> Optional[QV4.Heap.UrlObject]:
    """
    Calls Qt's 'Heap::UrlObject *QV4::ExecutionEngine::newUrlObject(const
    QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newUrlObject

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    Optional[QV4.Heap.UrlObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::UrlObject *QV4::ExecutionEngine::newUrlObject(const QUrl &url)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine12newUrlObjectERK4QUrl',
        self._valueOf(url),
    )
    return QV4.Heap.UrlObject._cuteAt(address)

  def newUrlSearchParamsObject(
      self,
  ) -> Optional[QV4.Heap.UrlSearchParamsObject]:
    """
    Calls Qt's 'Heap::UrlSearchParamsObject
    *QV4::ExecutionEngine::newUrlSearchParamsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newUrlSearchParamsObject

    Returns
    -------

    Optional[QV4.Heap.UrlSearchParamsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::UrlSearchParamsObject
    #      *QV4::ExecutionEngine::newUrlSearchParamsObject()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine24newUrlSearchParamsObjectEv',
    )
    return QV4.Heap.UrlSearchParamsObject._cuteAt(address)

  @overload(WAIT['QV4.Value'])
  def newErrorObject(self, value: QV4.Value) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newErrorObject(const
    Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newErrorObject

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newErrorObject(const Value &value)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newErrorObjectERKNS_5ValueE',
        self._valueOf(value),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newErrorObject(self, message: str) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newErrorObject(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newErrorObject(const QString
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14newErrorObjectERK7QString', message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str, str, int, int)
  def newSyntaxErrorObject(
      self,
      message: str,
      fileName: str,
      line: int,
      column: int,
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newSyntaxErrorObject(const QString &message, const
    QString &fileName, int line, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newSyntaxErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newSyntaxErrorObject(const QString
    #      &message, const QString &fileName, int line, int column)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine20newSyntaxErrorObjectERK7QStringS3_'
        'ii',
        message, fileName, line, column,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newSyntaxErrorObject(self, message: str) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newSyntaxErrorObject(const QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newSyntaxErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newSyntaxErrorObject(const QString
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine20newSyntaxErrorObjectERK7QString',
        message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newReferenceErrorObject(
      self,
      message: str,
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newReferenceErrorObject(const QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newReferenceErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newReferenceErrorObject(const
    #      QString &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine23newReferenceErrorObjectERK7QString',
        message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str, str, int, int)
  def newReferenceErrorObject(
      self,
      message: str,
      fileName: str,
      line: int,
      column: int,
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newReferenceErrorObject(const QString &message,
    const QString &fileName, int line, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newReferenceErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newReferenceErrorObject(const
    #      QString &message, const QString &fileName, int line, int column)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine23newReferenceErrorObjectERK7QString'
        'S3_ii',
        message, fileName, line, column,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newTypeErrorObject(self, message: str) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newTypeErrorObject(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newTypeErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newTypeErrorObject(const QString
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine18newTypeErrorObjectERK7QString',
        message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newRangeErrorObject(self, message: str) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newRangeErrorObject(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newRangeErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newRangeErrorObject(const QString
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine19newRangeErrorObjectERK7QString',
        message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newURIErrorObject(self, message: str) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newURIErrorObject(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newURIErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newURIErrorObject(const QString
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine17newURIErrorObjectERK7QString',
        message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.Value'])
  def newURIErrorObject(
      self,
      message: QV4.Value,
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newURIErrorObject(const
    Value &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newURIErrorObject

    Parameters
    ----------

    message : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newURIErrorObject(const Value
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine17newURIErrorObjectERKNS_5ValueE',
        self._valueOf(message),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def newEvalErrorObject(self, message: str) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newEvalErrorObject(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newEvalErrorObject

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newEvalErrorObject(const QString
    #      &message)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine18newEvalErrorObjectERK7QString',
        message,
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload()
  def newPromiseObject(self) -> Optional[QV4.Heap.PromiseObject]:
    """
    Calls Qt's 'Heap::PromiseObject
    *QV4::ExecutionEngine::newPromiseObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newPromiseObject

    Returns
    -------

    Optional[QV4.Heap.PromiseObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::PromiseObject *QV4::ExecutionEngine::newPromiseObject()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16newPromiseObjectEv',
    )
    return QV4.Heap.PromiseObject._cuteAt(address)

  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.PromiseCapability'])
  @overload(WAIT['QV4.FunctionObject'], NoneType)
  @overload(NoneType, WAIT['QV4.PromiseCapability'])
  @overload(NoneType, NoneType)
  def newPromiseObject(
      self,
      thisObject: Optional[QV4.FunctionObject],
      capability: Optional[QV4.PromiseCapability],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object *QV4::ExecutionEngine::newPromiseObject(const
    QV4::FunctionObject *thisObject, const QV4::PromiseCapability
    *capability)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newPromiseObject

    Parameters
    ----------

    thisObject : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    capability : Optional[QV4.PromiseCapability]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newPromiseObject(const
    #      QV4::FunctionObject *thisObject, const QV4::PromiseCapability
    #      *capability)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16newPromiseObjectEPKNS_14FunctionOb'
        'jectEPKNS_17PromiseCapabilityE',
        self._addressOf(thisObject), self._addressOf(capability),
    )
    return QV4.Heap.Object._cuteAt(address)

  def getPromiseReactionHandler(
      self,
  ) -> Optional[QV4.Promise.ReactionHandler]:
    """
    Calls Qt's 'Promise::ReactionHandler
    *QV4::ExecutionEngine::getPromiseReactionHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#getPromiseReactionHandler

    Returns
    -------

    Optional[QV4.Promise.ReactionHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Promise::ReactionHandler
    #      *QV4::ExecutionEngine::getPromiseReactionHandler()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine25getPromiseReactionHandlerEv',
    )
    return QV4.Promise.ReactionHandler._cuteAt(address)

  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def newForInIteratorObject(
      self,
      o: Optional[QV4.Object],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newForInIteratorObject(Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newForInIteratorObject

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newForInIteratorObject(Object *o)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine22newForInIteratorObjectEPNS_6Object'
        'E',
        self._addressOf(o),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def newSetIteratorObject(
      self,
      o: Optional[QV4.Object],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newSetIteratorObject(Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newSetIteratorObject

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newSetIteratorObject(Object *o)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine20newSetIteratorObjectEPNS_6ObjectE',
        self._addressOf(o),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def newMapIteratorObject(
      self,
      o: Optional[QV4.Object],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newMapIteratorObject(Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newMapIteratorObject

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newMapIteratorObject(Object *o)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine20newMapIteratorObjectEPNS_6ObjectE',
        self._addressOf(o),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def newArrayIteratorObject(
      self,
      o: Optional[QV4.Object],
  ) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Heap::Object
    *QV4::ExecutionEngine::newArrayIteratorObject(Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#newArrayIteratorObject

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::ExecutionEngine::newArrayIteratorObject(Object *o)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine22newArrayIteratorObjectEPNS_6Object'
        'E',
        self._addressOf(o),
    )
    return QV4.Heap.Object._cuteAt(address)

  @overload(str)
  def resolvedUrl(self, file: str) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::ExecutionEngine::resolvedUrl(const QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#resolvedUrl

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::ExecutionEngine::resolvedUrl(const QString &file)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine11resolvedUrlERK7QString', file,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def markObjects(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::markObjects(MarkStack
    *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#markObjects

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ExecutionEngine::markObjects(MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine11markObjectsEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  def initRootContext(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::initRootContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#initRootContext
    """
    #  void QV4::ExecutionEngine::initRootContext()
    self.uglySide.call('ritual_ZN3QV415ExecutionEngine15initRootContextEv')

  @overload(WAIT['QV4.Heap.InternalClass'])
  @overload(NoneType)
  def newClass(
      self,
      other: Optional[QV4.Heap.InternalClass],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::ExecutionEngine::newClass(Heap::InternalClass *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#newClass

    Parameters
    ----------

    other : Optional[QV4.Heap.InternalClass]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::ExecutionEngine::newClass(Heap::InternalClass *other)
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine8newClassEPNS_4Heap13InternalClassE',
        self._addressOf(other),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @overload(WAIT['QV4.Value'])
  def throwError(self, value: QV4.Value) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwError(const Value
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwError

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwError(const Value &value)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine10throwErrorERKNS_5ValueE',
        self._valueOf(value),
    )

  @overload(str)
  def throwError(self, message: str) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwError(const QString
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwError(const QString &message)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine10throwErrorERK7QString', message,
    )

  @overload(str)
  def throwSyntaxError(self, message: str) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwSyntaxError(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwSyntaxError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwSyntaxError(const QString
    #      &message)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16throwSyntaxErrorERK7QString',
        message,
    )

  @overload(str, str, int, int)
  def throwSyntaxError(
      self,
      message: str,
      fileName: str,
      lineNumber: int,
      column: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwSyntaxError(const
    QString &message, const QString &fileName, int lineNumber, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwSyntaxError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    lineNumber : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwSyntaxError(const QString
    #      &message, const QString &fileName, int lineNumber, int column)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16throwSyntaxErrorERK7QStringS3_ii',
        message, fileName, lineNumber, column,
    )

  @overload()
  def throwTypeError(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwTypeError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwTypeError
    """
    #  ReturnedValue QV4::ExecutionEngine::throwTypeError()
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14throwTypeErrorEv',
    )

  @overload(str)
  def throwTypeError(self, message: str) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwTypeError(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwTypeError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwTypeError(const QString
    #      &message)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine14throwTypeErrorERK7QString', message,
    )

  @overload(WAIT['QV4.Value'])
  def throwReferenceError(self, value: QV4.Value) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwReferenceError(const
    Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwReferenceError

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwReferenceError(const Value
    #      &value)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine19throwReferenceErrorERKNS_5ValueE',
        self._valueOf(value),
    )

  @overload(str)
  def throwReferenceError(self, name: str) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwReferenceError(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwReferenceError

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwReferenceError(const QString
    #      &name)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine19throwReferenceErrorERK7QString',
        name,
    )

  @overload(str, str, int, int)
  def throwReferenceError(
      self,
      value: str,
      fileName: str,
      lineNumber: int,
      column: int,
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwReferenceError(const
    QString &value, const QString &fileName, int lineNumber, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwReferenceError

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    lineNumber : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwReferenceError(const QString
    #      &value, const QString &fileName, int lineNumber, int column)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine19throwReferenceErrorERK7QStringS3_i'
        'i',
        value, fileName, lineNumber, column,
    )

  @overload(WAIT['QV4.Value'])
  def throwRangeError(self, value: QV4.Value) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwRangeError(const
    Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwRangeError

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwRangeError(const Value
    #      &value)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15throwRangeErrorERKNS_5ValueE',
        self._valueOf(value),
    )

  @overload(str)
  def throwRangeError(self, message: str) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwRangeError(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwRangeError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwRangeError(const QString
    #      &message)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine15throwRangeErrorERK7QString',
        message,
    )

  @overload(WAIT['QV4.Value'])
  def throwURIError(self, msg: QV4.Value) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwURIError(const Value
    &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwURIError

    Parameters
    ----------

    msg : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwURIError(const Value &msg)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13throwURIErrorERKNS_5ValueE',
        self._valueOf(msg),
    )

  @overload(str)
  def throwUnimplemented(self, message: str) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionEngine::throwUnimplemented(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#throwUnimplemented

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  ReturnedValue QV4::ExecutionEngine::throwUnimplemented(const QString
    #      &message)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine18throwUnimplementedERK7QString',
        message,
    )

  def catchExceptionAsQmlError(self) -> QQmlError:
    """
    Calls Qt's 'QQmlError QV4::ExecutionEngine::catchExceptionAsQmlError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#catchExceptionAsQmlError

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QV4::ExecutionEngine::catchExceptionAsQmlError()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine24catchExceptionAsQmlErrorEv',
    )
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  def amendException(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::amendException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#amendException
    """
    #  void QV4::ExecutionEngine::amendException()
    self.uglySide.call('ritual_ZN3QV415ExecutionEngine14amendExceptionEv')

  @overload(QVariant)
  def fromVariant(self, a0: QVariant) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::fromVariant(const
    QVariant &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#fromVariant

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QV4::ReturnedValue QV4::ExecutionEngine::fromVariant(const QVariant
    #      &a0)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine11fromVariantERK8QVariant',
        self._valueOf(a0),
    )

  @overload(QVariant, WAIT['QV4.Heap.Object'], int, int)
  @overload(QVariant, NoneType, int, int)
  def fromVariant(
      self,
      variant: QVariant,
      parent: Optional[QV4.Heap.Object],
      property: int,
      flags: int,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::fromVariant(const
    QVariant &variant, Heap::Object *parent, int property, uint flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#fromVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    parent : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : int
      Passed on as it is.

    flags : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QV4::ExecutionEngine::fromVariant(const QVariant
    #      &variant, Heap::Object *parent, int property, uint flags)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine11fromVariantERK8QVariantPNS_4Heap6O'
        'bjectEij',
        self._valueOf(variant), self._addressOf(parent), property, flags,
    )

  @overload(int)
  def safeForAllocLength(self, len64: int) -> int:
    """
    Calls Qt's 'int QV4::ExecutionEngine::safeForAllocLength(qint64 len64)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#safeForAllocLength

    Parameters
    ----------

    len64 : int
      Passed on as it is.
    """
    #  int QV4::ExecutionEngine::safeForAllocLength(qint64 len64)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine18safeForAllocLengthEx', len64,
    )

  def global_(self) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::global()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executionengine.html#global
    """
    #  QV4::ReturnedValue QV4::ExecutionEngine::global()
    return self.uglySide.call('ritual_ZN3QV415ExecutionEngine6globalEv')

  def initQmlGlobalObject(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::initQmlGlobalObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#initQmlGlobalObject
    """
    #  void QV4::ExecutionEngine::initQmlGlobalObject()
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine19initQmlGlobalObjectEv',
    )

  def initializeGlobal(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::initializeGlobal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#initializeGlobal
    """
    #  void QV4::ExecutionEngine::initializeGlobal()
    self.uglySide.call('ritual_ZN3QV415ExecutionEngine16initializeGlobalEv')

  def createQtObject(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::createQtObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#createQtObject
    """
    #  void QV4::ExecutionEngine::createQtObject()
    self.uglySide.call('ritual_ZN3QV415ExecutionEngine14createQtObjectEv')

  @overload(WAIT['QV4.Value'])
  def freezeObject(self, value: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::freezeObject(const QV4::Value
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#freezeObject

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::ExecutionEngine::freezeObject(const QV4::Value &value)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine12freezeObjectERKNS_5ValueE',
        self._valueOf(value),
    )

  @overload(WAIT['QV4.Value'])
  def lockObject(self, value: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::lockObject(const QV4::Value
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#lockObject

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::ExecutionEngine::lockObject(const QV4::Value &value)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine10lockObjectERKNS_5ValueE',
        self._valueOf(value),
    )

  def setupXmlHttpRequestExtension(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::setupXmlHttpRequestExtension()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html
    """
    #  void QV4::ExecutionEngine::setupXmlHttpRequestExtension()
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine28setupXmlHttpRequestExtensionEv',
    )

  def resetQmlEngine(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::resetQmlEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#resetQmlEngine
    """
    #  void QV4::ExecutionEngine::resetQmlEngine()
    self.uglySide.call('ritual_ZN3QV415ExecutionEngine14resetQmlEngineEv')

  def delayedCallQueue(self) -> Optional[QQmlDelayedCallQueue]:
    """
    Calls Qt's 'QQmlDelayedCallQueue
    *QV4::ExecutionEngine::delayedCallQueue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#delayedCallQueue

    Returns
    -------

    Optional[QQmlDelayedCallQueue]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelayedCallQueue *QV4::ExecutionEngine::delayedCallQueue()
    address = self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine16delayedCallQueueEv',
    )
    from . import QQmlDelayedCallQueue
    return QQmlDelayedCallQueue._cuteAt(address)

  @overload(str)
  def startTimer(self, timerName: str) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::startTimer(const QString
    &timerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#startTimer

    Parameters
    ----------

    timerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::ExecutionEngine::startTimer(const QString &timerName)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine10startTimerERK7QString', timerName,
    )

  @overload(str, int, int)
  def consoleCountHelper(self, file: str, line: int, column: int) -> int:
    """
    Calls Qt's 'int QV4::ExecutionEngine::consoleCountHelper(const QString
    &file, quint16 line, quint16 column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#consoleCountHelper

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QV4::ExecutionEngine::consoleCountHelper(const QString &file,
    #      quint16 line, quint16 column)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine18consoleCountHelperERK7QStringtt',
        file, line, column,
    )

  def trimCompilationUnits(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::trimCompilationUnits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#trimCompilationUnits
    """
    #  void QV4::ExecutionEngine::trimCompilationUnits()
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine20trimCompilationUnitsEv',
    )

  @overload(QUrl)
  def trimCompilationUnitsForUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QV4::ExecutionEngine::trimCompilationUnitsForUrl(const
    QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QV4::ExecutionEngine::trimCompilationUnitsForUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine26trimCompilationUnitsForUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(
      WAIT['QV4.Function'], QObject, WAIT['QV4.ExecutionContext'], int,
      WAIT['QV4.Value'],
  )
  @overload(
      WAIT['QV4.Function'], QObject, WAIT['QV4.ExecutionContext'], int,
      NoneType,
  )
  @overload(WAIT['QV4.Function'], QObject, NoneType, int, WAIT['QV4.Value'])
  @overload(WAIT['QV4.Function'], QObject, NoneType, int, NoneType)
  @overload(
      WAIT['QV4.Function'], NoneType, WAIT['QV4.ExecutionContext'], int,
      WAIT['QV4.Value'],
  )
  @overload(
      WAIT['QV4.Function'], NoneType, WAIT['QV4.ExecutionContext'], int,
      NoneType,
  )
  @overload(WAIT['QV4.Function'], NoneType, NoneType, int, WAIT['QV4.Value'])
  @overload(WAIT['QV4.Function'], NoneType, NoneType, int, NoneType)
  @overload(
      NoneType, QObject, WAIT['QV4.ExecutionContext'], int,
      WAIT['QV4.Value'],
  )
  @overload(NoneType, QObject, WAIT['QV4.ExecutionContext'], int, NoneType)
  @overload(NoneType, QObject, NoneType, int, WAIT['QV4.Value'])
  @overload(NoneType, QObject, NoneType, int, NoneType)
  @overload(
      NoneType, NoneType, WAIT['QV4.ExecutionContext'], int,
      WAIT['QV4.Value'],
  )
  @overload(NoneType, NoneType, WAIT['QV4.ExecutionContext'], int, NoneType)
  @overload(NoneType, NoneType, NoneType, int, WAIT['QV4.Value'])
  @overload(NoneType, NoneType, NoneType, int, NoneType)
  def callInContext(
      self,
      function: Optional[QV4.Function],
      self_: Optional[QObject],
      ctxt: Optional[QV4.ExecutionContext],
      argc: int,
      argv: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QV4::ExecutionEngine::callInContext(QV4::Function *function, QObject
    *self_, QV4::ExecutionContext *ctxt, int argc, const QV4::Value *argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executionengine.html#callInContext

    Parameters
    ----------

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    self_ : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ctxt : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::ReturnedValue QV4::ExecutionEngine::callInContext(QV4::Function
    #      *function, QObject *self_, QV4::ExecutionContext *ctxt, int argc,
    #      const QV4::Value *argv)
    return self.uglySide.call(
        'ritual_ZN3QV415ExecutionEngine13callInContextEPNS_8FunctionEP7QObj'
        'ectPNS_16ExecutionContextEiPKNS_5ValueE',
        self._addressOf(function), self._addressOf(self_, 'QObject'),
        self._addressOf(ctxt), argc, self._addressOf(argv),
    )

  @staticmethod
  def callingQmlContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QV4::ExecutionEngine::callingQmlContext() const': the compiler refuses
    its ritual as it would be written here: member access into incomplete
    type 'QQmlContextData'.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.callingQmlContext' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QQmlContextData> "
        "QV4::ExecutionEngine::callingQmlContext() const': the compiler "
        "refuses its ritual as it would be written here: member access into "
        "incomplete type 'QQmlContextData'.")

  @staticmethod
  def canJIT(*__, **_) -> Never:
    """
    Qt's 'QV4::ExecutionEngine::canJIT': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.canJIT' has no cute function yet. Qt's "
        "'QV4::ExecutionEngine::canJIT': a template: a pattern and no "
        "single function.")

  @staticmethod
  def catchException(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ExecutionEngine::catchException(StackTrace
    *trace)': names 'QV4::StackTrace', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.catchException' has no cute function yet. "
        "Qt's 'ReturnedValue "
        "QV4::ExecutionEngine::catchException(StackTrace *trace)': names "
        "'QV4::StackTrace', which has no cute class yet.")

  @staticmethod
  def checkStackLimits(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ExecutionEngine::checkStackLimits()': leans on
    'QV4::stackProperties()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.checkStackLimits' has no cute function yet. "
        "Qt's 'bool QV4::ExecutionEngine::checkStackLimits()': leans on "
        "'QV4::stackProperties()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def compilationUnitForUrl(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutionEngine::compilationUnitForUrl(const QUrl &url) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.compilationUnitForUrl' has no cute function "
        "yet. Qt's 'QQmlRefPointer<ExecutableCompilationUnit> "
        "QV4::ExecutionEngine::compilationUnitForUrl(const QUrl &url) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def compilationUnits(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QUrl, QQmlRefPointer<ExecutableCompilationUnit>>
    QV4::ExecutionEngine::compilationUnits() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.compilationUnits' has no cute function yet. "
        "Qt's 'QMultiHash<QUrl, QQmlRefPointer<ExecutableCompilationUnit>> "
        "QV4::ExecutionEngine::compilationUnits() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def createPrimitive(*__, **_) -> Never:
    """
    Qt's 'QV4::ExecutionEngine::createPrimitive': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.createPrimitive' has no cute function yet. "
        "Qt's 'QV4::ExecutionEngine::createPrimitive': a template: a "
        "pattern and no single function.")

  @staticmethod
  def currentContext(*__, **_) -> Never:
    """
    Qt's 'QV4::ExecutionEngine::currentContext': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.currentContext' has no cute function yet. "
        "Qt's 'QV4::ExecutionEngine::currentContext': a template: a pattern "
        "and no single function.")

  @staticmethod
  def executableCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutionEngine::executableCompilationUnit(QQmlRefPointer<QV4::
    CompiledData::CompilationUnit> &&unit)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.executableCompilationUnit' has no cute "
        "function yet. Qt's 'QQmlRefPointer<ExecutableCompilationUnit> "
        "QV4::ExecutionEngine::executableCompilationUnit(QQmlRefPointer<QV4:"
        ":CompiledData::CompilationUnit> &&unit)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def fromData(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::fromData(QMetaType type,
    const void *ptr, Heap::Object *parent, int property, uint flags)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.fromData' has no cute function yet. Qt's "
        "'QV4::ReturnedValue QV4::ExecutionEngine::fromData(QMetaType type, "
        "const void *ptr, Heap::Object *parent, int property, uint flags)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def hasCppStackOverflow(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ExecutionEngine::hasCppStackOverflow()': leans on
    'QV4::stackProperties()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.hasCppStackOverflow' has no cute function "
        "yet. Qt's 'bool QV4::ExecutionEngine::hasCppStackOverflow()': "
        "leans on 'QV4::stackProperties()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def hasStackOverflow(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ExecutionEngine::hasStackOverflow()': leans on
    'QV4::stackProperties()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.hasStackOverflow' has no cute function yet. "
        "Qt's 'bool QV4::ExecutionEngine::hasStackOverflow()': leans on "
        "'QV4::stackProperties()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def inStack(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ExecutionEngine::inStack(const void *current) const':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.inStack' has no cute function yet. Qt's 'bool "
        "QV4::ExecutionEngine::inStack(const void *current) const': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def insertCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::ExecutionEngine::insertCompilationUnit(QQmlRefPointer<QV4::
    CompiledData::CompilationUnit> &&unit)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.insertCompilationUnit' has no cute function "
        "yet. Qt's 'QQmlRefPointer<ExecutableCompilationUnit> "
        "QV4::ExecutionEngine::insertCompilationUnit(QQmlRefPointer<QV4::Com"
        "piledData::CompilationUnit> &&unit)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def metaTypeFromJS(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ExecutionEngine::metaTypeFromJS(const Value &value,
    QMetaType type, void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.metaTypeFromJS' has no cute function yet. "
        "Qt's 'bool QV4::ExecutionEngine::metaTypeFromJS(const Value "
        "&value, QMetaType type, void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def metaTypeToJS(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QV4::ExecutionEngine::metaTypeToJS(QMetaType
    type, const void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.metaTypeToJS' has no cute function yet. Qt's "
        "'QV4::ReturnedValue QV4::ExecutionEngine::metaTypeToJS(QMetaType "
        "type, const void *data)': names 'void', which has no cute class "
        "yet.")

  @staticmethod
  def moduleForUrl(*__, **_) -> Never:
    """
    Qt's 'Module QV4::ExecutionEngine::moduleForUrl(const QUrl &_url, const
    ExecutableCompilationUnit *referrer)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.moduleForUrl' has no cute function yet. Qt's "
        "'Module QV4::ExecutionEngine::moduleForUrl(const QUrl &_url, const "
        "ExecutableCompilationUnit *referrer)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def newInternalClass(*__, **_) -> Never:
    """
    Qt's 'Heap::InternalClass *QV4::ExecutionEngine::newInternalClass(const
    VTable *vtable, Object *prototype)': names 'QV4::VTable', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.newInternalClass' has no cute function yet. "
        "Qt's 'Heap::InternalClass "
        "*QV4::ExecutionEngine::newInternalClass(const VTable *vtable, "
        "Object *prototype)': names 'QV4::VTable', which has no cute class "
        "yet.")

  @staticmethod
  def newVariantObject(*__, **_) -> Never:
    """
    Qt's 'Heap::Object *QV4::ExecutionEngine::newVariantObject(const
    QMetaType type, const void *data)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.newVariantObject' has no cute function yet. "
        "Qt's 'Heap::Object *QV4::ExecutionEngine::newVariantObject(const "
        "QMetaType type, const void *data)': names 'void', which has no "
        "cute class yet.")

  @staticmethod
  def registerNativeModule(*__, **_) -> Never:
    """
    Qt's 'Module QV4::ExecutionEngine::registerNativeModule(const QUrl &url,
    const QV4::Value &value)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.registerNativeModule' has no cute function "
        "yet. Qt's 'Module QV4::ExecutionEngine::registerNativeModule(const "
        "QUrl &url, const QV4::Value &value)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def setCppStackProperties(*__, **_) -> Never:
    """
    Qt's 'void QV4::ExecutionEngine::setCppStackProperties()': leans on
    'QV4::stackProperties()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.setCppStackProperties' has no cute function "
        "yet. Qt's 'void QV4::ExecutionEngine::setCppStackProperties()': "
        "leans on 'QV4::stackProperties()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def stackTrace(*__, **_) -> Never:
    """
    Qt's 'StackTrace QV4::ExecutionEngine::stackTrace(int frameLimit) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.stackTrace' has no cute function yet. Qt's "
        "'StackTrace QV4::ExecutionEngine::stackTrace(int frameLimit) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def stopTimer(*__, **_) -> Never:
    """
    Qt's 'qint64 QV4::ExecutionEngine::stopTimer(const QString &timerName,
    bool *wasRunning)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.stopTimer' has no cute function yet. Qt's "
        "'qint64 QV4::ExecutionEngine::stopTimer(const QString &timerName, "
        "bool *wasRunning)': takes a number to change where it is.")

  @staticmethod
  def typeLoader(*__, **_) -> Never:
    """
    Qt's 'QV4::ExecutionEngine::typeLoader': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.typeLoader' has no cute function yet. Qt's "
        "'QV4::ExecutionEngine::typeLoader': a template: a pattern and no "
        "single function.")

  @staticmethod
  def xmlHttpRequestData(*__, **_) -> Never:
    """
    Qt's 'void *QV4::ExecutionEngine::xmlHttpRequestData() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ExecutionEngine.xmlHttpRequestData' has no cute function yet. "
        "Qt's 'void *QV4::ExecutionEngine::xmlHttpRequestData() const': "
        "gives 'void', which has no cute class yet.")
