"""
QSGGradientCacheKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGGradientCacheKey to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSGGradientCacheKey(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGGradientCacheKey: a plain Python object standing
  in front of one C++ QSGGradientCacheKey.

  C++ hands a QSGGradientCacheKey around as a copy, so every C++
  QSGGradientCacheKey behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGGradientCacheKey that has a ritual and that
  Python can call so far, 1 name in all: '__eq__'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGGradientCacheKey::QSGGradientCacheKey(const QGradientStops
    &stops, QGradient::Spread spread)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSGGradientCacheKey::~QSGGradientCacheKey()': the destructor:
    Python removes its C++ QSGGradientCacheKey by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSGGradientCacheKey is created at the first use, not by
    'QSGGradientCacheKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGGradientCacheKey back gives a copy the ritual made
    for Python, in a new cute QSGGradientCacheKey.
  - Each name of Qt's QSGGradientCacheKey that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGradientCacheKey'

  #  Qt's '~QSGGradientCacheKey()'. Naming it makes this a value class:
  #  Python owns every C++ QSGGradientCacheKey behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSGGradientCacheKeyD1Ev'

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
  def __eq__(self, other: QSGGradientCacheKey) -> bool:
    """
    Calls Qt's 'bool QSGGradientCacheKey::operator==(const
    QSGGradientCacheKey &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggradientcachekey.html#operator==

    Parameters
    ----------

    other : QSGGradientCacheKey
      Passed on as a value: Qt reads the C++ QSGGradientCacheKey, which stays
      Python's own.
    """
    #  bool QSGGradientCacheKey::operator==(const QSGGradientCacheKey &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QSGGradientCacheKeyeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGGradientCacheKey::QSGGradientCacheKey(const QGradientStops
    &stops, QGradient::Spread spread)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSGGradientCacheKey.__init__' has no cute function yet. Qt's "
        "'QSGGradientCacheKey::QSGGradientCacheKey(const QGradientStops "
        "&stops, QGradient::Spread spread)': takes a type Python has no way "
        "to hand over yet.")

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
