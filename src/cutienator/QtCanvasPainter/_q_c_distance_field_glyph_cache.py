"""
QCDistanceFieldGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCDistanceFieldGlyphCache to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRawFont, QRhiResourceUpdateBatch, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRawFont = WAIT['QRawFont']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCDistanceFieldGlyphCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCDistanceFieldGlyphCache: a plain Python object
  standing in front of one C++ QCDistanceFieldGlyphCache.

  What exists
  -----------

  Every function of Qt's QCDistanceFieldGlyphCache that has a ritual and that
  Python can call so far, 9 names in all: 'commitResourceUpdates',
  'getCurrentTextures', 'getOldTextures', 'setOldTexture',
  'optimizeCacheAfterRendering', 'colorGlyphTexture',
  'prevColorGlyphTexture', 'setPrevColorGlyphTexture', 'fontKeyDataFor'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCDistanceFieldGlyphCache::~QCDistanceFieldGlyphCache()': the
    destructor: Python never removes a C++ QCDistanceFieldGlyphCache.
  - Qt's 'const QCRhiDistanceFieldGlyphCache::VertexList
    &QCDistanceFieldGlyphCache::colorVertices() const': gives a type Python
    has no way to take yet.
  - Qt's 'const QCRhiDistanceFieldGlyphCache::IndexList
    &QCDistanceFieldGlyphCache::colorIndices() const': gives a type Python
    has no way to take yet.
  - Qt's 'bool operator==(const FontKey &f1, const FontKey &f2)': an operator
    between other classes, written inside this one.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 leans on 'QCRhiColorGlyphCache; 1
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QCDistanceFieldGlyphCache is created at the first use, not by
    'QCDistanceFieldGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCDistanceFieldGlyphCache.
  - Each name of Qt's QCDistanceFieldGlyphCache that has no cute function
    yet, '__init__', 'colorIndices', 'colorVertices', 'generate',
    'generateFromShapedText', 'generateGlyphRuns', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QCDistanceFieldGlyphCache, each a class in
  #  here as in C++.

  class FontKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCDistanceFieldGlyphCache::FontKey: a plain Python
    object standing in front of one C++ QCDistanceFieldGlyphCache::FontKey.

    C++ hands a QCDistanceFieldGlyphCache::FontKey around as a copy, so every
    C++ QCDistanceFieldGlyphCache::FontKey behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QCDistanceFieldGlyphCache::FontKey yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCDistanceFieldGlyphCache::FontKey::~FontKey()': the destructor:
      Python removes its C++ QCDistanceFieldGlyphCache::FontKey by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QCDistanceFieldGlyphCache::FontKey is created at the first use,
      not by 'QCDistanceFieldGlyphCache::FontKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCDistanceFieldGlyphCache::FontKey back gives a
      copy the ritual made for Python, in a new cute
      QCDistanceFieldGlyphCache::FontKey.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRawFont = WAIT['QRawFont']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCDistanceFieldGlyphCache::FontKey'

    #  Qt's '~QCDistanceFieldGlyphCache::FontKey()'. Naming it makes this a
    #  value class: Python owns every C++ QCDistanceFieldGlyphCache::FontKey
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QCDistanceFieldGlyphCache7FontKeyD1Ev'

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

    @overload(QRawFont)
    def __init__(self, font: QRawFont) -> None:
      """
      Notes what was given, for Qt's
      'QCDistanceFieldGlyphCache::FontKey::FontKey(const QRawFont &font)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcdistancefieldglyphcache-fontkey.html#FontKey

      Parameters
      ----------

      font : QRawFont
        Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
        own.
      """
      #  QCDistanceFieldGlyphCache::FontKey::FontKey(const QRawFont &font)
      self._noteCreation(
          QCDistanceFieldGlyphCache.FontKey, lambda: Rituals.call(
              'ritual_ZN25QCDistanceFieldGlyphCache7FontKeyC1ERK8QRawFont',
              self._valueOf(font),
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

  class FontKeyData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCDistanceFieldGlyphCache::FontKeyData: a plain
    Python object standing in front of one C++
    QCDistanceFieldGlyphCache::FontKeyData.

    What exists
    -----------

    No function of Qt's QCDistanceFieldGlyphCache::FontKeyData yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What to expect
    --------------

    - The C++ QCDistanceFieldGlyphCache::FontKeyData is created at the first
      use, not by 'QCDistanceFieldGlyphCache::FontKeyData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QCDistanceFieldGlyphCache::FontKeyData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCDistanceFieldGlyphCache::FontKeyData'

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

  class GlyphCacheKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCDistanceFieldGlyphCache::GlyphCacheKey: a plain
    Python object standing in front of one C++
    QCDistanceFieldGlyphCache::GlyphCacheKey.

    C++ hands a QCDistanceFieldGlyphCache::GlyphCacheKey around as a copy, so
    every C++ QCDistanceFieldGlyphCache::GlyphCacheKey behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QCDistanceFieldGlyphCache::GlyphCacheKey yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCDistanceFieldGlyphCache::GlyphCacheKey::~GlyphCacheKey()': the
      destructor: Python removes its C++
      QCDistanceFieldGlyphCache::GlyphCacheKey by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCDistanceFieldGlyphCache::GlyphCacheKey is created at the
      first use, not by 'QCDistanceFieldGlyphCache::GlyphCacheKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCDistanceFieldGlyphCache::GlyphCacheKey back gives
      a copy the ritual made for Python, in a new cute
      QCDistanceFieldGlyphCache::GlyphCacheKey.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCDistanceFieldGlyphCache::GlyphCacheKey'

    #  Qt's '~QCDistanceFieldGlyphCache::GlyphCacheKey()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCDistanceFieldGlyphCache::GlyphCacheKey behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QCDistanceFieldGlyphCache13GlyphCacheKeyD1Ev')

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

  class GlyphCacheValue(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCDistanceFieldGlyphCache::GlyphCacheValue: a plain
    Python object standing in front of one C++
    QCDistanceFieldGlyphCache::GlyphCacheValue.

    C++ hands a QCDistanceFieldGlyphCache::GlyphCacheValue around as a copy,
    so every C++ QCDistanceFieldGlyphCache::GlyphCacheValue behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QCDistanceFieldGlyphCache::GlyphCacheValue yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCDistanceFieldGlyphCache::GlyphCacheValue::~GlyphCacheValue()':
      the destructor: Python removes its C++
      QCDistanceFieldGlyphCache::GlyphCacheValue by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QCDistanceFieldGlyphCache::GlyphCacheValue is created at the
      first use, not by 'QCDistanceFieldGlyphCache::GlyphCacheValue(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCDistanceFieldGlyphCache::GlyphCacheValue back
      gives a copy the ritual made for Python, in a new cute
      QCDistanceFieldGlyphCache::GlyphCacheValue.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCDistanceFieldGlyphCache::GlyphCacheValue'

    #  Qt's '~QCDistanceFieldGlyphCache::GlyphCacheValue()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QCDistanceFieldGlyphCache::GlyphCacheValue behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QCDistanceFieldGlyphCache15GlyphCacheValueD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCDistanceFieldGlyphCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FontKeyData)
  @overload(NoneType)
  def getCurrentTextures(
      self,
      data: Optional[FontKeyData],
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QCDistanceFieldGlyphCache::getCurrentTextures(const FontKeyData *data)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html#getCurrentTextures

    Parameters
    ----------

    data : Optional[FontKeyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QCDistanceFieldGlyphCache::getCurrentTextures(const
    #      FontKeyData *data) const
    address = self.uglySide.call(
        'ritual_ZNK25QCDistanceFieldGlyphCache18getCurrentTexturesEPKNS_11F'
        'ontKeyDataE',
        self._addressOf(data),
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  @overload(FontKeyData)
  @overload(NoneType)
  def getOldTextures(
      self,
      data: Optional[FontKeyData],
  ) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QCDistanceFieldGlyphCache::getOldTextures(const
    FontKeyData *data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html#getOldTextures

    Parameters
    ----------

    data : Optional[FontKeyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QCDistanceFieldGlyphCache::getOldTextures(const
    #      FontKeyData *data) const
    address = self.uglySide.call(
        'ritual_ZNK25QCDistanceFieldGlyphCache14getOldTexturesEPKNS_11FontK'
        'eyDataE',
        self._addressOf(data),
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def colorGlyphTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QCDistanceFieldGlyphCache::colorGlyphTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html#colorGlyphTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QCDistanceFieldGlyphCache::colorGlyphTexture() const
    address = self.uglySide.call(
        'ritual_ZNK25QCDistanceFieldGlyphCache17colorGlyphTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def prevColorGlyphTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QCDistanceFieldGlyphCache::prevColorGlyphTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QCDistanceFieldGlyphCache::prevColorGlyphTexture() const
    address = self.uglySide.call(
        'ritual_ZNK25QCDistanceFieldGlyphCache21prevColorGlyphTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FontKeyData, QRhiTexture)
  @overload(FontKeyData, NoneType)
  @overload(NoneType, QRhiTexture)
  @overload(NoneType, NoneType)
  def setOldTexture(
      self,
      data: Optional[FontKeyData],
      tex: Optional[QRhiTexture],
  ) -> None:
    """
    Calls Qt's 'void QCDistanceFieldGlyphCache::setOldTexture(FontKeyData
    *data, QRhiTexture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html#setOldTexture

    Parameters
    ----------

    data : Optional[FontKeyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCDistanceFieldGlyphCache::setOldTexture(FontKeyData *data,
    #      QRhiTexture *tex)
    self.uglySide.call(
        'ritual_ZN25QCDistanceFieldGlyphCache13setOldTextureEPNS_11FontKeyD'
        'ataEP11QRhiTexture',
        self._addressOf(data), self._addressOf(tex),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setPrevColorGlyphTexture(self, tex: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void
    QCDistanceFieldGlyphCache::setPrevColorGlyphTexture(QRhiTexture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCDistanceFieldGlyphCache::setPrevColorGlyphTexture(QRhiTexture
    #      *tex)
    self.uglySide.call(
        'ritual_ZN25QCDistanceFieldGlyphCache24setPrevColorGlyphTextureEP11'
        'QRhiTexture',
        self._addressOf(tex),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QCDistanceFieldGlyphCache::QCDistanceFieldGlyphCache(QRhi *rhi)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QCDistanceFieldGlyphCache.__init__' has no cute function yet. "
        "Qt's 'QCDistanceFieldGlyphCache::QCDistanceFieldGlyphCache(QRhi "
        "*rhi)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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

  @overload(QRhiResourceUpdateBatch, FontKeyData)
  @overload(QRhiResourceUpdateBatch, NoneType)
  @overload(NoneType, FontKeyData)
  @overload(NoneType, NoneType)
  def commitResourceUpdates(
      self,
      batch: Optional[QRhiResourceUpdateBatch],
      data: Optional[FontKeyData],
  ) -> None:
    """
    Calls Qt's 'void
    QCDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatch
    *batch, FontKeyData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html

    Parameters
    ----------

    batch : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[FontKeyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCDistanceFieldGlyphCache::commitResourceUpdates(
    #      QRhiResourceUpdateBatch *batch, FontKeyData *data)
    self.uglySide.call(
        'ritual_ZN25QCDistanceFieldGlyphCache21commitResourceUpdatesEP23QRh'
        'iResourceUpdateBatchPNS_11FontKeyDataE',
        self._addressOf(batch), self._addressOf(data),
    )

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def commitResourceUpdates(
      self,
      batch: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void
    QCDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatch
    *batch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html

    Parameters
    ----------

    batch : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCDistanceFieldGlyphCache::commitResourceUpdates(
    #      QRhiResourceUpdateBatch *batch)
    self.uglySide.call(
        'ritual_ZN25QCDistanceFieldGlyphCache21commitResourceUpdatesEP23QRh'
        'iResourceUpdateBatch',
        self._addressOf(batch),
    )

  def optimizeCacheAfterRendering(self) -> None:
    """
    Calls Qt's 'void
    QCDistanceFieldGlyphCache::optimizeCacheAfterRendering()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html
    """
    #  void QCDistanceFieldGlyphCache::optimizeCacheAfterRendering()
    self.uglySide.call(
        'ritual_ZN25QCDistanceFieldGlyphCache27optimizeCacheAfterRenderingE'
        'v',
    )

  @overload(QRawFont)
  def fontKeyDataFor(self, rFont: QRawFont) -> Optional[FontKeyData]:
    """
    Calls Qt's 'FontKeyData *QCDistanceFieldGlyphCache::fontKeyDataFor(const
    QRawFont &rFont)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcdistancefieldglyphcache.html#fontKeyDataFor

    Parameters
    ----------

    rFont : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.

    Returns
    -------

    Optional[FontKeyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FontKeyData *QCDistanceFieldGlyphCache::fontKeyDataFor(const QRawFont
    #      &rFont)
    address = self.uglySide.call(
        'ritual_ZN25QCDistanceFieldGlyphCache14fontKeyDataForERK8QRawFont',
        self._valueOf(rFont),
    )
    return QCDistanceFieldGlyphCache.FontKeyData._cuteAt(address)

  @staticmethod
  def colorIndices(*__, **_) -> Never:
    """
    Qt's 'const QCRhiDistanceFieldGlyphCache::IndexList
    &QCDistanceFieldGlyphCache::colorIndices() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QCDistanceFieldGlyphCache.colorIndices' has no cute function yet. "
        "Qt's 'const QCRhiDistanceFieldGlyphCache::IndexList "
        "&QCDistanceFieldGlyphCache::colorIndices() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def colorVertices(*__, **_) -> Never:
    """
    Qt's 'const QCRhiDistanceFieldGlyphCache::VertexList
    &QCDistanceFieldGlyphCache::colorVertices() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QCDistanceFieldGlyphCache.colorVertices' has no cute function "
        "yet. Qt's 'const QCRhiDistanceFieldGlyphCache::VertexList "
        "&QCDistanceFieldGlyphCache::colorVertices() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def generate(*__, **_) -> Never:
    """
    Qt's 'FontKeyData *QCDistanceFieldGlyphCache::generate(const QString
    &text, const QRectF &rect, const QFont &font, QCState *state,
    QCanvasPainter::TextAlign alignment, float devicePixelRatio,
    QCRhiDistanceFieldGlyphCache::VertexList *verts,
    QCRhiDistanceFieldGlyphCache::IndexList *indices)': leans on
    'QCRhiColorGlyphCache::ensureGlyph(QCRhiColorGlyphCache::GlyphKey const&,
    QFontEngine*, QColor, QTransform const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCDistanceFieldGlyphCache.generate' has no cute function yet. "
        "Qt's 'FontKeyData *QCDistanceFieldGlyphCache::generate(const "
        "QString &text, const QRectF &rect, const QFont &font, QCState "
        "*state, QCanvasPainter::TextAlign alignment, float "
        "devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts, "
        "QCRhiDistanceFieldGlyphCache::IndexList *indices)': leans on "
        "'QCRhiColorGlyphCache::ensureGlyph(QCRhiColorGlyphCache::GlyphKey "
        "const&, QFontEngine*, QColor, QTransform const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def generateFromShapedText(*__, **_) -> Never:
    """
    Qt's 'FontKeyData
    *QCDistanceFieldGlyphCache::generateFromShapedText(QFontEngine
    *fontEngine, const quint32 *glyphIndexes, const QFixedPoint
    *glyphPositions, int glyphCount, const QCState &state, float
    devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts,
    QCRhiDistanceFieldGlyphCache::IndexList *indices)': leans on
    'QCRhiColorGlyphCache::ensureGlyph(QCRhiColorGlyphCache::GlyphKey const&,
    QFontEngine*, QColor, QTransform const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCDistanceFieldGlyphCache.generateFromShapedText' has no cute "
        "function yet. Qt's 'FontKeyData "
        "*QCDistanceFieldGlyphCache::generateFromShapedText(QFontEngine "
        "*fontEngine, const quint32 *glyphIndexes, const QFixedPoint "
        "*glyphPositions, int glyphCount, const QCState &state, float "
        "devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts, "
        "QCRhiDistanceFieldGlyphCache::IndexList *indices)': leans on "
        "'QCRhiColorGlyphCache::ensureGlyph(QCRhiColorGlyphCache::GlyphKey "
        "const&, QFontEngine*, QColor, QTransform const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def generateGlyphRuns(*__, **_) -> Never:
    """
    Qt's 'QList<QGlyphRun> QCDistanceFieldGlyphCache::generateGlyphRuns(const
    QString &text, const QRectF &rect, const QFont &font, const QFontMetricsF
    &metrics, QCState *state, QCanvasPainter::TextAlign alignment)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QCTextLayout'; did you
    mean 'QTextLayout'?.
    """
    raise NotImplementedError(
        "'QCDistanceFieldGlyphCache.generateGlyphRuns' has no cute function "
        "yet. Qt's 'QList<QGlyphRun> "
        "QCDistanceFieldGlyphCache::generateGlyphRuns(const QString &text, "
        "const QRectF &rect, const QFont &font, const QFontMetricsF "
        "&metrics, QCState *state, QCanvasPainter::TextAlign alignment)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QCTextLayout'; did you mean 'QTextLayout'?.")
