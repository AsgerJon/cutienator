"""
QQmlCustomParserScriptIndexer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlCustomParserScriptIndexer to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class QQmlCustomParserScriptIndexer(QQmlCompilePass):
  """
  The cute side of Qt's QQmlCustomParserScriptIndexer: a plain Python object
  standing in front of one C++ QQmlCustomParserScriptIndexer.

  It is built on the cute 'QQmlCompilePass', as Qt's
  QQmlCustomParserScriptIndexer is built on Qt's QQmlCompilePass, and has
  everything that class has.

  C++ hands a QQmlCustomParserScriptIndexer around as a copy, so every C++
  QQmlCustomParserScriptIndexer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlCustomParserScriptIndexer that has a ritual and
  that Python can call so far, 2 names in all:
  'annotateBindingsWithScriptStrings', 'scanObjectRecursively'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlCustomParserScriptIndexer::~QQmlCustomParserScriptIndexer()':
    the destructor: Python removes its C++ QQmlCustomParserScriptIndexer by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlCustomParserScriptIndexer is created at the first use, not by
    'QQmlCustomParserScriptIndexer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlCustomParserScriptIndexer back gives a copy the
    ritual made for Python, in a new cute QQmlCustomParserScriptIndexer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCustomParserScriptIndexer'

  #  Qt's '~QQmlCustomParserScriptIndexer()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlCustomParserScriptIndexer behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QQmlCustomParserScriptIndexerD1Ev'

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
    'QQmlCustomParserScriptIndexer::QQmlCustomParserScriptIndexer(
    QQmlTypeCompiler *typeCompiler)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcustomparserscriptindexer.html

    Parameters
    ----------

    typeCompiler : Optional[QQmlTypeCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlCustomParserScriptIndexer::QQmlCustomParserScriptIndexer(
    #      QQmlTypeCompiler *typeCompiler)
    self._noteCreation(QQmlCustomParserScriptIndexer, lambda: Rituals.call(
        'ritual_ZN29QQmlCustomParserScriptIndexerC1EP16QQmlTypeCompiler',
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

  def annotateBindingsWithScriptStrings(self) -> None:
    """
    Calls Qt's 'void
    QQmlCustomParserScriptIndexer::annotateBindingsWithScriptStrings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcustomparserscriptindexer.html
    """
    #  void
    #      QQmlCustomParserScriptIndexer::annotateBindingsWithScriptStrings()
    self.uglySide.call(
        'ritual_ZN29QQmlCustomParserScriptIndexer33annotateBindingsWithScri'
        'ptStringsEv',
    )

  @overload(int)
  @overload(int, bool)
  def scanObjectRecursively(
      self,
      objectIndex: int,
      annotateScriptBindings: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQmlCustomParserScriptIndexer::scanObjectRecursively(int
    objectIndex, bool annotateScriptBindings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcustomparserscriptindexer.html

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    annotateScriptBindings : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQmlCustomParserScriptIndexer::scanObjectRecursively(int
    #      objectIndex, bool annotateScriptBindings)
    self.uglySide.call(
        'ritual_ZN29QQmlCustomParserScriptIndexer21scanObjectRecursivelyEib',
        objectIndex, annotateScriptBindings,
    )
