"""
QV4::CompiledData::QmlUnit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::QmlUnit to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QmlUnit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::QmlUnit: a plain Python object
  standing in front of one C++ QV4::CompiledData::QmlUnit.

  C++ hands a QV4::CompiledData::QmlUnit around as a copy, so every C++
  QV4::CompiledData::QmlUnit behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::QmlUnit that has a ritual and
  that Python can call so far, 2 names in all: 'importAt', 'objectAt'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::QmlUnit::~QmlUnit()': the destructor: Python
    removes its C++ QV4::CompiledData::QmlUnit by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::QmlUnit is created at the first use, not by
    'QV4::CompiledData::QmlUnit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::QmlUnit back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::QmlUnit.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::QmlUnit'

  #  Qt's '~QV4::CompiledData::QmlUnit()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::QmlUnit behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData7QmlUnitD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def importAt(self, idx: int) -> Optional[QV4.CompiledData.Import]:
    """
    Calls Qt's 'const Import *QV4::CompiledData::QmlUnit::importAt(int idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-qmlunit.html#importAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Import]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Import *QV4::CompiledData::QmlUnit::importAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7QmlUnit8importAtEi', idx,
    )
    return QV4.CompiledData.Import._cuteAt(address)

  @overload(int)
  def objectAt(self, idx: int) -> Optional[QV4.CompiledData.Object]:
    """
    Calls Qt's 'const Object *QV4::CompiledData::QmlUnit::objectAt(int idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-qmlunit.html#objectAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Object *QV4::CompiledData::QmlUnit::objectAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData7QmlUnit8objectAtEi', idx,
    )
    return QV4.CompiledData.Object._cuteAt(address)

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
