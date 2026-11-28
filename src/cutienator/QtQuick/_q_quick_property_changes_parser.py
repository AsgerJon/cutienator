"""
QQuickPropertyChangesParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpropertychanges_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPropertyChangesParser to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtQml import QQmlCustomParser

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuickPropertyChangesParser(QQmlCustomParser):
  """
  The cute side of Qt's QQuickPropertyChangesParser: a plain Python object
  standing in front of one C++ QQuickPropertyChangesParser.

  It is built on the cute 'QQmlCustomParser', as Qt's
  QQuickPropertyChangesParser is built on Qt's QQmlCustomParser, and has
  everything that class has.

  C++ hands a QQuickPropertyChangesParser around as a copy, so every C++
  QQuickPropertyChangesParser behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQuickPropertyChangesParser yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickPropertyChangesParser::verifyList(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    const QV4::CompiledData::Binding *binding)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQuickPropertyChangesParser::verifyBindings(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    const QList<const QV4::CompiledData::Binding *> &props)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuickPropertyChangesParser::applyBindings(QObject *obj, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QList<const QV4::CompiledData::Binding *> &bindings)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQuickPropertyChangesParser::~QQuickPropertyChangesParser()': the
    destructor: Python removes its C++ QQuickPropertyChangesParser by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QQuickPropertyChangesParser.

  What to expect
  --------------

  - The C++ QQuickPropertyChangesParser is created at the first use, not by
    'QQuickPropertyChangesParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickPropertyChangesParser back gives a copy the
    ritual made for Python, in a new cute QQuickPropertyChangesParser.
  - Each name of Qt's QQuickPropertyChangesParser that has no cute function
    yet, '__init__', 'verifyList', holds a function that raises
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
  __qt_class__ = 'QQuickPropertyChangesParser'

  #  Qt's '~QQuickPropertyChangesParser()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickPropertyChangesParser behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QQuickPropertyChangesParserD1Ev'

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
    Qt's 'QQuickPropertyChangesParser::QQuickPropertyChangesParser()': leans
    on 'QQuickPropertyChangesParser::applyBindings(QObject*,
    QQmlRefPointer<QV4::ExecutableCompilationUnit> const&,
    QList<QV4::CompiledData::Binding const*> const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPropertyChangesParser.__init__' has no cute function yet. "
        "Qt's 'QQuickPropertyChangesParser::QQuickPropertyChangesParser()': "
        "leans on 'QQuickPropertyChangesParser::applyBindings(QObject*, "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> const&, "
        "QList<QV4::CompiledData::Binding const*> const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
  def verifyList(*__, **_) -> Never:
    """
    Qt's 'void QQuickPropertyChangesParser::verifyList(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    const QV4::CompiledData::Binding *binding)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyChangesParser.verifyList' has no cute function yet. "
        "Qt's 'void QQuickPropertyChangesParser::verifyList(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit, const QV4::CompiledData::Binding *binding)': "
        "takes a type Python has no way to hand over yet.")
