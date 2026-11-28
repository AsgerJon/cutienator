"""
ProceduralMeshSubset binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralmesh_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means ProceduralMeshSubset to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ProceduralMeshSubset(QObject):
  """
  The cute side of Qt's ProceduralMeshSubset: a plain Python object standing
  in front of one C++ ProceduralMeshSubset.

  It is built on the cute 'QObject', as Qt's ProceduralMeshSubset is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ProceduralMeshSubset that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'offset',
  'setOffset', 'count', 'setCount', 'name', 'setName', 'offsetChanged',
  'countChanged', 'nameChanged', 'isDirty'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ProceduralMeshSubset::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int ProceduralMeshSubset::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ProceduralMeshSubset is created at the first use, not by
    'ProceduralMeshSubset(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ProceduralMeshSubset.
  - Qt tells when it has removed the C++ ProceduralMeshSubset. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString ProceduralMeshSubset::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString ProceduralMeshSubset::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20ProceduralMeshSubset2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ProceduralMeshSubset'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ProceduralMeshSubset::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmeshsubset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ProceduralMeshSubset::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20ProceduralMeshSubset10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def offset(self) -> int:
    """
    Calls Qt's 'int ProceduralMeshSubset::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#offset
    """
    #  int ProceduralMeshSubset::offset() const
    return self.uglySide.call('ritual_ZNK20ProceduralMeshSubset6offsetEv')

  def count(self) -> int:
    """
    Calls Qt's 'int ProceduralMeshSubset::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#count
    """
    #  int ProceduralMeshSubset::count() const
    return self.uglySide.call('ritual_ZNK20ProceduralMeshSubset5countEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString ProceduralMeshSubset::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString ProceduralMeshSubset::name() const
    return self.uglySide.call('ritual_ZNK20ProceduralMeshSubset4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setOffset(self, newOffset: int) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::setOffset(int newOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmeshsubset.html#setOffset

    Parameters
    ----------

    newOffset : int
      Passed on as it is.
    """
    #  void ProceduralMeshSubset::setOffset(int newOffset)
    self.uglySide.call(
        'ritual_ZN20ProceduralMeshSubset9setOffsetEi', newOffset,
    )

  @overload(int)
  def setCount(self, newCount: int) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::setCount(int newCount)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#setCount

    Parameters
    ----------

    newCount : int
      Passed on as it is.
    """
    #  void ProceduralMeshSubset::setCount(int newCount)
    self.uglySide.call(
        'ritual_ZN20ProceduralMeshSubset8setCountEi', newCount,
    )

  @overload(str)
  def setName(self, newName: str) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::setName(const QString &newName)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#setName

    Parameters
    ----------

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ProceduralMeshSubset::setName(const QString &newName)
    self.uglySide.call(
        'ritual_ZN20ProceduralMeshSubset7setNameERK7QString', newName,
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

  def offsetChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::offsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmeshsubset.html#offsetChanged
    """
    #  void ProceduralMeshSubset::offsetChanged()
    self.uglySide.call('ritual_ZN20ProceduralMeshSubset13offsetChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmeshsubset.html#countChanged
    """
    #  void ProceduralMeshSubset::countChanged()
    self.uglySide.call('ritual_ZN20ProceduralMeshSubset12countChangedEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmeshsubset.html#nameChanged
    """
    #  void ProceduralMeshSubset::nameChanged()
    self.uglySide.call('ritual_ZN20ProceduralMeshSubset11nameChangedEv')

  def isDirty(self) -> None:
    """
    Calls Qt's 'void ProceduralMeshSubset::isDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmeshsubset.html#isDirty
    """
    #  void ProceduralMeshSubset::isDirty()
    self.uglySide.call('ritual_ZN20ProceduralMeshSubset7isDirtyEv')
