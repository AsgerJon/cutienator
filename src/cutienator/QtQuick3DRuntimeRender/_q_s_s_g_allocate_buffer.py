"""
QSSGAllocateBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAllocateBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGCommand


class QSSGAllocateBuffer(QSSGCommand):
  """
  The cute side of Qt's QSSGAllocateBuffer: a plain Python object standing in
  front of one C++ QSSGAllocateBuffer.

  It is built on the cute 'QSSGCommand', as Qt's QSSGAllocateBuffer is built
  on Qt's QSSGCommand, and has everything that class has.

  C++ hands a QSSGAllocateBuffer around as a copy, so every C++
  QSSGAllocateBuffer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGAllocateBuffer yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGAllocateBuffer::QSSGAllocateBuffer(const QByteArray &inName,
    QSSGRenderTextureFormat inFormat, QSSGRenderTextureFilterOp inFilterOp,
    QSSGRenderTextureCoordOp inCoordOp, float inMultiplier,
    QSSGAllocateBufferFlags inFlags)': names the enum
    'QSSGRenderTextureFilterOp', whose class cannot be named here.
  - Qt's 'void QSSGAllocateBuffer::addDebug(QDebug &stream) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGAllocateBuffer::~QSSGAllocateBuffer()': the destructor: Python
    removes its C++ QSSGAllocateBuffer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGAllocateBuffer is created at the first use, not by
    'QSSGAllocateBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGAllocateBuffer back gives a copy the ritual made
    for Python, in a new cute QSSGAllocateBuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGAllocateBuffer'

  #  Qt's '~QSSGAllocateBuffer()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGAllocateBuffer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSSGAllocateBufferD1Ev'

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
    'QSSGAllocateBuffer::QSSGAllocateBuffer()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatebuffer.html#QSSGAllocateBuffer
    """
    #  QSSGAllocateBuffer::QSSGAllocateBuffer()
    self._noteCreation(QSSGAllocateBuffer, lambda: Rituals.call(
        'ritual_ZN18QSSGAllocateBufferC1Ev',
    ))

  @overload(THIS)
  def __init__(self, command: QSSGAllocateBuffer) -> None:
    """
    Notes what was given, for Qt's
    'QSSGAllocateBuffer::QSSGAllocateBuffer(const QSSGAllocateBuffer
    &command)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgallocatebuffer.html#QSSGAllocateBuffer

    Parameters
    ----------

    command : QSSGAllocateBuffer
      Passed on as a value: Qt reads the C++ QSSGAllocateBuffer, which stays
      Python's own.
    """
    #  QSSGAllocateBuffer::QSSGAllocateBuffer(const QSSGAllocateBuffer
    #      &command)
    self._noteCreation(QSSGAllocateBuffer, lambda: Rituals.call(
        'ritual_ZN18QSSGAllocateBufferC1ERKS_', self._valueOf(command),
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
