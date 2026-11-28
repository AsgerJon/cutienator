"""
QSGSoftwareSpriteNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarespritenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareSpriteNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGSpriteNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRectF, QSize, QSizeF
  from ..QtGui import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareSpriteNode(QSGSpriteNode):
  """
  The cute side of Qt's QSGSoftwareSpriteNode: a plain Python object standing
  in front of one C++ QSGSoftwareSpriteNode.

  It is built on the cute 'QSGSpriteNode', as Qt's QSGSoftwareSpriteNode is
  built on Qt's QSGSpriteNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareSpriteNode that has a ritual and that
  Python can call so far, 12 names in all: 'setTexture', 'setTime',
  'setSourceA', 'setSourceB', 'setSpriteSize', 'setSheetSize', 'setSize',
  'setFiltering', 'update', 'paint', 'isOpaque', 'rect'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwareSpriteNode::~QSGSoftwareSpriteNode()': the destructor:
    Python never removes a C++ QSGSoftwareSpriteNode.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 leans on 'QSGSoftwarePixmapTexture.

  What to expect
  --------------

  - The C++ QSGSoftwareSpriteNode is created at the first use, not by
    'QSGSoftwareSpriteNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareSpriteNode.
  - Each name of Qt's QSGSoftwareSpriteNode that has no cute function yet,
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
  __qt_class__ = 'QSGSoftwareSpriteNode'

  #  A C++ QSGSoftwareSpriteNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareSpriteNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareSpriteNode::isOpaque() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#isOpaque
    """
    #  bool QSGSoftwareSpriteNode::isOpaque() const
    return self.uglySide.call('ritual_ZNK21QSGSoftwareSpriteNode8isOpaqueEv')

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareSpriteNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareSpriteNode::rect() const
    address = self.uglySide.call('ritual_ZNK21QSGSoftwareSpriteNode4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareSpriteNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN21QSGSoftwareSpriteNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(float)
  def setTime(self, time: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setTime(float time)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setTime

    Parameters
    ----------

    time : float
      Passed on as it is.
    """
    #  void QSGSoftwareSpriteNode::setTime(float time)
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode7setTimeEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode7setTimeEf'
    self.uglySide.call(ritual, time)

  @overload(QPoint)
  def setSourceA(self, source: QPoint) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setSourceA(const QPoint
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setSourceA

    Parameters
    ----------

    source : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSGSoftwareSpriteNode::setSourceA(const QPoint &source)
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode10setSourceAERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode10setSourceAERK6QPoint'
    self.uglySide.call(ritual, self._valueOf(source))

  @overload(QPoint)
  def setSourceB(self, source: QPoint) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setSourceB(const QPoint
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setSourceB

    Parameters
    ----------

    source : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSGSoftwareSpriteNode::setSourceB(const QPoint &source)
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode10setSourceBERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode10setSourceBERK6QPoint'
    self.uglySide.call(ritual, self._valueOf(source))

  @overload(QSize)
  def setSpriteSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setSpriteSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setSpriteSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSoftwareSpriteNode::setSpriteSize(const QSize &size)
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode13setSpriteSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode13setSpriteSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QSize)
  def setSheetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setSheetSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode12setSheetSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode12setSheetSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QSGSoftwareSpriteNode::setSize(const QSizeF &size)
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode7setSizeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode7setSizeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN21QSGSoftwareSpriteNode12setFilteringEN10QSGTexture9Filte'
        'ringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGSoftwareSpriteNode12setFilteringEN10QSGTexture'
          '9FilteringE')
    self.uglySide.call(ritual, filtering.value)

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
    Qt's 'QSGSoftwareSpriteNode::QSGSoftwareSpriteNode()': leans on
    'QSGSoftwarePixmapTexture::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareSpriteNode.__init__' has no cute function yet. Qt's "
        "'QSGSoftwareSpriteNode::QSGSoftwareSpriteNode()': leans on "
        "'QSGSoftwarePixmapTexture::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void QSGSoftwareSpriteNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#update
    """
    #  void QSGSoftwareSpriteNode::update()
    ritual = 'ritual_ZN21QSGSoftwareSpriteNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareSpriteNode6updateEv'
    self.uglySide.call(ritual)

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSGSoftwareSpriteNode::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarespritenode.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareSpriteNode::paint(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN21QSGSoftwareSpriteNode5paintEP8QPainter',
        self._addressOf(painter),
    )
