"""
QQmlTranslationPropertyBindingFunctorBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlTranslationPropertyBindingFunctorBase to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlTranslationPropertyBindingFunctorBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTranslationPropertyBindingFunctorBase: a plain
  Python object standing in front of one C++
  QQmlTranslationPropertyBindingFunctorBase.

  C++ hands a QQmlTranslationPropertyBindingFunctorBase around as a copy, so
  every C++ QQmlTranslationPropertyBindingFunctorBase behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlTranslationPropertyBindingFunctorBase yet. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlRefPointer<QV4::ExecutableCompilationUnit>
    &QQmlTranslationPropertyBindingFunctorBase::compilationUnit() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlTranslationPropertyBindingFunctorBase::
    QQmlTranslationPropertyBindingFunctorBase(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QQmlTranslationPropertyBindingFunctorBase::
    ~QQmlTranslationPropertyBindingFunctorBase()': the destructor: Python
    removes its C++ QQmlTranslationPropertyBindingFunctorBase by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlTranslationPropertyBindingFunctorBase is created at the first
    use, not by 'QQmlTranslationPropertyBindingFunctorBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTranslationPropertyBindingFunctorBase back gives
    a copy the ritual made for Python, in a new cute
    QQmlTranslationPropertyBindingFunctorBase.
  - Each name of Qt's QQmlTranslationPropertyBindingFunctorBase that has no
    cute function yet, '__init__', 'compilationUnit', 'translate', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTranslationPropertyBindingFunctorBase'

  #  Qt's '~QQmlTranslationPropertyBindingFunctorBase()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QQmlTranslationPropertyBindingFunctorBase behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN41QQmlTranslationPropertyBindingFunctorBaseD1Ev')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlTranslationPropertyBindingFunctorBase::
    QQmlTranslationPropertyBindingFunctorBase(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTranslationPropertyBindingFunctorBase.__init__' has no cute "
        "function yet. Qt's "
        "'QQmlTranslationPropertyBindingFunctorBase::QQmlTranslationProperty"
        "BindingFunctorBase(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': "
        "takes a type Python has no way to hand over yet.")

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
    Qt's 'const QQmlRefPointer<QV4::ExecutableCompilationUnit>
    &QQmlTranslationPropertyBindingFunctorBase::compilationUnit() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTranslationPropertyBindingFunctorBase.compilationUnit' has no "
        "cute function yet. Qt's 'const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "&QQmlTranslationPropertyBindingFunctorBase::compilationUnit() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def translate(*__, **_) -> Never:
    """
    Qt's 'QQmlTranslationPropertyBindingFunctorBase::translate': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlTranslationPropertyBindingFunctorBase.translate' has no cute "
        "function yet. Qt's "
        "'QQmlTranslationPropertyBindingFunctorBase::translate': a "
        "template: a pattern and no single function.")
