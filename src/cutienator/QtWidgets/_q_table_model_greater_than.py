"""
QTableModelGreaterThan binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTableModelGreaterThan to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTableWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTableWidgetItem = WAIT['QTableWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTableModelGreaterThan(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTableModelGreaterThan: a plain Python object
  standing in front of one C++ QTableModelGreaterThan.

  C++ hands a QTableModelGreaterThan around as a copy, so every C++
  QTableModelGreaterThan behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTableModelGreaterThan that has a ritual and that
  Python can call so far, 1 name in all: '__call__'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTableModelGreaterThan::~QTableModelGreaterThan()': the destructor:
    Python removes its C++ QTableModelGreaterThan by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTableModelGreaterThan is created at the first use, not by
    'QTableModelGreaterThan(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTableModelGreaterThan back gives a copy the ritual
    made for Python, in a new cute QTableModelGreaterThan.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableModelGreaterThan'

  #  Qt's '~QTableModelGreaterThan()'. Naming it makes this a value class:
  #  Python owns every C++ QTableModelGreaterThan behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QTableModelGreaterThanD1Ev'

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

  @overload(QTableWidgetItem, QTableWidgetItem)
  @overload(QTableWidgetItem, NoneType)
  @overload(NoneType, QTableWidgetItem)
  @overload(NoneType, NoneType)
  def __call__(
      self,
      i1: Optional[QTableWidgetItem],
      i2: Optional[QTableWidgetItem],
  ) -> bool:
    """
    Calls Qt's 'bool QTableModelGreaterThan::operator()(QTableWidgetItem *i1,
    QTableWidgetItem *i2) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodelgreaterthan.html#operator()

    Parameters
    ----------

    i1 : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    i2 : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTableModelGreaterThan::operator()(QTableWidgetItem *i1,
    #      QTableWidgetItem *i2) const
    return self.uglySide.call(
        'ritual_ZNK22QTableModelGreaterThanclEP16QTableWidgetItemS1_',
        self._addressOf(i1), self._addressOf(i2),
    )

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
