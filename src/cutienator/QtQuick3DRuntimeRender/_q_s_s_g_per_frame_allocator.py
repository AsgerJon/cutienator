"""
QSSGPerFrameAllocator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGPerFrameAllocator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGPerFrameAllocator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGPerFrameAllocator: a plain Python object standing
  in front of one C++ QSSGPerFrameAllocator.

  C++ hands a QSSGPerFrameAllocator around as a copy, so every C++
  QSSGPerFrameAllocator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGPerFrameAllocator that has a ritual and that
  Python can call so far, 1 name in all: 'reset'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSSGPerFrameAllocator::allocate(size_t size)': gives 'void',
    which has no cute class yet.
  - Qt's 'QSSGPerFrameAllocator::~QSSGPerFrameAllocator()': the destructor:
    Python removes its C++ QSSGPerFrameAllocator by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGPerFrameAllocator is created at the first use, not by
    'QSSGPerFrameAllocator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGPerFrameAllocator back gives a copy the ritual
    made for Python, in a new cute QSSGPerFrameAllocator.
  - Each name of Qt's QSSGPerFrameAllocator that has no cute function yet,
    'allocate', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGPerFrameAllocator'

  #  Qt's '~QSSGPerFrameAllocator()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGPerFrameAllocator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSSGPerFrameAllocatorD1Ev'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGPerFrameAllocator::QSSGPerFrameAllocator()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgperframeallocator.html#QSSGPerFrameAllocator
    """
    #  QSSGPerFrameAllocator::QSSGPerFrameAllocator()
    self._noteCreation(QSSGPerFrameAllocator, lambda: Rituals.call(
        'ritual_ZN21QSSGPerFrameAllocatorC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QSSGPerFrameAllocator::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qssgperframeallocator.html#reset
    """
    #  void QSSGPerFrameAllocator::reset()
    self.uglySide.call('ritual_ZN21QSSGPerFrameAllocator5resetEv')

  @staticmethod
  def allocate(*__, **_) -> Never:
    """
    Qt's 'void *QSSGPerFrameAllocator::allocate(size_t size)': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGPerFrameAllocator.allocate' has no cute function yet. Qt's "
        "'void *QSSGPerFrameAllocator::allocate(size_t size)': gives "
        "'void', which has no cute class yet.")
