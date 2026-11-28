"""
QSGDistanceFieldGlyphNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDistanceFieldGlyphNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickText, QSGDistanceFieldGlyphConsumer, QSGGlyphNode

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


class QSGDistanceFieldGlyphNode(QSGGlyphNode, QSGDistanceFieldGlyphConsumer):
  """
  The cute side of Qt's QSGDistanceFieldGlyphNode: a plain Python object
  standing in front of one C++ QSGDistanceFieldGlyphNode.

  It is built on the cute 'QSGGlyphNode', as Qt's QSGDistanceFieldGlyphNode
  is built on Qt's QSGGlyphNode, and has everything that class has. It is
  built on the cute 'QSGDistanceFieldGlyphConsumer' as well, as Qt's
  QSGDistanceFieldGlyphNode is built on Qt's QSGDistanceFieldGlyphConsumer
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDistanceFieldGlyphNode that has a ritual and that
  Python can call so far, 12 names in all: 'baseLine', 'setGlyphs',
  'setColor', 'setPreferredAntialiasingMode', 'setRenderTypeQuality',
  'setStyle', 'setStyleColor', 'update', 'preprocess', 'recycle', 'cleanup',
  'updateMaterial'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDistanceFieldGlyphNode::~QSGDistanceFieldGlyphNode()': the
    destructor: Python never removes a C++ QSGDistanceFieldGlyphNode.
  - Qt's 'void QSGDistanceFieldGlyphNode::invalidateGlyphs(const
    QList<quint32> &glyphs)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void
    QSGDistanceFieldGlyphNode::setGlyphNodeType(DistanceFieldGlyphNodeType
    type)': names the enum
    'QSGDistanceFieldGlyphNode::DistanceFieldGlyphNodeType', whose class
    cannot be named here.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'non-virtual thunk to QSGDistanceFieldGlyphNode.

  What to expect
  --------------

  - The C++ QSGDistanceFieldGlyphNode is created at the first use, not by
    'QSGDistanceFieldGlyphNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDistanceFieldGlyphNode.
  - Each name of Qt's QSGDistanceFieldGlyphNode that has no cute function
    yet, '__init__', 'setGlyphNodeType', 'updateGeometry', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDistanceFieldGlyphNode'

  #  Qt's QSGDistanceFieldGlyphNode is built on more than one class. The part
  #  of a C++ QSGDistanceFieldGlyphNode that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSGDistanceFieldGlyphConsumer':
          'ritual_cast_QSGDistanceFieldGlyphNode_QSGDistanceFieldGlyphConsumer',
  }

  #  A C++ QSGDistanceFieldGlyphNode Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDistanceFieldGlyphNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseLine(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSGDistanceFieldGlyphNode::baseLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#baseLine

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSGDistanceFieldGlyphNode::baseLine() const
    ritual = 'ritual_ZNK25QSGDistanceFieldGlyphNode8baseLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QSGDistanceFieldGlyphNode8baseLineEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF, QGlyphRun)
  def setGlyphs(self, position: QPointF, glyphs: QGlyphRun) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::setGlyphs(const QPointF
    &position, const QGlyphRun &glyphs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#setGlyphs

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    glyphs : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QSGDistanceFieldGlyphNode::setGlyphs(const QPointF &position,
    #      const QGlyphRun &glyphs)
    ritual = (
        'ritual_ZN25QSGDistanceFieldGlyphNode9setGlyphsERK7QPointFRK9QGlyph'
        'Run')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGDistanceFieldGlyphNode9setGlyphsERK7QPointFRK9'
          'QGlyphRun')
    self.uglySide.call(
        ritual, self._valueOf(position, 'QPointF'), self._valueOf(glyphs),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDistanceFieldGlyphNode::setColor(const QColor &color)
    ritual = 'ritual_ZN25QSGDistanceFieldGlyphNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGDistanceFieldGlyphNode8setColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QSGGlyphNode.AntialiasingMode)
  def setPreferredAntialiasingMode(
      self,
      mode: QSGGlyphNode.AntialiasingMode,
  ) -> None:
    """
    Calls Qt's 'void
    QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html

    Parameters
    ----------

    mode : QSGGlyphNode.AntialiasingMode
      Passed on as its number.
    """
    #  void QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(
    #      AntialiasingMode mode)
    ritual = (
        'ritual_ZN25QSGDistanceFieldGlyphNode28setPreferredAntialiasingMode'
        'EN12QSGGlyphNode16AntialiasingModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGDistanceFieldGlyphNode28setPreferredAntialiasi'
          'ngModeEN12QSGGlyphNode16AntialiasingModeE')
    self.uglySide.call(ritual, mode.value)

  @overload(int)
  def setRenderTypeQuality(self, renderTypeQuality: int) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::setRenderTypeQuality(int
    renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html

    Parameters
    ----------

    renderTypeQuality : int
      Passed on as it is.
    """
    #  void QSGDistanceFieldGlyphNode::setRenderTypeQuality(int
    #      renderTypeQuality)
    ritual = 'ritual_ZN25QSGDistanceFieldGlyphNode20setRenderTypeQualityEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGDistanceFieldGlyphNode20setRenderTypeQualityEi')
    self.uglySide.call(ritual, renderTypeQuality)

  @overload(QQuickText.TextStyle)
  def setStyle(self, style: QQuickText.TextStyle) -> None:
    """
    Calls Qt's 'void
    QSGDistanceFieldGlyphNode::setStyle(QQuickText::TextStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#setStyle

    Parameters
    ----------

    style : QQuickText.TextStyle
      Passed on as its number.
    """
    #  void QSGDistanceFieldGlyphNode::setStyle(QQuickText::TextStyle style)
    ritual = (
        'ritual_ZN25QSGDistanceFieldGlyphNode8setStyleEN10QQuickText9TextSt'
        'yleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGDistanceFieldGlyphNode8setStyleEN10QQuickText9'
          'TextStyleE')
    self.uglySide.call(ritual, style.value)

  @overload(QColor)
  def setStyleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::setStyleColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#setStyleColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDistanceFieldGlyphNode::setStyleColor(const QColor &color)
    ritual = 'ritual_ZN25QSGDistanceFieldGlyphNode13setStyleColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGDistanceFieldGlyphNode13setStyleColorERK6QColo'
          'r')
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QSGDistanceFieldGlyphNode::QSGDistanceFieldGlyphNode(QSGRenderContext
    *context)': leans on 'non-virtual thunk to
    QSGDistanceFieldGlyphNode::invalidateGlyphs(QList<unsigned int> const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphNode.__init__' has no cute function yet. "
        "Qt's "
        "'QSGDistanceFieldGlyphNode::QSGDistanceFieldGlyphNode(QSGRenderCont"
        "ext *context)': leans on 'non-virtual thunk to "
        "QSGDistanceFieldGlyphNode::invalidateGlyphs(QList<unsigned int> "
        "const&)', which Qt's source does not mark for use from outside Qt "
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
    Calls Qt's 'void QSGDistanceFieldGlyphNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#update
    """
    #  void QSGDistanceFieldGlyphNode::update()
    ritual = 'ritual_ZN25QSGDistanceFieldGlyphNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGDistanceFieldGlyphNode6updateEv'
    self.uglySide.call(ritual)

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#preprocess
    """
    #  void QSGDistanceFieldGlyphNode::preprocess()
    self.uglySide.call('ritual_ZN25QSGDistanceFieldGlyphNode10preprocessEv')

  def recycle(self) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::recycle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#recycle
    """
    #  void QSGDistanceFieldGlyphNode::recycle()
    ritual = 'ritual_ZN25QSGDistanceFieldGlyphNode7recycleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGDistanceFieldGlyphNode7recycleEv'
    self.uglySide.call(ritual)

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#cleanup
    """
    #  void QSGDistanceFieldGlyphNode::cleanup()
    self.uglySide.call('ritual_ZN25QSGDistanceFieldGlyphNode7cleanupEv')

  def updateMaterial(self) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldGlyphNode::updateMaterial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldglyphnode.html#updateMaterial
    """
    #  void QSGDistanceFieldGlyphNode::updateMaterial()
    self.uglySide.call(
        'ritual_ZN25QSGDistanceFieldGlyphNode14updateMaterialEv',
    )

  @staticmethod
  def setGlyphNodeType(*__, **_) -> Never:
    """
    Qt's 'void
    QSGDistanceFieldGlyphNode::setGlyphNodeType(DistanceFieldGlyphNodeType
    type)': names the enum
    'QSGDistanceFieldGlyphNode::DistanceFieldGlyphNodeType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphNode.setGlyphNodeType' has no cute function "
        "yet. Qt's 'void "
        "QSGDistanceFieldGlyphNode::setGlyphNodeType(DistanceFieldGlyphNodeT"
        "ype type)': names the enum "
        "'QSGDistanceFieldGlyphNode::DistanceFieldGlyphNodeType', whose "
        "class cannot be named here.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void QSGDistanceFieldGlyphNode::updateGeometry()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 's_totalAllocation'.
    """
    raise NotImplementedError(
        "'QSGDistanceFieldGlyphNode.updateGeometry' has no cute function "
        "yet. Qt's 'void QSGDistanceFieldGlyphNode::updateGeometry()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'s_totalAllocation'.")
