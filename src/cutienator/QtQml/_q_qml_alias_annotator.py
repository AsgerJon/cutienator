"""
QQmlAliasAnnotator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlAliasAnnotator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlCompilePass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlTypeCompiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlTypeCompiler = WAIT['QQmlTypeCompiler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAliasAnnotator(QQmlCompilePass):
  """
  The cute side of Qt's QQmlAliasAnnotator: a plain Python object standing in
  front of one C++ QQmlAliasAnnotator.

  It is built on the cute 'QQmlCompilePass', as Qt's QQmlAliasAnnotator is
  built on Qt's QQmlCompilePass, and has everything that class has.

  C++ hands a QQmlAliasAnnotator around as a copy, so every C++
  QQmlAliasAnnotator behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlAliasAnnotator that has a ritual and that Python
  can call so far, 1 name in all: 'annotateBindingsToAliases'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlAliasAnnotator::~QQmlAliasAnnotator()': the destructor: Python
    removes its C++ QQmlAliasAnnotator by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlAliasAnnotator is created at the first use, not by
    'QQmlAliasAnnotator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlAliasAnnotator back gives a copy the ritual made
    for Python, in a new cute QQmlAliasAnnotator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAliasAnnotator'

  #  Qt's '~QQmlAliasAnnotator()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlAliasAnnotator behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlAliasAnnotatorD1Ev'

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

  @overload(QQmlTypeCompiler)
  @overload(NoneType)
  def __init__(self, typeCompiler: Optional[QQmlTypeCompiler]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlAliasAnnotator::QQmlAliasAnnotator(QQmlTypeCompiler *typeCompiler)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlaliasannotator.html#QQmlAliasAnnotator

    Parameters
    ----------

    typeCompiler : Optional[QQmlTypeCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlAliasAnnotator::QQmlAliasAnnotator(QQmlTypeCompiler *typeCompiler)
    self._noteCreation(QQmlAliasAnnotator, lambda: Rituals.call(
        'ritual_ZN18QQmlAliasAnnotatorC1EP16QQmlTypeCompiler',
        self._addressOf(typeCompiler),
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

  def annotateBindingsToAliases(self) -> None:
    """
    Calls Qt's 'void QQmlAliasAnnotator::annotateBindingsToAliases()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlaliasannotator.html#annotateBindingsToAliases
    """
    #  void QQmlAliasAnnotator::annotateBindingsToAliases()
    self.uglySide.call(
        'ritual_ZN18QQmlAliasAnnotator25annotateBindingsToAliasesEv',
    )
