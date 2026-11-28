"""
QFontEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFontEngine to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QChar, QList
from . import QTextItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QLatin1String
  from . import QColor, QFixed, QFixedPoint, QFontVariableAxis, QGlyphLayout
  from . import QImage, QPainterPath, QTransform, glyph_metrics_t
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QFixed = WAIT['QFixed']
  QFixedPoint = WAIT['QFixedPoint']
  QGlyphLayout = WAIT['QGlyphLayout']
  QLatin1String = WAIT['QLatin1String']
  QPainterPath = WAIT['QPainterPath']
  QTransform = WAIT['QTransform']
  glyph_metrics_t = WAIT['glyph_metrics_t']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontEngine: a plain Python object standing in front
  of one C++ QFontEngine.

  What exists
  -----------

  Every function of Qt's QFontEngine that has a ritual and that Python can
  call so far, 68 names in all: 'type', 'properties', 'getUnscaledGlyph',
  'getSfntTable', 'faceId', 'synthesized', 'supportsSubPixelPositions',
  'supportsHorizontalSubPixelPositions', 'supportsVerticalSubPixelPositions',
  'subPixelPositionFor', 'subPixelPositionForX', 'preferTypoLineMetrics',
  'isColorFont', 'isIgnorableChar', 'maxCachedGlyphSize', 'emSquareSize',
  'glyphIndex', 'recalcAdvances', 'doKerning', 'addOutlineToPath',
  'addBitmapFontToPath', 'alphaMapForGlyph', 'alphaRGBMapForGlyph',
  'bitmapForGlyph', 'renderedPathForGlyph', 'effectivePixelSizeSquared',
  'glyphBoundingBoxExceedsLimit', 'glyphTransformExceedsLimit', 'glyphData',
  'hasInternalCaching', 'alphaMapBoundingBox', 'removeGlyphFromCache',
  'boundingBox', 'tightBoundingBox', 'ascent', 'capHeight', 'descent',
  'leading', 'xHeight', 'averageCharWidth', 'lineThickness',
  'underlinePosition', 'maxCharWidth', 'minLeftBearing', 'minRightBearing',
  'canRender', 'supportsTransformation', 'glyphCount', 'glyphMargin',
  'hasHinting', 'cloneWithSize', 'variableAxes', 'glyphName', 'findGlyph',
  'supportsScript', 'scriptRequiresOpenType',
  'convertToPostscriptFontFamilyName', 'hasUnreliableGlyphOutline',
  'expectsGammaCorrectedBlending', 'disableEmojiSegmenter',
  'setDefaultHintStyle', 'loadKerningPairs', 'firstLeftBearing',
  'lastRightBearing', 'calculatedCapHeight', 'initializeHeightMetrics',
  'processHheaTable', 'processOS2Table'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontEngine::~QFontEngine()': the destructor: Python never removes
    a C++ QFontEngine.
  - Qt's 'bool QFontEngine::getSfntTableData(uint tag, uchar *buffer, uint
    *length) const': takes a number to change where it is.
  - Qt's 'int QFontEngine::stringToCMap(const QChar *str, int len,
    QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const': takes a
    number to change where it is.
  - Qt's 'void QFontEngine::addGlyphsToPath(glyph_t *glyphs, QFixedPoint
    *positions, int nglyphs, QPainterPath *path, QTextItem::RenderFlags
    flags)': takes a number to change where it is.
  - Qt's 'void QFontEngine::getGlyphPositions(const QGlyphLayout &glyphs,
    const QTransform &matrix, QTextItem::RenderFlags flags,
    QVarLengthArray<glyph_t> &glyphs_out, QVarLengthArray<QFixedPoint>
    &positions)': takes a type Python has no way to hand over yet.
  - Qt's 'void QFontEngine::getGlyphBearings(glyph_t glyph, qreal
    *leftBearing, qreal *rightBearing)': takes a number to change where it
    is.
  - Qt's 'Qt::HANDLE QFontEngine::handle() const': gives 'void', which has no
    cute class yet.
  - Qt's 'void *QFontEngine::harfbuzzFont() const': gives 'void', which has
    no cute class yet.
  - Qt's 'void *QFontEngine::harfbuzzFace() const': gives 'void', which has
    no cute class yet.
  - Qt's 'int QFontEngine::getPointInOutline(glyph_t glyph, int flags,
    quint32 point, QFixed *xpos, QFixed *ypos, quint32 *nPoints)': takes a
    number to change where it is.
  - Qt's 'void QFontEngine::clearGlyphCache(const void *key)': names 'void',
    which has no cute class yet.
  - Qt's 'void QFontEngine::setGlyphCache(const void *key,
    QFontEngineGlyphCache *data)': names 'void', which has no cute class yet.
  - Qt's 'QFontEngineGlyphCache *QFontEngine::glyphCache(const void *key,
    GlyphFormat format, const QTransform &transform, const QColor &color)
    const': names 'void', which has no cute class yet.
  - Qt's 'const uchar *QFontEngine::getCMap(const uchar *table, uint
    tableSize, bool *isSymbolFont, int *cmapSize)': names 'uchar', which has
    no cute class yet.
  - Qt's 'quint32 QFontEngine::getTrueTypeGlyphIndex(const uchar *cmap, int
    cmapSize, uint unicode)': names 'uchar', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 90 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QFontEngine is created at the first use, not by
    'QFontEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontEngine.
  - Each name of Qt's QFontEngine that has no cute function yet, '__init__',
    'addGlyphsToPath', 'clearGlyphCache', 'getCMap', 'getGlyphBearings',
    'getGlyphPositions', 'getPointInOutline', 'getSfntTableData',
    'getTrueTypeGlyphIndex', 'glyphCache', 'handle', 'harfbuzzFace',
    'harfbuzzFont', 'setGlyphCache', 'stringToCMap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFontEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class GlyphFormat(CuteNum):
    """
    The enum 'QFontEngine::GlyphFormat' of Qt, with the 6 names Qt gives in
    it.
    """

    Format_None = Kee[int](0)
    Format_Render = Kee[int](0)
    Format_Mono = Kee[int](1)
    Format_A8 = Kee[int](2)
    Format_A32 = Kee[int](3)
    Format_ARGB = Kee[int](4)

  class HintStyle(CuteNum):
    """
    The enum 'QFontEngine::HintStyle' of Qt, with the 5 names Qt gives in it.
    """

    HintUnset = Kee[int](-1)
    HintNone = Kee[int](0)
    HintLight = Kee[int](1)
    HintMedium = Kee[int](2)
    HintFull = Kee[int](3)

  class ShaperFlag(CuteFlags):
    """
    The flags enum 'QFontEngine::ShaperFlag' of Qt, with the 3 names Qt gives
    in it. Qt names the type of its combinations 'QFontEngine::ShaperFlags'.
    """

    DesignMetrics = 0x2
    GlyphIndicesOnly = 0x4
    FullStringFallback = 0x8

  ShaperFlags = ShaperFlag

  class SubpixelAntialiasingType(CuteNum):
    """
    The enum 'QFontEngine::SubpixelAntialiasingType' of Qt, with the 6 names
    Qt gives in it.
    """

    Subpixel_Unset = Kee[int](-1)
    Subpixel_None = Kee[int](0)
    Subpixel_RGB = Kee[int](1)
    Subpixel_BGR = Kee[int](2)
    Subpixel_VRGB = Kee[int](3)
    Subpixel_VBGR = Kee[int](4)

  class SynthesizedFlags(CuteNum):
    """
    The enum 'QFontEngine::SynthesizedFlags' of Qt, with the 3 names Qt gives
    in it.
    """

    SynthesizedItalic = Kee[int](1)
    SynthesizedBold = Kee[int](2)
    SynthesizedStretch = Kee[int](4)

  class Type(CuteNum):
    """
    The enum 'QFontEngine::Type' of Qt, with the 10 names Qt gives in it.
    """

    Box = Kee[int](0)
    Multi = Kee[int](1)
    Win = Kee[int](2)
    Mac = Kee[int](3)
    Freetype = Kee[int](4)
    QPF1 = Kee[int](5)
    QPF2 = Kee[int](6)
    Proxy = Kee[int](7)
    DirectWrite = Kee[int](8)
    TestFontEngine = Kee[int](4096)

  #  The classes Qt writes inside QFontEngine, each a class in here as in
  #  C++.

  class FaceData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontEngine::FaceData: a plain Python object
    standing in front of one C++ QFontEngine::FaceData.

    C++ hands a QFontEngine::FaceData around as a copy, so every C++
    QFontEngine::FaceData behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QFontEngine::FaceData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontEngine::FaceData::~FaceData()': the destructor: Python
      removes its C++ QFontEngine::FaceData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QFontEngine::FaceData is created at the first use, not by
      'QFontEngine::FaceData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontEngine::FaceData back gives a copy the ritual
      made for Python, in a new cute QFontEngine::FaceData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontEngine::FaceData'

    #  Qt's '~QFontEngine::FaceData()'. Naming it makes this a value class:
    #  Python owns every C++ QFontEngine::FaceData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QFontEngine8FaceDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class FaceId(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontEngine::FaceId: a plain Python object standing
    in front of one C++ QFontEngine::FaceId.

    C++ hands a QFontEngine::FaceId around as a copy, so every C++
    QFontEngine::FaceId behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QFontEngine::FaceId yet. It can be made from Python,
    in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontEngine::FaceId::~FaceId()': the destructor: Python removes
      its C++ QFontEngine::FaceId by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFontEngine::FaceId is created at the first use, not by
      'QFontEngine::FaceId(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontEngine::FaceId back gives a copy the ritual
      made for Python, in a new cute QFontEngine::FaceId.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontEngine::FaceId'

    #  Qt's '~QFontEngine::FaceId()'. Naming it makes this a value class:
    #  Python owns every C++ QFontEngine::FaceId behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QFontEngine6FaceIdD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QFontEngine::FaceId::FaceId()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontengine-faceid.html#FaceId
      """
      #  QFontEngine::FaceId::FaceId()
      self._noteCreation(QFontEngine.FaceId, lambda: Rituals.call(
          'ritual_ZN11QFontEngine6FaceIdC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Glyph(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontEngine::Glyph: a plain Python object standing
    in front of one C++ QFontEngine::Glyph.

    What exists
    -----------

    No function of Qt's QFontEngine::Glyph yet. It can be made from Python,
    in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontEngine::Glyph::~Glyph()': the destructor: Python never
      removes a C++ QFontEngine::Glyph.

    What has no ritual
    ------------------

    2 of the 4 functions Qt declares: 2 forbidden.

    What to expect
    --------------

    - The C++ QFontEngine::Glyph is created at the first use, not by
      'QFontEngine::Glyph(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QFontEngine::Glyph.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontEngine::Glyph'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QFontEngine::Glyph::Glyph()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontengine-glyph.html#Glyph
      """
      #  QFontEngine::Glyph::Glyph()
      self._noteCreation(QFontEngine.Glyph, lambda: Rituals.call(
          'ritual_ZN11QFontEngine5GlyphC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Holder(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontEngine::Holder: a plain Python object standing
    in front of one C++ QFontEngine::Holder.

    What exists
    -----------

    Every function of Qt's QFontEngine::Holder that has a ritual and that
    Python can call so far, 1 name in all: 'reset'. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontEngine::Holder::Holder(void *p, qt_destroy_func_t d)': names
      'void', which has no cute class yet.
    - Qt's 'QFontEngine::Holder::~Holder()': the destructor: Python never
      removes a C++ QFontEngine::Holder.
    - Qt's 'QFontEngine::Holder::Holder(Holder &&other)': takes a type Python
      has no way to hand over yet.
    - Qt's 'Holder &QFontEngine::Holder::operator=(Holder &&other)':
      assignment: Python binds a name and has no operator for it.
    - Qt's 'void QFontEngine::Holder::swap(Holder &other)': takes a type
      Python has no way to hand over yet.
    - Qt's 'void *QFontEngine::Holder::get() const': gives 'void', which has
      no cute class yet.
    - Qt's 'void *QFontEngine::Holder::release()': gives 'void', which has no
      cute class yet.
    - Qt's 'qt_destroy_func_t QFontEngine::Holder::get_deleter() const':
      gives a type Python has no way to take yet.
    - Qt's 'bool QFontEngine::Holder::operator!() const': an operator Python
      has no name for.

    What to expect
    --------------

    - The C++ QFontEngine::Holder is created at the first use, not by
      'QFontEngine::Holder(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QFontEngine::Holder.
    - Each name of Qt's QFontEngine::Holder that has no cute function yet,
      'get', 'get_deleter', 'release', 'swap', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontEngine::Holder'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QFontEngine::Holder::Holder()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontengine-holder.html#Holder
      """
      #  QFontEngine::Holder::Holder()
      self._noteCreation(QFontEngine.Holder, lambda: Rituals.call(
          'ritual_ZN11QFontEngine6HolderC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def reset(self) -> None:
      """
      Calls Qt's 'void QFontEngine::Holder::reset()'.

      Qt's own words: https://doc.qt.io/qt-6/qfontengine-holder.html#reset
      """
      #  void QFontEngine::Holder::reset()
      self.uglySide.call('ritual_ZN11QFontEngine6Holder5resetEv')

    @staticmethod
    def get(*__, **_) -> Never:
      """
      Qt's 'void *QFontEngine::Holder::get() const': gives 'void', which has
      no cute class yet.
      """
      raise NotImplementedError(
          "'QFontEngine.Holder.get' has no cute function yet. Qt's 'void "
          "*QFontEngine::Holder::get() const': gives 'void', which has no "
          "cute class yet.")

    @staticmethod
    def get_deleter(*__, **_) -> Never:
      """
      Qt's 'qt_destroy_func_t QFontEngine::Holder::get_deleter() const':
      gives a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QFontEngine.Holder.get_deleter' has no cute function yet. Qt's "
          "'qt_destroy_func_t QFontEngine::Holder::get_deleter() const': "
          "gives a type Python has no way to take yet.")

    @staticmethod
    def release(*__, **_) -> Never:
      """
      Qt's 'void *QFontEngine::Holder::release()': gives 'void', which has no
      cute class yet.
      """
      raise NotImplementedError(
          "'QFontEngine.Holder.release' has no cute function yet. Qt's "
          "'void *QFontEngine::Holder::release()': gives 'void', which has "
          "no cute class yet.")

    @staticmethod
    def swap(*__, **_) -> Never:
      """
      Qt's 'void QFontEngine::Holder::swap(Holder &other)': takes a type
      Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QFontEngine.Holder.swap' has no cute function yet. Qt's 'void "
          "QFontEngine::Holder::swap(Holder &other)': takes a type Python "
          "has no way to hand over yet.")

  class KernPair(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontEngine::KernPair: a plain Python object
    standing in front of one C++ QFontEngine::KernPair.

    C++ hands a QFontEngine::KernPair around as a copy, so every C++
    QFontEngine::KernPair behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QFontEngine::KernPair that has a ritual and that
    Python can call so far, 1 name in all: '__lt__'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontEngine::KernPair::~KernPair()': the destructor: Python
      removes its C++ QFontEngine::KernPair by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QFontEngine::KernPair is created at the first use, not by
      'QFontEngine::KernPair(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontEngine::KernPair back gives a copy the ritual
      made for Python, in a new cute QFontEngine::KernPair.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontEngine::KernPair'

    #  Qt's '~QFontEngine::KernPair()'. Naming it makes this a value class:
    #  Python owns every C++ QFontEngine::KernPair behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QFontEngine8KernPairD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __lt__(self, other: QFontEngine.KernPair) -> bool:
      """
      Calls Qt's 'bool QFontEngine::KernPair::operator<(const KernPair
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfontengine-kernpair.html#operator<

      Parameters
      ----------

      other : QFontEngine.KernPair
        Passed on as a value: Qt reads the C++ QFontEngine::KernPair, which
        stays Python's own.
      """
      #  bool QFontEngine::KernPair::operator<(const KernPair &other) const
      return self.uglySide.call(
          'ritual_ZNK11QFontEngine8KernPairltERKS0_', self._valueOf(other),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Properties(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontEngine::Properties: a plain Python object
    standing in front of one C++ QFontEngine::Properties.

    C++ hands a QFontEngine::Properties around as a copy, so every C++
    QFontEngine::Properties behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QFontEngine::Properties yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontEngine::Properties::~Properties()': the destructor: Python
      removes its C++ QFontEngine::Properties by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QFontEngine::Properties is created at the first use, not by
      'QFontEngine::Properties(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontEngine::Properties back gives a copy the
      ritual made for Python, in a new cute QFontEngine::Properties.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontEngine::Properties'

    #  Qt's '~QFontEngine::Properties()'. Naming it makes this a value class:
    #  Python owns every C++ QFontEngine::Properties behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QFontEngine10PropertiesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def isIgnorableChar(ucs4: int) -> bool:
    """
    Calls Qt's 'bool QFontEngine::isIgnorableChar(char32_t ucs4)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#isIgnorableChar

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  bool QFontEngine::isIgnorableChar(char32_t ucs4)
    return Rituals.call('ritual_ZN11QFontEngine15isIgnorableCharEDi', ucs4)

  @staticmethod
  def maxCachedGlyphSize() -> int:
    """
    Calls Qt's 'int QFontEngine::maxCachedGlyphSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#maxCachedGlyphSize
    """
    #  int QFontEngine::maxCachedGlyphSize()
    return Rituals.call('ritual_ZN11QFontEngine18maxCachedGlyphSizeEv')

  @staticmethod
  @overload(float, float, float)
  def glyphBoundingBoxExceedsLimit(
      glyphWidth: float,
      glyphHeight: float,
      effectivePixelSizeSquared: float,
  ) -> bool:
    """
    Calls Qt's 'bool QFontEngine::glyphBoundingBoxExceedsLimit(qreal
    glyphWidth, qreal glyphHeight, qreal effectivePixelSizeSquared)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#glyphBoundingBoxExceedsLimit

    Parameters
    ----------

    glyphWidth : float
      Passed on as it is.

    glyphHeight : float
      Passed on as it is.

    effectivePixelSizeSquared : float
      Passed on as it is.
    """
    #  bool QFontEngine::glyphBoundingBoxExceedsLimit(qreal glyphWidth, qreal
    #      glyphHeight, qreal effectivePixelSizeSquared)
    return Rituals.call(
        'ritual_ZN11QFontEngine28glyphBoundingBoxExceedsLimitEddd',
        glyphWidth, glyphHeight, effectivePixelSizeSquared,
    )

  @staticmethod
  @overload(QChar.Script)
  def scriptRequiresOpenType(script: QChar.Script) -> bool:
    """
    Calls Qt's 'bool QFontEngine::scriptRequiresOpenType(QChar::Script
    script)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#scriptRequiresOpenType

    Parameters
    ----------

    script : QChar.Script
      Passed on as its number.
    """
    #  bool QFontEngine::scriptRequiresOpenType(QChar::Script script)
    return Rituals.call(
        'ritual_ZN11QFontEngine22scriptRequiresOpenTypeEN5QChar6ScriptE',
        script.value,
    )

  @staticmethod
  @overload(QByteArray)
  def convertToPostscriptFontFamilyName(
      fontFamily: QByteArray,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QFontEngine::convertToPostscriptFontFamilyName(const QByteArray
    &fontFamily)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#convertToPostscriptFontFamilyName

    Parameters
    ----------

    fontFamily : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFontEngine::convertToPostscriptFontFamilyName(const
    #      QByteArray &fontFamily)
    address = Rituals.call(
        'ritual_ZN11QFontEngine33convertToPostscriptFontFamilyNameERK10QByt'
        'eArray',
        CuteMixin._valueOf(fontFamily),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def disableEmojiSegmenter() -> bool:
    """
    Calls Qt's 'bool QFontEngine::disableEmojiSegmenter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#disableEmojiSegmenter
    """
    #  bool QFontEngine::disableEmojiSegmenter()
    return Rituals.call('ritual_ZN11QFontEngine21disableEmojiSegmenterEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontEngine'

  #  A C++ QFontEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontEngine'

  #  The functions Qt calls itself that QFontEngine is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getSfntTableData': (
          'bool QFontEngine::getSfntTableData(uint, uchar *, uint *) const',
      ),
      'stringToCMap': (
          'int QFontEngine::stringToCMap(const QChar *, int, QGlyphLayout '
          '*, int *, ShaperFlags) const',
      ),
      'addGlyphsToPath': (
          'void QFontEngine::addGlyphsToPath(glyph_t *, QFixedPoint *, '
          'int, QPainterPath *, QTextItem::RenderFlags)',
      ),
      'getGlyphBearings': (
          'void QFontEngine::getGlyphBearings(glyph_t, qreal *, qreal *)',
      ),
      'handle': (
          'Qt::HANDLE QFontEngine::handle() const',
      ),
      'variableAxes': (
          'QList<QFontVariableAxis> QFontEngine::variableAxes() const',
      ),
      'getPointInOutline': (
          'int QFontEngine::getPointInOutline(glyph_t, int, quint32, '
          'QFixed *, QFixed *, quint32 *)',
      ),
  }

  #  The functions Qt calls itself that QFontEngine is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'properties': (
          ('_ZNK11QFontEngine10propertiesEv',
           ('address', 'value', 'QtGui:QFontEngine.Properties'),
           ()),
      ),
      'getUnscaledGlyph': (
          ('_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_met'
           'rics_t',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
               ('address', 'address', 'QtGui:QPainterPath'),
               ('address', 'address', 'QtGui:glyph_metrics_t'),
           )),
      ),
      'faceId': (
          ('_ZNK11QFontEngine6faceIdEv',
           ('address', 'value', 'QtGui:QFontEngine.FaceId'),
           ()),
      ),
      'synthesized': (
          ('_ZNK11QFontEngine11synthesizedEv',
           ('int', 'number', ''),
           ()),
      ),
      'supportsHorizontalSubPixelPositions': (
          ('_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'supportsVerticalSubPixelPositions': (
          ('_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv',
           ('bool', 'number', ''),
           ()),
      ),
      'subPixelPositionFor': (
          ('_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint',
           ('address', 'value', 'QtGui:QFixedPoint'),
           (
               ('address', 'value', 'QtGui:QFixedPoint'),
           )),
      ),
      'emSquareSize': (
          ('_ZNK11QFontEngine12emSquareSizeEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'glyphIndex': (
          ('_ZNK11QFontEngine10glyphIndexEj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'recalcAdvances': (
          ('_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10S'
           'haperFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QGlyphLayout'),
               ('int', 'flags', 'QtGui:QFontEngine.ShaperFlag'),
           )),
      ),
      'doKerning': (
          ('_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperF'
           'lagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QGlyphLayout'),
               ('int', 'flags', 'QtGui:QFontEngine.ShaperFlag'),
           )),
      ),
      'addOutlineToPath': (
          ('_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainte'
           'rPath6QFlagsIN9QTextItem10RenderFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('address', 'value', 'QtGui:QGlyphLayout'),
               ('address', 'address', 'QtGui:QPainterPath'),
               ('int', 'flags', 'QtGui:QTextItem.RenderFlag'),
           )),
      ),
      'alphaMapForGlyph': (
          ('_ZN11QFontEngine16alphaMapForGlyphEj',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('unsigned int', 'number', ''),
           )),
          ('_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
           )),
          ('_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QTransform'),
           )),
          ('_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransfo'
           'rm',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'alphaRGBMapForGlyph': (
          ('_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTran'
           'sform',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'bitmapForGlyph': (
          ('_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransform'
           'RK6QColor',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
               ('address', 'value', 'QtGui:QTransform'),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'glyphData': (
          ('_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK1'
           '0QTransform',
           ('address', 'address', 'QtGui:QFontEngine.Glyph'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
               ('int', 'enum', 'QtGui:QFontEngine.GlyphFormat'),
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'hasInternalCaching': (
          ('_ZNK11QFontEngine18hasInternalCachingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'alphaMapBoundingBox': (
          ('_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTran'
           'sformNS_11GlyphFormatE',
           ('address', 'value', 'QtGui:glyph_metrics_t'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
               ('address', 'value', 'QtGui:QTransform'),
               ('int', 'enum', 'QtGui:QFontEngine.GlyphFormat'),
           )),
      ),
      'removeGlyphFromCache': (
          ('_ZN11QFontEngine20removeGlyphFromCacheEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'boundingBox': (
          ('_ZN11QFontEngine11boundingBoxERK12QGlyphLayout',
           ('address', 'value', 'QtGui:glyph_metrics_t'),
           (
               ('address', 'value', 'QtGui:QGlyphLayout'),
           )),
          ('_ZN11QFontEngine11boundingBoxEj',
           ('address', 'value', 'QtGui:glyph_metrics_t'),
           (
               ('unsigned int', 'number', ''),
           )),
          ('_ZN11QFontEngine11boundingBoxEjRK10QTransform',
           ('address', 'value', 'QtGui:glyph_metrics_t'),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'ascent': (
          ('_ZNK11QFontEngine6ascentEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'capHeight': (
          ('_ZNK11QFontEngine9capHeightEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'descent': (
          ('_ZNK11QFontEngine7descentEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'leading': (
          ('_ZNK11QFontEngine7leadingEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'xHeight': (
          ('_ZNK11QFontEngine7xHeightEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'averageCharWidth': (
          ('_ZNK11QFontEngine16averageCharWidthEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'lineThickness': (
          ('_ZNK11QFontEngine13lineThicknessEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'underlinePosition': (
          ('_ZNK11QFontEngine17underlinePositionEv',
           ('address', 'value', 'QtGui:QFixed'),
           ()),
      ),
      'maxCharWidth': (
          ('_ZNK11QFontEngine12maxCharWidthEv',
           ('double', 'number', ''),
           ()),
      ),
      'minLeftBearing': (
          ('_ZNK11QFontEngine14minLeftBearingEv',
           ('double', 'number', ''),
           ()),
      ),
      'minRightBearing': (
          ('_ZNK11QFontEngine15minRightBearingEv',
           ('double', 'number', ''),
           ()),
      ),
      'canRender': (
          ('_ZNK11QFontEngine9canRenderEPK5QChari',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QChar'),
               ('int', 'number', ''),
           )),
      ),
      'supportsTransformation': (
          ('_ZNK11QFontEngine22supportsTransformationERK10QTransform',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'glyphCount': (
          ('_ZNK11QFontEngine10glyphCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'glyphMargin': (
          ('_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QFontEngine.GlyphFormat'),
           )),
      ),
      'cloneWithSize': (
          ('_ZNK11QFontEngine13cloneWithSizeEd',
           ('address', 'address', 'QtGui:QFontEngine'),
           (
               ('double', 'number', ''),
           )),
      ),
      'glyphName': (
          ('_ZNK11QFontEngine9glyphNameEj',
           ('address', 'text', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'findGlyph': (
          ('_ZNK11QFontEngine9findGlyphE13QLatin1String',
           ('unsigned int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QLatin1String'),
           )),
      ),
      'hasUnreliableGlyphOutline': (
          ('_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv',
           ('bool', 'number', ''),
           ()),
      ),
      'expectsGammaCorrectedBlending': (
          ('_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphForm'
           'atE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QFontEngine.GlyphFormat'),
           )),
      ),
      'setDefaultHintStyle': (
          ('_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtGui:QFontEngine.HintStyle'),
           )),
      ),
      'initializeHeightMetrics': (
          ('_ZNK11QFontEngine23initializeHeightMetricsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QFontEngine::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QFontEngine::type() const
    return QFontEngine.Type(self.uglySide.call(
        'ritual_ZNK11QFontEngine4typeEv',
    ))

  def properties(self) -> Properties:
    """
    Calls Qt's 'Properties QFontEngine::properties() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#properties

    Returns
    -------

    Properties
      A new cute QFontEngine::Properties around the copy Qt gave back. Python
      owns it.
    """
    #  Properties QFontEngine::properties() const
    ritual = 'ritual_ZNK11QFontEngine10propertiesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine10propertiesEv'
    address = self.uglySide.call(ritual)
    return QFontEngine.Properties._cuteOwning(address)

  @overload(int)
  def getSfntTable(self, tag: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QFontEngine::getSfntTable(uint tag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#getSfntTable

    Parameters
    ----------

    tag : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QFontEngine::getSfntTable(uint tag) const
    address = self.uglySide.call(
        'ritual_ZNK11QFontEngine12getSfntTableEj', tag,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def faceId(self) -> FaceId:
    """
    Calls Qt's 'FaceId QFontEngine::faceId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#faceId

    Returns
    -------

    FaceId
      A new cute QFontEngine::FaceId around the copy Qt gave back. Python
      owns it.
    """
    #  FaceId QFontEngine::faceId() const
    ritual = 'ritual_ZNK11QFontEngine6faceIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine6faceIdEv'
    address = self.uglySide.call(ritual)
    return QFontEngine.FaceId._cuteOwning(address)

  def synthesized(self) -> int:
    """
    Calls Qt's 'int QFontEngine::synthesized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#synthesized
    """
    #  int QFontEngine::synthesized() const
    ritual = 'ritual_ZNK11QFontEngine11synthesizedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine11synthesizedEv'
    return self.uglySide.call(ritual)

  def supportsSubPixelPositions(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::supportsSubPixelPositions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#supportsSubPixelPositions
    """
    #  bool QFontEngine::supportsSubPixelPositions() const
    return self.uglySide.call(
        'ritual_ZNK11QFontEngine25supportsSubPixelPositionsEv',
    )

  def supportsHorizontalSubPixelPositions(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::supportsHorizontalSubPixelPositions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html
    """
    #  bool QFontEngine::supportsHorizontalSubPixelPositions() const
    ritual = 'ritual_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine35supportsHorizontalSubPixelPositions'
          'Ev')
    return self.uglySide.call(ritual)

  def supportsVerticalSubPixelPositions(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::supportsVerticalSubPixelPositions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#supportsVerticalSubPixelPositions
    """
    #  bool QFontEngine::supportsVerticalSubPixelPositions() const
    ritual = 'ritual_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv')
    return self.uglySide.call(ritual)

  @overload(QFixedPoint)
  def subPixelPositionFor(self, position: QFixedPoint) -> QFixedPoint:
    """
    Calls Qt's 'QFixedPoint QFontEngine::subPixelPositionFor(const
    QFixedPoint &position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#subPixelPositionFor

    Parameters
    ----------

    position : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    Returns
    -------

    QFixedPoint
      A new cute QFixedPoint around the copy Qt gave back. Python owns it.
    """
    #  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
    #      &position) const
    ritual = 'ritual_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint')
    address = self.uglySide.call(ritual, self._valueOf(position))
    from . import QFixedPoint
    return QFixedPoint._cuteOwning(address)

  @overload(QFixed)
  def subPixelPositionForX(self, x: QFixed) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::subPixelPositionForX(QFixed x) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#subPixelPositionForX

    Parameters
    ----------

    x : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::subPixelPositionForX(QFixed x) const
    address = self.uglySide.call(
        'ritual_ZNK11QFontEngine20subPixelPositionForXE6QFixed',
        self._valueOf(x),
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  def preferTypoLineMetrics(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::preferTypoLineMetrics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#preferTypoLineMetrics
    """
    #  bool QFontEngine::preferTypoLineMetrics() const
    return self.uglySide.call(
        'ritual_ZNK11QFontEngine21preferTypoLineMetricsEv',
    )

  def isColorFont(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::isColorFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#isColorFont
    """
    #  bool QFontEngine::isColorFont() const
    return self.uglySide.call('ritual_ZNK11QFontEngine11isColorFontEv')

  def emSquareSize(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::emSquareSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#emSquareSize

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::emSquareSize() const
    ritual = 'ritual_ZNK11QFontEngine12emSquareSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine12emSquareSizeEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  @overload(int)
  def glyphIndex(self, ucs4: int) -> int:
    """
    Calls Qt's 'glyph_t QFontEngine::glyphIndex(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#glyphIndex

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  glyph_t QFontEngine::glyphIndex(uint ucs4) const
    return self.uglySide.call('ritual_ZNK11QFontEngine10glyphIndexEj', ucs4)

  @overload(QTransform)
  def effectivePixelSizeSquared(self, transform: QTransform) -> float:
    """
    Calls Qt's 'qreal QFontEngine::effectivePixelSizeSquared(const QTransform
    &transform) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#effectivePixelSizeSquared

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  qreal QFontEngine::effectivePixelSizeSquared(const QTransform
    #      &transform) const
    return self.uglySide.call(
        'ritual_ZNK11QFontEngine25effectivePixelSizeSquaredERK10QTransform',
        self._valueOf(transform),
    )

  def hasInternalCaching(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::hasInternalCaching() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#hasInternalCaching
    """
    #  bool QFontEngine::hasInternalCaching() const
    ritual = 'ritual_ZNK11QFontEngine18hasInternalCachingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine18hasInternalCachingEv'
    return self.uglySide.call(ritual)

  def ascent(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#ascent

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::ascent() const
    ritual = 'ritual_ZNK11QFontEngine6ascentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine6ascentEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def capHeight(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::capHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#capHeight

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::capHeight() const
    address = self.uglySide.call('ritual_ZNK11QFontEngine9capHeightEv')
    from . import QFixed
    return QFixed._cuteOwning(address)

  def descent(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#descent

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::descent() const
    ritual = 'ritual_ZNK11QFontEngine7descentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine7descentEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def leading(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#leading

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::leading() const
    ritual = 'ritual_ZNK11QFontEngine7leadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine7leadingEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def xHeight(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::xHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#xHeight

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::xHeight() const
    ritual = 'ritual_ZNK11QFontEngine7xHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine7xHeightEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def averageCharWidth(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::averageCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#averageCharWidth

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::averageCharWidth() const
    ritual = 'ritual_ZNK11QFontEngine16averageCharWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine16averageCharWidthEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def lineThickness(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::lineThickness() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#lineThickness

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::lineThickness() const
    ritual = 'ritual_ZNK11QFontEngine13lineThicknessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine13lineThicknessEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def underlinePosition(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::underlinePosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#underlinePosition

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::underlinePosition() const
    ritual = 'ritual_ZNK11QFontEngine17underlinePositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine17underlinePositionEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def maxCharWidth(self) -> float:
    """
    Calls Qt's 'qreal QFontEngine::maxCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#maxCharWidth
    """
    #  qreal QFontEngine::maxCharWidth() const
    return self.uglySide.call('ritual_ZNK11QFontEngine12maxCharWidthEv')

  def minLeftBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontEngine::minLeftBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#minLeftBearing
    """
    #  qreal QFontEngine::minLeftBearing() const
    ritual = 'ritual_ZNK11QFontEngine14minLeftBearingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine14minLeftBearingEv'
    return self.uglySide.call(ritual)

  def minRightBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontEngine::minRightBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#minRightBearing
    """
    #  qreal QFontEngine::minRightBearing() const
    ritual = 'ritual_ZNK11QFontEngine15minRightBearingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine15minRightBearingEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def canRender(self, ucs4: int) -> bool:
    """
    Calls Qt's 'bool QFontEngine::canRender(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#canRender

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  bool QFontEngine::canRender(uint ucs4) const
    return self.uglySide.call('ritual_ZNK11QFontEngine9canRenderEj', ucs4)

  @overload(QChar, int)
  @overload(NoneType, int)
  def canRender(self, str: Optional[QChar], len: int) -> bool:
    """
    Calls Qt's 'bool QFontEngine::canRender(const QChar *str, int len)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#canRender

    Parameters
    ----------

    str : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.
    """
    #  bool QFontEngine::canRender(const QChar *str, int len) const
    ritual = 'ritual_ZNK11QFontEngine9canRenderEPK5QChari'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine9canRenderEPK5QChari'
    return self.uglySide.call(ritual, self._addressOf(str), len)

  @overload(QTransform)
  def supportsTransformation(self, transform: QTransform) -> bool:
    """
    Calls Qt's 'bool QFontEngine::supportsTransformation(const QTransform
    &transform) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#supportsTransformation

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QFontEngine::supportsTransformation(const QTransform &transform)
    #      const
    ritual = 'ritual_ZNK11QFontEngine22supportsTransformationERK10QTransform'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine22supportsTransformationERK10QTransfo'
          'rm')
    return self.uglySide.call(ritual, self._valueOf(transform))

  def glyphCount(self) -> int:
    """
    Calls Qt's 'int QFontEngine::glyphCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#glyphCount
    """
    #  int QFontEngine::glyphCount() const
    ritual = 'ritual_ZNK11QFontEngine10glyphCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine10glyphCountEv'
    return self.uglySide.call(ritual)

  def hasHinting(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::hasHinting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#hasHinting
    """
    #  bool QFontEngine::hasHinting() const
    return self.uglySide.call('ritual_ZNK11QFontEngine10hasHintingEv')

  @overload(float)
  def cloneWithSize(self, a0: float) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontEngine::cloneWithSize(qreal a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#cloneWithSize

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontEngine::cloneWithSize(qreal a0) const
    ritual = 'ritual_ZNK11QFontEngine13cloneWithSizeEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine13cloneWithSizeEd'
    address = self.uglySide.call(ritual, a0)
    return QFontEngine._cuteAt(address)

  def variableAxes(self) -> QList[QFontVariableAxis]:
    """
    Calls Qt's 'QList<QFontVariableAxis> QFontEngine::variableAxes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#variableAxes

    Returns
    -------

    QList[QFontVariableAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QFontVariableAxis> QFontEngine::variableAxes() const
    address = self.uglySide.call('ritual_ZNK11QFontEngine12variableAxesEv')
    from . import QFontVariableAxis
    return QList[QFontVariableAxis]._cuteOwning(address)

  @overload(int)
  def glyphName(self, index: int) -> str:
    """
    Calls Qt's 'QString QFontEngine::glyphName(glyph_t index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#glyphName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontEngine::glyphName(glyph_t index) const
    ritual = 'ritual_ZNK11QFontEngine9glyphNameEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine9glyphNameEj'
    return self.uglySide.call(ritual, index)

  @overload(QLatin1String)
  def findGlyph(self, name: QLatin1String) -> int:
    """
    Calls Qt's 'glyph_t QFontEngine::findGlyph(QLatin1StringView name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#findGlyph

    Parameters
    ----------

    name : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  glyph_t QFontEngine::findGlyph(QLatin1StringView name) const
    ritual = 'ritual_ZNK11QFontEngine9findGlyphE13QLatin1String'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine9findGlyphE13QLatin1String'
    return self.uglySide.call(ritual, self._valueOf(name))

  @overload(QChar.Script)
  def supportsScript(self, script: QChar.Script) -> bool:
    """
    Calls Qt's 'bool QFontEngine::supportsScript(QChar::Script script)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#supportsScript

    Parameters
    ----------

    script : QChar.Script
      Passed on as its number.
    """
    #  bool QFontEngine::supportsScript(QChar::Script script) const
    return self.uglySide.call(
        'ritual_ZNK11QFontEngine14supportsScriptEN5QChar6ScriptE',
        script.value,
    )

  def hasUnreliableGlyphOutline(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::hasUnreliableGlyphOutline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#hasUnreliableGlyphOutline
    """
    #  bool QFontEngine::hasUnreliableGlyphOutline() const
    ritual = 'ritual_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv'
    return self.uglySide.call(ritual)

  @overload(GlyphFormat)
  def expectsGammaCorrectedBlending(self, format: GlyphFormat) -> bool:
    """
    Calls Qt's 'bool
    QFontEngine::expectsGammaCorrectedBlending(QFontEngine::GlyphFormat
    format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#expectsGammaCorrectedBlending

    Parameters
    ----------

    format : GlyphFormat
      Passed on as its number.
    """
    #  bool QFontEngine::expectsGammaCorrectedBlending(QFontEngine::
    #      GlyphFormat format) const
    ritual = (
        'ritual_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphF'
        'ormatE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11'
          'GlyphFormatE')
    return self.uglySide.call(ritual, format.value)

  def calculatedCapHeight(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::calculatedCapHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#calculatedCapHeight

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::calculatedCapHeight() const
    address = self.uglySide.call(
        'ritual_ZNK11QFontEngine19calculatedCapHeightEv',
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  def processHheaTable(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::processHheaTable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#processHheaTable
    """
    #  bool QFontEngine::processHheaTable() const
    return self.uglySide.call('ritual_ZNK11QFontEngine16processHheaTableEv')

  def processOS2Table(self) -> bool:
    """
    Calls Qt's 'bool QFontEngine::processOS2Table() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#processOS2Table
    """
    #  bool QFontEngine::processOS2Table() const
    return self.uglySide.call('ritual_ZNK11QFontEngine15processOS2TableEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(HintStyle)
  def setDefaultHintStyle(self, a0: HintStyle) -> None:
    """
    Calls Qt's 'void QFontEngine::setDefaultHintStyle(HintStyle a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#setDefaultHintStyle

    Parameters
    ----------

    a0 : HintStyle
      Passed on as its number.
    """
    #  void QFontEngine::setDefaultHintStyle(HintStyle a0)
    ritual = 'ritual_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE')
    self.uglySide.call(ritual, a0.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QFontEngine::QFontEngine(Type type)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QFontEngine.__init__' has no cute function yet. Qt's "
        "'QFontEngine::QFontEngine(Type type)': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  @overload(int, QPainterPath, glyph_metrics_t)
  @overload(int, QPainterPath, NoneType)
  @overload(int, NoneType, glyph_metrics_t)
  @overload(int, NoneType, NoneType)
  def getUnscaledGlyph(
      self,
      glyph: int,
      path: Optional[QPainterPath],
      metrics: Optional[glyph_metrics_t],
  ) -> None:
    """
    Calls Qt's 'void QFontEngine::getUnscaledGlyph(glyph_t glyph,
    QPainterPath *path, glyph_metrics_t *metrics)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#getUnscaledGlyph

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    path : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metrics : Optional[glyph_metrics_t]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
    #      glyph_metrics_t *metrics)
    ritual = (
        'ritual_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_'
        'metrics_t')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15'
          'glyph_metrics_t')
    self.uglySide.call(
        ritual, glyph, self._addressOf(path), self._addressOf(metrics),
    )

  @overload(QGlyphLayout, ShaperFlags)
  @overload(NoneType, ShaperFlags)
  def recalcAdvances(
      self,
      a0: Optional[QGlyphLayout],
      a1: ShaperFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngine::recalcAdvances(QGlyphLayout *a0,
    ShaperFlags a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#recalcAdvances

    Parameters
    ----------

    a0 : Optional[QGlyphLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : ShaperFlags
      Passed on as its number.
    """
    #  void QFontEngine::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
    #      const
    ritual = (
        'ritual_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_'
        '10ShaperFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFla'
          'gsINS_10ShaperFlagEE')
    self.uglySide.call(ritual, self._addressOf(a0, 'QGlyphLayout'), a1.value)

  @overload(QGlyphLayout, ShaperFlags)
  @overload(NoneType, ShaperFlags)
  def doKerning(self, a0: Optional[QGlyphLayout], a1: ShaperFlags) -> None:
    """
    Calls Qt's 'void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#doKerning

    Parameters
    ----------

    a0 : Optional[QGlyphLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : ShaperFlags
      Passed on as its number.
    """
    #  void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
    ritual = (
        'ritual_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10Shap'
        'erFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_'
          '10ShaperFlagEE')
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
    Calls Qt's 'void QFontEngine::addOutlineToPath(qreal a0, qreal a1, const
    QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#addOutlineToPath

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
    #  void QFontEngine::addOutlineToPath(qreal a0, qreal a1, const
    #      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags flags)
    ritual = (
        'ritual_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPai'
        'nterPath6QFlagsIN9QTextItem10RenderFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP'
          '12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE')
    self.uglySide.call(
        ritual,
        a0, a1, self._valueOf(a2, 'QGlyphLayout'), self._addressOf(a3),
        flags.value,
    )

  @overload(float, float, QGlyphLayout, QPainterPath, QTextItem.RenderFlags)
  @overload(float, float, QGlyphLayout, NoneType, QTextItem.RenderFlags)
  def addBitmapFontToPath(
      self,
      x: float,
      y: float,
      a2: QGlyphLayout,
      a3: Optional[QPainterPath],
      a4: QTextItem.RenderFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngine::addBitmapFontToPath(qreal x, qreal y, const
    QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#addBitmapFontToPath

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    a2 : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    a3 : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a4 : QTextItem.RenderFlags
      Passed on as its number.
    """
    #  void QFontEngine::addBitmapFontToPath(qreal x, qreal y, const
    #      QGlyphLayout &a2, QPainterPath *a3, QTextItem::RenderFlags a4)
    self.uglySide.call(
        'ritual_ZN11QFontEngine19addBitmapFontToPathEddRK12QGlyphLayoutP12Q'
        'PainterPath6QFlagsIN9QTextItem10RenderFlagEE',
        x, y, self._valueOf(a2, 'QGlyphLayout'), self._addressOf(a3),
        a4.value,
    )

  @overload(int)
  def alphaMapForGlyph(self, a0: int) -> QImage:
    """
    Calls Qt's 'QImage QFontEngine::alphaMapForGlyph(glyph_t a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#alphaMapForGlyph

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngine::alphaMapForGlyph(glyph_t a0)
    ritual = 'ritual_ZN11QFontEngine16alphaMapForGlyphEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFontEngine16alphaMapForGlyphEj'
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
    Calls Qt's 'QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const
    QFixedPoint &subPixelPosition)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#alphaMapForGlyph

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
    #  QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
    #      &subPixelPosition)
    ritual = 'ritual_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint')
    address = self.uglySide.call(
        ritual, glyph, self._valueOf(subPixelPosition),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QTransform)
  def alphaMapForGlyph(self, a0: int, t: QTransform) -> QImage:
    """
    Calls Qt's 'QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const
    QTransform &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#alphaMapForGlyph

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
    #  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
    ritual = 'ritual_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform'
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
    Calls Qt's 'QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const
    QFixedPoint &subPixelPosition, const QTransform &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#alphaMapForGlyph

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
    #  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QFixedPoint
    #      &subPixelPosition, const QTransform &t)
    ritual = (
        'ritual_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTran'
        'sform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK1'
          '0QTransform')
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
    Calls Qt's 'QImage QFontEngine::alphaRGBMapForGlyph(glyph_t a0, const
    QFixedPoint &subPixelPosition, const QTransform &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#alphaRGBMapForGlyph

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
    #  QImage QFontEngine::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
    #      &subPixelPosition, const QTransform &t)
    ritual = (
        'ritual_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QT'
        'ransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPoint'
          'RK10QTransform')
    address = self.uglySide.call(
        ritual, a0, self._valueOf(subPixelPosition), self._valueOf(t),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QFixedPoint, QTransform)
  @overload(int, QFixedPoint, QTransform, QColor)
  def bitmapForGlyph(
      self,
      a0: int,
      subPixelPosition: QFixedPoint,
      t: QTransform,
      color: Optional[QColor] = None,
  ) -> QImage:
    """
    Calls Qt's 'QImage QFontEngine::bitmapForGlyph(glyph_t a0, const
    QFixedPoint &subPixelPosition, const QTransform &t, const QColor
    &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#bitmapForGlyph

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

    color : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor()' is then passed on.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
    #      &subPixelPosition, const QTransform &t, const QColor &color)
    if color is None:
      from . import QColor
      color = QColor()
    ritual = (
        'ritual_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransf'
        'ormRK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10Q'
          'TransformRK6QColor')
    address = self.uglySide.call(
        ritual,
        a0, self._valueOf(subPixelPosition), self._valueOf(t),
        self._valueOf(color),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QColor)
  def renderedPathForGlyph(self, glyph: int, color: QColor) -> QImage:
    """
    Calls Qt's 'QImage QFontEngine::renderedPathForGlyph(glyph_t glyph, const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#renderedPathForGlyph

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngine::renderedPathForGlyph(glyph_t glyph, const QColor
    #      &color)
    address = self.uglySide.call(
        'ritual_ZN11QFontEngine20renderedPathForGlyphEjRK6QColor',
        glyph, self._valueOf(color),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int, QTransform)
  def glyphTransformExceedsLimit(
      self,
      glyph: int,
      transform: QTransform,
  ) -> bool:
    """
    Calls Qt's 'bool QFontEngine::glyphTransformExceedsLimit(glyph_t glyph,
    const QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#glyphTransformExceedsLimit

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QFontEngine::glyphTransformExceedsLimit(glyph_t glyph, const
    #      QTransform &transform)
    return self.uglySide.call(
        'ritual_ZN11QFontEngine26glyphTransformExceedsLimitEjRK10QTransform',
        glyph, self._valueOf(transform),
    )

  @overload(int, QFixedPoint, GlyphFormat, QTransform)
  def glyphData(
      self,
      glyph: int,
      subPixelPosition: QFixedPoint,
      neededFormat: GlyphFormat,
      t: QTransform,
  ) -> Optional[Glyph]:
    """
    Calls Qt's 'Glyph *QFontEngine::glyphData(glyph_t glyph, const
    QFixedPoint &subPixelPosition, GlyphFormat neededFormat, const QTransform
    &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#glyphData

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    neededFormat : GlyphFormat
      Passed on as its number.

    t : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    Optional[Glyph]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Glyph *QFontEngine::glyphData(glyph_t glyph, const QFixedPoint
    #      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
    ritual = (
        'ritual_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatE'
        'RK10QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphF'
          'ormatERK10QTransform')
    address = self.uglySide.call(
        ritual,
        glyph, self._valueOf(subPixelPosition), neededFormat.value,
        self._valueOf(t),
    )
    return QFontEngine.Glyph._cuteAt(address)

  @overload(int, QFixedPoint, QTransform, GlyphFormat)
  def alphaMapBoundingBox(
      self,
      glyph: int,
      a1: QFixedPoint,
      matrix: QTransform,
      a3: GlyphFormat,
  ) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngine::alphaMapBoundingBox(glyph_t
    glyph, const QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#alphaMapBoundingBox

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    a1 : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    a3 : GlyphFormat
      Passed on as its number.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QFontEngine::alphaMapBoundingBox(glyph_t glyph, const
    #      QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
    ritual = (
        'ritual_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QT'
        'ransformNS_11GlyphFormatE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPoint'
          'RK10QTransformNS_11GlyphFormatE')
    address = self.uglySide.call(
        ritual, glyph, self._valueOf(a1), self._valueOf(matrix), a3.value,
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int)
  def removeGlyphFromCache(self, a0: int) -> None:
    """
    Calls Qt's 'void QFontEngine::removeGlyphFromCache(glyph_t a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#removeGlyphFromCache

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFontEngine::removeGlyphFromCache(glyph_t a0)
    ritual = 'ritual_ZN11QFontEngine20removeGlyphFromCacheEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFontEngine20removeGlyphFromCacheEj'
    self.uglySide.call(ritual, a0)

  @overload(QGlyphLayout)
  def boundingBox(self, glyphs: QGlyphLayout) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngine::boundingBox(const QGlyphLayout
    &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#boundingBox

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
    #  glyph_metrics_t QFontEngine::boundingBox(const QGlyphLayout &glyphs)
    ritual = 'ritual_ZN11QFontEngine11boundingBoxERK12QGlyphLayout'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFontEngine11boundingBoxERK12QGlyphLayout'
    address = self.uglySide.call(
        ritual, self._valueOf(glyphs, 'QGlyphLayout'),
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int)
  def boundingBox(self, glyph: int) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#boundingBox

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
    #  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph)
    address = self.uglySide.call(
        'ritual_ZN11QFontEngine11boundingBoxEj', glyph,
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int, QTransform)
  def boundingBox(self, glyph: int, matrix: QTransform) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const
    QTransform &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#boundingBox

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const
    #      QTransform &matrix)
    ritual = 'ritual_ZN11QFontEngine11boundingBoxEjRK10QTransform'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFontEngine11boundingBoxEjRK10QTransform'
    address = self.uglySide.call(ritual, glyph, self._valueOf(matrix))
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(QGlyphLayout, QTextItem.RenderFlags)
  def tightBoundingBox(
      self,
      glyphs: QGlyphLayout,
      flags: QTextItem.RenderFlags,
  ) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngine::tightBoundingBox(const
    QGlyphLayout &glyphs, QTextItem::RenderFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#tightBoundingBox

    Parameters
    ----------

    glyphs : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    flags : QTextItem.RenderFlags
      Passed on as its number.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t QFontEngine::tightBoundingBox(const QGlyphLayout
    #      &glyphs, QTextItem::RenderFlags flags)
    address = self.uglySide.call(
        'ritual_ZN11QFontEngine16tightBoundingBoxERK12QGlyphLayout6QFlagsIN'
        '9QTextItem10RenderFlagEE',
        self._valueOf(glyphs, 'QGlyphLayout'), flags.value,
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(GlyphFormat)
  def glyphMargin(self, format: GlyphFormat) -> int:
    """
    Calls Qt's 'int QFontEngine::glyphMargin(GlyphFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#glyphMargin

    Parameters
    ----------

    format : GlyphFormat
      Passed on as its number.
    """
    #  int QFontEngine::glyphMargin(GlyphFormat format)
    ritual = 'ritual_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE'
    return self.uglySide.call(ritual, format.value)

  @overload(QFixed)
  def loadKerningPairs(self, scalingFactor: QFixed) -> None:
    """
    Calls Qt's 'void QFontEngine::loadKerningPairs(QFixed scalingFactor)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#loadKerningPairs

    Parameters
    ----------

    scalingFactor : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  void QFontEngine::loadKerningPairs(QFixed scalingFactor)
    self.uglySide.call(
        'ritual_ZN11QFontEngine16loadKerningPairsE6QFixed',
        self._valueOf(scalingFactor),
    )

  @overload(QGlyphLayout)
  def firstLeftBearing(self, glyphs: QGlyphLayout) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::firstLeftBearing(const QGlyphLayout
    &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#firstLeftBearing

    Parameters
    ----------

    glyphs : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::firstLeftBearing(const QGlyphLayout &glyphs)
    address = self.uglySide.call(
        'ritual_ZN11QFontEngine16firstLeftBearingERK12QGlyphLayout',
        self._valueOf(glyphs, 'QGlyphLayout'),
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  @overload(QGlyphLayout)
  def lastRightBearing(self, glyphs: QGlyphLayout) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngine::lastRightBearing(const QGlyphLayout
    &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengine.html#lastRightBearing

    Parameters
    ----------

    glyphs : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngine::lastRightBearing(const QGlyphLayout &glyphs)
    address = self.uglySide.call(
        'ritual_ZN11QFontEngine16lastRightBearingERK12QGlyphLayout',
        self._valueOf(glyphs, 'QGlyphLayout'),
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  def initializeHeightMetrics(self) -> None:
    """
    Calls Qt's 'void QFontEngine::initializeHeightMetrics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengine.html#initializeHeightMetrics
    """
    #  void QFontEngine::initializeHeightMetrics() const
    ritual = 'ritual_ZNK11QFontEngine23initializeHeightMetricsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFontEngine23initializeHeightMetricsEv'
    self.uglySide.call(ritual)

  @staticmethod
  def addGlyphsToPath(*__, **_) -> Never:
    """
    Qt's 'void QFontEngine::addGlyphsToPath(glyph_t *glyphs, QFixedPoint
    *positions, int nglyphs, QPainterPath *path, QTextItem::RenderFlags
    flags)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QFontEngine.addGlyphsToPath' has no cute function yet. Qt's 'void "
        "QFontEngine::addGlyphsToPath(glyph_t *glyphs, QFixedPoint "
        "*positions, int nglyphs, QPainterPath *path, "
        "QTextItem::RenderFlags flags)': takes a number to change where it "
        "is.")

  @staticmethod
  def clearGlyphCache(*__, **_) -> Never:
    """
    Qt's 'void QFontEngine::clearGlyphCache(const void *key)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.clearGlyphCache' has no cute function yet. Qt's 'void "
        "QFontEngine::clearGlyphCache(const void *key)': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def getCMap(*__, **_) -> Never:
    """
    Qt's 'const uchar *QFontEngine::getCMap(const uchar *table, uint
    tableSize, bool *isSymbolFont, int *cmapSize)': names 'uchar', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.getCMap' has no cute function yet. Qt's 'const uchar "
        "*QFontEngine::getCMap(const uchar *table, uint tableSize, bool "
        "*isSymbolFont, int *cmapSize)': names 'uchar', which has no cute "
        "class yet.")

  @staticmethod
  def getGlyphBearings(*__, **_) -> Never:
    """
    Qt's 'void QFontEngine::getGlyphBearings(glyph_t glyph, qreal
    *leftBearing, qreal *rightBearing)': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QFontEngine.getGlyphBearings' has no cute function yet. Qt's "
        "'void QFontEngine::getGlyphBearings(glyph_t glyph, qreal "
        "*leftBearing, qreal *rightBearing)': takes a number to change "
        "where it is.")

  @staticmethod
  def getGlyphPositions(*__, **_) -> Never:
    """
    Qt's 'void QFontEngine::getGlyphPositions(const QGlyphLayout &glyphs,
    const QTransform &matrix, QTextItem::RenderFlags flags,
    QVarLengthArray<glyph_t> &glyphs_out, QVarLengthArray<QFixedPoint>
    &positions)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFontEngine.getGlyphPositions' has no cute function yet. Qt's "
        "'void QFontEngine::getGlyphPositions(const QGlyphLayout &glyphs, "
        "const QTransform &matrix, QTextItem::RenderFlags flags, "
        "QVarLengthArray<glyph_t> &glyphs_out, QVarLengthArray<QFixedPoint> "
        "&positions)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def getPointInOutline(*__, **_) -> Never:
    """
    Qt's 'int QFontEngine::getPointInOutline(glyph_t glyph, int flags,
    quint32 point, QFixed *xpos, QFixed *ypos, quint32 *nPoints)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QFontEngine.getPointInOutline' has no cute function yet. Qt's "
        "'int QFontEngine::getPointInOutline(glyph_t glyph, int flags, "
        "quint32 point, QFixed *xpos, QFixed *ypos, quint32 *nPoints)': "
        "takes a number to change where it is.")

  @staticmethod
  def getSfntTableData(*__, **_) -> Never:
    """
    Qt's 'bool QFontEngine::getSfntTableData(uint tag, uchar *buffer, uint
    *length) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QFontEngine.getSfntTableData' has no cute function yet. Qt's "
        "'bool QFontEngine::getSfntTableData(uint tag, uchar *buffer, uint "
        "*length) const': takes a number to change where it is.")

  @staticmethod
  def getTrueTypeGlyphIndex(*__, **_) -> Never:
    """
    Qt's 'quint32 QFontEngine::getTrueTypeGlyphIndex(const uchar *cmap, int
    cmapSize, uint unicode)': names 'uchar', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.getTrueTypeGlyphIndex' has no cute function yet. Qt's "
        "'quint32 QFontEngine::getTrueTypeGlyphIndex(const uchar *cmap, int "
        "cmapSize, uint unicode)': names 'uchar', which has no cute class "
        "yet.")

  @staticmethod
  def glyphCache(*__, **_) -> Never:
    """
    Qt's 'QFontEngineGlyphCache *QFontEngine::glyphCache(const void *key,
    GlyphFormat format, const QTransform &transform, const QColor &color)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.glyphCache' has no cute function yet. Qt's "
        "'QFontEngineGlyphCache *QFontEngine::glyphCache(const void *key, "
        "GlyphFormat format, const QTransform &transform, const QColor "
        "&color) const': names 'void', which has no cute class yet.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QFontEngine::handle() const': gives 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.handle' has no cute function yet. Qt's 'Qt::HANDLE "
        "QFontEngine::handle() const': gives 'void', which has no cute "
        "class yet.")

  @staticmethod
  def harfbuzzFace(*__, **_) -> Never:
    """
    Qt's 'void *QFontEngine::harfbuzzFace() const': gives 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.harfbuzzFace' has no cute function yet. Qt's 'void "
        "*QFontEngine::harfbuzzFace() const': gives 'void', which has no "
        "cute class yet.")

  @staticmethod
  def harfbuzzFont(*__, **_) -> Never:
    """
    Qt's 'void *QFontEngine::harfbuzzFont() const': gives 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.harfbuzzFont' has no cute function yet. Qt's 'void "
        "*QFontEngine::harfbuzzFont() const': gives 'void', which has no "
        "cute class yet.")

  @staticmethod
  def setGlyphCache(*__, **_) -> Never:
    """
    Qt's 'void QFontEngine::setGlyphCache(const void *key,
    QFontEngineGlyphCache *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFontEngine.setGlyphCache' has no cute function yet. Qt's 'void "
        "QFontEngine::setGlyphCache(const void *key, QFontEngineGlyphCache "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def stringToCMap(*__, **_) -> Never:
    """
    Qt's 'int QFontEngine::stringToCMap(const QChar *str, int len,
    QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QFontEngine.stringToCMap' has no cute function yet. Qt's 'int "
        "QFontEngine::stringToCMap(const QChar *str, int len, QGlyphLayout "
        "*glyphs, int *nglyphs, ShaperFlags flags) const': takes a number "
        "to change where it is.")
