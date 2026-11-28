"""
QSGCurveGlyphAtlas binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcurveglyphatlas_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGCurveGlyphAtlas to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtGui import QRawFont
  from . import QSGCurveFillNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRawFont = WAIT['QRawFont']
  QSGCurveFillNode = WAIT['QSGCurveFillNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGCurveGlyphAtlas(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGCurveGlyphAtlas: a plain Python object standing in
  front of one C++ QSGCurveGlyphAtlas.

  C++ hands a QSGCurveGlyphAtlas around as a copy, so every C++
  QSGCurveGlyphAtlas behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGCurveGlyphAtlas that has a ritual and that Python
  can call so far, 2 names in all: 'addGlyph', 'fontSize'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGCurveGlyphAtlas::~QSGCurveGlyphAtlas()': the destructor: Python
    removes its C++ QSGCurveGlyphAtlas by it, and has no other use for it.
  - Qt's 'void QSGCurveGlyphAtlas::populate(const QList<glyph_t> &glyphs)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSGCurveGlyphAtlas::addStroke(QSGCurveStrokeNode *node,
    glyph_t glyph, const QPointF &position) const': names
    'QSGCurveStrokeNode', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSGCurveGlyphAtlas is created at the first use, not by
    'QSGCurveGlyphAtlas(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGCurveGlyphAtlas back gives a copy the ritual made
    for Python, in a new cute QSGCurveGlyphAtlas.
  - Each name of Qt's QSGCurveGlyphAtlas that has no cute function yet,
    'addStroke', 'populate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCurveGlyphAtlas'

  #  Qt's '~QSGCurveGlyphAtlas()'. Naming it makes this a value class: Python
  #  owns every C++ QSGCurveGlyphAtlas behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSGCurveGlyphAtlasD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fontSize(self) -> float:
    """
    Calls Qt's 'qreal QSGCurveGlyphAtlas::fontSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphatlas.html#fontSize
    """
    #  qreal QSGCurveGlyphAtlas::fontSize() const
    return self.uglySide.call('ritual_ZNK18QSGCurveGlyphAtlas8fontSizeEv')

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

  @overload(QRawFont)
  def __init__(self, font: QRawFont) -> None:
    """
    Notes what was given, for Qt's
    'QSGCurveGlyphAtlas::QSGCurveGlyphAtlas(const QRawFont &font)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveglyphatlas.html#QSGCurveGlyphAtlas

    Parameters
    ----------

    font : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  QSGCurveGlyphAtlas::QSGCurveGlyphAtlas(const QRawFont &font)
    self._noteCreation(QSGCurveGlyphAtlas, lambda: Rituals.call(
        'ritual_ZN18QSGCurveGlyphAtlasC1ERK8QRawFont', self._valueOf(font),
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

  @overload(QSGCurveFillNode, int, QPointF, float)
  @overload(NoneType, int, QPointF, float)
  def addGlyph(
      self,
      node: Optional[QSGCurveFillNode],
      glyph: int,
      position: QPointF,
      pixelSize: float,
  ) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphAtlas::addGlyph(QSGCurveFillNode *node,
    glyph_t glyph, const QPointF &position, qreal pixelSize) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphatlas.html#addGlyph

    Parameters
    ----------

    node : Optional[QSGCurveFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    glyph : int
      Passed on as it is.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pixelSize : float
      Passed on as it is.
    """
    #  void QSGCurveGlyphAtlas::addGlyph(QSGCurveFillNode *node, glyph_t
    #      glyph, const QPointF &position, qreal pixelSize) const
    self.uglySide.call(
        'ritual_ZNK18QSGCurveGlyphAtlas8addGlyphEP16QSGCurveFillNodejRK7QPo'
        'intFd',
        self._addressOf(node), glyph, self._valueOf(position, 'QPointF'),
        pixelSize,
    )

  @staticmethod
  def addStroke(*__, **_) -> Never:
    """
    Qt's 'void QSGCurveGlyphAtlas::addStroke(QSGCurveStrokeNode *node,
    glyph_t glyph, const QPointF &position) const': names
    'QSGCurveStrokeNode', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGCurveGlyphAtlas.addStroke' has no cute function yet. Qt's "
        "'void QSGCurveGlyphAtlas::addStroke(QSGCurveStrokeNode *node, "
        "glyph_t glyph, const QPointF &position) const': names "
        "'QSGCurveStrokeNode', which has no cute class yet.")

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'void QSGCurveGlyphAtlas::populate(const QList<glyph_t> &glyphs)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGCurveGlyphAtlas.populate' has no cute function yet. Qt's 'void "
        "QSGCurveGlyphAtlas::populate(const QList<glyph_t> &glyphs)': takes "
        "a type Python has no way to hand over yet.")
