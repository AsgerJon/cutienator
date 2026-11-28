"""
QSGCurveGlyphNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcurveglyphnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGCurveGlyphNode to be private: it declares the class in a
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
  from ..QtGui import QColor, QGlyphRun
  from . import QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QGlyphRun = WAIT['QGlyphRun']
  QPointF = WAIT['QPointF']
  QSGRenderContext = WAIT['QSGRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGCurveGlyphNode(QSGGlyphNode):
  """
  The cute side of Qt's QSGCurveGlyphNode: a plain Python object standing in
  front of one C++ QSGCurveGlyphNode.

  It is built on the cute 'QSGGlyphNode', as Qt's QSGCurveGlyphNode is built
  on Qt's QSGGlyphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCurveGlyphNode that has a ritual and that Python
  can call so far, 11 names in all: 'setGlyphs', 'update', 'preprocess',
  'setPreferredAntialiasingMode', 'updateGeometry', 'setColor', 'setStyle',
  'setStyleColor', 'baseLine', 'recycle', 'cleanup'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGCurveGlyphNode::~QSGCurveGlyphNode()': the destructor: Python
    never removes a C++ QSGCurveGlyphNode.

  What to expect
  --------------

  - The C++ QSGCurveGlyphNode is created at the first use, not by
    'QSGCurveGlyphNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCurveGlyphNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGCurveGlyphNode'

  #  A C++ QSGCurveGlyphNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCurveGlyphNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseLine(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSGCurveGlyphNode::baseLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#baseLine

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSGCurveGlyphNode::baseLine() const
    ritual = 'ritual_ZNK17QSGCurveGlyphNode8baseLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSGCurveGlyphNode8baseLineEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF, QGlyphRun)
  def setGlyphs(self, position: QPointF, glyphs: QGlyphRun) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::setGlyphs(const QPointF &position,
    const QGlyphRun &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#setGlyphs

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    glyphs : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QSGCurveGlyphNode::setGlyphs(const QPointF &position, const
    #      QGlyphRun &glyphs)
    ritual = 'ritual_ZN17QSGCurveGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGCurveGlyphNode9setGlyphsERK7QPointFRK9QGlyphRu'
          'n')
    self.uglySide.call(
        ritual, self._valueOf(position, 'QPointF'), self._valueOf(glyphs),
    )

  @overload(QSGGlyphNode.AntialiasingMode)
  def setPreferredAntialiasingMode(
      self,
      a0: QSGGlyphNode.AntialiasingMode,
  ) -> None:
    """
    Calls Qt's 'void
    QSGCurveGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveglyphnode.html

    Parameters
    ----------

    a0 : QSGGlyphNode.AntialiasingMode
      Passed on as its number.
    """
    #  void QSGCurveGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
    #      a0)
    ritual = (
        'ritual_ZN17QSGCurveGlyphNode28setPreferredAntialiasingModeEN12QSGG'
        'lyphNode16AntialiasingModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGCurveGlyphNode28setPreferredAntialiasingModeEN'
          '12QSGGlyphNode16AntialiasingModeE')
    self.uglySide.call(ritual, a0.value)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGCurveGlyphNode::setColor(const QColor &color)
    ritual = 'ritual_ZN17QSGCurveGlyphNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGCurveGlyphNode8setColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QQuickText.TextStyle)
  def setStyle(self, style: QQuickText.TextStyle) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::setStyle(QQuickText::TextStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#setStyle

    Parameters
    ----------

    style : QQuickText.TextStyle
      Passed on as its number.
    """
    #  void QSGCurveGlyphNode::setStyle(QQuickText::TextStyle style)
    ritual = 'ritual_ZN17QSGCurveGlyphNode8setStyleEN10QQuickText9TextStyleE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QSGCurveGlyphNode8setStyleEN10QQuickText9TextStyl'
          'eE')
    self.uglySide.call(ritual, style.value)

  @overload(QColor)
  def setStyleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::setStyleColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveglyphnode.html#setStyleColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGCurveGlyphNode::setStyleColor(const QColor &color)
    ritual = 'ritual_ZN17QSGCurveGlyphNode13setStyleColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGCurveGlyphNode13setStyleColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGCurveGlyphNode::QSGCurveGlyphNode(QSGRenderContext *context)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveglyphnode.html#QSGCurveGlyphNode

    Parameters
    ----------

    context : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGCurveGlyphNode::QSGCurveGlyphNode(QSGRenderContext *context)
    self._noteCreation(QSGCurveGlyphNode, lambda: Rituals.call(
        'ritual_ZN17QSGCurveGlyphNodeC1EP16QSGRenderContext',
        self._addressOf(context),
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
    Calls Qt's 'void QSGCurveGlyphNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#update
    """
    #  void QSGCurveGlyphNode::update()
    ritual = 'ritual_ZN17QSGCurveGlyphNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGCurveGlyphNode6updateEv'
    self.uglySide.call(ritual)

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::preprocess()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#preprocess
    """
    #  void QSGCurveGlyphNode::preprocess()
    ritual = 'ritual_ZN17QSGCurveGlyphNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGCurveGlyphNode10preprocessEv'
    self.uglySide.call(ritual)

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcurveglyphnode.html#updateGeometry
    """
    #  void QSGCurveGlyphNode::updateGeometry()
    self.uglySide.call('ritual_ZN17QSGCurveGlyphNode14updateGeometryEv')

  def recycle(self) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::recycle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#recycle
    """
    #  void QSGCurveGlyphNode::recycle()
    ritual = 'ritual_ZN17QSGCurveGlyphNode7recycleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSGCurveGlyphNode7recycleEv'
    self.uglySide.call(ritual)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QSGCurveGlyphNode::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgcurveglyphnode.html#cleanup
    """
    #  void QSGCurveGlyphNode::cleanup()
    self.uglySide.call('ritual_ZN17QSGCurveGlyphNode7cleanupEv')
