"""
QSGDefaultSpriteNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultspritenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDefaultSpriteNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGSpriteNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QSize, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDefaultSpriteNode(QSGSpriteNode):
  """
  The cute side of Qt's QSGDefaultSpriteNode: a plain Python object standing
  in front of one C++ QSGDefaultSpriteNode.

  It is built on the cute 'QSGSpriteNode', as Qt's QSGDefaultSpriteNode is
  built on Qt's QSGSpriteNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultSpriteNode that has a ritual and that
  Python can call so far, 9 names in all: 'setTexture', 'setTime',
  'setSourceA', 'setSourceB', 'setSpriteSize', 'setSheetSize', 'setSize',
  'setFiltering', 'update'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSGDefaultSpriteNode is created at the first use, not by
    'QSGDefaultSpriteNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultSpriteNode.
  - Each name of Qt's QSGDefaultSpriteNode that has no cute function yet,
    '__init__', 'updateGeometry', holds a function that raises
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
  __qt_class__ = 'QSGDefaultSpriteNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultSpriteNode::setTexture(QSGTexture *texture)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode10setTextureEP10QSGTexture'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGDefaultSpriteNode10setTextureEP10QSGTexture')
    self.uglySide.call(ritual, self._addressOf(texture))

  @overload(float)
  def setTime(self, time: float) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setTime(float time)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setTime

    Parameters
    ----------

    time : float
      Passed on as it is.
    """
    #  void QSGDefaultSpriteNode::setTime(float time)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode7setTimeEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGDefaultSpriteNode7setTimeEf'
    self.uglySide.call(ritual, time)

  @overload(QPoint)
  def setSourceA(self, source: QPoint) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setSourceA(const QPoint &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setSourceA

    Parameters
    ----------

    source : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSGDefaultSpriteNode::setSourceA(const QPoint &source)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode10setSourceAERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGDefaultSpriteNode10setSourceAERK6QPoint'
    self.uglySide.call(ritual, self._valueOf(source))

  @overload(QPoint)
  def setSourceB(self, source: QPoint) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setSourceB(const QPoint &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setSourceB

    Parameters
    ----------

    source : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSGDefaultSpriteNode::setSourceB(const QPoint &source)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode10setSourceBERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGDefaultSpriteNode10setSourceBERK6QPoint'
    self.uglySide.call(ritual, self._valueOf(source))

  @overload(QSize)
  def setSpriteSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setSpriteSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setSpriteSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGDefaultSpriteNode::setSpriteSize(const QSize &size)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode13setSpriteSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGDefaultSpriteNode13setSpriteSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QSize)
  def setSheetSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setSheetSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setSheetSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGDefaultSpriteNode::setSheetSize(const QSize &size)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode12setSheetSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGDefaultSpriteNode12setSheetSizeERK5QSize'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QSizeF)
  def setSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QSGDefaultSpriteNode::setSize(const QSizeF &size)
    ritual = 'ritual_ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGDefaultSpriteNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultspritenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGDefaultSpriteNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN20QSGDefaultSpriteNode12setFilteringEN10QSGTexture9Filter'
        'ingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGDefaultSpriteNode12setFilteringEN10QSGTexture9'
          'FilteringE')
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
    Qt's 'QSGDefaultSpriteNode::QSGDefaultSpriteNode()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'Sprite_AttributeSet'.
    """
    raise NotImplementedError(
        "'QSGDefaultSpriteNode.__init__' has no cute function yet. Qt's "
        "'QSGDefaultSpriteNode::QSGDefaultSpriteNode()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'Sprite_AttributeSet'.")

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
    Calls Qt's 'void QSGDefaultSpriteNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgdefaultspritenode.html#update
    """
    #  void QSGDefaultSpriteNode::update()
    self.uglySide.call('ritual_ZN20QSGDefaultSpriteNode6updateEv')

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void QSGDefaultSpriteNode::updateGeometry()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickSpriteMaterial'.
    """
    raise NotImplementedError(
        "'QSGDefaultSpriteNode.updateGeometry' has no cute function yet. "
        "Qt's 'void QSGDefaultSpriteNode::updateGeometry()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickSpriteMaterial'.")
