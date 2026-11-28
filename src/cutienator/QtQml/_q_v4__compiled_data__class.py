"""
QV4::CompiledData::Class binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Class to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class Class(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Class: a plain Python object
  standing in front of one C++ QV4::CompiledData::Class.

  C++ hands a QV4::CompiledData::Class around as a copy, so every C++
  QV4::CompiledData::Class behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Class that has a ritual and that
  Python can call so far, 3 names in all: 'methodTable', 'calculateSize',
  'align'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::Class::~Class()': the destructor: Python removes
    its C++ QV4::CompiledData::Class by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Class is created at the first use, not by
    'QV4::CompiledData::Class(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Class back gives a copy the ritual
    made for Python, in a new cute QV4::CompiledData::Class.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int)
  def calculateSize(nStaticMethods: int, nMethods: int) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Class::calculateSize(int
    nStaticMethods, int nMethods)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-class.html#calculateSize

    Parameters
    ----------

    nStaticMethods : int
      Passed on as it is.

    nMethods : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::Class::calculateSize(int nStaticMethods, int
    #      nMethods)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData5Class13calculateSizeEii',
        nStaticMethods, nMethods,
    )

  @staticmethod
  @overload(int)
  def align(a: int) -> int:
    """
    Calls Qt's 'size_t QV4::CompiledData::Class::align(size_t a)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-class.html#align

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  size_t QV4::CompiledData::Class::align(size_t a)
    return Rituals.call('ritual_ZN3QV412CompiledData5Class5alignEm', a)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Class'

  #  Qt's '~QV4::CompiledData::Class()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::Class behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData5ClassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def methodTable(self) -> Optional[QV4.CompiledData.Method]:
    """
    Calls Qt's 'const Method *QV4::CompiledData::Class::methodTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-class.html#methodTable

    Returns
    -------

    Optional[QV4.CompiledData.Method]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Method *QV4::CompiledData::Class::methodTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData5Class11methodTableEv',
    )
    return QV4.CompiledData.Method._cuteAt(address)

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
