"""
QPRand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlerandomizer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QPRand to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRandomGenerator


class QPRand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPRand: a plain Python object standing in front of
  one C++ QPRand.

  C++ hands a QPRand around as a copy, so every C++ QPRand behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPRand that has a ritual and that Python can call so
  far, 4 names in all: 'init', 'setDeterministic', 'get', 'generator'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPRand::~QPRand()': the destructor: Python removes its C++ QPRand
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPRand is created at the first use, not by 'QPRand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPRand back gives a copy the ritual made for Python,
    in a new cute QPRand.
  """

  #  The enums Qt writes inside QPRand, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class UserType(CuteNum):
    """
    The enum 'QPRand::UserType' of Qt, with the 41 names Qt gives in it.
    """

    Default = Kee[int](0)
    WanderXPS = Kee[int](1)
    WanderYPS = Kee[int](2)
    WanderZPS = Kee[int](3)
    WanderXPV = Kee[int](4)
    WanderYPV = Kee[int](5)
    WanderZPV = Kee[int](6)
    WanderXAV = Kee[int](7)
    WanderYAV = Kee[int](8)
    WanderZAV = Kee[int](9)
    AttractorDurationV = Kee[int](10)
    AttractorPosVX = Kee[int](11)
    AttractorPosVY = Kee[int](12)
    AttractorPosVZ = Kee[int](13)
    Shape1 = Kee[int](14)
    Shape2 = Kee[int](15)
    Shape3 = Kee[int](16)
    Shape4 = Kee[int](17)
    SpriteAnimationI = Kee[int](18)
    DeterministicSeparator = Kee[int](19)
    LifeSpanV = Kee[int](20)
    ScaleV = Kee[int](21)
    ScaleEV = Kee[int](22)
    RotXV = Kee[int](23)
    RotYV = Kee[int](24)
    RotZV = Kee[int](25)
    RotXVV = Kee[int](26)
    RotYVV = Kee[int](27)
    RotZVV = Kee[int](28)
    ColorRV = Kee[int](29)
    ColorGV = Kee[int](30)
    ColorBV = Kee[int](31)
    ColorAV = Kee[int](32)
    TDirPosXV = Kee[int](33)
    TDirPosYV = Kee[int](34)
    TDirPosZV = Kee[int](35)
    TDirMagV = Kee[int](36)
    VDirXV = Kee[int](37)
    VDirYV = Kee[int](38)
    VDirZV = Kee[int](39)
    SpriteAnimationV = Kee[int](40)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPRand'

  #  Qt's '~QPRand()'. Naming it makes this a value class: Python owns every
  #  C++ QPRand behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QPRandD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def generator(self) -> QRandomGenerator:
    """
    Calls Qt's 'QRandomGenerator QPRand::generator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprand.html#generator

    Returns
    -------

    QRandomGenerator
      A new cute QRandomGenerator around the copy Qt gave back. Python owns
      it.
    """
    #  QRandomGenerator QPRand::generator() const
    address = self.uglySide.call('ritual_ZNK6QPRand9generatorEv')
    from ..QtCore import QRandomGenerator
    return QRandomGenerator._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDeterministic(self, deterministic: bool) -> None:
    """
    Calls Qt's 'void QPRand::setDeterministic(bool deterministic)'.

    Qt's own words: https://doc.qt.io/qt-6/qprand.html#setDeterministic

    Parameters
    ----------

    deterministic : bool
      Passed on as it is.
    """
    #  void QPRand::setDeterministic(bool deterministic)
    self.uglySide.call('ritual_ZN6QPRand16setDeterministicEb', deterministic)

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

  @overload(int)
  @overload(int, int)
  def init(self, seed: int, size: int = 65536) -> None:
    """
    Calls Qt's 'void QPRand::init(quint32 seed, int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qprand.html#init

    Parameters
    ----------

    seed : int
      Passed on as it is.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then 65536.
    """
    #  void QPRand::init(quint32 seed, int size)
    self.uglySide.call('ritual_ZN6QPRand4initEji', seed, size)

  @overload(int)
  @overload(int, UserType)
  def get(
      self,
      particleIndex: int,
      user: UserType = UserType.Default,
  ) -> float:
    """
    Calls Qt's 'float QPRand::get(int particleIndex, UserType user)'.

    Qt's own words: https://doc.qt.io/qt-6/qprand.html#get

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    user : UserType
      Passed on as its number. May be left out, as in Qt: it is then
      UserType.Default.
    """
    #  float QPRand::get(int particleIndex, UserType user)
    return self.uglySide.call(
        'ritual_ZN6QPRand3getEiNS_8UserTypeE', particleIndex, user.value,
    )

  @overload()
  def get(self) -> float:
    """
    Calls Qt's 'float QPRand::get()'.

    Qt's own words: https://doc.qt.io/qt-6/qprand.html#get
    """
    #  float QPRand::get()
    return self.uglySide.call('ritual_ZN6QPRand3getEv')
