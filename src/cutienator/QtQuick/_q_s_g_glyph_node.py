"""
QSGGlyphNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGGlyphNode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QQuickText, QSGTextNode, QSGVisitableNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QColor, QGlyphRun
  from . import QSGNodeVisitorEx
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QGlyphRun = WAIT['QGlyphRun']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSGNodeVisitorEx = WAIT['QSGNodeVisitorEx']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGGlyphNode(QSGVisitableNode):
  """
  The cute side of Qt's QSGGlyphNode: a plain Python object standing in front
  of one C++ QSGGlyphNode.

  It is built on the cute 'QSGVisitableNode', as Qt's QSGGlyphNode is built
  on Qt's QSGVisitableNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGGlyphNode that has a ritual and that Python can
  call so far, 13 names in all: 'setGlyphs', 'setColor', 'setStyle',
  'setStyleColor', 'baseLine', 'boundingRect', 'setBoundingRect',
  'setPreferredAntialiasingMode', 'setRenderTypeQuality', 'renderType',
  'recycle', 'update', 'accept'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGGlyphNode::~QSGGlyphNode()': the destructor: Python never
    removes a C++ QSGGlyphNode.

  What to expect
  --------------

  - The C++ QSGGlyphNode is created at the first use, not by
    'QSGGlyphNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGGlyphNode.
  """

  #  The enums Qt writes inside QSGGlyphNode, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AntialiasingMode(CuteNum):
    """
    The enum 'QSGGlyphNode::AntialiasingMode' of Qt, with the 4 names Qt
    gives in it.
    """

    DefaultAntialiasing = Kee[int](-1)
    GrayAntialiasing = Kee[int](0)
    LowQualitySubPixelAntialiasing = Kee[int](1)
    HighQualitySubPixelAntialiasing = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGlyphNode'

  #  A C++ QSGGlyphNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGGlyphNode'

  #  The functions Qt calls itself that QSGGlyphNode is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setGlyphs': (
          ('_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtGui:QGlyphRun'),
           )),
      ),
      'setColor': (
          ('_ZN12QSGGlyphNode8setColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setStyle': (
          ('_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QQuickText.TextStyle'),
           )),
      ),
      'setStyleColor': (
          ('_ZN12QSGGlyphNode13setStyleColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'baseLine': (
          ('_ZNK12QSGGlyphNode8baseLineEv',
           ('address', 'value', 'QtCore:QPointF'),
           ()),
      ),
      'boundingRect': (
          ('_ZNK12QSGGlyphNode12boundingRectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'setBoundingRect': (
          ('_ZN12QSGGlyphNode15setBoundingRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setPreferredAntialiasingMode': (
          ('_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16Antialiasi'
           'ngModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGGlyphNode.AntialiasingMode'),
           )),
      ),
      'setRenderTypeQuality': (
          ('_ZN12QSGGlyphNode20setRenderTypeQualityEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'recycle': (
          ('_ZN12QSGGlyphNode7recycleEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'update': (
          ('_ZN12QSGGlyphNode6updateEv',
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

  def baseLine(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSGGlyphNode::baseLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#baseLine

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSGGlyphNode::baseLine() const
    address = self.uglySide.call('ritual_ZNK12QSGGlyphNode8baseLineEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGGlyphNode::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGGlyphNode::boundingRect() const
    ritual = 'ritual_ZNK12QSGGlyphNode12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QSGGlyphNode12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def renderType(self) -> QSGTextNode.RenderType:
    """
    Calls Qt's 'QSGTextNode::RenderType QSGGlyphNode::renderType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#renderType

    Returns
    -------

    QSGTextNode.RenderType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGTextNode.RenderType(number)' gives.
    """
    #  QSGTextNode::RenderType QSGGlyphNode::renderType() const
    return QSGTextNode.RenderType(self.uglySide.call(
        'ritual_ZNK12QSGGlyphNode10renderTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF, QGlyphRun)
  def setGlyphs(self, position: QPointF, glyphs: QGlyphRun) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::setGlyphs(const QPointF &position, const
    QGlyphRun &glyphs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#setGlyphs

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    glyphs : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  void QSGGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun
    #      &glyphs)
    self.uglySide.call(
        'ritual_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun',
        self._valueOf(position, 'QPointF'), self._valueOf(glyphs),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGGlyphNode::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN12QSGGlyphNode8setColorERK6QColor', self._valueOf(color),
    )

  @overload(QQuickText.TextStyle)
  def setStyle(self, style: QQuickText.TextStyle) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::setStyle(QQuickText::TextStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#setStyle

    Parameters
    ----------

    style : QQuickText.TextStyle
      Passed on as its number.
    """
    #  void QSGGlyphNode::setStyle(QQuickText::TextStyle style)
    self.uglySide.call(
        'ritual_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE',
        style.value,
    )

  @overload(QColor)
  def setStyleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::setStyleColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#setStyleColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGGlyphNode::setStyleColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN12QSGGlyphNode13setStyleColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QRectF)
  def setBoundingRect(self, bounds: QRectF) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::setBoundingRect(const QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#setBoundingRect

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
    ritual = 'ritual_ZN12QSGGlyphNode15setBoundingRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSGGlyphNode15setBoundingRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(bounds))

  @overload(AntialiasingMode)
  def setPreferredAntialiasingMode(self, a0: AntialiasingMode) -> None:
    """
    Calls Qt's 'void
    QSGGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgglyphnode.html#setPreferredAntialiasingMode

    Parameters
    ----------

    a0 : AntialiasingMode
      Passed on as its number.
    """
    #  void QSGGlyphNode::setPreferredAntialiasingMode(AntialiasingMode a0)
    self.uglySide.call(
        'ritual_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16Antiali'
        'asingModeE',
        a0.value,
    )

  @overload(int)
  def setRenderTypeQuality(self, renderTypeQuality: int) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::setRenderTypeQuality(int
    renderTypeQuality)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgglyphnode.html#setRenderTypeQuality

    Parameters
    ----------

    renderTypeQuality : int
      Passed on as it is.
    """
    #  void QSGGlyphNode::setRenderTypeQuality(int renderTypeQuality)
    ritual = 'ritual_ZN12QSGGlyphNode20setRenderTypeQualityEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSGGlyphNode20setRenderTypeQualityEi'
    self.uglySide.call(ritual, renderTypeQuality)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTextNode.RenderType)
  def __init__(self, renderType: QSGTextNode.RenderType) -> None:
    """
    Notes what was given, for Qt's
    'QSGGlyphNode::QSGGlyphNode(QSGTextNode::RenderType renderType)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#QSGGlyphNode

    Parameters
    ----------

    renderType : QSGTextNode.RenderType
      Passed on as its number.
    """
    #  QSGGlyphNode::QSGGlyphNode(QSGTextNode::RenderType renderType)
    self._noteCreation(QSGGlyphNode, lambda: Rituals.call(
        'ritual_ZN12QSGGlyphNodeC1EN11QSGTextNode10RenderTypeE',
        renderType.value,
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

  def recycle(self) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::recycle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#recycle
    """
    #  void QSGGlyphNode::recycle()
    ritual = 'ritual_ZN12QSGGlyphNode7recycleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSGGlyphNode7recycleEv'
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#update
    """
    #  void QSGGlyphNode::update()
    self.uglySide.call('ritual_ZN12QSGGlyphNode6updateEv')

  @overload(QSGNodeVisitorEx)
  @overload(NoneType)
  def accept(self, visitor: Optional[QSGNodeVisitorEx]) -> None:
    """
    Calls Qt's 'void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgglyphnode.html#accept

    Parameters
    ----------

    visitor : Optional[QSGNodeVisitorEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
    ritual = 'ritual_ZN12QSGGlyphNode6acceptEP16QSGNodeVisitorEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSGGlyphNode6acceptEP16QSGNodeVisitorEx'
    self.uglySide.call(ritual, self._addressOf(visitor))
