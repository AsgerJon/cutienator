"""
QSGNinePatchNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgninepatchnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QSGGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QVector4D
  from . import QSGGeometry, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGGeometry = WAIT['QSGGeometry']
  QSGTexture = WAIT['QSGTexture']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGNinePatchNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGNinePatchNode: a plain Python object standing in
  front of one C++ QSGNinePatchNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGNinePatchNode is
  built on Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGNinePatchNode that has a ritual and that Python
  can call so far, 6 names in all: 'setTexture', 'setBounds',
  'setDevicePixelRatio', 'setPadding', 'update', 'rebuildGeometry'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGNinePatchNode::~QSGNinePatchNode()': the destructor: Python
    never removes a C++ QSGNinePatchNode.

  What to expect
  --------------

  - The C++ QSGNinePatchNode is created at the first use, not by
    'QSGNinePatchNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGNinePatchNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSGTexture, QSGGeometry, QVector4D, QRectF, float)
  @overload(QSGTexture, NoneType, QVector4D, QRectF, float)
  @overload(NoneType, QSGGeometry, QVector4D, QRectF, float)
  @overload(NoneType, NoneType, QVector4D, QRectF, float)
  def rebuildGeometry(
      texture: Optional[QSGTexture],
      geometry: Optional[QSGGeometry],
      padding: QVector4D,
      bounds: QRectF,
      dpr: float,
  ) -> None:
    """
    Calls Qt's 'void QSGNinePatchNode::rebuildGeometry(QSGTexture *texture,
    QSGGeometry *geometry, const QVector4D &padding, const QRectF &bounds,
    qreal dpr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgninepatchnode.html#rebuildGeometry

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    geometry : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    padding : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    dpr : float
      Passed on as it is.
    """
    #  void QSGNinePatchNode::rebuildGeometry(QSGTexture *texture,
    #      QSGGeometry *geometry, const QVector4D &padding, const QRectF
    #      &bounds, qreal dpr)
    Rituals.call(
        'ritual_ZN16QSGNinePatchNode15rebuildGeometryEP10QSGTextureP11QSGGe'
        'ometryRK9QVector4DRK6QRectFd',
        CuteMixin._addressOf(texture), CuteMixin._addressOf(geometry),
        CuteMixin._valueOf(padding), CuteMixin._valueOf(bounds), dpr,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGNinePatchNode'

  #  A C++ QSGNinePatchNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGNinePatchNode'

  #  The functions Qt calls itself that QSGNinePatchNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setTexture': (
          ('_ZN16QSGNinePatchNode10setTextureEP10QSGTexture',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTexture'),
           )),
      ),
      'setBounds': (
          ('_ZN16QSGNinePatchNode9setBoundsERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setDevicePixelRatio': (
          ('_ZN16QSGNinePatchNode19setDevicePixelRatioEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setPadding': (
          ('_ZN16QSGNinePatchNode10setPaddingEdddd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'update': (
          ('_ZN16QSGNinePatchNode6updateEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGNinePatchNode::setTexture(QSGTexture *texture)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgninepatchnode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGNinePatchNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN16QSGNinePatchNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(QRectF)
  def setBounds(self, bounds: QRectF) -> None:
    """
    Calls Qt's 'void QSGNinePatchNode::setBounds(const QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgninepatchnode.html#setBounds

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGNinePatchNode::setBounds(const QRectF &bounds)
    self.uglySide.call(
        'ritual_ZN16QSGNinePatchNode9setBoundsERK6QRectF',
        self._valueOf(bounds),
    )

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGNinePatchNode::setDevicePixelRatio(qreal ratio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgninepatchnode.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGNinePatchNode::setDevicePixelRatio(qreal ratio)
    self.uglySide.call(
        'ritual_ZN16QSGNinePatchNode19setDevicePixelRatioEd', ratio,
    )

  @overload(float, float, float, float)
  def setPadding(
      self,
      left: float,
      top: float,
      right: float,
      bottom: float,
  ) -> None:
    """
    Calls Qt's 'void QSGNinePatchNode::setPadding(qreal left, qreal top,
    qreal right, qreal bottom)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgninepatchnode.html#setPadding

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
    #  void QSGNinePatchNode::setPadding(qreal left, qreal top, qreal right,
    #      qreal bottom)
    self.uglySide.call(
        'ritual_ZN16QSGNinePatchNode10setPaddingEdddd',
        left, top, right, bottom,
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
    Calls Qt's 'void QSGNinePatchNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgninepatchnode.html#update
    """
    #  void QSGNinePatchNode::update()
    self.uglySide.call('ritual_ZN16QSGNinePatchNode6updateEv')
