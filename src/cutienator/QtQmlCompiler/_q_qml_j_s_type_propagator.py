"""
QQmlJSTypePropagator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstypepropagator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSTypePropagator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QSOperator, QV4
from . import QQmlJSCompilePass, QQmlJSTypeResolver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSMetaMethod, QQmlJSRegisterContent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaMethod = WAIT['QQmlJSMetaMethod']
  QQmlJSRegisterContent = WAIT['QQmlJSRegisterContent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSTypePropagator(QQmlJSCompilePass):
  """
  The cute side of Qt's QQmlJSTypePropagator: a plain Python object standing
  in front of one C++ QQmlJSTypePropagator.

  It is built on the cute 'QQmlJSCompilePass', as Qt's QQmlJSTypePropagator
  is built on Qt's QQmlJSCompilePass, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSTypePropagator that has a ritual and that
  Python can call so far, 176 names in all: 'run', 'generate_Ret',
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
  'endInstruction', 'handleUnqualifiedAccess',
  'handleUnqualifiedAccessAndContextProperties',
  'handleImportNamespaceLookup', 'handleLookupError', 'checkForEnumProblems',
  'warnAboutTypeCoercion', 'checkConversion',
  'generateUnaryArithmeticOperation', 'propagateBinaryOperation',
  'generateBinaryArithmeticOperation',
  'generateBinaryConstArithmeticOperation', 'generate_StoreNameCommon',
  'propagateCall', 'propagateTranslationMethod_SAcheck',
  'propagateTranslationMethod', 'propagateStringArgCall',
  'propagateArrayMethod', 'propagatePropertyLookup',
  'propagateScopeLookupCall', 'saveRegisterStateForJump', 'canConvertFromTo',
  'registerName', 'checkedInputRegister', 'setAccumulator', 'setRegister',
  'mergeRegister', 'addReadRegister', 'addReadAccumulator',
  'populatesAccumulator', 'isNoop', 'recordEqualsNullType',
  'recordEqualsIntType', 'recordEqualsType', 'recordCompareType',
  'generate_CallProperty_SCMath', 'generate_CallProperty_SCconsole',
  'generate_Construct_SCDate', 'generate_Construct_SCArray',
  'isLoggingMethod', 'addError', 'setVarAccumulatorAndError'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Verdict
    QQmlJSTypePropagator::startInstruction(QV4::Moth::Instr::Type instr)':
    gives the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot
    be named here.
  - Qt's 'void QQmlJSTypePropagator::checkDeprecated(QQmlJSScope::ConstPtr
    scope, const QString &name, bool isMethod) const': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QQmlJSTypePropagator::isCallingProperty(QQmlJSScope::ConstPtr
    scope, const QString &name) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'PropertyResolution
    QQmlJSTypePropagator::propertyResolution(QQmlJSScope::ConstPtr scope,
    const QString &type) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool QQmlJSTypePropagator::canConvertFromTo(QQmlJSRegisterContent
    from, const QQmlJSScope::ConstPtr &to)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlJSMetaMethod QQmlJSTypePropagator::bestMatchForCall(const
    QList<QQmlJSMetaMethod> &methods, int argc, int argv, QStringList
    *errors)': names 'QStringList', which has no cute class yet.
  - Qt's 'void QQmlJSTypePropagator::addReadRegister(int index, const
    QQmlJSScope::ConstPtr &convertTo)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlJSTypePropagator::addReadAccumulator(const
    QQmlJSScope::ConstPtr &convertTo)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QQmlJSTypePropagator is created at the first use, not by
    'QQmlJSTypePropagator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSTypePropagator.
  - Each name of Qt's QQmlJSTypePropagator that has no cute function yet,
    'bestMatchForCall', 'checkDeprecated', 'isCallingProperty',
    'propertyResolution', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def isLoggingMethod(consoleMethod: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypePropagator::isLoggingMethod(const QString
    &consoleMethod)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#isLoggingMethod

    Parameters
    ----------

    consoleMethod : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSTypePropagator::isLoggingMethod(const QString
    #      &consoleMethod)
    return Rituals.call(
        'ritual_ZN20QQmlJSTypePropagator15isLoggingMethodERK7QString',
        consoleMethod,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSTypePropagator'

  #  A C++ QQmlJSTypePropagator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSTypePropagator'

  #  The functions Qt calls itself that QQmlJSTypePropagator is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'checkDeprecated': (
          'void '
          'QQmlJSTypePropagator::checkDeprecated(QQmlJSScope::ConstPtr, '
          'const QString &, bool) const',
      ),
      'isCallingProperty': (
          'bool '
          'QQmlJSTypePropagator::isCallingProperty(QQmlJSScope::ConstPtr, '
          'const QString &) const',
      ),
      'propagateCall': (
          'void QQmlJSTypePropagator::propagateCall(const '
          'QList<QQmlJSMetaMethod> &, int, int, QQmlJSRegisterContent)',
      ),
  }

  #  The functions Qt calls itself that QQmlJSTypePropagator is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'handleUnqualifiedAccess': (
          ('_ZNK20QQmlJSTypePropagator23handleUnqualifiedAccessERK7QStringb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'handleUnqualifiedAccessAndContextProperties': (
          ('_ZNK20QQmlJSTypePropagator43handleUnqualifiedAccessAndContextPr'
           'opertiesERK7QStringb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'handleImportNamespaceLookup': (
          ('_ZN20QQmlJSTypePropagator27handleImportNamespaceLookupERK7QStri'
           'ng',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'handleLookupError': (
          ('_ZN20QQmlJSTypePropagator17handleLookupErrorERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'checkForEnumProblems': (
          ('_ZN20QQmlJSTypePropagator20checkForEnumProblemsE21QQmlJSRegiste'
           'rContentRK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtQmlCompiler:QQmlJSRegisterContent'),
               ('address', 'text', ''),
           )),
      ),
      'warnAboutTypeCoercion': (
          ('_ZN20QQmlJSTypePropagator21warnAboutTypeCoercionEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreNameCommon': (
          ('_ZN20QQmlJSTypePropagator24generate_StoreNameCommonEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'propagateTranslationMethod_SAcheck': (
          ('_ZN20QQmlJSTypePropagator34propagateTranslationMethod_SAcheckER'
           'K7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'propagatePropertyLookup': (
          ('_ZN20QQmlJSTypePropagator23propagatePropertyLookupERK7QStringi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def registerName(self, registerIndex: int) -> str:
    """
    Calls Qt's 'QString QQmlJSTypePropagator::registerName(int registerIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#registerName

    Parameters
    ----------

    registerIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSTypePropagator::registerName(int registerIndex) const
    return self.uglySide.call(
        'ritual_ZNK20QQmlJSTypePropagator12registerNameEi', registerIndex,
    )

  @overload(QV4.Moth.Instr.Type)
  def populatesAccumulator(self, instr: QV4.Moth.Instr.Type) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypePropagator::populatesAccumulator(QV4::Moth::Instr::Type instr)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#populatesAccumulator

    Parameters
    ----------

    instr : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  bool QQmlJSTypePropagator::populatesAccumulator(QV4::Moth::Instr::Type
    #      instr) const
    return self.uglySide.call(
        'ritual_ZNK20QQmlJSTypePropagator20populatesAccumulatorEN3QV44Moth5'
        'Instr4TypeE',
        instr.value,
    )

  @overload(QV4.Moth.Instr.Type)
  def isNoop(self, instr: QV4.Moth.Instr.Type) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypePropagator::isNoop(QV4::Moth::Instr::Type
    instr) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstypepropagator.html#isNoop

    Parameters
    ----------

    instr : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  bool QQmlJSTypePropagator::isNoop(QV4::Moth::Instr::Type instr) const
    return self.uglySide.call(
        'ritual_ZNK20QQmlJSTypePropagator6isNoopEN3QV44Moth5Instr4TypeE',
        instr.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlJSRegisterContent)
  def setAccumulator(self, content: QQmlJSRegisterContent) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::setAccumulator(QQmlJSRegisterContent content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#setAccumulator

    Parameters
    ----------

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypePropagator::setAccumulator(QQmlJSRegisterContent
    #      content)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator14setAccumulatorE21QQmlJSRegisterCo'
        'ntent',
        self._valueOf(content),
    )

  @overload(int, QQmlJSRegisterContent)
  def setRegister(self, index: int, content: QQmlJSRegisterContent) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::setRegister(int index,
    QQmlJSRegisterContent content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#setRegister

    Parameters
    ----------

    index : int
      Passed on as it is.

    content : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypePropagator::setRegister(int index,
    #      QQmlJSRegisterContent content)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator11setRegisterEi21QQmlJSRegisterCont'
        'ent',
        index, self._valueOf(content),
    )

  def setVarAccumulatorAndError(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::setVarAccumulatorAndError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::setVarAccumulatorAndError()
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator25setVarAccumulatorAndErrorEv',
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

  @overload(QQmlJSCompilePass.Function)
  @overload(NoneType)
  def run(
      self,
      m_function: Optional[QQmlJSCompilePass.Function],
  ) -> QQmlJSCompilePass.BlocksAndAnnotations:
    """
    Calls Qt's 'BlocksAndAnnotations QQmlJSTypePropagator::run(const Function
    *m_function)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstypepropagator.html#run

    Parameters
    ----------

    m_function : Optional[QQmlJSCompilePass.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlJSCompilePass.BlocksAndAnnotations
      A new cute QQmlJSCompilePass::BlocksAndAnnotations around the copy Qt
      gave back. Python owns it.
    """
    #  BlocksAndAnnotations QQmlJSTypePropagator::run(const Function
    #      *m_function)
    address = self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator3runEPKN17QQmlJSCompilePass8Functio'
        'nE',
        self._addressOf(m_function),
    )
    return QQmlJSCompilePass.BlocksAndAnnotations._cuteOwning(address)

  def generate_Ret(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Ret()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Ret
    """
    #  void QQmlJSTypePropagator::generate_Ret()
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_RetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_RetEv'
    self.uglySide.call(ritual)

  def generate_Debug(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Debug()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Debug
    """
    #  void QQmlJSTypePropagator::generate_Debug()
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_DebugEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_DebugEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_LoadConst(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadConst(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadConst

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadConst(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_LoadConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_LoadConstEi'
    self.uglySide.call(ritual, index)

  def generate_LoadZero(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadZero()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadZero
    """
    #  void QQmlJSTypePropagator::generate_LoadZero()
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_LoadZeroEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_LoadZeroEv'
    self.uglySide.call(ritual)

  def generate_LoadTrue(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadTrue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadTrue
    """
    #  void QQmlJSTypePropagator::generate_LoadTrue()
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_LoadTrueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_LoadTrueEv'
    self.uglySide.call(ritual)

  def generate_LoadFalse(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadFalse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadFalse
    """
    #  void QQmlJSTypePropagator::generate_LoadFalse()
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_LoadFalseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_LoadFalseEv'
    self.uglySide.call(ritual)

  def generate_LoadNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadNull
    """
    #  void QQmlJSTypePropagator::generate_LoadNull()
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_LoadNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_LoadNullEv'
    self.uglySide.call(ritual)

  def generate_LoadUndefined(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadUndefined
    """
    #  void QQmlJSTypePropagator::generate_LoadUndefined()
    ritual = 'ritual_ZN20QQmlJSTypePropagator22generate_LoadUndefinedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator22generate_LoadUndefinedEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_LoadInt(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadInt(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadInt

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadInt(int value)
    ritual = 'ritual_ZN20QQmlJSTypePropagator16generate_LoadIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator16generate_LoadIntEi'
    self.uglySide.call(ritual, value)

  @overload(int, int)
  def generate_MoveConst(self, constIndex: int, destTemp: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_MoveConst(int constIndex,
    int destTemp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_MoveConst

    Parameters
    ----------

    constIndex : int
      Passed on as it is.

    destTemp : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_MoveConst(int constIndex, int
    #      destTemp)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_MoveConstEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_MoveConstEii'
    self.uglySide.call(ritual, constIndex, destTemp)

  @overload(int)
  def generate_LoadReg(self, reg: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadReg(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadReg

    Parameters
    ----------

    reg : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadReg(int reg)
    ritual = 'ritual_ZN20QQmlJSTypePropagator16generate_LoadRegEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator16generate_LoadRegEi'
    self.uglySide.call(ritual, reg)

  @overload(int)
  def generate_StoreReg(self, reg: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreReg(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreReg

    Parameters
    ----------

    reg : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreReg(int reg)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_StoreRegEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_StoreRegEi'
    self.uglySide.call(ritual, reg)

  @overload(int, int)
  def generate_MoveReg(self, srcReg: int, destReg: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_MoveReg(int srcReg, int
    destReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_MoveReg

    Parameters
    ----------

    srcReg : int
      Passed on as it is.

    destReg : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_MoveReg(int srcReg, int destReg)
    ritual = 'ritual_ZN20QQmlJSTypePropagator16generate_MoveRegEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator16generate_MoveRegEii'
    self.uglySide.call(ritual, srcReg, destReg)

  @overload(int)
  def generate_LoadImport(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadImport(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadImport

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadImport(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_LoadImportEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_LoadImportEi'
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_LoadLocal(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadLocal(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadLocal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadLocal(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_LoadLocalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_LoadLocalEi'
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_StoreLocal(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreLocal(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreLocal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreLocal(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_StoreLocalEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_StoreLocalEi'
    self.uglySide.call(ritual, index)

  @overload(int, int)
  def generate_LoadScopedLocal(self, scope: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadScopedLocal(int
    scope, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadScopedLocal

    Parameters
    ----------

    scope : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadScopedLocal(int scope, int
    #      index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator24generate_LoadScopedLocalEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator24generate_LoadScopedLocalEii')
    self.uglySide.call(ritual, scope, index)

  @overload(int, int)
  def generate_StoreScopedLocal(self, scope: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreScopedLocal(int
    scope, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    scope : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreScopedLocal(int scope, int
    #      index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_StoreScopedLocalEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_StoreScopedLocalEi'
          'i')
    self.uglySide.call(ritual, scope, index)

  @overload(int)
  def generate_LoadRuntimeString(self, stringId: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadRuntimeString(int
    stringId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    stringId : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadRuntimeString(int stringId)
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_LoadRuntimeStringEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_LoadRuntimeStringE'
          'i')
    self.uglySide.call(ritual, stringId)

  @overload(int, int)
  def generate_MoveRegExp(self, regExpId: int, destReg: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_MoveRegExp(int regExpId,
    int destReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_MoveRegExp

    Parameters
    ----------

    regExpId : int
      Passed on as it is.

    destReg : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_MoveRegExp(int regExpId, int
    #      destReg)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_MoveRegExpEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_MoveRegExpEii'
    self.uglySide.call(ritual, regExpId, destReg)

  @overload(int)
  def generate_LoadClosure(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadClosure(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadClosure

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadClosure(int value)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_LoadClosureEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_LoadClosureEi'
    self.uglySide.call(ritual, value)

  @overload(int)
  def generate_LoadName(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadName(int nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadName

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadName(int nameIndex)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_LoadNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_LoadNameEi'
    self.uglySide.call(ritual, nameIndex)

  @overload(int)
  def generate_LoadGlobalLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadGlobalLookup(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadGlobalLookup(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_LoadGlobalLookupEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_LoadGlobalLookupEi')
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_LoadQmlContextPropertyLookup(self, index: int) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(int
    #      index)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator37generate_LoadQmlContextPropertyLo'
        'okupEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator37generate_LoadQmlContextProp'
          'ertyLookupEi')
    self.uglySide.call(ritual, index)

  @overload(int)
  def generate_StoreNameSloppy(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreNameSloppy(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreNameSloppy

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreNameSloppy(int nameIndex)
    ritual = 'ritual_ZN20QQmlJSTypePropagator24generate_StoreNameSloppyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator24generate_StoreNameSloppyEi')
    self.uglySide.call(ritual, nameIndex)

  @overload(int)
  def generate_StoreNameStrict(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreNameStrict(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreNameStrict

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreNameStrict(int name)
    ritual = 'ritual_ZN20QQmlJSTypePropagator24generate_StoreNameStrictEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator24generate_StoreNameStrictEi')
    self.uglySide.call(ritual, name)

  @overload(int)
  def generate_LoadElement(self, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadElement(int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadElement

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadElement(int base)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_LoadElementEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_LoadElementEi'
    self.uglySide.call(ritual, base)

  @overload(int, int)
  def generate_StoreElement(self, base: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreElement(int base,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreElement

    Parameters
    ----------

    base : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreElement(int base, int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator21generate_StoreElementEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator21generate_StoreElementEii')
    self.uglySide.call(ritual, base, index)

  @overload(int)
  def generate_LoadProperty(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadProperty(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_LoadProperty

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadProperty(int nameIndex)
    ritual = 'ritual_ZN20QQmlJSTypePropagator21generate_LoadPropertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator21generate_LoadPropertyEi'
    self.uglySide.call(ritual, nameIndex)

  @overload(int, int)
  def generate_LoadOptionalProperty(self, name: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadOptionalProperty(int
    name, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    name : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadOptionalProperty(int name, int
    #      offset)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator29generate_LoadOptionalPropertyEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator29generate_LoadOptionalProper'
          'tyEii')
    self.uglySide.call(ritual, name, offset)

  @overload(int)
  def generate_GetLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_GetLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_GetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_GetLookup(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_GetLookupEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_GetLookupEi'
    self.uglySide.call(ritual, index)

  @overload(int, int)
  def generate_GetOptionalLookup(self, index: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_GetOptionalLookup(int
    index, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_GetOptionalLookup(int index, int
    #      offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_GetOptionalLookupEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_GetOptionalLookupE'
          'ii')
    self.uglySide.call(ritual, index, offset)

  @overload(int, int)
  def generate_StoreProperty(self, name: int, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreProperty(int name,
    int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreProperty

    Parameters
    ----------

    name : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreProperty(int name, int base)
    ritual = 'ritual_ZN20QQmlJSTypePropagator22generate_StorePropertyEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator22generate_StorePropertyEii')
    self.uglySide.call(ritual, name, base)

  @overload(int, int)
  def generate_SetLookup(self, index: int, base: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_SetLookup(int index, int
    base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_SetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_SetLookup(int index, int base)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_SetLookupEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_SetLookupEii'
    self.uglySide.call(ritual, index, base)

  @overload(int)
  def generate_LoadSuperProperty(self, property: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadSuperProperty(int
    property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    property : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_LoadSuperProperty(int property)
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_LoadSuperPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_LoadSuperPropertyE'
          'i')
    self.uglySide.call(ritual, property)

  @overload(int)
  def generate_StoreSuperProperty(self, property: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreSuperProperty(int
    property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    property : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreSuperProperty(int property)
    ritual = 'ritual_ZN20QQmlJSTypePropagator27generate_StoreSuperPropertyEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator27generate_StoreSuperProperty'
          'Ei')
    self.uglySide.call(ritual, property)

  def generate_Yield(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Yield()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Yield
    """
    #  void QQmlJSTypePropagator::generate_Yield()
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_YieldEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_YieldEv'
    self.uglySide.call(ritual)

  def generate_YieldStar(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_YieldStar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_YieldStar
    """
    #  void QQmlJSTypePropagator::generate_YieldStar()
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_YieldStarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_YieldStarEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Resume(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Resume(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Resume

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Resume(int a0)
    ritual = 'ritual_ZN20QQmlJSTypePropagator15generate_ResumeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator15generate_ResumeEi'
    self.uglySide.call(ritual, a0)

  @overload(int, int, int)
  def generate_CallValue(self, name: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallValue(int name, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CallValue

    Parameters
    ----------

    name : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CallValue(int name, int argc, int
    #      argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_CallValueEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_CallValueEiii'
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
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallWithReceiver(int
    name, int thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

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
    #  void QQmlJSTypePropagator::generate_CallWithReceiver(int name, int
    #      thisObject, int argc, int argv)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator25generate_CallWithReceiverEiiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_CallWithReceiverEi'
          'iii')
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
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallProperty(int name,
    int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CallProperty

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
    #  void QQmlJSTypePropagator::generate_CallProperty(int name, int base,
    #      int argc, int argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator21generate_CallPropertyEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator21generate_CallPropertyEiiii')
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
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallPropertyLookup(int
    lookupIndex, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

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
    #  void QQmlJSTypePropagator::generate_CallPropertyLookup(int
    #      lookupIndex, int base, int argc, int argv)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator27generate_CallPropertyLookupEiiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator27generate_CallPropertyLookup'
          'Eiiii')
    self.uglySide.call(ritual, lookupIndex, base, argc, argv)

  @overload(int, int, int)
  def generate_CallName(self, name: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallName(int name, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CallName

    Parameters
    ----------

    name : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CallName(int name, int argc, int
    #      argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_CallNameEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_CallNameEiii'
    self.uglySide.call(ritual, name, argc, argv)

  @overload(int, int)
  def generate_CallPossiblyDirectEval(self, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_CallPossiblyDirectEval(int argc, int
    argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CallPossiblyDirectEval(int argc,
    #      int argv)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator31generate_CallPossiblyDirectEvalEi'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator31generate_CallPossiblyDirect'
          'EvalEii')
    self.uglySide.call(ritual, argc, argv)

  @overload(int, int, int)
  def generate_CallGlobalLookup(
      self,
      index: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallGlobalLookup(int
    index, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CallGlobalLookup(int index, int
    #      argc, int argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_CallGlobalLookupEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_CallGlobalLookupEi'
          'ii')
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
    QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(int index,
    int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(int
    #      index, int argc, int argv)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator37generate_CallQmlContextPropertyLo'
        'okupEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator37generate_CallQmlContextProp'
          'ertyLookupEiii')
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
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallWithSpread(int func,
    int thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CallWithSpread

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
    #  void QQmlJSTypePropagator::generate_CallWithSpread(int func, int
    #      thisObject, int argc, int argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator23generate_CallWithSpreadEiiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23generate_CallWithSpreadEiii'
          'i')
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
    Calls Qt's 'void QQmlJSTypePropagator::generate_TailCall(int func, int
    thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_TailCall

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
    #  void QQmlJSTypePropagator::generate_TailCall(int func, int thisObject,
    #      int argc, int argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_TailCallEiiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_TailCallEiiii'
    self.uglySide.call(ritual, func, thisObject, argc, argv)

  @overload(int, int, int)
  def generate_Construct(self, func: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Construct(int func, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Construct

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Construct(int func, int argc, int
    #      argv)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_ConstructEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_ConstructEiii'
    self.uglySide.call(ritual, func, argc, argv)

  @overload(int, int, int)
  def generate_ConstructWithSpread(
      self,
      func: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_ConstructWithSpread(int
    func, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_ConstructWithSpread(int func, int
    #      argc, int argv)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator28generate_ConstructWithSpreadEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator28generate_ConstructWithSprea'
          'dEiii')
    self.uglySide.call(ritual, func, argc, argv)

  @overload(int)
  def generate_SetUnwindHandler(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_SetUnwindHandler(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_SetUnwindHandler(int offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_SetUnwindHandlerEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_SetUnwindHandlerEi')
    self.uglySide.call(ritual, offset)

  def generate_UnwindDispatch(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UnwindDispatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UnwindDispatch
    """
    #  void QQmlJSTypePropagator::generate_UnwindDispatch()
    ritual = 'ritual_ZN20QQmlJSTypePropagator23generate_UnwindDispatchEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23generate_UnwindDispatchEv')
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_UnwindToLabel(self, level: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UnwindToLabel(int level,
    int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UnwindToLabel

    Parameters
    ----------

    level : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_UnwindToLabel(int level, int
    #      offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator22generate_UnwindToLabelEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator22generate_UnwindToLabelEii')
    self.uglySide.call(ritual, level, offset)

  @overload(int)
  def generate_DeadTemporalZoneCheck(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(int name)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator30generate_DeadTemporalZoneCheckEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator30generate_DeadTemporalZoneCh'
          'eckEi')
    self.uglySide.call(ritual, name)

  def generate_ThrowException(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_ThrowException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_ThrowException
    """
    #  void QQmlJSTypePropagator::generate_ThrowException()
    ritual = 'ritual_ZN20QQmlJSTypePropagator23generate_ThrowExceptionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23generate_ThrowExceptionEv')
    self.uglySide.call(ritual)

  def generate_GetException(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_GetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_GetException
    """
    #  void QQmlJSTypePropagator::generate_GetException()
    ritual = 'ritual_ZN20QQmlJSTypePropagator21generate_GetExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator21generate_GetExceptionEv'
    self.uglySide.call(ritual)

  def generate_SetException(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_SetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_SetException
    """
    #  void QQmlJSTypePropagator::generate_SetException()
    ritual = 'ritual_ZN20QQmlJSTypePropagator21generate_SetExceptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator21generate_SetExceptionEv'
    self.uglySide.call(ritual)

  def generate_CreateCallContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CreateCallContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_CreateCallContext()
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_CreateCallContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_CreateCallContextE'
          'v')
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_PushCatchContext(self, index: int, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_PushCatchContext(int
    index, int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_PushCatchContext(int index, int
    #      name)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_PushCatchContextEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_PushCatchContextEi'
          'i')
    self.uglySide.call(ritual, index, name)

  def generate_PushWithContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_PushWithContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_PushWithContext
    """
    #  void QQmlJSTypePropagator::generate_PushWithContext()
    ritual = 'ritual_ZN20QQmlJSTypePropagator24generate_PushWithContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator24generate_PushWithContextEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_PushBlockContext(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_PushBlockContext(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_PushBlockContext(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_PushBlockContextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_PushBlockContextEi')
    self.uglySide.call(ritual, index)

  def generate_CloneBlockContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CloneBlockContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_CloneBlockContext()
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_CloneBlockContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_CloneBlockContextE'
          'v')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_PushScriptContext(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_PushScriptContext(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_PushScriptContext(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_PushScriptContextEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_PushScriptContextE'
          'i')
    self.uglySide.call(ritual, index)

  def generate_PopScriptContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_PopScriptContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_PopScriptContext()
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_PopScriptContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_PopScriptContextEv')
    self.uglySide.call(ritual)

  def generate_PopContext(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_PopContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_PopContext
    """
    #  void QQmlJSTypePropagator::generate_PopContext()
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_PopContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_PopContextEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_GetIterator(self, iterator: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_GetIterator(int
    iterator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_GetIterator

    Parameters
    ----------

    iterator : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_GetIterator(int iterator)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_GetIteratorEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_GetIteratorEi'
    self.uglySide.call(ritual, iterator)

  @overload(int, int)
  def generate_IteratorNext(self, value: int, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_IteratorNext(int value,
    int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_IteratorNext

    Parameters
    ----------

    value : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_IteratorNext(int value, int
    #      offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator21generate_IteratorNextEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator21generate_IteratorNextEii')
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
    QQmlJSTypePropagator::generate_IteratorNextForYieldStar(int iterator, int
    object, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    iterator : int
      Passed on as it is.

    object : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_IteratorNextForYieldStar(int
    #      iterator, int object, int offset)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator33generate_IteratorNextForYieldStar'
        'Eiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator33generate_IteratorNextForYie'
          'ldStarEiii')
    self.uglySide.call(ritual, iterator, object, offset)

  def generate_IteratorClose(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_IteratorClose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_IteratorClose
    """
    #  void QQmlJSTypePropagator::generate_IteratorClose()
    ritual = 'ritual_ZN20QQmlJSTypePropagator22generate_IteratorCloseEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator22generate_IteratorCloseEv')
    self.uglySide.call(ritual)

  def generate_DestructureRestElement(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_DestructureRestElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_DestructureRestElement()
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator31generate_DestructureRestElementEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator31generate_DestructureRestEle'
          'mentEv')
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DeleteProperty(self, base: int, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_DeleteProperty(int base,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_DeleteProperty

    Parameters
    ----------

    base : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_DeleteProperty(int base, int
    #      index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator23generate_DeletePropertyEii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23generate_DeletePropertyEii')
    self.uglySide.call(ritual, base, index)

  @overload(int)
  def generate_DeleteName(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_DeleteName(int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_DeleteName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_DeleteName(int name)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_DeleteNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_DeleteNameEi'
    self.uglySide.call(ritual, name)

  @overload(int)
  def generate_TypeofName(self, name: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_TypeofName(int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_TypeofName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_TypeofName(int name)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_TypeofNameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_TypeofNameEi'
    self.uglySide.call(ritual, name)

  def generate_TypeofValue(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_TypeofValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_TypeofValue
    """
    #  void QQmlJSTypePropagator::generate_TypeofValue()
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_TypeofValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_TypeofValueEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def generate_DeclareVar(self, varName: int, isDeletable: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_DeclareVar(int varName,
    int isDeletable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_DeclareVar

    Parameters
    ----------

    varName : int
      Passed on as it is.

    isDeletable : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_DeclareVar(int varName, int
    #      isDeletable)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_DeclareVarEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_DeclareVarEii'
    self.uglySide.call(ritual, varName, isDeletable)

  @overload(int, int)
  def generate_DefineArray(self, argc: int, args: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_DefineArray(int argc, int
    args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_DefineArray

    Parameters
    ----------

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_DefineArray(int argc, int args)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_DefineArrayEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_DefineArrayEii'
    self.uglySide.call(ritual, argc, args)

  @overload(int, int, int)
  def generate_DefineObjectLiteral(
      self,
      internalClassId: int,
      argc: int,
      args: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_DefineObjectLiteral(int
    internalClassId, int argc, int args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    internalClassId : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_DefineObjectLiteral(int
    #      internalClassId, int argc, int args)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator28generate_DefineObjectLiteralEiii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator28generate_DefineObjectLitera'
          'lEiii')
    self.uglySide.call(ritual, internalClassId, argc, args)

  @overload(int, int, int)
  def generate_CreateClass(
      self,
      classIndex: int,
      heritage: int,
      computedNames: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CreateClass(int
    classIndex, int heritage, int computedNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CreateClass

    Parameters
    ----------

    classIndex : int
      Passed on as it is.

    heritage : int
      Passed on as it is.

    computedNames : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CreateClass(int classIndex, int
    #      heritage, int computedNames)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_CreateClassEiii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator20generate_CreateClassEiii')
    self.uglySide.call(ritual, classIndex, heritage, computedNames)

  def generate_CreateMappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_CreateMappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_CreateMappedArgumentsObject()
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator36generate_CreateMappedArgumentsObj'
        'ectEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator36generate_CreateMappedArgume'
          'ntsObjectEv')
    self.uglySide.call(ritual)

  def generate_CreateUnmappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject()
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator38generate_CreateUnmappedArgumentsO'
        'bjectEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator38generate_CreateUnmappedArgu'
          'mentsObjectEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CreateRestParameter(self, argIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CreateRestParameter(int
    argIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    argIndex : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CreateRestParameter(int argIndex)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator28generate_CreateRestParameterEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator28generate_CreateRestParamete'
          'rEi')
    self.uglySide.call(ritual, argIndex)

  def generate_ConvertThisToObject(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_ConvertThisToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_ConvertThisToObject()
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator28generate_ConvertThisToObjectEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator28generate_ConvertThisToObjec'
          'tEv')
    self.uglySide.call(ritual)

  def generate_LoadSuperConstructor(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_LoadSuperConstructor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_LoadSuperConstructor()
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator29generate_LoadSuperConstructorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator29generate_LoadSuperConstruct'
          'orEv')
    self.uglySide.call(ritual)

  def generate_ToObject(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_ToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_ToObject
    """
    #  void QQmlJSTypePropagator::generate_ToObject()
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_ToObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_ToObjectEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Jump(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Jump(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Jump

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Jump(int offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator13generate_JumpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator13generate_JumpEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpTrue(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_JumpTrue(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_JumpTrue

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_JumpTrue(int offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_JumpTrueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_JumpTrueEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpFalse(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_JumpFalse(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_JumpFalse

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_JumpFalse(int offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_JumpFalseEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_JumpFalseEi'
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpNoException(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_JumpNoException(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_JumpNoException

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_JumpNoException(int offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator24generate_JumpNoExceptionEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator24generate_JumpNoExceptionEi')
    self.uglySide.call(ritual, offset)

  @overload(int)
  def generate_JumpNotUndefined(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_JumpNotUndefined(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_JumpNotUndefined(int offset)
    ritual = 'ritual_ZN20QQmlJSTypePropagator25generate_JumpNotUndefinedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator25generate_JumpNotUndefinedEi')
    self.uglySide.call(ritual, offset)

  def generate_CheckException(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CheckException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CheckException
    """
    #  void QQmlJSTypePropagator::generate_CheckException()
    ritual = 'ritual_ZN20QQmlJSTypePropagator23generate_CheckExceptionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23generate_CheckExceptionEv')
    self.uglySide.call(ritual)

  def generate_CmpEqNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpEqNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpEqNull
    """
    #  void QQmlJSTypePropagator::generate_CmpEqNull()
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_CmpEqNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_CmpEqNullEv'
    self.uglySide.call(ritual)

  def generate_CmpNeNull(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpNeNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpNeNull
    """
    #  void QQmlJSTypePropagator::generate_CmpNeNull()
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_CmpNeNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_CmpNeNullEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_CmpEqInt(self, lhsConst: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpEqInt(int lhsConst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpEqInt

    Parameters
    ----------

    lhsConst : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpEqInt(int lhsConst)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_CmpEqIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_CmpEqIntEi'
    self.uglySide.call(ritual, lhsConst)

  @overload(int)
  def generate_CmpNeInt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpNeInt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpNeInt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpNeInt(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_CmpNeIntEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_CmpNeIntEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpEq(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpEq(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpEq

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpEq(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpEqEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpEqEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpNe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpNe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpNe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpNe(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpNeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpNeEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpGt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpGt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpGt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpGt(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpGtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpGtEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpGe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpGe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpGe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpGe(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpGeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpGeEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpLt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpLt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpLt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpLt(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpLtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpLtEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpLe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpLe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpLe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpLe(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpLeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpLeEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpStrictEqual(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpStrictEqual(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpStrictEqual

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpStrictEqual(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator23generate_CmpStrictEqualEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23generate_CmpStrictEqualEi')
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpStrictNotEqual(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpStrictNotEqual(int
    lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpStrictNotEqual(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_CmpStrictNotEqualEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_CmpStrictNotEqualE'
          'i')
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpIn(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpIn(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpIn

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpIn(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_CmpInEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_CmpInEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_CmpInstanceOf(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CmpInstanceOf(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_CmpInstanceOf

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CmpInstanceOf(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator22generate_CmpInstanceOfEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator22generate_CmpInstanceOfEi')
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_As(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_As(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_As

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_As(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator11generate_AsEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator11generate_AsEi'
    self.uglySide.call(ritual, lhs)

  def generate_UNot(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UNot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UNot
    """
    #  void QQmlJSTypePropagator::generate_UNot()
    ritual = 'ritual_ZN20QQmlJSTypePropagator13generate_UNotEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator13generate_UNotEv'
    self.uglySide.call(ritual)

  def generate_UPlus(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UPlus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UPlus
    """
    #  void QQmlJSTypePropagator::generate_UPlus()
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_UPlusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_UPlusEv'
    self.uglySide.call(ritual)

  def generate_UMinus(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UMinus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UMinus
    """
    #  void QQmlJSTypePropagator::generate_UMinus()
    ritual = 'ritual_ZN20QQmlJSTypePropagator15generate_UMinusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator15generate_UMinusEv'
    self.uglySide.call(ritual)

  def generate_UCompl(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UCompl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UCompl
    """
    #  void QQmlJSTypePropagator::generate_UCompl()
    ritual = 'ritual_ZN20QQmlJSTypePropagator15generate_UComplEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator15generate_UComplEv'
    self.uglySide.call(ritual)

  def generate_Increment(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Increment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Increment
    """
    #  void QQmlJSTypePropagator::generate_Increment()
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_IncrementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_IncrementEv'
    self.uglySide.call(ritual)

  def generate_Decrement(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Decrement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Decrement
    """
    #  void QQmlJSTypePropagator::generate_Decrement()
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_DecrementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_DecrementEv'
    self.uglySide.call(ritual)

  @overload(int)
  def generate_Add(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Add(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Add

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Add(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_AddEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_AddEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitAnd(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_BitAnd(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_BitAnd

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_BitAnd(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator15generate_BitAndEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator15generate_BitAndEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitOr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_BitOr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_BitOr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_BitOr(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator14generate_BitOrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator14generate_BitOrEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitXor(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_BitXor(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_BitXor

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_BitXor(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator15generate_BitXorEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator15generate_BitXorEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_UShr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UShr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UShr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_UShr(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator13generate_UShrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator13generate_UShrEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Shr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Shr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Shr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Shr(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_ShrEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_ShrEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Shl(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Shl(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Shl

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Shl(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_ShlEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_ShlEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_BitAndConst(self, rhsConst: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_BitAndConst(int
    rhsConst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_BitAndConst

    Parameters
    ----------

    rhsConst : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_BitAndConst(int rhsConst)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_BitAndConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_BitAndConstEi'
    self.uglySide.call(ritual, rhsConst)

  @overload(int)
  def generate_BitOrConst(self, rhsConst: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_BitOrConst(int
    rhsConst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_BitOrConst

    Parameters
    ----------

    rhsConst : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_BitOrConst(int rhsConst)
    ritual = 'ritual_ZN20QQmlJSTypePropagator19generate_BitOrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator19generate_BitOrConstEi'
    self.uglySide.call(ritual, rhsConst)

  @overload(int)
  def generate_BitXorConst(self, rhsConst: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_BitXorConst(int
    rhsConst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_BitXorConst

    Parameters
    ----------

    rhsConst : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_BitXorConst(int rhsConst)
    ritual = 'ritual_ZN20QQmlJSTypePropagator20generate_BitXorConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator20generate_BitXorConstEi'
    self.uglySide.call(ritual, rhsConst)

  @overload(int)
  def generate_UShrConst(self, rhsConst: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_UShrConst(int rhsConst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_UShrConst

    Parameters
    ----------

    rhsConst : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_UShrConst(int rhsConst)
    ritual = 'ritual_ZN20QQmlJSTypePropagator18generate_UShrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator18generate_UShrConstEi'
    self.uglySide.call(ritual, rhsConst)

  @overload(int)
  def generate_ShrConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_ShrConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_ShrConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_ShrConst(int rhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_ShrConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_ShrConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_ShlConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_ShlConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_ShlConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_ShlConst(int rhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17generate_ShlConstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator17generate_ShlConstEi'
    self.uglySide.call(ritual, rhs)

  @overload(int)
  def generate_Exp(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Exp(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Exp

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Exp(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_ExpEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_ExpEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Mul(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Mul(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Mul

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Mul(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_MulEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_MulEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Div(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Div(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Div

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Div(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_DivEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_DivEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Mod(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Mod(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Mod

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Mod(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_ModEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_ModEi'
    self.uglySide.call(ritual, lhs)

  @overload(int)
  def generate_Sub(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Sub(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_Sub

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Sub(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator12generate_SubEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator12generate_SubEi'
    self.uglySide.call(ritual, lhs)

  @overload(int, int)
  def generate_InitializeBlockDeadTemporalZone(
      self,
      firstReg: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(int
    firstReg, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    firstReg : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void
    #      QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(int
    #      firstReg, int count)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator40generate_InitializeBlockDeadTempo'
        'ralZoneEii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator40generate_InitializeBlockDea'
          'dTemporalZoneEii')
    self.uglySide.call(ritual, firstReg, count)

  def generate_ThrowOnNullOrUndefined(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html
    """
    #  void QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined()
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator31generate_ThrowOnNullOrUndefinedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator31generate_ThrowOnNullOrUndef'
          'inedEv')
    self.uglySide.call(ritual)

  @overload(int)
  def generate_GetTemplateObject(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_GetTemplateObject(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_GetTemplateObject(int index)
    ritual = 'ritual_ZN20QQmlJSTypePropagator26generate_GetTemplateObjectEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator26generate_GetTemplateObjectE'
          'i')
    self.uglySide.call(ritual, index)

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, instr: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::endInstruction(QV4::Moth::Instr::Type instr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#endInstruction

    Parameters
    ----------

    instr : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QQmlJSTypePropagator::endInstruction(QV4::Moth::Instr::Type
    #      instr)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator14endInstructionEN3QV44Moth5Instr4T'
        'ypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator14endInstructionEN3QV44Moth5I'
          'nstr4TypeE')
    self.uglySide.call(ritual, instr.value)

  @overload(str, bool)
  def handleUnqualifiedAccess(self, name: str, isMethod: bool) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::handleUnqualifiedAccess(const
    QString &name, bool isMethod) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#handleUnqualifiedAccess

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    isMethod : bool
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::handleUnqualifiedAccess(const QString
    #      &name, bool isMethod) const
    ritual = (
        'ritual_ZNK20QQmlJSTypePropagator23handleUnqualifiedAccessERK7QStri'
        'ngb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQmlJSTypePropagator23handleUnqualifiedAccessERK'
          '7QStringb')
    self.uglySide.call(ritual, name, isMethod)

  @overload(str, bool)
  def handleUnqualifiedAccessAndContextProperties(
      self,
      name: str,
      isMethod: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties(const
    QString &name, bool isMethod) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    isMethod : bool
      Passed on as it is.
    """
    #  void
    #      QQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties(
    #      const QString &name, bool isMethod) const
    ritual = (
        'ritual_ZNK20QQmlJSTypePropagator43handleUnqualifiedAccessAndContex'
        'tPropertiesERK7QStringb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQmlJSTypePropagator43handleUnqualifiedAccessAnd'
          'ContextPropertiesERK7QStringb')
    self.uglySide.call(ritual, name, isMethod)

  @overload(str)
  def handleImportNamespaceLookup(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypePropagator::handleImportNamespaceLookup(const
    QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSTypePropagator::handleImportNamespaceLookup(const QString
    #      &propertyName)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator27handleImportNamespaceLookupERK7QS'
        'tring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator27handleImportNamespaceLookup'
          'ERK7QString')
    return self.uglySide.call(ritual, propertyName)

  @overload(str)
  def handleLookupError(self, propertyName: str) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::handleLookupError(const QString
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#handleLookupError

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSTypePropagator::handleLookupError(const QString
    #      &propertyName)
    ritual = 'ritual_ZN20QQmlJSTypePropagator17handleLookupErrorERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator17handleLookupErrorERK7QStrin'
          'g')
    self.uglySide.call(ritual, propertyName)

  @overload(QQmlJSRegisterContent, str)
  def checkForEnumProblems(
      self,
      base: QQmlJSRegisterContent,
      propertyName: str,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypePropagator::checkForEnumProblems(QQmlJSRegisterContent base,
    const QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#checkForEnumProblems

    Parameters
    ----------

    base : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSTypePropagator::checkForEnumProblems(QQmlJSRegisterContent
    #      base, const QString &propertyName)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator20checkForEnumProblemsE21QQmlJSRegi'
        'sterContentRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator20checkForEnumProblemsE21QQml'
          'JSRegisterContentRK7QString')
    return self.uglySide.call(ritual, self._valueOf(base), propertyName)

  @overload(int)
  def warnAboutTypeCoercion(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::warnAboutTypeCoercion(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#warnAboutTypeCoercion

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::warnAboutTypeCoercion(int lhs)
    ritual = 'ritual_ZN20QQmlJSTypePropagator21warnAboutTypeCoercionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQmlJSTypePropagator21warnAboutTypeCoercionEi'
    self.uglySide.call(ritual, lhs)

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent)
  def checkConversion(
      self,
      from_: QQmlJSRegisterContent,
      to: QQmlJSRegisterContent,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::checkConversion(QQmlJSRegisterContent from,
    QQmlJSRegisterContent to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#checkConversion

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    to : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypePropagator::checkConversion(QQmlJSRegisterContent from,
    #      QQmlJSRegisterContent to)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator15checkConversionE21QQmlJSRegisterC'
        'ontentS0_',
        self._valueOf(from_), self._valueOf(to),
    )

  @overload(QQmlJSTypeResolver.UnaryOperator)
  def generateUnaryArithmeticOperation(
      self,
      op: QQmlJSTypeResolver.UnaryOperator,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generateUnaryArithmeticOperation(
    QQmlJSTypeResolver::UnaryOperator op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    op : QQmlJSTypeResolver.UnaryOperator
      Passed on as its number.
    """
    #  void QQmlJSTypePropagator::generateUnaryArithmeticOperation(
    #      QQmlJSTypeResolver::UnaryOperator op)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator32generateUnaryArithmeticOperationE'
        'N18QQmlJSTypeResolver13UnaryOperatorE',
        op.value,
    )

  @overload(QSOperator.Op, int)
  def propagateBinaryOperation(
      self,
      op: QSOperator.Op,
      lhs: int,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypePropagator::propagateBinaryOperation(QSOperator::Op op, int
    lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#propagateBinaryOperation

    Parameters
    ----------

    op : QSOperator.Op
      Passed on as its number.

    lhs : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSTypePropagator::propagateBinaryOperation(QSOperator::Op op,
    #      int lhs)
    address = self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator24propagateBinaryOperationEN10QSOpe'
        'rator2OpEi',
        op.value, lhs,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QSOperator.Op, int)
  def generateBinaryArithmeticOperation(
      self,
      op: QSOperator.Op,
      lhs: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generateBinaryArithmeticOperation(QSOperator::Op
    op, int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    op : QSOperator.Op
      Passed on as its number.

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generateBinaryArithmeticOperation(
    #      QSOperator::Op op, int lhs)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator33generateBinaryArithmeticOperation'
        'EN10QSOperator2OpEi',
        op.value, lhs,
    )

  @overload(QSOperator.Op)
  def generateBinaryConstArithmeticOperation(
      self,
      op: QSOperator.Op,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generateBinaryConstArithmeticOperation(
    QSOperator::Op op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    op : QSOperator.Op
      Passed on as its number.
    """
    #  void QQmlJSTypePropagator::generateBinaryConstArithmeticOperation(
    #      QSOperator::Op op)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator38generateBinaryConstArithmeticOper'
        'ationEN10QSOperator2OpE',
        op.value,
    )

  @overload(int)
  def generate_StoreNameCommon(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_StoreNameCommon(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#generate_StoreNameCommon

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_StoreNameCommon(int nameIndex)
    ritual = 'ritual_ZN20QQmlJSTypePropagator24generate_StoreNameCommonEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator24generate_StoreNameCommonEi')
    self.uglySide.call(ritual, nameIndex)

  @overload(QList[QQmlJSMetaMethod], int, int, QQmlJSRegisterContent)
  def propagateCall(
      self,
      methods: QList[QQmlJSMetaMethod],
      argc: int,
      argv: int,
      scope: QQmlJSRegisterContent,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::propagateCall(const
    QList<QQmlJSMetaMethod> &methods, int argc, int argv,
    QQmlJSRegisterContent scope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#propagateCall

    Parameters
    ----------

    methods : QList[QQmlJSMetaMethod]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.

    scope : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypePropagator::propagateCall(const QList<QQmlJSMetaMethod>
    #      &methods, int argc, int argv, QQmlJSRegisterContent scope)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator13propagateCallERK5QListI16QQmlJSMe'
        'taMethodEii21QQmlJSRegisterContent',
        self._valueOf(methods), argc, argv, self._valueOf(scope),
    )

  @overload(str)
  def propagateTranslationMethod_SAcheck(self, methodName: str) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::propagateTranslationMethod_SAcheck(const QString
    &methodName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    methodName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSTypePropagator::propagateTranslationMethod_SAcheck(const
    #      QString &methodName)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator34propagateTranslationMethod_SAchec'
        'kERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator34propagateTranslationMethod_'
          'SAcheckERK7QString')
    self.uglySide.call(ritual, methodName)

  @overload(QList[QQmlJSMetaMethod], int, int)
  def propagateTranslationMethod(
      self,
      methods: QList[QQmlJSMetaMethod],
      argc: int,
      argv: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypePropagator::propagateTranslationMethod(const
    QList<QQmlJSMetaMethod> &methods, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    methods : QList[QQmlJSMetaMethod]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  bool QQmlJSTypePropagator::propagateTranslationMethod(const
    #      QList<QQmlJSMetaMethod> &methods, int argc, int argv)
    return self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator26propagateTranslationMethodERK5QLi'
        'stI16QQmlJSMetaMethodEii',
        self._valueOf(methods), argc, argv,
    )

  @overload(QQmlJSRegisterContent, int)
  def propagateStringArgCall(
      self,
      base: QQmlJSRegisterContent,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::propagateStringArgCall(QQmlJSRegisterContent base,
    int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#propagateStringArgCall

    Parameters
    ----------

    base : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    argv : int
      Passed on as it is.
    """
    #  void
    #      QQmlJSTypePropagator::propagateStringArgCall(QQmlJSRegisterContent
    #      base, int argv)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator22propagateStringArgCallE21QQmlJSRe'
        'gisterContenti',
        self._valueOf(base), argv,
    )

  @overload(str, int, int, QQmlJSRegisterContent)
  def propagateArrayMethod(
      self,
      name: str,
      argc: int,
      argv: int,
      valueType: QQmlJSRegisterContent,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJSTypePropagator::propagateArrayMethod(const QString
    &name, int argc, int argv, QQmlJSRegisterContent valueType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#propagateArrayMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.

    valueType : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypePropagator::propagateArrayMethod(const QString &name,
    #      int argc, int argv, QQmlJSRegisterContent valueType)
    return self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator20propagateArrayMethodERK7QStringii'
        '21QQmlJSRegisterContent',
        name, argc, argv, self._valueOf(valueType),
    )

  @overload(str, int)
  def propagatePropertyLookup(self, name: str, lookupIndex: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::propagatePropertyLookup(const
    QString &name, int lookupIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#propagatePropertyLookup

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    lookupIndex : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::propagatePropertyLookup(const QString
    #      &name, int lookupIndex)
    ritual = (
        'ritual_ZN20QQmlJSTypePropagator23propagatePropertyLookupERK7QStrin'
        'gi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQmlJSTypePropagator23propagatePropertyLookupERK7'
          'QStringi')
    self.uglySide.call(ritual, name, lookupIndex)

  @overload(str, int, int)
  def propagateScopeLookupCall(
      self,
      functionName: str,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::propagateScopeLookupCall(const
    QString &functionName, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#propagateScopeLookupCall

    Parameters
    ----------

    functionName : str
      Passed on as it is: a QString is made of it for the call.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::propagateScopeLookupCall(const QString
    #      &functionName, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator24propagateScopeLookupCallERK7QStri'
        'ngii',
        functionName, argc, argv,
    )

  @overload(int)
  def saveRegisterStateForJump(self, offset: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::saveRegisterStateForJump(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#saveRegisterStateForJump

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::saveRegisterStateForJump(int offset)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator24saveRegisterStateForJumpEi',
        offset,
    )

  @overload(QQmlJSRegisterContent, QQmlJSRegisterContent)
  def canConvertFromTo(
      self,
      from_: QQmlJSRegisterContent,
      to: QQmlJSRegisterContent,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSTypePropagator::canConvertFromTo(QQmlJSRegisterContent from,
    QQmlJSRegisterContent to)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#canConvertFromTo

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    to : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool QQmlJSTypePropagator::canConvertFromTo(QQmlJSRegisterContent
    #      from, QQmlJSRegisterContent to)
    return self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator16canConvertFromToE21QQmlJSRegister'
        'ContentS0_',
        self._valueOf(from_), self._valueOf(to),
    )

  @overload(int)
  def checkedInputRegister(self, reg: int) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSTypePropagator::checkedInputRegister(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#checkedInputRegister

    Parameters
    ----------

    reg : int
      Passed on as it is.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSTypePropagator::checkedInputRegister(int
    #      reg)
    address = self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator20checkedInputRegisterEi', reg,
    )
    from . import QQmlJSRegisterContent
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(
      int, QQmlJSCompilePass.VirtualRegister,
      QQmlJSCompilePass.VirtualRegister,
  )
  def mergeRegister(
      self,
      index: int,
      a: QQmlJSCompilePass.VirtualRegister,
      b: QQmlJSCompilePass.VirtualRegister,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::mergeRegister(int index, const
    VirtualRegister &a, const VirtualRegister &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#mergeRegister

    Parameters
    ----------

    index : int
      Passed on as it is.

    a : QQmlJSCompilePass.VirtualRegister
      Passed on as a value: Qt reads the C++
      QQmlJSCompilePass::VirtualRegister, which stays Python's own.

    b : QQmlJSCompilePass.VirtualRegister
      Passed on as a value: Qt reads the C++
      QQmlJSCompilePass::VirtualRegister, which stays Python's own.
    """
    #  void QQmlJSTypePropagator::mergeRegister(int index, const
    #      VirtualRegister &a, const VirtualRegister &b)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator13mergeRegisterEiRKN17QQmlJSCompile'
        'Pass15VirtualRegisterES3_',
        index, self._valueOf(a), self._valueOf(b),
    )

  @overload(int)
  def addReadRegister(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::addReadRegister(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#addReadRegister

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::addReadRegister(int index)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator15addReadRegisterEi', index,
    )

  @overload(int, QQmlJSRegisterContent)
  def addReadRegister(
      self,
      index: int,
      convertTo: QQmlJSRegisterContent,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::addReadRegister(int index,
    QQmlJSRegisterContent convertTo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#addReadRegister

    Parameters
    ----------

    index : int
      Passed on as it is.

    convertTo : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypePropagator::addReadRegister(int index,
    #      QQmlJSRegisterContent convertTo)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator15addReadRegisterEi21QQmlJSRegister'
        'Content',
        index, self._valueOf(convertTo),
    )

  @overload()
  def addReadAccumulator(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::addReadAccumulator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#addReadAccumulator
    """
    #  void QQmlJSTypePropagator::addReadAccumulator()
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator18addReadAccumulatorEv',
    )

  @overload(QQmlJSRegisterContent)
  def addReadAccumulator(self, convertTo: QQmlJSRegisterContent) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::addReadAccumulator(QQmlJSRegisterContent
    convertTo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#addReadAccumulator

    Parameters
    ----------

    convertTo : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  void QQmlJSTypePropagator::addReadAccumulator(QQmlJSRegisterContent
    #      convertTo)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator18addReadAccumulatorE21QQmlJSRegist'
        'erContent',
        self._valueOf(convertTo),
    )

  def recordEqualsNullType(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::recordEqualsNullType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#recordEqualsNullType
    """
    #  void QQmlJSTypePropagator::recordEqualsNullType()
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator20recordEqualsNullTypeEv',
    )

  def recordEqualsIntType(self) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::recordEqualsIntType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#recordEqualsIntType
    """
    #  void QQmlJSTypePropagator::recordEqualsIntType()
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator19recordEqualsIntTypeEv',
    )

  @overload(int)
  def recordEqualsType(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::recordEqualsType(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#recordEqualsType

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::recordEqualsType(int lhs)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator16recordEqualsTypeEi', lhs,
    )

  @overload(int)
  def recordCompareType(self, lhs: int) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::recordCompareType(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html#recordCompareType

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::recordCompareType(int lhs)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator17recordCompareTypeEi', lhs,
    )

  @overload(str, int, int, int)
  def generate_CallProperty_SCMath(
      self,
      name: str,
      base: int,
      arcg: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_CallProperty_SCMath(const
    QString &name, int base, int arcg, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    base : int
      Passed on as it is.

    arcg : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_CallProperty_SCMath(const QString
    #      &name, int base, int arcg, int argv)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator28generate_CallProperty_SCMathERK7Q'
        'Stringiii',
        name, base, arcg, argv,
    )

  @overload(str, int, int, int)
  def generate_CallProperty_SCconsole(
      self,
      name: str,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSTypePropagator::generate_CallProperty_SCconsole(const QString
    &name, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

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
    #  void QQmlJSTypePropagator::generate_CallProperty_SCconsole(const
    #      QString &name, int base, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator31generate_CallProperty_SCconsoleER'
        'K7QStringiii',
        name, base, argc, argv,
    )

  @overload(QQmlJSMetaMethod, int, int)
  def generate_Construct_SCDate(
      self,
      ctor: QQmlJSMetaMethod,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Construct_SCDate(const
    QQmlJSMetaMethod &ctor, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    ctor : QQmlJSMetaMethod
      Passed on as a value: Qt reads the C++ QQmlJSMetaMethod, which stays
      Python's own.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Construct_SCDate(const
    #      QQmlJSMetaMethod &ctor, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator25generate_Construct_SCDateERK16QQm'
        'lJSMetaMethodii',
        self._valueOf(ctor), argc, argv,
    )

  @overload(QQmlJSMetaMethod, int, int)
  def generate_Construct_SCArray(
      self,
      ctor: QQmlJSMetaMethod,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::generate_Construct_SCArray(const
    QQmlJSMetaMethod &ctor, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljstypepropagator.html

    Parameters
    ----------

    ctor : QQmlJSMetaMethod
      Passed on as a value: Qt reads the C++ QQmlJSMetaMethod, which stays
      Python's own.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QQmlJSTypePropagator::generate_Construct_SCArray(const
    #      QQmlJSMetaMethod &ctor, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator26generate_Construct_SCArrayERK16QQ'
        'mlJSMetaMethodii',
        self._valueOf(ctor), argc, argv,
    )

  @overload(str)
  def addError(self, message: str) -> None:
    """
    Calls Qt's 'void QQmlJSTypePropagator::addError(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljstypepropagator.html#addError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSTypePropagator::addError(const QString &message)
    self.uglySide.call(
        'ritual_ZN20QQmlJSTypePropagator8addErrorERK7QString', message,
    )

  @staticmethod
  def bestMatchForCall(*__, **_) -> Never:
    """
    Qt's 'QQmlJSMetaMethod QQmlJSTypePropagator::bestMatchForCall(const
    QList<QQmlJSMetaMethod> &methods, int argc, int argv, QStringList
    *errors)': names 'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypePropagator.bestMatchForCall' has no cute function yet. "
        "Qt's 'QQmlJSMetaMethod "
        "QQmlJSTypePropagator::bestMatchForCall(const "
        "QList<QQmlJSMetaMethod> &methods, int argc, int argv, QStringList "
        "*errors)': names 'QStringList', which has no cute class yet.")

  @staticmethod
  def checkDeprecated(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSTypePropagator::checkDeprecated(QQmlJSScope::ConstPtr
    scope, const QString &name, bool isMethod) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypePropagator.checkDeprecated' has no cute function yet. "
        "Qt's 'void "
        "QQmlJSTypePropagator::checkDeprecated(QQmlJSScope::ConstPtr scope, "
        "const QString &name, bool isMethod) const': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def isCallingProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSTypePropagator::isCallingProperty(QQmlJSScope::ConstPtr
    scope, const QString &name) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypePropagator.isCallingProperty' has no cute function yet. "
        "Qt's 'bool "
        "QQmlJSTypePropagator::isCallingProperty(QQmlJSScope::ConstPtr "
        "scope, const QString &name) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def propertyResolution(*__, **_) -> Never:
    """
    Qt's 'PropertyResolution
    QQmlJSTypePropagator::propertyResolution(QQmlJSScope::ConstPtr scope,
    const QString &type) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSTypePropagator.propertyResolution' has no cute function "
        "yet. Qt's 'PropertyResolution "
        "QQmlJSTypePropagator::propertyResolution(QQmlJSScope::ConstPtr "
        "scope, const QString &type) const': takes a type Python has no way "
        "to hand over yet.")
