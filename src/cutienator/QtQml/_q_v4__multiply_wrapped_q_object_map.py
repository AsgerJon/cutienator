"""
QV4::MultiplyWrappedQObjectMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::MultiplyWrappedQObjectMap to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MultiplyWrappedQObjectMap(QObject):
  """
  The cute side of Qt's QV4::MultiplyWrappedQObjectMap: a plain Python object
  standing in front of one C++ QV4::MultiplyWrappedQObjectMap.

  It is built on the cute 'QObject', as Qt's QV4::MultiplyWrappedQObjectMap
  is built on Qt's QObject, and has everything that class has. Qt's
  QV4::MultiplyWrappedQObjectMap is built on Qt's QHash<QObjectBiPointer,
  QV4::WeakValue> as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QV4::MultiplyWrappedQObjectMap that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject',
  'removeDestroyedObject'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QV4::MultiplyWrappedQObjectMap::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QV4::MultiplyWrappedQObjectMap::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'ConstIterator QV4::MultiplyWrappedQObjectMap::begin() const': gives
    a type Python has no way to take yet.
  - Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::begin()': gives a type
    Python has no way to take yet.
  - Qt's 'ConstIterator QV4::MultiplyWrappedQObjectMap::end() const': gives a
    type Python has no way to take yet.
  - Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::end()': gives a type
    Python has no way to take yet.
  - Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::erase(Iterator it)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 16 functions Qt declares: 4 a template; 2 not a gap; 1 leans on
  'QV4.

  What to expect
  --------------

  - The C++ QV4::MultiplyWrappedQObjectMap is created at the first use, not
    by 'QV4::MultiplyWrappedQObjectMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::MultiplyWrappedQObjectMap.
  - Qt tells when it has removed the C++ QV4::MultiplyWrappedQObjectMap.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QV4::MultiplyWrappedQObjectMap that has no cute
    function yet, 'begin', 'end', 'erase', 'insert', 'mark', 'remove',
    'value', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QV4::MultiplyWrappedQObjectMap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QV4::MultiplyWrappedQObjectMap::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-multiplywrappedqobjectmap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::MultiplyWrappedQObjectMap::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV425MultiplyWrappedQObjectMap10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QObject)
  @overload(NoneType)
  def removeDestroyedObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QV4::MultiplyWrappedQObjectMap::removeDestroyedObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-multiplywrappedqobjectmap.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::MultiplyWrappedQObjectMap::removeDestroyedObject(QObject
    #      *a0)
    self.uglySide.call(
        'ritual_ZN3QV425MultiplyWrappedQObjectMap21removeDestroyedObjectEP7'
        'QObject',
        self._addressOf(a0, 'QObject'),
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    - Qt's 'ConstIterator QV4::MultiplyWrappedQObjectMap::begin() const':
      gives a type Python has no way to take yet.
    - Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::begin()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.begin' has no cute function yet. "
        "Qt's 'ConstIterator QV4::MultiplyWrappedQObjectMap::begin() "
        "const': gives a type Python has no way to take yet. Qt's 'Iterator "
        "QV4::MultiplyWrappedQObjectMap::begin()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    - Qt's 'ConstIterator QV4::MultiplyWrappedQObjectMap::end() const': gives
      a type Python has no way to take yet.
    - Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::end()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.end' has no cute function yet. Qt's "
        "'ConstIterator QV4::MultiplyWrappedQObjectMap::end() const': gives "
        "a type Python has no way to take yet. Qt's 'Iterator "
        "QV4::MultiplyWrappedQObjectMap::end()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def erase(*__, **_) -> Never:
    """
    Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::erase(Iterator it)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.erase' has no cute function yet. "
        "Qt's 'Iterator QV4::MultiplyWrappedQObjectMap::erase(Iterator "
        "it)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    Qt's 'QV4::MultiplyWrappedQObjectMap::insert': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.insert' has no cute function yet. "
        "Qt's 'QV4::MultiplyWrappedQObjectMap::insert': a template: a "
        "pattern and no single function.")

  @staticmethod
  def mark(*__, **_) -> Never:
    """
    Qt's 'QV4::MultiplyWrappedQObjectMap::mark': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.mark' has no cute function yet. "
        "Qt's 'QV4::MultiplyWrappedQObjectMap::mark': a template: a pattern "
        "and no single function.")

  @staticmethod
  def remove(*__, **_) -> Never:
    """
    Qt's 'QV4::MultiplyWrappedQObjectMap::remove': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.remove' has no cute function yet. "
        "Qt's 'QV4::MultiplyWrappedQObjectMap::remove': a template: a "
        "pattern and no single function.")

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QV4::MultiplyWrappedQObjectMap::value': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QV4.MultiplyWrappedQObjectMap.value' has no cute function yet. "
        "Qt's 'QV4::MultiplyWrappedQObjectMap::value': a template: a "
        "pattern and no single function.")
