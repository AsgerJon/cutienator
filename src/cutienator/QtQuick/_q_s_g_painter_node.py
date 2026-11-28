"""
QSGPainterNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGPainterNode to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickPaintedItem, QSGVisitableNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QColor, QImage
  from . import QSGNodeVisitorEx, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRect = WAIT['QRect']
  QSGNodeVisitorEx = WAIT['QSGNodeVisitorEx']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGPainterNode(QSGVisitableNode):
  """
  The cute side of Qt's QSGPainterNode: a plain Python object standing in
  front of one C++ QSGPainterNode.

  It is built on the cute 'QSGVisitableNode', as Qt's QSGPainterNode is built
  on Qt's QSGVisitableNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGPainterNode that has a ritual and that Python can
  call so far, 15 names in all: 'setPreferredRenderTarget', 'setSize',
  'setDirty', 'setOpaquePainting', 'setLinearFiltering', 'setMipmapping',
  'setSmoothPainting', 'setFillColor', 'setContentsScale',
  'setFastFBOResizing', 'setTextureSize', 'toImage', 'update', 'texture',
  'accept'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGPainterNode::~QSGPainterNode()': the destructor: Python never
    removes a C++ QSGPainterNode.

  What to expect
  --------------

  - The C++ QSGPainterNode is created at the first use, not by
    'QSGPainterNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGPainterNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGPainterNode'

  #  A C++ QSGPainterNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGPainterNode'

  #  The functions Qt calls itself that QSGPainterNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setPreferredRenderTarget': (
          ('_ZN14QSGPainterNode24setPreferredRenderTargetEN17QQuickPaintedI'
           'tem12RenderTargetE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QQuickPaintedItem.RenderTarget'),
           )),
      ),
      'setSize': (
          ('_ZN14QSGPainterNode7setSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'setDirty': (
          ('_ZN14QSGPainterNode8setDirtyERK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'setOpaquePainting': (
          ('_ZN14QSGPainterNode17setOpaquePaintingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setLinearFiltering': (
          ('_ZN14QSGPainterNode18setLinearFilteringEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setMipmapping': (
          ('_ZN14QSGPainterNode13setMipmappingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setSmoothPainting': (
          ('_ZN14QSGPainterNode17setSmoothPaintingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setFillColor': (
          ('_ZN14QSGPainterNode12setFillColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setContentsScale': (
          ('_ZN14QSGPainterNode16setContentsScaleEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setFastFBOResizing': (
          ('_ZN14QSGPainterNode18setFastFBOResizingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setTextureSize': (
          ('_ZN14QSGPainterNode14setTextureSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'toImage': (
          ('_ZNK14QSGPainterNode7toImageEv',
           ('address', 'value', 'QtGui:QImage'),
           ()),
      ),
      'update': (
          ('_ZN14QSGPainterNode6updateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'texture': (
          ('_ZNK14QSGPainterNode7textureEv',
           ('address', 'address', 'QtQuick:QSGTexture'),
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

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QSGPainterNode::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGPainterNode::toImage() const
    address = self.uglySide.call('ritual_ZNK14QSGPainterNode7toImageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGPainterNode::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGPainterNode::texture() const
    address = self.uglySide.call('ritual_ZNK14QSGPainterNode7textureEv')
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPaintedItem.RenderTarget)
  def setPreferredRenderTarget(
      self,
      target: QQuickPaintedItem.RenderTarget,
  ) -> None:
    """
    Calls Qt's 'void
    QSGPainterNode::setPreferredRenderTarget(QQuickPaintedItem::RenderTarget
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgpainternode.html#setPreferredRenderTarget

    Parameters
    ----------

    target : QQuickPaintedItem.RenderTarget
      Passed on as its number.
    """
    #  void QSGPainterNode::setPreferredRenderTarget(QQuickPaintedItem::
    #      RenderTarget target)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode24setPreferredRenderTargetEN17QQuickPaint'
        'edItem12RenderTargetE',
        target.value,
    )

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGPainterNode::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode7setSizeERK5QSize', self._valueOf(size),
    )

  @overload()
  @overload(QRect)
  def setDirty(self, dirtyRect: Optional[QRect] = None) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setDirty(const QRect &dirtyRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#setDirty

    Parameters
    ----------

    dirtyRect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QSGPainterNode::setDirty(const QRect &dirtyRect)
    if dirtyRect is None:
      from ..QtCore import QRect
      dirtyRect = QRect()
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode8setDirtyERK5QRect',
        self._valueOf(dirtyRect),
    )

  @overload(bool)
  def setOpaquePainting(self, opaque: bool) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setOpaquePainting(bool opaque)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgpainternode.html#setOpaquePainting

    Parameters
    ----------

    opaque : bool
      Passed on as it is.
    """
    #  void QSGPainterNode::setOpaquePainting(bool opaque)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode17setOpaquePaintingEb', opaque,
    )

  @overload(bool)
  def setLinearFiltering(self, linearFiltering: bool) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setLinearFiltering(bool
    linearFiltering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgpainternode.html#setLinearFiltering

    Parameters
    ----------

    linearFiltering : bool
      Passed on as it is.
    """
    #  void QSGPainterNode::setLinearFiltering(bool linearFiltering)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode18setLinearFilteringEb', linearFiltering,
    )

  @overload(bool)
  def setMipmapping(self, mipmapping: bool) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setMipmapping(bool mipmapping)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#setMipmapping

    Parameters
    ----------

    mipmapping : bool
      Passed on as it is.
    """
    #  void QSGPainterNode::setMipmapping(bool mipmapping)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode13setMipmappingEb', mipmapping,
    )

  @overload(bool)
  def setSmoothPainting(self, s: bool) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setSmoothPainting(bool s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgpainternode.html#setSmoothPainting

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QSGPainterNode::setSmoothPainting(bool s)
    self.uglySide.call('ritual_ZN14QSGPainterNode17setSmoothPaintingEb', s)

  @overload(QColor)
  def setFillColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setFillColor(const QColor &c)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#setFillColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGPainterNode::setFillColor(const QColor &c)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode12setFillColorERK6QColor',
        self._valueOf(c),
    )

  @overload(float)
  def setContentsScale(self, s: float) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setContentsScale(qreal s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgpainternode.html#setContentsScale

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QSGPainterNode::setContentsScale(qreal s)
    self.uglySide.call('ritual_ZN14QSGPainterNode16setContentsScaleEd', s)

  @overload(bool)
  def setFastFBOResizing(self, dynamic: bool) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setFastFBOResizing(bool dynamic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgpainternode.html#setFastFBOResizing

    Parameters
    ----------

    dynamic : bool
      Passed on as it is.
    """
    #  void QSGPainterNode::setFastFBOResizing(bool dynamic)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode18setFastFBOResizingEb', dynamic,
    )

  @overload(QSize)
  def setTextureSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGPainterNode::setTextureSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#setTextureSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGPainterNode::setTextureSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN14QSGPainterNode14setTextureSizeERK5QSize',
        self._valueOf(size),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'void QSGPainterNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#update
    """
    #  void QSGPainterNode::update()
    self.uglySide.call('ritual_ZN14QSGPainterNode6updateEv')

  @overload(QSGNodeVisitorEx)
  @overload(NoneType)
  def accept(self, visitor: Optional[QSGNodeVisitorEx]) -> None:
    """
    Calls Qt's 'void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgpainternode.html#accept

    Parameters
    ----------

    visitor : Optional[QSGNodeVisitorEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)
    ritual = 'ritual_ZN14QSGPainterNode6acceptEP16QSGNodeVisitorEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSGPainterNode6acceptEP16QSGNodeVisitorEx'
    self.uglySide.call(ritual, self._addressOf(visitor))
