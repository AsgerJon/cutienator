"""
QV4::CompiledData::JSClassMember binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::JSClassMember to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class JSClassMember(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::JSClassMember: a plain Python
  object standing in front of one C++ QV4::CompiledData::JSClassMember.

  C++ hands a QV4::CompiledData::JSClassMember around as a copy, so every C++
  QV4::CompiledData::JSClassMember behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::JSClassMember that has a ritual
  and that Python can call so far, 3 names in all: 'set', 'nameOffset',
  'isAccessor'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::JSClassMember::~JSClassMember()': the
    destructor: Python removes its C++ QV4::CompiledData::JSClassMember by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::JSClassMember is created at the first use, not
    by 'QV4::CompiledData::JSClassMember(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::JSClassMember back gives a copy
    the ritual made for Python, in a new cute
    QV4::CompiledData::JSClassMember.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::JSClassMember'

  #  Qt's '~QV4::CompiledData::JSClassMember()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::JSClassMember behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData13JSClassMemberD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nameOffset(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::JSClassMember::nameOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-jsclassmember.html#nameOffset
    """
    #  quint32 QV4::CompiledData::JSClassMember::nameOffset() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData13JSClassMember10nameOffsetEv',
    )

  def isAccessor(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::JSClassMember::isAccessor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-jsclassmember.html#isAccessor
    """
    #  bool QV4::CompiledData::JSClassMember::isAccessor() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData13JSClassMember10isAccessorEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QV4::CompiledData::JSClassMember::JSClassMember()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-jsclassmember.html#JSClassMember
    """
    #  QV4::CompiledData::JSClassMember::JSClassMember()
    self._noteCreation(JSClassMember, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData13JSClassMemberC1Ev',
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

  @overload(int, bool)
  def set(self, nameOffset: int, isAccessor: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::JSClassMember::set(quint32
    nameOffset, bool isAccessor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-jsclassmember.html#set

    Parameters
    ----------

    nameOffset : int
      Passed on as it is.

    isAccessor : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::JSClassMember::set(quint32 nameOffset, bool
    #      isAccessor)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData13JSClassMember3setEjb',
        nameOffset, isAccessor,
    )
