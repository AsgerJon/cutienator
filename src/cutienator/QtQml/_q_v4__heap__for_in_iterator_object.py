"""
QV4::Heap::ForInIteratorObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::ForInIteratorObject to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class ForInIteratorObject(QV4.Heap.Object, QV4.Heap.ForInIteratorObjectData):
  """
  The cute side of Qt's QV4::Heap::ForInIteratorObject: a plain Python object
  standing in front of one C++ QV4::Heap::ForInIteratorObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::ForInIteratorObject is built on Qt's QV4::Heap::Object, and has
  everything that class has. It is built on the cute
  'QV4::Heap::ForInIteratorObjectData' as well, as Qt's
  QV4::Heap::ForInIteratorObject is built on Qt's
  QV4::Heap::ForInIteratorObjectData too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ForInIteratorObject that has a ritual and
  that Python can call so far, 3 names in all: 'init', 'markObjects',
  'destroy'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::ForInIteratorObject is created at the first use, not
    by 'QV4::Heap::ForInIteratorObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ForInIteratorObject.
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
      that: Optional[QV4.Heap.Base],
      markStack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ForInIteratorObject::markObjects(Heap::Base
    *that, MarkStack *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-foriniteratorobject.html#markObjects

    Parameters
    ----------

    that : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ForInIteratorObject::markObjects(Heap::Base *that,
    #      MarkStack *markStack)
    Rituals.call(
        'ritual_ZN3QV44Heap19ForInIteratorObject11markObjectsEPNS0_4BaseEPN'
        'S_9MarkStackE',
        CuteMixin._addressOf(that), CuteMixin._addressOf(markStack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ForInIteratorObject'

  #  Qt's QV4::Heap::ForInIteratorObject is built on more than one class. The
  #  part of a C++ QV4::Heap::ForInIteratorObject that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::ForInIteratorObjectData':
          'ritual_cast_QV4_Heap_ForInIteratorObject_QV4_Heap_ForInIteratorObjectData',
  }

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

  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def init(self, o: Optional[QV4.Object]) -> None:
    """
    Calls Qt's 'void QV4::Heap::ForInIteratorObject::init(QV4::Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-foriniteratorobject.html#init

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ForInIteratorObject::init(QV4::Object *o)
    self.uglySide.call(
        'ritual_ZN3QV44Heap19ForInIteratorObject4initEPNS_6ObjectE',
        self._addressOf(o),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::ForInIteratorObject::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-foriniteratorobject.html#destroy
    """
    #  void QV4::Heap::ForInIteratorObject::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap19ForInIteratorObject7destroyEv')
