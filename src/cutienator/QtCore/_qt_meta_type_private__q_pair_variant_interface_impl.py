"""
QtMetaTypePrivate::QPairVariantInterfaceImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetatype.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPairVariantInterfaceImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMetaTypePrivate::QPairVariantInterfaceImpl: a plain
  Python object standing in front of one C++
  QtMetaTypePrivate::QPairVariantInterfaceImpl.

  C++ hands a QtMetaTypePrivate::QPairVariantInterfaceImpl around as a copy,
  so every C++ QtMetaTypePrivate::QPairVariantInterfaceImpl behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMetaTypePrivate::QPairVariantInterfaceImpl yet. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QtMetaTypePrivate::QPairVariantInterfaceImpl::first(void
    *dataPtr) const': names 'void', which has no cute class yet.
  - Qt's 'void QtMetaTypePrivate::QPairVariantInterfaceImpl::second(void
    *dataPtr) const': names 'void', which has no cute class yet.
  - Qt's 'QtMetaTypePrivate::QPairVariantInterfaceImpl::
    ~QPairVariantInterfaceImpl()': the destructor: Python removes its C++
    QtMetaTypePrivate::QPairVariantInterfaceImpl by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QtMetaTypePrivate::QPairVariantInterfaceImpl is created at the
    first use, not by 'QtMetaTypePrivate::QPairVariantInterfaceImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMetaTypePrivate::QPairVariantInterfaceImpl back
    gives a copy the ritual made for Python, in a new cute
    QtMetaTypePrivate::QPairVariantInterfaceImpl.
  - Each name of Qt's QtMetaTypePrivate::QPairVariantInterfaceImpl that has
    no cute function yet, 'first', 'getFirstImpl', 'getSecondImpl', 'second',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMetaTypePrivate::QPairVariantInterfaceImpl'

  #  Qt's '~QtMetaTypePrivate::QPairVariantInterfaceImpl()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QtMetaTypePrivate::QPairVariantInterfaceImpl behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplD1Ev')

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
    Notes what was given, for Qt's
    'QtMetaTypePrivate::QPairVariantInterfaceImpl::QPairVariantInterfaceImpl(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmetatypeprivate-qpairvariantinterfaceimpl.html
    """
    #  QtMetaTypePrivate::QPairVariantInterfaceImpl::
    #      QPairVariantInterfaceImpl()
    self._noteCreation(QPairVariantInterfaceImpl, lambda: Rituals.call(
        'ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplC1Ev',
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

  @staticmethod
  def first(*__, **_) -> Never:
    """
    Qt's 'void QtMetaTypePrivate::QPairVariantInterfaceImpl::first(void
    *dataPtr) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtMetaTypePrivate.QPairVariantInterfaceImpl.first' has no cute "
        "function yet. Qt's 'void "
        "QtMetaTypePrivate::QPairVariantInterfaceImpl::first(void *dataPtr) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def getFirstImpl(*__, **_) -> Never:
    """
    Qt's 'QtMetaTypePrivate::QPairVariantInterfaceImpl::getFirstImpl': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QtMetaTypePrivate.QPairVariantInterfaceImpl.getFirstImpl' has no "
        "cute function yet. Qt's "
        "'QtMetaTypePrivate::QPairVariantInterfaceImpl::getFirstImpl': a "
        "template: a pattern and no single function.")

  @staticmethod
  def getSecondImpl(*__, **_) -> Never:
    """
    Qt's 'QtMetaTypePrivate::QPairVariantInterfaceImpl::getSecondImpl': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QtMetaTypePrivate.QPairVariantInterfaceImpl.getSecondImpl' has no "
        "cute function yet. Qt's "
        "'QtMetaTypePrivate::QPairVariantInterfaceImpl::getSecondImpl': a "
        "template: a pattern and no single function.")

  @staticmethod
  def second(*__, **_) -> Never:
    """
    Qt's 'void QtMetaTypePrivate::QPairVariantInterfaceImpl::second(void
    *dataPtr) const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtMetaTypePrivate.QPairVariantInterfaceImpl.second' has no cute "
        "function yet. Qt's 'void "
        "QtMetaTypePrivate::QPairVariantInterfaceImpl::second(void "
        "*dataPtr) const': names 'void', which has no cute class yet.")
