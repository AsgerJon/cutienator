"""
QV4::CompiledData::TemplateObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::TemplateObject to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class TemplateObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::TemplateObject: a plain Python
  object standing in front of one C++ QV4::CompiledData::TemplateObject.

  C++ hands a QV4::CompiledData::TemplateObject around as a copy, so every
  C++ QV4::CompiledData::TemplateObject behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::TemplateObject that has a ritual
  and that Python can call so far, 4 names in all: 'calculateSize', 'align',
  'stringIndexAt', 'rawStringIndexAt'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const quint32_le *QV4::CompiledData::TemplateObject::stringTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'QV4::CompiledData::TemplateObject::~TemplateObject()': the
    destructor: Python removes its C++ QV4::CompiledData::TemplateObject by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::TemplateObject is created at the first use,
    not by 'QV4::CompiledData::TemplateObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::TemplateObject back gives a copy
    the ritual made for Python, in a new cute
    QV4::CompiledData::TemplateObject.
  - Each name of Qt's QV4::CompiledData::TemplateObject that has no cute
    function yet, 'stringTable', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def calculateSize(size: int) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::TemplateObject::calculateSize(int
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-templateobject.html#calculateSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::TemplateObject::calculateSize(int size)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData14TemplateObject13calculateSizeEi', size,
    )

  @staticmethod
  @overload(int)
  def align(a: int) -> int:
    """
    Calls Qt's 'size_t QV4::CompiledData::TemplateObject::align(size_t a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-templateobject.html#align

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  size_t QV4::CompiledData::TemplateObject::align(size_t a)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData14TemplateObject5alignEm', a,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::TemplateObject'

  #  Qt's '~QV4::CompiledData::TemplateObject()'. Naming it makes this a
  #  value class: Python owns every C++ QV4::CompiledData::TemplateObject
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData14TemplateObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def stringIndexAt(self, i: int) -> int:
    """
    Calls Qt's 'uint QV4::CompiledData::TemplateObject::stringIndexAt(uint i)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-templateobject.html#stringIndexAt

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  uint QV4::CompiledData::TemplateObject::stringIndexAt(uint i) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData14TemplateObject13stringIndexAtEj', i,
    )

  @overload(int)
  def rawStringIndexAt(self, i: int) -> int:
    """
    Calls Qt's 'uint QV4::CompiledData::TemplateObject::rawStringIndexAt(uint
    i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-templateobject.html

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  uint QV4::CompiledData::TemplateObject::rawStringIndexAt(uint i) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData14TemplateObject16rawStringIndexAtEj',
        i,
    )

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
  def stringTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::TemplateObject::stringTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.TemplateObject.stringTable' has no cute function "
        "yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::TemplateObject::stringTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")
