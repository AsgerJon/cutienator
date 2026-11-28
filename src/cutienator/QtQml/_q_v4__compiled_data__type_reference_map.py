"""
QV4::CompiledData::TypeReferenceMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::TypeReferenceMap to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class TypeReferenceMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::TypeReferenceMap: a plain Python
  object standing in front of one C++ QV4::CompiledData::TypeReferenceMap.

  C++ hands a QV4::CompiledData::TypeReferenceMap around as a copy, so every
  C++ QV4::CompiledData::TypeReferenceMap behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  No function of Qt's QV4::CompiledData::TypeReferenceMap yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TypeReference &QV4::CompiledData::TypeReferenceMap::add(int
    nameIndex, const Location &loc)': gives a type Python has no way to take
    yet.
  - Qt's 'QV4::CompiledData::TypeReferenceMap::~TypeReferenceMap()': the
    destructor: Python removes its C++ QV4::CompiledData::TypeReferenceMap by
    it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QV4::CompiledData::TypeReferenceMap is created at the first use,
    not by 'QV4::CompiledData::TypeReferenceMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::TypeReferenceMap back gives a copy
    the ritual made for Python, in a new cute
    QV4::CompiledData::TypeReferenceMap.
  - Each name of Qt's QV4::CompiledData::TypeReferenceMap that has no cute
    function yet, 'add', 'collectFromObject', 'collectFromObjects', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::TypeReferenceMap'

  #  Qt's '~QV4::CompiledData::TypeReferenceMap()'. Naming it makes this a
  #  value class: Python owns every C++ QV4::CompiledData::TypeReferenceMap
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData16TypeReferenceMapD1Ev'

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

  @staticmethod
  def add(*__, **_) -> Never:
    """
    Qt's 'TypeReference &QV4::CompiledData::TypeReferenceMap::add(int
    nameIndex, const Location &loc)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.TypeReferenceMap.add' has no cute function yet. "
        "Qt's 'TypeReference &QV4::CompiledData::TypeReferenceMap::add(int "
        "nameIndex, const Location &loc)': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def collectFromObject(*__, **_) -> Never:
    """
    Qt's 'QV4::CompiledData::TypeReferenceMap::collectFromObject': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.TypeReferenceMap.collectFromObject' has no cute "
        "function yet. Qt's "
        "'QV4::CompiledData::TypeReferenceMap::collectFromObject': a "
        "template: a pattern and no single function.")

  @staticmethod
  def collectFromObjects(*__, **_) -> Never:
    """
    Qt's 'QV4::CompiledData::TypeReferenceMap::collectFromObjects': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.TypeReferenceMap.collectFromObjects' has no cute "
        "function yet. Qt's "
        "'QV4::CompiledData::TypeReferenceMap::collectFromObjects': a "
        "template: a pattern and no single function.")
