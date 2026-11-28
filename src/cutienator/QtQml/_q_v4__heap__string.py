"""
QV4::Heap::String binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Heap::String to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class String(QV4.Heap.StringOrSymbol):
  """
  The cute side of Qt's QV4::Heap::String: a plain Python object standing in
  front of one C++ QV4::Heap::String.

  It is built on the cute 'QV4::Heap::StringOrSymbol', as Qt's
  QV4::Heap::String is built on Qt's QV4::Heap::StringOrSymbol, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::String that has a ritual and that Python
  can call so far, 9 names in all: 'markObjects', 'init', 'simplifyString',
  'length', 'retainedTextSize', 'toQString', 'isEqualTo', 'startsWithUpper',
  'append'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const VTable *QV4::Heap::String::vtable() const': gives
    'QV4::VTable', which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::Heap::String is created at the first use, not by
    'QV4::Heap::String(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::String.
  - Each name of Qt's QV4::Heap::String that has no cute function yet,
    'vtable', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'void QV4::Heap::String::markObjects(Heap::Base *that,
    MarkStack *markStack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-string.html#markObjects

    Parameters
    ----------

    that : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::String::markObjects(Heap::Base *that, MarkStack
    #      *markStack)
    Rituals.call(
        'ritual_ZN3QV44Heap6String11markObjectsEPNS0_4BaseEPNS_9MarkStackE',
        CuteMixin._addressOf(that), CuteMixin._addressOf(markStack),
    )

  @staticmethod
  @overload(THIS, QChar)
  @overload(THIS, NoneType)
  @overload(NoneType, QChar)
  @overload(NoneType, NoneType)
  def append(data: Optional[String], ch: Optional[QChar]) -> None:
    """
    Calls Qt's 'void QV4::Heap::String::append(const String *data, QChar
    *ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-string.html#append

    Parameters
    ----------

    data : Optional[String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ch : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::String::append(const String *data, QChar *ch)
    Rituals.call(
        'ritual_ZN3QV44Heap6String6appendEPKS1_P5QChar',
        CuteMixin._addressOf(data), CuteMixin._addressOf(ch),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::String'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def length(self) -> int:
    """
    Calls Qt's 'int QV4::Heap::String::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-string.html#length
    """
    #  int QV4::Heap::String::length() const
    return self.uglySide.call('ritual_ZNK3QV44Heap6String6lengthEv')

  def retainedTextSize(self) -> int:
    """
    Calls Qt's 'std::size_t QV4::Heap::String::retainedTextSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-string.html#retainedTextSize
    """
    #  std::size_t QV4::Heap::String::retainedTextSize() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap6String16retainedTextSizeEv',
    )

  def toQString(self) -> str:
    """
    Calls Qt's 'QString QV4::Heap::String::toQString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-string.html#toQString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Heap::String::toQString() const
    return self.uglySide.call('ritual_ZNK3QV44Heap6String9toQStringEv')

  @overload(THIS)
  @overload(NoneType)
  def isEqualTo(self, other: Optional[String]) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::String::isEqualTo(const String *other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-string.html#isEqualTo

    Parameters
    ----------

    other : Optional[String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Heap::String::isEqualTo(const String *other) const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap6String9isEqualToEPKS1_', self._addressOf(other),
    )

  def startsWithUpper(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::String::startsWithUpper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-string.html#startsWithUpper
    """
    #  bool QV4::Heap::String::startsWithUpper() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap6String15startsWithUpperEv',
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

  @overload(str)
  def init(self, text: str) -> None:
    """
    Calls Qt's 'void QV4::Heap::String::init(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-string.html#init

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::Heap::String::init(const QString &text)
    self.uglySide.call('ritual_ZN3QV44Heap6String4initERK7QString', text)

  def simplifyString(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::String::simplifyString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-string.html#simplifyString
    """
    #  void QV4::Heap::String::simplifyString() const
    self.uglySide.call('ritual_ZNK3QV44Heap6String14simplifyStringEv')

  @staticmethod
  def vtable(*__, **_) -> Never:
    """
    Qt's 'const VTable *QV4::Heap::String::vtable() const': gives
    'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.String.vtable' has no cute function yet. Qt's 'const "
        "VTable *QV4::Heap::String::vtable() const': gives 'QV4::VTable', "
        "which has no cute class yet.")
