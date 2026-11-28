"""
QV4::CompiledData::ParameterType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::ParameterType to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute


class ParameterType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::ParameterType: a plain Python
  object standing in front of one C++ QV4::CompiledData::ParameterType.

  C++ hands a QV4::CompiledData::ParameterType around as a copy, so every C++
  QV4::CompiledData::ParameterType behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::ParameterType that has a ritual
  and that Python can call so far, 4 names in all: 'set',
  'indexIsCommonType', 'isList', 'typeNameIndexOrCommonType'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::ParameterType::~ParameterType()': the
    destructor: Python removes its C++ QV4::CompiledData::ParameterType by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::ParameterType is created at the first use, not
    by 'QV4::CompiledData::ParameterType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::ParameterType back gives a copy
    the ritual made for Python, in a new cute
    QV4::CompiledData::ParameterType.
  """

  #  The enums Qt writes inside QV4::CompiledData::ParameterType, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QV4::CompiledData::ParameterType::Flag' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QV4::CompiledData::ParameterType::Flags'.
    """

    NoFlag = 0x0
    Common = 0x1
    List = 0x2

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::ParameterType'

  #  Qt's '~QV4::CompiledData::ParameterType()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::ParameterType behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData13ParameterTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def indexIsCommonType(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::ParameterType::indexIsCommonType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-parametertype.html
    """
    #  bool QV4::CompiledData::ParameterType::indexIsCommonType() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData13ParameterType17indexIsCommonTypeEv',
    )

  def isList(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::ParameterType::isList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-parametertype.html#isList
    """
    #  bool QV4::CompiledData::ParameterType::isList() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData13ParameterType6isListEv',
    )

  def typeNameIndexOrCommonType(self) -> int:
    """
    Calls Qt's 'quint32
    QV4::CompiledData::ParameterType::typeNameIndexOrCommonType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-parametertype.html
    """
    #  quint32 QV4::CompiledData::ParameterType::typeNameIndexOrCommonType()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData13ParameterType25typeNameIndexOrCommon'
        'TypeEv',
    )

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

  @overload(Flags, int)
  def set(self, flags: Flags, typeNameIndexOrCommonType: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::ParameterType::set(Flags flags,
    quint32 typeNameIndexOrCommonType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-parametertype.html#set

    Parameters
    ----------

    flags : Flags
      Passed on as its number.

    typeNameIndexOrCommonType : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::ParameterType::set(Flags flags, quint32
    #      typeNameIndexOrCommonType)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData13ParameterType3setE6QFlagsINS1_4FlagEE'
        'j',
        flags.value, typeNameIndexOrCommonType,
    )
