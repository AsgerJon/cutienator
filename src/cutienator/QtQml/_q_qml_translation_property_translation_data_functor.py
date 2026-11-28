"""
QQmlTranslationPropertyTranslationDataFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlTranslationPropertyTranslationDataFunctor to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQmlTranslationPropertyBindingFunctorBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlTranslationPropertyTranslationDataFunctor(QQmlTranslationPropertyBindingFunctorBase):
  """
  The cute side of Qt's QQmlTranslationPropertyTranslationDataFunctor: a
  plain Python object standing in front of one C++
  QQmlTranslationPropertyTranslationDataFunctor.

  It is built on the cute 'QQmlTranslationPropertyBindingFunctorBase', as
  Qt's QQmlTranslationPropertyTranslationDataFunctor is built on Qt's
  QQmlTranslationPropertyBindingFunctorBase, and has everything that class
  has.

  C++ hands a QQmlTranslationPropertyTranslationDataFunctor around as a copy,
  so every C++ QQmlTranslationPropertyTranslationDataFunctor behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlTranslationPropertyTranslationDataFunctor yet. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTranslationPropertyTranslationDataFunctor::
    QQmlTranslationPropertyTranslationDataFunctor(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QQmlTranslation &translationData)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool
    QQmlTranslationPropertyTranslationDataFunctor::operator()(QMetaType
    metaType, void *dataPtr)': names 'void', which has no cute class yet.
  - Qt's 'QQmlTranslationPropertyTranslationDataFunctor::
    ~QQmlTranslationPropertyTranslationDataFunctor()': the destructor: Python
    removes its C++ QQmlTranslationPropertyTranslationDataFunctor by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlTranslationPropertyTranslationDataFunctor is created at the
    first use, not by 'QQmlTranslationPropertyTranslationDataFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTranslationPropertyTranslationDataFunctor back
    gives a copy the ritual made for Python, in a new cute
    QQmlTranslationPropertyTranslationDataFunctor.
  - Each name of Qt's QQmlTranslationPropertyTranslationDataFunctor that has
    no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QQmlTranslationPropertyTranslationDataFunctor'

  #  Qt's '~QQmlTranslationPropertyTranslationDataFunctor()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QQmlTranslationPropertyTranslationDataFunctor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN45QQmlTranslationPropertyTranslationDataFunctorD1Ev')

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
    Qt's 'QQmlTranslationPropertyTranslationDataFunctor::
    QQmlTranslationPropertyTranslationDataFunctor(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QQmlTranslation &translationData)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTranslationPropertyTranslationDataFunctor.__init__' has no "
        "cute function yet. Qt's "
        "'QQmlTranslationPropertyTranslationDataFunctor::QQmlTranslationProp"
        "ertyTranslationDataFunctor(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, "
        "const QQmlTranslation &translationData)': takes a type Python has "
        "no way to hand over yet.")

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
