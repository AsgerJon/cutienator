"""
QSGSoftwareNinePatchNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareNinePatchNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGNinePatchNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from . import QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGTexture = WAIT['QSGTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareNinePatchNode(QSGNinePatchNode):
  """
  The cute side of Qt's QSGSoftwareNinePatchNode: a plain Python object
  standing in front of one C++ QSGSoftwareNinePatchNode.

  It is built on the cute 'QSGNinePatchNode', as Qt's
  QSGSoftwareNinePatchNode is built on Qt's QSGNinePatchNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareNinePatchNode that has a ritual and that
  Python can call so far, 7 names in all: 'setTexture', 'setBounds',
  'setDevicePixelRatio', 'setPadding', 'update', 'bounds', 'isOpaque'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 1 leans on 'QSGSoftwareHelpers; 1 leans
  on 'QSGSoftwarePixmapTexture.

  What to expect
  --------------

  - The C++ QSGSoftwareNinePatchNode is created at the first use, not by
    'QSGSoftwareNinePatchNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareNinePatchNode.
  - Each name of Qt's QSGSoftwareNinePatchNode that has no cute function yet,
    '__init__', 'paint', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareNinePatchNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bounds(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareNinePatchNode::bounds() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#bounds

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareNinePatchNode::bounds() const
    address = self.uglySide.call(
        'ritual_ZNK24QSGSoftwareNinePatchNode6boundsEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareNinePatchNode::isOpaque() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#isOpaque
    """
    #  bool QSGSoftwareNinePatchNode::isOpaque() const
    return self.uglySide.call(
        'ritual_ZNK24QSGSoftwareNinePatchNode8isOpaqueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGSoftwareNinePatchNode::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareNinePatchNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN24QSGSoftwareNinePatchNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(QRectF)
  def setBounds(self, bounds: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareNinePatchNode::setBounds(const QRectF
    &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#setBounds

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareNinePatchNode::setBounds(const QRectF &bounds)
    ritual = 'ritual_ZN24QSGSoftwareNinePatchNode9setBoundsERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSGSoftwareNinePatchNode9setBoundsERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(bounds))

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareNinePatchNode::setDevicePixelRatio(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGSoftwareNinePatchNode::setDevicePixelRatio(qreal ratio)
    ritual = 'ritual_ZN24QSGSoftwareNinePatchNode19setDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSGSoftwareNinePatchNode19setDevicePixelRatioEd')
    self.uglySide.call(ritual, ratio)

  @overload(float, float, float, float)
  def setPadding(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Calls Qt's 'void QSGSoftwareNinePatchNode::setPadding(qreal left, qreal
    top, qreal right, qreal bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#setPadding

    Parameters
    ----------

    left : float
      Passed on as it is.

    top : float
      Passed on as it is.

    right : float
      Passed on as it is.

    bottom : float
      Passed on as it is.
    """
    #  void QSGSoftwareNinePatchNode::setPadding(qreal left, qreal top, qreal
    #      right, qreal bottom)
    ritual = 'ritual_ZN24QSGSoftwareNinePatchNode10setPaddingEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSGSoftwareNinePatchNode10setPaddingEdddd'
    self.uglySide.call(ritual, left, top, right, bottom)

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
    Qt's 'QSGSoftwareNinePatchNode::QSGSoftwareNinePatchNode()': leans on
    'QSGSoftwarePixmapTexture::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareNinePatchNode.__init__' has no cute function yet. Qt's "
        "'QSGSoftwareNinePatchNode::QSGSoftwareNinePatchNode()': leans on "
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
    Calls Qt's 'void QSGSoftwareNinePatchNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareninepatchnode.html#update
    """
    #  void QSGSoftwareNinePatchNode::update()
    ritual = 'ritual_ZN24QSGSoftwareNinePatchNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSGSoftwareNinePatchNode6updateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def paint(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareNinePatchNode::paint(QPainter *painter)': leans on
    'QSGSoftwareHelpers::qDrawBorderPixmap(QPainter*, QRect const&, QMargins
    const&, QPixmap const&, QRect const&, QMargins const&,
    QSGSoftwareHelpers::QTileRules const&,
    QFlags<QSGSoftwareHelpers::QDrawBorderPixmap::DrawingHint>)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareNinePatchNode.paint' has no cute function yet. Qt's "
        "'void QSGSoftwareNinePatchNode::paint(QPainter *painter)': leans "
        "on 'QSGSoftwareHelpers::qDrawBorderPixmap(QPainter*, QRect const&, "
        "QMargins const&, QPixmap const&, QRect const&, QMargins const&, "
        "QSGSoftwareHelpers::QTileRules const&, "
        "QFlags<QSGSoftwareHelpers::QDrawBorderPixmap::DrawingHint>)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
