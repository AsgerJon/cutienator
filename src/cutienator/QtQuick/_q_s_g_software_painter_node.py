"""
QSGSoftwarePainterNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepainternode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwarePainterNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickPaintedItem, QSGPainterNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QColor, QImage, QPainter
  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwarePainterNode(QSGPainterNode):
  """
  The cute side of Qt's QSGSoftwarePainterNode: a plain Python object
  standing in front of one C++ QSGSoftwarePainterNode.

  It is built on the cute 'QSGPainterNode', as Qt's QSGSoftwarePainterNode is
  built on Qt's QSGPainterNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwarePainterNode that has a ritual and that
  Python can call so far, 24 names in all: 'setPreferredRenderTarget',
  'setSize', 'size', 'setDirty', 'setOpaquePainting', 'opaquePainting',
  'setLinearFiltering', 'linearFiltering', 'setMipmapping', 'mipmapping',
  'setSmoothPainting', 'smoothPainting', 'setFillColor', 'fillColor',
  'setContentsScale', 'contentsScale', 'setFastFBOResizing',
  'fastFBOResizing', 'toImage', 'update', 'texture', 'paint',
  'setTextureSize', 'textureSize'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwarePainterNode::~QSGSoftwarePainterNode()': the destructor:
    Python never removes a C++ QSGSoftwarePainterNode.

  What has no ritual
  ------------------

  1 of the 27 functions Qt declares: 1 leans on 'vtable for
  QSGSoftwarePixmapTexture', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QSGSoftwarePainterNode is created at the first use, not by
    'QSGSoftwarePainterNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwarePainterNode.
  - Each name of Qt's QSGSoftwarePainterNode that has no cute function yet,
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
  __qt_class__ = 'QSGSoftwarePainterNode'

  #  A C++ QSGSoftwarePainterNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwarePainterNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSGSoftwarePainterNode::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGSoftwarePainterNode::size() const
    address = self.uglySide.call('ritual_ZNK22QSGSoftwarePainterNode4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def opaquePainting(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePainterNode::opaquePainting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#opaquePainting
    """
    #  bool QSGSoftwarePainterNode::opaquePainting() const
    return self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode14opaquePaintingEv',
    )

  def linearFiltering(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePainterNode::linearFiltering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#linearFiltering
    """
    #  bool QSGSoftwarePainterNode::linearFiltering() const
    return self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode15linearFilteringEv',
    )

  def mipmapping(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePainterNode::mipmapping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#mipmapping
    """
    #  bool QSGSoftwarePainterNode::mipmapping() const
    return self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode10mipmappingEv',
    )

  def smoothPainting(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePainterNode::smoothPainting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#smoothPainting
    """
    #  bool QSGSoftwarePainterNode::smoothPainting() const
    return self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode14smoothPaintingEv',
    )

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSGSoftwarePainterNode::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGSoftwarePainterNode::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def contentsScale(self) -> float:
    """
    Calls Qt's 'qreal QSGSoftwarePainterNode::contentsScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#contentsScale
    """
    #  qreal QSGSoftwarePainterNode::contentsScale() const
    return self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode13contentsScaleEv',
    )

  def fastFBOResizing(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwarePainterNode::fastFBOResizing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#fastFBOResizing
    """
    #  bool QSGSoftwarePainterNode::fastFBOResizing() const
    return self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode15fastFBOResizingEv',
    )

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QSGSoftwarePainterNode::toImage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGSoftwarePainterNode::toImage() const
    ritual = 'ritual_ZNK22QSGSoftwarePainterNode7toImageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QSGSoftwarePainterNode7toImageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def texture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGSoftwarePainterNode::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#texture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGSoftwarePainterNode::texture() const
    ritual = 'ritual_ZNK22QSGSoftwarePainterNode7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QSGSoftwarePainterNode7textureEv'
    address = self.uglySide.call(ritual)
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize QSGSoftwarePainterNode::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGSoftwarePainterNode::textureSize() const
    address = self.uglySide.call(
        'ritual_ZNK22QSGSoftwarePainterNode11textureSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
    QSGSoftwarePainterNode::setPreferredRenderTarget(QQuickPaintedItem::
    RenderTarget target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html

    Parameters
    ----------

    target : QQuickPaintedItem.RenderTarget
      Passed on as its number.
    """
    #  void QSGSoftwarePainterNode::setPreferredRenderTarget(
    #      QQuickPaintedItem::RenderTarget target)
    ritual = (
        'ritual_ZN22QSGSoftwarePainterNode24setPreferredRenderTargetEN17QQu'
        'ickPaintedItem12RenderTargetE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSGSoftwarePainterNode24setPreferredRenderTargetE'
          'N17QQuickPaintedItem12RenderTargetE')
    self.uglySide.call(ritual, target.value)

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSoftwarePainterNode::setSize(const QSize &size)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode7setSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode7setSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload()
  @overload(QRect)
  def setDirty(self, dirtyRect: Optional[QRect] = None) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setDirty(const QRect
    &dirtyRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setDirty

    Parameters
    ----------

    dirtyRect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.
    """
    #  void QSGSoftwarePainterNode::setDirty(const QRect &dirtyRect)
    if dirtyRect is None:
      from ..QtCore import QRect
      dirtyRect = QRect()
    ritual = 'ritual_ZN22QSGSoftwarePainterNode8setDirtyERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode8setDirtyERK5QRect'
    self.uglySide.call(ritual, self._valueOf(dirtyRect))

  @overload(bool)
  def setOpaquePainting(self, opaque: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setOpaquePainting

    Parameters
    ----------

    opaque : bool
      Passed on as it is.
    """
    #  void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode17setOpaquePaintingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode17setOpaquePaintingEb'
    self.uglySide.call(ritual, opaque)

  @overload(bool)
  def setLinearFiltering(self, linearFiltering: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setLinearFiltering(bool
    linearFiltering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setLinearFiltering

    Parameters
    ----------

    linearFiltering : bool
      Passed on as it is.
    """
    #  void QSGSoftwarePainterNode::setLinearFiltering(bool linearFiltering)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode18setLinearFilteringEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode18setLinearFilteringEb'
    self.uglySide.call(ritual, linearFiltering)

  @overload(bool)
  def setMipmapping(self, mipmapping: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setMipmapping

    Parameters
    ----------

    mipmapping : bool
      Passed on as it is.
    """
    #  void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode13setMipmappingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode13setMipmappingEb'
    self.uglySide.call(ritual, mipmapping)

  @overload(bool)
  def setSmoothPainting(self, s: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setSmoothPainting(bool s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setSmoothPainting

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QSGSoftwarePainterNode::setSmoothPainting(bool s)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode17setSmoothPaintingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode17setSmoothPaintingEb'
    self.uglySide.call(ritual, s)

  @overload(QColor)
  def setFillColor(self, c: QColor) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setFillColor(const QColor &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setFillColor

    Parameters
    ----------

    c : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSoftwarePainterNode::setFillColor(const QColor &c)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode12setFillColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSGSoftwarePainterNode12setFillColorERK6QColor')
    self.uglySide.call(ritual, self._valueOf(c))

  @overload(float)
  def setContentsScale(self, s: float) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setContentsScale(qreal s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setContentsScale

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QSGSoftwarePainterNode::setContentsScale(qreal s)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode16setContentsScaleEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode16setContentsScaleEd'
    self.uglySide.call(ritual, s)

  @overload(bool)
  def setFastFBOResizing(self, dynamic: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setFastFBOResizing(bool
    dynamic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setFastFBOResizing

    Parameters
    ----------

    dynamic : bool
      Passed on as it is.
    """
    #  void QSGSoftwarePainterNode::setFastFBOResizing(bool dynamic)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode18setFastFBOResizingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGSoftwarePainterNode18setFastFBOResizingEb'
    self.uglySide.call(ritual, dynamic)

  @overload(QSize)
  def setTextureSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::setTextureSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#setTextureSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSoftwarePainterNode::setTextureSize(const QSize &size)
    ritual = 'ritual_ZN22QSGSoftwarePainterNode14setTextureSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSGSoftwarePainterNode14setTextureSizeERK5QSize')
    self.uglySide.call(ritual, self._valueOf(size))

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
    Qt's 'QSGSoftwarePainterNode::QSGSoftwarePainterNode(QQuickPaintedItem
    *item)': leans on 'vtable for QSGSoftwarePixmapTexture', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwarePainterNode.__init__' has no cute function yet. Qt's "
        "'QSGSoftwarePainterNode::QSGSoftwarePainterNode(QQuickPaintedItem "
        "*item)': leans on 'vtable for QSGSoftwarePixmapTexture', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void QSGSoftwarePainterNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#update
    """
    #  void QSGSoftwarePainterNode::update()
    self.uglySide.call('ritual_ZN22QSGSoftwarePainterNode6updateEv')

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwarePainterNode::paint(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN22QSGSoftwarePainterNode5paintEP8QPainter',
        self._addressOf(painter),
    )

  @overload()
  def paint(self) -> None:
    """
    Calls Qt's 'void QSGSoftwarePainterNode::paint()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarepainternode.html#paint
    """
    #  void QSGSoftwarePainterNode::paint()
    self.uglySide.call('ritual_ZN22QSGSoftwarePainterNode5paintEv')
