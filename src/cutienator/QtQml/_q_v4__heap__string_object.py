"""
QV4::Heap::StringObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::StringObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StringObject(QV4.Heap.Object, QV4.Heap.StringObjectData):
  """
  The cute side of Qt's QV4::Heap::StringObject: a plain Python object
  standing in front of one C++ QV4::Heap::StringObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::StringObject is built on Qt's QV4::Heap::Object, and has
  everything that class has. It is built on the cute
  'QV4::Heap::StringObjectData' as well, as Qt's QV4::Heap::StringObject is
  built on Qt's QV4::Heap::StringObjectData too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::StringObject that has a ritual and that
  Python can call so far, 4 names in all: 'markObjects', 'init', 'getIndex',
  'length'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::Heap::StringObject is created at the first use, not by
    'QV4::Heap::StringObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::StringObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::StringObject::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::StringObject::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap12StringObject11markObjectsEPNS0_4BaseEPNS_9Mark'
        'StackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::StringObject'

  #  Qt's QV4::Heap::StringObject is built on more than one class. The part
  #  of a C++ QV4::Heap::StringObject that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::StringObjectData':
          'ritual_cast_QV4_Heap_StringObject_QV4_Heap_StringObjectData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def getIndex(self, index: int) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::Heap::StringObject::getIndex(uint index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringobject.html#getIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::Heap::StringObject::getIndex(uint index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap12StringObject8getIndexEj', index,
    )
    return QV4.Heap.String._cuteAt(address)

  def length(self) -> int:
    """
    Calls Qt's 'uint QV4::Heap::StringObject::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-stringobject.html#length
    """
    #  uint QV4::Heap::StringObject::length() const
    return self.uglySide.call('ritual_ZNK3QV44Heap12StringObject6lengthEv')

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

  @overload(bool)
  def init(self, a0: bool) -> None:
    """
    Calls Qt's 'void QV4::Heap::StringObject::init(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-stringobject.html#init

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QV4::Heap::StringObject::init(bool a0)
    self.uglySide.call('ritual_ZN3QV44Heap12StringObject4initEb', a0)

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def init(self, string: Optional[QV4.String]) -> None:
    """
    Calls Qt's 'void QV4::Heap::StringObject::init(const QV4::String
    *string)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-stringobject.html#init

    Parameters
    ----------

    string : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::StringObject::init(const QV4::String *string)
    self.uglySide.call(
        'ritual_ZN3QV44Heap12StringObject4initEPKNS_6StringE',
        self._addressOf(string),
    )
