"""
QSSGAddShaderDefine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGAddShaderDefine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSSGCommand

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSSGAddShaderDefine(QSSGCommand):
  """
  The cute side of Qt's QSSGAddShaderDefine: a plain Python object standing
  in front of one C++ QSSGAddShaderDefine.

  It is built on the cute 'QSSGCommand', as Qt's QSSGAddShaderDefine is built
  on Qt's QSSGCommand, and has everything that class has.

  C++ hands a QSSGAddShaderDefine around as a copy, so every C++
  QSSGAddShaderDefine behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGAddShaderDefine yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGAddShaderDefine::addDebug(QDebug &stream) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSSGAddShaderDefine::~QSSGAddShaderDefine()': the destructor:
    Python removes its C++ QSSGAddShaderDefine by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGAddShaderDefine is created at the first use, not by
    'QSSGAddShaderDefine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGAddShaderDefine back gives a copy the ritual made
    for Python, in a new cute QSSGAddShaderDefine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGAddShaderDefine'

  #  Qt's '~QSSGAddShaderDefine()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGAddShaderDefine behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGAddShaderDefineD1Ev'

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
    'QSSGAddShaderDefine::QSSGAddShaderDefine()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgaddshaderdefine.html#QSSGAddShaderDefine
    """
    #  QSSGAddShaderDefine::QSSGAddShaderDefine()
    self._noteCreation(QSSGAddShaderDefine, lambda: Rituals.call(
        'ritual_ZN19QSSGAddShaderDefineC1Ev',
    ))

  @overload(QByteArray)
  @overload(QByteArray, int)
  def __init__(self, name: QByteArray, value: int = 0) -> None:
    """
    Notes what was given, for Qt's
    'QSSGAddShaderDefine::QSSGAddShaderDefine(const QByteArray &name, int
    value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgaddshaderdefine.html#QSSGAddShaderDefine

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QSSGAddShaderDefine::QSSGAddShaderDefine(const QByteArray &name, int
    #      value)
    self._noteCreation(QSSGAddShaderDefine, lambda: Rituals.call(
        'ritual_ZN19QSSGAddShaderDefineC1ERK10QByteArrayi',
        self._valueOf(name), value,
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
