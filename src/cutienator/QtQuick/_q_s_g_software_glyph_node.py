"""
QSGSoftwareGlyphNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwareglyphnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareGlyphNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickText, QSGGlyphNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtGui import QColor, QGlyphRun, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QGlyphRun = WAIT['QGlyphRun']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareGlyphNode(QSGGlyphNode):
  """
  The cute side of Qt's QSGSoftwareGlyphNode: a plain Python object standing
  in front of one C++ QSGSoftwareGlyphNode.

  It is built on the cute 'QSGGlyphNode', as Qt's QSGSoftwareGlyphNode is
  built on Qt's QSGGlyphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareGlyphNode that has a ritual and that
  Python can call so far, 10 names in all: 'setGlyphs', 'setColor',
  'setStyle', 'setStyleColor', 'baseLine', 'setPreferredAntialiasingMode',
  'update', 'paint', 'recycle', 'recalculateBoundingRect'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGSoftwareGlyphNode is created at the first use, not by
    'QSGSoftwareGlyphNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareGlyphNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareGlyphNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseLine(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSGSoftwareGlyphNode::baseLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#baseLine

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSGSoftwareGlyphNode::baseLine() const
    ritual = 'ritual_ZNK20QSGSoftwareGlyphNode8baseLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGSoftwareGlyphNode8baseLineEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF, QGlyphRun)
  def setGlyphs(self, position: QPointF, glyphs: QGlyphRun) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::setGlyphs(const QPointF &position,
    const QGlyphRun &glyphs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#setGlyphs

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    glyphs : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QSGSoftwareGlyphNode::setGlyphs(const QPointF &position, const
    #      QGlyphRun &glyphs)
    ritual = (
        'ritual_ZN20QSGSoftwareGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareGlyphNode9setGlyphsERK7QPointFRK9QGlyp'
          'hRun')
    self.uglySide.call(
        ritual, self._valueOf(position, 'QPointF'), self._valueOf(glyphs),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSoftwareGlyphNode::setColor(const QColor &color)
    ritual = 'ritual_ZN20QSGSoftwareGlyphNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareGlyphNode8setColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QQuickText.TextStyle)
  def setStyle(self, style: QQuickText.TextStyle) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::setStyle(QQuickText::TextStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#setStyle

    Parameters
    ----------

    style : QQuickText.TextStyle
      Passed on as its number.
    """
    #  void QSGSoftwareGlyphNode::setStyle(QQuickText::TextStyle style)
    ritual = (
        'ritual_ZN20QSGSoftwareGlyphNode8setStyleEN10QQuickText9TextStyleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareGlyphNode8setStyleEN10QQuickText9TextS'
          'tyleE')
    self.uglySide.call(ritual, style.value)

  @overload(QColor)
  def setStyleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::setStyleColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#setStyleColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSoftwareGlyphNode::setStyleColor(const QColor &color)
    ritual = 'ritual_ZN20QSGSoftwareGlyphNode13setStyleColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareGlyphNode13setStyleColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QSGGlyphNode.AntialiasingMode)
  def setPreferredAntialiasingMode(
      self,
      a0: QSGGlyphNode.AntialiasingMode,
  ) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html

    Parameters
    ----------

    a0 : QSGGlyphNode.AntialiasingMode
      Passed on as its number.
    """
    #  void QSGSoftwareGlyphNode::setPreferredAntialiasingMode(
    #      AntialiasingMode a0)
    ritual = (
        'ritual_ZN20QSGSoftwareGlyphNode28setPreferredAntialiasingModeEN12Q'
        'SGGlyphNode16AntialiasingModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGSoftwareGlyphNode28setPreferredAntialiasingMod'
          'eEN12QSGGlyphNode16AntialiasingModeE')
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSGSoftwareGlyphNode::QSGSoftwareGlyphNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#QSGSoftwareGlyphNode
    """
    #  QSGSoftwareGlyphNode::QSGSoftwareGlyphNode()
    self._noteCreation(QSGSoftwareGlyphNode, lambda: Rituals.call(
        'ritual_ZN20QSGSoftwareGlyphNodeC1Ev',
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

  def update(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#update
    """
    #  void QSGSoftwareGlyphNode::update()
    ritual = 'ritual_ZN20QSGSoftwareGlyphNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareGlyphNode6updateEv'
    self.uglySide.call(ritual)

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareGlyphNode::paint(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN20QSGSoftwareGlyphNode5paintEP8QPainter',
        self._addressOf(painter),
    )

  def recycle(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::recycle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#recycle
    """
    #  void QSGSoftwareGlyphNode::recycle()
    ritual = 'ritual_ZN20QSGSoftwareGlyphNode7recycleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGSoftwareGlyphNode7recycleEv'
    self.uglySide.call(ritual)

  def recalculateBoundingRect(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareGlyphNode::recalculateBoundingRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareglyphnode.html#recalculateBoundingRect
    """
    #  void QSGSoftwareGlyphNode::recalculateBoundingRect()
    self.uglySide.call(
        'ritual_ZN20QSGSoftwareGlyphNode23recalculateBoundingRectEv',
    )
