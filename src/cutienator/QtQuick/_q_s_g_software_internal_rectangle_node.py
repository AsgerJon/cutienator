"""
QSGSoftwareInternalRectangleNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalrectanglenode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGSoftwareInternalRectangleNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGInternalRectangleNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QRectF
  from ..QtGui import QColor, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareInternalRectangleNode(QSGInternalRectangleNode):
  """
  The cute side of Qt's QSGSoftwareInternalRectangleNode: a plain Python
  object standing in front of one C++ QSGSoftwareInternalRectangleNode.

  It is built on the cute 'QSGInternalRectangleNode', as Qt's
  QSGSoftwareInternalRectangleNode is built on Qt's QSGInternalRectangleNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareInternalRectangleNode that has a ritual
  and that Python can call so far, 23 names in all: 'setRect', 'setColor',
  'setPenColor', 'setPenWidth', 'setGradientVertical', 'setRadius',
  'setTopLeftRadius', 'setTopRightRadius', 'setBottomLeftRadius',
  'setBottomRightRadius', 'resetTopLeftRadius', 'resetTopRightRadius',
  'resetBottomLeftRadius', 'resetBottomRightRadius', 'setAntialiasing',
  'setAligned', 'update', 'paint', 'isOpaque', 'rect', 'paintRectangle',
  'paintRectangleIndividualCorners', 'generateCornerPixmap'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSGSoftwareInternalRectangleNode::setGradientStops(const
    QGradientStops &stops)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 25 functions Qt declares: 1 leans on
  'QSGSoftwareInternalRectangleNode.

  What to expect
  --------------

  - The C++ QSGSoftwareInternalRectangleNode is created at the first use, not
    by 'QSGSoftwareInternalRectangleNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareInternalRectangleNode.
  - Each name of Qt's QSGSoftwareInternalRectangleNode that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QSGSoftwareInternalRectangleNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareInternalRectangleNode::isOpaque() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#isOpaque
    """
    #  bool QSGSoftwareInternalRectangleNode::isOpaque() const
    return self.uglySide.call(
        'ritual_ZNK32QSGSoftwareInternalRectangleNode8isOpaqueEv',
    )

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareInternalRectangleNode::rect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareInternalRectangleNode::rect() const
    address = self.uglySide.call(
        'ritual_ZNK32QSGSoftwareInternalRectangleNode4rectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalRectangleNode::setRect(const QRectF &rect)
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode7setRectERK6QRect'
          'F')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalRectangleNode::setColor(const QColor &color)
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode8setColorERK6QCol'
          'or')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QColor)
  def setPenColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setPenColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#setPenColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSoftwareInternalRectangleNode::setPenColor(const QColor
    #      &color)
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode11setPenColorERK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode11setPenColorERK6'
          'QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(float)
  def setPenWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setPenWidth(qreal
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#setPenWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setPenWidth(qreal width)
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode11setPenWidthEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode11setPenWidthEd')
    self.uglySide.call(ritual, width)

  @overload(bool)
  def setGradientVertical(self, vertical: bool) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::setGradientVertical(bool vertical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    vertical : bool
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setGradientVertical(bool
    #      vertical)
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode19setGradientVerticalEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode19setGradientVert'
          'icalEb')
    self.uglySide.call(ritual, vertical)

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setRadius(qreal radius)
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode9setRadiusEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN32QSGSoftwareInternalRectangleNode9setRadiusEd'
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setTopLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setTopLeftRadius(qreal radius)
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode16setTopLeftRadiusEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode16setTopLeftRadiu'
          'sEd')
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::setTopRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setTopRightRadius(qreal radius)
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode17setTopRightRadiusEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode17setTopRightRadi'
          'usEd')
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::setBottomLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setBottomLeftRadius(qreal
    #      radius)
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode19setBottomLeftRadiusEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode19setBottomLeftRa'
          'diusEd')
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::setBottomRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setBottomRightRadius(qreal
    #      radius)
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode20setBottomRightRadiusE'
        'd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode20setBottomRightR'
          'adiusEd')
    self.uglySide.call(ritual, radius)

  @overload(bool)
  def setAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setAntialiasing(bool
    #      antialiasing)
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode15setAntialiasingEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode15setAntialiasing'
          'Eb')
    self.uglySide.call(ritual, antialiasing)

  @overload(bool)
  def setAligned(self, aligned: bool) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::setAligned(bool
    aligned)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#setAligned

    Parameters
    ----------

    aligned : bool
      Passed on as it is.
    """
    #  void QSGSoftwareInternalRectangleNode::setAligned(bool aligned)
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode10setAlignedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode10setAlignedEb')
    self.uglySide.call(ritual, aligned)

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
    Qt's
    'QSGSoftwareInternalRectangleNode::QSGSoftwareInternalRectangleNode()':
    leans on 'QSGSoftwareInternalRectangleNode::setGradientStops(QList<std::
    pair<double, QColor> > const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareInternalRectangleNode.__init__' has no cute function "
        "yet. Qt's "
        "'QSGSoftwareInternalRectangleNode::QSGSoftwareInternalRectangleNode"
        "()': leans on "
        "'QSGSoftwareInternalRectangleNode::setGradientStops(QList<std::pair"
        "<double, QColor> > const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html
    """
    #  void QSGSoftwareInternalRectangleNode::resetTopLeftRadius()
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode18resetTopLeftRadiusEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode18resetTopLeftRad'
          'iusEv')
    self.uglySide.call(ritual)

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html
    """
    #  void QSGSoftwareInternalRectangleNode::resetTopRightRadius()
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode19resetTopRightRadiusEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode19resetTopRightRa'
          'diusEv')
    self.uglySide.call(ritual)

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html
    """
    #  void QSGSoftwareInternalRectangleNode::resetBottomLeftRadius()
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode21resetBottomLeftRadius'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode21resetBottomLeft'
          'RadiusEv')
    self.uglySide.call(ritual)

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html
    """
    #  void QSGSoftwareInternalRectangleNode::resetBottomRightRadius()
    ritual = (
        'ritual_ZN32QSGSoftwareInternalRectangleNode22resetBottomRightRadiu'
        'sEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QSGSoftwareInternalRectangleNode22resetBottomRigh'
          'tRadiusEv')
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#update
    """
    #  void QSGSoftwareInternalRectangleNode::update()
    ritual = 'ritual_ZN32QSGSoftwareInternalRectangleNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN32QSGSoftwareInternalRectangleNode6updateEv'
    self.uglySide.call(ritual)

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, a0: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSGSoftwareInternalRectangleNode::paint(QPainter *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html#paint

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareInternalRectangleNode::paint(QPainter *a0)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareInternalRectangleNode5paintEP8QPainter',
        self._addressOf(a0),
    )

  @overload(QPainter, QRect)
  @overload(NoneType, QRect)
  def paintRectangle(self, painter: Optional[QPainter], rect: QRect) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::paintRectangle(QPainter *painter, const
    QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QSGSoftwareInternalRectangleNode::paintRectangle(QPainter
    #      *painter, const QRect &rect)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareInternalRectangleNode14paintRectangleEP8QPai'
        'nterRK5QRect',
        self._addressOf(painter), self._valueOf(rect),
    )

  @overload(QPainter, QRect)
  @overload(NoneType, QRect)
  def paintRectangleIndividualCorners(
      self,
      painter: Optional[QPainter],
      rect: QRect,
  ) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::paintRectangleIndividualCorners(
    QPainter *painter, const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void
    #      QSGSoftwareInternalRectangleNode::paintRectangleIndividualCorners(
    #      QPainter *painter, const QRect &rect)
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareInternalRectangleNode31paintRectangleIndivid'
        'ualCornersEP8QPainterRK5QRect',
        self._addressOf(painter), self._valueOf(rect),
    )

  def generateCornerPixmap(self) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareInternalRectangleNode::generateCornerPixmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwareinternalrectanglenode.html
    """
    #  void QSGSoftwareInternalRectangleNode::generateCornerPixmap()
    self.uglySide.call(
        'ritual_ZN32QSGSoftwareInternalRectangleNode20generateCornerPixmapE'
        'v',
    )
