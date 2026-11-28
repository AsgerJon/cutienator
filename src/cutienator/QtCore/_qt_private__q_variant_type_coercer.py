"""
QtPrivate::QVariantTypeCoercer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QVariantTypeCoercer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QVariantTypeCoercer: a plain Python object
  standing in front of one C++ QtPrivate::QVariantTypeCoercer.

  C++ hands a QtPrivate::QVariantTypeCoercer around as a copy, so every C++
  QtPrivate::QVariantTypeCoercer behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QtPrivate::QVariantTypeCoercer yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const void *QtPrivate::QVariantTypeCoercer::convert(const QVariant
    &value, const QMetaType &type)': gives 'void', which has no cute class
    yet.
  - Qt's 'const void *QtPrivate::QVariantTypeCoercer::coerce(const QVariant
    &value, const QMetaType &type)': gives 'void', which has no cute class
    yet.
  - Qt's 'QtPrivate::QVariantTypeCoercer::~QVariantTypeCoercer()': the
    destructor: Python removes its C++ QtPrivate::QVariantTypeCoercer by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QVariantTypeCoercer is created at the first use, not
    by 'QtPrivate::QVariantTypeCoercer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QVariantTypeCoercer back gives a copy the
    ritual made for Python, in a new cute QtPrivate::QVariantTypeCoercer.
  - Each name of Qt's QtPrivate::QVariantTypeCoercer that has no cute
    function yet, 'coerce', 'convert', holds a function that raises
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
  __qt_class__ = 'QtPrivate::QVariantTypeCoercer'

  #  Qt's '~QtPrivate::QVariantTypeCoercer()'. Naming it makes this a value
  #  class: Python owns every C++ QtPrivate::QVariantTypeCoercer behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate19QVariantTypeCoercerD1Ev'

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
  def coerce(*__, **_) -> Never:
    """
    Qt's 'const void *QtPrivate::QVariantTypeCoercer::coerce(const QVariant
    &value, const QMetaType &type)': gives 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QVariantTypeCoercer.coerce' has no cute function yet. "
        "Qt's 'const void *QtPrivate::QVariantTypeCoercer::coerce(const "
        "QVariant &value, const QMetaType &type)': gives 'void', which has "
        "no cute class yet.")

  @staticmethod
  def convert(*__, **_) -> Never:
    """
    Qt's 'const void *QtPrivate::QVariantTypeCoercer::convert(const QVariant
    &value, const QMetaType &type)': gives 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QVariantTypeCoercer.convert' has no cute function yet. "
        "Qt's 'const void *QtPrivate::QVariantTypeCoercer::convert(const "
        "QVariant &value, const QMetaType &type)': gives 'void', which has "
        "no cute class yet.")
