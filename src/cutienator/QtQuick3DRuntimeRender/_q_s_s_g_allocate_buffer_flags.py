"""
QSSGAllocateBufferFlags binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAllocateBufferFlags to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSSGAllocateBufferFlags(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGAllocateBufferFlags: a plain Python object
  standing in front of one C++ QSSGAllocateBufferFlags.

  C++ hands a QSSGAllocateBufferFlags around as a copy, so every C++
  QSSGAllocateBufferFlags behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGAllocateBufferFlags that has a ritual and that
  Python can call so far, 2 names in all: 'setSceneLifetime',
  'isSceneLifetime'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGAllocateBufferFlags::~QSSGAllocateBufferFlags()': the
    destructor: Python removes its C++ QSSGAllocateBufferFlags by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QSSGAllocateBufferFlags is created at the first use, not by
    'QSSGAllocateBufferFlags(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGAllocateBufferFlags back gives a copy the ritual
    made for Python, in a new cute QSSGAllocateBufferFlags.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGAllocateBufferFlags'

  #  Qt's '~QSSGAllocateBufferFlags()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGAllocateBufferFlags behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSSGAllocateBufferFlagsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSceneLifetime(self) -> bool:
    """
    Calls Qt's 'bool QSSGAllocateBufferFlags::isSceneLifetime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatebufferflags.html#isSceneLifetime
    """
    #  bool QSSGAllocateBufferFlags::isSceneLifetime() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGAllocateBufferFlags15isSceneLifetimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSceneLifetime(self, inValue: bool) -> None:
    """
    Calls Qt's 'void QSSGAllocateBufferFlags::setSceneLifetime(bool
    inValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatebufferflags.html#setSceneLifetime

    Parameters
    ----------

    inValue : bool
      Passed on as it is.
    """
    #  void QSSGAllocateBufferFlags::setSceneLifetime(bool inValue)
    self.uglySide.call(
        'ritual_ZN23QSSGAllocateBufferFlags16setSceneLifetimeEb', inValue,
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

  @overload(int)
  def __init__(self, inValues: int) -> None:
    """
    Notes what was given, for Qt's
    'QSSGAllocateBufferFlags::QSSGAllocateBufferFlags(quint32 inValues)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatebufferflags.html

    Parameters
    ----------

    inValues : int
      Passed on as it is.
    """
    #  QSSGAllocateBufferFlags::QSSGAllocateBufferFlags(quint32 inValues)
    self._noteCreation(QSSGAllocateBufferFlags, lambda: Rituals.call(
        'ritual_ZN23QSSGAllocateBufferFlagsC1Ej', inValues,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGAllocateBufferFlags::QSSGAllocateBufferFlags()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatebufferflags.html
    """
    #  QSSGAllocateBufferFlags::QSSGAllocateBufferFlags()
    self._noteCreation(QSSGAllocateBufferFlags, lambda: Rituals.call(
        'ritual_ZN23QSSGAllocateBufferFlagsC1Ev',
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
