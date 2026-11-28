"""
QSGBasicInternalImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbasicinternalimagenode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGBasicInternalImageNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QSGInternalImageNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSize
  from . import QSGGeometry, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']
  QSGTexture = WAIT['QSGTexture']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGBasicInternalImageNode(QSGInternalImageNode):
  """
  The cute side of Qt's QSGBasicInternalImageNode: a plain Python object
  standing in front of one C++ QSGBasicInternalImageNode.

  It is built on the cute 'QSGInternalImageNode', as Qt's
  QSGBasicInternalImageNode is built on Qt's QSGInternalImageNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGBasicInternalImageNode that has a ritual and that
  Python can call so far, 15 names in all: 'setTargetRect',
  'setInnerTargetRect', 'setInnerSourceRect', 'setSubSourceRect',
  'setTexture', 'setAntialiasing', 'setMirror', 'update', 'preprocess',
  'updateGeometry', 'updateMaterialAntialiasing', 'setMaterialTexture',
  'materialTexture', 'updateMaterialBlending', 'supportsWrap'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGBasicInternalImageNode is created at the first use, not by
    'QSGBasicInternalImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBasicInternalImageNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRectF, QRectF, QRectF, QRectF, QRectF, QSGGeometry)
  @overload(QRectF, QRectF, QRectF, QRectF, QRectF, NoneType)
  @overload(QRectF, QRectF, QRectF, QRectF, QRectF, QSGGeometry, bool)
  @overload(QRectF, QRectF, QRectF, QRectF, QRectF, NoneType, bool)
  @overload(QRectF, QRectF, QRectF, QRectF, QRectF, QSGGeometry, bool, bool)
  @overload(QRectF, QRectF, QRectF, QRectF, QRectF, NoneType, bool, bool)
  @overload(
      QRectF, QRectF, QRectF, QRectF, QRectF, QSGGeometry, bool, bool, bool,
  )
  @overload(
      QRectF, QRectF, QRectF, QRectF, QRectF, NoneType, bool, bool, bool,
  )
  def updateGeometry(
      targetRect: QRectF,
      innerTargetRect: QRectF,
      sourceRect: QRectF,
      innerSourceRect: QRectF,
      subSourceRect: QRectF,
      geometry: Optional[QSGGeometry],
      mirrorHorizontally: bool = False,
      mirrorVertically: bool = False,
      antialiasing: bool = False,
  ) -> Optional[QSGGeometry]:
    """
    Calls Qt's 'QSGGeometry *QSGBasicInternalImageNode::updateGeometry(const
    QRectF &targetRect, const QRectF &innerTargetRect, const QRectF
    &sourceRect, const QRectF &innerSourceRect, const QRectF &subSourceRect,
    QSGGeometry *geometry, bool mirrorHorizontally, bool mirrorVertically,
    bool antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#updateGeometry

    Parameters
    ----------

    targetRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    innerTargetRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    innerSourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    subSourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    geometry : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mirrorHorizontally : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    mirrorVertically : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    antialiasing : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QSGGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGeometry *QSGBasicInternalImageNode::updateGeometry(const QRectF
    #      &targetRect, const QRectF &innerTargetRect, const QRectF
    #      &sourceRect, const QRectF &innerSourceRect, const QRectF
    #      &subSourceRect, QSGGeometry *geometry, bool mirrorHorizontally,
    #      bool mirrorVertically, bool antialiasing)
    address = Rituals.call(
        'ritual_ZN25QSGBasicInternalImageNode14updateGeometryERK6QRectFS2_S'
        '2_S2_S2_P11QSGGeometrybbb',
        CuteMixin._valueOf(targetRect), CuteMixin._valueOf(innerTargetRect),
        CuteMixin._valueOf(sourceRect), CuteMixin._valueOf(innerSourceRect),
        CuteMixin._valueOf(subSourceRect), CuteMixin._addressOf(geometry),
        mirrorHorizontally, mirrorVertically, antialiasing,
    )
    from . import QSGGeometry
    return QSGGeometry._cuteAt(address)

  @overload()
  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#updateGeometry
    """
    #  void QSGBasicInternalImageNode::updateGeometry()
    self.uglySide.call(
        'ritual_ZN25QSGBasicInternalImageNode14updateGeometryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBasicInternalImageNode'

  #  A C++ QSGBasicInternalImageNode Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBasicInternalImageNode'

  #  The functions Qt calls itself that QSGBasicInternalImageNode is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'updateMaterialAntialiasing': (
          ('_ZN25QSGBasicInternalImageNode26updateMaterialAntialiasingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setMaterialTexture': (
          ('_ZN25QSGBasicInternalImageNode18setMaterialTextureEP10QSGTextur'
           'e',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTexture'),
           )),
      ),
      'materialTexture': (
          ('_ZNK25QSGBasicInternalImageNode15materialTextureEv',
           ('address', 'address', 'QtQuick:QSGTexture'),
           ()),
      ),
      'updateMaterialBlending': (
          ('_ZN25QSGBasicInternalImageNode22updateMaterialBlendingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'supportsWrap': (
          ('_ZNK25QSGBasicInternalImageNode12supportsWrapERK5QSize',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def materialTexture(self) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture *QSGBasicInternalImageNode::materialTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#materialTexture

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture *QSGBasicInternalImageNode::materialTexture() const
    address = self.uglySide.call(
        'ritual_ZNK25QSGBasicInternalImageNode15materialTextureEv',
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(QSize)
  def supportsWrap(self, size: QSize) -> bool:
    """
    Calls Qt's 'bool QSGBasicInternalImageNode::supportsWrap(const QSize
    &size) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#supportsWrap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool QSGBasicInternalImageNode::supportsWrap(const QSize &size) const
    return self.uglySide.call(
        'ritual_ZNK25QSGBasicInternalImageNode12supportsWrapERK5QSize',
        self._valueOf(size),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setTargetRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setTargetRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setTargetRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGBasicInternalImageNode::setTargetRect(const QRectF &rect)
    ritual = 'ritual_ZN25QSGBasicInternalImageNode13setTargetRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGBasicInternalImageNode13setTargetRectERK6QRect'
          'F')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setInnerTargetRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setInnerTargetRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setInnerTargetRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGBasicInternalImageNode::setInnerTargetRect(const QRectF &rect)
    ritual = (
        'ritual_ZN25QSGBasicInternalImageNode18setInnerTargetRectERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGBasicInternalImageNode18setInnerTargetRectERK6'
          'QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setInnerSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setInnerSourceRect(const
    QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setInnerSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGBasicInternalImageNode::setInnerSourceRect(const QRectF &rect)
    ritual = (
        'ritual_ZN25QSGBasicInternalImageNode18setInnerSourceRectERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGBasicInternalImageNode18setInnerSourceRectERK6'
          'QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QRectF)
  def setSubSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setSubSourceRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setSubSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGBasicInternalImageNode::setSubSourceRect(const QRectF &rect)
    ritual = (
        'ritual_ZN25QSGBasicInternalImageNode16setSubSourceRectERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGBasicInternalImageNode16setSubSourceRectERK6QR'
          'ectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBasicInternalImageNode::setTexture(QSGTexture *texture)
    ritual = 'ritual_ZN25QSGBasicInternalImageNode10setTextureEP10QSGTexture'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QSGBasicInternalImageNode10setTextureEP10QSGTextu'
          're')
    self.uglySide.call(ritual, self._addressOf(texture))

  @overload(bool)
  def setAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setAntialiasing

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QSGBasicInternalImageNode::setAntialiasing(bool antialiasing)
    ritual = 'ritual_ZN25QSGBasicInternalImageNode15setAntialiasingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGBasicInternalImageNode15setAntialiasingEb'
    self.uglySide.call(ritual, antialiasing)

  @overload(bool, bool)
  def setMirror(
      self,
      mirrorHorizontally: bool,
      mirrorVertically: bool,
  ) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setMirror(bool
    mirrorHorizontally, bool mirrorVertically)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setMirror

    Parameters
    ----------

    mirrorHorizontally : bool
      Passed on as it is.

    mirrorVertically : bool
      Passed on as it is.
    """
    #  void QSGBasicInternalImageNode::setMirror(bool mirrorHorizontally,
    #      bool mirrorVertically)
    ritual = 'ritual_ZN25QSGBasicInternalImageNode9setMirrorEbb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGBasicInternalImageNode9setMirrorEbb'
    self.uglySide.call(ritual, mirrorHorizontally, mirrorVertically)

  @overload(QSGTexture)
  @overload(NoneType)
  def setMaterialTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::setMaterialTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#setMaterialTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBasicInternalImageNode::setMaterialTexture(QSGTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN25QSGBasicInternalImageNode18setMaterialTextureEP10QSGTex'
        'ture',
        self._addressOf(texture),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSGBasicInternalImageNode::QSGBasicInternalImageNode()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html
    """
    #  QSGBasicInternalImageNode::QSGBasicInternalImageNode()
    self._noteCreation(QSGBasicInternalImageNode, lambda: Rituals.call(
        'ritual_ZN25QSGBasicInternalImageNodeC1Ev',
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
    Calls Qt's 'void QSGBasicInternalImageNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#update
    """
    #  void QSGBasicInternalImageNode::update()
    ritual = 'ritual_ZN25QSGBasicInternalImageNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGBasicInternalImageNode6updateEv'
    self.uglySide.call(ritual)

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalImageNode::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html#preprocess
    """
    #  void QSGBasicInternalImageNode::preprocess()
    ritual = 'ritual_ZN25QSGBasicInternalImageNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QSGBasicInternalImageNode10preprocessEv'
    self.uglySide.call(ritual)

  def updateMaterialAntialiasing(self) -> None:
    """
    Calls Qt's 'void
    QSGBasicInternalImageNode::updateMaterialAntialiasing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html
    """
    #  void QSGBasicInternalImageNode::updateMaterialAntialiasing()
    self.uglySide.call(
        'ritual_ZN25QSGBasicInternalImageNode26updateMaterialAntialiasingEv',
    )

  def updateMaterialBlending(self) -> bool:
    """
    Calls Qt's 'bool QSGBasicInternalImageNode::updateMaterialBlending()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalimagenode.html
    """
    #  bool QSGBasicInternalImageNode::updateMaterialBlending()
    return self.uglySide.call(
        'ritual_ZN25QSGBasicInternalImageNode22updateMaterialBlendingEv',
    )
