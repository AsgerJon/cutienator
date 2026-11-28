"""
QV4::MemberGeneratorFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::MemberGeneratorFunction to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class MemberGeneratorFunction(QV4.MemberFunction):
  """
  The cute side of Qt's QV4::MemberGeneratorFunction: a plain Python object
  standing in front of one C++ QV4::MemberGeneratorFunction.

  It is built on the cute 'QV4::MemberFunction', as Qt's
  QV4::MemberGeneratorFunction is built on Qt's QV4::MemberFunction, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::MemberGeneratorFunction that has a ritual and
  that Python can call so far, 4 names in all: '__dataTest', 'd_unchecked',
  'd', 'defaultInternalClass'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has no ritual
  ------------------

  7 of the 11 functions Qt declares: 3 forbidden; 3 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::MemberGeneratorFunction is created at the first use, not by
    'QV4::MemberGeneratorFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::MemberGeneratorFunction.
  - Each name of Qt's QV4::MemberGeneratorFunction that has no cute function
    yet, 'create', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::MemberGeneratorFunction::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-membergeneratorfunction.html

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::MemberGeneratorFunction::defaultInternalClass(QV4::
    #      EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV423MemberGeneratorFunction20defaultInternalClassEPNS_1'
        '0EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::MemberGeneratorFunction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.MemberGeneratorFunction]:
    """
    Calls Qt's 'QV4::Heap::MemberGeneratorFunction
    *QV4::MemberGeneratorFunction::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-membergeneratorfunction.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.MemberGeneratorFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::MemberGeneratorFunction
    #      *QV4::MemberGeneratorFunction::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV423MemberGeneratorFunction11d_uncheckedEv',
    )
    return QV4.Heap.MemberGeneratorFunction._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.MemberGeneratorFunction]:
    """
    Calls Qt's 'QV4::Heap::MemberGeneratorFunction
    *QV4::MemberGeneratorFunction::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-membergeneratorfunction.html#d

    Returns
    -------

    Optional[QV4.Heap.MemberGeneratorFunction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::MemberGeneratorFunction *QV4::MemberGeneratorFunction::d()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV423MemberGeneratorFunction1dEv',
    )
    return QV4.Heap.MemberGeneratorFunction._cuteAt(address)

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
    Calls Qt's 'void QV4::MemberGeneratorFunction::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-membergeneratorfunction.html#__dataTest
    """
    #  void QV4::MemberGeneratorFunction::__dataTest()
    self.uglySide.call(
        'ritual_ZN3QV423MemberGeneratorFunction10__dataTestEv',
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'Heap::FunctionObject
    *QV4::MemberGeneratorFunction::create(ExecutionContext *scope, Function
    *function, Object *homeObject, String *name)': leans on
    'QV4::MemberGeneratorFunction::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.MemberGeneratorFunction.create' has no cute function yet. "
        "Qt's 'Heap::FunctionObject "
        "*QV4::MemberGeneratorFunction::create(ExecutionContext *scope, "
        "Function *function, Object *homeObject, String *name)': leans on "
        "'QV4::MemberGeneratorFunction::static_vtbl', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
