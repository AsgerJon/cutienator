"""
QMimeGlobPattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeGlobPattern to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMimeGlobPattern(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeGlobPattern: a plain Python object standing in
  front of one C++ QMimeGlobPattern.

  C++ hands a QMimeGlobPattern around as a copy, so every C++
  QMimeGlobPattern behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMimeGlobPattern that has a ritual and that Python
  can call so far, 5 names in all: 'matchFileName', 'pattern', 'weight',
  'mimeType', 'isCaseSensitive'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMimeGlobPattern::swap(QMimeGlobPattern &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'PatternType QMimeGlobPattern::detectPatternType(QStringView
    pattern) const': gives the enum 'QMimeGlobPattern::PatternType', whose
    class cannot be named here.
  - Qt's 'QMimeGlobPattern::~QMimeGlobPattern()': the destructor: Python
    removes its C++ QMimeGlobPattern by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMimeGlobPattern is created at the first use, not by
    'QMimeGlobPattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMimeGlobPattern back gives a copy the ritual made
    for Python, in a new cute QMimeGlobPattern.
  - Each name of Qt's QMimeGlobPattern that has no cute function yet,
    'detectPatternType', 'swap', holds a function that raises
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
  __qt_class__ = 'QMimeGlobPattern'

  #  Qt's '~QMimeGlobPattern()'. Naming it makes this a value class: Python
  #  owns every C++ QMimeGlobPattern behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QMimeGlobPatternD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def matchFileName(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QMimeGlobPattern::matchFileName(const QString &fileName)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeglobpattern.html#matchFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeGlobPattern::matchFileName(const QString &fileName) const
    return self.uglySide.call(
        'ritual_ZNK16QMimeGlobPattern13matchFileNameERK7QString', fileName,
    )

  def pattern(self) -> str:
    """
    Calls Qt's 'const QString &QMimeGlobPattern::pattern() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeglobpattern.html#pattern

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QMimeGlobPattern::pattern() const
    return self.uglySide.call('ritual_ZNK16QMimeGlobPattern7patternEv')

  def weight(self) -> int:
    """
    Calls Qt's 'unsigned int QMimeGlobPattern::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeglobpattern.html#weight
    """
    #  unsigned int QMimeGlobPattern::weight() const
    return self.uglySide.call('ritual_ZNK16QMimeGlobPattern6weightEv')

  def mimeType(self) -> str:
    """
    Calls Qt's 'const QString &QMimeGlobPattern::mimeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeglobpattern.html#mimeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QMimeGlobPattern::mimeType() const
    return self.uglySide.call('ritual_ZNK16QMimeGlobPattern8mimeTypeEv')

  def isCaseSensitive(self) -> bool:
    """
    Calls Qt's 'bool QMimeGlobPattern::isCaseSensitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeglobpattern.html#isCaseSensitive
    """
    #  bool QMimeGlobPattern::isCaseSensitive() const
    return self.uglySide.call(
        'ritual_ZNK16QMimeGlobPattern15isCaseSensitiveEv',
    )

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

  @overload(str, str, int)
  @overload(str, str, int, Qt.CaseSensitivity)
  def __init__(
      self,
      thePattern: str,
      theMimeType: str,
      theWeight: int,
      s: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseInsensitive,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMimeGlobPattern::QMimeGlobPattern(const
    QString &thePattern, const QString &theMimeType, unsigned int theWeight,
    Qt::CaseSensitivity s)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeglobpattern.html#QMimeGlobPattern

    Parameters
    ----------

    thePattern : str
      Passed on as it is: a QString is made of it for the call.

    theMimeType : str
      Passed on as it is: a QString is made of it for the call.

    theWeight : int
      Passed on as it is.

    s : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseInsensitive.
    """
    #  QMimeGlobPattern::QMimeGlobPattern(const QString &thePattern, const
    #      QString &theMimeType, unsigned int theWeight, Qt::CaseSensitivity
    #      s)
    self._noteCreation(QMimeGlobPattern, lambda: Rituals.call(
        'ritual_ZN16QMimeGlobPatternC1ERK7QStringS2_jN2Qt15CaseSensitivityE',
        thePattern, theMimeType, theWeight, s.value,
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
  def detectPatternType(*__, **_) -> Never:
    """
    Qt's 'PatternType QMimeGlobPattern::detectPatternType(QStringView
    pattern) const': gives the enum 'QMimeGlobPattern::PatternType', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QMimeGlobPattern.detectPatternType' has no cute function yet. "
        "Qt's 'PatternType QMimeGlobPattern::detectPatternType(QStringView "
        "pattern) const': gives the enum 'QMimeGlobPattern::PatternType', "
        "whose class cannot be named here.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMimeGlobPattern::swap(QMimeGlobPattern &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeGlobPattern.swap' has no cute function yet. Qt's 'void "
        "QMimeGlobPattern::swap(QMimeGlobPattern &other)': takes a type "
        "Python has no way to hand over yet.")
