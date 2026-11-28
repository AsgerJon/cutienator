"""
SignalHandlerResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means SignalHandlerResolver to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
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


class SignalHandlerResolver(QQmlCompilePass):
  """
  The cute side of Qt's SignalHandlerResolver: a plain Python object standing
  in front of one C++ SignalHandlerResolver.

  It is built on the cute 'QQmlCompilePass', as Qt's SignalHandlerResolver is
  built on Qt's QQmlCompilePass, and has everything that class has.

  C++ hands a SignalHandlerResolver around as a copy, so every C++
  SignalHandlerResolver behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's SignalHandlerResolver that has a ritual and that
  Python can call so far, 2 names in all: 'tr',
  'resolveSignalHandlerExpressions'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SignalHandlerResolver::~SignalHandlerResolver()': the destructor:
    Python removes its C++ SignalHandlerResolver by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ SignalHandlerResolver is created at the first use, not by
    'SignalHandlerResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a SignalHandlerResolver back gives a copy the ritual
    made for Python, in a new cute SignalHandlerResolver.
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
    Calls Qt's 'QString SignalHandlerResolver::tr(const char *sourceText,
    const char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/signalhandlerresolver.html#tr

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
    #  QString SignalHandlerResolver::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN21SignalHandlerResolver2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SignalHandlerResolver'

  #  Qt's '~SignalHandlerResolver()'. Naming it makes this a value class:
  #  Python owns every C++ SignalHandlerResolver behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21SignalHandlerResolverD1Ev'

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
    'SignalHandlerResolver::SignalHandlerResolver(QQmlTypeCompiler
    *typeCompiler)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/signalhandlerresolver.html#SignalHandlerResolver

    Parameters
    ----------

    typeCompiler : Optional[QQmlTypeCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  SignalHandlerResolver::SignalHandlerResolver(QQmlTypeCompiler
    #      *typeCompiler)
    self._noteCreation(SignalHandlerResolver, lambda: Rituals.call(
        'ritual_ZN21SignalHandlerResolverC1EP16QQmlTypeCompiler',
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

  def resolveSignalHandlerExpressions(self) -> bool:
    """
    Calls Qt's 'bool
    SignalHandlerResolver::resolveSignalHandlerExpressions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signalhandlerresolver.html
    """
    #  bool SignalHandlerResolver::resolveSignalHandlerExpressions()
    return self.uglySide.call(
        'ritual_ZN21SignalHandlerResolver31resolveSignalHandlerExpressionsE'
        'v',
    )
