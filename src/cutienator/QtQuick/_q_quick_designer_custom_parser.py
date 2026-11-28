"""
QQuickDesignerCustomParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignercustomparserobject_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDesignerCustomParser to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtQml import QQmlCustomParser


class QQuickDesignerCustomParser(QQmlCustomParser):
  """
  The cute side of Qt's QQuickDesignerCustomParser: a plain Python object
  standing in front of one C++ QQuickDesignerCustomParser.

  It is built on the cute 'QQmlCustomParser', as Qt's
  QQuickDesignerCustomParser is built on Qt's QQmlCustomParser, and has
  everything that class has.

  C++ hands a QQuickDesignerCustomParser around as a copy, so every C++
  QQuickDesignerCustomParser behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQuickDesignerCustomParser yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickDesignerCustomParser::verifyBindings(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    const QList<const QV4::CompiledData::Binding *> &props)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuickDesignerCustomParser::applyBindings(QObject *obj, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QList<const QV4::CompiledData::Binding *> &bindings)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQuickDesignerCustomParser::~QQuickDesignerCustomParser()': the
    destructor: Python removes its C++ QQuickDesignerCustomParser by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickDesignerCustomParser is created at the first use, not by
    'QQuickDesignerCustomParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerCustomParser back gives a copy the
    ritual made for Python, in a new cute QQuickDesignerCustomParser.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerCustomParser'

  #  Qt's '~QQuickDesignerCustomParser()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickDesignerCustomParser behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuickDesignerCustomParserD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickDesignerCustomParser::QQuickDesignerCustomParser()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignercustomparser.html
    """
    #  QQuickDesignerCustomParser::QQuickDesignerCustomParser()
    self._noteCreation(QQuickDesignerCustomParser, lambda: Rituals.call(
        'ritual_ZN26QQuickDesignerCustomParserC1Ev',
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
