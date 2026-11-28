"""
QMetaObjectBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMetaObjectBuilder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QtMocConstants

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QMetaEnum, QMetaEnumBuilder, QMetaMethod
  from . import QMetaMethodBuilder, QMetaObject, QMetaProperty
  from . import QMetaPropertyBuilder, QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaEnum = WAIT['QMetaEnum']
  QMetaMethod = WAIT['QMetaMethod']
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaObjectBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaObjectBuilder: a plain Python object standing in
  front of one C++ QMetaObjectBuilder.

  What exists
  -----------

  Every function of Qt's QMetaObjectBuilder that has a ritual and that Python
  can call so far, 44 names in all: 'className', 'setClassName',
  'superClass', 'setSuperClass', 'flags', 'setFlags', 'methodCount',
  'constructorCount', 'propertyCount', 'enumeratorCount', 'classInfoCount',
  'relatedMetaObjectCount', 'addMethod', 'addSlot', 'addSignal',
  'addConstructor', 'addProperty', 'addEnumerator', 'addClassInfo',
  'addRelatedMetaObject', 'addMetaObject', 'method', 'signal', 'constructor',
  'property', 'enumerator', 'relatedMetaObject', 'classInfoName',
  'classInfoValue', 'removeMethod', 'removeSignal', 'removeConstructor',
  'removeProperty', 'removeEnumerator', 'removeClassInfo',
  'removeRelatedMetaObject', 'indexOfMethod', 'indexOfSignal', 'indexOfSlot',
  'indexOfConstructor', 'indexOfProperty', 'indexOfEnumerator',
  'indexOfClassInfo', 'toMetaObject'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMetaObjectBuilder::~QMetaObjectBuilder()': the destructor: Python
    never removes a C++ QMetaObjectBuilder.
  - Qt's 'QMetaObjectBuilder::StaticMetacallFunction
    QMetaObjectBuilder::staticMetacallFunction() const': gives a type Python
    has no way to take yet.
  - Qt's 'void
    QMetaObjectBuilder::setStaticMetacallFunction(QMetaObjectBuilder::
    StaticMetacallFunction value)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 59 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QMetaObjectBuilder is created at the first use, not by
    'QMetaObjectBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetaObjectBuilder.
  - Each name of Qt's QMetaObjectBuilder that has no cute function yet,
    'setStaticMetacallFunction', 'staticMetacallFunction', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMetaObjectBuilder, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AddMember(CuteFlags):
    """
    The flags enum 'QMetaObjectBuilder::AddMember' of Qt, with the 16 names
    Qt gives in it. Qt names the type of its combinations
    'QMetaObjectBuilder::AddMembers'.
    """

    ClassName = 0x1
    SuperClass = 0x2
    Methods = 0x4
    Signals = 0x8
    Slots = 0x10
    Constructors = 0x20
    Properties = 0x40
    Enumerators = 0x80
    ClassInfos = 0x100
    RelatedMetaObjects = 0x200
    StaticMetacall = 0x400
    PublicMethods = 0x800
    ProtectedMethods = 0x1000
    PrivateMethods = 0x2000
    AllMembers = 0x7fffffff
    AllPrimaryMembers = 0x7ffffbfc

  AddMembers = AddMember

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaObjectBuilder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def className(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaObjectBuilder::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#className

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaObjectBuilder::className() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder9classNameEv',
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def superClass(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaObjectBuilder::superClass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#superClass

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaObjectBuilder::superClass() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder10superClassEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def flags(self) -> QtMocConstants.MetaObjectFlags:
    """
    Calls Qt's 'MetaObjectFlags QMetaObjectBuilder::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#flags

    Returns
    -------

    QtMocConstants.MetaObjectFlags
      The value standing for the combination Qt gave back.
    """
    #  MetaObjectFlags QMetaObjectBuilder::flags() const
    return QtMocConstants.MetaObjectFlags(self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder5flagsEv',
    ))

  def methodCount(self) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::methodCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#methodCount
    """
    #  int QMetaObjectBuilder::methodCount() const
    return self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder11methodCountEv',
    )

  def constructorCount(self) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::constructorCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#constructorCount
    """
    #  int QMetaObjectBuilder::constructorCount() const
    return self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder16constructorCountEv',
    )

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::propertyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#propertyCount
    """
    #  int QMetaObjectBuilder::propertyCount() const
    return self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder13propertyCountEv',
    )

  def enumeratorCount(self) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::enumeratorCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#enumeratorCount
    """
    #  int QMetaObjectBuilder::enumeratorCount() const
    return self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder15enumeratorCountEv',
    )

  def classInfoCount(self) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::classInfoCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#classInfoCount
    """
    #  int QMetaObjectBuilder::classInfoCount() const
    return self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder14classInfoCountEv',
    )

  def relatedMetaObjectCount(self) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::relatedMetaObjectCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#relatedMetaObjectCount
    """
    #  int QMetaObjectBuilder::relatedMetaObjectCount() const
    return self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder22relatedMetaObjectCountEv',
    )

  @overload(int)
  def method(self, index: int) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::method(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#method

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::method(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder6methodEi', index,
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(int)
  def signal(self, index: int) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::signal(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#signal

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::signal(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder6signalEi', index,
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(int)
  def constructor(self, index: int) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::constructor(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#constructor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::constructor(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder11constructorEi', index,
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(int)
  def property(self, index: int) -> QMetaPropertyBuilder:
    """
    Calls Qt's 'QMetaPropertyBuilder QMetaObjectBuilder::property(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaPropertyBuilder
      A new cute QMetaPropertyBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaPropertyBuilder QMetaObjectBuilder::property(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder8propertyEi', index,
    )
    from . import QMetaPropertyBuilder
    return QMetaPropertyBuilder._cuteOwning(address)

  @overload(int)
  def enumerator(self, index: int) -> QMetaEnumBuilder:
    """
    Calls Qt's 'QMetaEnumBuilder QMetaObjectBuilder::enumerator(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#enumerator

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaEnumBuilder
      A new cute QMetaEnumBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaEnumBuilder QMetaObjectBuilder::enumerator(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder10enumeratorEi', index,
    )
    from . import QMetaEnumBuilder
    return QMetaEnumBuilder._cuteOwning(address)

  @overload(int)
  def relatedMetaObject(self, index: int) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaObjectBuilder::relatedMetaObject(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#relatedMetaObject

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaObjectBuilder::relatedMetaObject(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder17relatedMetaObjectEi', index,
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def classInfoName(self, index: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaObjectBuilder::classInfoName(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#classInfoName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaObjectBuilder::classInfoName(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder13classInfoNameEi', index,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def classInfoValue(self, index: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMetaObjectBuilder::classInfoValue(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#classInfoValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMetaObjectBuilder::classInfoValue(int index) const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder14classInfoValueEi', index,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def toMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'QMetaObject *QMetaObjectBuilder::toMetaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#toMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetaObject *QMetaObjectBuilder::toMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QMetaObjectBuilder12toMetaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setClassName(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::setClassName(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#setClassName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMetaObjectBuilder::setClassName(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder12setClassNameERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def setSuperClass(self, meta: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::setSuperClass(const QMetaObject
    *meta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#setSuperClass

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMetaObjectBuilder::setSuperClass(const QMetaObject *meta)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder13setSuperClassEPK11QMetaObject',
        self._addressOf(meta, 'QMetaObject'),
    )

  @overload(QtMocConstants.MetaObjectFlags)
  def setFlags(self, a0: QtMocConstants.MetaObjectFlags) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::setFlags(MetaObjectFlags a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#setFlags

    Parameters
    ----------

    a0 : QtMocConstants.MetaObjectFlags
      Passed on as its number.
    """
    #  void QMetaObjectBuilder::setFlags(MetaObjectFlags a0)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder8setFlagsE6QFlagsIN14QtMocConstants14'
        'MetaObjectFlagEE',
        a0.value,
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
    'QMetaObjectBuilder::QMetaObjectBuilder()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#QMetaObjectBuilder
    """
    #  QMetaObjectBuilder::QMetaObjectBuilder()
    self._noteCreation(QMetaObjectBuilder, lambda: Rituals.call(
        'ritual_ZN18QMetaObjectBuilderC1Ev',
    ))

  @overload(QMetaObject)
  @overload(NoneType)
  @overload(QMetaObject, AddMembers)
  @overload(NoneType, AddMembers)
  def __init__(
      self,
      prototype: Optional[QMetaObject],
      members: AddMembers = AddMembers.AllMembers,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QMetaObjectBuilder::QMetaObjectBuilder(const QMetaObject *prototype,
    QMetaObjectBuilder::AddMembers members)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#QMetaObjectBuilder

    Parameters
    ----------

    prototype : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    members : AddMembers
      Passed on as its number. May be left out, as in Qt: it is then
      AddMembers.AllMembers.
    """
    #  QMetaObjectBuilder::QMetaObjectBuilder(const QMetaObject *prototype,
    #      QMetaObjectBuilder::AddMembers members)
    self._noteCreation(QMetaObjectBuilder, lambda: Rituals.call(
        'ritual_ZN18QMetaObjectBuilderC1EPK11QMetaObject6QFlagsINS_9AddMemb'
        'erEE',
        self._addressOf(prototype, 'QMetaObject'), members.value,
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

  @overload(QByteArray)
  def addMethod(self, signature: QByteArray) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addMethod(const
    QByteArray &signature)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addMethod

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addMethod(const QByteArray
    #      &signature)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder9addMethodERK10QByteArray',
        self._valueOf(signature),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QByteArray, QByteArray)
  def addMethod(
      self,
      signature: QByteArray,
      returnType: QByteArray,
  ) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addMethod(const
    QByteArray &signature, const QByteArray &returnType)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addMethod

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    returnType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addMethod(const QByteArray
    #      &signature, const QByteArray &returnType)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder9addMethodERK10QByteArrayS2_',
        self._valueOf(signature), self._valueOf(returnType),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QMetaMethod)
  def addMethod(self, prototype: QMetaMethod) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addMethod(const
    QMetaMethod &prototype)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addMethod

    Parameters
    ----------

    prototype : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addMethod(const QMetaMethod
    #      &prototype)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder9addMethodERK11QMetaMethod',
        self._valueOf(prototype),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QByteArray)
  def addSlot(self, signature: QByteArray) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addSlot(const
    QByteArray &signature)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addSlot

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addSlot(const QByteArray
    #      &signature)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder7addSlotERK10QByteArray',
        self._valueOf(signature),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QByteArray)
  def addSignal(self, signature: QByteArray) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addSignal(const
    QByteArray &signature)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addSignal

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addSignal(const QByteArray
    #      &signature)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder9addSignalERK10QByteArray',
        self._valueOf(signature),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QByteArray)
  def addConstructor(self, signature: QByteArray) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addConstructor(const
    QByteArray &signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addConstructor

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addConstructor(const QByteArray
    #      &signature)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder14addConstructorERK10QByteArray',
        self._valueOf(signature),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QMetaMethod)
  def addConstructor(self, prototype: QMetaMethod) -> QMetaMethodBuilder:
    """
    Calls Qt's 'QMetaMethodBuilder QMetaObjectBuilder::addConstructor(const
    QMetaMethod &prototype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addConstructor

    Parameters
    ----------

    prototype : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.

    Returns
    -------

    QMetaMethodBuilder
      A new cute QMetaMethodBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaMethodBuilder QMetaObjectBuilder::addConstructor(const
    #      QMetaMethod &prototype)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder14addConstructorERK11QMetaMethod',
        self._valueOf(prototype),
    )
    from . import QMetaMethodBuilder
    return QMetaMethodBuilder._cuteOwning(address)

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, QByteArray, int)
  def addProperty(
      self,
      name: QByteArray,
      type: QByteArray,
      notifierId: int = -1,
  ) -> QMetaPropertyBuilder:
    """
    Calls Qt's 'QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const
    QByteArray &name, const QByteArray &type, int notifierId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addProperty

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    notifierId : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QMetaPropertyBuilder
      A new cute QMetaPropertyBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const QByteArray
    #      &name, const QByteArray &type, int notifierId)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder11addPropertyERK10QByteArrayS2_i',
        self._valueOf(name), self._valueOf(type), notifierId,
    )
    from . import QMetaPropertyBuilder
    return QMetaPropertyBuilder._cuteOwning(address)

  @overload(QByteArray, QByteArray, QMetaType)
  @overload(QByteArray, QByteArray, QMetaType, int)
  def addProperty(
      self,
      name: QByteArray,
      type: QByteArray,
      metaType: QMetaType,
      notifierId: int = -1,
  ) -> QMetaPropertyBuilder:
    """
    Calls Qt's 'QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const
    QByteArray &name, const QByteArray &type, QMetaType metaType, int
    notifierId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addProperty

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    notifierId : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QMetaPropertyBuilder
      A new cute QMetaPropertyBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const QByteArray
    #      &name, const QByteArray &type, QMetaType metaType, int notifierId)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder11addPropertyERK10QByteArrayS2_9QMeta'
        'Typei',
        self._valueOf(name), self._valueOf(type), self._valueOf(metaType),
        notifierId,
    )
    from . import QMetaPropertyBuilder
    return QMetaPropertyBuilder._cuteOwning(address)

  @overload(QMetaProperty)
  def addProperty(self, prototype: QMetaProperty) -> QMetaPropertyBuilder:
    """
    Calls Qt's 'QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const
    QMetaProperty &prototype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addProperty

    Parameters
    ----------

    prototype : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    Returns
    -------

    QMetaPropertyBuilder
      A new cute QMetaPropertyBuilder around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaPropertyBuilder QMetaObjectBuilder::addProperty(const
    #      QMetaProperty &prototype)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder11addPropertyERK13QMetaProperty',
        self._valueOf(prototype),
    )
    from . import QMetaPropertyBuilder
    return QMetaPropertyBuilder._cuteOwning(address)

  @overload(QByteArray)
  def addEnumerator(self, name: QByteArray) -> QMetaEnumBuilder:
    """
    Calls Qt's 'QMetaEnumBuilder QMetaObjectBuilder::addEnumerator(const
    QByteArray &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addEnumerator

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaEnumBuilder
      A new cute QMetaEnumBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaEnumBuilder QMetaObjectBuilder::addEnumerator(const QByteArray
    #      &name)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder13addEnumeratorERK10QByteArray',
        self._valueOf(name),
    )
    from . import QMetaEnumBuilder
    return QMetaEnumBuilder._cuteOwning(address)

  @overload(QMetaEnum)
  def addEnumerator(self, prototype: QMetaEnum) -> QMetaEnumBuilder:
    """
    Calls Qt's 'QMetaEnumBuilder QMetaObjectBuilder::addEnumerator(const
    QMetaEnum &prototype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addEnumerator

    Parameters
    ----------

    prototype : QMetaEnum
      Passed on as a value: Qt reads the C++ QMetaEnum, which stays Python's
      own.

    Returns
    -------

    QMetaEnumBuilder
      A new cute QMetaEnumBuilder around the copy Qt gave back. Python owns
      it.
    """
    #  QMetaEnumBuilder QMetaObjectBuilder::addEnumerator(const QMetaEnum
    #      &prototype)
    address = self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder13addEnumeratorERK9QMetaEnum',
        self._valueOf(prototype),
    )
    from . import QMetaEnumBuilder
    return QMetaEnumBuilder._cuteOwning(address)

  @overload(QByteArray, QByteArray)
  def addClassInfo(self, name: QByteArray, value: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::addClassInfo(const QByteArray &name,
    const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addClassInfo

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::addClassInfo(const QByteArray &name, const
    #      QByteArray &value)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder12addClassInfoERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(value),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def addRelatedMetaObject(self, meta: Optional[QMetaObject]) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::addRelatedMetaObject(const
    QMetaObject *meta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addRelatedMetaObject

    Parameters
    ----------

    meta : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QMetaObjectBuilder::addRelatedMetaObject(const QMetaObject *meta)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder20addRelatedMetaObjectEPK11QMetaObjec'
        't',
        self._addressOf(meta, 'QMetaObject'),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  @overload(QMetaObject, AddMembers)
  @overload(NoneType, AddMembers)
  def addMetaObject(
      self,
      prototype: Optional[QMetaObject],
      members: AddMembers = AddMembers.AllMembers,
  ) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::addMetaObject(const QMetaObject
    *prototype, QMetaObjectBuilder::AddMembers members)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#addMetaObject

    Parameters
    ----------

    prototype : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    members : AddMembers
      Passed on as its number. May be left out, as in Qt: it is then
      AddMembers.AllMembers.
    """
    #  void QMetaObjectBuilder::addMetaObject(const QMetaObject *prototype,
    #      QMetaObjectBuilder::AddMembers members)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder13addMetaObjectEPK11QMetaObject6QFlag'
        'sINS_9AddMemberEE',
        self._addressOf(prototype, 'QMetaObject'), members.value,
    )

  @overload(int)
  def removeMethod(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeMethod(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeMethod

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeMethod(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder12removeMethodEi', index,
    )

  @overload(int)
  def removeSignal(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeSignal(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeSignal(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder12removeSignalEi', index,
    )

  @overload(int)
  def removeConstructor(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeConstructor(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeConstructor

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeConstructor(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder17removeConstructorEi', index,
    )

  @overload(int)
  def removeProperty(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeProperty(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeProperty(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder14removePropertyEi', index,
    )

  @overload(int)
  def removeEnumerator(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeEnumerator(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeEnumerator

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeEnumerator(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder16removeEnumeratorEi', index,
    )

  @overload(int)
  def removeClassInfo(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeClassInfo(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeClassInfo

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeClassInfo(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder15removeClassInfoEi', index,
    )

  @overload(int)
  def removeRelatedMetaObject(self, index: int) -> None:
    """
    Calls Qt's 'void QMetaObjectBuilder::removeRelatedMetaObject(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#removeRelatedMetaObject

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QMetaObjectBuilder::removeRelatedMetaObject(int index)
    self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder23removeRelatedMetaObjectEi', index,
    )

  @overload(QByteArray)
  def indexOfMethod(self, signature: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfMethod(const QByteArray
    &signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfMethod

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfMethod(const QByteArray &signature)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder13indexOfMethodERK10QByteArray',
        self._valueOf(signature),
    )

  @overload(QByteArray)
  def indexOfSignal(self, signature: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfSignal(const QByteArray
    &signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfSignal

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfSignal(const QByteArray &signature)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder13indexOfSignalERK10QByteArray',
        self._valueOf(signature),
    )

  @overload(QByteArray)
  def indexOfSlot(self, signature: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfSlot(const QByteArray
    &signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfSlot

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfSlot(const QByteArray &signature)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder11indexOfSlotERK10QByteArray',
        self._valueOf(signature),
    )

  @overload(QByteArray)
  def indexOfConstructor(self, signature: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfConstructor(const QByteArray
    &signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfConstructor

    Parameters
    ----------

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfConstructor(const QByteArray
    #      &signature)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder18indexOfConstructorERK10QByteArray',
        self._valueOf(signature),
    )

  @overload(QByteArray)
  def indexOfProperty(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfProperty(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfProperty

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfProperty(const QByteArray &name)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder15indexOfPropertyERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QByteArray)
  def indexOfEnumerator(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfEnumerator(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfEnumerator

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfEnumerator(const QByteArray &name)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder17indexOfEnumeratorERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QByteArray)
  def indexOfClassInfo(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaObjectBuilder::indexOfClassInfo(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaobjectbuilder.html#indexOfClassInfo

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaObjectBuilder::indexOfClassInfo(const QByteArray &name)
    return self.uglySide.call(
        'ritual_ZN18QMetaObjectBuilder16indexOfClassInfoERK10QByteArray',
        self._valueOf(name),
    )

  @staticmethod
  def setStaticMetacallFunction(*__, **_) -> Never:
    """
    Qt's 'void
    QMetaObjectBuilder::setStaticMetacallFunction(QMetaObjectBuilder::
    StaticMetacallFunction value)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QMetaObjectBuilder.setStaticMetacallFunction' has no cute "
        "function yet. Qt's 'void "
        "QMetaObjectBuilder::setStaticMetacallFunction(QMetaObjectBuilder::S"
        "taticMetacallFunction value)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def staticMetacallFunction(*__, **_) -> Never:
    """
    Qt's 'QMetaObjectBuilder::StaticMetacallFunction
    QMetaObjectBuilder::staticMetacallFunction() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QMetaObjectBuilder.staticMetacallFunction' has no cute function "
        "yet. Qt's 'QMetaObjectBuilder::StaticMetacallFunction "
        "QMetaObjectBuilder::staticMetacallFunction() const': gives a type "
        "Python has no way to take yet.")
