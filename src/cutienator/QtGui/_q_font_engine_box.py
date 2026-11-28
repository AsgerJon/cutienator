"""
QFontEngineBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFontEngineBox to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QFontEngine, QTextItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
  from . import QFixed, QGlyphLayout, QImage, QPaintEngine, QPainterPath
  from . import QTextItemInt, glyph_metrics_t
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QGlyphLayout = WAIT['QGlyphLayout']
  QPaintEngine = WAIT['QPaintEngine']
  QPainterPath = WAIT['QPainterPath']
  QTextItemInt = WAIT['QTextItemInt']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontEngineBox(QFontEngine):
  """
  The cute side of Qt's QFontEngineBox: a plain Python object standing in
  front of one C++ QFontEngineBox.

  It is built on the cute 'QFontEngine', as Qt's QFontEngineBox is built on
  Qt's QFontEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFontEngineBox that has a ritual and that Python can
  call so far, 17 names in all: 'glyphIndex', 'recalcAdvances', 'draw',
  'addOutlineToPath', 'boundingBox', 'cloneWithSize', 'emSquareSize',
  'ascent', 'capHeight', 'descent', 'leading', 'maxCharWidth',
  'minLeftBearing', 'minRightBearing', 'alphaMapForGlyph', 'canRender',
  'size'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontEngineBox::~QFontEngineBox()': the destructor: Python never
    removes a C++ QFontEngineBox.
  - Qt's 'int QFontEngineBox::stringToCMap(const QChar *str, int len,
    QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const': takes a
    number to change where it is.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 leans on 'QFontEngineBox.

  What to expect
  --------------

  - The C++ QFontEngineBox is created at the first use, not by
    'QFontEngineBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontEngineBox.
  - Each name of Qt's QFontEngineBox that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontEngineBox'

  #  A C++ QFontEngineBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontEngineBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def glyphIndex(self, ucs4: int) -> int:
    """
    Calls Qt's 'glyph_t QFontEngineBox::glyphIndex(uint ucs4) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#glyphIndex

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  glyph_t QFontEngineBox::glyphIndex(uint ucs4) const
    ritual = 'ritual_ZNK14QFontEngineBox10glyphIndexEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox10glyphIndexEj'
    return self.uglySide.call(ritual, ucs4)

  @overload(float)
  def cloneWithSize(self, pixelSize: float) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontEngineBox::cloneWithSize(qreal pixelSize)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#cloneWithSize

    Parameters
    ----------

    pixelSize : float
      Passed on as it is.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontEngineBox::cloneWithSize(qreal pixelSize) const
    address = self.uglySide.call(
        'ritual_ZNK14QFontEngineBox13cloneWithSizeEd', pixelSize,
    )
    return QFontEngine._cuteAt(address)

  def emSquareSize(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineBox::emSquareSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#emSquareSize

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineBox::emSquareSize() const
    ritual = 'ritual_ZNK14QFontEngineBox12emSquareSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox12emSquareSizeEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def ascent(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineBox::ascent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#ascent

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineBox::ascent() const
    ritual = 'ritual_ZNK14QFontEngineBox6ascentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox6ascentEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def capHeight(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineBox::capHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#capHeight

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineBox::capHeight() const
    ritual = 'ritual_ZNK14QFontEngineBox9capHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox9capHeightEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def descent(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineBox::descent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#descent

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineBox::descent() const
    ritual = 'ritual_ZNK14QFontEngineBox7descentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox7descentEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def leading(self) -> QFixed:
    """
    Calls Qt's 'QFixed QFontEngineBox::leading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#leading

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QFontEngineBox::leading() const
    ritual = 'ritual_ZNK14QFontEngineBox7leadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox7leadingEv'
    address = self.uglySide.call(ritual)
    from . import QFixed
    return QFixed._cuteOwning(address)

  def maxCharWidth(self) -> float:
    """
    Calls Qt's 'qreal QFontEngineBox::maxCharWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#maxCharWidth
    """
    #  qreal QFontEngineBox::maxCharWidth() const
    ritual = 'ritual_ZNK14QFontEngineBox12maxCharWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox12maxCharWidthEv'
    return self.uglySide.call(ritual)

  def minLeftBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontEngineBox::minLeftBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#minLeftBearing
    """
    #  qreal QFontEngineBox::minLeftBearing() const
    ritual = 'ritual_ZNK14QFontEngineBox14minLeftBearingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox14minLeftBearingEv'
    return self.uglySide.call(ritual)

  def minRightBearing(self) -> float:
    """
    Calls Qt's 'qreal QFontEngineBox::minRightBearing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginebox.html#minRightBearing
    """
    #  qreal QFontEngineBox::minRightBearing() const
    ritual = 'ritual_ZNK14QFontEngineBox15minRightBearingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox15minRightBearingEv'
    return self.uglySide.call(ritual)

  @overload(QChar, int)
  @overload(NoneType, int)
  def canRender(self, string: Optional[QChar], len: int) -> bool:
    """
    Calls Qt's 'bool QFontEngineBox::canRender(const QChar *string, int len)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#canRender

    Parameters
    ----------

    string : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.
    """
    #  bool QFontEngineBox::canRender(const QChar *string, int len) const
    ritual = 'ritual_ZNK14QFontEngineBox9canRenderEPK5QChari'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFontEngineBox9canRenderEPK5QChari'
    return self.uglySide.call(ritual, self._addressOf(string), len)

  def size(self) -> int:
    """
    Calls Qt's 'int QFontEngineBox::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#size
    """
    #  int QFontEngineBox::size() const
    return self.uglySide.call('ritual_ZNK14QFontEngineBox4sizeEv')

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
    - Qt's 'QFontEngineBox::QFontEngineBox(int size)': leans on
      'QFontEngineBox::boundingBox(QGlyphLayout const&)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'QFontEngineBox::QFontEngineBox(Type type, int size)': leans on
      'QFontEngineBox::boundingBox(QGlyphLayout const&)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QFontEngineBox.__init__' has no cute function yet. Qt's "
        "'QFontEngineBox::QFontEngineBox(int size)': leans on "
        "'QFontEngineBox::boundingBox(QGlyphLayout const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken. Qt's 'QFontEngineBox::QFontEngineBox(Type "
        "type, int size)': leans on "
        "'QFontEngineBox::boundingBox(QGlyphLayout const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QGlyphLayout, QFontEngine.ShaperFlags)
  @overload(NoneType, QFontEngine.ShaperFlags)
  def recalcAdvances(
      self,
      a0: Optional[QGlyphLayout],
      a1: QFontEngine.ShaperFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngineBox::recalcAdvances(QGlyphLayout *a0,
    ShaperFlags a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#recalcAdvances

    Parameters
    ----------

    a0 : Optional[QGlyphLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QFontEngine.ShaperFlags
      Passed on as its number.
    """
    #  void QFontEngineBox::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
    #      const
    ritual = (
        'ritual_ZNK14QFontEngineBox14recalcAdvancesEP12QGlyphLayout6QFlagsI'
        'N11QFontEngine10ShaperFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QFontEngineBox14recalcAdvancesEP12QGlyphLayout6Q'
          'FlagsIN11QFontEngine10ShaperFlagEE')
    self.uglySide.call(ritual, self._addressOf(a0, 'QGlyphLayout'), a1.value)

  @overload(QPaintEngine, float, float, QTextItemInt)
  @overload(NoneType, float, float, QTextItemInt)
  def draw(
      self,
      p: Optional[QPaintEngine],
      x: float,
      y: float,
      si: QTextItemInt,
  ) -> None:
    """
    Calls Qt's 'void QFontEngineBox::draw(QPaintEngine *p, qreal x, qreal y,
    const QTextItemInt &si)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#draw

    Parameters
    ----------

    p : Optional[QPaintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    si : QTextItemInt
      Passed on as a value: Qt reads the C++ QTextItemInt, which stays
      Python's own.
    """
    #  void QFontEngineBox::draw(QPaintEngine *p, qreal x, qreal y, const
    #      QTextItemInt &si)
    self.uglySide.call(
        'ritual_ZN14QFontEngineBox4drawEP12QPaintEngineddRK12QTextItemInt',
        self._addressOf(p), x, y, self._valueOf(si),
    )

  @overload(float, float, QGlyphLayout, QPainterPath, QTextItem.RenderFlags)
  @overload(float, float, QGlyphLayout, NoneType, QTextItem.RenderFlags)
  def addOutlineToPath(
      self,
      x: float,
      y: float,
      glyphs: QGlyphLayout,
      path: Optional[QPainterPath],
      flags: QTextItem.RenderFlags,
  ) -> None:
    """
    Calls Qt's 'void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const
    QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginebox.html#addOutlineToPath

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    glyphs : QGlyphLayout
      Passed on as a value: Qt reads the C++ QGlyphLayout, which stays
      Python's own.

    path : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QTextItem.RenderFlags
      Passed on as its number.
    """
    #  void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const
    #      QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags
    #      flags)
    ritual = (
        'ritual_ZN14QFontEngineBox16addOutlineToPathEddRK12QGlyphLayoutP12Q'
        'PainterPath6QFlagsIN9QTextItem10RenderFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QFontEngineBox16addOutlineToPathEddRK12QGlyphLayo'
          'utP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE')
    self.uglySide.call(
        ritual,
        x, y, self._valueOf(glyphs, 'QGlyphLayout'), self._addressOf(path),
        flags.value,
    )

  @overload(QGlyphLayout)
  def boundingBox(self, glyphs: QGlyphLayout) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngineBox::boundingBox(const
    QGlyphLayout &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#boundingBox

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
    #  glyph_metrics_t QFontEngineBox::boundingBox(const QGlyphLayout
    #      &glyphs)
    address = self.uglySide.call(
        'ritual_ZN14QFontEngineBox11boundingBoxERK12QGlyphLayout',
        self._valueOf(glyphs, 'QGlyphLayout'),
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int)
  def boundingBox(self, glyph: int) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t QFontEngineBox::boundingBox(glyph_t glyph)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontenginebox.html#boundingBox

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
    #  glyph_metrics_t QFontEngineBox::boundingBox(glyph_t glyph)
    address = self.uglySide.call(
        'ritual_ZN14QFontEngineBox11boundingBoxEj', glyph,
    )
    from . import glyph_metrics_t
    return glyph_metrics_t._cuteOwning(address)

  @overload(int)
  def alphaMapForGlyph(self, a0: int) -> QImage:
    """
    Calls Qt's 'QImage QFontEngineBox::alphaMapForGlyph(glyph_t a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontenginebox.html#alphaMapForGlyph

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QFontEngineBox::alphaMapForGlyph(glyph_t a0)
    ritual = 'ritual_ZN14QFontEngineBox16alphaMapForGlyphEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QFontEngineBox16alphaMapForGlyphEj'
    address = self.uglySide.call(ritual, a0)
    from . import QImage
    return QImage._cuteOwning(address)
