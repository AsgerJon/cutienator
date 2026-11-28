"""
QV4::CompiledData::InlineComponentData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::InlineComponentData to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QQmlType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlType = WAIT['QQmlType']


class InlineComponentData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::InlineComponentData: a plain
  Python object standing in front of one C++
  QV4::CompiledData::InlineComponentData.

  C++ hands a QV4::CompiledData::InlineComponentData around as a copy, so
  every C++ QV4::CompiledData::InlineComponentData behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::CompiledData::InlineComponentData yet. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::InlineComponentData::~InlineComponentData()':
    the destructor: Python removes its C++
    QV4::CompiledData::InlineComponentData by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::InlineComponentData is created at the first
    use, not by 'QV4::CompiledData::InlineComponentData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::InlineComponentData back gives a
    copy the ritual made for Python, in a new cute
    QV4::CompiledData::InlineComponentData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::InlineComponentData'

  #  Qt's '~QV4::CompiledData::InlineComponentData()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QV4::CompiledData::InlineComponentData behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData19InlineComponentDataD1Ev'

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
    'QV4::CompiledData::InlineComponentData::InlineComponentData()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-inlinecomponentdata.html
    """
    #  QV4::CompiledData::InlineComponentData::InlineComponentData()
    self._noteCreation(InlineComponentData, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData19InlineComponentDataC1Ev',
    ))

  @overload(QQmlType, int, int)
  def __init__(
      self,
      qmlType: QQmlType,
      objectIndex: int,
      nameIndex: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::CompiledData::InlineComponentData::InlineComponentData(const
    QQmlType &qmlType, int objectIndex, int nameIndex)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-inlinecomponentdata.html

    Parameters
    ----------

    qmlType : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.

    objectIndex : int
      Passed on as it is.

    nameIndex : int
      Passed on as it is.
    """
    #  QV4::CompiledData::InlineComponentData::InlineComponentData(const
    #      QQmlType &qmlType, int objectIndex, int nameIndex)
    self._noteCreation(InlineComponentData, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData19InlineComponentDataC1ERK8QQmlTypeii',
        self._valueOf(qmlType), objectIndex, nameIndex,
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
