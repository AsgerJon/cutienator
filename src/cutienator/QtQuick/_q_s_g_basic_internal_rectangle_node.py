"""
QSGBasicInternalRectangleNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbasicinternalrectanglenode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGBasicInternalRectangleNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGInternalRectangleNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']


class QSGBasicInternalRectangleNode(QSGInternalRectangleNode):
  """
  The cute side of Qt's QSGBasicInternalRectangleNode: a plain Python object
  standing in front of one C++ QSGBasicInternalRectangleNode.

  It is built on the cute 'QSGInternalRectangleNode', as Qt's
  QSGBasicInternalRectangleNode is built on Qt's QSGInternalRectangleNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGBasicInternalRectangleNode that has a ritual and
  that Python can call so far, 20 names in all: 'setRect', 'setColor',
  'setPenColor', 'setPenWidth', 'setGradientVertical', 'setRadius',
  'setTopLeftRadius', 'setTopRightRadius', 'setBottomLeftRadius',
  'setBottomRightRadius', 'resetTopLeftRadius', 'resetTopRightRadius',
  'resetBottomLeftRadius', 'resetBottomRightRadius', 'setAntialiasing',
  'setAligned', 'update', 'supportsAntialiasing',
  'updateMaterialAntialiasing', 'updateGeometry'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSGBasicInternalRectangleNode::setGradientStops(const
    QGradientStops &stops)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSGBasicInternalRectangleNode::updateMaterialBlending(QSGNode::DirtyState
    *state)': names 'QSGNode::DirtyState', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 24 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSGBasicInternalRectangleNode is created at the first use, not by
    'QSGBasicInternalRectangleNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBasicInternalRectangleNode.
  - Each name of Qt's QSGBasicInternalRectangleNode that has no cute function
    yet, 'updateGradientTexture', 'updateMaterialBlending', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBasicInternalRectangleNode'

  #  A C++ QSGBasicInternalRectangleNode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBasicInternalRectangleNode'

  #  The functions Qt calls itself that QSGBasicInternalRectangleNode is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'updateMaterialBlending': (
          'void '
          'QSGBasicInternalRectangleNode::updateMaterialBlending(QSGNode::D'
          'irtyState *)',
      ),
  }

  #  The functions Qt calls itself that QSGBasicInternalRectangleNode is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'supportsAntialiasing': (
          ('_ZNK29QSGBasicInternalRectangleNode20supportsAntialiasingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'updateMaterialAntialiasing': (
          ('_ZN29QSGBasicInternalRectangleNode26updateMaterialAntialiasingE'
           'v',
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

  def supportsAntialiasing(self) -> bool:
    """
    Calls Qt's 'bool QSGBasicInternalRectangleNode::supportsAntialiasing()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  bool QSGBasicInternalRectangleNode::supportsAntialiasing() const
    ritual = (
        'ritual_ZNK29QSGBasicInternalRectangleNode20supportsAntialiasingEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGBasicInternalRectangleNode20supportsAntialias'
          'ingEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGBasicInternalRectangleNode::setRect(const QRectF &rect)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode7setRectERK6QRectF')
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGBasicInternalRectangleNode::setColor(const QColor &color)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode8setColorERK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QColor)
  def setPenColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setPenColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setPenColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGBasicInternalRectangleNode::setPenColor(const QColor &color)
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode11setPenColorERK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode11setPenColorERK6QCo'
          'lor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(float)
  def setPenWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setPenWidth(qreal
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setPenWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setPenWidth(qreal width)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode11setPenWidthEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QSGBasicInternalRectangleNode11setPenWidthEd'
    self.uglySide.call(ritual, width)

  @overload(bool)
  def setGradientVertical(self, vertical: bool) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setGradientVertical(bool
    vertical)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html

    Parameters
    ----------

    vertical : bool
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setGradientVertical(bool vertical)
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode19setGradientVerticalEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode19setGradientVertica'
          'lEb')
    self.uglySide.call(ritual, vertical)

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setRadius(qreal radius)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode9setRadiusEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QSGBasicInternalRectangleNode9setRadiusEd'
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setTopLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setTopLeftRadius(qreal radius)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode16setTopLeftRadiusEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode16setTopLeftRadiusEd')
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setTopRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setTopRightRadius(qreal radius)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode17setTopRightRadiusEd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode17setTopRightRadiusE'
          'd')
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setBottomLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setBottomLeftRadius(qreal radius)
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode19setBottomLeftRadiusEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode19setBottomLeftRadiu'
          'sEd')
    self.uglySide.call(ritual, radius)

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void
    QSGBasicInternalRectangleNode::setBottomRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setBottomRightRadius(qreal radius)
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode20setBottomRightRadiusEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode20setBottomRightRadi'
          'usEd')
    self.uglySide.call(ritual, radius)

  @overload(bool)
  def setAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setAntialiasing

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setAntialiasing(bool antialiasing)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode15setAntialiasingEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode15setAntialiasingEb')
    self.uglySide.call(ritual, antialiasing)

  @overload(bool)
  def setAligned(self, aligned: bool) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::setAligned(bool
    aligned)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#setAligned

    Parameters
    ----------

    aligned : bool
      Passed on as it is.
    """
    #  void QSGBasicInternalRectangleNode::setAligned(bool aligned)
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode10setAlignedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QSGBasicInternalRectangleNode10setAlignedEb'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSGBasicInternalRectangleNode::QSGBasicInternalRectangleNode()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  QSGBasicInternalRectangleNode::QSGBasicInternalRectangleNode()
    self._noteCreation(QSGBasicInternalRectangleNode, lambda: Rituals.call(
        'ritual_ZN29QSGBasicInternalRectangleNodeC1Ev',
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

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  void QSGBasicInternalRectangleNode::resetTopLeftRadius()
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode18resetTopLeftRadiusEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode18resetTopLeftRadius'
          'Ev')
    self.uglySide.call(ritual)

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  void QSGBasicInternalRectangleNode::resetTopRightRadius()
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode19resetTopRightRadiusEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode19resetTopRightRadiu'
          'sEv')
    self.uglySide.call(ritual)

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  void QSGBasicInternalRectangleNode::resetBottomLeftRadius()
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode21resetBottomLeftRadiusEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode21resetBottomLeftRad'
          'iusEv')
    self.uglySide.call(ritual)

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void
    QSGBasicInternalRectangleNode::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  void QSGBasicInternalRectangleNode::resetBottomRightRadius()
    ritual = (
        'ritual_ZN29QSGBasicInternalRectangleNode22resetBottomRightRadiusEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGBasicInternalRectangleNode22resetBottomRightRa'
          'diusEv')
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#update
    """
    #  void QSGBasicInternalRectangleNode::update()
    ritual = 'ritual_ZN29QSGBasicInternalRectangleNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QSGBasicInternalRectangleNode6updateEv'
    self.uglySide.call(ritual)

  def updateMaterialAntialiasing(self) -> None:
    """
    Calls Qt's 'void
    QSGBasicInternalRectangleNode::updateMaterialAntialiasing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html
    """
    #  void QSGBasicInternalRectangleNode::updateMaterialAntialiasing()
    self.uglySide.call(
        'ritual_ZN29QSGBasicInternalRectangleNode26updateMaterialAntialiasi'
        'ngEv',
    )

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QSGBasicInternalRectangleNode::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicinternalrectanglenode.html#updateGeometry
    """
    #  void QSGBasicInternalRectangleNode::updateGeometry()
    self.uglySide.call(
        'ritual_ZN29QSGBasicInternalRectangleNode14updateGeometryEv',
    )

  @staticmethod
  def updateGradientTexture(*__, **_) -> Never:
    """
    Qt's 'void QSGBasicInternalRectangleNode::updateGradientTexture()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QSGBasicInternalRectangleNode.updateGradientTexture' has no cute "
        "function yet. Qt's 'void "
        "QSGBasicInternalRectangleNode::updateGradientTexture()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def updateMaterialBlending(*__, **_) -> Never:
    """
    Qt's 'void
    QSGBasicInternalRectangleNode::updateMaterialBlending(QSGNode::DirtyState
    *state)': names 'QSGNode::DirtyState', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGBasicInternalRectangleNode.updateMaterialBlending' has no cute "
        "function yet. Qt's 'void "
        "QSGBasicInternalRectangleNode::updateMaterialBlending(QSGNode::Dirt"
        "yState *state)': names 'QSGNode::DirtyState', which has no cute "
        "class yet.")
