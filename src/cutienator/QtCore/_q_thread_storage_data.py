"""
QThreadStorageData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qthreadstorage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QThreadStorageData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QThreadStorageData: a plain Python object standing in
  front of one C++ QThreadStorageData.

  C++ hands a QThreadStorageData around as a copy, so every C++
  QThreadStorageData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QThreadStorageData yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QThreadStorageData::QThreadStorageData(void (*)(void *) func)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QThreadStorageData::~QThreadStorageData()': the destructor: Python
    removes its C++ QThreadStorageData by it, and has no other use for it.
  - Qt's 'void **QThreadStorageData::get() const': gives a type Python has no
    way to take yet.
  - Qt's 'void **QThreadStorageData::set(void *p)': names 'void', which has
    no cute class yet.

  What to expect
  --------------

  - The C++ QThreadStorageData is created at the first use, not by
    'QThreadStorageData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QThreadStorageData back gives a copy the ritual made
    for Python, in a new cute QThreadStorageData.
  - Each name of Qt's QThreadStorageData that has no cute function yet,
    '__init__', 'get', 'set', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThreadStorageData'

  #  Qt's '~QThreadStorageData()'. Naming it makes this a value class: Python
  #  owns every C++ QThreadStorageData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QThreadStorageDataD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QThreadStorageData::QThreadStorageData(void (*)(void *) func)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QThreadStorageData.__init__' has no cute function yet. Qt's "
        "'QThreadStorageData::QThreadStorageData(void (*)(void *) func)': "
        "takes a type Python has no way to hand over yet.")

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
  def get(*__, **_) -> Never:
    """
    Qt's 'void **QThreadStorageData::get() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QThreadStorageData.get' has no cute function yet. Qt's 'void "
        "**QThreadStorageData::get() const': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def set(*__, **_) -> Never:
    """
    Qt's 'void **QThreadStorageData::set(void *p)': names 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QThreadStorageData.set' has no cute function yet. Qt's 'void "
        "**QThreadStorageData::set(void *p)': names 'void', which has no "
        "cute class yet.")
