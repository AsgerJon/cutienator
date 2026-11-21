"""
QSemaphoreReleaser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsemaphore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSemaphore
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSemaphore = WAIT['QSemaphore']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSemaphoreReleaser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSemaphoreReleaser: a plain Python object standing in
  front of one C++ QSemaphoreReleaser.

  What exists
  -----------

  Every function of Qt's QSemaphoreReleaser that has a ritual and that Python
  can call so far, 2 names in all: 'semaphore', 'cancel'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSemaphoreReleaser::~QSemaphoreReleaser()': the destructor: Python
    never removes a C++ QSemaphoreReleaser.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QSemaphoreReleaser is created at the first use, not by
    'QSemaphoreReleaser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSemaphoreReleaser.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSemaphoreReleaser'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def semaphore(self) -> Optional[QSemaphore]:
    """
    Calls Qt's 'QSemaphore *QSemaphoreReleaser::semaphore() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphorereleaser.html#semaphore

    Returns
    -------

    Optional[QSemaphore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSemaphore *QSemaphoreReleaser::semaphore() const
    address = self.uglySide.call(
        'ritual_ZNK18QSemaphoreReleaser9semaphoreEv',
    )
    from . import QSemaphore
    return QSemaphore._cuteAt(address)

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
    'QSemaphoreReleaser::QSemaphoreReleaser()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsemaphorereleaser.html#QSemaphoreReleaser
    """
    #  QSemaphoreReleaser::QSemaphoreReleaser()
    self._noteCreation(QSemaphoreReleaser, lambda: Rituals.call(
        'ritual_ZN18QSemaphoreReleaserC1Ev',
    ))

  @overload(QSemaphore)
  @overload(NoneType)
  @overload(QSemaphore, int)
  @overload(NoneType, int)
  def __init__(self, sem: Optional[QSemaphore], n: int = 1) -> None:
    """
    Notes what was given, for Qt's
    'QSemaphoreReleaser::QSemaphoreReleaser(QSemaphore *sem, int n)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsemaphorereleaser.html#QSemaphoreReleaser

    Parameters
    ----------

    sem : Optional[QSemaphore]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QSemaphoreReleaser::QSemaphoreReleaser(QSemaphore *sem, int n)
    self._noteCreation(QSemaphoreReleaser, lambda: Rituals.call(
        'ritual_ZN18QSemaphoreReleaserC1EP10QSemaphorei',
        self._addressOf(sem), n,
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

  def cancel(self) -> Optional[QSemaphore]:
    """
    Calls Qt's 'QSemaphore *QSemaphoreReleaser::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphorereleaser.html#cancel

    Returns
    -------

    Optional[QSemaphore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSemaphore *QSemaphoreReleaser::cancel()
    address = self.uglySide.call('ritual_ZN18QSemaphoreReleaser6cancelEv')
    from . import QSemaphore
    return QSemaphore._cuteAt(address)
