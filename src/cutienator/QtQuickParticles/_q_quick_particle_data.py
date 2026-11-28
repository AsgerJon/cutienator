"""
QQuickParticleData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleData to be private: it declares the class in a
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

  from . import QQuickParticleSystem, QQuickV4ParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleSystem = WAIT['QQuickParticleSystem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickParticleData: a plain Python object standing in
  front of one C++ QQuickParticleData.

  C++ hands a QQuickParticleData around as a copy, so every C++
  QQuickParticleData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickParticleData that has a ritual and that Python
  can call so far, 20 names in all: 'setInstantaneousAX',
  'setInstantaneousVX', 'setInstantaneousX', 'setInstantaneousAY',
  'setInstantaneousVY', 'setInstantaneousY', 'curX', 'curVX', 'curAX',
  'curY', 'curVY', 'curAY', 'debugDump', 'stillAlive', 'alive', 'lifeLeft',
  'curSize', 'v4Value', 'extendLife', 'EPSILON'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickParticleData::~QQuickParticleData()': the destructor: Python
    removes its C++ QQuickParticleData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickParticleData is created at the first use, not by
    'QQuickParticleData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickParticleData back gives a copy the ritual made
    for Python, in a new cute QQuickParticleData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def EPSILON() -> float:
    """
    Calls Qt's 'float QQuickParticleData::EPSILON()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#EPSILON
    """
    #  float QQuickParticleData::EPSILON()
    return Rituals.call('ritual_ZN18QQuickParticleData7EPSILONEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleData'

  #  Qt's '~QQuickParticleData()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickParticleData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickParticleDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curX(self, particleSystem: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curX(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curX

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curX(QQuickParticleSystem *particleSystem)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData4curXEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curVX(self, particleSystem: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curVX(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curVX

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curVX(QQuickParticleSystem *particleSystem)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData5curVXEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload()
  def curAX(self) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curAX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curAX
    """
    #  float QQuickParticleData::curAX() const
    return self.uglySide.call('ritual_ZNK18QQuickParticleData5curAXEv')

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curAX(self, a0: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curAX(QQuickParticleSystem *a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curAX

    Parameters
    ----------

    a0 : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curAX(QQuickParticleSystem *a0) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData5curAXEP20QQuickParticleSystem',
        self._addressOf(a0),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curY(self, particleSystem: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curY(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curY

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curY(QQuickParticleSystem *particleSystem)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData4curYEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curVY(self, particleSystem: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curVY(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curVY

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curVY(QQuickParticleSystem *particleSystem)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData5curVYEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload()
  def curAY(self) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curAY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curAY
    """
    #  float QQuickParticleData::curAY() const
    return self.uglySide.call('ritual_ZNK18QQuickParticleData5curAYEv')

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curAY(self, a0: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curAY(QQuickParticleSystem *a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curAY

    Parameters
    ----------

    a0 : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curAY(QQuickParticleSystem *a0) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData5curAYEP20QQuickParticleSystem',
        self._addressOf(a0),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def stillAlive(
      self,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickParticleData::stillAlive(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#stillAlive

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickParticleData::stillAlive(QQuickParticleSystem
    #      *particleSystem) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData10stillAliveEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def alive(self, particleSystem: Optional[QQuickParticleSystem]) -> bool:
    """
    Calls Qt's 'bool QQuickParticleData::alive(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#alive

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickParticleData::alive(QQuickParticleSystem *particleSystem)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData5aliveEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def lifeLeft(
      self,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> float:
    """
    Calls Qt's 'float QQuickParticleData::lifeLeft(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#lifeLeft

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::lifeLeft(QQuickParticleSystem
    #      *particleSystem) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData8lifeLeftEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def curSize(self, particleSystem: Optional[QQuickParticleSystem]) -> float:
    """
    Calls Qt's 'float QQuickParticleData::curSize(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#curSize

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  float QQuickParticleData::curSize(QQuickParticleSystem
    #      *particleSystem) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParticleData7curSizeEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def setInstantaneousAX(
      self,
      ax: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::setInstantaneousAX(float ax,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledata.html#setInstantaneousAX

    Parameters
    ----------

    ax : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::setInstantaneousAX(float ax,
    #      QQuickParticleSystem *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData18setInstantaneousAXEfP20QQuickPartic'
        'leSystem',
        ax, self._addressOf(particleSystem),
    )

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def setInstantaneousVX(
      self,
      vx: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::setInstantaneousVX(float vx,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledata.html#setInstantaneousVX

    Parameters
    ----------

    vx : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::setInstantaneousVX(float vx,
    #      QQuickParticleSystem *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData18setInstantaneousVXEfP20QQuickPartic'
        'leSystem',
        vx, self._addressOf(particleSystem),
    )

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def setInstantaneousX(
      self,
      x: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::setInstantaneousX(float x,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledata.html#setInstantaneousX

    Parameters
    ----------

    x : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::setInstantaneousX(float x,
    #      QQuickParticleSystem *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData17setInstantaneousXEfP20QQuickParticl'
        'eSystem',
        x, self._addressOf(particleSystem),
    )

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def setInstantaneousAY(
      self,
      ay: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::setInstantaneousAY(float ay,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledata.html#setInstantaneousAY

    Parameters
    ----------

    ay : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::setInstantaneousAY(float ay,
    #      QQuickParticleSystem *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData18setInstantaneousAYEfP20QQuickPartic'
        'leSystem',
        ay, self._addressOf(particleSystem),
    )

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def setInstantaneousVY(
      self,
      vy: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::setInstantaneousVY(float vy,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledata.html#setInstantaneousVY

    Parameters
    ----------

    vy : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::setInstantaneousVY(float vy,
    #      QQuickParticleSystem *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData18setInstantaneousVYEfP20QQuickPartic'
        'leSystem',
        vy, self._addressOf(particleSystem),
    )

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def setInstantaneousY(
      self,
      y: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::setInstantaneousY(float y,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledata.html#setInstantaneousY

    Parameters
    ----------

    y : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::setInstantaneousY(float y,
    #      QQuickParticleSystem *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData17setInstantaneousYEfP20QQuickParticl'
        'eSystem',
        y, self._addressOf(particleSystem),
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

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def debugDump(
      self,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::debugDump(QQuickParticleSystem
    *particleSystem) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#debugDump

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::debugDump(QQuickParticleSystem
    #      *particleSystem) const
    self.uglySide.call(
        'ritual_ZNK18QQuickParticleData9debugDumpEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def v4Value(
      self,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> QQuickV4ParticleData:
    """
    Calls Qt's 'QQuickV4ParticleData
    QQuickParticleData::v4Value(QQuickParticleSystem *particleSystem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#v4Value

    Parameters
    ----------

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickV4ParticleData
      A new cute QQuickV4ParticleData around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickV4ParticleData QQuickParticleData::v4Value(QQuickParticleSystem
    #      *particleSystem)
    address = self.uglySide.call(
        'ritual_ZN18QQuickParticleData7v4ValueEP20QQuickParticleSystem',
        self._addressOf(particleSystem),
    )
    from . import QQuickV4ParticleData
    return QQuickV4ParticleData._cuteOwning(address)

  @overload(float, QQuickParticleSystem)
  @overload(float, NoneType)
  def extendLife(
      self,
      time: float,
      particleSystem: Optional[QQuickParticleSystem],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleData::extendLife(float time,
    QQuickParticleSystem *particleSystem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledata.html#extendLife

    Parameters
    ----------

    time : float
      Passed on as it is.

    particleSystem : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleData::extendLife(float time, QQuickParticleSystem
    #      *particleSystem)
    self.uglySide.call(
        'ritual_ZN18QQuickParticleData10extendLifeEfP20QQuickParticleSystem',
        time, self._addressOf(particleSystem),
    )


#  Qt's 'QList<QQuickParticleData *>': the list of QQuickParticleData, which
#  'QList[QQuickParticleData]' gives. It is made here, so that there is one
#  as soon as there can be a QQuickParticleData.
QList.createKind(
    QQuickParticleData, 'address',
    make='ritual_list_make_QQuickParticleData_ptr',
    add='ritual_list_add_QQuickParticleData_ptr',
    size='ritual_list_size_QQuickParticleData_ptr',
    at='ritual_list_at_QQuickParticleData_ptr',
    drop='ritual_list_drop_QQuickParticleData_ptr',
)
