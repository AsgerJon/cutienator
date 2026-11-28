"""
QtPrivate::QModelIndexWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractitemmodel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtPrivate::QModelIndexWrapper to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class QModelIndexWrapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QModelIndexWrapper: a plain Python object
  standing in front of one C++ QtPrivate::QModelIndexWrapper.

  C++ hands a QtPrivate::QModelIndexWrapper around as a copy, so every C++
  QtPrivate::QModelIndexWrapper behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::QModelIndexWrapper that has a ritual and
  that Python can call so far, 2 names in all: '__eq__', '__ne__'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModelIndex QtPrivate::QModelIndexWrapper::operator QModelIndex()
    const': an operator Python has no name for.
  - Qt's 'bool operator==(const QModelIndex &l, const QModelIndexWrapper
    &r)': takes in Python what 'bool operator==(const QModelIndexWrapper &l,
    const QModelIndex &r)' takes.
  - Qt's 'bool operator!=(const QModelIndex &l, const QModelIndexWrapper
    &r)': takes in Python what 'bool operator!=(const QModelIndexWrapper &l,
    const QModelIndex &r)' takes.
  - Qt's 'QtPrivate::QModelIndexWrapper::~QModelIndexWrapper()': the
    destructor: Python removes its C++ QtPrivate::QModelIndexWrapper by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QModelIndexWrapper is created at the first use, not by
    'QtPrivate::QModelIndexWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QModelIndexWrapper back gives a copy the
    ritual made for Python, in a new cute QtPrivate::QModelIndexWrapper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QModelIndexWrapper'

  #  Qt's '~QtPrivate::QModelIndexWrapper()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::QModelIndexWrapper behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate18QModelIndexWrapperD1Ev'

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
  def __eq__(self, r: QModelIndexWrapper) -> bool:
    """
    Calls Qt's 'bool operator==(const QModelIndexWrapper &l, const
    QModelIndexWrapper &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qmodelindexwrapper.html#operator==

    Parameters
    ----------

    r : QModelIndexWrapper
      Passed on as a value: Qt reads the C++ QtPrivate::QModelIndexWrapper,
      which stays Python's own.
    """
    #  bool operator==(const QModelIndexWrapper &l, const QModelIndexWrapper
    #      &r)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_18QModelIndexWrapperES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(r),
    )

  @overload(QModelIndex)
  def __eq__(self, r: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator==(const QModelIndexWrapper &l, const
    QModelIndex &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qmodelindexwrapper.html#operator==

    Parameters
    ----------

    r : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator==(const QModelIndexWrapper &l, const QModelIndex &r)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_18QModelIndexWrapperERK11QModelIndex',
        CuteMixin._valueOf(self), CuteMixin._valueOf(r),
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
  def __ne__(self, r: QModelIndexWrapper) -> bool:
    """
    Calls Qt's 'bool operator!=(const QModelIndexWrapper &l, const
    QModelIndexWrapper &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qmodelindexwrapper.html#operator!=

    Parameters
    ----------

    r : QModelIndexWrapper
      Passed on as a value: Qt reads the C++ QtPrivate::QModelIndexWrapper,
      which stays Python's own.
    """
    #  bool operator!=(const QModelIndexWrapper &l, const QModelIndexWrapper
    #      &r)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_18QModelIndexWrapperES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(r),
    )

  @overload(QModelIndex)
  def __ne__(self, r: QModelIndex) -> bool:
    """
    Calls Qt's 'bool operator!=(const QModelIndexWrapper &l, const
    QModelIndex &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qmodelindexwrapper.html#operator!=

    Parameters
    ----------

    r : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool operator!=(const QModelIndexWrapper &l, const QModelIndex &r)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_18QModelIndexWrapperERK11QModelIndex',
        CuteMixin._valueOf(self), CuteMixin._valueOf(r),
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

  @overload(QModelIndex)
  def __init__(self, i: QModelIndex) -> None:
    """
    Notes what was given, for Qt's
    'QtPrivate::QModelIndexWrapper::QModelIndexWrapper(const QModelIndex
    &i)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qmodelindexwrapper.html

    Parameters
    ----------

    i : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  QtPrivate::QModelIndexWrapper::QModelIndexWrapper(const QModelIndex
    #      &i)
    self._noteCreation(QModelIndexWrapper, lambda: Rituals.call(
        'ritual_ZN9QtPrivate18QModelIndexWrapperC1ERK11QModelIndex',
        self._valueOf(i),
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
