"""
QTextItemInt binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextItemInt to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QTextItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar
  from . import QFont, QFontEngine, QGlyphLayout, QScriptItem
  from . import QTextCharFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QFont = WAIT['QFont']
  QFontEngine = WAIT['QFontEngine']
  QGlyphLayout = WAIT['QGlyphLayout']
  QScriptItem = WAIT['QScriptItem']
  QTextCharFormat = WAIT['QTextCharFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextItemInt(QTextItem):
  """
  The cute side of Qt's QTextItemInt: a plain Python object standing in front
  of one C++ QTextItemInt.

  It is built on the cute 'QTextItem', as Qt's QTextItemInt is built on Qt's
  QTextItem, and has everything that class has.

  C++ hands a QTextItemInt around as a copy, so every C++ QTextItemInt behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextItemInt that has a ritual and that Python can
  call so far, 2 names in all: 'midItem', 'initWithScriptItem'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextItemInt::~QTextItemInt()': the destructor: Python removes its
    C++ QTextItemInt by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextItemInt is created at the first use, not by
    'QTextItemInt(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextItemInt back gives a copy the ritual made for
    Python, in a new cute QTextItemInt.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextItemInt'

  #  Qt's '~QTextItemInt()'. Naming it makes this a value class: Python owns
  #  every C++ QTextItemInt behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QTextItemIntD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFontEngine, int, int)
  @overload(NoneType, int, int)
  def midItem(
      self,
      fontEngine: Optional[QFontEngine],
      firstGlyphIndex: int,
      numGlyphs: int,
  ) -> QTextItemInt:
    """
    Calls Qt's 'QTextItemInt QTextItemInt::midItem(QFontEngine *fontEngine,
    int firstGlyphIndex, int numGlyphs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextitemint.html#midItem

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstGlyphIndex : int
      Passed on as it is.

    numGlyphs : int
      Passed on as it is.

    Returns
    -------

    QTextItemInt
      A new cute QTextItemInt around the copy Qt gave back. Python owns it.
    """
    #  QTextItemInt QTextItemInt::midItem(QFontEngine *fontEngine, int
    #      firstGlyphIndex, int numGlyphs) const
    address = self.uglySide.call(
        'ritual_ZNK12QTextItemInt7midItemEP11QFontEngineii',
        self._addressOf(fontEngine), firstGlyphIndex, numGlyphs,
    )
    return QTextItemInt._cuteOwning(address)

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
    Notes what was given, for Qt's 'QTextItemInt::QTextItemInt()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextitemint.html#QTextItemInt
    """
    #  QTextItemInt::QTextItemInt()
    self._noteCreation(QTextItemInt, lambda: Rituals.call(
        'ritual_ZN12QTextItemIntC1Ev',
    ))

  @overload(QScriptItem, QFont)
  @overload(QScriptItem, NoneType)
  @overload(QScriptItem, QFont, QTextCharFormat)
  @overload(QScriptItem, NoneType, QTextCharFormat)
  def __init__(
      self,
      si: QScriptItem,
      font: Optional[QFont],
      format: Optional[QTextCharFormat] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextItemInt::QTextItemInt(const
    QScriptItem &si, QFont *font, const QTextCharFormat &format)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextitemint.html#QTextItemInt

    Parameters
    ----------

    si : QScriptItem
      Passed on as a value: Qt reads the C++ QScriptItem, which stays
      Python's own.

    font : Optional[QFont]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[QTextCharFormat]
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own. May be left out, as in Qt: a new 'QTextCharFormat()' is
      then passed on.
    """
    #  QTextItemInt::QTextItemInt(const QScriptItem &si, QFont *font, const
    #      QTextCharFormat &format)
    if format is None:
      from . import QTextCharFormat
      format = QTextCharFormat()
    self._noteCreation(QTextItemInt, lambda: Rituals.call(
        'ritual_ZN12QTextItemIntC1ERK11QScriptItemP5QFontRK15QTextCharForma'
        't',
        self._valueOf(si), self._addressOf(font), self._valueOf(format),
    ))

  @overload(QGlyphLayout, QFont, QChar, int, QFontEngine)
  @overload(QGlyphLayout, QFont, QChar, int, NoneType)
  @overload(QGlyphLayout, QFont, NoneType, int, QFontEngine)
  @overload(QGlyphLayout, QFont, NoneType, int, NoneType)
  @overload(QGlyphLayout, NoneType, QChar, int, QFontEngine)
  @overload(QGlyphLayout, NoneType, QChar, int, NoneType)
  @overload(QGlyphLayout, NoneType, NoneType, int, QFontEngine)
  @overload(QGlyphLayout, NoneType, NoneType, int, NoneType)
  @overload(QGlyphLayout, QFont, QChar, int, QFontEngine, QTextCharFormat)
  @overload(QGlyphLayout, QFont, QChar, int, NoneType, QTextCharFormat)
  @overload(QGlyphLayout, QFont, NoneType, int, QFontEngine, QTextCharFormat)
  @overload(QGlyphLayout, QFont, NoneType, int, NoneType, QTextCharFormat)
  @overload(QGlyphLayout, NoneType, QChar, int, QFontEngine, QTextCharFormat)
  @overload(QGlyphLayout, NoneType, QChar, int, NoneType, QTextCharFormat)
  @overload(
      QGlyphLayout, NoneType, NoneType, int, QFontEngine, QTextCharFormat,
  )
  @overload(QGlyphLayout, NoneType, NoneType, int, NoneType, QTextCharFormat)
  def __init__(
      self,
      g: QGlyphLayout,
      font: Optional[QFont],
      chars: Optional[QChar],
      numChars: int,
      fe: Optional[QFontEngine],
      format: Optional[QTextCharFormat] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextItemInt::QTextItemInt(const
    QGlyphLayout &g, QFont *font, const QChar *chars, int numChars,
    QFontEngine *fe, const QTextCharFormat &format)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextitemint.html#QTextItemInt

    Parameters
    ----------

    g : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    font : Optional[QFont]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    chars : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    numChars : int
      Passed on as it is.

    fe : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : Optional[QTextCharFormat]
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own. May be left out, as in Qt: a new 'QTextCharFormat()' is
      then passed on.
    """
    #  QTextItemInt::QTextItemInt(const QGlyphLayout &g, QFont *font, const
    #      QChar *chars, int numChars, QFontEngine *fe, const QTextCharFormat
    #      &format)
    if format is None:
      from . import QTextCharFormat
      format = QTextCharFormat()
    self._noteCreation(QTextItemInt, lambda: Rituals.call(
        'ritual_ZN12QTextItemIntC1ERK12QGlyphLayoutP5QFontPK5QChariP11QFont'
        'EngineRK15QTextCharFormat',
        self._valueOf(g, 'QGlyphLayout'), self._addressOf(font),
        self._addressOf(chars), numChars, self._addressOf(fe),
        self._valueOf(format),
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

  @overload(QScriptItem)
  def initWithScriptItem(self, si: QScriptItem) -> None:
    """
    Calls Qt's 'void QTextItemInt::initWithScriptItem(const QScriptItem
    &si)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextitemint.html#initWithScriptItem

    Parameters
    ----------

    si : QScriptItem
      Passed on as a value: Qt reads the C++ QScriptItem, which stays
      Python's own.
    """
    #  void QTextItemInt::initWithScriptItem(const QScriptItem &si)
    self.uglySide.call(
        'ritual_ZN12QTextItemInt18initWithScriptItemERK11QScriptItem',
        self._valueOf(si),
    )
