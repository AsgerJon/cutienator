"""
QRandomGenerator64 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrandom.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QRandomGenerator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QRandomGenerator64(QRandomGenerator):
  """
  The cute side of Qt's QRandomGenerator64: a plain Python object standing in
  front of one C++ QRandomGenerator64.

  It is built on the cute 'QRandomGenerator', as Qt's QRandomGenerator64 is
  built on Qt's QRandomGenerator, and has everything that class has.

  C++ hands a QRandomGenerator64 around as a copy, so every C++
  QRandomGenerator64 behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRandomGenerator64 that has a ritual and that Python
  can call so far, 8 names in all: 'generate', '__call__', 'discard', 'min',
  'max', 'system', 'global_', 'securelySeeded'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRandomGenerator64::~QRandomGenerator64()': the destructor: Python
    removes its C++ QRandomGenerator64 by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QRandomGenerator64 is created at the first use, not by
    'QRandomGenerator64(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRandomGenerator64 back gives a copy the ritual made
    for Python, in a new cute QRandomGenerator64.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def min() -> int:
    """
    Calls Qt's 'result_type QRandomGenerator64::min()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#min
    """
    #  result_type QRandomGenerator64::min()
    return Rituals.call('ritual_ZN18QRandomGenerator643minEv')

  @staticmethod
  def max() -> int:
    """
    Calls Qt's 'result_type QRandomGenerator64::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#max
    """
    #  result_type QRandomGenerator64::max()
    return Rituals.call('ritual_ZN18QRandomGenerator643maxEv')

  @staticmethod
  def system() -> Optional[QRandomGenerator64]:
    """
    Calls Qt's 'QRandomGenerator64 *QRandomGenerator64::system()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#system

    Returns
    -------

    Optional[QRandomGenerator64]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomGenerator64 *QRandomGenerator64::system()
    address = Rituals.call('ritual_ZN18QRandomGenerator646systemEv')
    return QRandomGenerator64._cuteAt(address)

  @staticmethod
  def global_() -> Optional[QRandomGenerator64]:
    """
    Calls Qt's 'QRandomGenerator64 *QRandomGenerator64::global()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#global

    Returns
    -------

    Optional[QRandomGenerator64]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRandomGenerator64 *QRandomGenerator64::global()
    address = Rituals.call('ritual_ZN18QRandomGenerator646globalEv')
    return QRandomGenerator64._cuteAt(address)

  @staticmethod
  def securelySeeded() -> QRandomGenerator64:
    """
    Calls Qt's 'QRandomGenerator64 QRandomGenerator64::securelySeeded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator64.html#securelySeeded

    Returns
    -------

    QRandomGenerator64
      A new cute QRandomGenerator64 around the copy Qt gave back. Python owns
      it.
    """
    #  QRandomGenerator64 QRandomGenerator64::securelySeeded()
    address = Rituals.call('ritual_ZN18QRandomGenerator6414securelySeededEv')
    return QRandomGenerator64._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRandomGenerator64'

  #  Qt's '~QRandomGenerator64()'. Naming it makes this a value class: Python
  #  owns every C++ QRandomGenerator64 behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QRandomGenerator64D1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __call__(self) -> int:
    """
    Calls Qt's 'result_type QRandomGenerator64::operator()()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#operator()
    """
    #  result_type QRandomGenerator64::operator()()
    return self.uglySide.call('ritual_ZN18QRandomGenerator64clEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(int)
  def __init__(self, seedValue: int = 1) -> None:
    """
    Notes what was given, for Qt's
    'QRandomGenerator64::QRandomGenerator64(quint32 seedValue)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator64.html#QRandomGenerator64

    Parameters
    ----------

    seedValue : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QRandomGenerator64::QRandomGenerator64(quint32 seedValue)
    self._noteCreation(QRandomGenerator64, lambda: Rituals.call(
        'ritual_ZN18QRandomGenerator64C1Ej', seedValue,
    ))

  @overload(QRandomGenerator)
  def __init__(self, other: QRandomGenerator) -> None:
    """
    Notes what was given, for Qt's
    'QRandomGenerator64::QRandomGenerator64(const QRandomGenerator &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrandomgenerator64.html#QRandomGenerator64

    Parameters
    ----------

    other : QRandomGenerator
      Passed on as a value: Qt reads the C++ QRandomGenerator, which stays
      Python's own.
    """
    #  QRandomGenerator64::QRandomGenerator64(const QRandomGenerator &other)
    self._noteCreation(QRandomGenerator64, lambda: Rituals.call(
        'ritual_ZN18QRandomGenerator64C1ERK16QRandomGenerator',
        self._valueOf(other),
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

  def generate(self) -> int:
    """
    Calls Qt's 'quint64 QRandomGenerator64::generate()'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#generate
    """
    #  quint64 QRandomGenerator64::generate()
    return self.uglySide.call('ritual_ZN18QRandomGenerator648generateEv')

  @overload(int)
  def discard(self, z: int) -> None:
    """
    Calls Qt's 'void QRandomGenerator64::discard(unsigned long long z)'.

    Qt's own words: https://doc.qt.io/qt-6/qrandomgenerator64.html#discard

    Parameters
    ----------

    z : int
      Passed on as it is.
    """
    #  void QRandomGenerator64::discard(unsigned long long z)
    self.uglySide.call('ritual_ZN18QRandomGenerator647discardEy', z)
