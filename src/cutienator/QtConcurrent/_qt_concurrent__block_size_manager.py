"""
QtConcurrent::BlockSizeManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtConcurrent/qtconcurrentiteratekernel.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QThreadPool
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QThreadPool = WAIT['QThreadPool']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BlockSizeManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtConcurrent::BlockSizeManager: a plain Python object
  standing in front of one C++ QtConcurrent::BlockSizeManager.

  What exists
  -----------

  Every function of Qt's QtConcurrent::BlockSizeManager that has a ritual and
  that Python can call so far, 4 names in all: 'timeBeforeUser',
  'timeAfterUser', 'blockSize', 'blockSizeMaxed'. It can be made from Python,
  in 1 way; see '__init__'.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QtConcurrent::BlockSizeManager is created at the first use, not
    by 'QtConcurrent::BlockSizeManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtConcurrent::BlockSizeManager.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtConcurrent::BlockSizeManager'

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

  @overload(QThreadPool, int)
  @overload(NoneType, int)
  def __init__(
      self,
      pool: Optional[QThreadPool],
      iterationCount: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtConcurrent::BlockSizeManager::BlockSizeManager(QThreadPool *pool, int
    iterationCount)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-blocksizemanager.html

    Parameters
    ----------

    pool : Optional[QThreadPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iterationCount : int
      Passed on as it is.
    """
    #  QtConcurrent::BlockSizeManager::BlockSizeManager(QThreadPool *pool,
    #      int iterationCount)
    self._noteCreation(BlockSizeManager, lambda: Rituals.call(
        'ritual_ZN12QtConcurrent16BlockSizeManagerC1EP11QThreadPooli',
        self._addressOf(pool), iterationCount,
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

  def timeBeforeUser(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::BlockSizeManager::timeBeforeUser()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-blocksizemanager.html#timeBeforeUser
    """
    #  void QtConcurrent::BlockSizeManager::timeBeforeUser()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16BlockSizeManager14timeBeforeUserEv',
    )

  def timeAfterUser(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::BlockSizeManager::timeAfterUser()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-blocksizemanager.html#timeAfterUser
    """
    #  void QtConcurrent::BlockSizeManager::timeAfterUser()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16BlockSizeManager13timeAfterUserEv',
    )

  def blockSize(self) -> int:
    """
    Calls Qt's 'int QtConcurrent::BlockSizeManager::blockSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-blocksizemanager.html#blockSize
    """
    #  int QtConcurrent::BlockSizeManager::blockSize()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent16BlockSizeManager9blockSizeEv',
    )

  def blockSizeMaxed(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::BlockSizeManager::blockSizeMaxed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-blocksizemanager.html#blockSizeMaxed
    """
    #  bool QtConcurrent::BlockSizeManager::blockSizeMaxed()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent16BlockSizeManager14blockSizeMaxedEv',
    )
