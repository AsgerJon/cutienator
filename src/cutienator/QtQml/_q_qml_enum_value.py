"""
QQmlEnumValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlenumvalue_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlEnumValue to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QQmlEnumValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlEnumValue: a plain Python object standing in
  front of one C++ QQmlEnumValue.

  C++ hands a QQmlEnumValue around as a copy, so every C++ QQmlEnumValue
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlEnumValue yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlEnumValue::~QQmlEnumValue()': the destructor: Python removes
    its C++ QQmlEnumValue by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlEnumValue is created at the first use, not by
    'QQmlEnumValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlEnumValue back gives a copy the ritual made for
    Python, in a new cute QQmlEnumValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlEnumValue'

  #  Qt's '~QQmlEnumValue()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlEnumValue behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QQmlEnumValueD1Ev'

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
    Notes what was given, for Qt's 'QQmlEnumValue::QQmlEnumValue()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlenumvalue.html#QQmlEnumValue
    """
    #  QQmlEnumValue::QQmlEnumValue()
    self._noteCreation(QQmlEnumValue, lambda: Rituals.call(
        'ritual_ZN13QQmlEnumValueC1Ev',
    ))

  @overload(str, int)
  def __init__(self, n: str, v: int) -> None:
    """
    Notes what was given, for Qt's 'QQmlEnumValue::QQmlEnumValue(const
    QString &n, int v)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlenumvalue.html#QQmlEnumValue

    Parameters
    ----------

    n : str
      Passed on as it is: a QString is made of it for the call.

    v : int
      Passed on as it is.
    """
    #  QQmlEnumValue::QQmlEnumValue(const QString &n, int v)
    self._noteCreation(QQmlEnumValue, lambda: Rituals.call(
        'ritual_ZN13QQmlEnumValueC1ERK7QStringi', n, v,
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


#  Qt's 'QList<QQmlEnumValue>': the list of QQmlEnumValue, which
#  'QList[QQmlEnumValue]' gives. It is made here, so that there is one as
#  soon as there can be a QQmlEnumValue.
QList.createKind(
    QQmlEnumValue, 'value',
    make='ritual_list_make_QQmlEnumValue',
    add='ritual_list_add_QQmlEnumValue',
    size='ritual_list_size_QQmlEnumValue',
    at='ritual_list_at_QQmlEnumValue',
    drop='ritual_list_drop_QQmlEnumValue',
)
