"""
QQmlPropertyData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlPropertyData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaMethod, QMetaObject, QMetaProperty, QMetaType
  from ..QtCore import QObject, QTypeRevision, QUntypedBindable
  from . import QQmlPropertyCacheMethodArguments
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaMethod = WAIT['QMetaMethod']
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlPropertyCacheMethodArguments = WAIT['QQmlPropertyCacheMethodArguments']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyData: a plain Python object standing in
  front of one C++ QQmlPropertyData.

  C++ hands a QQmlPropertyData around as a copy, so every C++
  QQmlPropertyData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyData that has a ritual and that Python
  can call so far, 72 names in all: '__eq__', 'flags', 'setFlags', 'isValid',
  'isConstant', 'isWritable', 'setWritable', 'isResettable', 'isAlias',
  'isFinal', 'isVirtual', 'doesOverride', 'isOverridden', 'isRequired',
  'isFunction', 'isQObject', 'isEnum', 'isQList', 'isVarProperty',
  'isQVariant', 'isComponentWrapper', 'isVMEFunction', 'hasArguments',
  'isSignal', 'isVMESignal', 'isV4Function', 'isSignalHandler',
  'hasMetaObject', 'hasStaticMetaCallFunction', 'isOverridableSignal',
  'isCloned', 'isConstructor', 'notifiesViaBindable', 'acceptsQBinding',
  'hasOverride', 'hasRevision', 'propType', 'setPropType', 'notifyIndex',
  'setNotifyIndex', 'overrideIndexIsProperty', 'setOverrideIndexIsProperty',
  'overrideIndex', 'setOverrideIndex', 'coreIndex', 'setCoreIndex',
  'aliasTarget', 'setAliasTarget', 'aliasTargetObjectId',
  'setAliasTargetObjectId', 'wrappedObjectIndex', 'setWrappedObjectIndex',
  'revision', 'setRevision', 'typeVersion', 'setTypeVersion', 'arguments',
  'setArguments', 'metaObject', 'setMetaObject', 'metaMethod',
  'metaObjectOffset', 'setMetaObjectOffset', 'relativePropertyIndex',
  'flagsForProperty', 'load', 'name', 'markAsOverrideOf', 'resetProperty',
  'propertyBindable', 'defaultSignalFlags', 'defaultSlotFlags'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'StaticMetaCallFunction QQmlPropertyData::staticMetaCallFunction()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    QQmlPropertyData::trySetStaticMetaCallFunction(StaticMetaCallFunction f,
    unsigned int relativePropertyIndex)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlPropertyData::readProperty(QObject *target, void
    *property) const': names 'void', which has no cute class yet.
  - Qt's 'void QQmlPropertyData::readPropertyWithArgs(QObject *target, void
    **args) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlPropertyData::writeProperty(QObject *target, void *value,
    WriteFlags flags) const': names 'void', which has no cute class yet.
  - Qt's 'QQmlPropertyData::~QQmlPropertyData()': the destructor: Python
    removes its C++ QQmlPropertyData by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 81 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlPropertyData is created at the first use, not by
    'QQmlPropertyData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyData back gives a copy the ritual made
    for Python, in a new cute QQmlPropertyData.
  - Each name of Qt's QQmlPropertyData that has no cute function yet,
    'doMetacall', 'readProperty', 'readPropertyWithArgs',
    'staticMetaCallFunction', 'trySetStaticMetaCallFunction',
    'writeProperty', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQmlPropertyData, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class WriteFlag(CuteFlags):
    """
    The flags enum 'QQmlPropertyData::WriteFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QQmlPropertyData::WriteFlags'.
    """

    BypassInterceptor = 0x1
    DontRemoveBinding = 0x2
    RemoveBindingOnAliasWrite = 0x4
    HasInternalIndex = 0x8

  WriteFlags = WriteFlag

  #  The classes Qt writes inside QQmlPropertyData, each a class in here as
  #  in C++.

  class Flags(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlPropertyData::Flags: a plain Python object
    standing in front of one C++ QQmlPropertyData::Flags.

    C++ hands a QQmlPropertyData::Flags around as a copy, so every C++
    QQmlPropertyData::Flags behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQmlPropertyData::Flags that has a ritual and that
    Python can call so far, 24 names in all: '__eq__',
    'copyPropertyTypeFlags', 'setIsConstant', 'setIsWritable',
    'setIsResettable', 'setIsAlias', 'setIsDeepAlias', 'setIsFinal',
    'setIsVirtual', 'setDoesOverride', 'setIsOverridden', 'setIsBindable',
    'setIsRequired', 'setIsVMEFunction', 'setHasArguments', 'setIsSignal',
    'setIsVMESignal', 'setIsV4Function', 'setIsSignalHandler',
    'setIsOverridableSignal', 'setIsCloned', 'setIsConstructor',
    'setHasMetaObject', 'setType'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlPropertyData::Flags::~Flags()': the destructor: Python
      removes its C++ QQmlPropertyData::Flags by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlPropertyData::Flags is created at the first use, not by
      'QQmlPropertyData::Flags(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlPropertyData::Flags back gives a copy the
      ritual made for Python, in a new cute QQmlPropertyData::Flags.
    """

    #  The enums Qt writes inside QQmlPropertyData::Flags, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Type(CuteNum):
      """
      The enum 'QQmlPropertyData::Flags::Type' of Qt, with the 8 names Qt
      gives in it.
      """

      OtherType = Kee[int](0)
      FunctionType = Kee[int](1)
      QObjectDerivedType = Kee[int](2)
      EnumType = Kee[int](3)
      QListType = Kee[int](4)
      VarPropertyType = Kee[int](5)
      QVariantType = Kee[int](6)
      ComponentWrapperType = Kee[int](7)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlPropertyData::Flags'

    #  Qt's '~QQmlPropertyData::Flags()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlPropertyData::Flags behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQmlPropertyData5FlagsD1Ev'

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

    @overload(bool)
    def setIsConstant(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsConstant(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsConstant

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsConstant(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags13setIsConstantEb', b,
      )

    @overload(bool)
    def setIsWritable(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsWritable(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsWritable

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsWritable(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags13setIsWritableEb', b,
      )

    @overload(bool)
    def setIsResettable(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsResettable(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsResettable

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsResettable(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags15setIsResettableEb', b,
      )

    @overload(bool)
    def setIsAlias(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsAlias(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsAlias

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsAlias(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags10setIsAliasEb', b,
      )

    @overload(bool)
    def setIsDeepAlias(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsDeepAlias(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsDeepAlias

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsDeepAlias(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags14setIsDeepAliasEb', b,
      )

    @overload(bool)
    def setIsFinal(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsFinal(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsFinal

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsFinal(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags10setIsFinalEb', b,
      )

    @overload(bool)
    def setIsVirtual(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsVirtual(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsVirtual

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsVirtual(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags12setIsVirtualEb', b,
      )

    @overload(bool)
    def setDoesOverride(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setDoesOverride(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setDoesOverride

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setDoesOverride(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags15setDoesOverrideEb', b,
      )

    @overload(bool)
    def setIsOverridden(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsOverridden(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsOverridden

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsOverridden(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags15setIsOverriddenEb', b,
      )

    @overload(bool)
    def setIsBindable(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsBindable(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsBindable

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsBindable(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags13setIsBindableEb', b,
      )

    @overload(bool)
    def setIsRequired(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsRequired(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsRequired

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsRequired(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags13setIsRequiredEb', b,
      )

    @overload(bool)
    def setIsVMEFunction(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsVMEFunction(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsVMEFunction

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsVMEFunction(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags16setIsVMEFunctionEb', b,
      )

    @overload(bool)
    def setHasArguments(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setHasArguments(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setHasArguments

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setHasArguments(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags15setHasArgumentsEb', b,
      )

    @overload(bool)
    def setIsSignal(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsSignal(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsSignal

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsSignal(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags11setIsSignalEb', b,
      )

    @overload(bool)
    def setIsVMESignal(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsVMESignal(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsVMESignal

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsVMESignal(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags14setIsVMESignalEb', b,
      )

    @overload(bool)
    def setIsV4Function(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsV4Function(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsV4Function

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsV4Function(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags15setIsV4FunctionEb', b,
      )

    @overload(bool)
    def setIsSignalHandler(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsSignalHandler(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsSignalHandler

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsSignalHandler(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags18setIsSignalHandlerEb', b,
      )

    @overload(bool)
    def setIsOverridableSignal(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsOverridableSignal(bool
      b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsOverridableSignal(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags22setIsOverridableSignalEb', b,
      )

    @overload(bool)
    def setIsCloned(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsCloned(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsCloned

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsCloned(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags11setIsClonedEb', b,
      )

    @overload(bool)
    def setIsConstructor(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setIsConstructor(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setIsConstructor

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setIsConstructor(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags16setIsConstructorEb', b,
      )

    @overload(bool)
    def setHasMetaObject(self, b: bool) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setHasMetaObject(bool b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setHasMetaObject

      Parameters
      ----------

      b : bool
        Passed on as it is.
      """
      #  void QQmlPropertyData::Flags::setHasMetaObject(bool b)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags16setHasMetaObjectEb', b,
      )

    @overload(Type)
    def setType(self, newType: Type) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::setType(Type newType)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#setType

      Parameters
      ----------

      newType : Type
        Passed on as its number.
      """
      #  void QQmlPropertyData::Flags::setType(Type newType)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags7setTypeENS0_4TypeE',
          newType.value,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, other: QQmlPropertyData.Flags) -> bool:
      """
      Calls Qt's 'bool QQmlPropertyData::Flags::operator==(const Flags
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#operator==

      Parameters
      ----------

      other : QQmlPropertyData.Flags
        Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
        stays Python's own.
      """
      #  bool QQmlPropertyData::Flags::operator==(const Flags &other) const
      return self.uglySide.call(
          'ritual_ZNK16QQmlPropertyData5FlagseqERKS0_', self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlPropertyData::Flags::Flags()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html#Flags
      """
      #  QQmlPropertyData::Flags::Flags()
      self._noteCreation(QQmlPropertyData.Flags, lambda: Rituals.call(
          'ritual_ZN16QQmlPropertyData5FlagsC1Ev',
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

    @overload(THIS)
    def copyPropertyTypeFlags(self, from_: QQmlPropertyData.Flags) -> None:
      """
      Calls Qt's 'void QQmlPropertyData::Flags::copyPropertyTypeFlags(Flags
      from)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlpropertydata-flags.html

      Parameters
      ----------

      from_ : QQmlPropertyData.Flags
        Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
        stays Python's own.
      """
      #  void QQmlPropertyData::Flags::copyPropertyTypeFlags(Flags from)
      self.uglySide.call(
          'ritual_ZN16QQmlPropertyData5Flags21copyPropertyTypeFlagsES0_',
          self._valueOf(from_),
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaProperty)
  def flagsForProperty(a0: QMetaProperty) -> Flags:
    """
    Calls Qt's 'Flags QQmlPropertyData::flagsForProperty(const QMetaProperty
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#flagsForProperty

    Parameters
    ----------

    a0 : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    Returns
    -------

    Flags
      A new cute QQmlPropertyData::Flags around the copy Qt gave back. Python
      owns it.
    """
    #  Flags QQmlPropertyData::flagsForProperty(const QMetaProperty &a0)
    address = Rituals.call(
        'ritual_ZN16QQmlPropertyData16flagsForPropertyERK13QMetaProperty',
        CuteMixin._valueOf(a0),
    )
    return QQmlPropertyData.Flags._cuteOwning(address)

  @staticmethod
  def defaultSignalFlags() -> Flags:
    """
    Calls Qt's 'Flags QQmlPropertyData::defaultSignalFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#defaultSignalFlags

    Returns
    -------

    Flags
      A new cute QQmlPropertyData::Flags around the copy Qt gave back. Python
      owns it.
    """
    #  Flags QQmlPropertyData::defaultSignalFlags()
    address = Rituals.call(
        'ritual_ZN16QQmlPropertyData18defaultSignalFlagsEv',
    )
    return QQmlPropertyData.Flags._cuteOwning(address)

  @staticmethod
  def defaultSlotFlags() -> Flags:
    """
    Calls Qt's 'Flags QQmlPropertyData::defaultSlotFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#defaultSlotFlags

    Returns
    -------

    Flags
      A new cute QQmlPropertyData::Flags around the copy Qt gave back. Python
      owns it.
    """
    #  Flags QQmlPropertyData::defaultSlotFlags()
    address = Rituals.call('ritual_ZN16QQmlPropertyData16defaultSlotFlagsEv')
    return QQmlPropertyData.Flags._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyData'

  #  Qt's '~QQmlPropertyData()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlPropertyData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlPropertyDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QQmlPropertyData::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#flags

    Returns
    -------

    Flags
      A new cute QQmlPropertyData::Flags around the copy Qt gave back. Python
      owns it.
    """
    #  Flags QQmlPropertyData::flags() const
    address = self.uglySide.call('ritual_ZNK16QQmlPropertyData5flagsEv')
    return QQmlPropertyData.Flags._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isValid
    """
    #  bool QQmlPropertyData::isValid() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData7isValidEv')

  def isConstant(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isConstant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isConstant
    """
    #  bool QQmlPropertyData::isConstant() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData10isConstantEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isWritable
    """
    #  bool QQmlPropertyData::isWritable() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData10isWritableEv')

  def isResettable(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isResettable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isResettable
    """
    #  bool QQmlPropertyData::isResettable() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData12isResettableEv')

  def isAlias(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isAlias
    """
    #  bool QQmlPropertyData::isAlias() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData7isAliasEv')

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isFinal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isFinal
    """
    #  bool QQmlPropertyData::isFinal() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData7isFinalEv')

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isVirtual() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isVirtual
    """
    #  bool QQmlPropertyData::isVirtual() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData9isVirtualEv')

  def doesOverride(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::doesOverride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#doesOverride
    """
    #  bool QQmlPropertyData::doesOverride() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData12doesOverrideEv')

  def isOverridden(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isOverridden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isOverridden
    """
    #  bool QQmlPropertyData::isOverridden() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData12isOverriddenEv')

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isRequired() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isRequired
    """
    #  bool QQmlPropertyData::isRequired() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData10isRequiredEv')

  def isFunction(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isFunction
    """
    #  bool QQmlPropertyData::isFunction() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData10isFunctionEv')

  def isQObject(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isQObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isQObject
    """
    #  bool QQmlPropertyData::isQObject() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData9isQObjectEv')

  def isEnum(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isEnum
    """
    #  bool QQmlPropertyData::isEnum() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData6isEnumEv')

  def isQList(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isQList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isQList
    """
    #  bool QQmlPropertyData::isQList() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData7isQListEv')

  def isVarProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isVarProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#isVarProperty
    """
    #  bool QQmlPropertyData::isVarProperty() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData13isVarPropertyEv',
    )

  def isQVariant(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isQVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isQVariant
    """
    #  bool QQmlPropertyData::isQVariant() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData10isQVariantEv')

  def isComponentWrapper(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isComponentWrapper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#isComponentWrapper
    """
    #  bool QQmlPropertyData::isComponentWrapper() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData18isComponentWrapperEv',
    )

  def isVMEFunction(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isVMEFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#isVMEFunction
    """
    #  bool QQmlPropertyData::isVMEFunction() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData13isVMEFunctionEv',
    )

  def hasArguments(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::hasArguments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#hasArguments
    """
    #  bool QQmlPropertyData::hasArguments() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData12hasArgumentsEv')

  def isSignal(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isSignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isSignal
    """
    #  bool QQmlPropertyData::isSignal() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData8isSignalEv')

  def isVMESignal(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isVMESignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isVMESignal
    """
    #  bool QQmlPropertyData::isVMESignal() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData11isVMESignalEv')

  def isV4Function(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isV4Function() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isV4Function
    """
    #  bool QQmlPropertyData::isV4Function() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData12isV4FunctionEv')

  def isSignalHandler(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isSignalHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#isSignalHandler
    """
    #  bool QQmlPropertyData::isSignalHandler() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData15isSignalHandlerEv',
    )

  def hasMetaObject(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::hasMetaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#hasMetaObject
    """
    #  bool QQmlPropertyData::hasMetaObject() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData13hasMetaObjectEv',
    )

  def hasStaticMetaCallFunction(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::hasStaticMetaCallFunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#hasStaticMetaCallFunction
    """
    #  bool QQmlPropertyData::hasStaticMetaCallFunction() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData25hasStaticMetaCallFunctionEv',
    )

  def isOverridableSignal(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isOverridableSignal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#isOverridableSignal
    """
    #  bool QQmlPropertyData::isOverridableSignal() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData19isOverridableSignalEv',
    )

  def isCloned(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isCloned() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#isCloned
    """
    #  bool QQmlPropertyData::isCloned() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData8isClonedEv')

  def isConstructor(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::isConstructor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#isConstructor
    """
    #  bool QQmlPropertyData::isConstructor() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData13isConstructorEv',
    )

  def notifiesViaBindable(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::notifiesViaBindable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#notifiesViaBindable
    """
    #  bool QQmlPropertyData::notifiesViaBindable() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData19notifiesViaBindableEv',
    )

  def acceptsQBinding(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::acceptsQBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#acceptsQBinding
    """
    #  bool QQmlPropertyData::acceptsQBinding() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData15acceptsQBindingEv',
    )

  def hasOverride(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::hasOverride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#hasOverride
    """
    #  bool QQmlPropertyData::hasOverride() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData11hasOverrideEv')

  def hasRevision(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::hasRevision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#hasRevision
    """
    #  bool QQmlPropertyData::hasRevision() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData11hasRevisionEv')

  def propType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlPropertyData::propType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#propType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlPropertyData::propType() const
    address = self.uglySide.call('ritual_ZNK16QQmlPropertyData8propTypeEv')
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def notifyIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::notifyIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#notifyIndex
    """
    #  int QQmlPropertyData::notifyIndex() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData11notifyIndexEv')

  def overrideIndexIsProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::overrideIndexIsProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#overrideIndexIsProperty
    """
    #  bool QQmlPropertyData::overrideIndexIsProperty() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData23overrideIndexIsPropertyEv',
    )

  def overrideIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::overrideIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#overrideIndex
    """
    #  int QQmlPropertyData::overrideIndex() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData13overrideIndexEv',
    )

  def coreIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::coreIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#coreIndex
    """
    #  int QQmlPropertyData::coreIndex() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData9coreIndexEv')

  def aliasTarget(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::aliasTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#aliasTarget
    """
    #  int QQmlPropertyData::aliasTarget() const
    return self.uglySide.call('ritual_ZNK16QQmlPropertyData11aliasTargetEv')

  def aliasTargetObjectId(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::aliasTargetObjectId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#aliasTargetObjectId
    """
    #  int QQmlPropertyData::aliasTargetObjectId() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData19aliasTargetObjectIdEv',
    )

  def wrappedObjectIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::wrappedObjectIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#wrappedObjectIndex
    """
    #  int QQmlPropertyData::wrappedObjectIndex() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData18wrappedObjectIndexEv',
    )

  def revision(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlPropertyData::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#revision

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlPropertyData::revision() const
    address = self.uglySide.call('ritual_ZNK16QQmlPropertyData8revisionEv')
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def typeVersion(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlPropertyData::typeVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#typeVersion

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlPropertyData::typeVersion() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData11typeVersionEv',
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def arguments(self) -> Optional[QQmlPropertyCacheMethodArguments]:
    """
    Calls Qt's 'QQmlPropertyCacheMethodArguments
    *QQmlPropertyData::arguments() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#arguments

    Returns
    -------

    Optional[QQmlPropertyCacheMethodArguments]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyCacheMethodArguments *QQmlPropertyData::arguments() const
    address = self.uglySide.call('ritual_ZNK16QQmlPropertyData9argumentsEv')
    from . import QQmlPropertyCacheMethodArguments
    return QQmlPropertyCacheMethodArguments._cuteAt(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlPropertyData::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlPropertyData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaMethod(self) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QQmlPropertyData::metaMethod() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#metaMethod

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QQmlPropertyData::metaMethod() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData10metaMethodEv',
    )
    from ..QtCore import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  def metaObjectOffset(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyData::metaObjectOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#metaObjectOffset
    """
    #  int QQmlPropertyData::metaObjectOffset() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData16metaObjectOffsetEv',
    )

  def relativePropertyIndex(self) -> int:
    """
    Calls Qt's 'quint16 QQmlPropertyData::relativePropertyIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#relativePropertyIndex
    """
    #  quint16 QQmlPropertyData::relativePropertyIndex() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData21relativePropertyIndexEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def name(self, object: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QQmlPropertyData::name(QObject *object) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#name

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPropertyData::name(QObject *object) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData4nameEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QMetaObject)
  def name(self, metaObject: Optional[QMetaObject]) -> str:
    """
    Calls Qt's 'QString QQmlPropertyData::name(const QMetaObject *metaObject)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#name

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPropertyData::name(const QMetaObject *metaObject) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData4nameEPK11QMetaObject',
        self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(QObject, WriteFlags)
  @overload(NoneType, WriteFlags)
  def resetProperty(
      self,
      target: Optional[QObject],
      flags: WriteFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::resetProperty(QObject *target,
    WriteFlags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#resetProperty

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : WriteFlags
      Passed on as its number.
    """
    #  bool QQmlPropertyData::resetProperty(QObject *target, WriteFlags
    #      flags) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData13resetPropertyEP7QObject6QFlagsINS_9W'
        'riteFlagEE',
        self._addressOf(target, 'QObject'), flags.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def propertyBindable(self, target: Optional[QObject]) -> QUntypedBindable:
    """
    Calls Qt's 'QUntypedBindable QQmlPropertyData::propertyBindable(QObject
    *target) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#propertyBindable

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QUntypedBindable
      A new cute QUntypedBindable around the copy Qt gave back. Python owns
      it.
    """
    #  QUntypedBindable QQmlPropertyData::propertyBindable(QObject *target)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlPropertyData16propertyBindableEP7QObject',
        self._addressOf(target, 'QObject'),
    )
    from ..QtCore import QUntypedBindable
    return QUntypedBindable._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  def setFlags(self, f: Flags) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setFlags(Flags f)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#setFlags

    Parameters
    ----------

    f : Flags
      Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
      stays Python's own.
    """
    #  void QQmlPropertyData::setFlags(Flags f)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData8setFlagsENS_5FlagsE', self._valueOf(f),
    )

  @overload(bool)
  def setWritable(self, onoff: bool) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setWritable(bool onoff)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#setWritable

    Parameters
    ----------

    onoff : bool
      Passed on as it is.
    """
    #  void QQmlPropertyData::setWritable(bool onoff)
    self.uglySide.call('ritual_ZN16QQmlPropertyData11setWritableEb', onoff)

  @overload(QMetaType)
  def setPropType(self, pt: QMetaType) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setPropType(QMetaType pt)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#setPropType

    Parameters
    ----------

    pt : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QQmlPropertyData::setPropType(QMetaType pt)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData11setPropTypeE9QMetaType',
        self._valueOf(pt),
    )

  @overload(int)
  def setNotifyIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setNotifyIndex(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setNotifyIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setNotifyIndex(int idx)
    self.uglySide.call('ritual_ZN16QQmlPropertyData14setNotifyIndexEi', idx)

  @overload(bool)
  def setOverrideIndexIsProperty(self, onoff: bool) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setOverrideIndexIsProperty(bool
    onoff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setOverrideIndexIsProperty

    Parameters
    ----------

    onoff : bool
      Passed on as it is.
    """
    #  void QQmlPropertyData::setOverrideIndexIsProperty(bool onoff)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData26setOverrideIndexIsPropertyEb', onoff,
    )

  @overload(int)
  def setOverrideIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setOverrideIndex(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setOverrideIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setOverrideIndex(int idx)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData16setOverrideIndexEi', idx,
    )

  @overload(int)
  def setCoreIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setCoreIndex(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#setCoreIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setCoreIndex(int idx)
    self.uglySide.call('ritual_ZN16QQmlPropertyData12setCoreIndexEi', idx)

  @overload(int)
  def setAliasTarget(self, target: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setAliasTarget(int target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setAliasTarget

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setAliasTarget(int target)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData14setAliasTargetEi', target,
    )

  @overload(int)
  def setAliasTargetObjectId(self, id: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setAliasTargetObjectId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setAliasTargetObjectId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setAliasTargetObjectId(int id)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData22setAliasTargetObjectIdEi', id,
    )

  @overload(int)
  def setWrappedObjectIndex(self, wrappedObjectIndex: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setWrappedObjectIndex(int
    wrappedObjectIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setWrappedObjectIndex

    Parameters
    ----------

    wrappedObjectIndex : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setWrappedObjectIndex(int wrappedObjectIndex)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData21setWrappedObjectIndexEi',
        wrappedObjectIndex,
    )

  @overload(QTypeRevision)
  def setRevision(self, revision: QTypeRevision) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setRevision(QTypeRevision revision)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#setRevision

    Parameters
    ----------

    revision : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlPropertyData::setRevision(QTypeRevision revision)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData11setRevisionE13QTypeRevision',
        self._valueOf(revision),
    )

  @overload(QTypeRevision)
  def setTypeVersion(self, typeVersion: QTypeRevision) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setTypeVersion(QTypeRevision
    typeVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setTypeVersion

    Parameters
    ----------

    typeVersion : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlPropertyData::setTypeVersion(QTypeRevision typeVersion)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData14setTypeVersionE13QTypeRevision',
        self._valueOf(typeVersion),
    )

  @overload(QQmlPropertyCacheMethodArguments)
  @overload(NoneType)
  def setArguments(
      self,
      args: Optional[QQmlPropertyCacheMethodArguments],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPropertyData::setArguments(QQmlPropertyCacheMethodArguments *args)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#setArguments

    Parameters
    ----------

    args : Optional[QQmlPropertyCacheMethodArguments]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyData::setArguments(QQmlPropertyCacheMethodArguments
    #      *args)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData12setArgumentsEP32QQmlPropertyCacheMeth'
        'odArguments',
        self._addressOf(args),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def setMetaObject(self, metaObject: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setMetaObject(const QMetaObject
    *metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setMetaObject

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyData::setMetaObject(const QMetaObject *metaObject)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData13setMetaObjectEPK11QMetaObject',
        self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(int)
  def setMetaObjectOffset(self, off: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::setMetaObjectOffset(int off)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#setMetaObjectOffset

    Parameters
    ----------

    off : int
      Passed on as it is.
    """
    #  void QQmlPropertyData::setMetaObjectOffset(int off)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData19setMetaObjectOffsetEi', off,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a0: QQmlPropertyData) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyData::operator==(const QQmlPropertyData &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#operator==

    Parameters
    ----------

    a0 : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.
    """
    #  bool QQmlPropertyData::operator==(const QQmlPropertyData &a0) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlPropertyDataeqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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

  @overload(QMetaProperty)
  def load(self, a0: QMetaProperty) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::load(const QMetaProperty &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#load

    Parameters
    ----------

    a0 : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlPropertyData::load(const QMetaProperty &a0)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData4loadERK13QMetaProperty',
        self._valueOf(a0),
    )

  @overload(QMetaMethod)
  def load(self, a0: QMetaMethod) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::load(const QMetaMethod &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertydata.html#load

    Parameters
    ----------

    a0 : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QQmlPropertyData::load(const QMetaMethod &a0)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData4loadERK11QMetaMethod',
        self._valueOf(a0),
    )

  @overload(THIS)
  @overload(NoneType)
  def markAsOverrideOf(
      self,
      predecessor: Optional[QQmlPropertyData],
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyData::markAsOverrideOf(QQmlPropertyData
    *predecessor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertydata.html#markAsOverrideOf

    Parameters
    ----------

    predecessor : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyData::markAsOverrideOf(QQmlPropertyData *predecessor)
    self.uglySide.call(
        'ritual_ZN16QQmlPropertyData16markAsOverrideOfEPS_',
        self._addressOf(predecessor),
    )

  @staticmethod
  def doMetacall(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyData::doMetacall': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlPropertyData.doMetacall' has no cute function yet. Qt's "
        "'QQmlPropertyData::doMetacall': a template: a pattern and no "
        "single function.")

  @staticmethod
  def readProperty(*__, **_) -> Never:
    """
    Qt's 'void QQmlPropertyData::readProperty(QObject *target, void
    *property) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyData.readProperty' has no cute function yet. Qt's "
        "'void QQmlPropertyData::readProperty(QObject *target, void "
        "*property) const': names 'void', which has no cute class yet.")

  @staticmethod
  def readPropertyWithArgs(*__, **_) -> Never:
    """
    Qt's 'void QQmlPropertyData::readPropertyWithArgs(QObject *target, void
    **args) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyData.readPropertyWithArgs' has no cute function yet. "
        "Qt's 'void QQmlPropertyData::readPropertyWithArgs(QObject *target, "
        "void **args) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def staticMetaCallFunction(*__, **_) -> Never:
    """
    Qt's 'StaticMetaCallFunction QQmlPropertyData::staticMetaCallFunction()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyData.staticMetaCallFunction' has no cute function "
        "yet. Qt's 'StaticMetaCallFunction "
        "QQmlPropertyData::staticMetaCallFunction() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def trySetStaticMetaCallFunction(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlPropertyData::trySetStaticMetaCallFunction(StaticMetaCallFunction f,
    unsigned int relativePropertyIndex)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyData.trySetStaticMetaCallFunction' has no cute "
        "function yet. Qt's 'void "
        "QQmlPropertyData::trySetStaticMetaCallFunction(StaticMetaCallFuncti"
        "on f, unsigned int relativePropertyIndex)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def writeProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPropertyData::writeProperty(QObject *target, void *value,
    WriteFlags flags) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyData.writeProperty' has no cute function yet. Qt's "
        "'bool QQmlPropertyData::writeProperty(QObject *target, void "
        "*value, WriteFlags flags) const': names 'void', which has no cute "
        "class yet.")
