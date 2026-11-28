"""
QBlittable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qblittable_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QBlittable to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QFontEngine, QPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF, QSize
  from . import QColor, QImage, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPixmap = WAIT['QPixmap']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']


class QBlittable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBlittable: a plain Python object standing in front
  of one C++ QBlittable.

  What exists
  -----------

  Every function of Qt's QBlittable that has a ritual and that Python can
  call so far, 11 names in all: 'capabilities', 'size', 'fillRect',
  'drawPixmap', 'alphaFillRect', 'drawPixmapOpacity', 'lock', 'unlock',
  'isLocked', 'doLock', 'doUnlock'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBlittablePrivate *QBlittable::d_func()': gives
    'QBlittablePrivate', which has no cute class yet.
  - Qt's 'const QBlittablePrivate *QBlittable::d_func() const': gives
    'QBlittablePrivate', which has no cute class yet.
  - Qt's 'QBlittable::~QBlittable()': the destructor: Python never removes a
    C++ QBlittable.
  - Qt's 'bool QBlittable::drawCachedGlyphs(const QPaintEngineState *state,
    QFontEngine::GlyphFormat glyphFormat, int numGlyphs, const glyph_t
    *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)': names
    'glyph_t', which has no cute class yet.

  What to expect
  --------------

  - The C++ QBlittable is created at the first use, not by 'QBlittable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBlittable.
  - Each name of Qt's QBlittable that has no cute function yet, 'd_func',
    'drawCachedGlyphs', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QBlittable, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Capability(CuteFlags):
    """
    The flags enum 'QBlittable::Capability' of Qt, with the 10 names Qt gives
    in it. Qt names the type of its combinations 'QBlittable::Capabilities'.
    """

    SolidRectCapability = 0x1
    SourcePixmapCapability = 0x2
    SourceOverPixmapCapability = 0x4
    SourceOverScaledPixmapCapability = 0x8
    AlphaFillRectCapability = 0x10
    OpacityPixmapCapability = 0x20
    DrawScaledCachedGlyphsCapability = 0x40
    SubPixelGlyphsCapability = 0x80
    ComplexClipCapability = 0x100
    OutlineCapability = 0x1000

  Capabilities = Capability

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBlittable'

  #  A C++ QBlittable Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBlittable'

  #  The functions Qt calls itself that QBlittable is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'drawCachedGlyphs': (
          'bool QBlittable::drawCachedGlyphs(const QPaintEngineState *, '
          'QFontEngine::GlyphFormat, int, const glyph_t *, const '
          'QFixedPoint *, QFontEngine *)',
      ),
  }

  #  The functions Qt calls itself that QBlittable is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'fillRect': (
          ('_ZN10QBlittable8fillRectERK6QRectFRK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'drawPixmap': (
          ('_ZN10QBlittable10drawPixmapERK6QRectFRK7QPixmapS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'alphaFillRect': (
          ('_ZN10QBlittable13alphaFillRectERK6QRectFRK6QColorN8QPainter15Co'
           'mpositionModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QColor'),
               ('int', 'enum', 'QtGui:QPainter.CompositionMode'),
           )),
      ),
      'drawPixmapOpacity': (
          ('_ZN10QBlittable17drawPixmapOpacityERK6QRectFRK7QPixmapS2_N8QPai'
           'nter15CompositionModeEd',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QPixmap'),
               ('address', 'value', 'QtCore:QRectF'),
               ('int', 'enum', 'QtGui:QPainter.CompositionMode'),
               ('double', 'number', ''),
           )),
      ),
      'doLock': (
          ('_ZN10QBlittable6doLockEv',
           ('address', 'address', 'QtGui:QImage'),
           ()),
      ),
      'doUnlock': (
          ('_ZN10QBlittable8doUnlockEv',
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

  def capabilities(self) -> Capabilities:
    """
    Calls Qt's 'Capabilities QBlittable::capabilities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#capabilities

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QBlittable::capabilities() const
    return QBlittable.Capabilities(self.uglySide.call(
        'ritual_ZNK10QBlittable12capabilitiesEv',
    ))

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QBlittable::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QBlittable::size() const
    address = self.uglySide.call('ritual_ZNK10QBlittable4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isLocked(self) -> bool:
    """
    Calls Qt's 'bool QBlittable::isLocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#isLocked
    """
    #  bool QBlittable::isLocked() const
    return self.uglySide.call('ritual_ZNK10QBlittable8isLockedEv')

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

  @overload(QSize, Capabilities)
  def __init__(self, size: QSize, caps: Capabilities) -> None:
    """
    Notes what was given, for Qt's 'QBlittable::QBlittable(const QSize &size,
    Capabilities caps)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#QBlittable

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    caps : Capabilities
      Passed on as its number.
    """
    #  QBlittable::QBlittable(const QSize &size, Capabilities caps)
    self._noteCreation(QBlittable, lambda: Rituals.call(
        'ritual_ZN10QBlittableC1ERK5QSize6QFlagsINS_10CapabilityEE',
        self._valueOf(size), caps.value,
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

  @overload(QRectF, QColor)
  def fillRect(self, rect: QRectF, color: QColor) -> None:
    """
    Calls Qt's 'void QBlittable::fillRect(const QRectF &rect, const QColor
    &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QBlittable::fillRect(const QRectF &rect, const QColor &color)
    self.uglySide.call(
        'ritual_ZN10QBlittable8fillRectERK6QRectFRK6QColor',
        self._valueOf(rect), self._valueOf(color),
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(
      self,
      rect: QRectF,
      pixmap: QPixmap,
      subrect: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QBlittable::drawPixmap(const QRectF &rect, const QPixmap
    &pixmap, const QRectF &subrect)'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#drawPixmap

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    subrect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QBlittable::drawPixmap(const QRectF &rect, const QPixmap &pixmap,
    #      const QRectF &subrect)
    self.uglySide.call(
        'ritual_ZN10QBlittable10drawPixmapERK6QRectFRK7QPixmapS2_',
        self._valueOf(rect), self._valueOf(pixmap), self._valueOf(subrect),
    )

  @overload(QRectF, QColor, QPainter.CompositionMode)
  def alphaFillRect(
      self,
      rect: QRectF,
      color: QColor,
      cmode: QPainter.CompositionMode,
  ) -> None:
    """
    Calls Qt's 'void QBlittable::alphaFillRect(const QRectF &rect, const
    QColor &color, QPainter::CompositionMode cmode)'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#alphaFillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    cmode : QPainter.CompositionMode
      Passed on as its number.
    """
    #  void QBlittable::alphaFillRect(const QRectF &rect, const QColor
    #      &color, QPainter::CompositionMode cmode)
    ritual = (
        'ritual_ZN10QBlittable13alphaFillRectERK6QRectFRK6QColorN8QPainter1'
        '5CompositionModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QBlittable13alphaFillRectERK6QRectFRK6QColorN8QPa'
          'inter15CompositionModeE')
    self.uglySide.call(
        ritual, self._valueOf(rect), self._valueOf(color), cmode.value,
    )

  @overload(QRectF, QPixmap, QRectF, QPainter.CompositionMode, float)
  def drawPixmapOpacity(
      self,
      rect: QRectF,
      pixmap: QPixmap,
      subrect: QRectF,
      cmode: QPainter.CompositionMode,
      opacity: float,
  ) -> None:
    """
    Calls Qt's 'void QBlittable::drawPixmapOpacity(const QRectF &rect, const
    QPixmap &pixmap, const QRectF &subrect, QPainter::CompositionMode cmode,
    qreal opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#drawPixmapOpacity

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    subrect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    cmode : QPainter.CompositionMode
      Passed on as its number.

    opacity : float
      Passed on as it is.
    """
    #  void QBlittable::drawPixmapOpacity(const QRectF &rect, const QPixmap
    #      &pixmap, const QRectF &subrect, QPainter::CompositionMode cmode,
    #      qreal opacity)
    ritual = (
        'ritual_ZN10QBlittable17drawPixmapOpacityERK6QRectFRK7QPixmapS2_N8Q'
        'Painter15CompositionModeEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QBlittable17drawPixmapOpacityERK6QRectFRK7QPixmap'
          'S2_N8QPainter15CompositionModeEd')
    self.uglySide.call(
        ritual,
        self._valueOf(rect), self._valueOf(pixmap), self._valueOf(subrect),
        cmode.value, opacity,
    )

  def lock(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage *QBlittable::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#lock

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QBlittable::lock()
    address = self.uglySide.call('ritual_ZN10QBlittable4lockEv')
    from . import QImage
    return QImage._cuteAt(address)

  def unlock(self) -> None:
    """
    Calls Qt's 'void QBlittable::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#unlock
    """
    #  void QBlittable::unlock()
    self.uglySide.call('ritual_ZN10QBlittable6unlockEv')

  def doLock(self) -> Optional[QImage]:
    """
    Calls Qt's 'QImage *QBlittable::doLock()'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#doLock

    Returns
    -------

    Optional[QImage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QImage *QBlittable::doLock()
    address = self.uglySide.call('ritual_ZN10QBlittable6doLockEv')
    from . import QImage
    return QImage._cuteAt(address)

  def doUnlock(self) -> None:
    """
    Calls Qt's 'void QBlittable::doUnlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qblittable.html#doUnlock
    """
    #  void QBlittable::doUnlock()
    self.uglySide.call('ritual_ZN10QBlittable8doUnlockEv')

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QBlittablePrivate *QBlittable::d_func()': gives
      'QBlittablePrivate', which has no cute class yet.
    - Qt's 'const QBlittablePrivate *QBlittable::d_func() const': gives
      'QBlittablePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBlittable.d_func' has no cute function yet. Qt's "
        "'QBlittablePrivate *QBlittable::d_func()': gives "
        "'QBlittablePrivate', which has no cute class yet. Qt's 'const "
        "QBlittablePrivate *QBlittable::d_func() const': gives "
        "'QBlittablePrivate', which has no cute class yet.")

  @staticmethod
  def drawCachedGlyphs(*__, **_) -> Never:
    """
    Qt's 'bool QBlittable::drawCachedGlyphs(const QPaintEngineState *state,
    QFontEngine::GlyphFormat glyphFormat, int numGlyphs, const glyph_t
    *glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)': names
    'glyph_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBlittable.drawCachedGlyphs' has no cute function yet. Qt's 'bool "
        "QBlittable::drawCachedGlyphs(const QPaintEngineState *state, "
        "QFontEngine::GlyphFormat glyphFormat, int numGlyphs, const glyph_t "
        "*glyphs, const QFixedPoint *positions, QFontEngine *fontEngine)': "
        "names 'glyph_t', which has no cute class yet.")
