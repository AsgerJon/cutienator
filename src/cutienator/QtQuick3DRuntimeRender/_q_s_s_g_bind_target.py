"""
QSSGBindTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGBindTarget to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSSGCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtQuick3DUtils import QSSGRenderTextureFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderTextureFormat = WAIT['QSSGRenderTextureFormat']


class QSSGBindTarget(QSSGCommand):
  """
  The cute side of Qt's QSSGBindTarget: a plain Python object standing in
  front of one C++ QSSGBindTarget.

  It is built on the cute 'QSSGCommand', as Qt's QSSGBindTarget is built on
  Qt's QSSGCommand, and has everything that class has.

  C++ hands a QSSGBindTarget around as a copy, so every C++ QSSGBindTarget
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGBindTarget yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGBindTarget::addDebug(QDebug &stream) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGBindTarget::~QSSGBindTarget()': the destructor: Python removes
    its C++ QSSGBindTarget by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGBindTarget is created at the first use, not by
    'QSSGBindTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGBindTarget back gives a copy the ritual made for
    Python, in a new cute QSSGBindTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGBindTarget'

  #  Qt's '~QSSGBindTarget()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGBindTarget behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSSGBindTargetD1Ev'

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

  @overload(QSSGRenderTextureFormat)
  def __init__(self, inFormat: QSSGRenderTextureFormat) -> None:
    """
    Notes what was given, for Qt's
    'QSSGBindTarget::QSSGBindTarget(QSSGRenderTextureFormat inFormat)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgbindtarget.html#QSSGBindTarget

    Parameters
    ----------

    inFormat : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.
    """
    #  QSSGBindTarget::QSSGBindTarget(QSSGRenderTextureFormat inFormat)
    self._noteCreation(QSSGBindTarget, lambda: Rituals.call(
        'ritual_ZN14QSSGBindTargetC1E23QSSGRenderTextureFormat',
        self._valueOf(inFormat),
    ))

  @overload(THIS)
  def __init__(self, command: QSSGBindTarget) -> None:
    """
    Notes what was given, for Qt's 'QSSGBindTarget::QSSGBindTarget(const
    QSSGBindTarget &command)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgbindtarget.html#QSSGBindTarget

    Parameters
    ----------

    command : QSSGBindTarget
      Passed on as a value: Qt reads the C++ QSSGBindTarget, which stays
      Python's own.
    """
    #  QSSGBindTarget::QSSGBindTarget(const QSSGBindTarget &command)
    self._noteCreation(QSSGBindTarget, lambda: Rituals.call(
        'ritual_ZN14QSSGBindTargetC1ERKS_', self._valueOf(command),
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
