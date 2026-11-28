"""
QQmlJSDocumentEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSDocumentEdit to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QQmlJSDocumentEdit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSDocumentEdit: a plain Python object standing in
  front of one C++ QQmlJSDocumentEdit.

  C++ hands a QQmlJSDocumentEdit around as a copy, so every C++
  QQmlJSDocumentEdit behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSDocumentEdit that has a ritual and that Python
  can call so far, 2 names in all: '__eq__', '__ne__'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSDocumentEdit::~QQmlJSDocumentEdit()': the destructor: Python
    removes its C++ QQmlJSDocumentEdit by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSDocumentEdit is created at the first use, not by
    'QQmlJSDocumentEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSDocumentEdit back gives a copy the ritual made
    for Python, in a new cute QQmlJSDocumentEdit.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSDocumentEdit'

  #  Qt's '~QQmlJSDocumentEdit()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSDocumentEdit behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlJSDocumentEditD1Ev'

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

  @overload(THIS)
  def __eq__(self, rhs: QQmlJSDocumentEdit) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlJSDocumentEdit &lhs, const
    QQmlJSDocumentEdit &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsdocumentedit.html#operator==

    Parameters
    ----------

    rhs : QQmlJSDocumentEdit
      Passed on as a value: Qt reads the C++ QQmlJSDocumentEdit, which stays
      Python's own.
    """
    #  bool operator==(const QQmlJSDocumentEdit &lhs, const
    #      QQmlJSDocumentEdit &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QQmlJSDocumentEditS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QQmlJSDocumentEdit) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlJSDocumentEdit &lhs, const
    QQmlJSDocumentEdit &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsdocumentedit.html#operator!=

    Parameters
    ----------

    rhs : QQmlJSDocumentEdit
      Passed on as a value: Qt reads the C++ QQmlJSDocumentEdit, which stays
      Python's own.
    """
    #  bool operator!=(const QQmlJSDocumentEdit &lhs, const
    #      QQmlJSDocumentEdit &rhs)
    return Rituals.call(
        'ritual_ZneRK18QQmlJSDocumentEditS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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


#  Qt's 'QList<QQmlJSDocumentEdit>': the list of QQmlJSDocumentEdit, which
#  'QList[QQmlJSDocumentEdit]' gives. It is made here, so that there is one
#  as soon as there can be a QQmlJSDocumentEdit.
QList.createKind(
    QQmlJSDocumentEdit, 'value',
    make='ritual_list_make_QQmlJSDocumentEdit',
    add='ritual_list_add_QQmlJSDocumentEdit',
    size='ritual_list_size_QQmlJSDocumentEdit',
    at='ritual_list_at_QQmlJSDocumentEdit',
    drop='ritual_list_drop_QQmlJSDocumentEdit',
)
