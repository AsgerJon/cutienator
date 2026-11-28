"""
QSGDistanceFieldGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGDistanceFieldGlyphCache to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QDistanceField, QRawFont, QRhiTexture
  from . import QSGDistanceFieldGlyphConsumer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDistanceField = WAIT['QDistanceField']
  QRhiTexture = WAIT['QRhiTexture']
  QSGDistanceFieldGlyphConsumer = WAIT['QSGDistanceFieldGlyphConsumer']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDistanceFieldGlyphCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGDistanceFieldGlyphCache: a plain Python object
  standing in front of one C++ QSGDistanceFieldGlyphCache.

  What exists
  -----------

  Every function of Qt's QSGDistanceFieldGlyphCache that has a ritual and
  that Python can call so far, 21 names in all: 'referenceFont', 'fontScale',
  'distanceFieldRadius', 'glyphCount', 'doubleGlyphResolution',
  'renderTypeQuality', 'glyphMetrics', 'glyphTexCoord', 'glyphTexture',
  'update', 'registerGlyphNode', 'unregisterGlyphNode',
  'processPendingGlyphs', 'eightBitFormatIsAlphaSwizzled',
  'screenSpaceDerivativesSupported', 'isActive', 'storeGlyphs',
  'removeGlyph', 'updateRhiTexture', 'containsGlyph', 'baseFontSize'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDistanceFieldGlyphCache::~QSGDistanceFieldGlyphCache()': the
    destructor: Python never removes a C++ QSGDistanceFieldGlyphCache.
  - Qt's 'void QSGDistanceFieldGlyphCache::populate(const QList<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::release(const QList<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::requestGlyphs(const QSet<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::referenceGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::releaseGlyphs(const QSet<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::setGlyphsPosition(const
    QList<GlyphPosition> &glyphs)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::setGlyphsTexture(const
    QList<glyph_t> &glyphs, const Texture &tex)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QSGDistanceFieldGlyphCache::markGlyphsToRender(const
    QList<glyph_t> &glyphs)': takes a type Python has no way to hand over
    yet.
  - Qt's 'GlyphData &QSGDistanceFieldGlyphCache::glyphData(glyph_t glyph)':
    gives a type Python has no way to take yet.
  - Qt's 'GlyphData &QSGDistanceFieldGlyphCache::emptyData(glyph_t glyph)':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 33 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QSGDistanceFieldGlyphCache is created at the first use, not by
    'QSGDistanceFieldGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDistanceFieldGlyphCache.
  - Each name of Qt's QSGDistanceFieldGlyphCache that has no cute function
    yet, '__init__', 'emptyData', 'glyphData', 'markGlyphsToRender',
    'populate', 'referenceGlyphs', 'release', 'releaseGlyphs',
    'requestGlyphs', 'setGlyphsPosition', 'setGlyphsTexture', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGDistanceFieldGlyphCache, each a class in
  #  here as in C++.

  class Metrics(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGDistanceFieldGlyphCache::Metrics: a plain Python
    object standing in front of one C++ QSGDistanceFieldGlyphCache::Metrics.

    C++ hands a QSGDistanceFieldGlyphCache::Metrics around as a copy, so
    every C++ QSGDistanceFieldGlyphCache::Metrics behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSGDistanceFieldGlyphCache::Metrics that has a
    ritual and that Python can call so far, 1 name in all: 'isNull'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGDistanceFieldGlyphCache::Metrics::~Metrics()': the destructor:
      Python removes its C++ QSGDistanceFieldGlyphCache::Metrics by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QSGDistanceFieldGlyphCache::Metrics is created at the first
      use, not by 'QSGDistanceFieldGlyphCache::Metrics(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGDistanceFieldGlyphCache::Metrics back gives a
      copy the ritual made for Python, in a new cute
      QSGDistanceFieldGlyphCache::Metrics.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGDistanceFieldGlyphCache::Metrics'

    #  Qt's '~QSGDistanceFieldGlyphCache::Metrics()'. Naming it makes this a
    #  value class: Python owns every C++ QSGDistanceFieldGlyphCache::Metrics
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN26QSGDistanceFieldGlyphCache7MetricsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QSGDistanceFieldGlyphCache::Metrics::isNull() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgdistancefieldglyphcache-metrics.html#isNull
      """
      #  bool QSGDistanceFieldGlyphCache::Metrics::isNull() const
      return self.uglySide.call(
          'ritual_ZNK26QSGDistanceFieldGlyphCache7Metrics6isNullEv',
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
    The cute side of Qt's QSGDistanceFieldGlyphCache::TexCoord: a plain
    Python object standing in front of one C++
    QSGDistanceFieldGlyphCache::TexCoord.

    C++ hands a QSGDistanceFieldGlyphCache::TexCoord around as a copy, so
    every C++ QSGDistanceFieldGlyphCache::TexCoord behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSGDistanceFieldGlyphCache::TexCoord that has a
    ritual and that Python can call so far, 2 names in all: 'isNull',
    'isValid'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGDistanceFieldGlyphCache::TexCoord::~TexCoord()': the
      destructor: Python removes its C++ QSGDistanceFieldGlyphCache::TexCoord
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSGDistanceFieldGlyphCache::TexCoord is created at the first
      use, not by 'QSGDistanceFieldGlyphCache::TexCoord(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGDistanceFieldGlyphCache::TexCoord back gives a
      copy the ritual made for Python, in a new cute
      QSGDistanceFieldGlyphCache::TexCoord.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGDistanceFieldGlyphCache::TexCoord'

    #  Qt's '~QSGDistanceFieldGlyphCache::TexCoord()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QSGDistanceFieldGlyphCache::TexCoord behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN26QSGDistanceFieldGlyphCache8TexCoordD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QSGDistanceFieldGlyphCache::TexCoord::isNull() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgdistancefieldglyphcache-texcoord.html#isNull
      """
      #  bool QSGDistanceFieldGlyphCache::TexCoord::isNull() const
      return self.uglySide.call(
          'ritual_ZNK26QSGDistanceFieldGlyphCache8TexCoord6isNullEv',
      )

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QSGDistanceFieldGlyphCache::TexCoord::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgdistancefieldglyphcache-texcoord.html#isValid
      """
      #  bool QSGDistanceFieldGlyphCache::TexCoord::isValid() const
      return self.uglySide.call(
          'ritual_ZNK26QSGDistanceFieldGlyphCache8TexCoord7isValidEv',
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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSGDistanceFieldGlyphCache::TexCoord::TexCoord()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgdistancefieldglyphcache-texcoord.html
      """
      #  QSGDistanceFieldGlyphCache::TexCoord::TexCoord()
      self._noteCreation(
          QSGDistanceFieldGlyphCache.TexCoord, lambda: Rituals.call(
              'ritual_ZN26QSGDistanceFieldGlyphCache8TexCoordC1Ev',
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

  class Texture(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGDistanceFieldGlyphCache::Texture: a plain Python
    object standing in front of one C++ QSGDistanceFieldGlyphCache::Texture.

    C++ hands a QSGDistanceFieldGlyphCache::Texture around as a copy, so
    every C++ QSGDistanceFieldGlyphCache::Texture behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QSGDistanceFieldGlyphCache::Texture that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGDistanceFieldGlyphCache::Texture::~Texture()': the destructor:
      Python removes its C++ QSGDistanceFieldGlyphCache::Texture by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QSGDistanceFieldGlyphCache::Texture is created at the first
      use, not by 'QSGDistanceFieldGlyphCache::Texture(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGDistanceFieldGlyphCache::Texture back gives a
      copy the ritual made for Python, in a new cute
      QSGDistanceFieldGlyphCache::Texture.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGDistanceFieldGlyphCache::Texture'

    #  Qt's '~QSGDistanceFieldGlyphCache::Texture()'. Naming it makes this a
    #  value class: Python owns every C++ QSGDistanceFieldGlyphCache::Texture
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN26QSGDistanceFieldGlyphCache7TextureD1Ev'

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
    def __eq__(self, other: QSGDistanceFieldGlyphCache.Texture) -> bool:
      """
      Calls Qt's 'bool QSGDistanceFieldGlyphCache::Texture::operator==(const
      Texture &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgdistancefieldglyphcache-texture.html

      Parameters
      ----------

      other : QSGDistanceFieldGlyphCache.Texture
        Passed on as a value: Qt reads the C++
        QSGDistanceFieldGlyphCache::Texture, which stays Python's own.
      """
      #  bool QSGDistanceFieldGlyphCache::Texture::operator==(const Texture
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK26QSGDistanceFieldGlyphCache7TextureeqERKS0_',
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
  __qt_class__ = 'QSGDistanceFieldGlyphCache'

  #  A C++ QSGDistanceFieldGlyphCache Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDistanceFieldGlyphCache'

  #  The functions Qt calls itself that QSGDistanceFieldGlyphCache is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'requestGlyphs': (
          'void QSGDistanceFieldGlyphCache::requestGlyphs(const '
          'QSet<glyph_t> &)',
      ),
      'storeGlyphs': (
          'void QSGDistanceFieldGlyphCache::storeGlyphs(const '
          'QList<QDistanceField> &)',
      ),
      'referenceGlyphs': (
          'void QSGDistanceFieldGlyphCache::referenceGlyphs(const '
          'QSet<glyph_t> &)',
      ),
      'releaseGlyphs': (
          'void QSGDistanceFieldGlyphCache::releaseGlyphs(const '
          'QSet<glyph_t> &)',
      ),
  }

  #  The functions Qt calls itself that QSGDistanceFieldGlyphCache is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'processPendingGlyphs': (
          ('_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'eightBitFormatIsAlphaSwizzled': (
          ('_ZNK26QSGDistanceFieldGlyphCache29eightBitFormatIsAlphaSwizzled'
           'Ev',
           ('bool', 'number', ''),
           ()),
      ),
      'screenSpaceDerivativesSupported': (
          ('_ZNK26QSGDistanceFieldGlyphCache31screenSpaceDerivativesSupport'
           'edEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isActive': (
          ('_ZNK26QSGDistanceFieldGlyphCache8isActiveEv',
           ('bool', 'number', ''),
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

  def referenceFont(self) -> QRawFont:
    """
    Calls Qt's 'const QRawFont &QSGDistanceFieldGlyphCache::referenceFont()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#referenceFont

    Returns
    -------

    QRawFont
      A new cute QRawFont around the copy Qt gave back. Python owns it.
    """
    #  const QRawFont &QSGDistanceFieldGlyphCache::referenceFont() const
    address = self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache13referenceFontEv',
    )
    from ..QtGui import QRawFont
    return QRawFont._cuteOwning(address)

  @overload(float)
  def fontScale(self, pixelSize: float) -> float:
    """
    Calls Qt's 'qreal QSGDistanceFieldGlyphCache::fontScale(qreal pixelSize)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#fontScale

    Parameters
    ----------

    pixelSize : float
      Passed on as it is.
    """
    #  qreal QSGDistanceFieldGlyphCache::fontScale(qreal pixelSize) const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache9fontScaleEd', pixelSize,
    )

  def distanceFieldRadius(self) -> float:
    """
    Calls Qt's 'qreal QSGDistanceFieldGlyphCache::distanceFieldRadius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html
    """
    #  qreal QSGDistanceFieldGlyphCache::distanceFieldRadius() const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache19distanceFieldRadiusEv',
    )

  def glyphCount(self) -> int:
    """
    Calls Qt's 'int QSGDistanceFieldGlyphCache::glyphCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#glyphCount
    """
    #  int QSGDistanceFieldGlyphCache::glyphCount() const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache10glyphCountEv',
    )

  def doubleGlyphResolution(self) -> bool:
    """
    Calls Qt's 'bool QSGDistanceFieldGlyphCache::doubleGlyphResolution()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html
    """
    #  bool QSGDistanceFieldGlyphCache::doubleGlyphResolution() const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache21doubleGlyphResolutionEv',
    )

  def renderTypeQuality(self) -> int:
    """
    Calls Qt's 'int QSGDistanceFieldGlyphCache::renderTypeQuality() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#renderTypeQuality
    """
    #  int QSGDistanceFieldGlyphCache::renderTypeQuality() const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache17renderTypeQualityEv',
    )

  def eightBitFormatIsAlphaSwizzled(self) -> bool:
    """
    Calls Qt's 'bool
    QSGDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html
    """
    #  bool QSGDistanceFieldGlyphCache::eightBitFormatIsAlphaSwizzled() const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache29eightBitFormatIsAlphaSwizz'
        'ledEv',
    )

  def screenSpaceDerivativesSupported(self) -> bool:
    """
    Calls Qt's 'bool
    QSGDistanceFieldGlyphCache::screenSpaceDerivativesSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html
    """
    #  bool QSGDistanceFieldGlyphCache::screenSpaceDerivativesSupported()
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache31screenSpaceDerivativesSupp'
        'ortedEv',
    )

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSGDistanceFieldGlyphCache::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#isActive
    """
    #  bool QSGDistanceFieldGlyphCache::isActive() const
    ritual = 'ritual_ZNK26QSGDistanceFieldGlyphCache8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QSGDistanceFieldGlyphCache8isActiveEv'
    return self.uglySide.call(ritual)

  def baseFontSize(self) -> int:
    """
    Calls Qt's 'int QSGDistanceFieldGlyphCache::baseFontSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#baseFontSize
    """
    #  int QSGDistanceFieldGlyphCache::baseFontSize() const
    return self.uglySide.call(
        'ritual_ZNK26QSGDistanceFieldGlyphCache12baseFontSizeEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGDistanceFieldGlyphCache::QSGDistanceFieldGlyphCache(const
    QRawFont &font, int renderTypeQuality)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.__init__' has no cute function yet. "
        "Qt's 'QSGDistanceFieldGlyphCache::QSGDistanceFieldGlyphCache(const "
        "QRawFont &font, int renderTypeQuality)': the class is abstract, so "
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

  @overload(int, float)
  def glyphMetrics(self, glyph: int, pixelSize: float) -> Metrics:
    """
    Calls Qt's 'Metrics QSGDistanceFieldGlyphCache::glyphMetrics(glyph_t
    glyph, qreal pixelSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#glyphMetrics

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    pixelSize : float
      Passed on as it is.

    Returns
    -------

    Metrics
      A new cute QSGDistanceFieldGlyphCache::Metrics around the copy Qt gave
      back. Python owns it.
    """
    #  Metrics QSGDistanceFieldGlyphCache::glyphMetrics(glyph_t glyph, qreal
    #      pixelSize)
    address = self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache12glyphMetricsEjd',
        glyph, pixelSize,
    )
    return QSGDistanceFieldGlyphCache.Metrics._cuteOwning(address)

  @overload(int)
  def glyphTexCoord(self, glyph: int) -> TexCoord:
    """
    Calls Qt's 'TexCoord QSGDistanceFieldGlyphCache::glyphTexCoord(glyph_t
    glyph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#glyphTexCoord

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    Returns
    -------

    TexCoord
      A new cute QSGDistanceFieldGlyphCache::TexCoord around the copy Qt gave
      back. Python owns it.
    """
    #  TexCoord QSGDistanceFieldGlyphCache::glyphTexCoord(glyph_t glyph)
    address = self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache13glyphTexCoordEj', glyph,
    )
    return QSGDistanceFieldGlyphCache.TexCoord._cuteOwning(address)

  @overload(int)
  def glyphTexture(self, glyph: int) -> Optional[Texture]:
    """
    Calls Qt's 'const Texture
    *QSGDistanceFieldGlyphCache::glyphTexture(glyph_t glyph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#glyphTexture

    Parameters
    ----------

    glyph : int
      Passed on as it is.

    Returns
    -------

    Optional[Texture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Texture *QSGDistanceFieldGlyphCache::glyphTexture(glyph_t glyph)
    address = self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache12glyphTextureEj', glyph,
    )
    return QSGDistanceFieldGlyphCache.Texture._cuteAt(address)

  def update(self) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphCache::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#update
    """
    #  void QSGDistanceFieldGlyphCache::update()
    self.uglySide.call('ritual_ZN26QSGDistanceFieldGlyphCache6updateEv')

  @overload(QSGDistanceFieldGlyphConsumer)
  @overload(NoneType)
  def registerGlyphNode(
      self,
      node: Optional[QSGDistanceFieldGlyphConsumer],
  ) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphCache::registerGlyphNode(
    QSGDistanceFieldGlyphConsumer *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#registerGlyphNode

    Parameters
    ----------

    node : Optional[QSGDistanceFieldGlyphConsumer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDistanceFieldGlyphCache::registerGlyphNode(
    #      QSGDistanceFieldGlyphConsumer *node)
    self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache17registerGlyphNodeEP29QSGDis'
        'tanceFieldGlyphConsumer',
        self._addressOf(node, 'QSGDistanceFieldGlyphConsumer'),
    )

  @overload(QSGDistanceFieldGlyphConsumer)
  @overload(NoneType)
  def unregisterGlyphNode(
      self,
      node: Optional[QSGDistanceFieldGlyphConsumer],
  ) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphCache::unregisterGlyphNode(
    QSGDistanceFieldGlyphConsumer *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html

    Parameters
    ----------

    node : Optional[QSGDistanceFieldGlyphConsumer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDistanceFieldGlyphCache::unregisterGlyphNode(
    #      QSGDistanceFieldGlyphConsumer *node)
    self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache19unregisterGlyphNodeEP29QSGD'
        'istanceFieldGlyphConsumer',
        self._addressOf(node, 'QSGDistanceFieldGlyphConsumer'),
    )

  def processPendingGlyphs(self) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphCache::processPendingGlyphs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html
    """
    #  void QSGDistanceFieldGlyphCache::processPendingGlyphs()
    ritual = 'ritual_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QSGDistanceFieldGlyphCache20processPendingGlyphsE'
          'v')
    self.uglySide.call(ritual)

  @overload(QList[QDistanceField])
  def storeGlyphs(self, glyphs: QList[QDistanceField]) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphCache::storeGlyphs(const
    QList<QDistanceField> &glyphs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#storeGlyphs

    Parameters
    ----------

    glyphs : QList[QDistanceField]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QSGDistanceFieldGlyphCache::storeGlyphs(const
    #      QList<QDistanceField> &glyphs)
    self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache11storeGlyphsERK5QListI14QDis'
        'tanceFieldE',
        self._valueOf(glyphs),
    )

  @overload(int)
  def removeGlyph(self, glyph: int) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphCache::removeGlyph(glyph_t glyph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#removeGlyph

    Parameters
    ----------

    glyph : int
      Passed on as it is.
    """
    #  void QSGDistanceFieldGlyphCache::removeGlyph(glyph_t glyph)
    self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache11removeGlyphEj', glyph,
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
    Calls Qt's 'void QSGDistanceFieldGlyphCache::updateRhiTexture(QRhiTexture
    *oldTex, QRhiTexture *newTex, const QSize &newTexSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#updateRhiTexture

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
    #  void QSGDistanceFieldGlyphCache::updateRhiTexture(QRhiTexture *oldTex,
    #      QRhiTexture *newTex, const QSize &newTexSize)
    self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache16updateRhiTextureEP11QRhiTex'
        'tureS1_RK5QSize',
        self._addressOf(oldTex), self._addressOf(newTex),
        self._valueOf(newTexSize),
    )

  @overload(int)
  def containsGlyph(self, glyph: int) -> bool:
    """
    Calls Qt's 'bool QSGDistanceFieldGlyphCache::containsGlyph(glyph_t
    glyph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphcache.html#containsGlyph

    Parameters
    ----------

    glyph : int
      Passed on as it is.
    """
    #  bool QSGDistanceFieldGlyphCache::containsGlyph(glyph_t glyph)
    return self.uglySide.call(
        'ritual_ZN26QSGDistanceFieldGlyphCache13containsGlyphEj', glyph,
    )

  @staticmethod
  def emptyData(*__, **_) -> Never:
    """
    Qt's 'GlyphData &QSGDistanceFieldGlyphCache::emptyData(glyph_t glyph)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.emptyData' has no cute function yet. "
        "Qt's 'GlyphData &QSGDistanceFieldGlyphCache::emptyData(glyph_t "
        "glyph)': gives a type Python has no way to take yet.")

  @staticmethod
  def glyphData(*__, **_) -> Never:
    """
    Qt's 'GlyphData &QSGDistanceFieldGlyphCache::glyphData(glyph_t glyph)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.glyphData' has no cute function yet. "
        "Qt's 'GlyphData &QSGDistanceFieldGlyphCache::glyphData(glyph_t "
        "glyph)': gives a type Python has no way to take yet.")

  @staticmethod
  def markGlyphsToRender(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::markGlyphsToRender(const
    QList<glyph_t> &glyphs)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.markGlyphsToRender' has no cute "
        "function yet. Qt's 'void "
        "QSGDistanceFieldGlyphCache::markGlyphsToRender(const "
        "QList<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::populate(const QList<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.populate' has no cute function yet. "
        "Qt's 'void QSGDistanceFieldGlyphCache::populate(const "
        "QList<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def referenceGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::referenceGlyphs(const
    QSet<glyph_t> &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.referenceGlyphs' has no cute function "
        "yet. Qt's 'void QSGDistanceFieldGlyphCache::referenceGlyphs(const "
        "QSet<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::release(const QList<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.release' has no cute function yet. "
        "Qt's 'void QSGDistanceFieldGlyphCache::release(const "
        "QList<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def releaseGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::releaseGlyphs(const QSet<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.releaseGlyphs' has no cute function "
        "yet. Qt's 'void QSGDistanceFieldGlyphCache::releaseGlyphs(const "
        "QSet<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def requestGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::requestGlyphs(const QSet<glyph_t>
    &glyphs)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.requestGlyphs' has no cute function "
        "yet. Qt's 'void QSGDistanceFieldGlyphCache::requestGlyphs(const "
        "QSet<glyph_t> &glyphs)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setGlyphsPosition(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::setGlyphsPosition(const
    QList<GlyphPosition> &glyphs)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.setGlyphsPosition' has no cute "
        "function yet. Qt's 'void "
        "QSGDistanceFieldGlyphCache::setGlyphsPosition(const "
        "QList<GlyphPosition> &glyphs)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setGlyphsTexture(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphCache::setGlyphsTexture(const
    QList<glyph_t> &glyphs, const Texture &tex)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphCache.setGlyphsTexture' has no cute function "
        "yet. Qt's 'void QSGDistanceFieldGlyphCache::setGlyphsTexture(const "
        "QList<glyph_t> &glyphs, const Texture &tex)': takes a type Python "
        "has no way to hand over yet.")
