"""
QTextureGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextureGlyphCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QFontEngine, QFontEngineGlyphCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QColor, QFixedPoint, QImage, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFixedPoint = WAIT['QFixedPoint']
  QTransform = WAIT['QTransform']


class QTextureGlyphCache(QFontEngineGlyphCache):
  """
  The cute side of Qt's QTextureGlyphCache: a plain Python object standing in
  front of one C++ QTextureGlyphCache.

  It is built on the cute 'QFontEngineGlyphCache', as Qt's QTextureGlyphCache
  is built on Qt's QFontEngineGlyphCache, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextureGlyphCache that has a ritual and that Python
  can call so far, 15 names in all: 'hasPendingGlyphs',
  'fillInPendingGlyphs', 'createTextureData', 'resizeTextureData',
  'glyphPadding', 'beginFillTexture', 'fillTexture', 'endFillTexture',
  'createCache', 'resizeCache', 'isNull', 'maxTextureWidth',
  'maxTextureHeight', 'textureMapForGlyph', 'calculateSubPixelPositionCount'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextureGlyphCache::~QTextureGlyphCache()': the destructor: Python
    never removes a C++ QTextureGlyphCache.
  - Qt's 'bool QTextureGlyphCache::populate(QFontEngine *fontEngine,
    qsizetype numGlyphs, const glyph_t *glyphs, const QFixedPoint *positions,
    QPainter::RenderHints renderHints, bool includeGlyphCacheScale)': names
    'glyph_t', which has no cute class yet.

  What to expect
  --------------

  - The C++ QTextureGlyphCache is created at the first use, not by
    'QTextureGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextureGlyphCache.
  - Each name of Qt's QTextureGlyphCache that has no cute function yet,
    'populate', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QTextureGlyphCache, each a class in here as
  #  in C++.

  class Coord(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextureGlyphCache::Coord: a plain Python object
    standing in front of one C++ QTextureGlyphCache::Coord.

    C++ hands a QTextureGlyphCache::Coord around as a copy, so every C++
    QTextureGlyphCache::Coord behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QTextureGlyphCache::Coord that has a ritual and
    that Python can call so far, 1 name in all: 'isNull'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextureGlyphCache::Coord::~Coord()': the destructor: Python
      removes its C++ QTextureGlyphCache::Coord by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QTextureGlyphCache::Coord is created at the first use, not by
      'QTextureGlyphCache::Coord(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextureGlyphCache::Coord back gives a copy the
      ritual made for Python, in a new cute QTextureGlyphCache::Coord.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextureGlyphCache::Coord'

    #  Qt's '~QTextureGlyphCache::Coord()'. Naming it makes this a value
    #  class: Python owns every C++ QTextureGlyphCache::Coord behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QTextureGlyphCache5CoordD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QTextureGlyphCache::Coord::isNull() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextureglyphcache-coord.html#isNull
      """
      #  bool QTextureGlyphCache::Coord::isNull() const
      return self.uglySide.call(
          'ritual_ZNK18QTextureGlyphCache5Coord6isNullEv',
      )

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

  class GlyphAndSubPixelPosition(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextureGlyphCache::GlyphAndSubPixelPosition: a
    plain Python object standing in front of one C++
    QTextureGlyphCache::GlyphAndSubPixelPosition.

    C++ hands a QTextureGlyphCache::GlyphAndSubPixelPosition around as a
    copy, so every C++ QTextureGlyphCache::GlyphAndSubPixelPosition behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QTextureGlyphCache::GlyphAndSubPixelPosition that
    has a ritual and that Python can call so far, 1 name in all: '__eq__'. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextureGlyphCache::GlyphAndSubPixelPosition::
      ~GlyphAndSubPixelPosition()': the destructor: Python removes its C++
      QTextureGlyphCache::GlyphAndSubPixelPosition by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QTextureGlyphCache::GlyphAndSubPixelPosition is created at the
      first use, not by 'QTextureGlyphCache::GlyphAndSubPixelPosition(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextureGlyphCache::GlyphAndSubPixelPosition back
      gives a copy the ritual made for Python, in a new cute
      QTextureGlyphCache::GlyphAndSubPixelPosition.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QFixedPoint = WAIT['QFixedPoint']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextureGlyphCache::GlyphAndSubPixelPosition'

    #  Qt's '~QTextureGlyphCache::GlyphAndSubPixelPosition()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QTextureGlyphCache::GlyphAndSubPixelPosition behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18QTextureGlyphCache24GlyphAndSubPixelPositionD1Ev')

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
    def __eq__(
        self,
        other: QTextureGlyphCache.GlyphAndSubPixelPosition,
    ) -> bool:
      """
      Calls Qt's 'bool
      QTextureGlyphCache::GlyphAndSubPixelPosition::operator==(const
      GlyphAndSubPixelPosition &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextureglyphcache-glyphandsubpixelposition.html

      Parameters
      ----------

      other : QTextureGlyphCache.GlyphAndSubPixelPosition
        Passed on as a value: Qt reads the C++
        QTextureGlyphCache::GlyphAndSubPixelPosition, which stays Python's
        own.
      """
      #  bool QTextureGlyphCache::GlyphAndSubPixelPosition::operator==(const
      #      GlyphAndSubPixelPosition &other) const
      return self.uglySide.call(
          'ritual_ZNK18QTextureGlyphCache24GlyphAndSubPixelPositioneqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int, QFixedPoint)
    def __init__(self, g: int, spp: QFixedPoint) -> None:
      """
      Notes what was given, for Qt's
      'QTextureGlyphCache::GlyphAndSubPixelPosition::
      GlyphAndSubPixelPosition(glyph_t g, const QFixedPoint &spp)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextureglyphcache-glyphandsubpixelposition.html

      Parameters
      ----------

      g : int
        Passed on as it is.

      spp : QFixedPoint
        Passed on as a value: Qt reads the C++ QFixedPoint, which stays
        Python's own.
      """
      #  QTextureGlyphCache::GlyphAndSubPixelPosition::
      #      GlyphAndSubPixelPosition(glyph_t g, const QFixedPoint &spp)
      self._noteCreation(
          QTextureGlyphCache.GlyphAndSubPixelPosition, lambda: Rituals.call(
              'ritual_ZN18QTextureGlyphCache24GlyphAndSubPixelPositionC1EjR'
              'K11QFixedPoint',
              g, self._valueOf(spp),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextureGlyphCache'

  #  A C++ QTextureGlyphCache Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextureGlyphCache'

  #  The functions Qt calls itself that QTextureGlyphCache is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createTextureData': (
          ('_ZN18QTextureGlyphCache17createTextureDataEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'resizeTextureData': (
          ('_ZN18QTextureGlyphCache17resizeTextureDataEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'glyphPadding': (
          ('_ZNK18QTextureGlyphCache12glyphPaddingEv',
           ('int', 'number', ''),
           ()),
      ),
      'beginFillTexture': (
          ('_ZN18QTextureGlyphCache16beginFillTextureEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'fillTexture': (
          ('_ZN18QTextureGlyphCache11fillTextureERKNS_5CoordEjRK11QFixedPoi'
           'nt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTextureGlyphCache.Coord'),
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QFixedPoint'),
           )),
      ),
      'endFillTexture': (
          ('_ZN18QTextureGlyphCache14endFillTextureEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'maxTextureWidth': (
          ('_ZNK18QTextureGlyphCache15maxTextureWidthEv',
           ('int', 'number', ''),
           ()),
      ),
      'maxTextureHeight': (
          ('_ZNK18QTextureGlyphCache16maxTextureHeightEv',
           ('int', 'number', ''),
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

  def hasPendingGlyphs(self) -> bool:
    """
    Calls Qt's 'bool QTextureGlyphCache::hasPendingGlyphs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#hasPendingGlyphs
    """
    #  bool QTextureGlyphCache::hasPendingGlyphs() const
    return self.uglySide.call(
        'ritual_ZNK18QTextureGlyphCache16hasPendingGlyphsEv',
    )

  def glyphPadding(self) -> int:
    """
    Calls Qt's 'int QTextureGlyphCache::glyphPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#glyphPadding
    """
    #  int QTextureGlyphCache::glyphPadding() const
    ritual = 'ritual_ZNK18QTextureGlyphCache12glyphPaddingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QTextureGlyphCache12glyphPaddingEv'
    return self.uglySide.call(ritual)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QTextureGlyphCache::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextureglyphcache.html#isNull
    """
    #  bool QTextureGlyphCache::isNull() const
    return self.uglySide.call('ritual_ZNK18QTextureGlyphCache6isNullEv')

  def maxTextureWidth(self) -> int:
    """
    Calls Qt's 'int QTextureGlyphCache::maxTextureWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#maxTextureWidth
    """
    #  int QTextureGlyphCache::maxTextureWidth() const
    ritual = 'ritual_ZNK18QTextureGlyphCache15maxTextureWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QTextureGlyphCache15maxTextureWidthEv'
    return self.uglySide.call(ritual)

  def maxTextureHeight(self) -> int:
    """
    Calls Qt's 'int QTextureGlyphCache::maxTextureHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#maxTextureHeight
    """
    #  int QTextureGlyphCache::maxTextureHeight() const
    ritual = 'ritual_ZNK18QTextureGlyphCache16maxTextureHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QTextureGlyphCache16maxTextureHeightEv'
    return self.uglySide.call(ritual)

  @overload(int, QFixedPoint)
  def textureMapForGlyph(
      self,
      g: int,
      subPixelPosition: QFixedPoint,
  ) -> QImage:
    """
    Calls Qt's 'QImage QTextureGlyphCache::textureMapForGlyph(glyph_t g,
    const QFixedPoint &subPixelPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#textureMapForGlyph

    Parameters
    ----------

    g : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QTextureGlyphCache::textureMapForGlyph(glyph_t g, const
    #      QFixedPoint &subPixelPosition) const
    address = self.uglySide.call(
        'ritual_ZNK18QTextureGlyphCache18textureMapForGlyphEjRK11QFixedPoin'
        't',
        g, self._valueOf(subPixelPosition),
    )
    from . import QImage
    return QImage._cuteOwning(address)

  @overload(int)
  def calculateSubPixelPositionCount(self, a0: int) -> int:
    """
    Calls Qt's 'int
    QTextureGlyphCache::calculateSubPixelPositionCount(glyph_t a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QTextureGlyphCache::calculateSubPixelPositionCount(glyph_t a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QTextureGlyphCache30calculateSubPixelPositionCountEj',
        a0,
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

  @overload(QFontEngine.GlyphFormat, QTransform)
  @overload(QFontEngine.GlyphFormat, QTransform, QColor)
  def __init__(
      self,
      format: QFontEngine.GlyphFormat,
      matrix: QTransform,
      color: Optional[QColor] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextureGlyphCache::QTextureGlyphCache(QFontEngine::GlyphFormat format,
    const QTransform &matrix, const QColor &color)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#QTextureGlyphCache

    Parameters
    ----------

    format : QFontEngine.GlyphFormat
      Passed on as its number.

    matrix : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    color : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor()' is then passed on.
    """
    #  QTextureGlyphCache::QTextureGlyphCache(QFontEngine::GlyphFormat
    #      format, const QTransform &matrix, const QColor &color)
    if color is None:
      from . import QColor
      color = QColor()
    self._noteCreation(QTextureGlyphCache, lambda: Rituals.call(
        'ritual_ZN18QTextureGlyphCacheC1EN11QFontEngine11GlyphFormatERK10QT'
        'ransformRK6QColor',
        format.value, self._valueOf(matrix), self._valueOf(color),
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

  def fillInPendingGlyphs(self) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::fillInPendingGlyphs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#fillInPendingGlyphs
    """
    #  void QTextureGlyphCache::fillInPendingGlyphs()
    self.uglySide.call(
        'ritual_ZN18QTextureGlyphCache19fillInPendingGlyphsEv',
    )

  @overload(int, int)
  def createTextureData(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::createTextureData(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#createTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QTextureGlyphCache::createTextureData(int width, int height)
    self.uglySide.call(
        'ritual_ZN18QTextureGlyphCache17createTextureDataEii', width, height,
    )

  @overload(int, int)
  def resizeTextureData(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::resizeTextureData(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#resizeTextureData

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QTextureGlyphCache::resizeTextureData(int width, int height)
    self.uglySide.call(
        'ritual_ZN18QTextureGlyphCache17resizeTextureDataEii', width, height,
    )

  def beginFillTexture(self) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::beginFillTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#beginFillTexture
    """
    #  void QTextureGlyphCache::beginFillTexture()
    ritual = 'ritual_ZN18QTextureGlyphCache16beginFillTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QTextureGlyphCache16beginFillTextureEv'
    self.uglySide.call(ritual)

  @overload(Coord, int, QFixedPoint)
  def fillTexture(
      self,
      coord: Coord,
      glyph: int,
      subPixelPosition: QFixedPoint,
  ) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::fillTexture(const Coord &coord,
    glyph_t glyph, const QFixedPoint &subPixelPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#fillTexture

    Parameters
    ----------

    coord : Coord
      Passed on as a value: Qt reads the C++ QTextureGlyphCache::Coord, which
      stays Python's own.

    glyph : int
      Passed on as it is.

    subPixelPosition : QFixedPoint
      Passed on as a value: Qt reads the C++ QFixedPoint, which stays
      Python's own.
    """
    #  void QTextureGlyphCache::fillTexture(const Coord &coord, glyph_t
    #      glyph, const QFixedPoint &subPixelPosition)
    self.uglySide.call(
        'ritual_ZN18QTextureGlyphCache11fillTextureERKNS_5CoordEjRK11QFixed'
        'Point',
        self._valueOf(coord), glyph, self._valueOf(subPixelPosition),
    )

  def endFillTexture(self) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::endFillTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#endFillTexture
    """
    #  void QTextureGlyphCache::endFillTexture()
    ritual = 'ritual_ZN18QTextureGlyphCache14endFillTextureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QTextureGlyphCache14endFillTextureEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def createCache(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::createCache(int width, int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#createCache

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QTextureGlyphCache::createCache(int width, int height)
    self.uglySide.call(
        'ritual_ZN18QTextureGlyphCache11createCacheEii', width, height,
    )

  @overload(int, int)
  def resizeCache(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QTextureGlyphCache::resizeCache(int width, int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextureglyphcache.html#resizeCache

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QTextureGlyphCache::resizeCache(int width, int height)
    self.uglySide.call(
        'ritual_ZN18QTextureGlyphCache11resizeCacheEii', width, height,
    )

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'bool QTextureGlyphCache::populate(QFontEngine *fontEngine,
    qsizetype numGlyphs, const glyph_t *glyphs, const QFixedPoint *positions,
    QPainter::RenderHints renderHints, bool includeGlyphCacheScale)': names
    'glyph_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextureGlyphCache.populate' has no cute function yet. Qt's 'bool "
        "QTextureGlyphCache::populate(QFontEngine *fontEngine, qsizetype "
        "numGlyphs, const glyph_t *glyphs, const QFixedPoint *positions, "
        "QPainter::RenderHints renderHints, bool includeGlyphCacheScale)': "
        "names 'glyph_t', which has no cute class yet.")
