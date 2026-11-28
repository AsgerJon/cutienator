"""
QV4::CompiledData::Binding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Binding to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals


class Binding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Binding: a plain Python object
  standing in front of one C++ QV4::CompiledData::Binding.

  C++ hands a QV4::CompiledData::Binding around as a copy, so every C++
  QV4::CompiledData::Binding behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Binding that has a ritual and
  that Python can call so far, 19 names in all: 'clearFlags', 'setFlag',
  'hasFlag', 'flags', 'setType', 'type', 'hasSignalHandlerBindingFlag',
  'isValueBinding', 'isValueBindingNoAlias', 'isValueBindingToAlias',
  'isSignalHandler', 'isAttachedProperty', 'isGroupProperty',
  'isFunctionExpression', 'escapedString', 'isTranslationBinding',
  'evaluatesToString', 'isNumberBinding', 'valueAsBoolean'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::Binding::~Binding()': the destructor: Python
    removes its C++ QV4::CompiledData::Binding by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Binding is created at the first use, not by
    'QV4::CompiledData::Binding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Binding back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::Binding.
  """

  #  The enums Qt writes inside QV4::CompiledData::Binding, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QV4::CompiledData::Binding::Flag' of Qt, with the 11
    names Qt gives in it. Qt names the type of its combinations
    'QV4::CompiledData::Binding::Flags'.
    """

    IsSignalHandlerExpression = 0x1
    IsSignalHandlerObject = 0x2
    IsOnAssignment = 0x4
    InitializerForReadOnlyDeclaration = 0x8
    IsResolvedEnum = 0x10
    IsListItem = 0x20
    IsBindingToAlias = 0x40
    IsDeferredBinding = 0x80
    IsCustomParserBinding = 0x100
    IsFunctionExpression = 0x200
    IsPropertyObserver = 0x400

  Flags = Flag

  class Type(CuteNum):
    """
    The enum 'QV4::CompiledData::Binding::Type' of Qt, with the 11 names Qt
    gives in it.
    """

    Type_Invalid = Kee[int](0)
    Type_Boolean = Kee[int](1)
    Type_Number = Kee[int](2)
    Type_String = Kee[int](3)
    Type_Null = Kee[int](4)
    Type_Translation = Kee[int](5)
    Type_TranslationById = Kee[int](6)
    Type_Script = Kee[int](7)
    Type_Object = Kee[int](8)
    Type_AttachedProperty = Kee[int](9)
    Type_GroupProperty = Kee[int](10)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def escapedString(string: str) -> str:
    """
    Calls Qt's 'QString QV4::CompiledData::Binding::escapedString(const
    QString &string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#escapedString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::Binding::escapedString(const QString
    #      &string)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData7Binding13escapedStringERK7QString',
        string,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Binding'

  #  Qt's '~QV4::CompiledData::Binding()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::Binding behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData7BindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flag)
  def hasFlag(self, flag: Flag) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::hasFlag(Flag flag) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#hasFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.
    """
    #  bool QV4::CompiledData::Binding::hasFlag(Flag flag) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding7hasFlagENS1_4FlagE',
        flag.value,
    )

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QV4::CompiledData::Binding::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QV4::CompiledData::Binding::flags() const
    return Binding.Flags(self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding5flagsEv',
    ))

  def type(self) -> Type:
    """
    Calls Qt's 'Type QV4::CompiledData::Binding::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-binding.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QV4::CompiledData::Binding::type() const
    return Binding.Type(self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding4typeEv',
    ))

  def hasSignalHandlerBindingFlag(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::Binding::hasSignalHandlerBindingFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html
    """
    #  bool QV4::CompiledData::Binding::hasSignalHandlerBindingFlag() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding27hasSignalHandlerBindingFlagE'
        'v',
    )

  def isValueBinding(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isValueBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isValueBinding
    """
    #  bool QV4::CompiledData::Binding::isValueBinding() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding14isValueBindingEv',
    )

  def isValueBindingNoAlias(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isValueBindingNoAlias()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html
    """
    #  bool QV4::CompiledData::Binding::isValueBindingNoAlias() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding21isValueBindingNoAliasEv',
    )

  def isValueBindingToAlias(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isValueBindingToAlias()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html
    """
    #  bool QV4::CompiledData::Binding::isValueBindingToAlias() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding21isValueBindingToAliasEv',
    )

  def isSignalHandler(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isSignalHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isSignalHandler
    """
    #  bool QV4::CompiledData::Binding::isSignalHandler() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding15isSignalHandlerEv',
    )

  def isAttachedProperty(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isAttachedProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isAttachedProperty
    """
    #  bool QV4::CompiledData::Binding::isAttachedProperty() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding18isAttachedPropertyEv',
    )

  def isGroupProperty(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isGroupProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isGroupProperty
    """
    #  bool QV4::CompiledData::Binding::isGroupProperty() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding15isGroupPropertyEv',
    )

  def isFunctionExpression(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isFunctionExpression()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isFunctionExpression
    """
    #  bool QV4::CompiledData::Binding::isFunctionExpression() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding20isFunctionExpressionEv',
    )

  def isTranslationBinding(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isTranslationBinding()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isTranslationBinding
    """
    #  bool QV4::CompiledData::Binding::isTranslationBinding() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding20isTranslationBindingEv',
    )

  def evaluatesToString(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::evaluatesToString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#evaluatesToString
    """
    #  bool QV4::CompiledData::Binding::evaluatesToString() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding17evaluatesToStringEv',
    )

  def isNumberBinding(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::isNumberBinding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#isNumberBinding
    """
    #  bool QV4::CompiledData::Binding::isNumberBinding() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding15isNumberBindingEv',
    )

  def valueAsBoolean(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Binding::valueAsBoolean() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#valueAsBoolean
    """
    #  bool QV4::CompiledData::Binding::valueAsBoolean() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7Binding14valueAsBooleanEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flag)
  def setFlag(self, flag: Flag) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Binding::setFlag(Flag flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#setFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.
    """
    #  void QV4::CompiledData::Binding::setFlag(Flag flag)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData7Binding7setFlagENS1_4FlagE', flag.value,
    )

  @overload(Type)
  def setType(self, type: Type) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Binding::setType(Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#setType

    Parameters
    ----------

    type : Type
      Passed on as its number.
    """
    #  void QV4::CompiledData::Binding::setType(Type type)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData7Binding7setTypeENS1_4TypeE', type.value,
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

  def clearFlags(self) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Binding::clearFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-binding.html#clearFlags
    """
    #  void QV4::CompiledData::Binding::clearFlags()
    self.uglySide.call('ritual_ZN3QV412CompiledData7Binding10clearFlagsEv')
