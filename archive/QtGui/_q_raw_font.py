"""
QRawFont binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qrawfont.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QFont, QFontDatabase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QChar, QRectF
  from . import QImage, QPainterPath, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRawFont(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRawFont: a plain Python object standing in front of
  one C++ QRawFont.

  C++ hands a QRawFont around as a copy, so every C++ QRawFont behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRawFont that has a ritual and that Python can call
  so far, 30 names in all: 'isValid', '__eq__', '__ne__', 'glyphCount',
  'familyName', 'styleName', 'style', 'weight', 'alphaMapForGlyph',
  'pathForGlyph', 'boundingRect', 'setPixelSize', 'pixelSize',
  'hintingPreference', 'ascent', 'capHeight', 'descent', 'leading',
  'xHeight', 'averageCharWidth', 'maxCharWidth', 'lineThickness',
  'underlinePosition', 'unitsPerEm', 'glyphName', 'loadFromFile',
  'loadFromData', 'supportsCharacter', 'fontTable', 'fromFont'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRawFont::~QRawFont()': the destructor: Python removes its C++
    QRawFont by it, and has no other use for it.
  - Qt's 'bool QRawFont::glyphIndexesForChars(const QChar *chars, int
    numChars, quint32 *glyphIndexes, int *numGlyphs) const': takes a number
    to change where it is.

  What has no ritual
  ------------------

  9 of the 47 functions Qt declares: 9 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QRawFont is created at the first use, not by 'QRawFont(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRawFont back gives a copy the ritual made for
    Python, in a new cute QRawFont.
  """

  #  The enums Qt writes inside QRawFont, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class AntialiasingType(CuteNum):
    """
    The enum 'QRawFont::AntialiasingType' of Qt, with the 2 names Qt gives in
    it.
    """

    PixelAntialiasing = Kee[int](0)
    SubPixelAntialiasing = Kee[int](1)

  class LayoutFlag(CuteFlags):
    """
    The flags enum 'QRawFont::LayoutFlag' of Qt, with the 3 names Qt gives in
    it. Qt names the type of its combinations 'QRawFont::LayoutFlags'.
    """

    SeparateAdvances = 0x0
    KernedAdvances = 0x1
    UseDesignMetrics = 0x2

  LayoutFlags = LayoutFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QFont)
  @overload(QFont, QFontDatabase.WritingSystem)
  def fromFont(
      font: QFont,
      writingSystem: QFontDatabase.WritingSystem = (
          QFontDatabase.WritingSystem.Any),
  ) -> QRawFont:
    """
    Calls Qt's 'QRawFont QRawFont::fromFont(const QFont &font,
    QFontDatabase::WritingSystem writingSystem)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#fromFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    writingSystem : QFontDatabase.WritingSystem
      Passed on as its number. May be left out, as in Qt: it is then
      QFontDatabase.WritingSystem.Any.

    Returns
    -------

    QRawFont
      A new cute QRawFont around the copy Qt gave back. Python owns it.
    """
    #  QRawFont QRawFont::fromFont(const QFont &font,
    #      QFontDatabase::WritingSystem writingSystem)
    address = Rituals.call(
        'ritual_ZN8QRawFont8fromFontERK5QFontN13QFontDatabase13WritingSyste'
        'mE',
        CuteMixin._valueOf(font), writingSystem.value,
    )
    return QRawFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRawFont'

  #  Qt's '~QRawFont()'. Naming it makes this a value class: Python owns
  #  every C++ QRawFont behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QRawFontD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QRawFont::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#isValid
    """
    #  bool QRawFont::isValid() const
    return self.uglySide.call('ritual_ZNK8QRawFont7isValidEv')

  def glyphCount(self) -> int:
    """
    Calls Qt's 'quint32 QRawFont::glyphCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#glyphCount
    """
    #  quint32 QRawFont::glyphCount() const
    return self.uglySide.call('ritual_ZNK8QRawFont10glyphCountEv')

  def familyName(self) -> str:
    """
    Calls Qt's 'QString QRawFont::familyName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#familyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRawFont::familyName() const
    return self.uglySide.call('ritual_ZNK8QRawFont10familyNameEv')

  def styleName(self) -> str:
    """
    Calls Qt's 'QString QRawFont::styleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRawFont::styleName() const
    return self.uglySide.call('ritual_ZNK8QRawFont9styleNameEv')

  def style(self) -> QFont.Style:
    """
    Calls Qt's 'QFont::Style QRawFont::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#style

    Returns
    -------

    QFont.Style
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QFont.Style(number)'
      gives.
    """
    #  QFont::Style QRawFont::style() const
    return QFont.Style(self.uglySide.call('ritual_ZNK8QRawFont5styleEv'))

  def weight(self) -> int:
    """
    Calls Qt's 'int QRawFont::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#weight
    """
    #  int QRawFont::weight() const
    return self.uglySide.call('ritual_ZNK8QRawFont6weightEv')

  @overload(int)
  @overload(int, AntialiasingType)
  @overload(int, AntialiasingType, QTransform)
  def alphaMapForGlyph(
      self,
      glyphIndex: int,
      antialiasingType: AntialiasingType = (
          AntialiasingType.SubPixelAntialiasing),
      transform: Optional[QTransform] = None,
  ) -> QImage:
    """
    Calls Qt's 'QImage QRawFont::alphaMapForGlyph(quint32 glyphIndex,
    AntialiasingType antialiasingType, const QTransform &transform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#alphaMapForGlyph

    Parameters
    ----------

    glyphIndex : int
      Passed on as it is.

    antialiasingType : AntialiasingType
      Passed on as its number. May be left out, as in Qt: it is then
      AntialiasingType.SubPixelAntialiasing.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRawFont::alphaMapForGlyph(quint32 glyphIndex, AntialiasingType
    #      antialiasingType, const QTransform &transform) const
    if transform is None:
      from . import QTransform
      transform = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK8QRawFont16alphaMapForGlyphEjNS_16AntialiasingTypeERK10Q'
        'Transform',
        glyphIndex, antialiasingType.value, self._valueOf(transform),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int)
  def pathForGlyph(self, glyphIndex: int) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QRawFont::pathForGlyph(quint32 glyphIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#pathForGlyph

    Parameters
    ----------

    glyphIndex : int
      Passed on as it is.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QRawFont::pathForGlyph(quint32 glyphIndex) const
    address = self.uglySide.call(
        'ritual_ZNK8QRawFont12pathForGlyphEj', glyphIndex,
    )
    from . import QPainterPath
    return QPainterPath._cuteOwning(address)

  @overload(int)
  def boundingRect(self, glyphIndex: int) -> QRectF:
    """
    Calls Qt's 'QRectF QRawFont::boundingRect(quint32 glyphIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#boundingRect

    Parameters
    ----------

    glyphIndex : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QRawFont::boundingRect(quint32 glyphIndex) const
    address = self.uglySide.call(
        'ritual_ZNK8QRawFont12boundingRectEj', glyphIndex,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def pixelSize(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#pixelSize
    """
    #  qreal QRawFont::pixelSize() const
    return self.uglySide.call('ritual_ZNK8QRawFont9pixelSizeEv')

  def hintingPreference(self) -> QFont.HintingPreference:
    """
    Calls Qt's 'QFont::HintingPreference QRawFont::hintingPreference()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#hintingPreference

    Returns
    -------

    QFont.HintingPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.HintingPreference(number)' gives.
    """
    #  QFont::HintingPreference QRawFont::hintingPreference() const
    return QFont.HintingPreference(self.uglySide.call(
        'ritual_ZNK8QRawFont17hintingPreferenceEv',
    ))

  def ascent(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#ascent
    """
    #  qreal QRawFont::ascent() const
    return self.uglySide.call('ritual_ZNK8QRawFont6ascentEv')

  def capHeight(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::capHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#capHeight
    """
    #  qreal QRawFont::capHeight() const
    return self.uglySide.call('ritual_ZNK8QRawFont9capHeightEv')

  def descent(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#descent
    """
    #  qreal QRawFont::descent() const
    return self.uglySide.call('ritual_ZNK8QRawFont7descentEv')

  def leading(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#leading
    """
    #  qreal QRawFont::leading() const
    return self.uglySide.call('ritual_ZNK8QRawFont7leadingEv')

  def xHeight(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::xHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#xHeight
    """
    #  qreal QRawFont::xHeight() const
    return self.uglySide.call('ritual_ZNK8QRawFont7xHeightEv')

  def averageCharWidth(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::averageCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#averageCharWidth
    """
    #  qreal QRawFont::averageCharWidth() const
    return self.uglySide.call('ritual_ZNK8QRawFont16averageCharWidthEv')

  def maxCharWidth(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::maxCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#maxCharWidth
    """
    #  qreal QRawFont::maxCharWidth() const
    return self.uglySide.call('ritual_ZNK8QRawFont12maxCharWidthEv')

  def lineThickness(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::lineThickness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#lineThickness
    """
    #  qreal QRawFont::lineThickness() const
    return self.uglySide.call('ritual_ZNK8QRawFont13lineThicknessEv')

  def underlinePosition(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::underlinePosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#underlinePosition
    """
    #  qreal QRawFont::underlinePosition() const
    return self.uglySide.call('ritual_ZNK8QRawFont17underlinePositionEv')

  def unitsPerEm(self) -> float:
    """
    Calls Qt's 'qreal QRawFont::unitsPerEm() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#unitsPerEm
    """
    #  qreal QRawFont::unitsPerEm() const
    return self.uglySide.call('ritual_ZNK8QRawFont10unitsPerEmEv')

  @overload(int)
  def glyphName(self, glyphIndex: int) -> str:
    """
    Calls Qt's 'QString QRawFont::glyphName(quint32 glyphIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#glyphName

    Parameters
    ----------

    glyphIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRawFont::glyphName(quint32 glyphIndex) const
    return self.uglySide.call('ritual_ZNK8QRawFont9glyphNameEj', glyphIndex)

  @overload(int)
  def supportsCharacter(self, ucs4: int) -> bool:
    """
    Calls Qt's 'bool QRawFont::supportsCharacter(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#supportsCharacter

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  bool QRawFont::supportsCharacter(uint ucs4) const
    return self.uglySide.call(
        'ritual_ZNK8QRawFont17supportsCharacterEj', ucs4,
    )

  @overload(QChar)
  def supportsCharacter(self, character: QChar) -> bool:
    """
    Calls Qt's 'bool QRawFont::supportsCharacter(QChar character) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#supportsCharacter

    Parameters
    ----------

    character : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QRawFont::supportsCharacter(QChar character) const
    return self.uglySide.call(
        'ritual_ZNK8QRawFont17supportsCharacterE5QChar',
        self._valueOf(character),
    )

  @overload(str)
  @overload(NoneType)
  def fontTable(self, tagName: Optional[str]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRawFont::fontTable(const char *tagName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#fontTable

    Parameters
    ----------

    tagName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRawFont::fontTable(const char *tagName) const
    address = self.uglySide.call(
        'ritual_ZNK8QRawFont9fontTableEPKc', self._bytesOf(tagName),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QFont.Tag)
  def fontTable(self, tag: QFont.Tag) -> QByteArray:
    """
    Calls Qt's 'QByteArray QRawFont::fontTable(QFont::Tag tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#fontTable

    Parameters
    ----------

    tag : QFont.Tag
      Passed on as a value: Qt reads the C++ QFont::Tag, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QRawFont::fontTable(QFont::Tag tag) const
    address = self.uglySide.call(
        'ritual_ZNK8QRawFont9fontTableEN5QFont3TagE', self._valueOf(tag),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPixelSize(self, pixelSize: float) -> None:
    """
    Calls Qt's 'void QRawFont::setPixelSize(qreal pixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#setPixelSize

    Parameters
    ----------

    pixelSize : float
      Passed on as it is.
    """
    #  void QRawFont::setPixelSize(qreal pixelSize)
    self.uglySide.call('ritual_ZN8QRawFont12setPixelSizeEd', pixelSize)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QRawFont) -> bool:
    """
    Calls Qt's 'bool QRawFont::operator==(const QRawFont &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#operator==

    Parameters
    ----------

    other : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  bool QRawFont::operator==(const QRawFont &other) const
    return self.uglySide.call(
        'ritual_ZNK8QRawFonteqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QRawFont) -> bool:
    """
    Calls Qt's 'bool QRawFont::operator!=(const QRawFont &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#operator!=

    Parameters
    ----------

    other : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  bool QRawFont::operator!=(const QRawFont &other) const
    return self.uglySide.call(
        'ritual_ZNK8QRawFontneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRawFont::QRawFont()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#QRawFont
    """
    #  QRawFont::QRawFont()
    self._noteCreation(QRawFont, lambda: Rituals.call(
        'ritual_ZN8QRawFontC1Ev',
    ))

  @overload(str, float)
  @overload(str, float, QFont.HintingPreference)
  def __init__(
      self,
      fileName: str,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference = (
          QFont.HintingPreference.PreferDefaultHinting),
  ) -> None:
    """
    Notes what was given, for Qt's 'QRawFont::QRawFont(const QString
    &fileName, qreal pixelSize, QFont::HintingPreference hintingPreference)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#QRawFont

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    pixelSize : float
      Passed on as it is.

    hintingPreference : QFont.HintingPreference
      Passed on as its number. May be left out, as in Qt: it is then
      QFont.HintingPreference.PreferDefaultHinting.
    """
    #  QRawFont::QRawFont(const QString &fileName, qreal pixelSize,
    #      QFont::HintingPreference hintingPreference)
    self._noteCreation(QRawFont, lambda: Rituals.call(
        'ritual_ZN8QRawFontC1ERK7QStringdN5QFont17HintingPreferenceE',
        fileName, pixelSize, hintingPreference.value,
    ))

  @overload(QByteArray, float)
  @overload(QByteArray, float, QFont.HintingPreference)
  def __init__(
      self,
      fontData: QByteArray,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference = (
          QFont.HintingPreference.PreferDefaultHinting),
  ) -> None:
    """
    Notes what was given, for Qt's 'QRawFont::QRawFont(const QByteArray
    &fontData, qreal pixelSize, QFont::HintingPreference hintingPreference)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#QRawFont

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    pixelSize : float
      Passed on as it is.

    hintingPreference : QFont.HintingPreference
      Passed on as its number. May be left out, as in Qt: it is then
      QFont.HintingPreference.PreferDefaultHinting.
    """
    #  QRawFont::QRawFont(const QByteArray &fontData, qreal pixelSize,
    #      QFont::HintingPreference hintingPreference)
    self._noteCreation(QRawFont, lambda: Rituals.call(
        'ritual_ZN8QRawFontC1ERK10QByteArraydN5QFont17HintingPreferenceE',
        self._valueOf(fontData), pixelSize, hintingPreference.value,
    ))

  @overload(THIS)
  def __init__(self, other: QRawFont) -> None:
    """
    Notes what was given, for Qt's 'QRawFont::QRawFont(const QRawFont
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#QRawFont

    Parameters
    ----------

    other : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  QRawFont::QRawFont(const QRawFont &other)
    self._noteCreation(QRawFont, lambda: Rituals.call(
        'ritual_ZN8QRawFontC1ERKS_', self._valueOf(other),
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

  @overload(str, float, QFont.HintingPreference)
  def loadFromFile(
      self,
      fileName: str,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference,
  ) -> None:
    """
    Calls Qt's 'void QRawFont::loadFromFile(const QString &fileName, qreal
    pixelSize, QFont::HintingPreference hintingPreference)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#loadFromFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    pixelSize : float
      Passed on as it is.

    hintingPreference : QFont.HintingPreference
      Passed on as its number.
    """
    #  void QRawFont::loadFromFile(const QString &fileName, qreal pixelSize,
    #      QFont::HintingPreference hintingPreference)
    self.uglySide.call(
        'ritual_ZN8QRawFont12loadFromFileERK7QStringdN5QFont17HintingPrefer'
        'enceE',
        fileName, pixelSize, hintingPreference.value,
    )

  @overload(QByteArray, float, QFont.HintingPreference)
  def loadFromData(
      self,
      fontData: QByteArray,
      pixelSize: float,
      hintingPreference: QFont.HintingPreference,
  ) -> None:
    """
    Calls Qt's 'void QRawFont::loadFromData(const QByteArray &fontData, qreal
    pixelSize, QFont::HintingPreference hintingPreference)'.

    Qt's own words: https://doc.qt.io/qt-6/qrawfont.html#loadFromData

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    pixelSize : float
      Passed on as it is.

    hintingPreference : QFont.HintingPreference
      Passed on as its number.
    """
    #  void QRawFont::loadFromData(const QByteArray &fontData, qreal
    #      pixelSize, QFont::HintingPreference hintingPreference)
    self.uglySide.call(
        'ritual_ZN8QRawFont12loadFromDataERK10QByteArraydN5QFont17HintingPr'
        'eferenceE',
        self._valueOf(fontData), pixelSize, hintingPreference.value,
    )
