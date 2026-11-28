"""
QQuickRectangularShadowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickrectangularshadow_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRectangularShadowPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem, QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QVector4D
  from . import QQuickRectangularShadow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QQuickRectangularShadowPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickRectangularShadowPrivate: a plain Python object
  standing in front of one C++ QQuickRectangularShadowPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's
  QQuickRectangularShadowPrivate is built on Qt's QQuickItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRectangularShadowPrivate that has a ritual and
  that Python can call so far, 15 names in all: 'q_func', 'initialize',
  'handleGeometryChange', 'handleItemChange', 'getPadding', 'updateColor',
  'updateShaderSource', 'updateSizeProperties', 'updateCached',
  'clampedRadius', 'clampedRadius4R', 'currentMaterial',
  'maybeSetImplicitAntialiasing', 'useIndividualRadius',
  'updateDefaultShader'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickRectangularShadow
    *QQuickRectangularShadowPrivate::q_func() const': takes in Python what
    'QQuickRectangularShadow *QQuickRectangularShadowPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickRectangularShadowPrivate is created at the first use, not
    by 'QQuickRectangularShadowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRectangularShadowPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRectangularShadowPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadowPrivate::getPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html#getPadding
    """
    #  qreal QQuickRectangularShadowPrivate::getPadding() const
    return self.uglySide.call(
        'ritual_ZNK30QQuickRectangularShadowPrivate10getPaddingEv',
    )

  @overload(float)
  def clampedRadius(self, radius: float) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadowPrivate::clampedRadius(qreal
    radius) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html#clampedRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  qreal QQuickRectangularShadowPrivate::clampedRadius(qreal radius)
    #      const
    return self.uglySide.call(
        'ritual_ZNK30QQuickRectangularShadowPrivate13clampedRadiusEd',
        radius,
    )

  def clampedRadius4R(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuickRectangularShadowPrivate::clampedRadius4R()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuickRectangularShadowPrivate::clampedRadius4R() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickRectangularShadowPrivate15clampedRadius4REv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def currentMaterial(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickRectangularShadowPrivate::currentMaterial()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickRectangularShadowPrivate::currentMaterial() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickRectangularShadowPrivate15currentMaterialEv',
    )
    return QQuickItem._cuteAt(address)

  def useIndividualRadius(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangularShadowPrivate::useIndividualRadius()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html
    """
    #  bool QQuickRectangularShadowPrivate::useIndividualRadius() const
    return self.uglySide.call(
        'ritual_ZNK30QQuickRectangularShadowPrivate19useIndividualRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickRectangularShadowPrivate::QQuickRectangularShadowPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html
    """
    #  QQuickRectangularShadowPrivate::QQuickRectangularShadowPrivate()
    self._noteCreation(QQuickRectangularShadowPrivate, lambda: Rituals.call(
        'ritual_ZN30QQuickRectangularShadowPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickRectangularShadow]:
    """
    Calls Qt's 'QQuickRectangularShadow
    *QQuickRectangularShadowPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html#q_func

    Returns
    -------

    Optional[QQuickRectangularShadow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRectangularShadow *QQuickRectangularShadowPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate6q_funcEv',
    )
    from . import QQuickRectangularShadow
    return QQuickRectangularShadow._cuteAt(address)

  def initialize(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadowPrivate::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html#initialize
    """
    #  void QQuickRectangularShadowPrivate::initialize()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate10initializeEv',
    )

  @overload(QRectF, QRectF)
  def handleGeometryChange(
      self,
      newGeometry: QRectF,
      oldGeometry: QRectF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRectangularShadowPrivate::handleGeometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickRectangularShadowPrivate::handleGeometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate20handleGeometryChangeERK'
        '6QRectFS2_',
        self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def handleItemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRectangularShadowPrivate::handleItemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickRectangularShadowPrivate::handleItemChange(QQuickItem::
    #      ItemChange change, const QQuickItem::ItemChangeData &value)
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate16handleItemChangeEN10QQu'
        'ickItem10ItemChangeERKNS0_14ItemChangeDataE',
        change.value, self._valueOf(value),
    )

  def updateColor(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadowPrivate::updateColor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html#updateColor
    """
    #  void QQuickRectangularShadowPrivate::updateColor()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate11updateColorEv',
    )

  def updateShaderSource(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadowPrivate::updateShaderSource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html
    """
    #  void QQuickRectangularShadowPrivate::updateShaderSource()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate18updateShaderSourceEv',
    )

  def updateSizeProperties(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadowPrivate::updateSizeProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html
    """
    #  void QQuickRectangularShadowPrivate::updateSizeProperties()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate20updateSizePropertiesEv',
    )

  def updateCached(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadowPrivate::updateCached()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html#updateCached
    """
    #  void QQuickRectangularShadowPrivate::updateCached()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate12updateCachedEv',
    )

  def maybeSetImplicitAntialiasing(self) -> None:
    """
    Calls Qt's 'void
    QQuickRectangularShadowPrivate::maybeSetImplicitAntialiasing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html
    """
    #  void QQuickRectangularShadowPrivate::maybeSetImplicitAntialiasing()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate28maybeSetImplicitAntiali'
        'asingEv',
    )

  def updateDefaultShader(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadowPrivate::updateDefaultShader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadowprivate.html
    """
    #  void QQuickRectangularShadowPrivate::updateDefaultShader()
    self.uglySide.call(
        'ritual_ZN30QQuickRectangularShadowPrivate19updateDefaultShaderEv',
    )
