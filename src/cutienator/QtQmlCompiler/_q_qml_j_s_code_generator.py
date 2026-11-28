"""
QQmlJSCodeGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscodegenerator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSCodeGenerator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QStringList
from ..QtQml import QV4
from . import QQmlJSCompilePass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
  from . import QQmlJSAotFunction, QQmlJSMetaMethod, QQmlJSMetaProperty
  from . import QQmlJSRegisterContent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaMethod = WAIT['QQmlJSMetaMethod']
  QQmlJSRegisterContent = WAIT['QQmlJSRegisterContent']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSCodeGenerator(QQmlJSCompilePass):
  """
  The cute side of Qt's QQmlJSCodeGenerator: a plain Python object standing
  in front of one C++ QQmlJSCodeGenerator.

  It is built on the cute 'QQmlJSCompilePass', as Qt's QQmlJSCodeGenerator is
  built on Qt's QQmlJSCompilePass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSCodeGenerator that has a ritual and that
  Python can call so far, 187 names in all: 'run', 'generate_Ret',
  'generate_Debug', 'generate_LoadConst', 'generate_LoadZero',
  'generate_LoadTrue', 'generate_LoadFalse', 'generate_LoadNull',
  'generate_LoadUndefined', 'generate_LoadInt', 'generate_MoveConst',
  'generate_LoadReg', 'generate_StoreReg', 'generate_MoveReg',
  'generate_LoadImport', 'generate_LoadLocal', 'generate_StoreLocal',
  'generate_LoadScopedLocal', 'generate_StoreScopedLocal',
  'generate_LoadRuntimeString', 'generate_MoveRegExp',
  'generate_LoadClosure', 'generate_LoadName', 'generate_LoadGlobalLookup',
  'generate_LoadQmlContextPropertyLookup', 'generate_StoreNameSloppy',
  'generate_StoreNameStrict', 'generate_LoadElement',
  'generate_StoreElement', 'generate_LoadProperty',
  'generate_LoadOptionalProperty', 'generate_GetLookup',
  'generate_GetOptionalLookup', 'generate_StoreProperty',
  'generate_SetLookup', 'generate_LoadSuperProperty',
  'generate_StoreSuperProperty', 'generate_Yield', 'generate_YieldStar',
  'generate_Resume', 'generate_CallValue', 'generate_CallWithReceiver',
  'generate_CallProperty', 'generate_CallPropertyLookup',
  'generate_CallName', 'generate_CallPossiblyDirectEval',
  'generate_CallGlobalLookup', 'generate_CallQmlContextPropertyLookup',
  'generate_CallWithSpread', 'generate_TailCall', 'generate_Construct',
  'generate_ConstructWithSpread', 'generate_SetUnwindHandler',
  'generate_UnwindDispatch', 'generate_UnwindToLabel',
  'generate_DeadTemporalZoneCheck', 'generate_ThrowException',
  'generate_GetException', 'generate_SetException',
  'generate_CreateCallContext', 'generate_PushCatchContext',
  'generate_PushWithContext', 'generate_PushBlockContext',
  'generate_CloneBlockContext', 'generate_PushScriptContext',
  'generate_PopScriptContext', 'generate_PopContext', 'generate_GetIterator',
  'generate_IteratorNext', 'generate_IteratorNextForYieldStar',
  'generate_IteratorClose', 'generate_DestructureRestElement',
  'generate_DeleteProperty', 'generate_DeleteName', 'generate_TypeofName',
  'generate_TypeofValue', 'generate_DeclareVar', 'generate_DefineArray',
  'generate_DefineObjectLiteral', 'generate_CreateClass',
  'generate_CreateMappedArgumentsObject',
  'generate_CreateUnmappedArgumentsObject', 'generate_CreateRestParameter',
  'generate_ConvertThisToObject', 'generate_LoadSuperConstructor',
  'generate_ToObject', 'generate_Jump', 'generate_JumpTrue',
  'generate_JumpFalse', 'generate_JumpNoException',
  'generate_JumpNotUndefined', 'generate_CheckException',
  'generate_CmpEqNull', 'generate_CmpNeNull', 'generate_CmpEqInt',
  'generate_CmpNeInt', 'generate_CmpEq', 'generate_CmpNe', 'generate_CmpGt',
  'generate_CmpGe', 'generate_CmpLt', 'generate_CmpLe',
  'generate_CmpStrictEqual', 'generate_CmpStrictNotEqual', 'generate_CmpIn',
  'generate_CmpInstanceOf', 'generate_As', 'generate_UNot', 'generate_UPlus',
  'generate_UMinus', 'generate_UCompl', 'generate_Increment',
  'generate_Decrement', 'generate_Add', 'generate_BitAnd', 'generate_BitOr',
  'generate_BitXor', 'generate_UShr', 'generate_Shr', 'generate_Shl',
  'generate_BitAndConst', 'generate_BitOrConst', 'generate_BitXorConst',
  'generate_UShrConst', 'generate_ShrConst', 'generate_ShlConst',
  'generate_Exp', 'generate_Mul', 'generate_Div', 'generate_Mod',
  'generate_Sub', 'generate_InitializeBlockDeadTemporalZone',
  'generate_ThrowOnNullOrUndefined', 'generate_GetTemplateObject',
  'endInstruction', 'addInclude', 'conversion', 'convertContained',
  'generateReturnError', 'reject', 'skip', 'compositeMetaType',
  'compositeListMetaType', 'contentPointer', 'contentType',
  'generateSetInstructionPointer', 'generateLookup', 'getLookupPreparation',
  'generateEnumLookup', 'registerVariable', 'lookupVariable',
  'consumedRegisterVariable', 'consumedAccumulatorVariableIn',
  'changedRegisterVariable', 'registerType', 'lookupType',
  'shouldMoveRegister', 'resetState', 'generateExceptionCheck',
  'generateEqualityOperation', 'generateCompareOperation',
  'generateArithmeticOperation', 'generateShiftOperation',
  'generateArithmeticConstOperation', 'generateJumpCodeWithTypeConversions',
  'generateUnaryOperation', 'generateInPlaceOperation',
  'generateMoveOutVarAfterCall', 'generateTypeLookup',
  'generateVariantEqualityComparison', 'generateArrayInitializer',
  'generateWriteBack', 'rejectIfNonQObjectOut', 'rejectIfBadArray',
  'initAndCall', 'inlineStringMethod', 'inlineTranslateMethod',
  'inlineMathMethod', 'inlineConsoleMethod', 'inlineArrayMethod',
  'generate_GetLookupHelper', 'generateCallConstructor',
  'generateVariantMapGetLookup', 'originalType', 'originalProperty',
  'originalMethod', 'isRegisterAffectedBySideEffects'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSCodeGenerator::QQmlJSCodeGenerator(const
    QV4::Compiler::Context *compilerContext, const
    QV4::Compiler::JSUnitGenerator *unitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations, bool noAotValidation)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QQmlJSCodeGenerator::~QQmlJSCodeGenerator()': the destructor:
    Python never removes a C++ QQmlJSCodeGenerator.
  - Qt's 'LookupSignatures QQmlJSCodeGenerator::lookupSignatures() const':
    gives a type Python has no way to take yet.
  - Qt's 'QString QQmlJSCodeGenerator::metaObject(const QQmlJSScope::ConstPtr
    &objectType)': takes a type Python has no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::metaType(const QQmlJSScope::ConstPtr
    &type)': takes a type Python has no way to hand over yet.
  - Qt's 'Verdict
    QQmlJSCodeGenerator::startInstruction(QV4::Moth::Instr::Type a0)': gives
    the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot be
    named here.
  - Qt's 'QString QQmlJSCodeGenerator::conversion(const QQmlJSScope::ConstPtr
    &from, QQmlJSRegisterContent to, const QString &variable)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::conversion(QQmlJSRegisterContent from,
    const QQmlJSScope::ConstPtr &to, const QString &variable)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::conversion(const QQmlJSScope::ConstPtr
    &from, const QQmlJSScope::ConstPtr &to, const QString &variable)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::convertStored(const
    QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to, const
    QString &variable)': takes a type Python has no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::metaTypeFromType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::metaTypeFromName(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlJSCodeGenerator::recordPropertyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQmlJSCodeGenerator::recordMethodLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QQmlJSCodeGenerator::recordEnumKeyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const
    QString &keyName)': takes a type Python has no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::castTargetName(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::resolveValueTypeContentPointer(const
    QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
    QString &variable, const QString &errorMessage)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::resolveQObjectPointer(const
    QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
    QString &variable, const QString &errorMessage)': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QQmlJSCodeGenerator::generateContentPointerCheck(const
    QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
    QString &variable, const QString &errorMessage)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QString QQmlJSCodeGenerator::generateVariantMapSetLookup(const
    QString &map, const int nameIndex, const QQmlJSScope::ConstPtr &property,
    const QString &variableIn)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSCodeGenerator::literalType(const
    QQmlJSScope::ConstPtr &contained)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 213 functions Qt declares: 1 a template; 1 not a gap.

  What to expect
  --------------

  - The C++ QQmlJSCodeGenerator is created at the first use, not by
    'QQmlJSCodeGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSCodeGenerator.
  - Each name of Qt's QQmlJSCodeGenerator that has no cute function yet,
    '__init__', 'castTargetName', 'convertStored',
    'generateContentPointerCheck', 'generateVariantMapSetLookup',
    'literalType', 'lookupSignatures', 'metaObject', 'metaType',
    'metaTypeFromName', 'metaTypeFromType', 'recordEnumKeyLookup',
    'recordMethodLookup', 'recordPropertyLookup', 'resolveQObjectPointer',
    'resolveValueTypeContentPointer', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSCodeGenerator'

  #  A C++ QQmlJSCodeGenerator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSCodeGenerator'

  #  The functions Qt calls itself that QQmlJSCodeGenerator is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'metaType': (
          'QString QQmlJSCodeGenerator::metaType(const '
          'QQmlJSScope::ConstPtr &)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def compositeMetaType(self, elementName: str) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::compositeMetaType(const QString
    &elementName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#compositeMetaType

    Parameters
    ----------

    elementName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::compositeMetaType(const QString
    #      &elementName) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator17compositeMetaTypeERK7QString',
        elementName,
    )

  @overload(str)
  def compositeListMetaType(self, elementName: str) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::compositeListMetaType(const
    QString &elementName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#compositeListMetaType

    Parameters
    ----------

    elementName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::compositeListMetaType(const QString
    #      &elementName) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator21compositeListMetaTypeERK7QString',
        elementName,
    )

  @overload(int)
  def registerVariable(self, index: int) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::registerVariable(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#registerVariable

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::registerVariable(int index) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator16registerVariableEi', index,
    )

  @overload(int)
  def lookupVariable(self, lookupIndex: int) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::lookupVariable(int lookupIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#lookupVariable

    Parameters
    ----------

    lookupIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::lookupVariable(int lookupIndex) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator14lookupVariableEi', lookupIndex,
    )

  @overload(int)
  def consumedRegisterVariable(self, index: int) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::consumedRegisterVariable(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#consumedRegisterVariable

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::consumedRegisterVariable(int index) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator24consumedRegisterVariableEi', index,
    )

  def consumedAccumulatorVariableIn(self) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::consumedAccumulatorVariableIn()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::consumedAccumulatorVariableIn() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator29consumedAccumulatorVariableInEv',
    )

  def changedRegisterVariable(self) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::changedRegisterVariable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#changedRegisterVariable

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::changedRegisterVariable() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator23changedRegisterVariableEv',
    )

  @overload(int)
  def registerType(self, index: int) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSCodeGenerator::registerType(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#registerType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSCodeGenerator::registerType(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator12registerTypeEi', index,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(int)
  def lookupType(self, lookupIndex: int) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSCodeGenerator::lookupType(int
    lookupIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#lookupType

    Parameters
    ----------

    lookupIndex : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSCodeGenerator::lookupType(int lookupIndex)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator10lookupTypeEi', lookupIndex,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(int)
  def shouldMoveRegister(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::shouldMoveRegister(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#shouldMoveRegister

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::shouldMoveRegister(int index) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator18shouldMoveRegisterEi', index,
    )

  @overload(QQmlJSRegisterContent)
  def originalProperty(
      self,
      reg: QQmlJSRegisterContent,
  ) -> QQmlJSMetaProperty:
    """
    Calls Qt's 'QQmlJSMetaProperty
    QQmlJSCodeGenerator::originalProperty(const QQmlJSRegisterContent &reg)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#originalProperty

    Parameters
    ----------

    reg : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSMetaProperty
      A new cute QQmlJSMetaProperty around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaProperty QQmlJSCodeGenerator::originalProperty(const
    #      QQmlJSRegisterContent &reg) const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator16originalPropertyERK21QQmlJSRegist'
        'erContent',
        self._valueOf(reg),
    )
    from . import QQmlJSMetaProperty
    return QQmlJSMetaProperty._cuteOwning(address)

  @overload(QQmlJSRegisterContent)
  def originalMethod(self, reg: QQmlJSRegisterContent) -> QQmlJSMetaMethod:
    """
    Calls Qt's 'QQmlJSMetaMethod QQmlJSCodeGenerator::originalMethod(const
    QQmlJSRegisterContent &reg) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#originalMethod

    Parameters
    ----------

    reg : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSMetaMethod
      A new cute QQmlJSMetaMethod around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaMethod QQmlJSCodeGenerator::originalMethod(const
    #      QQmlJSRegisterContent &reg) const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSCodeGenerator14originalMethodERK21QQmlJSRegister'
        'Content',
        self._valueOf(reg),
    )
    from . import QQmlJSMetaMethod
    return QQmlJSMetaMethod._cuteOwning(address)

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
    Qt's 'QQmlJSCodeGenerator::QQmlJSCodeGenerator(const
    QV4::Compiler::Context *compilerContext, const
    QV4::Compiler::JSUnitGenerator *unitGenerator, const QQmlJSTypeResolver
    *typeResolver, QQmlJSLogger *logger, const BasicBlocks &basicBlocks,
    const InstructionAnnotations &annotations, bool noAotValidation)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.__init__' has no cute function yet. Qt's "
        "'QQmlJSCodeGenerator::QQmlJSCodeGenerator(const "
        "QV4::Compiler::Context *compilerContext, const "
        "QV4::Compiler::JSUnitGenerator *unitGenerator, const "
        "QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger, const "
        "BasicBlocks &basicBlocks, const InstructionAnnotations "
        "&annotations, bool noAotValidation)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload(QQmlJSCompilePass.Function, bool)
  @overload(NoneType, bool)
  def run(
      self,
      function: Optional[QQmlJSCompilePass.Function],
      basicBlocksValidationFailed: bool,
  ) -> QQmlJSAotFunction:
    """
    Calls Qt's 'QQmlJSAotFunction QQmlJSCodeGenerator::run(const Function
    *function, bool basicBlocksValidationFailed)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscodegenerator.html#run

    Parameters
    ----------

    function : Optional[QQmlJSCompilePass.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    basicBlocksValidationFailed : bool
      Passed on as it is.

    Returns
    -------

    QQmlJSAotFunction
      A new cute QQmlJSAotFunction around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSAotFunction QQmlJSCodeGenerator::run(const Function *function,
    #      bool basicBlocksValidationFailed)
    address = self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator3runEPKN17QQmlJSCompilePass8Function'
        'Eb',
        self._addressOf(function), basicBlocksValidationFailed,
    )
    from . import QQmlJSAotFunction
    return QQmlJSAotFunction._cuteOwning(address)

  def generate_Ret(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Ret()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Ret
    """
    #  void QQmlJSCodeGenerator::generate_Ret()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_RetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_RetEv'
    self.uglySide.call(ritual)

  def generate_Debug(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Debug()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Debug
    """
    #  void QQmlJSCodeGenerator::generate_Debug()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_DebugEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_DebugEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_LoadConst(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadConst(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadConst

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadConst(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_LoadConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_LoadConstEi'
    self.uglySide.call(ritual, index)

  def generate_LoadZero(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadZero()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadZero
    """
    #  void QQmlJSCodeGenerator::generate_LoadZero()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_LoadZeroEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadZeroEv'
    self.uglySide.call(ritual)

  def generate_LoadTrue(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadTrue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadTrue
    """
    #  void QQmlJSCodeGenerator::generate_LoadTrue()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_LoadTrueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadTrueEv'
    self.uglySide.call(ritual)

  def generate_LoadFalse(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadFalse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadFalse
    """
    #  void QQmlJSCodeGenerator::generate_LoadFalse()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_LoadFalseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_LoadFalseEv'
    self.uglySide.call(ritual)

  def generate_LoadNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadNull
    """
    #  void QQmlJSCodeGenerator::generate_LoadNull()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_LoadNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadNullEv'
    self.uglySide.call(ritual)

  def generate_LoadUndefined(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadUndefined
    """
    #  void QQmlJSCodeGenerator::generate_LoadUndefined()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator22generate_LoadUndefinedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator22generate_LoadUndefinedEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_LoadInt(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadInt(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadInt

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadInt(int value)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator16generate_LoadIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator16generate_LoadIntEi'
    self.uglySide.call(ritual, value)

  @overload(int, int)
  def generate_MoveConst(self, constIndex: int, destTemp: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_MoveConst(int constIndex,
    int destTemp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_MoveConst

    Parameters
    ----------

    constIndex : int
      Passed on as it is.

    destTemp : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_MoveConst(int constIndex, int
    #      destTemp)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_MoveConstEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_MoveConstEii'
    self.uglySide.call(ritual, constIndex, destTemp)

  @overload(int)
  def generate_LoadReg(self, reg: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadReg(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadReg

    Parameters
    ----------

    reg : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadReg(int reg)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator16generate_LoadRegEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator16generate_LoadRegEi'
    self.uglySide.call(ritual, reg)

  @overload(int)
  def generate_StoreReg(self, reg: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreReg(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreReg

    Parameters
    ----------

    reg : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreReg(int reg)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_StoreRegEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_StoreRegEi'
    self.uglySide.call(ritual, reg)

  @overload(int, int)
  def generate_MoveReg(self, srcReg: int, destReg: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_MoveReg(int srcReg, int
    destReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_MoveReg

    Parameters
    ----------

    srcReg : int
      Passed on as it is.

    destReg : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_MoveReg(int srcReg, int destReg)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator16generate_MoveRegEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator16generate_MoveRegEii'
    self.uglySide.call(ritual, srcReg, destReg)

  @overload(int)
  def generate_LoadImport(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadImport(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadImport

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadImport(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_LoadImportEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_LoadImportEi'
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_LoadLocal(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadLocal(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadLocal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadLocal(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_LoadLocalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_LoadLocalEi'
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_StoreLocal(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreLocal(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreLocal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreLocal(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_StoreLocalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_StoreLocalEi'
    self.uglySide.call(ritual, index)

  @overload(int, int)
  def generate_LoadScopedLocal(self, scope: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadScopedLocal(int scope,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadScopedLocal

    Parameters
    ----------

    scope : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadScopedLocal(int scope, int
    #      index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator24generate_LoadScopedLocalEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator24generate_LoadScopedLocalEii')
    self.uglySide.call(ritual, scope, index)

  @overload(int, int)
  def generate_StoreScopedLocal(self, scope: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreScopedLocal(int
    scope, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreScopedLocal

    Parameters
    ----------

    scope : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreScopedLocal(int scope, int
    #      index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_StoreScopedLocalEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_StoreScopedLocalEii')
    self.uglySide.call(ritual, scope, index)

  @overload(int)
  def generate_LoadRuntimeString(self, stringId: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadRuntimeString(int
    stringId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    stringId : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadRuntimeString(int stringId)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_LoadRuntimeStringEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_LoadRuntimeStringEi')
    self.uglySide.call(ritual, stringId)

  @overload(int, int)
  def generate_MoveRegExp(self, regExpId: int, destReg: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_MoveRegExp(int regExpId,
    int destReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_MoveRegExp

    Parameters
    ----------

    regExpId : int
      Passed on as it is.

    destReg : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_MoveRegExp(int regExpId, int
    #      destReg)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_MoveRegExpEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_MoveRegExpEii'
    self.uglySide.call(ritual, regExpId, destReg)

  @overload(int)
  def generate_LoadClosure(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadClosure(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadClosure

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadClosure(int value)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_LoadClosureEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_LoadClosureEi'
    self.uglySide.call(ritual, value)

  @overload(int)
  def generate_LoadName(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadName(int nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadName

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadName(int nameIndex)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_LoadNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadNameEi'
    self.uglySide.call(ritual, nameIndex)

  @overload(int)
  def generate_LoadGlobalLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadGlobalLookup(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadGlobalLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadGlobalLookup(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_LoadGlobalLookupEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_LoadGlobalLookupEi')
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_LoadQmlContextPropertyLookup(self, index: int) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(int
    #      index)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator37generate_LoadQmlContextPropertyLoo'
        'kupEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator37generate_LoadQmlContextPrope'
          'rtyLookupEi')
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_StoreNameSloppy(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreNameSloppy(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreNameSloppy

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreNameSloppy(int nameIndex)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator24generate_StoreNameSloppyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator24generate_StoreNameSloppyEi')
    self.uglySide.call(ritual, nameIndex)

  @overload(int)
  def generate_StoreNameStrict(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreNameStrict(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreNameStrict

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreNameStrict(int name)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator24generate_StoreNameStrictEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator24generate_StoreNameStrictEi')
    self.uglySide.call(ritual, name)

  @overload(int)
  def generate_LoadElement(self, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadElement(int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadElement

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadElement(int base)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_LoadElementEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_LoadElementEi'
    self.uglySide.call(ritual, base)

  @overload(int, int)
  def generate_StoreElement(self, base: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreElement(int base, int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreElement

    Parameters
    ----------

    base : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreElement(int base, int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator21generate_StoreElementEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator21generate_StoreElementEii'
    self.uglySide.call(ritual, base, index)

  @overload(int)
  def generate_LoadProperty(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadProperty(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_LoadProperty

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadProperty(int nameIndex)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator21generate_LoadPropertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator21generate_LoadPropertyEi'
    self.uglySide.call(ritual, nameIndex)

  @overload(int, int)
  def generate_LoadOptionalProperty(self, name: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadOptionalProperty(int
    name, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    name : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadOptionalProperty(int name, int
    #      offset)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator29generate_LoadOptionalPropertyEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator29generate_LoadOptionalPropert'
          'yEii')
    self.uglySide.call(ritual, name, offset)

  @overload(int)
  def generate_GetLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_GetLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_GetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_GetLookup(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_GetLookupEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_GetLookupEi'
    self.uglySide.call(ritual, index)

  @overload(int, int)
  def generate_GetOptionalLookup(self, index: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_GetOptionalLookup(int
    index, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_GetOptionalLookup(int index, int
    #      offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_GetOptionalLookupEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_GetOptionalLookupEi'
          'i')
    self.uglySide.call(ritual, index, offset)

  @overload(int, int)
  def generate_StoreProperty(self, name: int, baseReg: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreProperty(int name,
    int baseReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_StoreProperty

    Parameters
    ----------

    name : int
      Passed on as it is.

    baseReg : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreProperty(int name, int
    #      baseReg)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator22generate_StorePropertyEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator22generate_StorePropertyEii')
    self.uglySide.call(ritual, name, baseReg)

  @overload(int, int)
  def generate_SetLookup(self, index: int, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_SetLookup(int index, int
    base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_SetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_SetLookup(int index, int base)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_SetLookupEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_SetLookupEii'
    self.uglySide.call(ritual, index, base)

  @overload(int)
  def generate_LoadSuperProperty(self, property: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadSuperProperty(int
    property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    property : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_LoadSuperProperty(int property)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_LoadSuperPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_LoadSuperPropertyEi')
    self.uglySide.call(ritual, property)

  @overload(int)
  def generate_StoreSuperProperty(self, property: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_StoreSuperProperty(int
    property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    property : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_StoreSuperProperty(int property)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator27generate_StoreSuperPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator27generate_StoreSuperPropertyE'
          'i')
    self.uglySide.call(ritual, property)

  def generate_Yield(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Yield()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Yield
    """
    #  void QQmlJSCodeGenerator::generate_Yield()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_YieldEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_YieldEv'
    self.uglySide.call(ritual)

  def generate_YieldStar(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_YieldStar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_YieldStar
    """
    #  void QQmlJSCodeGenerator::generate_YieldStar()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_YieldStarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_YieldStarEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Resume(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Resume(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Resume

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Resume(int a0)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator15generate_ResumeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator15generate_ResumeEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int, int)
  def generate_CallValue(self, name: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallValue(int name, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CallValue

    Parameters
    ----------

    name : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallValue(int name, int argc, int
    #      argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_CallValueEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_CallValueEiii'
    self.uglySide.call(ritual, name, argc, argv)

  @overload(int, int, int, int)
  def generate_CallWithReceiver(
      self,
      name: int,
      thisObject: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallWithReceiver(int name,
    int thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CallWithReceiver

    Parameters
    ----------

    name : int
      Passed on as it is.

    thisObject : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallWithReceiver(int name, int
    #      thisObject, int argc, int argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_CallWithReceiverEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_CallWithReceiverEii'
          'ii')
    self.uglySide.call(ritual, name, thisObject, argc, argv)

  @overload(int, int, int, int)
  def generate_CallProperty(
      self,
      name: int,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallProperty(int name, int
    base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CallProperty

    Parameters
    ----------

    name : int
      Passed on as it is.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallProperty(int name, int base,
    #      int argc, int argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator21generate_CallPropertyEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator21generate_CallPropertyEiiii')
    self.uglySide.call(ritual, name, base, argc, argv)

  @overload(int, int, int, int)
  def generate_CallPropertyLookup(
      self,
      lookupIndex: int,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallPropertyLookup(int
    lookupIndex, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    lookupIndex : int
      Passed on as it is.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallPropertyLookup(int lookupIndex,
    #      int base, int argc, int argv)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator27generate_CallPropertyLookupEiiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator27generate_CallPropertyLookupE'
          'iiii')
    self.uglySide.call(ritual, lookupIndex, base, argc, argv)

  @overload(int, int, int)
  def generate_CallName(self, name: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallName(int name, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CallName

    Parameters
    ----------

    name : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallName(int name, int argc, int
    #      argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_CallNameEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_CallNameEiii'
    self.uglySide.call(ritual, name, argc, argv)

  @overload(int, int)
  def generate_CallPossiblyDirectEval(self, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallPossiblyDirectEval(int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallPossiblyDirectEval(int argc,
    #      int argv)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator31generate_CallPossiblyDirectEvalEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator31generate_CallPossiblyDirectE'
          'valEii')
    self.uglySide.call(ritual, argc, argv)

  @overload(int, int, int)
  def generate_CallGlobalLookup(
      self,
      index: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallGlobalLookup(int
    index, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CallGlobalLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallGlobalLookup(int index, int
    #      argc, int argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_CallGlobalLookupEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_CallGlobalLookupEii'
          'i')
    self.uglySide.call(ritual, index, argc, argv)

  @overload(int, int, int)
  def generate_CallQmlContextPropertyLookup(
      self,
      index: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(int index, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(int
    #      index, int argc, int argv)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator37generate_CallQmlContextPropertyLoo'
        'kupEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator37generate_CallQmlContextPrope'
          'rtyLookupEiii')
    self.uglySide.call(ritual, index, argc, argv)

  @overload(int, int, int, int)
  def generate_CallWithSpread(
      self,
      func: int,
      thisObject: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CallWithSpread(int func,
    int thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CallWithSpread

    Parameters
    ----------

    func : int
      Passed on as it is.

    thisObject : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CallWithSpread(int func, int
    #      thisObject, int argc, int argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator23generate_CallWithSpreadEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator23generate_CallWithSpreadEiiii')
    self.uglySide.call(ritual, func, thisObject, argc, argv)

  @overload(int, int, int, int)
  def generate_TailCall(
      self,
      func: int,
      thisObject: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_TailCall(int func, int
    thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_TailCall

    Parameters
    ----------

    func : int
      Passed on as it is.

    thisObject : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_TailCall(int func, int thisObject,
    #      int argc, int argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_TailCallEiiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_TailCallEiiii'
    self.uglySide.call(ritual, func, thisObject, argc, argv)

  @overload(int, int, int)
  def generate_Construct(self, func: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Construct(int func, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Construct

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Construct(int func, int argc, int
    #      argv)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_ConstructEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_ConstructEiii'
    self.uglySide.call(ritual, func, argc, argv)

  @overload(int, int, int)
  def generate_ConstructWithSpread(
      self,
      func: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ConstructWithSpread(int
    func, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_ConstructWithSpread(int func, int
    #      argc, int argv)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator28generate_ConstructWithSpreadEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator28generate_ConstructWithSpread'
          'Eiii')
    self.uglySide.call(ritual, func, argc, argv)

  @overload(int)
  def generate_SetUnwindHandler(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_SetUnwindHandler(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_SetUnwindHandler

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_SetUnwindHandler(int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_SetUnwindHandlerEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_SetUnwindHandlerEi')
    self.uglySide.call(ritual, offset)

  def generate_UnwindDispatch(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UnwindDispatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UnwindDispatch
    """
    #  void QQmlJSCodeGenerator::generate_UnwindDispatch()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator23generate_UnwindDispatchEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator23generate_UnwindDispatchEv')
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_UnwindToLabel(self, level: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UnwindToLabel(int level,
    int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UnwindToLabel

    Parameters
    ----------

    level : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_UnwindToLabel(int level, int
    #      offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator22generate_UnwindToLabelEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator22generate_UnwindToLabelEii')
    self.uglySide.call(ritual, level, offset)

  @overload(int)
  def generate_DeadTemporalZoneCheck(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(int name)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator30generate_DeadTemporalZoneCheckEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator30generate_DeadTemporalZoneChe'
          'ckEi')
    self.uglySide.call(ritual, name)

  def generate_ThrowException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ThrowException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_ThrowException
    """
    #  void QQmlJSCodeGenerator::generate_ThrowException()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator23generate_ThrowExceptionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator23generate_ThrowExceptionEv')
    self.uglySide.call(ritual)

  def generate_GetException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_GetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_GetException
    """
    #  void QQmlJSCodeGenerator::generate_GetException()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator21generate_GetExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator21generate_GetExceptionEv'
    self.uglySide.call(ritual)

  def generate_SetException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_SetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_SetException
    """
    #  void QQmlJSCodeGenerator::generate_SetException()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator21generate_SetExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator21generate_SetExceptionEv'
    self.uglySide.call(ritual)

  def generate_CreateCallContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CreateCallContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_CreateCallContext()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_CreateCallContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_CreateCallContextEv')
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_PushCatchContext(self, index: int, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_PushCatchContext(int
    index, int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_PushCatchContext

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_PushCatchContext(int index, int
    #      name)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_PushCatchContextEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_PushCatchContextEii')
    self.uglySide.call(ritual, index, name)

  def generate_PushWithContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_PushWithContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_PushWithContext
    """
    #  void QQmlJSCodeGenerator::generate_PushWithContext()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator24generate_PushWithContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator24generate_PushWithContextEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_PushBlockContext(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_PushBlockContext(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_PushBlockContext

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_PushBlockContext(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_PushBlockContextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_PushBlockContextEi')
    self.uglySide.call(ritual, index)

  def generate_CloneBlockContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CloneBlockContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_CloneBlockContext()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_CloneBlockContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_CloneBlockContextEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_PushScriptContext(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_PushScriptContext(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_PushScriptContext(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_PushScriptContextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_PushScriptContextEi')
    self.uglySide.call(ritual, index)

  def generate_PopScriptContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_PopScriptContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_PopScriptContext
    """
    #  void QQmlJSCodeGenerator::generate_PopScriptContext()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_PopScriptContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_PopScriptContextEv')
    self.uglySide.call(ritual)

  def generate_PopContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_PopContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_PopContext
    """
    #  void QQmlJSCodeGenerator::generate_PopContext()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_PopContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_PopContextEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_GetIterator(self, iterator: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_GetIterator(int
    iterator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_GetIterator

    Parameters
    ----------

    iterator : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_GetIterator(int iterator)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_GetIteratorEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_GetIteratorEi'
    self.uglySide.call(ritual, iterator)

  @overload(int, int)
  def generate_IteratorNext(self, value: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_IteratorNext(int value,
    int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_IteratorNext

    Parameters
    ----------

    value : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_IteratorNext(int value, int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator21generate_IteratorNextEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator21generate_IteratorNextEii'
    self.uglySide.call(ritual, value, offset)

  @overload(int, int, int)
  def generate_IteratorNextForYieldStar(
      self,
      iterator: int,
      object: int,
      offset: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generate_IteratorNextForYieldStar(int iterator, int
    object, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    iterator : int
      Passed on as it is.

    object : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_IteratorNextForYieldStar(int
    #      iterator, int object, int offset)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator33generate_IteratorNextForYieldStarE'
        'iii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator33generate_IteratorNextForYiel'
          'dStarEiii')
    self.uglySide.call(ritual, iterator, object, offset)

  def generate_IteratorClose(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_IteratorClose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_IteratorClose
    """
    #  void QQmlJSCodeGenerator::generate_IteratorClose()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator22generate_IteratorCloseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator22generate_IteratorCloseEv'
    self.uglySide.call(ritual)

  def generate_DestructureRestElement(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DestructureRestElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_DestructureRestElement()
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator31generate_DestructureRestElementEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator31generate_DestructureRestElem'
          'entEv')
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DeleteProperty(self, base: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DeleteProperty(int base,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_DeleteProperty

    Parameters
    ----------

    base : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_DeleteProperty(int base, int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator23generate_DeletePropertyEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator23generate_DeletePropertyEii')
    self.uglySide.call(ritual, base, index)

  @overload(int)
  def generate_DeleteName(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DeleteName(int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_DeleteName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_DeleteName(int name)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_DeleteNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_DeleteNameEi'
    self.uglySide.call(ritual, name)

  @overload(int)
  def generate_TypeofName(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_TypeofName(int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_TypeofName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_TypeofName(int name)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_TypeofNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_TypeofNameEi'
    self.uglySide.call(ritual, name)

  def generate_TypeofValue(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_TypeofValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_TypeofValue
    """
    #  void QQmlJSCodeGenerator::generate_TypeofValue()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_TypeofValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_TypeofValueEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DeclareVar(self, varName: int, isDeletable: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DeclareVar(int varName,
    int isDeletable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_DeclareVar

    Parameters
    ----------

    varName : int
      Passed on as it is.

    isDeletable : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_DeclareVar(int varName, int
    #      isDeletable)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_DeclareVarEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_DeclareVarEii'
    self.uglySide.call(ritual, varName, isDeletable)

  @overload(int, int)
  def generate_DefineArray(self, argc: int, args: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DefineArray(int argc, int
    args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_DefineArray

    Parameters
    ----------

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_DefineArray(int argc, int args)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_DefineArrayEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_DefineArrayEii'
    self.uglySide.call(ritual, argc, args)

  @overload(int, int, int)
  def generate_DefineObjectLiteral(
      self,
      internalClassId: int,
      argc: int,
      args: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_DefineObjectLiteral(int
    internalClassId, int argc, int args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    internalClassId : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_DefineObjectLiteral(int
    #      internalClassId, int argc, int args)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator28generate_DefineObjectLiteralEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator28generate_DefineObjectLiteral'
          'Eiii')
    self.uglySide.call(ritual, internalClassId, argc, args)

  @overload(int, int, int)
  def generate_CreateClass(
      self,
      classIndex: int,
      heritage: int,
      computedNames: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CreateClass(int
    classIndex, int heritage, int computedNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CreateClass

    Parameters
    ----------

    classIndex : int
      Passed on as it is.

    heritage : int
      Passed on as it is.

    computedNames : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CreateClass(int classIndex, int
    #      heritage, int computedNames)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_CreateClassEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_CreateClassEiii'
    self.uglySide.call(ritual, classIndex, heritage, computedNames)

  def generate_CreateMappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject()
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator36generate_CreateMappedArgumentsObje'
        'ctEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator36generate_CreateMappedArgumen'
          'tsObjectEv')
    self.uglySide.call(ritual)

  def generate_CreateUnmappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject()
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator38generate_CreateUnmappedArgumentsOb'
        'jectEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator38generate_CreateUnmappedArgum'
          'entsObjectEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CreateRestParameter(self, argIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CreateRestParameter(int
    argIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    argIndex : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CreateRestParameter(int argIndex)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator28generate_CreateRestParameterEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator28generate_CreateRestParameter'
          'Ei')
    self.uglySide.call(ritual, argIndex)

  def generate_ConvertThisToObject(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ConvertThisToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_ConvertThisToObject()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator28generate_ConvertThisToObjectEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator28generate_ConvertThisToObject'
          'Ev')
    self.uglySide.call(ritual)

  def generate_LoadSuperConstructor(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_LoadSuperConstructor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_LoadSuperConstructor()
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator29generate_LoadSuperConstructorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator29generate_LoadSuperConstructo'
          'rEv')
    self.uglySide.call(ritual)

  def generate_ToObject(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_ToObject
    """
    #  void QQmlJSCodeGenerator::generate_ToObject()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_ToObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_ToObjectEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Jump(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Jump(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Jump

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Jump(int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator13generate_JumpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator13generate_JumpEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpTrue(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_JumpTrue(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_JumpTrue

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_JumpTrue(int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_JumpTrueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_JumpTrueEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpFalse(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_JumpFalse(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_JumpFalse

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_JumpFalse(int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_JumpFalseEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_JumpFalseEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpNoException(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_JumpNoException(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_JumpNoException

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_JumpNoException(int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator24generate_JumpNoExceptionEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator24generate_JumpNoExceptionEi')
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpNotUndefined(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_JumpNotUndefined(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_JumpNotUndefined

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_JumpNotUndefined(int offset)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator25generate_JumpNotUndefinedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator25generate_JumpNotUndefinedEi')
    self.uglySide.call(ritual, offset)

  def generate_CheckException(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CheckException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CheckException
    """
    #  void QQmlJSCodeGenerator::generate_CheckException()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator23generate_CheckExceptionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator23generate_CheckExceptionEv')
    self.uglySide.call(ritual)

  def generate_CmpEqNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpEqNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpEqNull
    """
    #  void QQmlJSCodeGenerator::generate_CmpEqNull()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_CmpEqNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_CmpEqNullEv'
    self.uglySide.call(ritual)

  def generate_CmpNeNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpNeNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpNeNull
    """
    #  void QQmlJSCodeGenerator::generate_CmpNeNull()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_CmpNeNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_CmpNeNullEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CmpEqInt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpEqInt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpEqInt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpEqInt(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_CmpEqIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_CmpEqIntEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpNeInt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpNeInt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpNeInt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpNeInt(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_CmpNeIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_CmpNeIntEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpEq(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpEq(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpEq

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpEq(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpEqEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpEqEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpNe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpNe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpNe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpNe(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpNeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpNeEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpGt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpGt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpGt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpGt(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpGtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpGtEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpGe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpGe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpGe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpGe(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpGeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpGeEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpLt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpLt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpLt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpLt(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpLtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpLtEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpLe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpLe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpLe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpLe(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpLeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpLeEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpStrictEqual(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpStrictEqual(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpStrictEqual

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpStrictEqual(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator23generate_CmpStrictEqualEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator23generate_CmpStrictEqualEi')
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpStrictNotEqual(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpStrictNotEqual(int
    lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpStrictNotEqual(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_CmpStrictNotEqualEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_CmpStrictNotEqualEi')
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpIn(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpIn(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpIn

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpIn(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_CmpInEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpInEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpInstanceOf(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_CmpInstanceOf(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_CmpInstanceOf

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_CmpInstanceOf(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator22generate_CmpInstanceOfEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator22generate_CmpInstanceOfEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_As(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_As(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_As

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_As(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator11generate_AsEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator11generate_AsEi'
    self.uglySide.call(ritual, lhs)

  def generate_UNot(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UNot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UNot
    """
    #  void QQmlJSCodeGenerator::generate_UNot()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator13generate_UNotEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator13generate_UNotEv'
    self.uglySide.call(ritual)

  def generate_UPlus(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UPlus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UPlus
    """
    #  void QQmlJSCodeGenerator::generate_UPlus()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_UPlusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_UPlusEv'
    self.uglySide.call(ritual)

  def generate_UMinus(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UMinus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UMinus
    """
    #  void QQmlJSCodeGenerator::generate_UMinus()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator15generate_UMinusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator15generate_UMinusEv'
    self.uglySide.call(ritual)

  def generate_UCompl(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UCompl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UCompl
    """
    #  void QQmlJSCodeGenerator::generate_UCompl()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator15generate_UComplEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator15generate_UComplEv'
    self.uglySide.call(ritual)

  def generate_Increment(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Increment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Increment
    """
    #  void QQmlJSCodeGenerator::generate_Increment()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_IncrementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_IncrementEv'
    self.uglySide.call(ritual)

  def generate_Decrement(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Decrement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Decrement
    """
    #  void QQmlJSCodeGenerator::generate_Decrement()
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_DecrementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_DecrementEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Add(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Add(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Add

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Add(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_AddEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_AddEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitAnd(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_BitAnd(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_BitAnd

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_BitAnd(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator15generate_BitAndEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator15generate_BitAndEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitOr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_BitOr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_BitOr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_BitOr(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator14generate_BitOrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator14generate_BitOrEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitXor(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_BitXor(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_BitXor

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_BitXor(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator15generate_BitXorEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator15generate_BitXorEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_UShr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UShr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UShr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_UShr(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator13generate_UShrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator13generate_UShrEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Shr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Shr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Shr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Shr(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_ShrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_ShrEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Shl(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Shl(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Shl

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Shl(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_ShlEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_ShlEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitAndConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_BitAndConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_BitAndConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_BitAndConst(int rhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_BitAndConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_BitAndConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_BitOrConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_BitOrConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_BitOrConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_BitOrConst(int rhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator19generate_BitOrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator19generate_BitOrConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_BitXorConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_BitXorConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_BitXorConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_BitXorConst(int rhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator20generate_BitXorConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator20generate_BitXorConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_UShrConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_UShrConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_UShrConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_UShrConst(int rhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator18generate_UShrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator18generate_UShrConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_ShrConst(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ShrConst(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_ShrConst

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_ShrConst(int value)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_ShrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_ShrConstEi'
    self.uglySide.call(ritual, value)

  @overload(int)
  def generate_ShlConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ShlConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_ShlConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_ShlConst(int rhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator17generate_ShlConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator17generate_ShlConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_Exp(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Exp(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Exp

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Exp(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_ExpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_ExpEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Mul(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Mul(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Mul

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Mul(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_MulEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_MulEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Div(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Div(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Div

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Div(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_DivEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_DivEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Mod(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Mod(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Mod

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Mod(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_ModEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_ModEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Sub(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_Sub(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_Sub

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_Sub(int lhs)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator12generate_SubEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSCodeGenerator12generate_SubEi'
    self.uglySide.call(ritual, lhs)

  @overload(int, int)
  def generate_InitializeBlockDeadTemporalZone(
      self,
      firstReg: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(int
    firstReg, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    firstReg : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(int
    #      firstReg, int count)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator40generate_InitializeBlockDeadTempor'
        'alZoneEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator40generate_InitializeBlockDead'
          'TemporalZoneEii')
    self.uglySide.call(ritual, firstReg, count)

  def generate_ThrowOnNullOrUndefined(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined()
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator31generate_ThrowOnNullOrUndefinedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator31generate_ThrowOnNullOrUndefi'
          'nedEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_GetTemplateObject(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_GetTemplateObject(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_GetTemplateObject(int index)
    ritual = 'ritual_ZN19QQmlJSCodeGenerator26generate_GetTemplateObjectEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator26generate_GetTemplateObjectEi')
    self.uglySide.call(ritual, index)

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, a0: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::endInstruction(QV4::Moth::Instr::Type a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#endInstruction

    Parameters
    ----------

    a0 : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QQmlJSCodeGenerator::endInstruction(QV4::Moth::Instr::Type a0)
    ritual = (
        'ritual_ZN19QQmlJSCodeGenerator14endInstructionEN3QV44Moth5Instr4Ty'
        'peE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSCodeGenerator14endInstructionEN3QV44Moth5In'
          'str4TypeE')
    self.uglySide.call(ritual, a0.value)

  @overload(str)
  def addInclude(self, include: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::addInclude(const QString
    &include)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#addInclude

    Parameters
    ----------

    include : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::addInclude(const QString &include)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator10addIncludeERK7QString', include,
    )

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent, str)
  def conversion(
      self,
      from_: QQmlJSRegisterContent,
      to: QQmlJSRegisterContent,
      variable: str,
  ) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::conversion(QQmlJSRegisterContent
    from, QQmlJSRegisterContent to, const QString &variable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#conversion

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    to : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    variable : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::conversion(QQmlJSRegisterContent from,
    #      QQmlJSRegisterContent to, const QString &variable)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator10conversionE21QQmlJSRegisterContent'
        'S0_RK7QString',
        self._valueOf(from_), self._valueOf(to), variable,
    )

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent, str)
  def convertContained(
      self,
      from_: QQmlJSRegisterContent,
      to: QQmlJSRegisterContent,
      variable: str,
  ) -> str:
    """
    Calls Qt's 'QString
    QQmlJSCodeGenerator::convertContained(QQmlJSRegisterContent from,
    QQmlJSRegisterContent to, const QString &variable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#convertContained

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    to : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    variable : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::convertContained(QQmlJSRegisterContent
    #      from, QQmlJSRegisterContent to, const QString &variable)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator16convertContainedE21QQmlJSRegisterC'
        'ontentS0_RK7QString',
        self._valueOf(from_), self._valueOf(to), variable,
    )

  def generateReturnError(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateReturnError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateReturnError
    """
    #  void QQmlJSCodeGenerator::generateReturnError()
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator19generateReturnErrorEv',
    )

  @overload(str)
  def reject(self, thing: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::reject(const QString &thing)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscodegenerator.html#reject

    Parameters
    ----------

    thing : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::reject(const QString &thing)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator6rejectERK7QString', thing,
    )

  @overload(str)
  def skip(self, thing: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::skip(const QString &thing)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljscodegenerator.html#skip

    Parameters
    ----------

    thing : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::skip(const QString &thing)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator4skipERK7QString', thing,
    )

  @overload(QQmlJSRegisterContent, str)
  def contentPointer(self, content: QQmlJSRegisterContent, var: str) -> str:
    """
    Calls Qt's 'QString
    QQmlJSCodeGenerator::contentPointer(QQmlJSRegisterContent content, const
    QString &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#contentPointer

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    var : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::contentPointer(QQmlJSRegisterContent
    #      content, const QString &var)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator14contentPointerE21QQmlJSRegisterCon'
        'tentRK7QString',
        self._valueOf(content), var,
    )

  @overload(QQmlJSRegisterContent, str)
  def contentType(self, content: QQmlJSRegisterContent, var: str) -> str:
    """
    Calls Qt's 'QString
    QQmlJSCodeGenerator::contentType(QQmlJSRegisterContent content, const
    QString &var)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#contentType

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    var : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::contentType(QQmlJSRegisterContent
    #      content, const QString &var)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator11contentTypeE21QQmlJSRegisterConten'
        'tRK7QString',
        self._valueOf(content), var,
    )

  def generateSetInstructionPointer(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateSetInstructionPointer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html
    """
    #  void QQmlJSCodeGenerator::generateSetInstructionPointer()
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator29generateSetInstructionPointerEv',
    )

  @overload(str, str)
  @overload(str, str, str)
  def generateLookup(
      self,
      lookup: str,
      initialization: str,
      resultPreparation: str = '',
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateLookup(const QString
    &lookup, const QString &initialization, const QString
    &resultPreparation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateLookup

    Parameters
    ----------

    lookup : str
      Passed on as it is: a QString is made of it for the call.

    initialization : str
      Passed on as it is: a QString is made of it for the call.

    resultPreparation : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QQmlJSCodeGenerator::generateLookup(const QString &lookup, const
    #      QString &initialization, const QString &resultPreparation)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator14generateLookupERK7QStringS2_S2_',
        lookup, initialization, resultPreparation,
    )

  @overload(QQmlJSRegisterContent, str, int)
  def getLookupPreparation(
      self,
      content: QQmlJSRegisterContent,
      var: str,
      lookup: int,
  ) -> str:
    """
    Calls Qt's 'QString
    QQmlJSCodeGenerator::getLookupPreparation(QQmlJSRegisterContent content,
    const QString &var, int lookup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#getLookupPreparation

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    var : str
      Passed on as it is: a QString is made of it for the call.

    lookup : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QQmlJSCodeGenerator::getLookupPreparation(QQmlJSRegisterContent
    #      content, const QString &var, int lookup)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator20getLookupPreparationE21QQmlJSRegis'
        'terContentRK7QStringi',
        self._valueOf(content), var, lookup,
    )

  @overload(int)
  def generateEnumLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateEnumLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateEnumLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateEnumLookup(int index)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator18generateEnumLookupEi', index,
    )

  def resetState(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::resetState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#resetState
    """
    #  void QQmlJSCodeGenerator::resetState()
    self.uglySide.call('ritual_ZN19QQmlJSCodeGenerator10resetStateEv')

  def generateExceptionCheck(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateExceptionCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateExceptionCheck
    """
    #  void QQmlJSCodeGenerator::generateExceptionCheck()
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator22generateExceptionCheckEv',
    )

  @overload(QQmlJSRegisterContent, str, str, bool)
  def generateEqualityOperation(
      self,
      lhsContent: QQmlJSRegisterContent,
      lhsName: str,
      function: str,
      invert: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generateEqualityOperation(QQmlJSRegisterContent
    lhsContent, const QString &lhsName, const QString &function, bool
    invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateEqualityOperation

    Parameters
    ----------

    lhsContent : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    lhsName : str
      Passed on as it is: a QString is made of it for the call.

    function : str
      Passed on as it is: a QString is made of it for the call.

    invert : bool
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateEqualityOperation(
    #      QQmlJSRegisterContent lhsContent, const QString &lhsName, const
    #      QString &function, bool invert)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator25generateEqualityOperationE21QQmlJS'
        'RegisterContentRK7QStringS3_b',
        self._valueOf(lhsContent), lhsName, function, invert,
    )

  @overload(
      QQmlJSRegisterContent, QQmlJSRegisterContent, str, str, str, bool,
  )
  def generateEqualityOperation(
      self,
      lhsContent: QQmlJSRegisterContent,
      rhsContent: QQmlJSRegisterContent,
      lhsName: str,
      rhsName: str,
      function: str,
      invert: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generateEqualityOperation(QQmlJSRegisterContent
    lhsContent, QQmlJSRegisterContent rhsContent, const QString &lhsName,
    const QString &rhsName, const QString &function, bool invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateEqualityOperation

    Parameters
    ----------

    lhsContent : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    rhsContent : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    lhsName : str
      Passed on as it is: a QString is made of it for the call.

    rhsName : str
      Passed on as it is: a QString is made of it for the call.

    function : str
      Passed on as it is: a QString is made of it for the call.

    invert : bool
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateEqualityOperation(
    #      QQmlJSRegisterContent lhsContent, QQmlJSRegisterContent
    #      rhsContent, const QString &lhsName, const QString &rhsName, const
    #      QString &function, bool invert)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator25generateEqualityOperationE21QQmlJS'
        'RegisterContentS0_RK7QStringS3_S3_b',
        self._valueOf(lhsContent), self._valueOf(rhsContent), lhsName,
        rhsName, function, invert,
    )

  @overload(int, str)
  def generateCompareOperation(self, lhs: int, cppOperator: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateCompareOperation(int lhs,
    const QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateCompareOperation

    Parameters
    ----------

    lhs : int
      Passed on as it is.

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateCompareOperation(int lhs, const
    #      QString &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator24generateCompareOperationEiRK7QStri'
        'ng',
        lhs, cppOperator,
    )

  @overload(int, str)
  def generateArithmeticOperation(self, lhs: int, cppOperator: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateArithmeticOperation(int
    lhs, const QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    lhs : int
      Passed on as it is.

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateArithmeticOperation(int lhs, const
    #      QString &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator27generateArithmeticOperationEiRK7QS'
        'tring',
        lhs, cppOperator,
    )

  @overload(str, str, str)
  def generateArithmeticOperation(
      self,
      lhs: str,
      rhs: str,
      cppOperator: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateArithmeticOperation(const
    QString &lhs, const QString &rhs, const QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    lhs : str
      Passed on as it is: a QString is made of it for the call.

    rhs : str
      Passed on as it is: a QString is made of it for the call.

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateArithmeticOperation(const QString
    #      &lhs, const QString &rhs, const QString &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator27generateArithmeticOperationERK7QSt'
        'ringS2_S2_',
        lhs, rhs, cppOperator,
    )

  @overload(int, str)
  def generateShiftOperation(self, lhs: int, cppOperator: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateShiftOperation(int lhs,
    const QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateShiftOperation

    Parameters
    ----------

    lhs : int
      Passed on as it is.

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateShiftOperation(int lhs, const
    #      QString &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator22generateShiftOperationEiRK7QString',
        lhs, cppOperator,
    )

  @overload(int, str)
  def generateArithmeticConstOperation(
      self,
      lhsConst: int,
      cppOperator: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generateArithmeticConstOperation(int lhsConst, const
    QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    lhsConst : int
      Passed on as it is.

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateArithmeticConstOperation(int
    #      lhsConst, const QString &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator32generateArithmeticConstOperationEi'
        'RK7QString',
        lhsConst, cppOperator,
    )

  @overload(int)
  def generateJumpCodeWithTypeConversions(self, relativeOffset: int) -> None:
    """
    Calls Qt's 'void
    QQmlJSCodeGenerator::generateJumpCodeWithTypeConversions(int
    relativeOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    relativeOffset : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateJumpCodeWithTypeConversions(int
    #      relativeOffset)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator35generateJumpCodeWithTypeConversion'
        'sEi',
        relativeOffset,
    )

  @overload(str)
  def generateUnaryOperation(self, cppOperator: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateUnaryOperation(const
    QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateUnaryOperation

    Parameters
    ----------

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateUnaryOperation(const QString
    #      &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator22generateUnaryOperationERK7QString',
        cppOperator,
    )

  @overload(str)
  def generateInPlaceOperation(self, cppOperator: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateInPlaceOperation(const
    QString &cppOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateInPlaceOperation

    Parameters
    ----------

    cppOperator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateInPlaceOperation(const QString
    #      &cppOperator)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator24generateInPlaceOperationERK7QStrin'
        'g',
        cppOperator,
    )

  @overload(str)
  def generateMoveOutVarAfterCall(self, outVar: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateMoveOutVarAfterCall(const
    QString &outVar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    outVar : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::generateMoveOutVarAfterCall(const QString
    #      &outVar)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator27generateMoveOutVarAfterCallERK7QSt'
        'ring',
        outVar,
    )

  @overload(int)
  def generateTypeLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateTypeLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateTypeLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateTypeLookup(int index)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator18generateTypeLookupEi', index,
    )

  @overload(QQmlJSRegisterContent, str, bool)
  def generateVariantEqualityComparison(
      self,
      nonStorable: QQmlJSRegisterContent,
      registerName: str,
      invert: bool,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateVariantEqualityComparison(
    QQmlJSRegisterContent nonStorable, const QString &registerName, bool
    invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    nonStorable : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    registerName : str
      Passed on as it is: a QString is made of it for the call.

    invert : bool
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateVariantEqualityComparison(
    #      QQmlJSRegisterContent nonStorable, const QString &registerName,
    #      bool invert)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator33generateVariantEqualityComparisonE'
        '21QQmlJSRegisterContentRK7QStringb',
        self._valueOf(nonStorable), registerName, invert,
    )

  @overload(QQmlJSRegisterContent, str, str, bool)
  def generateVariantEqualityComparison(
      self,
      storableContent: QQmlJSRegisterContent,
      typedRegisterName: str,
      varRegisterName: str,
      invert: bool,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateVariantEqualityComparison(
    QQmlJSRegisterContent storableContent, const QString &typedRegisterName,
    const QString &varRegisterName, bool invert)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    storableContent : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    typedRegisterName : str
      Passed on as it is: a QString is made of it for the call.

    varRegisterName : str
      Passed on as it is: a QString is made of it for the call.

    invert : bool
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateVariantEqualityComparison(
    #      QQmlJSRegisterContent storableContent, const QString
    #      &typedRegisterName, const QString &varRegisterName, bool invert)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator33generateVariantEqualityComparisonE'
        '21QQmlJSRegisterContentRK7QStringS3_b',
        self._valueOf(storableContent), typedRegisterName, varRegisterName,
        invert,
    )

  @overload(int, int)
  def generateArrayInitializer(self, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateArrayInitializer(int argc,
    int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateArrayInitializer

    Parameters
    ----------

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateArrayInitializer(int argc, int argv)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator24generateArrayInitializerEii',
        argc, argv,
    )

  @overload(int)
  def generateWriteBack(self, registerIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generateWriteBack(int
    registerIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateWriteBack

    Parameters
    ----------

    registerIndex : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generateWriteBack(int registerIndex)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator17generateWriteBackEi', registerIndex,
    )

  @overload(str)
  def rejectIfNonQObjectOut(self, error: str) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::rejectIfNonQObjectOut(const QString
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#rejectIfNonQObjectOut

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSCodeGenerator::rejectIfNonQObjectOut(const QString &error)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator21rejectIfNonQObjectOutERK7QString',
        error,
    )

  def rejectIfBadArray(self) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::rejectIfBadArray()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#rejectIfBadArray
    """
    #  void QQmlJSCodeGenerator::rejectIfBadArray()
    self.uglySide.call('ritual_ZN19QQmlJSCodeGenerator16rejectIfBadArrayEv')

  @overload(int, int, str, str, QString)
  @overload(int, int, str, str, NoneType)
  def initAndCall(
      self,
      argc: int,
      argv: int,
      callMethodTemplate: str,
      initMethodTemplate: str,
      outVar: Optional[QString],
  ) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::initAndCall(int argc, int argv,
    const QString &callMethodTemplate, const QString &initMethodTemplate,
    QString *outVar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#initAndCall

    Parameters
    ----------

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.

    callMethodTemplate : str
      Passed on as it is: a QString is made of it for the call.

    initMethodTemplate : str
      Passed on as it is: a QString is made of it for the call.

    outVar : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::initAndCall(int argc, int argv, const
    #      QString &callMethodTemplate, const QString &initMethodTemplate,
    #      QString *outVar)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator11initAndCallEiiRK7QStringS2_PS0_',
        argc, argv, callMethodTemplate, initMethodTemplate,
        self._addressOf(outVar),
    )

  @overload(str, int, int, int)
  def inlineStringMethod(
      self,
      name: str,
      base: int,
      argc: int,
      argv: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::inlineStringMethod(const QString
    &name, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#inlineStringMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::inlineStringMethod(const QString &name, int
    #      base, int argc, int argv)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator18inlineStringMethodERK7QStringiii',
        name, base, argc, argv,
    )

  @overload(str, int, int)
  def inlineTranslateMethod(self, name: str, argc: int, argv: int) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::inlineTranslateMethod(const QString
    &name, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#inlineTranslateMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::inlineTranslateMethod(const QString &name,
    #      int argc, int argv)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator21inlineTranslateMethodERK7QStringii',
        name, argc, argv,
    )

  @overload(str, int, int)
  def inlineMathMethod(self, name: str, argc: int, argv: int) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::inlineMathMethod(const QString
    &name, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#inlineMathMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::inlineMathMethod(const QString &name, int
    #      argc, int argv)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator16inlineMathMethodERK7QStringii',
        name, argc, argv,
    )

  @overload(str, int, int)
  def inlineConsoleMethod(self, name: str, argc: int, argv: int) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::inlineConsoleMethod(const QString
    &name, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#inlineConsoleMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::inlineConsoleMethod(const QString &name, int
    #      argc, int argv)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator19inlineConsoleMethodERK7QStringii',
        name, argc, argv,
    )

  @overload(str, int, int, int)
  def inlineArrayMethod(
      self,
      name: str,
      base: int,
      argc: int,
      argv: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::inlineArrayMethod(const QString
    &name, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#inlineArrayMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::inlineArrayMethod(const QString &name, int
    #      base, int argc, int argv)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator17inlineArrayMethodERK7QStringiii',
        name, base, argc, argv,
    )

  @overload(int)
  def generate_GetLookupHelper(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSCodeGenerator::generate_GetLookupHelper(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generate_GetLookupHelper

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSCodeGenerator::generate_GetLookupHelper(int index)
    self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator24generate_GetLookupHelperEi', index,
    )

  @overload(
      QQmlJSMetaMethod, QList[QQmlJSRegisterContent], QStringList, str, str,
  )
  def generateCallConstructor(
      self,
      ctor: QQmlJSMetaMethod,
      argumentTypes: QList[QQmlJSRegisterContent],
      arguments: QStringList,
      metaType: str,
      metaObject: str,
  ) -> str:
    """
    Calls Qt's 'QString QQmlJSCodeGenerator::generateCallConstructor(const
    QQmlJSMetaMethod &ctor, const QList<QQmlJSRegisterContent>
    &argumentTypes, const QStringList &arguments, const QString &metaType,
    const QString &metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#generateCallConstructor

    Parameters
    ----------

    ctor : QQmlJSMetaMethod
      Passed on as a value: Qt reads the C++ QQmlJSMetaMethod, which stays
      Python's own.

    argumentTypes : QList[QQmlJSRegisterContent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    arguments : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    metaType : str
      Passed on as it is: a QString is made of it for the call.

    metaObject : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::generateCallConstructor(const
    #      QQmlJSMetaMethod &ctor, const QList<QQmlJSRegisterContent>
    #      &argumentTypes, const QStringList &arguments, const QString
    #      &metaType, const QString &metaObject)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator23generateCallConstructorERK16QQmlJS'
        'MetaMethodRK5QListI21QQmlJSRegisterContentERKS3_I7QStringERKS8_SD_',
        self._valueOf(ctor), self._valueOf(argumentTypes),
        self._valueOf(arguments), metaType, metaObject,
    )

  @overload(str, int)
  def generateVariantMapGetLookup(self, map: str, nameIndex: int) -> str:
    """
    Calls Qt's 'QString
    QQmlJSCodeGenerator::generateVariantMapGetLookup(const QString &map,
    const int nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    map : str
      Passed on as it is: a QString is made of it for the call.

    nameIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSCodeGenerator::generateVariantMapGetLookup(const QString
    #      &map, const int nameIndex)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator27generateVariantMapGetLookupERK7QSt'
        'ringi',
        map, nameIndex,
    )

  @overload(QQmlJSRegisterContent)
  def originalType(
      self,
      tracked: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSCodeGenerator::originalType(QQmlJSRegisterContent tracked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html#originalType

    Parameters
    ----------

    tracked : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSCodeGenerator::originalType(QQmlJSRegisterContent tracked)
    address = self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator12originalTypeE21QQmlJSRegisterConte'
        'nt',
        self._valueOf(tracked),
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(int)
  def isRegisterAffectedBySideEffects(self, registerIndex: int) -> bool:
    """
    Calls Qt's 'bool QQmlJSCodeGenerator::isRegisterAffectedBySideEffects(int
    registerIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljscodegenerator.html

    Parameters
    ----------

    registerIndex : int
      Passed on as it is.
    """
    #  bool QQmlJSCodeGenerator::isRegisterAffectedBySideEffects(int
    #      registerIndex)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSCodeGenerator31isRegisterAffectedBySideEffectsEi',
        registerIndex,
    )

  @staticmethod
  def castTargetName(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::castTargetName(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.castTargetName' has no cute function yet. "
        "Qt's 'QString QQmlJSCodeGenerator::castTargetName(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def convertStored(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::convertStored(const
    QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to, const
    QString &variable)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.convertStored' has no cute function yet. Qt's "
        "'QString QQmlJSCodeGenerator::convertStored(const "
        "QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to, "
        "const QString &variable)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def generateContentPointerCheck(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSCodeGenerator::generateContentPointerCheck(const
    QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
    QString &variable, const QString &errorMessage)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.generateContentPointerCheck' has no cute "
        "function yet. Qt's 'bool "
        "QQmlJSCodeGenerator::generateContentPointerCheck(const "
        "QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, "
        "const QString &variable, const QString &errorMessage)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def generateVariantMapSetLookup(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::generateVariantMapSetLookup(const
    QString &map, const int nameIndex, const QQmlJSScope::ConstPtr &property,
    const QString &variableIn)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.generateVariantMapSetLookup' has no cute "
        "function yet. Qt's 'QString "
        "QQmlJSCodeGenerator::generateVariantMapSetLookup(const QString "
        "&map, const int nameIndex, const QQmlJSScope::ConstPtr &property, "
        "const QString &variableIn)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def literalType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSCodeGenerator::literalType(const
    QQmlJSScope::ConstPtr &contained)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.literalType' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent QQmlJSCodeGenerator::literalType(const "
        "QQmlJSScope::ConstPtr &contained)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def lookupSignatures(*__, **_) -> Never:
    """
    Qt's 'LookupSignatures QQmlJSCodeGenerator::lookupSignatures() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.lookupSignatures' has no cute function yet. "
        "Qt's 'LookupSignatures QQmlJSCodeGenerator::lookupSignatures() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def metaObject(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::metaObject(const QQmlJSScope::ConstPtr
    &objectType)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.metaObject' has no cute function yet. Qt's "
        "'QString QQmlJSCodeGenerator::metaObject(const "
        "QQmlJSScope::ConstPtr &objectType)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def metaType(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::metaType(const QQmlJSScope::ConstPtr
    &type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.metaType' has no cute function yet. Qt's "
        "'QString QQmlJSCodeGenerator::metaType(const QQmlJSScope::ConstPtr "
        "&type)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def metaTypeFromName(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::metaTypeFromName(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.metaTypeFromName' has no cute function yet. "
        "Qt's 'QString QQmlJSCodeGenerator::metaTypeFromName(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def metaTypeFromType(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::metaTypeFromType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.metaTypeFromType' has no cute function yet. "
        "Qt's 'QString QQmlJSCodeGenerator::metaTypeFromType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def recordEnumKeyLookup(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSCodeGenerator::recordEnumKeyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const
    QString &keyName)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.recordEnumKeyLookup' has no cute function "
        "yet. Qt's 'void QQmlJSCodeGenerator::recordEnumKeyLookup(const "
        "QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const "
        "QString &keyName)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def recordMethodLookup(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSCodeGenerator::recordMethodLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.recordMethodLookup' has no cute function yet. "
        "Qt's 'void QQmlJSCodeGenerator::recordMethodLookup(const "
        "QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def recordPropertyLookup(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSCodeGenerator::recordPropertyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.recordPropertyLookup' has no cute function "
        "yet. Qt's 'void QQmlJSCodeGenerator::recordPropertyLookup(const "
        "QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def resolveQObjectPointer(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::resolveQObjectPointer(const
    QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
    QString &variable, const QString &errorMessage)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.resolveQObjectPointer' has no cute function "
        "yet. Qt's 'QString "
        "QQmlJSCodeGenerator::resolveQObjectPointer(const "
        "QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, "
        "const QString &variable, const QString &errorMessage)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def resolveValueTypeContentPointer(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSCodeGenerator::resolveValueTypeContentPointer(const
    QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
    QString &variable, const QString &errorMessage)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSCodeGenerator.resolveValueTypeContentPointer' has no cute "
        "function yet. Qt's 'QString "
        "QQmlJSCodeGenerator::resolveValueTypeContentPointer(const "
        "QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, "
        "const QString &variable, const QString &errorMessage)': takes a "
        "type Python has no way to hand over yet.")
