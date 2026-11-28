"""
QSGDefaultNinePatchNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultninepatchnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDefaultNinePatchNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGNinePatchNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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


class QSGDefaultNinePatchNode(QSGNinePatchNode):
  """
  The cute side of Qt's QSGDefaultNinePatchNode: a plain Python object
  standing in front of one C++ QSGDefaultNinePatchNode.

  It is built on the cute 'QSGNinePatchNode', as Qt's QSGDefaultNinePatchNode
  is built on Qt's QSGNinePatchNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDefaultNinePatchNode that has a ritual and that
  Python can call so far, 5 names in all: 'setTexture', 'setBounds',
  'setDevicePixelRatio', 'setPadding', 'update'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDefaultNinePatchNode::~QSGDefaultNinePatchNode()': the
    destructor: Python never removes a C++ QSGDefaultNinePatchNode.

  What to expect
  --------------

  - The C++ QSGDefaultNinePatchNode is created at the first use, not by
    'QSGDefaultNinePatchNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDefaultNinePatchNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDefaultNinePatchNode'

  #  A C++ QSGDefaultNinePatchNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDefaultNinePatchNode'

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
    Calls Qt's 'void QSGDefaultNinePatchNode::setTexture(QSGTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultninepatchnode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGDefaultNinePatchNode::setTexture(QSGTexture *texture)
    ritual = 'ritual_ZN23QSGDefaultNinePatchNode10setTextureEP10QSGTexture'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultNinePatchNode10setTextureEP10QSGTexture')
    self.uglySide.call(ritual, self._addressOf(texture))

  @overload(QRectF)
  def setBounds(self, bounds: QRectF) -> None:
    """
    Calls Qt's 'void QSGDefaultNinePatchNode::setBounds(const QRectF
    &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultninepatchnode.html#setBounds

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGDefaultNinePatchNode::setBounds(const QRectF &bounds)
    ritual = 'ritual_ZN23QSGDefaultNinePatchNode9setBoundsERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGDefaultNinePatchNode9setBoundsERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(bounds))

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGDefaultNinePatchNode::setDevicePixelRatio(qreal
    ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultninepatchnode.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGDefaultNinePatchNode::setDevicePixelRatio(qreal ratio)
    ritual = 'ritual_ZN23QSGDefaultNinePatchNode19setDevicePixelRatioEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSGDefaultNinePatchNode19setDevicePixelRatioEd')
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
    Calls Qt's 'void QSGDefaultNinePatchNode::setPadding(qreal left, qreal
    top, qreal right, qreal bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultninepatchnode.html#setPadding

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
    #  void QSGDefaultNinePatchNode::setPadding(qreal left, qreal top, qreal
    #      right, qreal bottom)
    ritual = 'ritual_ZN23QSGDefaultNinePatchNode10setPaddingEdddd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGDefaultNinePatchNode10setPaddingEdddd'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSGDefaultNinePatchNode::QSGDefaultNinePatchNode()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultninepatchnode.html
    """
    #  QSGDefaultNinePatchNode::QSGDefaultNinePatchNode()
    self._noteCreation(QSGDefaultNinePatchNode, lambda: Rituals.call(
        'ritual_ZN23QSGDefaultNinePatchNodeC1Ev',
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
    Calls Qt's 'void QSGDefaultNinePatchNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdefaultninepatchnode.html#update
    """
    #  void QSGDefaultNinePatchNode::update()
    ritual = 'ritual_ZN23QSGDefaultNinePatchNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSGDefaultNinePatchNode6updateEv'
    self.uglySide.call(ritual)
