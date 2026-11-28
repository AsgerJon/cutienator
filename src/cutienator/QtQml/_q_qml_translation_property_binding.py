"""
QQmlTranslationPropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlTranslationPropertyBinding to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlTranslationPropertyBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTranslationPropertyBinding: a plain Python object
  standing in front of one C++ QQmlTranslationPropertyBinding.

  C++ hands a QQmlTranslationPropertyBinding around as a copy, so every C++
  QQmlTranslationPropertyBinding behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQmlTranslationPropertyBinding yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUntypedPropertyBinding
    QQmlTranslationPropertyBinding::create(const QQmlPropertyData *pd, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QV4::CompiledData::Binding *binding)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QUntypedPropertyBinding
    QQmlTranslationPropertyBinding::create(const QMetaType &propertyType,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
    const QQmlTranslation &translationData)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlTranslationPropertyBinding::compilationUnit(const
    QPropertyBindingPrivate *priv)': gives a type Python has no way to take
    yet.
  - Qt's 'QQmlTranslationPropertyBinding::~QQmlTranslationPropertyBinding()':
    the destructor: Python removes its C++ QQmlTranslationPropertyBinding by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlTranslationPropertyBinding is created at the first use, not
    by 'QQmlTranslationPropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTranslationPropertyBinding back gives a copy the
    ritual made for Python, in a new cute QQmlTranslationPropertyBinding.
  - Each name of Qt's QQmlTranslationPropertyBinding that has no cute
    function yet, 'compilationUnit', 'create', holds a function that raises
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
  __qt_class__ = 'QQmlTranslationPropertyBinding'

  #  Qt's '~QQmlTranslationPropertyBinding()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlTranslationPropertyBinding behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QQmlTranslationPropertyBindingD1Ev'

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
  def compilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlTranslationPropertyBinding::compilationUnit(const
    QPropertyBindingPrivate *priv)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlTranslationPropertyBinding.compilationUnit' has no cute "
        "function yet. Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "QQmlTranslationPropertyBinding::compilationUnit(const "
        "QPropertyBindingPrivate *priv)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    - Qt's 'QUntypedPropertyBinding
      QQmlTranslationPropertyBinding::create(const QQmlPropertyData *pd,
      const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
      const QV4::CompiledData::Binding *binding)': takes a type Python has no
      way to hand over yet.
    - Qt's 'QUntypedPropertyBinding
      QQmlTranslationPropertyBinding::create(const QMetaType &propertyType,
      const QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
      const QQmlTranslation &translationData)': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTranslationPropertyBinding.create' has no cute function yet. "
        "Qt's 'QUntypedPropertyBinding "
        "QQmlTranslationPropertyBinding::create(const QQmlPropertyData *pd, "
        "const QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "&compilationUnit, const QV4::CompiledData::Binding *binding)': "
        "takes a type Python has no way to hand over yet. Qt's "
        "'QUntypedPropertyBinding "
        "QQmlTranslationPropertyBinding::create(const QMetaType "
        "&propertyType, const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, "
        "const QQmlTranslation &translationData)': takes a type Python has "
        "no way to hand over yet.")
