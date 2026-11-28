"""
QCanvasBoxShadowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasboxshadow_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCanvasBoxShadowPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QCanvasBrushPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor, QVector4D
  from . import QCPaint, QCanvasBoxShadow, QCanvasBrush, QCanvasPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBoxShadow = WAIT['QCanvasBoxShadow']
  QCanvasBrush = WAIT['QCanvasBrush']
  QCanvasPainter = WAIT['QCanvasPainter']
  QColor = WAIT['QColor']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasBoxShadowPrivate(QCanvasBrushPrivate):
  """
  The cute side of Qt's QCanvasBoxShadowPrivate: a plain Python object
  standing in front of one C++ QCanvasBoxShadowPrivate.

  It is built on the cute 'QCanvasBrushPrivate', as Qt's
  QCanvasBoxShadowPrivate is built on Qt's QCanvasBrushPrivate, and has
  everything that class has.

  C++ hands a QCanvasBoxShadowPrivate around as a copy, so every C++
  QCanvasBoxShadowPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasBoxShadowPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'clone', 'get', 'create',
  'getFromCanvasBrush', 'createPaint', 'createBoxShadow', 'clampedRadius',
  'clampedColor'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QCanvasBoxShadowPrivate::equals(const QCanvasBrushPrivate
    &other) const': takes a type Python has no way to hand over yet.
  - Qt's 'const QCanvasBoxShadowPrivate *QCanvasBoxShadowPrivate::get(const
    QCanvasBoxShadow *brush)': takes in Python what 'QCanvasBoxShadowPrivate
    *QCanvasBoxShadowPrivate::get(QCanvasBoxShadow *brush)' takes.
  - Qt's 'QCanvasBoxShadowPrivate::~QCanvasBoxShadowPrivate()': the
    destructor: Python removes its C++ QCanvasBoxShadowPrivate by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QCanvasBoxShadowPrivate is created at the first use, not by
    'QCanvasBoxShadowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasBoxShadowPrivate back gives a copy the ritual
    made for Python, in a new cute QCanvasBoxShadowPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCanvasBoxShadow)
  @overload(NoneType)
  def get(
      brush: Optional[QCanvasBoxShadow],
  ) -> Optional[QCanvasBoxShadowPrivate]:
    """
    Calls Qt's 'QCanvasBoxShadowPrivate
    *QCanvasBoxShadowPrivate::get(QCanvasBoxShadow *brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#get

    Parameters
    ----------

    brush : Optional[QCanvasBoxShadow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasBoxShadowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBoxShadowPrivate *QCanvasBoxShadowPrivate::get(QCanvasBoxShadow
    #      *brush)
    address = Rituals.call(
        'ritual_ZN23QCanvasBoxShadowPrivate3getEP16QCanvasBoxShadow',
        CuteMixin._addressOf(brush),
    )
    return QCanvasBoxShadowPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def create(p: Optional[QCanvasBoxShadowPrivate]) -> QCanvasBoxShadow:
    """
    Calls Qt's 'QCanvasBoxShadow
    QCanvasBoxShadowPrivate::create(QCanvasBoxShadowPrivate *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#create

    Parameters
    ----------

    p : Optional[QCanvasBoxShadowPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCanvasBoxShadow
      A new cute QCanvasBoxShadow around the copy Qt gave back. Python owns
      it.
    """
    #  QCanvasBoxShadow
    #      QCanvasBoxShadowPrivate::create(QCanvasBoxShadowPrivate *p)
    address = Rituals.call(
        'ritual_ZN23QCanvasBoxShadowPrivate6createEPS_',
        CuteMixin._addressOf(p),
    )
    from . import QCanvasBoxShadow
    return QCanvasBoxShadow._cuteOwning(address)

  @staticmethod
  @overload(QCanvasBrush)
  def getFromCanvasBrush(brush: QCanvasBrush) -> QCanvasBoxShadow:
    """
    Calls Qt's 'QCanvasBoxShadow
    QCanvasBoxShadowPrivate::getFromCanvasBrush(const QCanvasBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#getFromCanvasBrush

    Parameters
    ----------

    brush : QCanvasBrush
      Passed on as a value: Qt reads the C++ QCanvasBrush, which stays
      Python's own.

    Returns
    -------

    QCanvasBoxShadow
      A new cute QCanvasBoxShadow around the copy Qt gave back. Python owns
      it.
    """
    #  QCanvasBoxShadow QCanvasBoxShadowPrivate::getFromCanvasBrush(const
    #      QCanvasBrush &brush)
    address = Rituals.call(
        'ritual_ZN23QCanvasBoxShadowPrivate18getFromCanvasBrushERK12QCanvas'
        'Brush',
        CuteMixin._valueOf(brush),
    )
    from . import QCanvasBoxShadow
    return QCanvasBoxShadow._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasBoxShadowPrivate'

  #  A C++ QCanvasBoxShadowPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasBoxShadowPrivate'

  #  Qt's '~QCanvasBoxShadowPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCanvasBoxShadowPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QCanvasBoxShadowPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCanvasPainter)
  @overload(NoneType)
  def createPaint(self, painter: Optional[QCanvasPainter]) -> QCPaint:
    """
    Calls Qt's 'QCPaint QCanvasBoxShadowPrivate::createPaint(QCanvasPainter
    *painter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#createPaint

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QCPaint
      A new cute QCPaint around the copy Qt gave back. Python owns it.
    """
    #  QCPaint QCanvasBoxShadowPrivate::createPaint(QCanvasPainter *painter)
    #      const
    ritual = (
        'ritual_ZNK23QCanvasBoxShadowPrivate11createPaintEP14QCanvasPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QCanvasBoxShadowPrivate11createPaintEP14QCanvasP'
          'ainter')
    address = self.uglySide.call(ritual, self._addressOf(painter))
    from . import QCPaint
    return QCPaint._cuteOwning(address)

  @overload(float, float, float)
  def clampedRadius(
      self,
      radius: float,
      width: float,
      height: float,
  ) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadowPrivate::clampedRadius(qreal radius,
    qreal width, qreal height) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#clampedRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  qreal QCanvasBoxShadowPrivate::clampedRadius(qreal radius, qreal
    #      width, qreal height) const
    return self.uglySide.call(
        'ritual_ZNK23QCanvasBoxShadowPrivate13clampedRadiusEddd',
        radius, width, height,
    )

  def clampedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasBoxShadowPrivate::clampedColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#clampedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasBoxShadowPrivate::clampedColor() const
    address = self.uglySide.call(
        'ritual_ZNK23QCanvasBoxShadowPrivate12clampedColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

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
    'QCanvasBoxShadowPrivate::QCanvasBoxShadowPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html
    """
    #  QCanvasBoxShadowPrivate::QCanvasBoxShadowPrivate()
    self._noteCreation(QCanvasBoxShadowPrivate, lambda: Rituals.call(
        'ritual_ZN23QCanvasBoxShadowPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasBoxShadowPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasBoxShadowPrivate::QCanvasBoxShadowPrivate(const
    QCanvasBoxShadowPrivate &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html

    Parameters
    ----------

    a0 : QCanvasBoxShadowPrivate
      Passed on as a value: Qt reads the C++ QCanvasBoxShadowPrivate, which
      stays Python's own.
    """
    #  QCanvasBoxShadowPrivate::QCanvasBoxShadowPrivate(const
    #      QCanvasBoxShadowPrivate &a0)
    self._noteCreation(QCanvasBoxShadowPrivate, lambda: Rituals.call(
        'ritual_ZN23QCanvasBoxShadowPrivateC1ERKS_', self._valueOf(a0),
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

  def clone(self) -> Optional[QCanvasBrushPrivate]:
    """
    Calls Qt's 'QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#clone

    Returns
    -------

    Optional[QCanvasBrushPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasBrushPrivate *QCanvasBoxShadowPrivate::clone()
    ritual = 'ritual_ZN23QCanvasBoxShadowPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QCanvasBoxShadowPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QCanvasBrushPrivate._cuteAt(address)

  @overload(float, float, float, float, QVector4D, float, QColor)
  def createBoxShadow(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      radius: QVector4D,
      blur: float,
      color: QColor,
  ) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadowPrivate::createBoxShadow(qreal x, qreal
    y, qreal width, qreal height, const QVector4D &radius, qreal blur, QColor
    color) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadowprivate.html#createBoxShadow

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    radius : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.

    blur : float
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasBoxShadowPrivate::createBoxShadow(qreal x, qreal y, qreal
    #      width, qreal height, const QVector4D &radius, qreal blur, QColor
    #      color) const
    self.uglySide.call(
        'ritual_ZNK23QCanvasBoxShadowPrivate15createBoxShadowEddddRK9QVecto'
        'r4Dd6QColor',
        x, y, width, height, self._valueOf(radius), blur,
        self._valueOf(color),
    )
