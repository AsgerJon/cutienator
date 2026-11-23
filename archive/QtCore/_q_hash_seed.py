"""
QHashSeed binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qhashfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QHashSeed(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHashSeed: a plain Python object standing in front of
  one C++ QHashSeed.

  C++ hands a QHashSeed around as a copy, so every C++ QHashSeed behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHashSeed that has a ritual and that Python can call
  so far, 3 names in all: 'globalSeed', 'setDeterministicGlobalSeed',
  'resetRandomGlobalSeed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHashSeed::~QHashSeed()': the destructor: Python removes its C++
    QHashSeed by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QHashSeed is created at the first use, not by 'QHashSeed(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHashSeed back gives a copy the ritual made for
    Python, in a new cute QHashSeed.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def globalSeed() -> QHashSeed:
    """
    Calls Qt's 'QHashSeed QHashSeed::globalSeed()'.

    Qt's own words: https://doc.qt.io/qt-6/qhashseed.html#globalSeed

    Returns
    -------

    QHashSeed
      A new cute QHashSeed around the copy Qt gave back. Python owns it.
    """
    #  QHashSeed QHashSeed::globalSeed()
    address = Rituals.call('ritual_ZN9QHashSeed10globalSeedEv')
    return QHashSeed._cuteOwning(address)

  @staticmethod
  def setDeterministicGlobalSeed() -> None:
    """
    Calls Qt's 'void QHashSeed::setDeterministicGlobalSeed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashseed.html#setDeterministicGlobalSeed
    """
    #  void QHashSeed::setDeterministicGlobalSeed()
    Rituals.call('ritual_ZN9QHashSeed26setDeterministicGlobalSeedEv')

  @staticmethod
  def resetRandomGlobalSeed() -> None:
    """
    Calls Qt's 'void QHashSeed::resetRandomGlobalSeed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhashseed.html#resetRandomGlobalSeed
    """
    #  void QHashSeed::resetRandomGlobalSeed()
    Rituals.call('ritual_ZN9QHashSeed21resetRandomGlobalSeedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHashSeed'

  #  Qt's '~QHashSeed()'. Naming it makes this a value class: Python owns
  #  every C++ QHashSeed behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QHashSeedD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(int)
  def __init__(self, d: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QHashSeed::QHashSeed(size_t d)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhashseed.html#QHashSeed

    Parameters
    ----------

    d : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QHashSeed::QHashSeed(size_t d)
    self._noteCreation(QHashSeed, lambda: Rituals.call(
        'ritual_ZN9QHashSeedC1Em', d,
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
