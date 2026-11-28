"""
QQuickParticleDataHeap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleDataHeap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleDataHeap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickParticleDataHeap: a plain Python object
  standing in front of one C++ QQuickParticleDataHeap.

  C++ hands a QQuickParticleDataHeap around as a copy, so every C++
  QQuickParticleDataHeap behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickParticleDataHeap that has a ritual and that
  Python can call so far, 10 names in all: 'insert', 'insertTimed', 'top',
  'isEmpty', 'clear', 'contains', 'grow', 'swap', 'bubbleUp', 'bubbleDown'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSet<QQuickParticleData *> QQuickParticleDataHeap::pop()': gives a
    type Python has no way to take yet.
  - Qt's 'QQuickParticleDataHeap::~QQuickParticleDataHeap()': the destructor:
    Python removes its C++ QQuickParticleDataHeap by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickParticleDataHeap is created at the first use, not by
    'QQuickParticleDataHeap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickParticleDataHeap back gives a copy the ritual
    made for Python, in a new cute QQuickParticleDataHeap.
  - Each name of Qt's QQuickParticleDataHeap that has no cute function yet,
    'pop', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQuickParticleDataHeap'

  #  Qt's '~QQuickParticleDataHeap()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickParticleDataHeap behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QQuickParticleDataHeapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleDataHeap::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledataheap.html#isEmpty
    """
    #  bool QQuickParticleDataHeap::isEmpty() const
    return self.uglySide.call('ritual_ZNK22QQuickParticleDataHeap7isEmptyEv')

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
    'QQuickParticleDataHeap::QQuickParticleDataHeap()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledataheap.html#QQuickParticleDataHeap
    """
    #  QQuickParticleDataHeap::QQuickParticleDataHeap()
    self._noteCreation(QQuickParticleDataHeap, lambda: Rituals.call(
        'ritual_ZN22QQuickParticleDataHeapC1Ev',
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

  @overload(QQuickParticleData)
  @overload(NoneType)
  def insert(self, data: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::insert(QQuickParticleData
    *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledataheap.html#insert

    Parameters
    ----------

    data : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleDataHeap::insert(QQuickParticleData *data)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleDataHeap6insertEP18QQuickParticleData',
        self._addressOf(data),
    )

  @overload(QQuickParticleData, int)
  @overload(NoneType, int)
  def insertTimed(
      self,
      data: Optional[QQuickParticleData],
      time: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::insertTimed(QQuickParticleData
    *data, int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledataheap.html#insertTimed

    Parameters
    ----------

    data : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    time : int
      Passed on as it is.
    """
    #  void QQuickParticleDataHeap::insertTimed(QQuickParticleData *data, int
    #      time)
    self.uglySide.call(
        'ritual_ZN22QQuickParticleDataHeap11insertTimedEP18QQuickParticleDa'
        'tai',
        self._addressOf(data), time,
    )

  def top(self) -> int:
    """
    Calls Qt's 'int QQuickParticleDataHeap::top()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledataheap.html#top
    """
    #  int QQuickParticleDataHeap::top()
    return self.uglySide.call('ritual_ZN22QQuickParticleDataHeap3topEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledataheap.html#clear
    """
    #  void QQuickParticleDataHeap::clear()
    self.uglySide.call('ritual_ZN22QQuickParticleDataHeap5clearEv')

  @overload(QQuickParticleData)
  @overload(NoneType)
  def contains(self, a0: Optional[QQuickParticleData]) -> bool:
    """
    Calls Qt's 'bool QQuickParticleDataHeap::contains(QQuickParticleData
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledataheap.html#contains

    Parameters
    ----------

    a0 : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickParticleDataHeap::contains(QQuickParticleData *a0)
    return self.uglySide.call(
        'ritual_ZN22QQuickParticleDataHeap8containsEP18QQuickParticleData',
        self._addressOf(a0),
    )

  def grow(self) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::grow()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledataheap.html#grow
    """
    #  void QQuickParticleDataHeap::grow()
    self.uglySide.call('ritual_ZN22QQuickParticleDataHeap4growEv')

  @overload(int, int)
  def swap(self, a0: int, a1: int) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::swap(int a0, int a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticledataheap.html#swap

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  void QQuickParticleDataHeap::swap(int a0, int a1)
    self.uglySide.call('ritual_ZN22QQuickParticleDataHeap4swapEii', a0, a1)

  @overload(int)
  def bubbleUp(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::bubbleUp(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledataheap.html#bubbleUp

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickParticleDataHeap::bubbleUp(int a0)
    self.uglySide.call('ritual_ZN22QQuickParticleDataHeap8bubbleUpEi', a0)

  @overload(int)
  def bubbleDown(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickParticleDataHeap::bubbleDown(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticledataheap.html#bubbleDown

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickParticleDataHeap::bubbleDown(int a0)
    self.uglySide.call('ritual_ZN22QQuickParticleDataHeap10bubbleDownEi', a0)

  @staticmethod
  def pop(*__, **_) -> Never:
    """
    Qt's 'QSet<QQuickParticleData *> QQuickParticleDataHeap::pop()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickParticleDataHeap.pop' has no cute function yet. Qt's "
        "'QSet<QQuickParticleData *> QQuickParticleDataHeap::pop()': gives "
        "a type Python has no way to take yet.")
