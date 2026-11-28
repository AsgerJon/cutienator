"""
QV4::Heap::ErrorObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::ErrorObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ErrorObject(QV4.Heap.Object, QV4.Heap.ErrorObjectData):
  """
  The cute side of Qt's QV4::Heap::ErrorObject: a plain Python object
  standing in front of one C++ QV4::Heap::ErrorObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's QV4::Heap::ErrorObject
  is built on Qt's QV4::Heap::Object, and has everything that class has. It
  is built on the cute 'QV4::Heap::ErrorObjectData' as well, as Qt's
  QV4::Heap::ErrorObject is built on Qt's QV4::Heap::ErrorObjectData too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ErrorObject that has a ritual and that
  Python can call so far, 3 names in all: 'markObjects', 'init', 'destroy'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::ErrorObject is created at the first use, not by
    'QV4::Heap::ErrorObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ErrorObject.
  """

  #  The enums Qt writes inside QV4::Heap::ErrorObject, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ErrorType(CuteNum):
    """
    The enum 'QV4::Heap::ErrorObject::ErrorType' of Qt, with the 7 names Qt
    gives in it.
    """

    Error = Kee[int](0)
    EvalError = Kee[int](1)
    RangeError = Kee[int](2)
    ReferenceError = Kee[int](3)
    SyntaxError = Kee[int](4)
    TypeError = Kee[int](5)
    URIError = Kee[int](6)

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
    Calls Qt's 'void QV4::Heap::ErrorObject::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-errorobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ErrorObject::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap11ErrorObject11markObjectsEPNS0_4BaseEPNS_9MarkS'
        'tackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ErrorObject'

  #  Qt's QV4::Heap::ErrorObject is built on more than one class. The part of
  #  a C++ QV4::Heap::ErrorObject that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::ErrorObjectData':
          'ritual_cast_QV4_Heap_ErrorObject_QV4_Heap_ErrorObjectData',
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

  @overload()
  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::ErrorObject::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-errorobject.html#init
    """
    #  void QV4::Heap::ErrorObject::init()
    self.uglySide.call('ritual_ZN3QV44Heap11ErrorObject4initEv')

  @overload(WAIT['QV4.Value'])
  @overload(WAIT['QV4.Value'], ErrorType)
  def init(self, message: QV4.Value, t: ErrorType = ErrorType.Error) -> None:
    """
    Calls Qt's 'void QV4::Heap::ErrorObject::init(const Value &message,
    ErrorType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-errorobject.html#init

    Parameters
    ----------

    message : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    t : ErrorType
      Passed on as its number. May be left out, as in Qt: it is then
      ErrorType.Error.
    """
    #  void QV4::Heap::ErrorObject::init(const Value &message, ErrorType t)
    self.uglySide.call(
        'ritual_ZN3QV44Heap11ErrorObject4initERKNS_5ValueENS1_9ErrorTypeE',
        self._valueOf(message), t.value,
    )

  @overload(WAIT['QV4.Value'], str, int, int)
  @overload(WAIT['QV4.Value'], str, int, int, ErrorType)
  def init(
      self,
      message: QV4.Value,
      fileName: str,
      line: int,
      column: int,
      t: ErrorType = ErrorType.Error,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ErrorObject::init(const Value &message, const
    QString &fileName, int line, int column, ErrorType t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-errorobject.html#init

    Parameters
    ----------

    message : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.

    t : ErrorType
      Passed on as its number. May be left out, as in Qt: it is then
      ErrorType.Error.
    """
    #  void QV4::Heap::ErrorObject::init(const Value &message, const QString
    #      &fileName, int line, int column, ErrorType t)
    self.uglySide.call(
        'ritual_ZN3QV44Heap11ErrorObject4initERKNS_5ValueERK7QStringiiNS1_9'
        'ErrorTypeE',
        self._valueOf(message), fileName, line, column, t.value,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::ErrorObject::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-errorobject.html#destroy
    """
    #  void QV4::Heap::ErrorObject::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap11ErrorObject7destroyEv')
