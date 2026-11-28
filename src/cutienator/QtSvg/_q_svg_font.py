"""
QSvgFont binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgfont_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgFont to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QPainterPath
  from . import QSvgGlyph
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']


class QSvgFont(QSvgNode):
  """
  The cute side of Qt's QSvgFont: a plain Python object standing in front of
  one C++ QSvgFont.

  It is built on the cute 'QSvgNode', as Qt's QSvgFont is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgFont that has a ritual and that Python can call
  so far, 5 names in all: 'type', 'setUnitsPerEm', 'addGlyph',
  'addMissingGlyph', 'findFirstGlyphFor'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFont::~QSvgFont()': the destructor: Python never removes a C++
    QSvgFont.
  - Qt's 'void QSvgFont::drawCommand(QPainter *a0, QSvgExtraStates &a1)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgFont::draw(QPainter *p, const QPointF &point, const
    QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
    alignment) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgFont::boundingRect(QPainter *p, const QPointF &point,
    const QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
    alignment) const': takes a type Python has no way to hand over yet.
  - Qt's 'QList<const QSvgGlyph *> QSvgFont::toGlyphs(QStringView text)
    const': gives a type Python has no way to take yet.
  - Qt's 'void QSvgFont::draw_helper(QPainter *p, const QPointF &point, const
    QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
    alignment, QRectF *boundingRect) const': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ QSvgFont is created at the first use, not by 'QSvgFont(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgFont.
  - Each name of Qt's QSvgFont that has no cute function yet, 'boundingRect',
    'draw_helper', 'toGlyphs', holds a function that raises
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
  __qt_class__ = 'QSvgFont'

  #  A C++ QSvgFont Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFont'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgFont::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfont.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgFont::type() const
    ritual = 'ritual_ZNK8QSvgFont4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgFont4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  @overload(str)
  def findFirstGlyphFor(self, text: str) -> Optional[QSvgGlyph]:
    """
    Calls Qt's 'const QSvgGlyph *QSvgFont::findFirstGlyphFor(QStringView
    text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfont.html#findFirstGlyphFor

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSvgGlyph]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSvgGlyph *QSvgFont::findFirstGlyphFor(QStringView text) const
    address = self.uglySide.call(
        'ritual_ZNK8QSvgFont17findFirstGlyphForE11QStringView', text,
    )
    from . import QSvgGlyph
    return QSvgGlyph._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setUnitsPerEm(self, upem: float) -> None:
    """
    Calls Qt's 'void QSvgFont::setUnitsPerEm(qreal upem)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfont.html#setUnitsPerEm

    Parameters
    ----------

    upem : float
      Passed on as it is.
    """
    #  void QSvgFont::setUnitsPerEm(qreal upem)
    self.uglySide.call('ritual_ZN8QSvgFont13setUnitsPerEmEd', upem)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def __init__(self, horizAdvX: float) -> None:
    """
    Notes what was given, for Qt's 'QSvgFont::QSvgFont(qreal horizAdvX)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfont.html#QSvgFont

    Parameters
    ----------

    horizAdvX : float
      Passed on as it is.
    """
    #  QSvgFont::QSvgFont(qreal horizAdvX)
    self._noteCreation(QSvgFont, lambda: Rituals.call(
        'ritual_ZN8QSvgFontC1Ed', horizAdvX,
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

  @overload(str, QPainterPath)
  @overload(str, QPainterPath, float)
  def addGlyph(
      self,
      unicode: str,
      path: QPainterPath,
      horizAdvX: float = -1.0,
  ) -> None:
    """
    Calls Qt's 'void QSvgFont::addGlyph(const QString &unicode, const
    QPainterPath &path, qreal horizAdvX)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfont.html#addGlyph

    Parameters
    ----------

    unicode : str
      Passed on as it is: a QString is made of it for the call.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    horizAdvX : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.
    """
    #  void QSvgFont::addGlyph(const QString &unicode, const QPainterPath
    #      &path, qreal horizAdvX)
    self.uglySide.call(
        'ritual_ZN8QSvgFont8addGlyphERK7QStringRK12QPainterPathd',
        unicode, self._valueOf(path), horizAdvX,
    )

  @overload(QPainterPath, float)
  def addMissingGlyph(self, path: QPainterPath, horizAdvX: float) -> bool:
    """
    Calls Qt's 'bool QSvgFont::addMissingGlyph(const QPainterPath &path,
    qreal horizAdvX)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfont.html#addMissingGlyph

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    horizAdvX : float
      Passed on as it is.
    """
    #  bool QSvgFont::addMissingGlyph(const QPainterPath &path, qreal
    #      horizAdvX)
    return self.uglySide.call(
        'ritual_ZN8QSvgFont15addMissingGlyphERK12QPainterPathd',
        self._valueOf(path), horizAdvX,
    )

  @staticmethod
  def boundingRect(*__, **_) -> Never:
    """
    Qt's 'QRectF QSvgFont::boundingRect(QPainter *p, const QPointF &point,
    const QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
    alignment) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgFont.boundingRect' has no cute function yet. Qt's 'QRectF "
        "QSvgFont::boundingRect(QPainter *p, const QPointF &point, const "
        "QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment "
        "alignment) const': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def draw_helper(*__, **_) -> Never:
    """
    Qt's 'void QSvgFont::draw_helper(QPainter *p, const QPointF &point, const
    QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment
    alignment, QRectF *boundingRect) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgFont.draw_helper' has no cute function yet. Qt's 'void "
        "QSvgFont::draw_helper(QPainter *p, const QPointF &point, const "
        "QList<const QSvgGlyph *> &glyphs, qreal pixelSize, Qt::Alignment "
        "alignment, QRectF *boundingRect) const': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def toGlyphs(*__, **_) -> Never:
    """
    Qt's 'QList<const QSvgGlyph *> QSvgFont::toGlyphs(QStringView text)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgFont.toGlyphs' has no cute function yet. Qt's 'QList<const "
        "QSvgGlyph *> QSvgFont::toGlyphs(QStringView text) const': gives a "
        "type Python has no way to take yet.")
