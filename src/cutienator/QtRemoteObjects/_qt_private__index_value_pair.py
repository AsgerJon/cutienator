"""
QtPrivate::IndexValuePair binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtPrivate::IndexValuePair to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class IndexValuePair(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::IndexValuePair: a plain Python object
  standing in front of one C++ QtPrivate::IndexValuePair.

  C++ hands a QtPrivate::IndexValuePair around as a copy, so every C++
  QtPrivate::IndexValuePair behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::IndexValuePair that has a ritual and that
  Python can call so far, 2 names in all: '__eq__', '__ne__'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::IndexValuePair::IndexValuePair(const IndexList index_,
    const QVariantList &data_, bool hasChildren_, const Qt::ItemFlags
    &flags_, const QSize &size_)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QtPrivate::IndexValuePair::~IndexValuePair()': the destructor:
    Python removes its C++ QtPrivate::IndexValuePair by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtPrivate::IndexValuePair is created at the first use, not by
    'QtPrivate::IndexValuePair(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::IndexValuePair back gives a copy the
    ritual made for Python, in a new cute QtPrivate::IndexValuePair.
  - Each name of Qt's QtPrivate::IndexValuePair that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::IndexValuePair'

  #  Qt's '~QtPrivate::IndexValuePair()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::IndexValuePair behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate14IndexValuePairD1Ev'

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
  def __eq__(self, other: IndexValuePair) -> bool:
    """
    Calls Qt's 'bool QtPrivate::IndexValuePair::operator==(const
    IndexValuePair &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-indexvaluepair.html#operator==

    Parameters
    ----------

    other : IndexValuePair
      Passed on as a value: Qt reads the C++ QtPrivate::IndexValuePair, which
      stays Python's own.
    """
    #  bool QtPrivate::IndexValuePair::operator==(const IndexValuePair
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate14IndexValuePaireqERKS0_', self._valueOf(other),
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
  def __ne__(self, other: IndexValuePair) -> bool:
    """
    Calls Qt's 'bool QtPrivate::IndexValuePair::operator!=(const
    IndexValuePair &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-indexvaluepair.html#operator!=

    Parameters
    ----------

    other : IndexValuePair
      Passed on as a value: Qt reads the C++ QtPrivate::IndexValuePair, which
      stays Python's own.
    """
    #  bool QtPrivate::IndexValuePair::operator!=(const IndexValuePair
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate14IndexValuePairneERKS0_', self._valueOf(other),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::IndexValuePair::IndexValuePair(const IndexList index_,
    const QVariantList &data_, bool hasChildren_, const Qt::ItemFlags
    &flags_, const QSize &size_)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QtPrivate.IndexValuePair.__init__' has no cute function yet. Qt's "
        "'QtPrivate::IndexValuePair::IndexValuePair(const IndexList index_, "
        "const QVariantList &data_, bool hasChildren_, const Qt::ItemFlags "
        "&flags_, const QSize &size_)': takes a type Python has no way to "
        "hand over yet.")

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
