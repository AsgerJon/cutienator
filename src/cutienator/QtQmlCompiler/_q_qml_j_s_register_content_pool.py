"""
QQmlJSRegisterContentPool binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSRegisterContentPool to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlJSRegisterContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QQmlJSMetaEnum, QQmlJSMetaProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSMetaEnum = WAIT['QQmlJSMetaEnum']
  QQmlJSMetaProperty = WAIT['QQmlJSMetaProperty']


class QQmlJSRegisterContentPool(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSRegisterContentPool: a plain Python object
  standing in front of one C++ QQmlJSRegisterContentPool.

  What exists
  -----------

  Every function of Qt's QQmlJSRegisterContentPool that has a ritual and that
  Python can call so far, 5 names in all: 'createProperty',
  'createEnumeration', 'clone', 'setAllocationMode', 'clearTemporaries'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSRegisterContentPool::~QQmlJSRegisterContentPool()': the
    destructor: Python never removes a C++ QQmlJSRegisterContentPool.
  - Qt's 'QQmlJSRegisterContent QQmlJSRegisterContentPool::createType(const
    QQmlJSScope::ConstPtr &type, int resultLookupIndex, ContentVariant
    variant, QQmlJSRegisterContent scope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent QQmlJSRegisterContentPool::createMethod(const
    QList<QQmlJSMetaMethod> &methods, const QQmlJSScope::ConstPtr
    &methodType, ContentVariant variant, QQmlJSRegisterContent scope)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createMethodCall(const QQmlJSMetaMethod
    &method, const QQmlJSScope::ConstPtr &returnType, QQmlJSRegisterContent
    scope)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createImportNamespace(uint
    importNamespaceStringId, const QQmlJSScope::ConstPtr
    &importNamespaceType, ContentVariant variant, QQmlJSRegisterContent
    scope)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createConversion(const
    QList<QQmlJSRegisterContent> &origins, const QQmlJSScope::ConstPtr
    &conversion, QQmlJSRegisterContent conversionScope, ContentVariant
    variant, QQmlJSRegisterContent scope)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::storedIn(QQmlJSRegisterContent content, const
    QQmlJSScope::ConstPtr &newStoredType)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::castTo(QQmlJSRegisterContent content, const
    QQmlJSScope::ConstPtr &newContainedType)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QQmlJSRegisterContentPool::storeType(QQmlJSRegisterContent
    content, const QQmlJSScope::ConstPtr &stored)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlJSRegisterContentPool::adjustType(QQmlJSRegisterContent
    content, const QQmlJSScope::ConstPtr &adjusted)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QQmlJSRegisterContentPool::generalizeType(QQmlJSRegisterContent content,
    const QQmlJSScope::ConstPtr &generalized)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlJSRegisterContentPrivate
    *QQmlJSRegisterContentPool::clone(const QQmlJSRegisterContentPrivate
    *from)': names 'QQmlJSRegisterContentPrivate', which has no cute class
    yet.
  - Qt's 'QQmlJSRegisterContentPrivate *QQmlJSRegisterContentPool::create()':
    gives 'QQmlJSRegisterContentPrivate', which has no cute class yet.
  - Qt's 'QQmlJSRegisterContentPrivate
    *QQmlJSRegisterContentPool::create(QQmlJSRegisterContent scope,
    ContentVariant variant)': gives 'QQmlJSRegisterContentPrivate', which has
    no cute class yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlJSRegisterContentPool is created at the first use, not by
    'QQmlJSRegisterContentPool(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSRegisterContentPool.
  - Each name of Qt's QQmlJSRegisterContentPool that has no cute function
    yet, 'adjustType', 'castTo', 'create', 'createConversion',
    'createImportNamespace', 'createMethod', 'createMethodCall',
    'createType', 'generalizeType', 'storeType', 'storedIn', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSRegisterContentPool, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class AllocationMode(CuteNum):
    """
    The enum 'QQmlJSRegisterContentPool::AllocationMode' of Qt, with the 2
    names Qt gives in it.
    """

    Permanent = Kee[int](0)
    Temporary = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSRegisterContentPool'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(AllocationMode)
  def setAllocationMode(self, mode: AllocationMode) -> None:
    """
    Calls Qt's 'void
    QQmlJSRegisterContentPool::setAllocationMode(AllocationMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontentpool.html#setAllocationMode

    Parameters
    ----------

    mode : AllocationMode
      Passed on as its number.
    """
    #  void QQmlJSRegisterContentPool::setAllocationMode(AllocationMode mode)
    self.uglySide.call(
        'ritual_ZN25QQmlJSRegisterContentPool17setAllocationModeENS_14Alloc'
        'ationModeE',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSRegisterContentPool::QQmlJSRegisterContentPool()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontentpool.html
    """
    #  QQmlJSRegisterContentPool::QQmlJSRegisterContentPool()
    self._noteCreation(QQmlJSRegisterContentPool, lambda: Rituals.call(
        'ritual_ZN25QQmlJSRegisterContentPoolC1Ev',
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

  @overload(
      QQmlJSMetaProperty, int, int, QQmlJSRegisterContent.ContentVariant,
      QQmlJSRegisterContent,
  )
  def createProperty(
      self,
      property: QQmlJSMetaProperty,
      baseLookupIndex: int,
      resultLookupIndex: int,
      variant: QQmlJSRegisterContent.ContentVariant,
      scope: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createProperty(const QQmlJSMetaProperty
    &property, int baseLookupIndex, int resultLookupIndex, ContentVariant
    variant, QQmlJSRegisterContent scope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontentpool.html#createProperty

    Parameters
    ----------

    property : QQmlJSMetaProperty
      Passed on as a value: Qt reads the C++ QQmlJSMetaProperty, which stays
      Python's own.

    baseLookupIndex : int
      Passed on as it is.

    resultLookupIndex : int
      Passed on as it is.

    variant : QQmlJSRegisterContent.ContentVariant
      Passed on as its number.

    scope : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent QQmlJSRegisterContentPool::createProperty(const
    #      QQmlJSMetaProperty &property, int baseLookupIndex, int
    #      resultLookupIndex, ContentVariant variant, QQmlJSRegisterContent
    #      scope)
    address = self.uglySide.call(
        'ritual_ZN25QQmlJSRegisterContentPool14createPropertyERK18QQmlJSMet'
        'aPropertyiiN21QQmlJSRegisterContent14ContentVariantES3_',
        self._valueOf(property), baseLookupIndex, resultLookupIndex,
        variant.value, self._valueOf(scope),
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(
      QQmlJSMetaEnum, str, QQmlJSRegisterContent.ContentVariant,
      QQmlJSRegisterContent,
  )
  def createEnumeration(
      self,
      enumeration: QQmlJSMetaEnum,
      enumMember: str,
      variant: QQmlJSRegisterContent.ContentVariant,
      scope: QQmlJSRegisterContent,
  ) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createEnumeration(const QQmlJSMetaEnum
    &enumeration, const QString &enumMember, ContentVariant variant,
    QQmlJSRegisterContent scope)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontentpool.html#createEnumeration

    Parameters
    ----------

    enumeration : QQmlJSMetaEnum
      Passed on as a value: Qt reads the C++ QQmlJSMetaEnum, which stays
      Python's own.

    enumMember : str
      Passed on as it is: a QString is made of it for the call.

    variant : QQmlJSRegisterContent.ContentVariant
      Passed on as its number.

    scope : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSRegisterContentPool::createEnumeration(const QQmlJSMetaEnum
    #      &enumeration, const QString &enumMember, ContentVariant variant,
    #      QQmlJSRegisterContent scope)
    address = self.uglySide.call(
        'ritual_ZN25QQmlJSRegisterContentPool17createEnumerationERK14QQmlJS'
        'MetaEnumRK7QStringN21QQmlJSRegisterContent14ContentVariantES6_',
        self._valueOf(enumeration), enumMember, variant.value,
        self._valueOf(scope),
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  @overload(QQmlJSRegisterContent)
  def clone(self, from_: QQmlJSRegisterContent) -> QQmlJSRegisterContent:
    """
    Calls Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::clone(QQmlJSRegisterContent from)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontentpool.html#clone

    Parameters
    ----------

    from_ : QQmlJSRegisterContent
      Passed on as a value: Qt reads the C++ QQmlJSRegisterContent, which
      stays Python's own.

    Returns
    -------

    QQmlJSRegisterContent
      A new cute QQmlJSRegisterContent around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlJSRegisterContent
    #      QQmlJSRegisterContentPool::clone(QQmlJSRegisterContent from)
    address = self.uglySide.call(
        'ritual_ZN25QQmlJSRegisterContentPool5cloneE21QQmlJSRegisterContent',
        self._valueOf(from_),
    )
    return QQmlJSRegisterContent._cuteOwning(address)

  def clearTemporaries(self) -> None:
    """
    Calls Qt's 'void QQmlJSRegisterContentPool::clearTemporaries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsregistercontentpool.html#clearTemporaries
    """
    #  void QQmlJSRegisterContentPool::clearTemporaries()
    self.uglySide.call(
        'ritual_ZN25QQmlJSRegisterContentPool16clearTemporariesEv',
    )

  @staticmethod
  def adjustType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSRegisterContentPool::adjustType(QQmlJSRegisterContent
    content, const QQmlJSScope::ConstPtr &adjusted)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.adjustType' has no cute function yet. "
        "Qt's 'void "
        "QQmlJSRegisterContentPool::adjustType(QQmlJSRegisterContent "
        "content, const QQmlJSScope::ConstPtr &adjusted)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def castTo(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::castTo(QQmlJSRegisterContent content, const
    QQmlJSScope::ConstPtr &newContainedType)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.castTo' has no cute function yet. Qt's "
        "'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::castTo(QQmlJSRegisterContent content, "
        "const QQmlJSScope::ConstPtr &newContainedType)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    - Qt's 'QQmlJSRegisterContentPrivate
      *QQmlJSRegisterContentPool::create()': gives
      'QQmlJSRegisterContentPrivate', which has no cute class yet.
    - Qt's 'QQmlJSRegisterContentPrivate
      *QQmlJSRegisterContentPool::create(QQmlJSRegisterContent scope,
      ContentVariant variant)': gives 'QQmlJSRegisterContentPrivate', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.create' has no cute function yet. Qt's "
        "'QQmlJSRegisterContentPrivate "
        "*QQmlJSRegisterContentPool::create()': gives "
        "'QQmlJSRegisterContentPrivate', which has no cute class yet. Qt's "
        "'QQmlJSRegisterContentPrivate "
        "*QQmlJSRegisterContentPool::create(QQmlJSRegisterContent scope, "
        "ContentVariant variant)': gives 'QQmlJSRegisterContentPrivate', "
        "which has no cute class yet.")

  @staticmethod
  def createConversion(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createConversion(const
    QList<QQmlJSRegisterContent> &origins, const QQmlJSScope::ConstPtr
    &conversion, QQmlJSRegisterContent conversionScope, ContentVariant
    variant, QQmlJSRegisterContent scope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.createConversion' has no cute function "
        "yet. Qt's 'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::createConversion(const "
        "QList<QQmlJSRegisterContent> &origins, const QQmlJSScope::ConstPtr "
        "&conversion, QQmlJSRegisterContent conversionScope, ContentVariant "
        "variant, QQmlJSRegisterContent scope)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def createImportNamespace(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createImportNamespace(uint
    importNamespaceStringId, const QQmlJSScope::ConstPtr
    &importNamespaceType, ContentVariant variant, QQmlJSRegisterContent
    scope)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.createImportNamespace' has no cute "
        "function yet. Qt's 'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::createImportNamespace(uint "
        "importNamespaceStringId, const QQmlJSScope::ConstPtr "
        "&importNamespaceType, ContentVariant variant, "
        "QQmlJSRegisterContent scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def createMethod(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSRegisterContentPool::createMethod(const
    QList<QQmlJSMetaMethod> &methods, const QQmlJSScope::ConstPtr
    &methodType, ContentVariant variant, QQmlJSRegisterContent scope)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.createMethod' has no cute function yet. "
        "Qt's 'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::createMethod(const "
        "QList<QQmlJSMetaMethod> &methods, const QQmlJSScope::ConstPtr "
        "&methodType, ContentVariant variant, QQmlJSRegisterContent "
        "scope)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createMethodCall(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::createMethodCall(const QQmlJSMetaMethod
    &method, const QQmlJSScope::ConstPtr &returnType, QQmlJSRegisterContent
    scope)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.createMethodCall' has no cute function "
        "yet. Qt's 'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::createMethodCall(const QQmlJSMetaMethod "
        "&method, const QQmlJSScope::ConstPtr &returnType, "
        "QQmlJSRegisterContent scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def createType(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent QQmlJSRegisterContentPool::createType(const
    QQmlJSScope::ConstPtr &type, int resultLookupIndex, ContentVariant
    variant, QQmlJSRegisterContent scope)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.createType' has no cute function yet. "
        "Qt's 'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::createType(const QQmlJSScope::ConstPtr "
        "&type, int resultLookupIndex, ContentVariant variant, "
        "QQmlJSRegisterContent scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def generalizeType(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSRegisterContentPool::generalizeType(QQmlJSRegisterContent content,
    const QQmlJSScope::ConstPtr &generalized)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.generalizeType' has no cute function "
        "yet. Qt's 'void "
        "QQmlJSRegisterContentPool::generalizeType(QQmlJSRegisterContent "
        "content, const QQmlJSScope::ConstPtr &generalized)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def storeType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSRegisterContentPool::storeType(QQmlJSRegisterContent
    content, const QQmlJSScope::ConstPtr &stored)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.storeType' has no cute function yet. "
        "Qt's 'void "
        "QQmlJSRegisterContentPool::storeType(QQmlJSRegisterContent "
        "content, const QQmlJSScope::ConstPtr &stored)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def storedIn(*__, **_) -> Never:
    """
    Qt's 'QQmlJSRegisterContent
    QQmlJSRegisterContentPool::storedIn(QQmlJSRegisterContent content, const
    QQmlJSScope::ConstPtr &newStoredType)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSRegisterContentPool.storedIn' has no cute function yet. "
        "Qt's 'QQmlJSRegisterContent "
        "QQmlJSRegisterContentPool::storedIn(QQmlJSRegisterContent content, "
        "const QQmlJSScope::ConstPtr &newStoredType)': takes a type Python "
        "has no way to hand over yet.")
