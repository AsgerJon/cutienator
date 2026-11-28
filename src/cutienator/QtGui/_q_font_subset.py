"""
QFontSubset binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontsubset_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFontSubset to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFontEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFontEngine = WAIT['QFontEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontSubset(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontSubset: a plain Python object standing in front
  of one C++ QFontSubset.

  C++ hands a QFontSubset around as a copy, so every C++ QFontSubset behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontSubset that has a ritual and that Python can
  call so far, 2 names in all: 'addGlyph', 'nGlyphs'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontSubset::~QFontSubset()': the destructor: Python removes its
    C++ QFontSubset by it, and has no other use for it.
  - Qt's 'QList<int> QFontSubset::getReverseMap() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QPdf.

  What to expect
  --------------

  - The C++ QFontSubset is created at the first use, not by
    'QFontSubset(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontSubset back gives a copy the ritual made for
    Python, in a new cute QFontSubset.
  - Each name of Qt's QFontSubset that has no cute function yet,
    'createToUnicodeMap', 'getReverseMap', 'glyphName', 'toTruetype',
    'widthArray', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontSubset'

  #  Qt's '~QFontSubset()'. Naming it makes this a value class: Python owns
  #  every C++ QFontSubset behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QFontSubsetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nGlyphs(self) -> int:
    """
    Calls Qt's 'qsizetype QFontSubset::nGlyphs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontsubset.html#nGlyphs
    """
    #  qsizetype QFontSubset::nGlyphs() const
    return self.uglySide.call('ritual_ZNK11QFontSubset7nGlyphsEv')

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

  @overload(QFontEngine)
  @overload(NoneType)
  @overload(QFontEngine, int)
  @overload(NoneType, int)
  def __init__(self, fe: Optional[QFontEngine], obj_id: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QFontSubset::QFontSubset(QFontEngine *fe,
    uint obj_id)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontsubset.html#QFontSubset

    Parameters
    ----------

    fe : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj_id : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QFontSubset::QFontSubset(QFontEngine *fe, uint obj_id)
    self._noteCreation(QFontSubset, lambda: Rituals.call(
        'ritual_ZN11QFontSubsetC1EP11QFontEnginej',
        self._addressOf(fe), obj_id,
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

  @overload(int)
  def addGlyph(self, index: int) -> int:
    """
    Calls Qt's 'qsizetype QFontSubset::addGlyph(uint index)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontsubset.html#addGlyph

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qsizetype QFontSubset::addGlyph(uint index)
    return self.uglySide.call('ritual_ZN11QFontSubset8addGlyphEj', index)

  @staticmethod
  def createToUnicodeMap(*__, **_) -> Never:
    """
    Qt's 'QByteArray QFontSubset::createToUnicodeMap() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'checkRanges'.
    """
    raise NotImplementedError(
        "'QFontSubset.createToUnicodeMap' has no cute function yet. Qt's "
        "'QByteArray QFontSubset::createToUnicodeMap() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'checkRanges'.")

  @staticmethod
  def getReverseMap(*__, **_) -> Never:
    """
    Qt's 'QList<int> QFontSubset::getReverseMap() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QFontSubset.getReverseMap' has no cute function yet. Qt's "
        "'QList<int> QFontSubset::getReverseMap() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def glyphName(*__, **_) -> Never:
    """
    Qt's 'QByteArray QFontSubset::glyphName(unsigned short unicode, bool
    symbol)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'AGLEntry'.
    """
    raise NotImplementedError(
        "'QFontSubset.glyphName' has no cute function yet. Qt's 'QByteArray "
        "QFontSubset::glyphName(unsigned short unicode, bool symbol)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'AGLEntry'.")

  @staticmethod
  def toTruetype(*__, **_) -> Never:
    """
    Qt's 'QByteArray QFontSubset::toTruetype() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qttf_font_tables'.
    """
    raise NotImplementedError(
        "'QFontSubset.toTruetype' has no cute function yet. Qt's "
        "'QByteArray QFontSubset::toTruetype() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qttf_font_tables'.")

  @staticmethod
  def widthArray(*__, **_) -> Never:
    """
    Qt's 'QByteArray QFontSubset::widthArray() const': leans on
    'QPdf::ByteStream::operator<<(char const*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFontSubset.widthArray' has no cute function yet. Qt's "
        "'QByteArray QFontSubset::widthArray() const': leans on "
        "'QPdf::ByteStream::operator<<(char const*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
