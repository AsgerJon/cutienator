"""
QLatin1StringMatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlatin1stringmatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']


class QLatin1StringMatcher(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLatin1StringMatcher: a plain Python object standing
  in front of one C++ QLatin1StringMatcher.

  C++ hands a QLatin1StringMatcher around as a copy, so every C++
  QLatin1StringMatcher behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLatin1StringMatcher that has a ritual and that
  Python can call so far, 5 names in all: 'setPattern', 'pattern',
  'setCaseSensitivity', 'caseSensitivity', 'indexIn'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLatin1StringMatcher::~QLatin1StringMatcher()': the destructor:
    Python removes its C++ QLatin1StringMatcher by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 2 private; 1 a template.

  What to expect
  --------------

  - The C++ QLatin1StringMatcher is created at the first use, not by
    'QLatin1StringMatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLatin1StringMatcher back gives a copy the ritual
    made for Python, in a new cute QLatin1StringMatcher.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLatin1StringMatcher'

  #  Qt's '~QLatin1StringMatcher()'. Naming it makes this a value class:
  #  Python owns every C++ QLatin1StringMatcher behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QLatin1StringMatcherD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pattern(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QLatin1StringMatcher::pattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1stringmatcher.html#pattern

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QLatin1StringMatcher::pattern() const
    address = self.uglySide.call(
        'ritual_ZNK20QLatin1StringMatcher7patternEv',
    )
    from . import QLatin1String
    return QLatin1String._cuteOwning(address)

  def caseSensitivity(self) -> Qt.CaseSensitivity:
    """
    Calls Qt's 'Qt::CaseSensitivity QLatin1StringMatcher::caseSensitivity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlatin1stringmatcher.html#caseSensitivity

    Returns
    -------

    Qt.CaseSensitivity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CaseSensitivity(number)' gives.
    """
    #  Qt::CaseSensitivity QLatin1StringMatcher::caseSensitivity() const
    return Qt.CaseSensitivity(self.uglySide.call(
        'ritual_ZNK20QLatin1StringMatcher15caseSensitivityEv',
    ))

  @overload(QLatin1String)
  @overload(QLatin1String, int)
  def indexIn(self, haystack: QLatin1String, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QLatin1StringMatcher::indexIn(QLatin1StringView
    haystack, qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1stringmatcher.html#indexIn

    Parameters
    ----------

    haystack : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QLatin1StringMatcher::indexIn(QLatin1StringView haystack,
    #      qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK20QLatin1StringMatcher7indexInE13QLatin1Stringx',
        self._valueOf(haystack), from_,
    )

  @overload(str)
  @overload(str, int)
  def indexIn(self, haystack: str, from_: int = 0) -> int:
    """
    Calls Qt's 'qsizetype QLatin1StringMatcher::indexIn(QStringView haystack,
    qsizetype from) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatin1stringmatcher.html#indexIn

    Parameters
    ----------

    haystack : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  qsizetype QLatin1StringMatcher::indexIn(QStringView haystack,
    #      qsizetype from) const
    return self.uglySide.call(
        'ritual_ZNK20QLatin1StringMatcher7indexInE11QStringViewx',
        haystack, from_,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLatin1String)
  def setPattern(self, pattern: QLatin1String) -> None:
    """
    Calls Qt's 'void QLatin1StringMatcher::setPattern(QLatin1StringView
    pattern)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlatin1stringmatcher.html#setPattern

    Parameters
    ----------

    pattern : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QLatin1StringMatcher::setPattern(QLatin1StringView pattern)
    self.uglySide.call(
        'ritual_ZN20QLatin1StringMatcher10setPatternE13QLatin1String',
        self._valueOf(pattern),
    )

  @overload(Qt.CaseSensitivity)
  def setCaseSensitivity(self, cs: Qt.CaseSensitivity) -> None:
    """
    Calls Qt's 'void
    QLatin1StringMatcher::setCaseSensitivity(Qt::CaseSensitivity cs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlatin1stringmatcher.html#setCaseSensitivity

    Parameters
    ----------

    cs : Qt.CaseSensitivity
      Passed on as its number.
    """
    #  void QLatin1StringMatcher::setCaseSensitivity(Qt::CaseSensitivity cs)
    self.uglySide.call(
        'ritual_ZN20QLatin1StringMatcher18setCaseSensitivityEN2Qt15CaseSens'
        'itivityE',
        cs.value,
    )

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
    'QLatin1StringMatcher::QLatin1StringMatcher()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlatin1stringmatcher.html#QLatin1StringMatcher
    """
    #  QLatin1StringMatcher::QLatin1StringMatcher()
    self._noteCreation(QLatin1StringMatcher, lambda: Rituals.call(
        'ritual_ZN20QLatin1StringMatcherC1Ev',
    ))

  @overload(QLatin1String)
  @overload(QLatin1String, Qt.CaseSensitivity)
  def __init__(
      self,
      pattern: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QLatin1StringMatcher::QLatin1StringMatcher(QLatin1StringView pattern,
    Qt::CaseSensitivity cs)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlatin1stringmatcher.html#QLatin1StringMatcher

    Parameters
    ----------

    pattern : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  QLatin1StringMatcher::QLatin1StringMatcher(QLatin1StringView pattern,
    #      Qt::CaseSensitivity cs)
    self._noteCreation(QLatin1StringMatcher, lambda: Rituals.call(
        'ritual_ZN20QLatin1StringMatcherC1E13QLatin1StringN2Qt15CaseSensiti'
        'vityE',
        self._valueOf(pattern), cs.value,
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
