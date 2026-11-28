"""
HPack::BitOStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means HPack::BitOStream to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class BitOStream(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::BitOStream: a plain Python object standing in
  front of one C++ HPack::BitOStream.

  What exists
  -----------

  Every function of Qt's HPack::BitOStream that has a ritual and that Python
  can call so far, 5 names in all: 'writeBits', 'write', 'bitLength',
  'byteLength', 'clear'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HPack::BitOStream::BitOStream(std::vector<uchar> &buffer)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const uchar *HPack::BitOStream::begin() const': gives 'unsigned
    char', which has no cute class yet.
  - Qt's 'const uchar *HPack::BitOStream::end() const': gives 'unsigned
    char', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 4 forbidden; 1 leans on 'HPack.

  What to expect
  --------------

  - The C++ HPack::BitOStream is created at the first use, not by
    'HPack::BitOStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ HPack::BitOStream.
  - Each name of Qt's HPack::BitOStream that has no cute function yet,
    '__init__', 'begin', 'end', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HPack::BitOStream'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bitLength(self) -> int:
    """
    Calls Qt's 'quint64 HPack::BitOStream::bitLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitostream.html#bitLength
    """
    #  quint64 HPack::BitOStream::bitLength() const
    return self.uglySide.call('ritual_ZNK5HPack10BitOStream9bitLengthEv')

  def byteLength(self) -> int:
    """
    Calls Qt's 'quint64 HPack::BitOStream::byteLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitostream.html#byteLength
    """
    #  quint64 HPack::BitOStream::byteLength() const
    return self.uglySide.call('ritual_ZNK5HPack10BitOStream10byteLengthEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'HPack::BitOStream::BitOStream(std::vector<uchar> &buffer)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'HPack.BitOStream.__init__' has no cute function yet. Qt's "
        "'HPack::BitOStream::BitOStream(std::vector<uchar> &buffer)': takes "
        "a type Python has no way to hand over yet.")

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

  @overload(int, int)
  def writeBits(self, bits: int, bitLength: int) -> None:
    """
    Calls Qt's 'void HPack::BitOStream::writeBits(uchar bits, quint8
    bitLength)'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitostream.html#writeBits

    Parameters
    ----------

    bits : int
      Passed on as it is.

    bitLength : int
      Passed on as it is.
    """
    #  void HPack::BitOStream::writeBits(uchar bits, quint8 bitLength)
    self.uglySide.call(
        'ritual_ZN5HPack10BitOStream9writeBitsEhh', bits, bitLength,
    )

  @overload(int)
  def write(self, src: int) -> None:
    """
    Calls Qt's 'void HPack::BitOStream::write(quint32 src)'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitostream.html#write

    Parameters
    ----------

    src : int
      Passed on as it is.
    """
    #  void HPack::BitOStream::write(quint32 src)
    self.uglySide.call('ritual_ZN5HPack10BitOStream5writeEj', src)

  def clear(self) -> None:
    """
    Calls Qt's 'void HPack::BitOStream::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitostream.html#clear
    """
    #  void HPack::BitOStream::clear()
    self.uglySide.call('ritual_ZN5HPack10BitOStream5clearEv')

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'const uchar *HPack::BitOStream::begin() const': gives 'unsigned
    char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'HPack.BitOStream.begin' has no cute function yet. Qt's 'const "
        "uchar *HPack::BitOStream::begin() const': gives 'unsigned char', "
        "which has no cute class yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'const uchar *HPack::BitOStream::end() const': gives 'unsigned
    char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'HPack.BitOStream.end' has no cute function yet. Qt's 'const uchar "
        "*HPack::BitOStream::end() const': gives 'unsigned char', which has "
        "no cute class yet.")
