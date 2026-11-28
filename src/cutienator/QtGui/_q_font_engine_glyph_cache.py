"""
QFontEngineGlyphCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontengineglyphcache_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFontEngineGlyphCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QFontEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QColor, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QTransform = WAIT['QTransform']


class QFontEngineGlyphCache(QSharedData):
  """
  The cute side of Qt's QFontEngineGlyphCache: a plain Python object standing
  in front of one C++ QFontEngineGlyphCache.

  It is built on the cute 'QSharedData', as Qt's QFontEngineGlyphCache is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QFontEngineGlyphCache around as a copy, so every C++
  QFontEngineGlyphCache behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontEngineGlyphCache that has a ritual and that
  Python can call so far, 3 names in all: 'glyphFormat', 'transform',
  'color'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontEngineGlyphCache::~QFontEngineGlyphCache()': the destructor:
    Python removes its C++ QFontEngineGlyphCache by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QFontEngineGlyphCache is created at the first use, not by
    'QFontEngineGlyphCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontEngineGlyphCache back gives a copy the ritual
    made for Python, in a new cute QFontEngineGlyphCache.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontEngineGlyphCache'

  #  Qt's '~QFontEngineGlyphCache()'. Naming it makes this a value class:
  #  Python owns every C++ QFontEngineGlyphCache behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QFontEngineGlyphCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def glyphFormat(self) -> QFontEngine.GlyphFormat:
    """
    Calls Qt's 'QFontEngine::GlyphFormat QFontEngineGlyphCache::glyphFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengineglyphcache.html#glyphFormat

    Returns
    -------

    QFontEngine.GlyphFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFontEngine.GlyphFormat(number)' gives.
    """
    #  QFontEngine::GlyphFormat QFontEngineGlyphCache::glyphFormat() const
    return QFontEngine.GlyphFormat(self.uglySide.call(
        'ritual_ZNK21QFontEngineGlyphCache11glyphFormatEv',
    ))

  def transform(self) -> QTransform:
    """
    Calls Qt's 'const QTransform &QFontEngineGlyphCache::transform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengineglyphcache.html#transform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  const QTransform &QFontEngineGlyphCache::transform() const
    address = self.uglySide.call(
        'ritual_ZNK21QFontEngineGlyphCache9transformEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'const QColor &QFontEngineGlyphCache::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontengineglyphcache.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QFontEngineGlyphCache::color() const
    address = self.uglySide.call('ritual_ZNK21QFontEngineGlyphCache5colorEv')
    from . import QColor
    return QColor._cuteOwning(address)

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
    'QFontEngineGlyphCache::QFontEngineGlyphCache(QFontEngine::GlyphFormat
    format, const QTransform &matrix, const QColor &color)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontengineglyphcache.html#QFontEngineGlyphCache

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
    #  QFontEngineGlyphCache::QFontEngineGlyphCache(QFontEngine::GlyphFormat
    #      format, const QTransform &matrix, const QColor &color)
    if color is None:
      from . import QColor
      color = QColor()
    self._noteCreation(QFontEngineGlyphCache, lambda: Rituals.call(
        'ritual_ZN21QFontEngineGlyphCacheC1EN11QFontEngine11GlyphFormatERK1'
        '0QTransformRK6QColor',
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
