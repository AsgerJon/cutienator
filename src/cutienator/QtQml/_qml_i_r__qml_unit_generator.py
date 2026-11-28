"""
QmlIR::QmlUnitGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::QmlUnitGenerator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QmlUnitGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::QmlUnitGenerator: a plain Python object
  standing in front of one C++ QmlIR::QmlUnitGenerator.

  C++ hands a QmlIR::QmlUnitGenerator around as a copy, so every C++
  QmlIR::QmlUnitGenerator behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QmlIR::QmlUnitGenerator yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QmlIR::QmlUnitGenerator::generate(Document &output, const
    QV4::CompiledData::DependentTypesHasher &dependencyHasher)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QmlIR::QmlUnitGenerator::~QmlUnitGenerator()': the destructor:
    Python removes its C++ QmlIR::QmlUnitGenerator by it, and has no other
    use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QmlIR::QmlUnitGenerator is created at the first use, not by
    'QmlIR::QmlUnitGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::QmlUnitGenerator back gives a copy the ritual
    made for Python, in a new cute QmlIR::QmlUnitGenerator.
  - Each name of Qt's QmlIR::QmlUnitGenerator that has no cute function yet,
    'generate', 'writeBindings', holds a function that raises
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
  __qt_class__ = 'QmlIR::QmlUnitGenerator'

  #  Qt's '~QmlIR::QmlUnitGenerator()'. Naming it makes this a value class:
  #  Python owns every C++ QmlIR::QmlUnitGenerator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR16QmlUnitGeneratorD1Ev'

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
  def generate(*__, **_) -> Never:
    """
    Qt's 'void QmlIR::QmlUnitGenerator::generate(Document &output, const
    QV4::CompiledData::DependentTypesHasher &dependencyHasher)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QmlIR.QmlUnitGenerator.generate' has no cute function yet. Qt's "
        "'void QmlIR::QmlUnitGenerator::generate(Document &output, const "
        "QV4::CompiledData::DependentTypesHasher &dependencyHasher)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def writeBindings(*__, **_) -> Never:
    """
    Qt's 'char *QmlIR::QmlUnitGenerator::writeBindings(char *bindingPtr,
    const Object *o, BindingFilter filter) const': takes or gives a type that
    cannot be passed yet: bool (QmlIR::Binding::*)() const.
    """
    raise NotImplementedError(
        "'QmlIR.QmlUnitGenerator.writeBindings' has no cute function yet. "
        "Qt's 'char *QmlIR::QmlUnitGenerator::writeBindings(char "
        "*bindingPtr, const Object *o, BindingFilter filter) const': takes "
        "or gives a type that cannot be passed yet: bool "
        "(QmlIR::Binding::*)() const.")
