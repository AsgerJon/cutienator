"""
qfloat16 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfloat16.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Qt


class qfloat16(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qfloat16: a plain Python object standing in front of
  one C++ qfloat16.

  C++ hands a qfloat16 around as a copy, so every C++ qfloat16 behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qfloat16 that has a ritual and that Python can call
  so far, 14 names in all: 'isInf', 'isNaN', 'isFinite', 'fpClassify',
  'copySign', '_limit_epsilon', '_limit_min', '_limit_denorm_min',
  '_limit_max', '_limit_lowest', '_limit_infinity', '_limit_quiet_NaN',
  '_limit_signaling_NaN', 'isNormal'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'float qfloat16::operator float() const': an operator, which is not
    reflected yet.
  - Qt's 'qfloat16 qfloat16::operator++(int a0)': an operator, which is not
    reflected yet.
  - Qt's 'qfloat16 qfloat16::operator--(int a0)': an operator, which is not
    reflected yet.
  - Qt's 'qfloat16::~qfloat16()': the destructor: Python removes its C++
    qfloat16 by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ qfloat16 is created at the first use, not by 'qfloat16(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qfloat16 back gives a copy the ritual made for
    Python, in a new cute qfloat16.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _limit_epsilon() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_epsilon()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_epsilon

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_epsilon()
    address = Rituals.call('ritual_ZN8qfloat1614_limit_epsilonEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_min() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_min()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_min

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_min()
    address = Rituals.call('ritual_ZN8qfloat1610_limit_minEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_denorm_min() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_denorm_min()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_denorm_min

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_denorm_min()
    address = Rituals.call('ritual_ZN8qfloat1617_limit_denorm_minEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_max() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_max()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_max

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_max()
    address = Rituals.call('ritual_ZN8qfloat1610_limit_maxEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_lowest() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_lowest()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_lowest

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_lowest()
    address = Rituals.call('ritual_ZN8qfloat1613_limit_lowestEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_infinity() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_infinity()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_infinity

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_infinity()
    address = Rituals.call('ritual_ZN8qfloat1615_limit_infinityEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_quiet_NaN() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_quiet_NaN()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_quiet_NaN

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_quiet_NaN()
    address = Rituals.call('ritual_ZN8qfloat1616_limit_quiet_NaNEv')
    return qfloat16._cuteOwning(address)

  @staticmethod
  def _limit_signaling_NaN() -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::_limit_signaling_NaN()'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#_limit_signaling_NaN

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::_limit_signaling_NaN()
    address = Rituals.call('ritual_ZN8qfloat1620_limit_signaling_NaNEv')
    return qfloat16._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qfloat16'

  #  Qt's '~qfloat16()'. Naming it makes this a value class: Python owns
  #  every C++ qfloat16 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8qfloat16D1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInf(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isInf() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isInf
    """
    #  bool qfloat16::isInf() const
    return self.uglySide.call('ritual_ZNK8qfloat165isInfEv')

  def isNaN(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isNaN() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isNaN
    """
    #  bool qfloat16::isNaN() const
    return self.uglySide.call('ritual_ZNK8qfloat165isNaNEv')

  def isFinite(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isFinite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isFinite
    """
    #  bool qfloat16::isFinite() const
    return self.uglySide.call('ritual_ZNK8qfloat168isFiniteEv')

  def fpClassify(self) -> int:
    """
    Calls Qt's 'int qfloat16::fpClassify() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#fpClassify
    """
    #  int qfloat16::fpClassify() const
    return self.uglySide.call('ritual_ZNK8qfloat1610fpClassifyEv')

  @overload(THIS)
  def copySign(self, sign: qfloat16) -> qfloat16:
    """
    Calls Qt's 'qfloat16 qfloat16::copySign(qfloat16 sign) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#copySign

    Parameters
    ----------

    sign : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.

    Returns
    -------

    qfloat16
      A new cute qfloat16 around the copy Qt gave back. Python owns it.
    """
    #  qfloat16 qfloat16::copySign(qfloat16 sign) const
    address = self.uglySide.call(
        'ritual_ZNK8qfloat168copySignES_', self._valueOf(sign),
    )
    return qfloat16._cuteOwning(address)

  def isNormal(self) -> bool:
    """
    Calls Qt's 'bool qfloat16::isNormal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#isNormal
    """
    #  bool qfloat16::isNormal() const
    return self.uglySide.call('ritual_ZNK8qfloat168isNormalEv')

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

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's 'qfloat16::qfloat16(Qt::Initialization
    a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#qfloat16

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  qfloat16::qfloat16(Qt::Initialization a0)
    self._noteCreation(qfloat16, lambda: Rituals.call(
        'ritual_ZN8qfloat16C1EN2Qt14InitializationE', a0.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'qfloat16::qfloat16()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#qfloat16
    """
    #  qfloat16::qfloat16()
    self._noteCreation(qfloat16, lambda: Rituals.call(
        'ritual_ZN8qfloat16C1Ev',
    ))

  @overload(float)
  def __init__(self, f: float) -> None:
    """
    Notes what was given, for Qt's 'qfloat16::qfloat16(float f)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfloat16.html#qfloat16

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  qfloat16::qfloat16(float f)
    self._noteCreation(qfloat16, lambda: Rituals.call(
        'ritual_ZN8qfloat16C1Ef', f,
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
