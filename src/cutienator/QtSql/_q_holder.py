"""
QHolder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlresult_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QHolder to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QHolder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHolder: a plain Python object standing in front of
  one C++ QHolder.

  C++ hands a QHolder around as a copy, so every C++ QHolder behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHolder that has a ritual and that Python can call
  so far, 2 names in all: '__eq__', '__ne__'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHolder::~QHolder()': the destructor: Python removes its C++
    QHolder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QHolder is created at the first use, not by 'QHolder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHolder back gives a copy the ritual made for Python,
    in a new cute QHolder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHolder'

  #  Qt's '~QHolder()'. Naming it makes this a value class: Python owns every
  #  C++ QHolder behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QHolderD1Ev'

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
  def __eq__(self, h: QHolder) -> bool:
    """
    Calls Qt's 'bool QHolder::operator==(const QHolder &h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qholder.html#operator==

    Parameters
    ----------

    h : QHolder
      Passed on as a value: Qt reads the C++ QHolder, which stays Python's
      own.
    """
    #  bool QHolder::operator==(const QHolder &h) const
    return self.uglySide.call('ritual_ZNK7QHoldereqERKS_', self._valueOf(h))

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, h: QHolder) -> bool:
    """
    Calls Qt's 'bool QHolder::operator!=(const QHolder &h) const'.

    Qt's own words: https://doc.qt.io/qt-6/qholder.html#operator!=

    Parameters
    ----------

    h : QHolder
      Passed on as a value: Qt reads the C++ QHolder, which stays Python's
      own.
    """
    #  bool QHolder::operator!=(const QHolder &h) const
    return self.uglySide.call('ritual_ZNK7QHolderneERKS_', self._valueOf(h))

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

  @overload()
  @overload(str)
  @overload(str, int)
  def __init__(self, hldr: str = '', index: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QHolder::QHolder(const QString &hldr,
    qsizetype index)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qholder.html#QHolder

    Parameters
    ----------

    hldr : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QHolder::QHolder(const QString &hldr, qsizetype index)
    self._noteCreation(QHolder, lambda: Rituals.call(
        'ritual_ZN7QHolderC1ERK7QStringx', hldr, index,
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
