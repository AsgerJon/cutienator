"""
QV4::ReferenceObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ReferenceObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ReferenceObject(QV4.Object):
  """
  The cute side of Qt's QV4::ReferenceObject: a plain Python object standing
  in front of one C++ QV4::ReferenceObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::ReferenceObject is
  built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ReferenceObject that has a ritual and that
  Python can call so far, 6 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'shouldConnect', 'connect'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  8 of the 14 functions Qt declares: 3 forbidden; 3 a template; 1 not a gap;
  1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::ReferenceObject is created at the first use, not by
    'QV4::ReferenceObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ReferenceObject.
  - Each name of Qt's QV4::ReferenceObject that has no cute function yet,
    'detached', 'readReference', 'writeBack', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::ReferenceObject::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-referenceobject.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ReferenceObject::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV415ReferenceObject14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.Heap.ReferenceObject'])
  @overload(NoneType)
  def shouldConnect(ref: Optional[QV4.Heap.ReferenceObject]) -> bool:
    """
    Calls Qt's 'bool
    QV4::ReferenceObject::shouldConnect(Heap::ReferenceObject *ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-referenceobject.html#shouldConnect

    Parameters
    ----------

    ref : Optional[QV4.Heap.ReferenceObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::ReferenceObject::shouldConnect(Heap::ReferenceObject *ref)
    return Rituals.call(
        'ritual_ZN3QV415ReferenceObject13shouldConnectEPNS_4Heap15Reference'
        'ObjectE',
        CuteMixin._addressOf(ref),
    )

  @staticmethod
  @overload(WAIT['QV4.Heap.ReferenceObject'])
  @overload(NoneType)
  def connect(ref: Optional[QV4.Heap.ReferenceObject]) -> None:
    """
    Calls Qt's 'void QV4::ReferenceObject::connect(Heap::ReferenceObject
    *ref)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-referenceobject.html#connect

    Parameters
    ----------

    ref : Optional[QV4.Heap.ReferenceObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ReferenceObject::connect(Heap::ReferenceObject *ref)
    Rituals.call(
        'ritual_ZN3QV415ReferenceObject7connectEPNS_4Heap15ReferenceObjectE',
        CuteMixin._addressOf(ref),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ReferenceObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ReferenceObject]:
    """
    Calls Qt's 'QV4::Heap::ReferenceObject
    *QV4::ReferenceObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-referenceobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ReferenceObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ReferenceObject *QV4::ReferenceObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV415ReferenceObject11d_uncheckedEv',
    )
    return QV4.Heap.ReferenceObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ReferenceObject]:
    """
    Calls Qt's 'QV4::Heap::ReferenceObject *QV4::ReferenceObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-referenceobject.html#d

    Returns
    -------

    Optional[QV4.Heap.ReferenceObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ReferenceObject *QV4::ReferenceObject::d() const
    address = self.uglySide.call('ritual_ZNK3QV415ReferenceObject1dEv')
    return QV4.Heap.ReferenceObject._cuteAt(address)

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::ReferenceObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-referenceobject.html#__dataTest
    """
    #  void QV4::ReferenceObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV415ReferenceObject10__dataTestEv')

  @staticmethod
  def detached(*__, **_) -> Never:
    """
    Qt's 'QV4::ReferenceObject::detached': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.ReferenceObject.detached' has no cute function yet. Qt's "
        "'QV4::ReferenceObject::detached': a template: a pattern and no "
        "single function.")

  @staticmethod
  def readReference(*__, **_) -> Never:
    """
    Qt's 'QV4::ReferenceObject::readReference': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.ReferenceObject.readReference' has no cute function yet. Qt's "
        "'QV4::ReferenceObject::readReference': a template: a pattern and "
        "no single function.")

  @staticmethod
  def writeBack(*__, **_) -> Never:
    """
    Qt's 'QV4::ReferenceObject::writeBack': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QV4.ReferenceObject.writeBack' has no cute function yet. Qt's "
        "'QV4::ReferenceObject::writeBack': a template: a pattern and no "
        "single function.")
