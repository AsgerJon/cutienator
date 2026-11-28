"""
QFontEngineMulti binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFontEngineMulti to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QFontEngine, QTextItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar, QLatin1String
  from . import QFixed, QFixedPoint, QFontVariableAxis, QGlyphLayout, QImage
  from . import QPainterPath, QTransform, glyph_metrics_t
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QFixedPoint = WAIT['QFixedPoint']
  QGlyphLayout = WAIT['QGlyphLayout']
  QLatin1String = WAIT['QLatin1String']
  QPainterPath = WAIT['QPainterPath']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontEngineMulti(QFontEngine):
  """
  The cute side of Qt's QFontEngineMulti: a plain Python object standing in
  front of one C++ QFontEngineMulti.

  It is built on the cute 'QFontEngine', as Qt's QFontEngineMulti is built on
  Qt's QFontEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFontEngineMulti that has a ritual and that Python
  can call so far, 34 names in all: 'glyphCount', 'glyphIndex',
  'boundingBox', 'recalcAdvances', 'doKerning', 'addOutlineToPath',
  'emSquareSize', 'ascent', 'capHeight', 'descent', 'leading', 'xHeight',
  'averageCharWidth', 'alphaMapForGlyph', 'alphaRGBMapForGlyph',
  'lineThickness', 'underlinePosition', 'maxCharWidth', 'minLeftBearing',
  'minRightBearing', 'variableAxes', 'canRender', 'glyphName', 'findGlyph',
  'fallbackFamilyCount', 'fallbackFamilyAt', 'setFallbackFamiliesList',
  'highByte', 'engine', 'ensureEngineAt', 'createMultiFontEngine',
  'ensureFallbackFamiliesQueried', 'shouldLoadFontEngineForCharacter',
  'loadEngine'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontEngineMulti::~QFontEngineMulti()': the destructor: Python
    never removes a C++ QFontEngineMulti.
  - Qt's 'int QFontEngineMulti::stringToCMap(const QChar *str, int len,
    QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const': takes a
    number to change where it is.
  - Qt's 'void QFontEngineMulti::getGlyphBearings(glyph_t glyph, qreal
    *leftBearing, qreal *rightBearing)': takes a number to change where it
    is.

  What to expect
  --------------

  - The C++ QFontEngineMulti is created at the first use, not by
    'QFontEngineMulti(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontEngineMulti.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def highByte(glyph: int) -> int:
    """
    Calls Qt's 'uchar QFontEngineMulti::highByte(glyph_t glyph)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#highByte

    Parameters
    ----------

    glyph : int
      Passed on as it is.
    """
    #  uchar QFontEngineMulti::highByte(glyph_t glyph)
    return Rituals.call('ritual_ZN16QFontEngineMulti8highByteEj', glyph)

  @staticmethod
  @overload(QFontEngine, int)
  @overload(NoneType, int)
  def createMultiFontEngine(
      fe: Optional[QFontEngine],
      script: int,
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine
    *QFontEngineMulti::createMultiFontEngine(QFontEngine *fe, int script)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#createMultiFontEngine

    Parameters
    ----------

    fe : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    script : int
      Passed on as it is.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontEngineMulti::createMultiFontEngine(QFontEngine *fe,
    #      int script)
    address = Rituals.call(
        'ritual_ZN16QFontEngineMulti21createMultiFontEngineEP11QFontEnginei',
        CuteMixin._addressOf(fe), script,
    )
    return QFontEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontEngineMulti'

  #  A C++ QFontEngineMulti Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontEngineMulti'

  #  The functions Qt calls itself that QFontEngineMulti is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'ensureFallbackFamiliesQueried': (
          ('_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'shouldLoadFontEngineForCharacter': (
          ('_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharacterEij',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'loadEngine': (
          ('_ZN16QFontEngineMulti10loadEngineEi',
           ('address', 'address', 'QtGui:QFontEngine'),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def glyphCount(self) -> int:
    """
    Calls Qt's 'int QFontEngineMulti::glyphCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#glyphCount
    """
    #  int QFontEngineMulti::glyphCount() const
    ritual = 'ritual_ZNK16QFontEngineMulti10glyphCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti10glyphCountEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def glyphIndex(self, ucs4: int) -> int:
    """
    Calls Qt's 'glyph_t QFontEngineMulti::glyphIndex(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#glyphIndex

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  glyph_t QFontEngineMulti::glyphIndex(uint ucs4) const
    ritual = 'ritual_ZNK16QFontEngineMulti10glyphIndexEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti10glyphIndexEj'
    return self.uglySide.call(ritual, ucs4)

  def emSquareSize(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::emSquareSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#emSquareSize

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::emSquareSize() const
    ritual = 'ritual_ZNK16QFontEngineMulti12emSquareSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti12emSquareSizeEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def ascent(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#ascent

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::ascent() const
    ritual = 'ritual_ZNK16QFontEngineMulti6ascentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti6ascentEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def capHeight(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::capHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#capHeight

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::capHeight() const
    ritual = 'ritual_ZNK16QFontEngineMulti9capHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti9capHeightEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def descent(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#descent

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::descent() const
    ritual = 'ritual_ZNK16QFontEngineMulti7descentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti7descentEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def leading(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#leading

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::leading() const
    ritual = 'ritual_ZNK16QFontEngineMulti7leadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti7leadingEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def xHeight(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::xHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#xHeight

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::xHeight() const
    ritual = 'ritual_ZNK16QFontEngineMulti7xHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti7xHeightEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def averageCharWidth(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::averageCharWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#averageCharWidth

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::averageCharWidth() const
    ritual = 'ritual_ZNK16QFontEngineMulti16averageCharWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti16averageCharWidthEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def lineThickness(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::lineThickness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#lineThickness

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::lineThickness() const
    ritual = 'ritual_ZNK16QFontEngineMulti13lineThicknessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti13lineThicknessEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def underlinePosition(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineMulti::underlinePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#underlinePosition

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineMulti::underlinePosition() const
    ritual = 'ritual_ZNK16QFontEngineMulti17underlinePositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti17underlinePositionEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def maxCharWidth(self) -> float:
    """
    Calls Qt's 'qreal QFontEngineMulti::maxCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#maxCharWidth
    """
    #  qreal QFontEngineMulti::maxCharWidth() const
    ritual = 'ritual_ZNK16QFontEngineMulti12maxCharWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti12maxCharWidthEv'
    return self.uglySide.call(ritual)

  def minLeftBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontEngineMulti::minLeftBearing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#minLeftBearing
    """
    #  qreal QFontEngineMulti::minLeftBearing() const
    ritual = 'ritual_ZNK16QFontEngineMulti14minLeftBearingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti14minLeftBearingEv'
    return self.uglySide.call(ritual)

  def minRightBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontEngineMulti::minRightBearing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#minRightBearing
    """
    #  qreal QFontEngineMulti::minRightBearing() const
    ritual = 'ritual_ZNK16QFontEngineMulti15minRightBearingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti15minRightBearingEv'
    return self.uglySide.call(ritual)

  def variableAxes(self) -> QList[QFontVariableAxis]:
    """
    Calls Qt's 'QList<QFontVariableAxis> QFontEngineMulti::variableAxes()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#variableAxes

    Returns
    -------

    QList[QFontVariableAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QFontVariableAxis> QFontEngineMulti::variableAxes() const
    address = self.uglySide.call(
        'ritual_ZNK16QFontEngineMulti12variableAxesEv',
    )
    from . import QFontVariableAxis
    return QList[QFontVariableAxis]._cuteOwning(address)

  @overload(QChar, int)
  @overload(NoneType, int)
  def canRender(self, string: Optional[QChar], len: int) -> bool:
    """
    Calls Qt's 'bool QFontEngineMulti::canRender(const QChar *string, int
    len) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#canRender

    Parameters
    ----------

    string : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.
    """
    #  bool QFontEngineMulti::canRender(const QChar *string, int len) const
    ritual = 'ritual_ZNK16QFontEngineMulti9canRenderEPK5QChari'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti9canRenderEPK5QChari'
    return self.uglySide.call(ritual, self._addressOf(string), len)

  @overload(int)
  def glyphName(self, glyph: int) -> str:
    """
    Calls Qt's 'QString QFontEngineMulti::glyphName(glyph_t glyph) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#glyphName

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontEngineMulti::glyphName(glyph_t glyph) const
    ritual = 'ritual_ZNK16QFontEngineMulti9glyphNameEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti9glyphNameEj'
    return self.uglySide.call(ritual, glyph)

  @overload(QLatin1String)
  def findGlyph(self, name: QLatin1String) -> int:
    """
    Calls Qt's 'glyph_t QFontEngineMulti::findGlyph(QLatin1StringView name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#findGlyph

    Parameters
    ----------

    name : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  glyph_t QFontEngineMulti::findGlyph(QLatin1StringView name) const
    ritual = 'ritual_ZNK16QFontEngineMulti9findGlyphE13QLatin1String'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QFontEngineMulti9findGlyphE13QLatin1String'
    return self.uglySide.call(ritual, self._valueOf(name))

  def fallbackFamilyCount(self) -> int:
    """
    Calls Qt's 'int QFontEngineMulti::fallbackFamilyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#fallbackFamilyCount
    """
    #  int QFontEngineMulti::fallbackFamilyCount() const
    return self.uglySide.call(
        'ritual_ZNK16QFontEngineMulti19fallbackFamilyCountEv',
    )

  @overload(int)
  def fallbackFamilyAt(self, at: int) -> str:
    """
    Calls Qt's 'QString QFontEngineMulti::fallbackFamilyAt(int at) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#fallbackFamilyAt

    Parameters
    ----------

    at : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontEngineMulti::fallbackFamilyAt(int at) const
    return self.uglySide.call(
        'ritual_ZNK16QFontEngineMulti16fallbackFamilyAtEi', at,
    )

  @overload(int)
  def engine(self, at: int) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontEngineMulti::engine(int at) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#engine

    Parameters
    ----------

    at : int
      Passed on as it is.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontEngineMulti::engine(int at) const
    address = self.uglySide.call('ritual_ZNK16QFontEngineMulti6engineEi', at)
    return QFontEngine._cuteAt(address)

  @overload(int, int)
  def shouldLoadFontEngineForCharacter(self, at: int, ucs4: int) -> bool:
    """
    Calls Qt's 'bool QFontEngineMulti::shouldLoadFontEngineForCharacter(int
    at, uint ucs4) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html

    Parameters
    ----------

    at : int
      Passed on as it is.

    ucs4 : int
      Passed on as it is.
    """
    #  bool QFontEngineMulti::shouldLoadFontEngineForCharacter(int at, uint
    #      ucs4) const
    ritual = (
        'ritual_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharacterEij')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFontEngineMulti32shouldLoadFontEngineForCharact'
          'erEij')
    return self.uglySide.call(ritual, at, ucs4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setFallbackFamiliesList(self, fallbackFamilies: QStringList) -> None:
    """
    Calls Qt's 'void QFontEngineMulti::setFallbackFamiliesList(const
    QStringList &fallbackFamilies)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#setFallbackFamiliesList

    Parameters
    ----------

    fallbackFamilies : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFontEngineMulti::setFallbackFamiliesList(const QStringList
    #      &fallbackFamilies)
    self.uglySide.call(
        'ritual_ZN16QFontEngineMulti23setFallbackFamiliesListERK5QListI7QSt'
        'ringE',
        self._valueOf(fallbackFamilies),
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

  @overload(QFontEngine, int, QStringList)
  @overload(NoneType, int, QStringList)
  def __init__(
      self,
      engine: Optional[QFontEngine],
      script: int,
      fallbackFamilies: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QFontEngineMulti::QFontEngineMulti(QFontEngine *engine, int script,
    const QStringList &fallbackFamilies)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#QFontEngineMulti

    Parameters
    ----------

    engine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    script : int
      Passed on as it is.

    fallbackFamilies : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QFontEngineMulti::QFontEngineMulti(QFontEngine *engine, int script,
    #      const QStringList &fallbackFamilies)
    self._noteCreation(QFontEngineMulti, lambda: Rituals.call(
        'ritual_ZN16QFontEngineMultiC1EP11QFontEngineiRK5QListI7QStringE',
        self._addressOf(engine), script, self._valueOf(fallbackFamilies),
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

  @overload(QGlyphLayout)
  def boundingBox(self, glyphs: QGlyphLayout) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngineMulti::boundingBox(const
    QGlyphLayout &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#boundingBox

    Parameters
    ----------

    glyphs : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QFontEngineMulti::boundingBox(const QGlyphLayout
    #      &glyphs)
    ritual = 'ritual_ZN16QFontEngineMulti11boundingBoxERK12QGlyphLayout'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti11boundingBoxERK12QGlyphLayout')
    address = self.uglySide.call(
        ritual, self._valueOf(glyphs, 'QGlyphLayout'),
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int)
  def boundingBox(self, glyph: int) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngineMulti::boundingBox(glyph_t
    glyph)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#boundingBox

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QFontEngineMulti::boundingBox(glyph_t glyph)
    ritual = 'ritual_ZN16QFontEngineMulti11boundingBoxEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFontEngineMulti11boundingBoxEj'
    address = self.uglySide.call(ritual, glyph)
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(QGlyphLayout, QFontEngine.ShaperFlags)
  @overload(NoneType, QFontEngine.ShaperFlags)
  def recalcAdvances(
      self,
      a0: Optional[QGlyphLayout],
      a1: QFontEngine.ShaperFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngineMulti::recalcAdvances(QGlyphLayout *a0,
    ShaperFlags a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#recalcAdvances

    Parameters
    ----------

    a0 : Optional[QGlyphLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QFontEngine.ShaperFlags
      Passed on as its number.
    """
    #  void QFontEngineMulti::recalcAdvances(QGlyphLayout *a0, ShaperFlags
    #      a1) const
    ritual = (
        'ritual_ZNK16QFontEngineMulti14recalcAdvancesEP12QGlyphLayout6QFlag'
        'sIN11QFontEngine10ShaperFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFontEngineMulti14recalcAdvancesEP12QGlyphLayout'
          '6QFlagsIN11QFontEngine10ShaperFlagEE')
    self.uglySide.call(ritual, self._addressOf(a0, 'QGlyphLayout'), a1.value)

  @overload(QGlyphLayout, QFontEngine.ShaperFlags)
  @overload(NoneType, QFontEngine.ShaperFlags)
  def doKerning(
      self,
      a0: Optional[QGlyphLayout],
      a1: QFontEngine.ShaperFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngineMulti::doKerning(QGlyphLayout *a0,
    ShaperFlags a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#doKerning

    Parameters
    ----------

    a0 : Optional[QGlyphLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QFontEngine.ShaperFlags
      Passed on as its number.
    """
    #  void QFontEngineMulti::doKerning(QGlyphLayout *a0, ShaperFlags a1)
    #      const
    ritual = (
        'ritual_ZNK16QFontEngineMulti9doKerningEP12QGlyphLayout6QFlagsIN11Q'
        'FontEngine10ShaperFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QFontEngineMulti9doKerningEP12QGlyphLayout6QFlag'
          'sIN11QFontEngine10ShaperFlagEE')
    self.uglySide.call(ritual, self._addressOf(a0, 'QGlyphLayout'), a1.value)

  @overload(float, float, QGlyphLayout, QPainterPath, QTextItem.RenderFlags)
  @overload(float, float, QGlyphLayout, NoneType, QTextItem.RenderFlags)
  def addOutlineToPath(
      self,
      a0: float,
      a1: float,
      a2: QGlyphLayout,
      a3: Optional[QPainterPath],
      flags: QTextItem.RenderFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngineMulti::addOutlineToPath(qreal a0, qreal a1,
    const QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#addOutlineToPath

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    a2 : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    a3 : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QTextItem.RenderFlags
      Passed on as its number.
    """
    #  void QFontEngineMulti::addOutlineToPath(qreal a0, qreal a1, const
    #      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
    ritual = (
        'ritual_ZN16QFontEngineMulti16addOutlineToPathEddRK12QGlyphLayoutP1'
        '2QPainterPath6QFlagsIN9QTextItem10RenderFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti16addOutlineToPathEddRK12QGlyphLa'
          'youtP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE')
    self.uglySide.call(
        ritual,
        a0, a1, self._valueOf(a2, 'QGlyphLayout'), self._addressOf(a3),
        flags.value,
    )

  @overload(int)
  def alphaMapForGlyph(self, a0: int) -> QImage:
    """
    Calls Qt's 'QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#alphaMapForGlyph

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0)
    ritual = 'ritual_ZN16QFontEngineMulti16alphaMapForGlyphEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEj'
    address = self.uglySide.call(ritual, a0)
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QFixedPoint)
  def alphaMapForGlyph(
      self,
      glyph: int,
      subPixelPosition: QFixedPoint,
  ) -> QImage:
    """
    Calls Qt's 'QImage QFontEngineMulti::alphaMapForGlyph(glyph_t glyph,
    const QFixedPoint &subPixelPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#alphaMapForGlyph

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t glyph, const
    #      QFixedPoint &subPixelPosition)
    ritual = 'ritual_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPoi'
          'nt')
    address = self.uglySide.call(
        ritual, glyph, self._valueOf(subPixelPosition),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QTransform)
  def alphaMapForGlyph(self, a0: int, t: QTransform) -> QImage:
    """
    Calls Qt's 'QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const
    QTransform &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#alphaMapForGlyph

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    t : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const QTransform
    #      &t)
    ritual = 'ritual_ZN16QFontEngineMulti16alphaMapForGlyphEjRK10QTransform'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEjRK10QTransfor'
          'm')
    address = self.uglySide.call(ritual, a0, self._valueOf(t))
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QFixedPoint, QTransform)
  def alphaMapForGlyph(
      self,
      a0: int,
      subPixelPosition: QFixedPoint,
      t: QTransform,
  ) -> QImage:
    """
    Calls Qt's 'QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const
    QFixedPoint &subPixelPosition, const QTransform &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#alphaMapForGlyph

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    t : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngineMulti::alphaMapForGlyph(glyph_t a0, const
    #      QFixedPoint &subPixelPosition, const QTransform &t)
    ritual = (
        'ritual_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPointRK10'
        'QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti16alphaMapForGlyphEjRK11QFixedPoi'
          'ntRK10QTransform')
    address = self.uglySide.call(
        ritual, a0, self._valueOf(subPixelPosition), self._valueOf(t),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QFixedPoint, QTransform)
  def alphaRGBMapForGlyph(
      self,
      a0: int,
      subPixelPosition: QFixedPoint,
      t: QTransform,
  ) -> QImage:
    """
    Calls Qt's 'QImage QFontEngineMulti::alphaRGBMapForGlyph(glyph_t a0,
    const QFixedPoint &subPixelPosition, const QTransform &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#alphaRGBMapForGlyph

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    t : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngineMulti::alphaRGBMapForGlyph(glyph_t a0, const
    #      QFixedPoint &subPixelPosition, const QTransform &t)
    ritual = (
        'ritual_ZN16QFontEngineMulti19alphaRGBMapForGlyphEjRK11QFixedPointR'
        'K10QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti19alphaRGBMapForGlyphEjRK11QFixed'
          'PointRK10QTransform')
    address = self.uglySide.call(
        ritual, a0, self._valueOf(subPixelPosition), self._valueOf(t),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int)
  def ensureEngineAt(self, at: int) -> None:
    """
    Calls Qt's 'void QFontEngineMulti::ensureEngineAt(int at)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html#ensureEngineAt

    Parameters
    ----------

    at : int
      Passed on as it is.
    """
    #  void QFontEngineMulti::ensureEngineAt(int at)
    self.uglySide.call('ritual_ZN16QFontEngineMulti14ensureEngineAtEi', at)

  def ensureFallbackFamiliesQueried(self) -> None:
    """
    Calls Qt's 'void QFontEngineMulti::ensureFallbackFamiliesQueried()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginemulti.html
    """
    #  void QFontEngineMulti::ensureFallbackFamiliesQueried()
    ritual = 'ritual_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QFontEngineMulti29ensureFallbackFamiliesQueriedEv')
    self.uglySide.call(ritual)

  @overload(int)
  def loadEngine(self, at: int) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontEngineMulti::loadEngine(int at)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginemulti.html#loadEngine

    Parameters
    ----------

    at : int
      Passed on as it is.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontEngineMulti::loadEngine(int at)
    ritual = 'ritual_ZN16QFontEngineMulti10loadEngineEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QFontEngineMulti10loadEngineEi'
    address = self.uglySide.call(ritual, at)
    return QFontEngine._cuteAt(address)
