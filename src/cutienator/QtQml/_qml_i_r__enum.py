"""
QmlIR::Enum binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Enum to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Enum(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::Enum: a plain Python object standing in front
  of one C++ QmlIR::Enum.

  C++ hands a QmlIR::Enum around as a copy, so every C++ QmlIR::Enum behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QmlIR::Enum that has a ritual and that Python can
  call so far, 1 name in all: 'enumValueCount'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlIR::Enum::~Enum()': the destructor: Python removes its C++
    QmlIR::Enum by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QmlIR::Enum is created at the first use, not by
    'QmlIR::Enum(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::Enum back gives a copy the ritual made for
    Python, in a new cute QmlIR::Enum.
  - Each name of Qt's QmlIR::Enum that has no cute function yet,
    'enumValuesBegin', 'enumValuesEnd', holds a function that raises
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
  __qt_class__ = 'QmlIR::Enum'

  #  Qt's '~QmlIR::Enum()'. Naming it makes this a value class: Python owns
  #  every C++ QmlIR::Enum behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR4EnumD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def enumValueCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Enum::enumValueCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-enum.html#enumValueCount
    """
    #  int QmlIR::Enum::enumValueCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR4Enum14enumValueCountEv')

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

  @staticmethod
  def enumValuesBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<EnumValue>::Iterator QmlIR::Enum::enumValuesBegin()
    const': the compiler refuses its ritual as it would be written here: no
    template named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Enum.enumValuesBegin' has no cute function yet. Qt's "
        "'PoolList<EnumValue>::Iterator QmlIR::Enum::enumValuesBegin() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def enumValuesEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<EnumValue>::Iterator QmlIR::Enum::enumValuesEnd() const':
    the compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Enum.enumValuesEnd' has no cute function yet. Qt's "
        "'PoolList<EnumValue>::Iterator QmlIR::Enum::enumValuesEnd() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")
