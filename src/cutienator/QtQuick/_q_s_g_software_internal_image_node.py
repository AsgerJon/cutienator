"""
QSGSoftwareInternalImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalimagenode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGSoftwareInternalImageNode to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGInternalImageNode, QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareInternalImageNode(QSGInternalImageNode):
  """
  The cute side of Qt's QSGSoftwareInternalImageNode: a plain Python object
  standing in front of one C++ QSGSoftwareInternalImageNode.

  It is built on the cute 'QSGInternalImageNode', as Qt's
  QSGSoftwareInternalImageNode is built on Qt's QSGInternalImageNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareInternalImageNode that has a ritual and
  that Python can call so far, 13 names in all: 'setTargetRect',
  'setInnerTargetRect', 'setInnerSourceRect', 'setSubSourceRect',
  'setTexture', 'setMirror', 'setMipmapFiltering', 'setFiltering',
  'setHorizontalWrapMode', 'setVerticalWrapMode', 'update', 'preprocess',
  'rect'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 leans on 'QSGSoftwareLayer.

  What to expect
  --------------

  - The C++ QSGSoftwareInternalImageNode is created at the first use, not by
    'QSGSoftwareInternalImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareInternalImageNode.
  - Each name of Qt's QSGSoftwareInternalImageNode that has no cute function
    yet, '__init__', 'paint', 'pixmap', 'updateCachedMirroredPixmap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareInternalImageNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareInternalImageNode::rect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareInternalImageNode::rect() const
    address = self.uglySide.call(
        'ritual_ZNK28QSGSoftwareInternalImageNode4rectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setTargetRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::setTargetRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#setTargetRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalImageNode::setTargetRect(const QRectF &rect)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode13setTargetRectERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode13setTargetRectERK6QR'
          'ectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setInnerTargetRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::setInnerTargetRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalImageNode::setInnerTargetRect(const QRectF
    #      &rect)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode18setInnerTargetRectERK6QRe'
        'ctF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode18setInnerTargetRectE'
          'RK6QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setInnerSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::setInnerSourceRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalImageNode::setInnerSourceRect(const QRectF
    #      &rect)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode18setInnerSourceRectERK6QRe'
        'ctF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode18setInnerSourceRectE'
          'RK6QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setSubSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::setSubSourceRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#setSubSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalImageNode::setSubSourceRect(const QRectF
    #      &rect)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode16setSubSourceRectERK6QRect'
        'F')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode16setSubSourceRectERK'
          '6QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareInternalImageNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN28QSGSoftwareInternalImageNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(bool, bool)
  def setMirror(
      self,
      mirrorHorizontally: bool,
      mirrorVertically: bool,
  ) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::setMirror(bool
    mirrorHorizontally, bool mirrorVertically)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#setMirror

    Parameters
    ----------

    mirrorHorizontally : bool
      Passed on as it is.

    mirrorVertically : bool
      Passed on as it is.
    """
    #  void QSGSoftwareInternalImageNode::setMirror(bool mirrorHorizontally,
    #      bool mirrorVertically)
    ritual = 'ritual_ZN28QSGSoftwareInternalImageNode9setMirrorEbb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QSGSoftwareInternalImageNode9setMirrorEbb'
    self.uglySide.call(ritual, mirrorHorizontally, mirrorVertically)

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSoftwareInternalImageNode::setMipmapFiltering(QSGTexture::
    #      Filtering filtering)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode18setMipmapFilteringEN10QSG'
        'Texture9FilteringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode18setMipmapFilteringE'
          'N10QSGTexture9FilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalImageNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGSoftwareInternalImageNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode12setFilteringEN10QSGTextur'
        'e9FilteringE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode12setFilteringEN10QSG'
          'Texture9FilteringE')
    self.uglySide.call(ritual, filtering.value)

  @overload(QSGTexture.WrapMode)
  def setHorizontalWrapMode(self, wrapMode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html

    Parameters
    ----------

    wrapMode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGSoftwareInternalImageNode::setHorizontalWrapMode(QSGTexture::
    #      WrapMode wrapMode)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode21setHorizontalWrapModeEN10'
        'QSGTexture8WrapModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode21setHorizontalWrapMo'
          'deEN10QSGTexture8WrapModeE')
    self.uglySide.call(ritual, wrapMode.value)

  @overload(QSGTexture.WrapMode)
  def setVerticalWrapMode(self, wrapMode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html

    Parameters
    ----------

    wrapMode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGSoftwareInternalImageNode::setVerticalWrapMode(QSGTexture::
    #      WrapMode wrapMode)
    ritual = (
        'ritual_ZN28QSGSoftwareInternalImageNode19setVerticalWrapModeEN10QS'
        'GTexture8WrapModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSGSoftwareInternalImageNode19setVerticalWrapMode'
          'EN10QSGTexture8WrapModeE')
    self.uglySide.call(ritual, wrapMode.value)

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
    Qt's 'QSGSoftwareInternalImageNode::QSGSoftwareInternalImageNode()':
    leans on 'QSGSoftwareLayer::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareInternalImageNode.__init__' has no cute function yet. "
        "Qt's "
        "'QSGSoftwareInternalImageNode::QSGSoftwareInternalImageNode()': "
        "leans on 'QSGSoftwareLayer::staticMetaObject', which Qt's source "
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
    Calls Qt's 'void QSGSoftwareInternalImageNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#update
    """
    #  void QSGSoftwareInternalImageNode::update()
    self.uglySide.call('ritual_ZN28QSGSoftwareInternalImageNode6updateEv')

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalImageNode::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalimagenode.html#preprocess
    """
    #  void QSGSoftwareInternalImageNode::preprocess()
    ritual = 'ritual_ZN28QSGSoftwareInternalImageNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QSGSoftwareInternalImageNode10preprocessEv'
    self.uglySide.call(ritual)

  @staticmethod
  def paint(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareInternalImageNode::paint(QPainter *painter)': leans
    on 'QSGSoftwareLayer::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareInternalImageNode.paint' has no cute function yet. "
        "Qt's 'void QSGSoftwareInternalImageNode::paint(QPainter "
        "*painter)': leans on 'QSGSoftwareLayer::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def pixmap(*__, **_) -> Never:
    """
    Qt's 'const QPixmap &QSGSoftwareInternalImageNode::pixmap() const': leans
    on 'QSGSoftwareLayer::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareInternalImageNode.pixmap' has no cute function yet. "
        "Qt's 'const QPixmap &QSGSoftwareInternalImageNode::pixmap() "
        "const': leans on 'QSGSoftwareLayer::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateCachedMirroredPixmap(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareInternalImageNode::updateCachedMirroredPixmap()':
    leans on 'QSGSoftwareLayer::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareInternalImageNode.updateCachedMirroredPixmap' has no "
        "cute function yet. Qt's 'void "
        "QSGSoftwareInternalImageNode::updateCachedMirroredPixmap()': leans "
        "on 'QSGSoftwareLayer::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
