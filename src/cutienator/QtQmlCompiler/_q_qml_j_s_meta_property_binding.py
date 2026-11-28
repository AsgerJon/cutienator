"""
QQmlJSMetaPropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSMetaPropertyBinding to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QQmlJS
from . import QQmlSA, QQmlJSMetaMethod

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtQml import QQmlTranslation
  from . import QQmlJSMetaProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaProperty = WAIT['QQmlJSMetaProperty']


class QQmlJSMetaPropertyBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSMetaPropertyBinding: a plain Python object
  standing in front of one C++ QQmlJSMetaPropertyBinding.

  C++ hands a QQmlJSMetaPropertyBinding around as a copy, so every C++
  QQmlJSMetaPropertyBinding behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSMetaPropertyBinding that has a ritual and that
  Python can call so far, 30 names in all: 'ensureSetBindingTypeOnce',
  'isLiteralBinding', 'setPropertyName', 'propertyName', 'sourceLocation',
  'bindingType', 'isValid', 'setStringLiteral', 'setBoolLiteral',
  'setNullLiteral', 'setNumberLiteral', 'setRegexpLiteral', 'setTranslation',
  'setTranslationId', 'boolValue', 'numberValue', 'stringValue',
  'regExpValue', 'translationDataValue', 'scriptIndex', 'scriptKind',
  'objectTypeName', 'interceptorTypeName', 'valueSourceTypeName',
  'hasLiteral', 'hasObject', 'hasInterceptor', 'hasValueSource', '__eq__',
  '__ne__'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJSMetaPropertyBinding::setScriptBinding(QQmlJSMetaMethod::
    RelativeFunctionIndex value, ScriptBindingKind kind,
    ScriptBindingValueType valueType)': names the enum
    'ScriptBindingValueType', whose class cannot be named here.
  - Qt's 'void QQmlJSMetaPropertyBinding::setGroupBinding(const
    QSharedPointer<const QQmlJSScope> &groupScope)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlJSMetaPropertyBinding::setAttachedBinding(const
    QSharedPointer<const QQmlJSScope> &attachingScope)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QQmlJSMetaPropertyBinding::setObject(const QString &typeName,
    const QSharedPointer<const QQmlJSScope> &type)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlJSMetaPropertyBinding::setInterceptor(const QString
    &typeName, const QSharedPointer<const QQmlJSScope> &type)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlJSMetaPropertyBinding::setValueSource(const QString
    &typeName, const QSharedPointer<const QQmlJSScope> &type)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::literalType(const QQmlJSTypeResolver
    *resolver) const': gives a type Python has no way to take yet.
  - Qt's 'ScriptBindingValueType QQmlJSMetaPropertyBinding::scriptValueType()
    const': gives the enum 'ScriptBindingValueType', whose class cannot be
    named here.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::objectType() const': gives a type Python has
    no way to take yet.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::interceptorType() const': gives a type Python
    has no way to take yet.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::valueSourceType() const': gives a type Python
    has no way to take yet.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::groupType() const': gives a type Python has no
    way to take yet.
  - Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::attachedType() const': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlJSMetaPropertyBinding::~QQmlJSMetaPropertyBinding()': the
    destructor: Python removes its C++ QQmlJSMetaPropertyBinding by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSMetaPropertyBinding is created at the first use, not by
    'QQmlJSMetaPropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSMetaPropertyBinding back gives a copy the
    ritual made for Python, in a new cute QQmlJSMetaPropertyBinding.
  - Each name of Qt's QQmlJSMetaPropertyBinding that has no cute function
    yet, 'attachedType', 'groupType', 'interceptorType', 'literalType',
    'objectType', 'scriptValueType', 'setAttachedBinding', 'setGroupBinding',
    'setInterceptor', 'setObject', 'setScriptBinding', 'setValueSource',
    'valueSourceType', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSMetaPropertyBinding'

  #  Qt's '~QQmlJSMetaPropertyBinding()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJSMetaPropertyBinding behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QQmlJSMetaPropertyBindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def isLiteralBinding(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::isLiteralBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#isLiteralBinding
    """
    #  bool QQmlJSMetaPropertyBinding::isLiteralBinding() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding16isLiteralBindingEv',
    )

  @staticmethod
  @overload(QQmlSA.BindingType)
  def isLiteralBinding(type: QQmlSA.BindingType) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::isLiteralBinding(BindingType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#isLiteralBinding

    Parameters
    ----------

    type : QQmlSA.BindingType
      Passed on as its number.
    """
    #  bool QQmlJSMetaPropertyBinding::isLiteralBinding(BindingType type)
    return Rituals.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding16isLiteralBindingEN6QQmlSA11B'
        'indingTypeE',
        type.value,
    )

  def propertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaPropertyBinding::propertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaPropertyBinding::propertyName() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding12propertyNameEv',
    )

  def sourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'const QQmlJS::SourceLocation
    &QQmlJSMetaPropertyBinding::sourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#sourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  const QQmlJS::SourceLocation
    #      &QQmlJSMetaPropertyBinding::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding14sourceLocationEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def bindingType(self) -> QQmlSA.BindingType:
    """
    Calls Qt's 'BindingType QQmlJSMetaPropertyBinding::bindingType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#bindingType

    Returns
    -------

    QQmlSA.BindingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.BindingType(number)' gives.
    """
    #  BindingType QQmlJSMetaPropertyBinding::bindingType() const
    return QQmlSA.BindingType(self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding11bindingTypeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#isValid
    """
    #  bool QQmlJSMetaPropertyBinding::isValid() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding7isValidEv',
    )

  def boolValue(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::boolValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#boolValue
    """
    #  bool QQmlJSMetaPropertyBinding::boolValue() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding9boolValueEv',
    )

  def numberValue(self) -> float:
    """
    Calls Qt's 'double QQmlJSMetaPropertyBinding::numberValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#numberValue
    """
    #  double QQmlJSMetaPropertyBinding::numberValue() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding11numberValueEv',
    )

  def stringValue(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaPropertyBinding::stringValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#stringValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaPropertyBinding::stringValue() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding11stringValueEv',
    )

  def regExpValue(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaPropertyBinding::regExpValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#regExpValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaPropertyBinding::regExpValue() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding11regExpValueEv',
    )

  @overload()
  @overload(str)
  def translationDataValue(
      self,
      qmlFileNameForContext: str = '',
  ) -> QQmlTranslation:
    """
    Calls Qt's 'QQmlTranslation
    QQmlJSMetaPropertyBinding::translationDataValue(QString
    qmlFileNameForContext) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html

    Parameters
    ----------

    qmlFileNameForContext : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QQmlTranslation
      A new cute QQmlTranslation around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlTranslation
    #      QQmlJSMetaPropertyBinding::translationDataValue(QString
    #      qmlFileNameForContext) const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding20translationDataValueE7QStri'
        'ng',
        qmlFileNameForContext,
    )
    from ..QtQml import QQmlTranslation
    return QQmlTranslation._cuteOwning(address)

  def scriptIndex(self) -> QQmlJSMetaMethod.RelativeFunctionIndex:
    """
    Calls Qt's 'QQmlJSMetaMethod::RelativeFunctionIndex
    QQmlJSMetaPropertyBinding::scriptIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#scriptIndex

    Returns
    -------

    QQmlJSMetaMethod.RelativeFunctionIndex
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlJSMetaMethod.RelativeFunctionIndex(number)' gives.
    """
    #  QQmlJSMetaMethod::RelativeFunctionIndex
    #      QQmlJSMetaPropertyBinding::scriptIndex() const
    return QQmlJSMetaMethod.RelativeFunctionIndex(self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding11scriptIndexEv',
    ))

  def scriptKind(self) -> QQmlSA.ScriptBindingKind:
    """
    Calls Qt's 'ScriptBindingKind QQmlJSMetaPropertyBinding::scriptKind()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#scriptKind

    Returns
    -------

    QQmlSA.ScriptBindingKind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.ScriptBindingKind(number)' gives.
    """
    #  ScriptBindingKind QQmlJSMetaPropertyBinding::scriptKind() const
    return QQmlSA.ScriptBindingKind(self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding10scriptKindEv',
    ))

  def objectTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaPropertyBinding::objectTypeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#objectTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaPropertyBinding::objectTypeName() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding14objectTypeNameEv',
    )

  def interceptorTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaPropertyBinding::interceptorTypeName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#interceptorTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaPropertyBinding::interceptorTypeName() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding19interceptorTypeNameEv',
    )

  def valueSourceTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSMetaPropertyBinding::valueSourceTypeName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#valueSourceTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSMetaPropertyBinding::valueSourceTypeName() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding19valueSourceTypeNameEv',
    )

  def hasLiteral(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::hasLiteral() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#hasLiteral
    """
    #  bool QQmlJSMetaPropertyBinding::hasLiteral() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding10hasLiteralEv',
    )

  def hasObject(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::hasObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#hasObject
    """
    #  bool QQmlJSMetaPropertyBinding::hasObject() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding9hasObjectEv',
    )

  def hasInterceptor(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::hasInterceptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#hasInterceptor
    """
    #  bool QQmlJSMetaPropertyBinding::hasInterceptor() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding14hasInterceptorEv',
    )

  def hasValueSource(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSMetaPropertyBinding::hasValueSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#hasValueSource
    """
    #  bool QQmlJSMetaPropertyBinding::hasValueSource() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlJSMetaPropertyBinding14hasValueSourceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPropertyName(self, propertyName: str) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::setPropertyName(const QString
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setPropertyName

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaPropertyBinding::setPropertyName(const QString
    #      &propertyName)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding15setPropertyNameERK7QString',
        propertyName,
    )

  @overload(str)
  def setStringLiteral(self, value: str) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaPropertyBinding::setStringLiteral(QAnyStringView value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setStringLiteral

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaPropertyBinding::setStringLiteral(QAnyStringView value)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding16setStringLiteralE14QAnyStrin'
        'gView',
        value,
    )

  @overload(bool)
  def setBoolLiteral(self, value: bool) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::setBoolLiteral(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setBoolLiteral

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QQmlJSMetaPropertyBinding::setBoolLiteral(bool value)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding14setBoolLiteralEb', value,
    )

  def setNullLiteral(self) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::setNullLiteral()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setNullLiteral
    """
    #  void QQmlJSMetaPropertyBinding::setNullLiteral()
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding14setNullLiteralEv',
    )

  @overload(float)
  def setNumberLiteral(self, value: float) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::setNumberLiteral(double
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setNumberLiteral

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQmlJSMetaPropertyBinding::setNumberLiteral(double value)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding16setNumberLiteralEd', value,
    )

  @overload(str)
  def setRegexpLiteral(self, value: str) -> None:
    """
    Calls Qt's 'void
    QQmlJSMetaPropertyBinding::setRegexpLiteral(QAnyStringView value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setRegexpLiteral

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSMetaPropertyBinding::setRegexpLiteral(QAnyStringView value)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding16setRegexpLiteralE14QAnyStrin'
        'gView',
        value,
    )

  @overload(str, str, str, int)
  def setTranslation(
      self,
      text: str,
      comment: str,
      context: str,
      number: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::setTranslation(QStringView
    text, QStringView comment, QStringView context, int number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setTranslation

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    comment : str
      Passed on as it is: a QString is made of it for the call.

    context : str
      Passed on as it is: a QString is made of it for the call.

    number : int
      Passed on as it is.
    """
    #  void QQmlJSMetaPropertyBinding::setTranslation(QStringView text,
    #      QStringView comment, QStringView context, int number)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding14setTranslationE11QStringView'
        'S0_S0_i',
        text, comment, context, number,
    )

  @overload(str, int)
  def setTranslationId(self, id: str, number: int) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::setTranslationId(QStringView
    id, int number)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#setTranslationId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    number : int
      Passed on as it is.
    """
    #  void QQmlJSMetaPropertyBinding::setTranslationId(QStringView id, int
    #      number)
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding16setTranslationIdE11QStringVi'
        'ewi',
        id, number,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlJSMetaPropertyBinding) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlJSMetaPropertyBinding &a, const
    QQmlJSMetaPropertyBinding &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#operator==

    Parameters
    ----------

    b : QQmlJSMetaPropertyBinding
      Passed on as a value: Qt reads the C++ QQmlJSMetaPropertyBinding, which
      stays Python's own.
    """
    #  bool operator==(const QQmlJSMetaPropertyBinding &a, const
    #      QQmlJSMetaPropertyBinding &b)
    return Rituals.call(
        'ritual_ZeqRK25QQmlJSMetaPropertyBindingS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QQmlJSMetaPropertyBinding) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlJSMetaPropertyBinding &a, const
    QQmlJSMetaPropertyBinding &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html#operator!=

    Parameters
    ----------

    b : QQmlJSMetaPropertyBinding
      Passed on as a value: Qt reads the C++ QQmlJSMetaPropertyBinding, which
      stays Python's own.
    """
    #  bool operator!=(const QQmlJSMetaPropertyBinding &a, const
    #      QQmlJSMetaPropertyBinding &b)
    return Rituals.call(
        'ritual_ZneRK25QQmlJSMetaPropertyBindingS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html
    """
    #  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding()
    self._noteCreation(QQmlJSMetaPropertyBinding, lambda: Rituals.call(
        'ritual_ZN25QQmlJSMetaPropertyBindingC1Ev',
    ))

  @overload(WAIT['QQmlJS.SourceLocation'])
  def __init__(self, location: QQmlJS.SourceLocation) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::
    SourceLocation location)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html

    Parameters
    ----------

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::
    #      SourceLocation location)
    self._noteCreation(QQmlJSMetaPropertyBinding, lambda: Rituals.call(
        'ritual_ZN25QQmlJSMetaPropertyBindingC1EN6QQmlJS14SourceLocationE',
        self._valueOf(location),
    ))

  @overload(WAIT['QQmlJS.SourceLocation'], str)
  def __init__(self, location: QQmlJS.SourceLocation, propName: str) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::
    SourceLocation location, const QString &propName)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html

    Parameters
    ----------

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    propName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::
    #      SourceLocation location, const QString &propName)
    self._noteCreation(QQmlJSMetaPropertyBinding, lambda: Rituals.call(
        'ritual_ZN25QQmlJSMetaPropertyBindingC1EN6QQmlJS14SourceLocationERK'
        '7QString',
        self._valueOf(location), propName,
    ))

  @overload(WAIT['QQmlJS.SourceLocation'], QQmlJSMetaProperty)
  def __init__(
      self,
      location: QQmlJS.SourceLocation,
      prop: QQmlJSMetaProperty,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::
    SourceLocation location, const QQmlJSMetaProperty &prop)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html

    Parameters
    ----------

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    prop : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.
    """
    #  QQmlJSMetaPropertyBinding::QQmlJSMetaPropertyBinding(QQmlJS::
    #      SourceLocation location, const QQmlJSMetaProperty &prop)
    self._noteCreation(QQmlJSMetaPropertyBinding, lambda: Rituals.call(
        'ritual_ZN25QQmlJSMetaPropertyBindingC1EN6QQmlJS14SourceLocationERK'
        '18QQmlJSMetaProperty',
        self._valueOf(location), self._valueOf(prop),
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

  def ensureSetBindingTypeOnce(self) -> None:
    """
    Calls Qt's 'void QQmlJSMetaPropertyBinding::ensureSetBindingTypeOnce()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsmetapropertybinding.html
    """
    #  void QQmlJSMetaPropertyBinding::ensureSetBindingTypeOnce()
    self.uglySide.call(
        'ritual_ZN25QQmlJSMetaPropertyBinding24ensureSetBindingTypeOnceEv',
    )

  @staticmethod
  def attachedType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::attachedType() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.attachedType' has no cute function yet. "
        "Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaPropertyBinding::attachedType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def groupType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::groupType() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.groupType' has no cute function yet. "
        "Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaPropertyBinding::groupType() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def interceptorType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::interceptorType() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.interceptorType' has no cute function "
        "yet. Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaPropertyBinding::interceptorType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def literalType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::literalType(const QQmlJSTypeResolver
    *resolver) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.literalType' has no cute function yet. "
        "Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaPropertyBinding::literalType(const QQmlJSTypeResolver "
        "*resolver) const': gives a type Python has no way to take yet.")

  @staticmethod
  def objectType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::objectType() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.objectType' has no cute function yet. "
        "Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaPropertyBinding::objectType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def scriptValueType(*__, **_) -> Never:
    """
    Qt's 'ScriptBindingValueType QQmlJSMetaPropertyBinding::scriptValueType()
    const': gives the enum 'ScriptBindingValueType', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.scriptValueType' has no cute function "
        "yet. Qt's 'ScriptBindingValueType "
        "QQmlJSMetaPropertyBinding::scriptValueType() const': gives the "
        "enum 'ScriptBindingValueType', whose class cannot be named here.")

  @staticmethod
  def setAttachedBinding(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaPropertyBinding::setAttachedBinding(const
    QSharedPointer<const QQmlJSScope> &attachingScope)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.setAttachedBinding' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSMetaPropertyBinding::setAttachedBinding(const "
        "QSharedPointer<const QQmlJSScope> &attachingScope)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setGroupBinding(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaPropertyBinding::setGroupBinding(const
    QSharedPointer<const QQmlJSScope> &groupScope)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.setGroupBinding' has no cute function "
        "yet. Qt's 'void QQmlJSMetaPropertyBinding::setGroupBinding(const "
        "QSharedPointer<const QQmlJSScope> &groupScope)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setInterceptor(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaPropertyBinding::setInterceptor(const QString
    &typeName, const QSharedPointer<const QQmlJSScope> &type)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.setInterceptor' has no cute function "
        "yet. Qt's 'void QQmlJSMetaPropertyBinding::setInterceptor(const "
        "QString &typeName, const QSharedPointer<const QQmlJSScope> "
        "&type)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setObject(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaPropertyBinding::setObject(const QString &typeName,
    const QSharedPointer<const QQmlJSScope> &type)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.setObject' has no cute function yet. "
        "Qt's 'void QQmlJSMetaPropertyBinding::setObject(const QString "
        "&typeName, const QSharedPointer<const QQmlJSScope> &type)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def setScriptBinding(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaPropertyBinding::setScriptBinding(QQmlJSMetaMethod::
    RelativeFunctionIndex value, ScriptBindingKind kind,
    ScriptBindingValueType valueType)': names the enum
    'ScriptBindingValueType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.setScriptBinding' has no cute function "
        "yet. Qt's 'void "
        "QQmlJSMetaPropertyBinding::setScriptBinding(QQmlJSMetaMethod::Relat"
        "iveFunctionIndex value, ScriptBindingKind kind, "
        "ScriptBindingValueType valueType)': names the enum "
        "'ScriptBindingValueType', whose class cannot be named here.")

  @staticmethod
  def setValueSource(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSMetaPropertyBinding::setValueSource(const QString
    &typeName, const QSharedPointer<const QQmlJSScope> &type)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.setValueSource' has no cute function "
        "yet. Qt's 'void QQmlJSMetaPropertyBinding::setValueSource(const "
        "QString &typeName, const QSharedPointer<const QQmlJSScope> "
        "&type)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def valueSourceType(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<const QQmlJSScope>
    QQmlJSMetaPropertyBinding::valueSourceType() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSMetaPropertyBinding.valueSourceType' has no cute function "
        "yet. Qt's 'QSharedPointer<const QQmlJSScope> "
        "QQmlJSMetaPropertyBinding::valueSourceType() const': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QQmlJSMetaPropertyBinding>': the list of
#  QQmlJSMetaPropertyBinding, which 'QList[QQmlJSMetaPropertyBinding]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QQmlJSMetaPropertyBinding.
QList.createKind(
    QQmlJSMetaPropertyBinding, 'value',
    make='ritual_list_make_QQmlJSMetaPropertyBinding',
    add='ritual_list_add_QQmlJSMetaPropertyBinding',
    size='ritual_list_size_QQmlJSMetaPropertyBinding',
    at='ritual_list_at_QQmlJSMetaPropertyBinding',
    drop='ritual_list_drop_QQmlJSMetaPropertyBinding',
)
