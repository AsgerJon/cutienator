"""
QV4::Heap::QObjectWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::QObjectWrapper to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectWrapper(QV4.Heap.Object):
  """
  The cute side of Qt's QV4::Heap::QObjectWrapper: a plain Python object
  standing in front of one C++ QV4::Heap::QObjectWrapper.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::QObjectWrapper is built on Qt's QV4::Heap::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QObjectWrapper that has a ritual and that
  Python can call so far, 4 names in all: 'init', 'destroy', 'object',
  'markObjects'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::QObjectWrapper is created at the first use, not by
    'QV4::Heap::QObjectWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QObjectWrapper.
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
    Calls Qt's 'void QV4::Heap::QObjectWrapper::markObjects(Heap::Base *that,
    MarkStack *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectwrapper.html#markObjects

    Parameters
    ----------

    that : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QObjectWrapper::markObjects(Heap::Base *that,
    #      MarkStack *markStack)
    Rituals.call(
        'ritual_ZN3QV44Heap14QObjectWrapper11markObjectsEPNS0_4BaseEPNS_9Ma'
        'rkStackE',
        CuteMixin._addressOf(that), CuteMixin._addressOf(markStack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::QObjectWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::Heap::QObjectWrapper::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectwrapper.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::Heap::QObjectWrapper::object() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap14QObjectWrapper6objectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

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
  def init(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QV4::Heap::QObjectWrapper::init(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qobjectwrapper.html#init

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QObjectWrapper::init(QObject *object)
    self.uglySide.call(
        'ritual_ZN3QV44Heap14QObjectWrapper4initEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QObjectWrapper::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qobjectwrapper.html#destroy
    """
    #  void QV4::Heap::QObjectWrapper::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap14QObjectWrapper7destroyEv')
