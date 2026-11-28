"""
QQuickV4ParticleData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickv4particledata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickV4ParticleData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickParticleData, QQuickParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickParticleSystem = WAIT['QQuickParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickV4ParticleData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickV4ParticleData: a plain Python object standing
  in front of one C++ QQuickV4ParticleData.

  C++ hands a QQuickV4ParticleData around as a copy, so every C++
  QQuickV4ParticleData behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickV4ParticleData that has a ritual and that
  Python can call so far, 69 names in all: 'initialX', 'set_initialX',
  'initialVX', 'set_initialVX', 'initialAX', 'set_initialAX', 'initialY',
  'set_initialY', 'initialVY', 'set_initialVY', 'initialAY', 'set_initialAY',
  't', 'set_t', 'startSize', 'set_startSize', 'endSize', 'set_endSize',
  'lifeSpan', 'set_lifeSpan', 'rotation', 'set_rotation', 'rotationVelocity',
  'set_rotationVelocity', 'autoRotate', 'set_autoRotate', 'update',
  'set_update', 'xDeformationVectorX', 'set_xDeformationVectorX',
  'yDeformationVectorX', 'set_yDeformationVectorX', 'xDeformationVectorY',
  'set_xDeformationVectorY', 'yDeformationVectorY',
  'set_yDeformationVectorY', 'animationIndex', 'set_animationIndex',
  'frameDuration', 'set_frameDuration', 'frameAt', 'set_frameAt',
  'frameCount', 'set_frameCount', 'animationT', 'set_animationT', 'x',
  'set_x', 'vx', 'set_vx', 'ax', 'set_ax', 'y', 'set_y', 'vy', 'set_vy',
  'ay', 'set_ay', 'red', 'set_red', 'green', 'set_green', 'blue', 'set_blue',
  'alpha', 'set_alpha', 'discard', 'lifeLeft', 'currentSize'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickV4ParticleData::~QQuickV4ParticleData()': the destructor:
    Python removes its C++ QQuickV4ParticleData by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 75 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickV4ParticleData is created at the first use, not by
    'QQuickV4ParticleData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickV4ParticleData back gives a copy the ritual
    made for Python, in a new cute QQuickV4ParticleData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickV4ParticleData'

  #  Qt's '~QQuickV4ParticleData()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickV4ParticleData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickV4ParticleDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def initialX(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::initialX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#initialX
    """
    #  float QQuickV4ParticleData::initialX() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData8initialXEv')

  def initialVX(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::initialVX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#initialVX
    """
    #  float QQuickV4ParticleData::initialVX() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData9initialVXEv')

  def initialAX(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::initialAX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#initialAX
    """
    #  float QQuickV4ParticleData::initialAX() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData9initialAXEv')

  def initialY(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::initialY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#initialY
    """
    #  float QQuickV4ParticleData::initialY() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData8initialYEv')

  def initialVY(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::initialVY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#initialVY
    """
    #  float QQuickV4ParticleData::initialVY() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData9initialVYEv')

  def initialAY(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::initialAY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#initialAY
    """
    #  float QQuickV4ParticleData::initialAY() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData9initialAYEv')

  def t(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::t() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#t
    """
    #  float QQuickV4ParticleData::t() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData1tEv')

  def startSize(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::startSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#startSize
    """
    #  float QQuickV4ParticleData::startSize() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData9startSizeEv')

  def endSize(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::endSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#endSize
    """
    #  float QQuickV4ParticleData::endSize() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData7endSizeEv')

  def lifeSpan(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::lifeSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#lifeSpan
    """
    #  float QQuickV4ParticleData::lifeSpan() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData8lifeSpanEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#rotation
    """
    #  float QQuickV4ParticleData::rotation() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData8rotationEv')

  def rotationVelocity(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::rotationVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#rotationVelocity
    """
    #  float QQuickV4ParticleData::rotationVelocity() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData16rotationVelocityEv',
    )

  def autoRotate(self) -> bool:
    """
    Calls Qt's 'bool QQuickV4ParticleData::autoRotate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#autoRotate
    """
    #  bool QQuickV4ParticleData::autoRotate() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData10autoRotateEv',
    )

  def update(self) -> bool:
    """
    Calls Qt's 'bool QQuickV4ParticleData::update() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#update
    """
    #  bool QQuickV4ParticleData::update() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData6updateEv')

  def xDeformationVectorX(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::xDeformationVectorX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#xDeformationVectorX
    """
    #  float QQuickV4ParticleData::xDeformationVectorX() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData19xDeformationVectorXEv',
    )

  def yDeformationVectorX(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::yDeformationVectorX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#yDeformationVectorX
    """
    #  float QQuickV4ParticleData::yDeformationVectorX() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData19yDeformationVectorXEv',
    )

  def xDeformationVectorY(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::xDeformationVectorY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#xDeformationVectorY
    """
    #  float QQuickV4ParticleData::xDeformationVectorY() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData19xDeformationVectorYEv',
    )

  def yDeformationVectorY(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::yDeformationVectorY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#yDeformationVectorY
    """
    #  float QQuickV4ParticleData::yDeformationVectorY() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData19yDeformationVectorYEv',
    )

  def animationIndex(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::animationIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#animationIndex
    """
    #  float QQuickV4ParticleData::animationIndex() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData14animationIndexEv',
    )

  def frameDuration(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::frameDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#frameDuration
    """
    #  float QQuickV4ParticleData::frameDuration() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData13frameDurationEv',
    )

  def frameAt(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::frameAt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#frameAt
    """
    #  float QQuickV4ParticleData::frameAt() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData7frameAtEv')

  def frameCount(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::frameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#frameCount
    """
    #  float QQuickV4ParticleData::frameCount() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData10frameCountEv',
    )

  def animationT(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::animationT() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#animationT
    """
    #  float QQuickV4ParticleData::animationT() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData10animationTEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#x
    """
    #  float QQuickV4ParticleData::x() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData1xEv')

  def vx(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::vx() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#vx
    """
    #  float QQuickV4ParticleData::vx() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData2vxEv')

  def ax(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::ax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#ax
    """
    #  float QQuickV4ParticleData::ax() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData2axEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#y
    """
    #  float QQuickV4ParticleData::y() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData1yEv')

  def vy(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::vy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#vy
    """
    #  float QQuickV4ParticleData::vy() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData2vyEv')

  def ay(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::ay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#ay
    """
    #  float QQuickV4ParticleData::ay() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData2ayEv')

  def red(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::red() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#red
    """
    #  float QQuickV4ParticleData::red() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData3redEv')

  def green(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::green() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#green
    """
    #  float QQuickV4ParticleData::green() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData5greenEv')

  def blue(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::blue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#blue
    """
    #  float QQuickV4ParticleData::blue() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData4blueEv')

  def alpha(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::alpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#alpha
    """
    #  float QQuickV4ParticleData::alpha() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData5alphaEv')

  def lifeLeft(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::lifeLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#lifeLeft
    """
    #  float QQuickV4ParticleData::lifeLeft() const
    return self.uglySide.call('ritual_ZNK20QQuickV4ParticleData8lifeLeftEv')

  def currentSize(self) -> float:
    """
    Calls Qt's 'float QQuickV4ParticleData::currentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#currentSize
    """
    #  float QQuickV4ParticleData::currentSize() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickV4ParticleData11currentSizeEv',
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
    'QQuickV4ParticleData::QQuickV4ParticleData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#QQuickV4ParticleData
    """
    #  QQuickV4ParticleData::QQuickV4ParticleData()
    self._noteCreation(QQuickV4ParticleData, lambda: Rituals.call(
        'ritual_ZN20QQuickV4ParticleDataC1Ev',
    ))

  @overload(QQuickParticleData, QQuickParticleSystem)
  @overload(QQuickParticleData, NoneType)
  @overload(NoneType, QQuickParticleSystem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      datum: Optional[QQuickParticleData],
      system: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickV4ParticleData::QQuickV4ParticleData(QQuickParticleData *datum,
    QQuickParticleSystem *system)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#QQuickV4ParticleData

    Parameters
    ----------

    datum : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    system : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickV4ParticleData::QQuickV4ParticleData(QQuickParticleData *datum,
    #      QQuickParticleSystem *system)
    self._noteCreation(QQuickV4ParticleData, lambda: Rituals.call(
        'ritual_ZN20QQuickV4ParticleDataC1EP18QQuickParticleDataP20QQuickPa'
        'rticleSystem',
        self._addressOf(datum), self._addressOf(system),
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

  @overload(float)
  def set_initialX(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_initialX(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_initialX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_initialX(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData12set_initialXEf', a)

  @overload(float)
  def set_initialVX(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_initialVX(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_initialVX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_initialVX(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData13set_initialVXEf', a)

  @overload(float)
  def set_initialAX(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_initialAX(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_initialAX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_initialAX(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData13set_initialAXEf', a)

  @overload(float)
  def set_initialY(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_initialY(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_initialY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_initialY(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData12set_initialYEf', a)

  @overload(float)
  def set_initialVY(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_initialVY(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_initialVY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_initialVY(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData13set_initialVYEf', a)

  @overload(float)
  def set_initialAY(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_initialAY(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_initialAY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_initialAY(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData13set_initialAYEf', a)

  @overload(float)
  def set_t(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_t(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_t

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_t(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData5set_tEf', a)

  @overload(float)
  def set_startSize(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_startSize(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_startSize

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_startSize(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData13set_startSizeEf', a)

  @overload(float)
  def set_endSize(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_endSize(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_endSize

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_endSize(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData11set_endSizeEf', a)

  @overload(float)
  def set_lifeSpan(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_lifeSpan(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_lifeSpan

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_lifeSpan(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData12set_lifeSpanEf', a)

  @overload(float)
  def set_rotation(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_rotation(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_rotation

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_rotation(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData12set_rotationEf', a)

  @overload(float)
  def set_rotationVelocity(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_rotationVelocity(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_rotationVelocity

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_rotationVelocity(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData20set_rotationVelocityEf', a,
    )

  @overload(bool)
  def set_autoRotate(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_autoRotate(bool a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_autoRotate

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_autoRotate(bool a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData14set_autoRotateEb', a,
    )

  @overload(bool)
  def set_update(self, a: bool) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_update(bool a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_update

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_update(bool a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData10set_updateEb', a)

  @overload(float)
  def set_xDeformationVectorX(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_xDeformationVectorX(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_xDeformationVectorX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_xDeformationVectorX(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData23set_xDeformationVectorXEf', a,
    )

  @overload(float)
  def set_yDeformationVectorX(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_yDeformationVectorX(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_yDeformationVectorX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_yDeformationVectorX(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData23set_yDeformationVectorXEf', a,
    )

  @overload(float)
  def set_xDeformationVectorY(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_xDeformationVectorY(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_xDeformationVectorY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_xDeformationVectorY(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData23set_xDeformationVectorYEf', a,
    )

  @overload(float)
  def set_yDeformationVectorY(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_yDeformationVectorY(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_yDeformationVectorY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_yDeformationVectorY(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData23set_yDeformationVectorYEf', a,
    )

  @overload(float)
  def set_animationIndex(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_animationIndex(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_animationIndex

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_animationIndex(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData18set_animationIndexEf', a,
    )

  @overload(float)
  def set_frameDuration(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_frameDuration(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_frameDuration

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_frameDuration(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData17set_frameDurationEf', a,
    )

  @overload(float)
  def set_frameAt(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_frameAt(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_frameAt

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_frameAt(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData11set_frameAtEf', a)

  @overload(float)
  def set_frameCount(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_frameCount(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_frameCount

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_frameCount(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData14set_frameCountEf', a,
    )

  @overload(float)
  def set_animationT(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_animationT(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_animationT

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_animationT(float a)
    self.uglySide.call(
        'ritual_ZN20QQuickV4ParticleData14set_animationTEf', a,
    )

  @overload(float)
  def set_x(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_x(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_x

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_x(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData5set_xEf', a)

  @overload(float)
  def set_vx(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_vx(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_vx

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_vx(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData6set_vxEf', a)

  @overload(float)
  def set_ax(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_ax(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_ax

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_ax(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData6set_axEf', a)

  @overload(float)
  def set_y(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_y(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_y

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_y(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData5set_yEf', a)

  @overload(float)
  def set_vy(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_vy(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_vy

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_vy(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData6set_vyEf', a)

  @overload(float)
  def set_ay(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_ay(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_ay

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_ay(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData6set_ayEf', a)

  @overload(float)
  def set_red(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_red(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_red

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_red(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData7set_redEf', a)

  @overload(float)
  def set_green(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_green(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_green

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_green(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData9set_greenEf', a)

  @overload(float)
  def set_blue(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_blue(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#set_blue

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_blue(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData8set_blueEf', a)

  @overload(float)
  def set_alpha(self, a: float) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::set_alpha(float a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickv4particledata.html#set_alpha

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void QQuickV4ParticleData::set_alpha(float a)
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData9set_alphaEf', a)

  def discard(self) -> None:
    """
    Calls Qt's 'void QQuickV4ParticleData::discard()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickv4particledata.html#discard
    """
    #  void QQuickV4ParticleData::discard()
    self.uglySide.call('ritual_ZN20QQuickV4ParticleData7discardEv')


#  Qt's 'QList<QQuickV4ParticleData>': the list of QQuickV4ParticleData,
#  which 'QList[QQuickV4ParticleData]' gives. It is made here, so that there
#  is one as soon as there can be a QQuickV4ParticleData.
QList.createKind(
    QQuickV4ParticleData, 'value',
    make='ritual_list_make_QQuickV4ParticleData',
    add='ritual_list_add_QQuickV4ParticleData',
    size='ritual_list_size_QQuickV4ParticleData',
    at='ritual_list_at_QQuickV4ParticleData',
    drop='ritual_list_drop_QQuickV4ParticleData',
)
