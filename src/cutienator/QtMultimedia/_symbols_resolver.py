"""
SymbolsResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsymbolsresolveutils_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means SymbolsResolver to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SymbolsResolver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's SymbolsResolver: a plain Python object standing in
  front of one C++ SymbolsResolver.

  What exists
  -----------

  Every function of Qt's SymbolsResolver that has a ritual and that Python
  can call so far, 2 names in all: 'isLazyLoadEnabled', 'isLoaded'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'SymbolsResolver::~SymbolsResolver()': the destructor: Python never
    removes a C++ SymbolsResolver.
  - Qt's 'SymbolsResolver::SymbolsResolver(const char *libLoggingName,
    LibraryLoader loader)': takes a type Python has no way to hand over yet.
  - Qt's 'QFunctionPointer SymbolsResolver::initOptionalFunction(const char
    *name)': gives a type Python has no way to take yet.
  - Qt's 'QFunctionPointer SymbolsResolver::initFunction(const char *name)':
    gives a type Python has no way to take yet.
  - Qt's 'void SymbolsResolver::checkLibrariesLoaded(SymbolsMarker *begin,
    SymbolsMarker *end)': names 'SymbolsResolver::SymbolsMarker', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ SymbolsResolver is created at the first use, not by
    'SymbolsResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SymbolsResolver.
  - Each name of Qt's SymbolsResolver that has no cute function yet,
    'checkLibrariesLoaded', 'initFunction', 'initOptionalFunction', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isLazyLoadEnabled() -> bool:
    """
    Calls Qt's 'bool SymbolsResolver::isLazyLoadEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/symbolsresolver.html#isLazyLoadEnabled
    """
    #  bool SymbolsResolver::isLazyLoadEnabled()
    return Rituals.call('ritual_ZN15SymbolsResolver17isLazyLoadEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SymbolsResolver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isLoaded(self) -> bool:
    """
    Calls Qt's 'bool SymbolsResolver::isLoaded() const'.

    Qt's own words: https://doc.qt.io/qt-6/symbolsresolver.html#isLoaded
    """
    #  bool SymbolsResolver::isLoaded() const
    return self.uglySide.call('ritual_ZNK15SymbolsResolver8isLoadedEv')

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

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, str)
  @overload(str, str, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(NoneType, str, str)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, str)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      libName: Optional[str],
      version: Optional[str],
      libLoggingName: Optional[str] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'SymbolsResolver::SymbolsResolver(const
    char *libName, const char *version, const char *libLoggingName)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/symbolsresolver.html#SymbolsResolver

    Parameters
    ----------

    libName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    version : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    libLoggingName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.
    """
    #  SymbolsResolver::SymbolsResolver(const char *libName, const char
    #      *version, const char *libLoggingName)
    self._noteCreation(SymbolsResolver, lambda: Rituals.call(
        'ritual_ZN15SymbolsResolverC1EPKcS1_S1_',
        self._bytesOf(libName), self._bytesOf(version),
        self._bytesOf(libLoggingName),
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
  def checkLibrariesLoaded(*__, **_) -> Never:
    """
    Qt's 'void SymbolsResolver::checkLibrariesLoaded(SymbolsMarker *begin,
    SymbolsMarker *end)': names 'SymbolsResolver::SymbolsMarker', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'SymbolsResolver.checkLibrariesLoaded' has no cute function yet. "
        "Qt's 'void SymbolsResolver::checkLibrariesLoaded(SymbolsMarker "
        "*begin, SymbolsMarker *end)': names "
        "'SymbolsResolver::SymbolsMarker', which has no cute class yet.")

  @staticmethod
  def initFunction(*__, **_) -> Never:
    """
    Qt's 'QFunctionPointer SymbolsResolver::initFunction(const char *name)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SymbolsResolver.initFunction' has no cute function yet. Qt's "
        "'QFunctionPointer SymbolsResolver::initFunction(const char "
        "*name)': gives a type Python has no way to take yet.")

  @staticmethod
  def initOptionalFunction(*__, **_) -> Never:
    """
    Qt's 'QFunctionPointer SymbolsResolver::initOptionalFunction(const char
    *name)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SymbolsResolver.initOptionalFunction' has no cute function yet. "
        "Qt's 'QFunctionPointer SymbolsResolver::initOptionalFunction(const "
        "char *name)': gives a type Python has no way to take yet.")
