"""
QQmlPropertyCacheVector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertycachevector_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlPropertyCacheVector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlPropertyCacheVector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyCacheVector: a plain Python object
  standing in front of one C++ QQmlPropertyCacheVector.

  What exists
  -----------

  Every function of Qt's QQmlPropertyCacheVector that has a ritual and that
  Python can call so far, 12 names in all: 'resize', 'count', 'isEmpty',
  'clear', 'resetAndResize', 'append', 'at', 'set', 'setNeedsVMEMetaObject',
  'needsVMEMetaObject', 'seal', 'releaseElement'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQmlPropertyCacheVector::QQmlPropertyCacheVector(QQmlPropertyCacheVector
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlPropertyCacheVector
    &QQmlPropertyCacheVector::operator=(QQmlPropertyCacheVector &&a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlPropertyCacheVector::~QQmlPropertyCacheVector()': the
    destructor: Python never removes a C++ QQmlPropertyCacheVector.
  - Qt's 'void QQmlPropertyCacheVector::appendOwn(const
    QQmlPropertyCache::Ptr &cache)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCacheVector::ownAt(int index)
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlPropertyCacheVector::setOwn(int index, const
    QQmlPropertyCache::Ptr &replacement)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlPropertyCacheVector is created at the first use, not by
    'QQmlPropertyCacheVector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyCacheVector.
  - Each name of Qt's QQmlPropertyCacheVector that has no cute function yet,
    'appendOwn', 'ownAt', 'setOwn', holds a function that raises
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
  __qt_class__ = 'QQmlPropertyCacheVector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCacheVector::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycachevector.html#count
    """
    #  int QQmlPropertyCacheVector::count() const
    return self.uglySide.call('ritual_ZNK23QQmlPropertyCacheVector5countEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyCacheVector::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#isEmpty
    """
    #  bool QQmlPropertyCacheVector::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK23QQmlPropertyCacheVector7isEmptyEv',
    )

  @overload(int)
  def at(self, index: int) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr QQmlPropertyCacheVector::at(int
    index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycachevector.html#at

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlPropertyCacheVector::at(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlPropertyCacheVector2atEi', index,
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(int)
  def needsVMEMetaObject(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyCacheVector::needsVMEMetaObject(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#needsVMEMetaObject

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQmlPropertyCacheVector::needsVMEMetaObject(int index) const
    return self.uglySide.call(
        'ritual_ZNK23QQmlPropertyCacheVector18needsVMEMetaObjectEi', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNeedsVMEMetaObject(self, index: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::setNeedsVMEMetaObject(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#setNeedsVMEMetaObject

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQmlPropertyCacheVector::setNeedsVMEMetaObject(int index)
    self.uglySide.call(
        'ritual_ZN23QQmlPropertyCacheVector21setNeedsVMEMetaObjectEi', index,
    )

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
    'QQmlPropertyCacheVector::QQmlPropertyCacheVector()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html
    """
    #  QQmlPropertyCacheVector::QQmlPropertyCacheVector()
    self._noteCreation(QQmlPropertyCacheVector, lambda: Rituals.call(
        'ritual_ZN23QQmlPropertyCacheVectorC1Ev',
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

  @overload(int)
  def resize(self, size: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::resize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#resize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQmlPropertyCacheVector::resize(int size)
    self.uglySide.call('ritual_ZN23QQmlPropertyCacheVector6resizeEi', size)

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycachevector.html#clear
    """
    #  void QQmlPropertyCacheVector::clear()
    self.uglySide.call('ritual_ZN23QQmlPropertyCacheVector5clearEv')

  @overload(int)
  def resetAndResize(self, size: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::resetAndResize(int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#resetAndResize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QQmlPropertyCacheVector::resetAndResize(int size)
    self.uglySide.call(
        'ritual_ZN23QQmlPropertyCacheVector14resetAndResizeEi', size,
    )

  @overload(QQmlPropertyCache.ConstPtr)
  def append(self, cache: QQmlPropertyCache.ConstPtr) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::append(const
    QQmlPropertyCache::ConstPtr &cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#append

    Parameters
    ----------

    cache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QQmlPropertyCacheVector::append(const QQmlPropertyCache::ConstPtr
    #      &cache)
    self.uglySide.call(
        'ritual_ZN23QQmlPropertyCacheVector6appendERKN17QQmlPropertyCache8C'
        'onstPtrE',
        self._valueOf(cache),
    )

  @overload(int, QQmlPropertyCache.ConstPtr)
  def set(self, index: int, replacement: QQmlPropertyCache.ConstPtr) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::set(int index, const
    QQmlPropertyCache::ConstPtr &replacement)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycachevector.html#set

    Parameters
    ----------

    index : int
      Passed on as it is.

    replacement : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QQmlPropertyCacheVector::set(int index, const
    #      QQmlPropertyCache::ConstPtr &replacement)
    self.uglySide.call(
        'ritual_ZN23QQmlPropertyCacheVector3setEiRKN17QQmlPropertyCache8Con'
        'stPtrE',
        index, self._valueOf(replacement),
    )

  def seal(self) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::seal()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycachevector.html#seal
    """
    #  void QQmlPropertyCacheVector::seal()
    self.uglySide.call('ritual_ZN23QQmlPropertyCacheVector4sealEv')

  @overload(int)
  def releaseElement(self, i: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyCacheVector::releaseElement(int i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycachevector.html#releaseElement

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QQmlPropertyCacheVector::releaseElement(int i)
    self.uglySide.call(
        'ritual_ZN23QQmlPropertyCacheVector14releaseElementEi', i,
    )

  @staticmethod
  def appendOwn(*__, **_) -> Never:
    """
    Qt's 'void QQmlPropertyCacheVector::appendOwn(const
    QQmlPropertyCache::Ptr &cache)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheVector.appendOwn' has no cute function yet. Qt's "
        "'void QQmlPropertyCacheVector::appendOwn(const "
        "QQmlPropertyCache::Ptr &cache)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def ownAt(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCacheVector::ownAt(int index)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheVector.ownAt' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlPropertyCacheVector::ownAt(int index) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setOwn(*__, **_) -> Never:
    """
    Qt's 'void QQmlPropertyCacheVector::setOwn(int index, const
    QQmlPropertyCache::Ptr &replacement)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCacheVector.setOwn' has no cute function yet. Qt's "
        "'void QQmlPropertyCacheVector::setOwn(int index, const "
        "QQmlPropertyCache::Ptr &replacement)': takes a type Python has no "
        "way to hand over yet.")
