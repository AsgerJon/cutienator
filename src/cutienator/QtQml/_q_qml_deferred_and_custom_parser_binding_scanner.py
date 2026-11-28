"""
QQmlDeferredAndCustomParserBindingScanner binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlDeferredAndCustomParserBindingScanner to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQmlCompilePass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlTypeCompiler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlTypeCompiler = WAIT['QQmlTypeCompiler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDeferredAndCustomParserBindingScanner(QQmlCompilePass):
  """
  The cute side of Qt's QQmlDeferredAndCustomParserBindingScanner: a plain
  Python object standing in front of one C++
  QQmlDeferredAndCustomParserBindingScanner.

  It is built on the cute 'QQmlCompilePass', as Qt's
  QQmlDeferredAndCustomParserBindingScanner is built on Qt's QQmlCompilePass,
  and has everything that class has.

  C++ hands a QQmlDeferredAndCustomParserBindingScanner around as a copy, so
  every C++ QQmlDeferredAndCustomParserBindingScanner behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlDeferredAndCustomParserBindingScanner that has a
  ritual and that Python can call so far, 1 name in all: 'tr'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDeferredAndCustomParserBindingScanner::
    ~QQmlDeferredAndCustomParserBindingScanner()': the destructor: Python
    removes its C++ QQmlDeferredAndCustomParserBindingScanner by it, and has
    no other use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQmlDeferredAndCustomParserBindingScanner.

  What to expect
  --------------

  - The C++ QQmlDeferredAndCustomParserBindingScanner is created at the first
    use, not by 'QQmlDeferredAndCustomParserBindingScanner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDeferredAndCustomParserBindingScanner back gives
    a copy the ritual made for Python, in a new cute
    QQmlDeferredAndCustomParserBindingScanner.
  - Each name of Qt's QQmlDeferredAndCustomParserBindingScanner that has no
    cute function yet, 'scanObject', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQmlDeferredAndCustomParserBindingScanner::tr(const
    char *sourceText, const char *disambiguation, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldeferredandcustomparserbindingscanner.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDeferredAndCustomParserBindingScanner::tr(const char
    #      *sourceText, const char *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN41QQmlDeferredAndCustomParserBindingScanner2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDeferredAndCustomParserBindingScanner'

  #  Qt's '~QQmlDeferredAndCustomParserBindingScanner()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QQmlDeferredAndCustomParserBindingScanner behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN41QQmlDeferredAndCustomParserBindingScannerD1Ev')

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
    'QQmlDeferredAndCustomParserBindingScanner::
    QQmlDeferredAndCustomParserBindingScanner(QQmlTypeCompiler
    *typeCompiler)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldeferredandcustomparserbindingscanner.html

    Parameters
    ----------

    typeCompiler : Optional[QQmlTypeCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlDeferredAndCustomParserBindingScanner::
    #      QQmlDeferredAndCustomParserBindingScanner(QQmlTypeCompiler
    #      *typeCompiler)
    self._noteCreation(
        QQmlDeferredAndCustomParserBindingScanner, lambda: Rituals.call(
            'ritual_ZN41QQmlDeferredAndCustomParserBindingScannerC1EP16QQml'
            'TypeCompiler',
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

  @staticmethod
  def scanObject(*__, **_) -> Never:
    """
    - Qt's 'bool QQmlDeferredAndCustomParserBindingScanner::scanObject(int
      objectIndex, ScopeDeferred scopeDeferred)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'COMPILE_EXCEPTION'.
    - Qt's 'bool QQmlDeferredAndCustomParserBindingScanner::scanObject()':
      leans on 'QQmlDeferredAndCustomParserBindingScanner::scanObject(int,
      QQmlDeferredAndCustomParserBindingScanner::ScopeDeferred)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QQmlDeferredAndCustomParserBindingScanner.scanObject' has no cute "
        "function yet. Qt's 'bool "
        "QQmlDeferredAndCustomParserBindingScanner::scanObject(int "
        "objectIndex, ScopeDeferred scopeDeferred)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'COMPILE_EXCEPTION'. "
        "Qt's 'bool "
        "QQmlDeferredAndCustomParserBindingScanner::scanObject()': leans on "
        "'QQmlDeferredAndCustomParserBindingScanner::scanObject(int, "
        "QQmlDeferredAndCustomParserBindingScanner::ScopeDeferred)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
