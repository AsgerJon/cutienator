"""
QCache3QTileEvictionPolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCache3QTileEvictionPolicy to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCache3QTileEvictionPolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCache3QTileEvictionPolicy: a plain Python object
  standing in front of one C++ QCache3QTileEvictionPolicy.

  C++ hands a QCache3QTileEvictionPolicy around as a copy, so every C++
  QCache3QTileEvictionPolicy behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QCache3QTileEvictionPolicy yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QCache3QTileEvictionPolicy::aboutToBeRemoved(const
    QGeoTileSpec &key, QSharedPointer<QGeoCachedTileDisk> obj)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QCache3QTileEvictionPolicy::aboutToBeEvicted(const
    QGeoTileSpec &key, QSharedPointer<QGeoCachedTileDisk> obj)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QCache3QTileEvictionPolicy::~QCache3QTileEvictionPolicy()': the
    destructor: Python removes its C++ QCache3QTileEvictionPolicy by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QCache3QTileEvictionPolicy is created at the first use, not by
    'QCache3QTileEvictionPolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCache3QTileEvictionPolicy back gives a copy the
    ritual made for Python, in a new cute QCache3QTileEvictionPolicy.
  - Each name of Qt's QCache3QTileEvictionPolicy that has no cute function
    yet, 'aboutToBeEvicted', 'aboutToBeRemoved', holds a function that raises
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
  __qt_class__ = 'QCache3QTileEvictionPolicy'

  #  Qt's '~QCache3QTileEvictionPolicy()'. Naming it makes this a value
  #  class: Python owns every C++ QCache3QTileEvictionPolicy behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QCache3QTileEvictionPolicyD1Ev'

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
  def aboutToBeEvicted(*__, **_) -> Never:
    """
    Qt's 'void QCache3QTileEvictionPolicy::aboutToBeEvicted(const
    QGeoTileSpec &key, QSharedPointer<QGeoCachedTileDisk> obj)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCache3QTileEvictionPolicy.aboutToBeEvicted' has no cute function "
        "yet. Qt's 'void QCache3QTileEvictionPolicy::aboutToBeEvicted(const "
        "QGeoTileSpec &key, QSharedPointer<QGeoCachedTileDisk> obj)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def aboutToBeRemoved(*__, **_) -> Never:
    """
    Qt's 'void QCache3QTileEvictionPolicy::aboutToBeRemoved(const
    QGeoTileSpec &key, QSharedPointer<QGeoCachedTileDisk> obj)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCache3QTileEvictionPolicy.aboutToBeRemoved' has no cute function "
        "yet. Qt's 'void QCache3QTileEvictionPolicy::aboutToBeRemoved(const "
        "QGeoTileSpec &key, QSharedPointer<QGeoCachedTileDisk> obj)': takes "
        "a type Python has no way to hand over yet.")
