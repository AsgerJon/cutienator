"""
QV4::Heap::StringOrSymbol binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Heap::StringOrSymbol to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StringOrSymbol(QV4.Heap.Base):
  """
  The cute side of Qt's QV4::Heap::StringOrSymbol: a plain Python object
  standing in front of one C++ QV4::Heap::StringOrSymbol.

  It is built on the cute 'QV4::Heap::Base', as Qt's
  QV4::Heap::StringOrSymbol is built on Qt's QV4::Heap::Base, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::StringOrSymbol that has a ritual and that
  Python can call so far, 6 names in all: 'init', 'markObjects', 'destroy',
  'toQString', 'createHashValue', 'hashValue'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Heap::StringOrSymbol::init(QStringPrivate text)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QStringPrivate &QV4::Heap::StringOrSymbol::text() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QV4::Heap::StringOrSymbol is created at the first use, not by
    'QV4::Heap::StringOrSymbol(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::StringOrSymbol.
  - Each name of Qt's QV4::Heap::StringOrSymbol that has no cute function
    yet, 'text', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QV4::Heap::StringOrSymbol, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class StringType(CuteNum):
    """
    The enum 'QV4::Heap::StringOrSymbol::StringType' of Qt, with the 7 names
    Qt gives in it.
    """

    StringType_Symbol = Kee[int](0)
    StringType_Regular = Kee[int](1)
    StringType_ArrayIndex = Kee[int](2)
    StringType_Unknown = Kee[int](3)
    StringType_AddedString = Kee[int](4)
    StringType_SubString = Kee[int](5)
    StringType_Complex = Kee[int](4)

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
    Calls Qt's 'void QV4::Heap::StringOrSymbol::markObjects(Heap::Base *that,
    MarkStack *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringorsymbol.html#markObjects

    Parameters
    ----------

    that : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::StringOrSymbol::markObjects(Heap::Base *that,
    #      MarkStack *markStack)
    Rituals.call(
        'ritual_ZN3QV44Heap14StringOrSymbol11markObjectsEPNS0_4BaseEPNS_9Ma'
        'rkStackE',
        CuteMixin._addressOf(that), CuteMixin._addressOf(markStack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::StringOrSymbol'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toQString(self) -> str:
    """
    Calls Qt's 'QString QV4::Heap::StringOrSymbol::toQString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringorsymbol.html#toQString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Heap::StringOrSymbol::toQString() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap14StringOrSymbol9toQStringEv',
    )

  def hashValue(self) -> int:
    """
    Calls Qt's 'unsigned int QV4::Heap::StringOrSymbol::hashValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringorsymbol.html#hashValue
    """
    #  unsigned int QV4::Heap::StringOrSymbol::hashValue() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap14StringOrSymbol9hashValueEv',
    )

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

  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::StringOrSymbol::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-stringorsymbol.html#init
    """
    #  void QV4::Heap::StringOrSymbol::init()
    self.uglySide.call('ritual_ZN3QV44Heap14StringOrSymbol4initEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::StringOrSymbol::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringorsymbol.html#destroy
    """
    #  void QV4::Heap::StringOrSymbol::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap14StringOrSymbol7destroyEv')

  def createHashValue(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::StringOrSymbol::createHashValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-stringorsymbol.html#createHashValue
    """
    #  void QV4::Heap::StringOrSymbol::createHashValue() const
    self.uglySide.call(
        'ritual_ZNK3QV44Heap14StringOrSymbol15createHashValueEv',
    )

  @staticmethod
  def text(*__, **_) -> Never:
    """
    Qt's 'QStringPrivate &QV4::Heap::StringOrSymbol::text() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.StringOrSymbol.text' has no cute function yet. Qt's "
        "'QStringPrivate &QV4::Heap::StringOrSymbol::text() const': gives a "
        "type Python has no way to take yet.")
