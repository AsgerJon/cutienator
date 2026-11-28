"""
QSGDefaultGlyphNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGDefaultGlyphNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickText, QSGGlyphNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPointF
  from ..QtGui import QColor, QGlyphRun
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QGlyphRun = WAIT['QGlyphRun']
  QPointF = WAIT['QPointF']


class QSGDefaultGlyphNode(QSGGlyphNode):
  """
  The cute side of Qt's QSGDefaultGlyphNode: a plain Python object standing
  in front of one C++ QSGDefaultGlyphNode.

  It is built on the cute 'QSGGlyphNode', as Qt's QSGDefaultGlyphNode is
  built on Qt's QSGGlyphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultGlyphNode that has a ritual and that
  Python can call so far, 10 names in all: 'setGlyphs', 'setColor',
  'setStyle', 'setStyleColor', 'baseLine', 'update', 'preprocess',
  'setPreferredAntialiasingMode', 'recycle', 'cleanup'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDefaultGlyphNode::~QSGDefaultGlyphNode()': the destructor:
    Python never removes a C++ QSGDefaultGlyphNode.
  - Qt's 'void QSGDefaultGlyphNode::setGlyphNodeType(DefaultGlyphNodeType
    type)': names the enum 'QSGDefaultGlyphNode::DefaultGlyphNodeType', whose
    class cannot be named here.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 leans on 'QSGTextMaskMaterial.

  What to expect
  --------------

  - The C++ QSGDefaultGlyphNode is created at the first use, not by
    'QSGDefaultGlyphNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultGlyphNode.
  - Each name of Qt's QSGDefaultGlyphNode that has no cute function yet,
    '__init__', 'setGlyphNodeType', 'updateGeometry', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultGlyphNode'

  #  A C++ QSGDefaultGlyphNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDefaultGlyphNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseLine(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSGDefaultGlyphNode::baseLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#baseLine

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSGDefaultGlyphNode::baseLine() const
    ritual = 'ritual_ZNK19QSGDefaultGlyphNode8baseLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QSGDefaultGlyphNode8baseLineEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF, QGlyphRun)
  def setGlyphs(self, position: QPointF, glyphs: QGlyphRun) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::setGlyphs(const QPointF &position,
    const QGlyphRun &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#setGlyphs

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    glyphs : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QSGDefaultGlyphNode::setGlyphs(const QPointF &position, const
    #      QGlyphRun &glyphs)
    ritual = (
        'ritual_ZN19QSGDefaultGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultGlyphNode9setGlyphsERK7QPointFRK9QGlyph'
          'Run')
    self.uglySide.call(
        ritual, self._valueOf(position, 'QPointF'), self._valueOf(glyphs),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDefaultGlyphNode::setColor(const QColor &color)
    ritual = 'ritual_ZN19QSGDefaultGlyphNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultGlyphNode8setColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QQuickText.TextStyle)
  def setStyle(self, a0: QQuickText.TextStyle) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::setStyle(QQuickText::TextStyle
    a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#setStyle

    Parameters
    ----------

    a0 : QQuickText.TextStyle
      Passed on as its number.
    """
    #  void QSGDefaultGlyphNode::setStyle(QQuickText::TextStyle a0)
    ritual = (
        'ritual_ZN19QSGDefaultGlyphNode8setStyleEN10QQuickText9TextStyleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultGlyphNode8setStyleEN10QQuickText9TextSt'
          'yleE')
    self.uglySide.call(ritual, a0.value)

  @overload(QColor)
  def setStyleColor(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::setStyleColor(const QColor &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#setStyleColor

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDefaultGlyphNode::setStyleColor(const QColor &a0)
    ritual = 'ritual_ZN19QSGDefaultGlyphNode13setStyleColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultGlyphNode13setStyleColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QSGGlyphNode.AntialiasingMode)
  def setPreferredAntialiasingMode(
      self,
      a0: QSGGlyphNode.AntialiasingMode,
  ) -> None:
    """
    Calls Qt's 'void
    QSGDefaultGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultglyphnode.html

    Parameters
    ----------

    a0 : QSGGlyphNode.AntialiasingMode
      Passed on as its number.
    """
    #  void
    #      QSGDefaultGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
    #      a0)
    ritual = (
        'ritual_ZN19QSGDefaultGlyphNode28setPreferredAntialiasingModeEN12QS'
        'GGlyphNode16AntialiasingModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QSGDefaultGlyphNode28setPreferredAntialiasingMode'
          'EN12QSGGlyphNode16AntialiasingModeE')
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGDefaultGlyphNode::QSGDefaultGlyphNode(QSGRenderContext
    *context)': leans on
    'QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGDefaultGlyphNode.__init__' has no cute function yet. Qt's "
        "'QSGDefaultGlyphNode::QSGDefaultGlyphNode(QSGRenderContext "
        "*context)': leans on "
        "'QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode"
        ") const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'void QSGDefaultGlyphNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#update
    """
    #  void QSGDefaultGlyphNode::update()
    self.uglySide.call('ritual_ZN19QSGDefaultGlyphNode6updateEv')

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#preprocess
    """
    #  void QSGDefaultGlyphNode::preprocess()
    self.uglySide.call('ritual_ZN19QSGDefaultGlyphNode10preprocessEv')

  def recycle(self) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::recycle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#recycle
    """
    #  void QSGDefaultGlyphNode::recycle()
    ritual = 'ritual_ZN19QSGDefaultGlyphNode7recycleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QSGDefaultGlyphNode7recycleEv'
    self.uglySide.call(ritual)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QSGDefaultGlyphNode::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultglyphnode.html#cleanup
    """
    #  void QSGDefaultGlyphNode::cleanup()
    self.uglySide.call('ritual_ZN19QSGDefaultGlyphNode7cleanupEv')

  @staticmethod
  def setGlyphNodeType(*__, **_) -> Never:
    """
    Qt's 'void QSGDefaultGlyphNode::setGlyphNodeType(DefaultGlyphNodeType
    type)': names the enum 'QSGDefaultGlyphNode::DefaultGlyphNodeType', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QSGDefaultGlyphNode.setGlyphNodeType' has no cute function yet. "
        "Qt's 'void "
        "QSGDefaultGlyphNode::setGlyphNodeType(DefaultGlyphNodeType type)': "
        "names the enum 'QSGDefaultGlyphNode::DefaultGlyphNodeType', whose "
        "class cannot be named here.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void QSGDefaultGlyphNode::updateGeometry()': leans on
    'QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGDefaultGlyphNode.updateGeometry' has no cute function yet. "
        "Qt's 'void QSGDefaultGlyphNode::updateGeometry()': leans on "
        "'QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode"
        ") const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
