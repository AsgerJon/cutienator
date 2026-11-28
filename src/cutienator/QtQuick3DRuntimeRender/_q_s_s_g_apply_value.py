"""
QSSGApplyValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGApplyValue to be private: it declares the class in a header
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
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QSSGApplyValue(QSSGCommand):
  """
  The cute side of Qt's QSSGApplyValue: a plain Python object standing in
  front of one C++ QSSGApplyValue.

  It is built on the cute 'QSSGCommand', as Qt's QSSGApplyValue is built on
  Qt's QSSGCommand, and has everything that class has.

  C++ hands a QSSGApplyValue around as a copy, so every C++ QSSGApplyValue
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGApplyValue yet. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSSGApplyValue::addDebug(QDebug &stream) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSSGApplyValue::~QSSGApplyValue()': the destructor: Python removes
    its C++ QSSGApplyValue by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGApplyValue is created at the first use, not by
    'QSSGApplyValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGApplyValue back gives a copy the ritual made for
    Python, in a new cute QSSGApplyValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGApplyValue'

  #  Qt's '~QSSGApplyValue()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGApplyValue behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSSGApplyValueD1Ev'

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

  @overload(QByteArray)
  def __init__(self, inName: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QSSGApplyValue::QSSGApplyValue(const
    QByteArray &inName)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgapplyvalue.html#QSSGApplyValue

    Parameters
    ----------

    inName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QSSGApplyValue::QSSGApplyValue(const QByteArray &inName)
    self._noteCreation(QSSGApplyValue, lambda: Rituals.call(
        'ritual_ZN14QSSGApplyValueC1ERK10QByteArray', self._valueOf(inName),
    ))

  @overload(THIS)
  def __init__(self, command: QSSGApplyValue) -> None:
    """
    Notes what was given, for Qt's 'QSSGApplyValue::QSSGApplyValue(const
    QSSGApplyValue &command)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgapplyvalue.html#QSSGApplyValue

    Parameters
    ----------

    command : QSSGApplyValue
      Passed on as a value: Qt reads the C++ QSSGApplyValue, which stays
      Python's own.
    """
    #  QSSGApplyValue::QSSGApplyValue(const QSSGApplyValue &command)
    self._noteCreation(QSSGApplyValue, lambda: Rituals.call(
        'ritual_ZN14QSSGApplyValueC1ERKS_', self._valueOf(command),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGApplyValue::QSSGApplyValue()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgapplyvalue.html#QSSGApplyValue
    """
    #  QSSGApplyValue::QSSGApplyValue()
    self._noteCreation(QSSGApplyValue, lambda: Rituals.call(
        'ritual_ZN14QSSGApplyValueC1Ev',
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
