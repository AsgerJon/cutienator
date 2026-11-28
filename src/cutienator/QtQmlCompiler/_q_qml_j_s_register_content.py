"""
QQmlJSRegisterContent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSRegisterContent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QQmlJSMetaEnum, QQmlJSMetaMethod, QQmlJSMetaProperty


class QQmlJSRegisterContent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSRegisterContent: a plain Python object standing
  in front of one C++ QQmlJSRegisterContent.

  C++ hands a QQmlJSRegisterContent around as a copy, so every C++
  QQmlJSRegisterContent behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSRegisterContent that has a ritual and that
  Python can call so far, 34 names in all: 'isNull', 'isValid', 'isList',
  'isWritable', 'variant', 'descriptiveName', 'containedTypeName',
  'resultLookupIndex', 'isType', 'isProperty', 'property', 'baseLookupIndex',
  'isEnumeration', 'enumeration', 'enumMember', 'isMethod', 'method',
  'isImportNamespace', 'importNamespace', 'isConversion',
  'conversionResultScope', 'conversionOrigins', 'isMethodCall', 'methodCall',
  'isJavaScriptReturnValue', 'attacher', 'attachee', 'scope', 'storage',
  'original', 'shadowed', 'id', '__eq__', '__ne__'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::storedType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::containedType()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::scopeType() const':
    gives a type Python has no way to take yet.
  - Qt's 'bool QQmlJSRegisterContent::contains(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSRegisterContent::isStoredIn(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::type() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::methodType() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::importNamespaceType()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::conversionResultType()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlJSRegisterContent::QQmlJSRegisterContent(
    QQmlJSRegisterContentPrivate *dd)': names 'QQmlJSRegisterContentPrivate',
    which has no cute class yet.
  - Qt's 'QQmlJSRegisterContent::~QQmlJSRegisterContent()': the destructor:
    Python removes its C++ QQmlJSRegisterContent by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlJSRegisterContent is created at the first use, not by
    'QQmlJSRegisterContent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSRegisterContent back gives a copy the ritual
    made for Python, in a new cute QQmlJSRegisterContent.
  - Each name of Qt's QQmlJSRegisterContent that has no cute function yet,
    'containedType', 'contains', 'conversionResultType',
    'importNamespaceType', 'isStoredIn', 'methodType', 'scopeType',
    'storedType', 'type', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSRegisterContent, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ContentVariant(CuteNum):
    """
    The enum 'QQmlJSRegisterContent::ContentVariant' of Qt, with the 22 names
    Qt gives in it.
    """

    ObjectById = Kee[int](0)
    TypeByName = Kee[int](1)
    Singleton = Kee[int](2)
    Script = Kee[int](3)
    MetaType = Kee[int](4)
    Extension = Kee[int](5)
    ScopeObject = Kee[int](6)
    ParentScope = Kee[int](7)
    Property = Kee[int](8)
    Method = Kee[int](9)
    Enum = Kee[int](10)
    Attachment = Kee[int](11)
    ModulePrefix = Kee[int](12)
    MethodCall = Kee[int](13)
    ListValue = Kee[int](14)
    ListIterator = Kee[int](15)
    Literal = Kee[int](16)
    Operation = Kee[int](17)
    BaseType = Kee[int](18)
    Cast = Kee[int](19)
    Storage = Kee[int](20)
    Unknown = Kee[int](21)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSRegisterContent'

  #  Qt's '~QQmlJSRegisterContent()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJSRegisterContent behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQmlJSRegisterContentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#isNull
    """
    #  bool QQmlJSRegisterContent::isNull() const
    return self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent6isNullEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#isValid
    """
    #  bool QQmlJSRegisterContent::isValid() const
    return self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent7isValidEv')

  def isList(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#isList
    """
    #  bool QQmlJSRegisterContent::isList() const
    return self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent6isListEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isWritable
    """
    #  bool QQmlJSRegisterContent::isWritable() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent10isWritableEv',
    )

  def variant(self) -> ContentVariant:
    """
    Calls Qt's 'ContentVariant QQmlJSRegisterContent::variant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#variant

    Returns
    -------

    ContentVariant
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ContentVariant(number)'
      gives.
    """
    #  ContentVariant QQmlJSRegisterContent::variant() const
    return QQmlJSRegisterContent.ContentVariant(self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent7variantEv',
    ))

  def descriptiveName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSRegisterContent::descriptiveName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#descriptiveName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSRegisterContent::descriptiveName() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent15descriptiveNameEv',
    )

  def containedTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlJSRegisterContent::containedTypeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#containedTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSRegisterContent::containedTypeName() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent17containedTypeNameEv',
    )

  def resultLookupIndex(self) -> int:
    """
    Calls Qt's 'int QQmlJSRegisterContent::resultLookupIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#resultLookupIndex
    """
    #  int QQmlJSRegisterContent::resultLookupIndex() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent17resultLookupIndexEv',
    )

  def isType(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#isType
    """
    #  bool QQmlJSRegisterContent::isType() const
    return self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent6isTypeEv')

  def isProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isProperty
    """
    #  bool QQmlJSRegisterContent::isProperty() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent10isPropertyEv',
    )

  def property(self) -> QQmlJSMetaProperty:
    """
    Calls Qt's 'QQmlJSMetaProperty QQmlJSRegisterContent::property() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#property

    Returns
    -------

    QQmlJSMetaProperty
      A new cute QQmlJSMetaProperty around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaProperty QQmlJSRegisterContent::property() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent8propertyEv',
    )
    from . import QQmlJSMetaProperty
    return QQmlJSMetaProperty._cuteOwning(address)

  def baseLookupIndex(self) -> int:
    """
    Calls Qt's 'int QQmlJSRegisterContent::baseLookupIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#baseLookupIndex
    """
    #  int QQmlJSRegisterContent::baseLookupIndex() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent15baseLookupIndexEv',
    )

  def isEnumeration(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isEnumeration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isEnumeration
    """
    #  bool QQmlJSRegisterContent::isEnumeration() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent13isEnumerationEv',
    )

  def enumeration(self) -> QQmlJSMetaEnum:
    """
    Calls Qt's 'QQmlJSMetaEnum QQmlJSRegisterContent::enumeration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#enumeration

    Returns
    -------

    QQmlJSMetaEnum
      A new cute QQmlJSMetaEnum around the copy Qt gave back. Python owns it.
    """
    #  QQmlJSMetaEnum QQmlJSRegisterContent::enumeration() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent11enumerationEv',
    )
    from . import QQmlJSMetaEnum
    return QQmlJSMetaEnum._cuteOwning(address)

  def enumMember(self) -> str:
    """
    Calls Qt's 'QString QQmlJSRegisterContent::enumMember() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#enumMember

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSRegisterContent::enumMember() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent10enumMemberEv',
    )

  def isMethod(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isMethod
    """
    #  bool QQmlJSRegisterContent::isMethod() const
    return self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent8isMethodEv')

  def method(self) -> QList[QQmlJSMetaMethod]:
    """
    Calls Qt's 'QList<QQmlJSMetaMethod> QQmlJSRegisterContent::method()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#method

    Returns
    -------

    QList[QQmlJSMetaMethod]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSMetaMethod> QQmlJSRegisterContent::method() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent6methodEv',
    )
    from . import QQmlJSMetaMethod
    return QList[QQmlJSMetaMethod]._cuteOwning(address)

  def isImportNamespace(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isImportNamespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isImportNamespace
    """
    #  bool QQmlJSRegisterContent::isImportNamespace() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent17isImportNamespaceEv',
    )

  def importNamespace(self) -> int:
    """
    Calls Qt's 'uint QQmlJSRegisterContent::importNamespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#importNamespace
    """
    #  uint QQmlJSRegisterContent::importNamespace() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent15importNamespaceEv',
    )

  def isConversion(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isConversion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isConversion
    """
    #  bool QQmlJSRegisterContent::isConversion() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent12isConversionEv',
    )

  def conversionResultScope(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContent::conversionResultScope() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#conversionResultScope

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::conversionResultScope()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent21conversionResultScopeEv',
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def conversionOrigins(self) -> QList[QQmlJSRegisterContent]:
    """
    Calls Qt's 'const QList<QQmlJSRegisterContent>
    &QQmlJSRegisterContent::conversionOrigins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#conversionOrigins

    Returns
    -------

    QList[QQmlJSRegisterContent]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QQmlJSRegisterContent>
    #      &QQmlJSRegisterContent::conversionOrigins() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent17conversionOriginsEv',
    )
    return QList[QQmlJSRegisterContent]._cuteOwning(address)

  def isMethodCall(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isMethodCall() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isMethodCall
    """
    #  bool QQmlJSRegisterContent::isMethodCall() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent12isMethodCallEv',
    )

  def methodCall(self) -> QQmlJSMetaMethod:
    """
    Calls Qt's 'QQmlJSMetaMethod QQmlJSRegisterContent::methodCall() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#methodCall

    Returns
    -------

    QQmlJSMetaMethod
      A new cute QQmlJSMetaMethod around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSMetaMethod QQmlJSRegisterContent::methodCall() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent10methodCallEv',
    )
    from . import QQmlJSMetaMethod
    return QQmlJSMetaMethod._cuteOwning(address)

  def isJavaScriptReturnValue(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSRegisterContent::isJavaScriptReturnValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#isJavaScriptReturnValue
    """
    #  bool QQmlJSRegisterContent::isJavaScriptReturnValue() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent23isJavaScriptReturnValueEv',
    )

  def attacher(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSRegisterContent::attacher()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#attacher

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::attacher() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent8attacherEv',
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def attachee(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSRegisterContent::attachee()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#attachee

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::attachee() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent8attacheeEv',
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def scope(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSRegisterContent::scope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#scope

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::scope() const
    address = self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent5scopeEv')
    return QQmlJSRegisterContent._cuteOwning(address)

  def storage(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSRegisterContent::storage()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#storage

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::storage() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent7storageEv',
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def original(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSRegisterContent::original()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#original

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::original() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent8originalEv',
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def shadowed(self) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent QQmlJSRegisterContent::shadowed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#shadowed

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContent::shadowed() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlJSRegisterContent8shadowedEv',
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def id(self) -> int:
    """
    Calls Qt's 'quintptr QQmlJSRegisterContent::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsregistercontent.html#id
    """
    #  quintptr QQmlJSRegisterContent::id() const
    return self.uglySide.call('ritual_ZNK21QQmlJSRegisterContent2idEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool operator==(QQmlJSRegisterContent a,
    QQmlJSRegisterContent b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#operator==

    Parameters
    ----------

    b : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool operator==(QQmlJSRegisterContent a, QQmlJSRegisterContent b)
    return Rituals.call(
        'ritual_Zeq21QQmlJSRegisterContentS_',
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
  def __ne__(self, b: QQmlJSRegisterContent) -> bool:
    """
    Calls Qt's 'bool operator!=(QQmlJSRegisterContent a,
    QQmlJSRegisterContent b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#operator!=

    Parameters
    ----------

    b : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.
    """
    #  bool operator!=(QQmlJSRegisterContent a, QQmlJSRegisterContent b)
    return Rituals.call(
        'ritual_Zne21QQmlJSRegisterContentS_',
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
    'QQmlJSRegisterContent::QQmlJSRegisterContent()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontent.html#QQmlJSRegisterContent
    """
    #  QQmlJSRegisterContent::QQmlJSRegisterContent()
    self._noteCreation(QQmlJSRegisterContent, lambda: Rituals.call(
        'ritual_ZN21QQmlJSRegisterContentC1Ev',
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

  @staticmethod
  def containedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::containedType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.containedType' has no cute function yet. "
        "Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::containedType() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def contains(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSRegisterContent::contains(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.contains' has no cute function yet. Qt's "
        "'bool QQmlJSRegisterContent::contains(const QQmlJSScope::ConstPtr "
        "&type) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def conversionResultType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::conversionResultType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.conversionResultType' has no cute function "
        "yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSRegisterContent::conversionResultType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def importNamespaceType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::importNamespaceType()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.importNamespaceType' has no cute function "
        "yet. Qt's 'QQmlJSScope::ConstPtr "
        "QQmlJSRegisterContent::importNamespaceType() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def isStoredIn(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSRegisterContent::isStoredIn(const QQmlJSScope::ConstPtr
    &type) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.isStoredIn' has no cute function yet. Qt's "
        "'bool QQmlJSRegisterContent::isStoredIn(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def methodType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::methodType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.methodType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSRegisterContent::methodType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def scopeType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::scopeType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.scopeType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSRegisterContent::scopeType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def storedType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::storedType() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.storedType' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSRegisterContent::storedType() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def type(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSRegisterContent::type() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContent.type' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSRegisterContent::type() const': gives "
        "a type Python has no way to take yet.")


#  Qt's 'QList<QQmlJSRegisterContent>': the list of QQmlJSRegisterContent,
#  which 'QList[QQmlJSRegisterContent]' gives. It is made here, so that there
#  is one as soon as there can be a QQmlJSRegisterContent.
QList.createKind(
    QQmlJSRegisterContent, 'value',
    make='ritual_list_make_QQmlJSRegisterContent',
    add='ritual_list_add_QQmlJSRegisterContent',
    size='ritual_list_size_QQmlJSRegisterContent',
    at='ritual_list_at_QQmlJSRegisterContent',
    drop='ritual_list_drop_QQmlJSRegisterContent',
)
