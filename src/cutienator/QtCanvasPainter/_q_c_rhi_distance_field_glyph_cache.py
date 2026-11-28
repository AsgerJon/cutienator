"""
QCRhiDistanceFieldGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCRhiDistanceFieldGlyphCache to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QRawFont, QRhi, QRhiResourceUpdateBatch, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRawFont = WAIT['QRawFont']
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiTexture = WAIT['QRhiTexture']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCRhiDistanceFieldGlyphCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCRhiDistanceFieldGlyphCache: a plain Python object
  standing in front of one C++ QCRhiDistanceFieldGlyphCache.

  What exists
  -----------

  Every function of Qt's QCRhiDistanceFieldGlyphCache that has a ritual and
  that Python can call so far, 16 names in all: 'setRawFont',
  'createTexture', 'resizeTexture', 'optimizeAfterRendering',
  'commitResourceUpdate', 'solidTileTexCoord', 'ensureSolidTileTexture',
  'uploadSolidTileIfNeeded', 'maxTextureSize', 'useTextureResizeWorkaround',
  'updateRhiTexture', 'glyphMetrics', 'fontScale', 'distanceFieldRadius',
  'textureInfo', 'ensureUpdateBatch'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCRhiDistanceFieldGlyphCache::~QCRhiDistanceFieldGlyphCache()': the
    destructor: Python never removes a C++ QCRhiDistanceFieldGlyphCache.
  - Qt's 'void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo
    *texInfo, int width, int height, const void *pixels)': names 'void',
    which has no cute class yet.
  - Qt's 'void QCRhiDistanceFieldGlyphCache::referenceGlyphs(const
    QVarLengthArray<glyph_t, 16> &glyphs)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<TextureInfo> &QCRhiDistanceFieldGlyphCache::getTextures()':
    gives a type Python has no way to take yet.
  - Qt's 'const QList<TextureInfo>
    &QCRhiDistanceFieldGlyphCache::getTextures() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QCRhiDistanceFieldGlyphCache::markGlyphsToRender(const
    QList<glyph_t> &glyphs)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QCRhiDistanceFieldGlyphCache::releaseGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  12 of the 36 functions Qt declares: 11 leans on
  'QCRhiDistanceFieldGlyphCache; 1 Qt's library has no name for it, and its
  code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCRhiDistanceFieldGlyphCache is created at the first use, not by
    'QCRhiDistanceFieldGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCRhiDistanceFieldGlyphCache.
  - Each name of Qt's QCRhiDistanceFieldGlyphCache that has no cute function
    yet, 'addGlyphs', 'emptyData', 'ensureSolidTile', 'generateVertices',
    'getTextures', 'glyphData', 'markGlyphsToRender', 'populate',
    'referenceGlyphs', 'releaseGlyphs', 'requestGlyphs', 'setGlyphTexture',
    'setGlyphs', 'setGlyphsPosition', 'storeGlyphs', 'update', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QCRhiDistanceFieldGlyphCache, each a class
  #  in here as in C++.

  class GlyphData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCRhiDistanceFieldGlyphCache::GlyphData: a plain
    Python object standing in front of one C++
    QCRhiDistanceFieldGlyphCache::GlyphData.

    C++ hands a QCRhiDistanceFieldGlyphCache::GlyphData around as a copy, so
    every C++ QCRhiDistanceFieldGlyphCache::GlyphData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QCRhiDistanceFieldGlyphCache::GlyphData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCRhiDistanceFieldGlyphCache::GlyphData::~GlyphData()': the
      destructor: Python removes its C++
      QCRhiDistanceFieldGlyphCache::GlyphData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCRhiDistanceFieldGlyphCache::GlyphData is created at the first
      use, not by 'QCRhiDistanceFieldGlyphCache::GlyphData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCRhiDistanceFieldGlyphCache::GlyphData back gives
      a copy the ritual made for Python, in a new cute
      QCRhiDistanceFieldGlyphCache::GlyphData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCRhiDistanceFieldGlyphCache::GlyphData'

    #  Qt's '~QCRhiDistanceFieldGlyphCache::GlyphData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCRhiDistanceFieldGlyphCache::GlyphData behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QCRhiDistanceFieldGlyphCache9GlyphDataD1Ev')

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

  class GlyphPosition(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCRhiDistanceFieldGlyphCache::GlyphPosition: a
    plain Python object standing in front of one C++
    QCRhiDistanceFieldGlyphCache::GlyphPosition.

    C++ hands a QCRhiDistanceFieldGlyphCache::GlyphPosition around as a copy,
    so every C++ QCRhiDistanceFieldGlyphCache::GlyphPosition behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QCRhiDistanceFieldGlyphCache::GlyphPosition yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCRhiDistanceFieldGlyphCache::GlyphPosition::~GlyphPosition()':
      the destructor: Python removes its C++
      QCRhiDistanceFieldGlyphCache::GlyphPosition by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCRhiDistanceFieldGlyphCache::GlyphPosition is created at the
      first use, not by 'QCRhiDistanceFieldGlyphCache::GlyphPosition(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCRhiDistanceFieldGlyphCache::GlyphPosition back
      gives a copy the ritual made for Python, in a new cute
      QCRhiDistanceFieldGlyphCache::GlyphPosition.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCRhiDistanceFieldGlyphCache::GlyphPosition'

    #  Qt's '~QCRhiDistanceFieldGlyphCache::GlyphPosition()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCRhiDistanceFieldGlyphCache::GlyphPosition behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QCRhiDistanceFieldGlyphCache13GlyphPositionD1Ev')

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

  class Metrics(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCRhiDistanceFieldGlyphCache::Metrics: a plain
    Python object standing in front of one C++
    QCRhiDistanceFieldGlyphCache::Metrics.

    C++ hands a QCRhiDistanceFieldGlyphCache::Metrics around as a copy, so
    every C++ QCRhiDistanceFieldGlyphCache::Metrics behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCRhiDistanceFieldGlyphCache::Metrics that has a
    ritual and that Python can call so far, 1 name in all: 'isNull'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCRhiDistanceFieldGlyphCache::Metrics::~Metrics()': the
      destructor: Python removes its C++
      QCRhiDistanceFieldGlyphCache::Metrics by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCRhiDistanceFieldGlyphCache::Metrics is created at the first
      use, not by 'QCRhiDistanceFieldGlyphCache::Metrics(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCRhiDistanceFieldGlyphCache::Metrics back gives a
      copy the ritual made for Python, in a new cute
      QCRhiDistanceFieldGlyphCache::Metrics.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCRhiDistanceFieldGlyphCache::Metrics'

    #  Qt's '~QCRhiDistanceFieldGlyphCache::Metrics()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QCRhiDistanceFieldGlyphCache::Metrics behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN28QCRhiDistanceFieldGlyphCache7MetricsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QCRhiDistanceFieldGlyphCache::Metrics::isNull()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache-metrics.html#isNull
      """
      #  bool QCRhiDistanceFieldGlyphCache::Metrics::isNull() const
      return self.uglySide.call(
          'ritual_ZNK28QCRhiDistanceFieldGlyphCache7Metrics6isNullEv',
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

  class TexCoord(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCRhiDistanceFieldGlyphCache::TexCoord: a plain
    Python object standing in front of one C++
    QCRhiDistanceFieldGlyphCache::TexCoord.

    C++ hands a QCRhiDistanceFieldGlyphCache::TexCoord around as a copy, so
    every C++ QCRhiDistanceFieldGlyphCache::TexCoord behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCRhiDistanceFieldGlyphCache::TexCoord that has a
    ritual and that Python can call so far, 2 names in all: 'isNull',
    'isValid'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCRhiDistanceFieldGlyphCache::TexCoord::~TexCoord()': the
      destructor: Python removes its C++
      QCRhiDistanceFieldGlyphCache::TexCoord by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCRhiDistanceFieldGlyphCache::TexCoord is created at the first
      use, not by 'QCRhiDistanceFieldGlyphCache::TexCoord(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCRhiDistanceFieldGlyphCache::TexCoord back gives a
      copy the ritual made for Python, in a new cute
      QCRhiDistanceFieldGlyphCache::TexCoord.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCRhiDistanceFieldGlyphCache::TexCoord'

    #  Qt's '~QCRhiDistanceFieldGlyphCache::TexCoord()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QCRhiDistanceFieldGlyphCache::TexCoord behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QCRhiDistanceFieldGlyphCache8TexCoordD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QCRhiDistanceFieldGlyphCache::TexCoord::isNull()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache-texcoord.html
      """
      #  bool QCRhiDistanceFieldGlyphCache::TexCoord::isNull() const
      return self.uglySide.call(
          'ritual_ZNK28QCRhiDistanceFieldGlyphCache8TexCoord6isNullEv',
      )

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QCRhiDistanceFieldGlyphCache::TexCoord::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache-texcoord.html
      """
      #  bool QCRhiDistanceFieldGlyphCache::TexCoord::isValid() const
      return self.uglySide.call(
          'ritual_ZNK28QCRhiDistanceFieldGlyphCache8TexCoord7isValidEv',
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

  class TextureInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCRhiDistanceFieldGlyphCache::TextureInfo: a plain
    Python object standing in front of one C++
    QCRhiDistanceFieldGlyphCache::TextureInfo.

    C++ hands a QCRhiDistanceFieldGlyphCache::TextureInfo around as a copy,
    so every C++ QCRhiDistanceFieldGlyphCache::TextureInfo behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCRhiDistanceFieldGlyphCache::TextureInfo that has
    a ritual and that Python can call so far, 1 name in all: '__eq__'. It can
    be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCRhiDistanceFieldGlyphCache::TextureInfo::~TextureInfo()': the
      destructor: Python removes its C++
      QCRhiDistanceFieldGlyphCache::TextureInfo by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCRhiDistanceFieldGlyphCache::TextureInfo is created at the
      first use, not by 'QCRhiDistanceFieldGlyphCache::TextureInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCRhiDistanceFieldGlyphCache::TextureInfo back
      gives a copy the ritual made for Python, in a new cute
      QCRhiDistanceFieldGlyphCache::TextureInfo.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRect = WAIT['QRect']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCRhiDistanceFieldGlyphCache::TextureInfo'

    #  Qt's '~QCRhiDistanceFieldGlyphCache::TextureInfo()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCRhiDistanceFieldGlyphCache::TextureInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QCRhiDistanceFieldGlyphCache11TextureInfoD1Ev')

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
        other: QCRhiDistanceFieldGlyphCache.TextureInfo,
    ) -> bool:
      """
      Calls Qt's 'bool
      QCRhiDistanceFieldGlyphCache::TextureInfo::operator==(const TextureInfo
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache-textureinfo.html

      Parameters
      ----------

      other : QCRhiDistanceFieldGlyphCache.TextureInfo
        Passed on as a value: Qt reads the C++
        QCRhiDistanceFieldGlyphCache::TextureInfo, which stays Python's own.
      """
      #  bool QCRhiDistanceFieldGlyphCache::TextureInfo::operator==(const
      #      TextureInfo &other) const
      return self.uglySide.call(
          'ritual_ZNK28QCRhiDistanceFieldGlyphCache11TextureInfoeqERKS0_',
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

    @overload()
    @overload(QRect)
    def __init__(self, preallocRect: Optional[QRect] = None) -> None:
      """
      Notes what was given, for Qt's
      'QCRhiDistanceFieldGlyphCache::TextureInfo::TextureInfo(const QRect
      &preallocRect)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache-textureinfo.html

      Parameters
      ----------

      preallocRect : Optional[QRect]
        Passed on as a value: Qt reads the C++ QRect, which stays Python's
        own. May be left out, as in Qt: a new 'QRect()' is then passed on.
      """
      #  QCRhiDistanceFieldGlyphCache::TextureInfo::TextureInfo(const QRect
      #      &preallocRect)
      if preallocRect is None:
        from ..QtCore import QRect
        preallocRect = QRect()
      self._noteCreation(
          QCRhiDistanceFieldGlyphCache.TextureInfo, lambda: Rituals.call(
              'ritual_ZN28QCRhiDistanceFieldGlyphCache11TextureInfoC1ERK5QR'
              'ect',
              self._valueOf(preallocRect),
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

  class TexturedPoint2D(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCRhiDistanceFieldGlyphCache::TexturedPoint2D: a
    plain Python object standing in front of one C++
    QCRhiDistanceFieldGlyphCache::TexturedPoint2D.

    C++ hands a QCRhiDistanceFieldGlyphCache::TexturedPoint2D around as a
    copy, so every C++ QCRhiDistanceFieldGlyphCache::TexturedPoint2D behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCRhiDistanceFieldGlyphCache::TexturedPoint2D that
    has a ritual and that Python can call so far, 1 name in all: 'set'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QCRhiDistanceFieldGlyphCache::TexturedPoint2D::~TexturedPoint2D()':
      the destructor: Python removes its C++
      QCRhiDistanceFieldGlyphCache::TexturedPoint2D by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QCRhiDistanceFieldGlyphCache::TexturedPoint2D is created at the
      first use, not by 'QCRhiDistanceFieldGlyphCache::TexturedPoint2D(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCRhiDistanceFieldGlyphCache::TexturedPoint2D back
      gives a copy the ritual made for Python, in a new cute
      QCRhiDistanceFieldGlyphCache::TexturedPoint2D.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCRhiDistanceFieldGlyphCache::TexturedPoint2D'

    #  Qt's '~QCRhiDistanceFieldGlyphCache::TexturedPoint2D()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QCRhiDistanceFieldGlyphCache::TexturedPoint2D behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN28QCRhiDistanceFieldGlyphCache15TexturedPoint2DD1Ev')

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

    @overload(float, float, float, float)
    def set(self, nx: float, ny: float, ntx: float, nty: float) -> None:
      """
      Calls Qt's 'void
      QCRhiDistanceFieldGlyphCache::TexturedPoint2D::set(float nx, float ny,
      float ntx, float nty)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache-texturedpoint2d.html

      Parameters
      ----------

      nx : float
        Passed on as it is.

      ny : float
        Passed on as it is.

      ntx : float
        Passed on as it is.

      nty : float
        Passed on as it is.
      """
      #  void QCRhiDistanceFieldGlyphCache::TexturedPoint2D::set(float nx,
      #      float ny, float ntx, float nty)
      self.uglySide.call(
          'ritual_ZN28QCRhiDistanceFieldGlyphCache15TexturedPoint2D3setEfff'
          'f',
          nx, ny, ntx, nty,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCRhiDistanceFieldGlyphCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def solidTileTexCoord(self) -> TexCoord:
    """
    Calls Qt's 'TexCoord QCRhiDistanceFieldGlyphCache::solidTileTexCoord()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html

    Returns
    -------

    TexCoord
      A new cute QCRhiDistanceFieldGlyphCache::TexCoord around the copy Qt
      gave back. Python owns it.
    """
    #  TexCoord QCRhiDistanceFieldGlyphCache::solidTileTexCoord() const
    address = self.uglySide.call(
        'ritual_ZNK28QCRhiDistanceFieldGlyphCache17solidTileTexCoordEv',
    )
    return QCRhiDistanceFieldGlyphCache.TexCoord._cuteOwning(address)

  def maxTextureSize(self) -> int:
    """
    Calls Qt's 'int QCRhiDistanceFieldGlyphCache::maxTextureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#maxTextureSize
    """
    #  int QCRhiDistanceFieldGlyphCache::maxTextureSize() const
    return self.uglySide.call(
        'ritual_ZNK28QCRhiDistanceFieldGlyphCache14maxTextureSizeEv',
    )

  def useTextureResizeWorkaround(self) -> bool:
    """
    Calls Qt's 'bool
    QCRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html
    """
    #  bool QCRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const
    return self.uglySide.call(
        'ritual_ZNK28QCRhiDistanceFieldGlyphCache26useTextureResizeWorkarou'
        'ndEv',
    )

  @overload(GlyphData, float)
  def glyphMetrics(self, gd: GlyphData, pixelSize: float) -> Metrics:
    """
    Calls Qt's 'Metrics QCRhiDistanceFieldGlyphCache::glyphMetrics(const
    GlyphData &gd, qreal pixelSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#glyphMetrics

    Parameters
    ----------

    gd : GlyphData
      Passed on as a value: Qt reads the C++
      QCRhiDistanceFieldGlyphCache::GlyphData, which stays Python's own.

    pixelSize : float
      Passed on as it is.

    Returns
    -------

    Metrics
      A new cute QCRhiDistanceFieldGlyphCache::Metrics around the copy Qt
      gave back. Python owns it.
    """
    #  Metrics QCRhiDistanceFieldGlyphCache::glyphMetrics(const GlyphData
    #      &gd, qreal pixelSize) const
    address = self.uglySide.call(
        'ritual_ZNK28QCRhiDistanceFieldGlyphCache12glyphMetricsERKNS_9Glyph'
        'DataEd',
        self._valueOf(gd), pixelSize,
    )
    return QCRhiDistanceFieldGlyphCache.Metrics._cuteOwning(address)

  @overload(float)
  def fontScale(self, pixelSize: float) -> float:
    """
    Calls Qt's 'qreal QCRhiDistanceFieldGlyphCache::fontScale(qreal
    pixelSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#fontScale

    Parameters
    ----------

    pixelSize : float
      Passed on as it is.
    """
    #  qreal QCRhiDistanceFieldGlyphCache::fontScale(qreal pixelSize) const
    return self.uglySide.call(
        'ritual_ZNK28QCRhiDistanceFieldGlyphCache9fontScaleEd', pixelSize,
    )

  def distanceFieldRadius(self) -> float:
    """
    Calls Qt's 'qreal QCRhiDistanceFieldGlyphCache::distanceFieldRadius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html
    """
    #  qreal QCRhiDistanceFieldGlyphCache::distanceFieldRadius() const
    return self.uglySide.call(
        'ritual_ZNK28QCRhiDistanceFieldGlyphCache19distanceFieldRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRawFont)
  def setRawFont(self, font: QRawFont) -> None:
    """
    Calls Qt's 'void QCRhiDistanceFieldGlyphCache::setRawFont(const QRawFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#setRawFont

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  void QCRhiDistanceFieldGlyphCache::setRawFont(const QRawFont &font)
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache10setRawFontERK8QRawFont',
        self._valueOf(font),
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

  @overload(QRhi)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhi]) -> None:
    """
    Notes what was given, for Qt's
    'QCRhiDistanceFieldGlyphCache::QCRhiDistanceFieldGlyphCache(QRhi *rhi)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCRhiDistanceFieldGlyphCache::QCRhiDistanceFieldGlyphCache(QRhi *rhi)
    self._noteCreation(QCRhiDistanceFieldGlyphCache, lambda: Rituals.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCacheC1EP4QRhi',
        self._addressOf(rhi),
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

  @overload(TextureInfo, int, int)
  @overload(NoneType, int, int)
  def createTexture(
      self,
      texInfo: Optional[TextureInfo],
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo
    *texInfo, int width, int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#createTexture

    Parameters
    ----------

    texInfo : Optional[TextureInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo,
    #      int width, int height)
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache13createTextureEPNS_11Textu'
        'reInfoEii',
        self._addressOf(texInfo), width, height,
    )

  @overload(TextureInfo, int, int)
  @overload(NoneType, int, int)
  def resizeTexture(
      self,
      texInfo: Optional[TextureInfo],
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QCRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo
    *texInfo, int width, int height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#resizeTexture

    Parameters
    ----------

    texInfo : Optional[TextureInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QCRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo *texInfo,
    #      int width, int height)
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache13resizeTextureEPNS_11Textu'
        'reInfoEii',
        self._addressOf(texInfo), width, height,
    )

  def optimizeAfterRendering(self) -> None:
    """
    Calls Qt's 'void QCRhiDistanceFieldGlyphCache::optimizeAfterRendering()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html
    """
    #  void QCRhiDistanceFieldGlyphCache::optimizeAfterRendering()
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache22optimizeAfterRenderingEv',
    )

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def commitResourceUpdate(
      self,
      batch: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QCRhiDistanceFieldGlyphCache::commitResourceUpdate(
    QRhiResourceUpdateBatch *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html

    Parameters
    ----------

    batch : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCRhiDistanceFieldGlyphCache::commitResourceUpdate(
    #      QRhiResourceUpdateBatch *batch)
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache20commitResourceUpdateEP23Q'
        'RhiResourceUpdateBatch',
        self._addressOf(batch),
    )

  def ensureSolidTileTexture(self) -> None:
    """
    Calls Qt's 'void QCRhiDistanceFieldGlyphCache::ensureSolidTileTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html
    """
    #  void QCRhiDistanceFieldGlyphCache::ensureSolidTileTexture()
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache22ensureSolidTileTextureEv',
    )

  def uploadSolidTileIfNeeded(self) -> None:
    """
    Calls Qt's 'void
    QCRhiDistanceFieldGlyphCache::uploadSolidTileIfNeeded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html
    """
    #  void QCRhiDistanceFieldGlyphCache::uploadSolidTileIfNeeded()
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache23uploadSolidTileIfNeededEv',
    )

  @overload(QRhiTexture, QRhiTexture, QSize)
  @overload(QRhiTexture, NoneType, QSize)
  @overload(NoneType, QRhiTexture, QSize)
  @overload(NoneType, NoneType, QSize)
  def updateRhiTexture(
      self,
      oldTex: Optional[QRhiTexture],
      newTex: Optional[QRhiTexture],
      newTexSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void
    QCRhiDistanceFieldGlyphCache::updateRhiTexture(QRhiTexture *oldTex,
    QRhiTexture *newTex, QSize newTexSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#updateRhiTexture

    Parameters
    ----------

    oldTex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newTex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newTexSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QCRhiDistanceFieldGlyphCache::updateRhiTexture(QRhiTexture
    #      *oldTex, QRhiTexture *newTex, QSize newTexSize)
    self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache16updateRhiTextureEP11QRhiT'
        'extureS1_5QSize',
        self._addressOf(oldTex), self._addressOf(newTex),
        self._valueOf(newTexSize),
    )

  @overload(int)
  def textureInfo(self, index: int) -> Optional[TextureInfo]:
    """
    Calls Qt's 'TextureInfo *QCRhiDistanceFieldGlyphCache::textureInfo(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html#textureInfo

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[TextureInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  TextureInfo *QCRhiDistanceFieldGlyphCache::textureInfo(int index)
    address = self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache11textureInfoEi', index,
    )
    return QCRhiDistanceFieldGlyphCache.TextureInfo._cuteAt(address)

  def ensureUpdateBatch(self) -> bool:
    """
    Calls Qt's 'bool QCRhiDistanceFieldGlyphCache::ensureUpdateBatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcrhidistancefieldglyphcache.html
    """
    #  bool QCRhiDistanceFieldGlyphCache::ensureUpdateBatch()
    return self.uglySide.call(
        'ritual_ZN28QCRhiDistanceFieldGlyphCache17ensureUpdateBatchEv',
    )

  @staticmethod
  def addGlyphs(*__, **_) -> Never:
    """
    Qt's 'bool QCRhiDistanceFieldGlyphCache::addGlyphs(QPointF position,
    const QGlyphRun &glyphs)': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.addGlyphs' has no cute function yet. "
        "Qt's 'bool QCRhiDistanceFieldGlyphCache::addGlyphs(QPointF "
        "position, const QGlyphRun &glyphs)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def emptyData(*__, **_) -> Never:
    """
    Qt's 'GlyphData &QCRhiDistanceFieldGlyphCache::emptyData(glyph_t glyph)':
    leans on 'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.emptyData' has no cute function yet. "
        "Qt's 'GlyphData &QCRhiDistanceFieldGlyphCache::emptyData(glyph_t "
        "glyph)': leans on 'QCRhiDistanceFieldGlyphCache::s_emptyTexture', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def ensureSolidTile(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::ensureSolidTile()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier
    'RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING'.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.ensureSolidTile' has no cute "
        "function yet. Qt's 'void "
        "QCRhiDistanceFieldGlyphCache::ensureSolidTile()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING'.")

  @staticmethod
  def generateVertices(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::generateVertices(VertexList
    *verts, IndexList *indices, const QTransform &transform, QRectF
    *boundingRect)': leans on 'QCRhiDistanceFieldGlyphCache::s_emptyTexture',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.generateVertices' has no cute "
        "function yet. Qt's 'void "
        "QCRhiDistanceFieldGlyphCache::generateVertices(VertexList *verts, "
        "IndexList *indices, const QTransform &transform, QRectF "
        "*boundingRect)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getTextures(*__, **_) -> Never:
    """
    - Qt's 'QList<TextureInfo> &QCRhiDistanceFieldGlyphCache::getTextures()':
      gives a type Python has no way to take yet.
    - Qt's 'const QList<TextureInfo>
      &QCRhiDistanceFieldGlyphCache::getTextures() const': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.getTextures' has no cute function "
        "yet. Qt's 'QList<TextureInfo> "
        "&QCRhiDistanceFieldGlyphCache::getTextures()': gives a type Python "
        "has no way to take yet. Qt's 'const QList<TextureInfo> "
        "&QCRhiDistanceFieldGlyphCache::getTextures() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def glyphData(*__, **_) -> Never:
    """
    Qt's 'GlyphData &QCRhiDistanceFieldGlyphCache::glyphData(glyph_t glyph)':
    leans on 'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.glyphData' has no cute function yet. "
        "Qt's 'GlyphData &QCRhiDistanceFieldGlyphCache::glyphData(glyph_t "
        "glyph)': leans on 'QCRhiDistanceFieldGlyphCache::s_emptyTexture', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def markGlyphsToRender(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::markGlyphsToRender(const
    QList<glyph_t> &glyphs)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.markGlyphsToRender' has no cute "
        "function yet. Qt's 'void "
        "QCRhiDistanceFieldGlyphCache::markGlyphsToRender(const "
        "QList<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'bool QCRhiDistanceFieldGlyphCache::populate(const QList<glyph_t>
    &glyphs)': leans on 'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.populate' has no cute function yet. "
        "Qt's 'bool QCRhiDistanceFieldGlyphCache::populate(const "
        "QList<glyph_t> &glyphs)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def referenceGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::referenceGlyphs(const
    QVarLengthArray<glyph_t, 16> &glyphs)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.referenceGlyphs' has no cute "
        "function yet. Qt's 'void "
        "QCRhiDistanceFieldGlyphCache::referenceGlyphs(const "
        "QVarLengthArray<glyph_t, 16> &glyphs)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def releaseGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::releaseGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.releaseGlyphs' has no cute function "
        "yet. Qt's 'void QCRhiDistanceFieldGlyphCache::releaseGlyphs(const "
        "QSet<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def requestGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::requestGlyphs(const
    QVarLengthArray<glyph_t, 16> &glyphs)': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.requestGlyphs' has no cute function "
        "yet. Qt's 'void QCRhiDistanceFieldGlyphCache::requestGlyphs(const "
        "QVarLengthArray<glyph_t, 16> &glyphs)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setGlyphTexture(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::setGlyphTexture(const
    QList<glyph_t> &glyphs, const TextureInfo &tex)': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.setGlyphTexture' has no cute "
        "function yet. Qt's 'void "
        "QCRhiDistanceFieldGlyphCache::setGlyphTexture(const QList<glyph_t> "
        "&glyphs, const TextureInfo &tex)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setGlyphs(*__, **_) -> Never:
    """
    Qt's 'bool QCRhiDistanceFieldGlyphCache::setGlyphs(QPointF position,
    const QGlyphRun &glyphs)': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.setGlyphs' has no cute function yet. "
        "Qt's 'bool QCRhiDistanceFieldGlyphCache::setGlyphs(QPointF "
        "position, const QGlyphRun &glyphs)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setGlyphsPosition(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::setGlyphsPosition(const
    QList<GlyphPosition> &glyphs)': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.setGlyphsPosition' has no cute "
        "function yet. Qt's 'void "
        "QCRhiDistanceFieldGlyphCache::setGlyphsPosition(const "
        "QList<GlyphPosition> &glyphs)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def storeGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::storeGlyphs(const
    QList<QDistanceField> &glyphs)': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.storeGlyphs' has no cute function "
        "yet. Qt's 'void QCRhiDistanceFieldGlyphCache::storeGlyphs(const "
        "QList<QDistanceField> &glyphs)': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void QCRhiDistanceFieldGlyphCache::update()': leans on
    'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCRhiDistanceFieldGlyphCache.update' has no cute function yet. "
        "Qt's 'void QCRhiDistanceFieldGlyphCache::update()': leans on "
        "'QCRhiDistanceFieldGlyphCache::s_emptyTexture', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
