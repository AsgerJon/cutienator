"""
QQmlJSMetaMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSMetaMethod to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QList, QStringList
from ..QtQml import QQmlJS
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QQmlJSAnnotation, QQmlJSMetaParameter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSAnnotation = WAIT['QQmlJSAnnotation']
  QQmlJSMetaParameter = WAIT['QQmlJSMetaParameter']


class QQmlJSMetaMethod(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSMetaMethod: a plain Python object standing in
  front of one C++ QQmlJSMetaMethod.

  C++ hands a QQmlJSMetaMethod around as a copy, so every C++
  QQmlJSMetaMethod behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSMetaMethod that has a ritual and that Python
  can call so far, 38 names in all: 'methodName', 'setMethodName',
  'sourceLocation', 'setSourceLocation', 'returnValue', 'setReturnValue',
  'returnTypeName', 'setReturnTypeName', 'parameters', 'parameterNames',
  'setParameters', 'addParameter', 'methodType', 'setMethodType', 'access',
  'revision', 'setRevision', 'isCloned', 'setIsCloned', 'isConstructor',
  'setIsConstructor', 'isJavaScriptFunction', 'setIsJavaScriptFunction',
  'isImplicitQmlPropertyChangeSignal',
  'setIsImplicitQmlPropertyChangeSignal', 'isConst', 'setIsConst', 'isValid',
  'annotations', 'setAnnotations', 'setJsFunctionIndex', 'jsFunctionIndex',
  'setConstructorIndex', 'constructorIndex', 'setMethodIndex', 'methodIndex',
  'setOtherMethodIndex', 'otherMethodIndex'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSharedPointer<const QQmlJSScope> QQmlJSMetaMethod::returnType()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlJSMetaMethod::setReturnType(QWeakPointer<const
    QQmlJSScope> type)': takes a type Python has no way to hand over yet.
  - Qt's 'std::pair<QList<QQmlJSMetaParameter>::iterator,
    QList<QQmlJSMetaParameter>::iterator>
    QQmlJSMetaMethod::mutableParametersRange()': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlJSMetaMethod::~QQmlJSMetaMethod()': the destructor: Python
    removes its C++ QQmlJSMetaMethod by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 leans on 'operator==(QQmlJSAnnotation
  const&, QQmlJSAnnotation const&)', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQmlJSMetaMethod is created at the first use, not by
    'QQmlJSMetaMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSMetaMethod back gives a copy the ritual made
    for Python, in a new cute QQmlJSMetaMethod.
  - Each name of Qt's QQmlJSMetaMethod that has no cute function yet,
    'mutableParametersRange', 'returnType', 'setReturnType', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSMetaMethod, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AbsoluteFunctionIndex(CuteNum, scoped=True):
    """
    The enum 'QQmlJSMetaMethod::AbsoluteFunctionIndex' of Qt, with the 1
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Invalid = Kee[int](-1)

  class Access(CuteNum):
    """
    The enum 'QQmlJSMetaMethod::Access' of Qt, with the 3 names Qt gives in
    it.
    """

    Private = Kee[int](0)
    Protected = Kee[int](1)
    Public = Kee[int](2)

  class RelativeFunctionIndex(CuteNum, scoped=True):
    """
    The enum 'QQmlJSMetaMethod::RelativeFunctionIndex' of Qt, with the 1
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Invalid = Kee[int](-1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSMetaMethod'

  #  Qt's '~QQmlJSMetaMethod()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSMetaMethod behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlJSMetaMethodD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def methodName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaMethod::methodName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#methodName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaMethod::methodName() const
    return self.uglySide.call('ritual_ZNK16QQmlJSMetaMethod10methodNameEv')

  def sourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'QQmlJS::SourceLocation QQmlJSMetaMethod::sourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#sourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJS::SourceLocation QQmlJSMetaMethod::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod14sourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def returnValue(self) -> QQmlJSMetaParameter:
    """
    Calls Qt's 'QQmlJSMetaReturnType QQmlJSMetaMethod::returnValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#returnValue

    Returns
    -------

    QQmlJSMetaParameter
      A new cute QQmlJSMetaParameter around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSMetaReturnType QQmlJSMetaMethod::returnValue() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod11returnValueEv',
    )
    from . import QQmlJSMetaParameter
    return QQmlJSMetaParameter._cuteOwning(address)

  def returnTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaMethod::returnTypeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#returnTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaMethod::returnTypeName() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod14returnTypeNameEv',
    )

  def parameters(self) -> QList[QQmlJSMetaParameter]:
    """
    Calls Qt's 'QList<QQmlJSMetaParameter> QQmlJSMetaMethod::parameters()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#parameters

    Returns
    -------

    QList[QQmlJSMetaParameter]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaParameter> QQmlJSMetaMethod::parameters() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod10parametersEv',
    )
    from . import QQmlJSMetaParameter
    return QList[QQmlJSMetaParameter]._cuteOwning(address)

  def parameterNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSMetaMethod::parameterNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#parameterNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSMetaMethod::parameterNames() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod14parameterNamesEv',
    )
    return QStringList._cuteOwning(address)

  def methodType(self) -> QQmlSA.MethodType:
    """
    Calls Qt's 'QQmlJSMetaMethodType QQmlJSMetaMethod::methodType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#methodType

    Returns
    -------

    QQmlSA.MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.MethodType(number)' gives.
    """
    #  QQmlJSMetaMethodType QQmlJSMetaMethod::methodType() const
    return QQmlSA.MethodType(self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod10methodTypeEv',
    ))

  def access(self) -> Access:
    """
    Calls Qt's 'Access QQmlJSMetaMethod::access() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#access

    Returns
    -------

    Access
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Access(number)' gives.
    """
    #  Access QQmlJSMetaMethod::access() const
    return QQmlJSMetaMethod.Access(self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod6accessEv',
    ))

  def revision(self) -> int:
    """
    Calls Qt's 'int QQmlJSMetaMethod::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#revision
    """
    #  int QQmlJSMetaMethod::revision() const
    return self.uglySide.call('ritual_ZNK16QQmlJSMetaMethod8revisionEv')

  def isCloned(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaMethod::isCloned() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#isCloned
    """
    #  bool QQmlJSMetaMethod::isCloned() const
    return self.uglySide.call('ritual_ZNK16QQmlJSMetaMethod8isClonedEv')

  def isConstructor(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaMethod::isConstructor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#isConstructor
    """
    #  bool QQmlJSMetaMethod::isConstructor() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod13isConstructorEv',
    )

  def isJavaScriptFunction(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaMethod::isJavaScriptFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#isJavaScriptFunction
    """
    #  bool QQmlJSMetaMethod::isJavaScriptFunction() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod20isJavaScriptFunctionEv',
    )

  def isImplicitQmlPropertyChangeSignal(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaMethod::isImplicitQmlPropertyChangeSignal()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html
    """
    #  bool QQmlJSMetaMethod::isImplicitQmlPropertyChangeSignal() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod33isImplicitQmlPropertyChangeSignalEv',
    )

  def isConst(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaMethod::isConst() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#isConst
    """
    #  bool QQmlJSMetaMethod::isConst() const
    return self.uglySide.call('ritual_ZNK16QQmlJSMetaMethod7isConstEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaMethod::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#isValid
    """
    #  bool QQmlJSMetaMethod::isValid() const
    return self.uglySide.call('ritual_ZNK16QQmlJSMetaMethod7isValidEv')

  def annotations(self) -> QList[QQmlJSAnnotation]:
    """
    Calls Qt's 'const QList<QQmlJSAnnotation>
    &QQmlJSMetaMethod::annotations() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#annotations

    Returns
    -------

    QList[QQmlJSAnnotation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QQmlJSAnnotation> &QQmlJSMetaMethod::annotations() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod11annotationsEv',
    )
    from . import QQmlJSAnnotation
    return QList[QQmlJSAnnotation]._cuteOwning(address)

  def jsFunctionIndex(self) -> RelativeFunctionIndex:
    """
    Calls Qt's 'RelativeFunctionIndex QQmlJSMetaMethod::jsFunctionIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#jsFunctionIndex

    Returns
    -------

    RelativeFunctionIndex
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RelativeFunctionIndex(number)' gives.
    """
    #  RelativeFunctionIndex QQmlJSMetaMethod::jsFunctionIndex() const
    return QQmlJSMetaMethod.RelativeFunctionIndex(self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod15jsFunctionIndexEv',
    ))

  def constructorIndex(self) -> RelativeFunctionIndex:
    """
    Calls Qt's 'RelativeFunctionIndex QQmlJSMetaMethod::constructorIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#constructorIndex

    Returns
    -------

    RelativeFunctionIndex
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RelativeFunctionIndex(number)' gives.
    """
    #  RelativeFunctionIndex QQmlJSMetaMethod::constructorIndex() const
    return QQmlJSMetaMethod.RelativeFunctionIndex(self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod16constructorIndexEv',
    ))

  def methodIndex(self) -> RelativeFunctionIndex:
    """
    Calls Qt's 'RelativeFunctionIndex QQmlJSMetaMethod::methodIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#methodIndex

    Returns
    -------

    RelativeFunctionIndex
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RelativeFunctionIndex(number)' gives.
    """
    #  RelativeFunctionIndex QQmlJSMetaMethod::methodIndex() const
    return QQmlJSMetaMethod.RelativeFunctionIndex(self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod11methodIndexEv',
    ))

  def otherMethodIndex(self) -> RelativeFunctionIndex:
    """
    Calls Qt's 'RelativeFunctionIndex QQmlJSMetaMethod::otherMethodIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#otherMethodIndex

    Returns
    -------

    RelativeFunctionIndex
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RelativeFunctionIndex(number)' gives.
    """
    #  RelativeFunctionIndex QQmlJSMetaMethod::otherMethodIndex() const
    return QQmlJSMetaMethod.RelativeFunctionIndex(self.uglySide.call(
        'ritual_ZNK16QQmlJSMetaMethod16otherMethodIndexEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setMethodName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setMethodName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setMethodName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaMethod::setMethodName(const QString &name)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod13setMethodNameERK7QString', name,
    )

  @overload(WAIT['QQmlJS.SourceLocation'])
  def setSourceLocation(self, location: QQmlJS.SourceLocation) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaMethod::setSourceLocation(QQmlJS::SourceLocation location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setSourceLocation

    Parameters
    ----------

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSMetaMethod::setSourceLocation(QQmlJS::SourceLocation
    #      location)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod17setSourceLocationEN6QQmlJS14SourceLoc'
        'ationE',
        self._valueOf(location),
    )

  @overload(QQmlJSMetaParameter)
  def setReturnValue(self, returnValue: QQmlJSMetaParameter) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setReturnValue(const
    QQmlJSMetaReturnType returnValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setReturnValue

    Parameters
    ----------

    returnValue : QQmlJSMetaParameter
      Passed on as a value: Qt reads the C++ QQmlJSMetaParameter, which stays
      Python's own.
    """
    #  void QQmlJSMetaMethod::setReturnValue(const QQmlJSMetaReturnType
    #      returnValue)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod14setReturnValueE19QQmlJSMetaParameter',
        self._valueOf(returnValue),
    )

  @overload(str)
  def setReturnTypeName(self, typeName: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setReturnTypeName(const QString
    &typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setReturnTypeName

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaMethod::setReturnTypeName(const QString &typeName)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod17setReturnTypeNameERK7QString',
        typeName,
    )

  @overload(QList[QQmlJSMetaParameter])
  def setParameters(self, parameters: QList[QQmlJSMetaParameter]) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setParameters(const
    QList<QQmlJSMetaParameter> &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setParameters

    Parameters
    ----------

    parameters : QList[QQmlJSMetaParameter]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSMetaMethod::setParameters(const QList<QQmlJSMetaParameter>
    #      &parameters)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod13setParametersERK5QListI19QQmlJSMetaPa'
        'rameterE',
        self._valueOf(parameters),
    )

  @overload(QQmlSA.MethodType)
  def setMethodType(self, methodType: QQmlSA.MethodType) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setMethodType(MethodType methodType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setMethodType

    Parameters
    ----------

    methodType : QQmlSA.MethodType
      Passed on as its number.
    """
    #  void QQmlJSMetaMethod::setMethodType(MethodType methodType)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod13setMethodTypeEN6QQmlSA10MethodTypeE',
        methodType.value,
    )

  @overload(int)
  def setRevision(self, r: int) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setRevision(int r)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#setRevision

    Parameters
    ----------

    r : int
      Passed on as it is.
    """
    #  void QQmlJSMetaMethod::setRevision(int r)
    self.uglySide.call('ritual_ZN16QQmlJSMetaMethod11setRevisionEi', r)

  @overload(bool)
  def setIsCloned(self, isCloned: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setIsCloned(bool isCloned)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#setIsCloned

    Parameters
    ----------

    isCloned : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaMethod::setIsCloned(bool isCloned)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod11setIsClonedEb', isCloned,
    )

  @overload(bool)
  def setIsConstructor(self, isConstructor: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setIsConstructor(bool isConstructor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setIsConstructor

    Parameters
    ----------

    isConstructor : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaMethod::setIsConstructor(bool isConstructor)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod16setIsConstructorEb', isConstructor,
    )

  @overload(bool)
  def setIsJavaScriptFunction(self, isJavaScriptFunction: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setIsJavaScriptFunction(bool
    isJavaScriptFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setIsJavaScriptFunction

    Parameters
    ----------

    isJavaScriptFunction : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaMethod::setIsJavaScriptFunction(bool
    #      isJavaScriptFunction)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod23setIsJavaScriptFunctionEb',
        isJavaScriptFunction,
    )

  @overload(bool)
  def setIsImplicitQmlPropertyChangeSignal(
      self,
      isPropertyChangeSignal: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaMethod::setIsImplicitQmlPropertyChangeSignal(bool
    isPropertyChangeSignal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html

    Parameters
    ----------

    isPropertyChangeSignal : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaMethod::setIsImplicitQmlPropertyChangeSignal(bool
    #      isPropertyChangeSignal)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod36setIsImplicitQmlPropertyChangeSignalE'
        'b',
        isPropertyChangeSignal,
    )

  @overload(bool)
  def setIsConst(self, isConst: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setIsConst(bool isConst)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#setIsConst

    Parameters
    ----------

    isConst : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaMethod::setIsConst(bool isConst)
    self.uglySide.call('ritual_ZN16QQmlJSMetaMethod10setIsConstEb', isConst)

  @overload(QList[QQmlJSAnnotation])
  def setAnnotations(self, annotations: QList[QQmlJSAnnotation]) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setAnnotations(QList<QQmlJSAnnotation>
    annotations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setAnnotations

    Parameters
    ----------

    annotations : QList[QQmlJSAnnotation]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSMetaMethod::setAnnotations(QList<QQmlJSAnnotation>
    #      annotations)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod14setAnnotationsE5QListI16QQmlJSAnnotat'
        'ionE',
        self._valueOf(annotations),
    )

  @overload(RelativeFunctionIndex)
  def setJsFunctionIndex(self, index: RelativeFunctionIndex) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaMethod::setJsFunctionIndex(RelativeFunctionIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setJsFunctionIndex

    Parameters
    ----------

    index : RelativeFunctionIndex
      Passed on as its number.
    """
    #  void QQmlJSMetaMethod::setJsFunctionIndex(RelativeFunctionIndex index)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod18setJsFunctionIndexENS_21RelativeFunct'
        'ionIndexE',
        index.value,
    )

  @overload(RelativeFunctionIndex)
  def setConstructorIndex(self, index: RelativeFunctionIndex) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaMethod::setConstructorIndex(RelativeFunctionIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setConstructorIndex

    Parameters
    ----------

    index : RelativeFunctionIndex
      Passed on as its number.
    """
    #  void QQmlJSMetaMethod::setConstructorIndex(RelativeFunctionIndex
    #      index)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod19setConstructorIndexENS_21RelativeFunc'
        'tionIndexE',
        index.value,
    )

  @overload(RelativeFunctionIndex)
  def setMethodIndex(self, index: RelativeFunctionIndex) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::setMethodIndex(RelativeFunctionIndex
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setMethodIndex

    Parameters
    ----------

    index : RelativeFunctionIndex
      Passed on as its number.
    """
    #  void QQmlJSMetaMethod::setMethodIndex(RelativeFunctionIndex index)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod14setMethodIndexENS_21RelativeFunctionI'
        'ndexE',
        index.value,
    )

  @overload(RelativeFunctionIndex)
  def setOtherMethodIndex(self, index: RelativeFunctionIndex) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaMethod::setOtherMethodIndex(RelativeFunctionIndex index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#setOtherMethodIndex

    Parameters
    ----------

    index : RelativeFunctionIndex
      Passed on as its number.
    """
    #  void QQmlJSMetaMethod::setOtherMethodIndex(RelativeFunctionIndex
    #      index)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod19setOtherMethodIndexENS_21RelativeFunc'
        'tionIndexE',
        index.value,
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
    Notes what was given, for Qt's 'QQmlJSMetaMethod::QQmlJSMetaMethod()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#QQmlJSMetaMethod
    """
    #  QQmlJSMetaMethod::QQmlJSMetaMethod()
    self._noteCreation(QQmlJSMetaMethod, lambda: Rituals.call(
        'ritual_ZN16QQmlJSMetaMethodC1Ev',
    ))

  @overload(str)
  @overload(str, str)
  def __init__(self, name: str, returnType: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSMetaMethod::QQmlJSMetaMethod(QString name, QString returnType)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetamethod.html#QQmlJSMetaMethod

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    returnType : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QQmlJSMetaMethod::QQmlJSMetaMethod(QString name, QString returnType)
    self._noteCreation(QQmlJSMetaMethod, lambda: Rituals.call(
        'ritual_ZN16QQmlJSMetaMethodC1E7QStringS0_', name, returnType,
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

  @overload(QQmlJSMetaParameter)
  def addParameter(self, p: QQmlJSMetaParameter) -> None:
    """
    Calls Qt's 'void QQmlJSMetaMethod::addParameter(const QQmlJSMetaParameter
    &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsmetamethod.html#addParameter

    Parameters
    ----------

    p : QQmlJSMetaParameter
      Passed on as a value: Qt reads the C++ QQmlJSMetaParameter, which stays
      Python's own.
    """
    #  void QQmlJSMetaMethod::addParameter(const QQmlJSMetaParameter &p)
    self.uglySide.call(
        'ritual_ZN16QQmlJSMetaMethod12addParameterERK19QQmlJSMetaParameter',
        self._valueOf(p),
    )

  @staticmethod
  def mutableParametersRange(*__, **_) -> Never:
    """
    Qt's 'std::pair<QList<QQmlJSMetaParameter>::iterator,
    QList<QQmlJSMetaParameter>::iterator>
    QQmlJSMetaMethod::mutableParametersRange()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaMethod.mutableParametersRange' has no cute function "
        "yet. Qt's 'std::pair<QList<QQmlJSMetaParameter>::iterator, "
        "QList<QQmlJSMetaParameter>::iterator> "
        "QQmlJSMetaMethod::mutableParametersRange()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def returnType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope> QQmlJSMetaMethod::returnType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaMethod.returnType' has no cute function yet. Qt's "
        "'QSharedPointer<const QQmlJSScope> QQmlJSMetaMethod::returnType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setReturnType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaMethod::setReturnType(QWeakPointer<const
    QQmlJSScope> type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaMethod.setReturnType' has no cute function yet. Qt's "
        "'void QQmlJSMetaMethod::setReturnType(QWeakPointer<const "
        "QQmlJSScope> type)': takes a type Python has no way to hand over "
        "yet.")


#  Qt's 'QList<QQmlJSMetaMethod>': the list of QQmlJSMetaMethod, which
#  'QList[QQmlJSMetaMethod]' gives. It is made here, so that there is one as
#  soon as there can be a QQmlJSMetaMethod.
QList.createKind(
    QQmlJSMetaMethod, 'value',
    make='ritual_list_make_QQmlJSMetaMethod',
    add='ritual_list_add_QQmlJSMetaMethod',
    size='ritual_list_size_QQmlJSMetaMethod',
    at='ritual_list_at_QQmlJSMetaMethod',
    drop='ritual_list_drop_QQmlJSMetaMethod',
)


#  Qt's 'QHash<QString, QQmlJSMetaMethod>': the QHash from text to
#  QQmlJSMetaMethod, which 'QHash[str, QQmlJSMetaMethod]' gives. It is
#  completed here, in the file of the class of its values.
QHash.createKind(
    str, QQmlJSMetaMethod, 'value',
    make='ritual_map_make_QHash_QString_QQmlJSMetaMethod',
    put='ritual_map_put_QHash_QString_QQmlJSMetaMethod',
    size='ritual_map_size_QHash_QString_QQmlJSMetaMethod',
    key='ritual_map_key_QHash_QString_QQmlJSMetaMethod',
    value='ritual_map_value_QHash_QString_QQmlJSMetaMethod',
    has='ritual_map_has_QHash_QString_QQmlJSMetaMethod',
    get='ritual_map_get_QHash_QString_QQmlJSMetaMethod',
    drop='ritual_map_drop_QHash_QString_QQmlJSMetaMethod',
)
