"""
HPack::BitIStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means HPack::BitIStream to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class BitIStream(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::BitIStream: a plain Python object standing in
  front of one C++ HPack::BitIStream.

  C++ hands a HPack::BitIStream around as a copy, so every C++
  HPack::BitIStream behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's HPack::BitIStream that has a ritual and that Python
  can call so far, 7 names in all: 'bitLength', 'hasMoreBits',
  'streamOffset', 'skipBits', 'rewindOffset', 'error', 'setError'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HPack::BitIStream::BitIStream(const uchar *f, const uchar *l)':
    names 'uchar', which has no cute class yet.
  - Qt's 'bool HPack::BitIStream::read(quint32 *dstPtr)': takes a number to
    change where it is.
  - Qt's 'HPack::BitIStream::~BitIStream()': the destructor: Python removes
    its C++ HPack::BitIStream by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 1 a template; 1 leans on 'HPack.

  What to expect
  --------------

  - The C++ HPack::BitIStream is created at the first use, not by
    'HPack::BitIStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a HPack::BitIStream back gives a copy the ritual made
    for Python, in a new cute HPack::BitIStream.
  - Each name of Qt's HPack::BitIStream that has no cute function yet,
    'peekBits', 'read', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside HPack::BitIStream, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'HPack::BitIStream::Error' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoError = Kee[int](0)
    NotEnoughData = Kee[int](1)
    CompressionError = Kee[int](2)
    InvalidInteger = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HPack::BitIStream'

  #  Qt's '~HPack::BitIStream()'. Naming it makes this a value class: Python
  #  owns every C++ HPack::BitIStream behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN5HPack10BitIStreamD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bitLength(self) -> int:
    """
    Calls Qt's 'quint64 HPack::BitIStream::bitLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#bitLength
    """
    #  quint64 HPack::BitIStream::bitLength() const
    return self.uglySide.call('ritual_ZNK5HPack10BitIStream9bitLengthEv')

  def hasMoreBits(self) -> bool:
    """
    Calls Qt's 'bool HPack::BitIStream::hasMoreBits() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#hasMoreBits
    """
    #  bool HPack::BitIStream::hasMoreBits() const
    return self.uglySide.call('ritual_ZNK5HPack10BitIStream11hasMoreBitsEv')

  def streamOffset(self) -> int:
    """
    Calls Qt's 'quint64 HPack::BitIStream::streamOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#streamOffset
    """
    #  quint64 HPack::BitIStream::streamOffset() const
    return self.uglySide.call('ritual_ZNK5HPack10BitIStream12streamOffsetEv')

  def error(self) -> Error:
    """
    Calls Qt's 'Error HPack::BitIStream::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error HPack::BitIStream::error() const
    return BitIStream.Error(self.uglySide.call(
        'ritual_ZNK5HPack10BitIStream5errorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Error)
  def setError(self, newState: Error) -> None:
    """
    Calls Qt's 'void HPack::BitIStream::setError(Error newState)'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#setError

    Parameters
    ----------

    newState : Error
      Passed on as its number.
    """
    #  void HPack::BitIStream::setError(Error newState)
    self.uglySide.call(
        'ritual_ZN5HPack10BitIStream8setErrorENS0_5ErrorE', newState.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'HPack::BitIStream::BitIStream()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#BitIStream
    """
    #  HPack::BitIStream::BitIStream()
    self._noteCreation(BitIStream, lambda: Rituals.call(
        'ritual_ZN5HPack10BitIStreamC1Ev',
    ))

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

  @overload(int)
  def skipBits(self, nBits: int) -> bool:
    """
    Calls Qt's 'bool HPack::BitIStream::skipBits(quint64 nBits)'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#skipBits

    Parameters
    ----------

    nBits : int
      Passed on as it is.
    """
    #  bool HPack::BitIStream::skipBits(quint64 nBits)
    return self.uglySide.call(
        'ritual_ZN5HPack10BitIStream8skipBitsEy', nBits,
    )

  @overload(int)
  def rewindOffset(self, nBits: int) -> bool:
    """
    Calls Qt's 'bool HPack::BitIStream::rewindOffset(quint64 nBits)'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-bitistream.html#rewindOffset

    Parameters
    ----------

    nBits : int
      Passed on as it is.
    """
    #  bool HPack::BitIStream::rewindOffset(quint64 nBits)
    return self.uglySide.call(
        'ritual_ZN5HPack10BitIStream12rewindOffsetEy', nBits,
    )

  @staticmethod
  def peekBits(*__, **_) -> Never:
    """
    Qt's 'HPack::BitIStream::peekBits': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'HPack.BitIStream.peekBits' has no cute function yet. Qt's "
        "'HPack::BitIStream::peekBits': a template: a pattern and no single "
        "function.")

  @staticmethod
  def read(*__, **_) -> Never:
    """
    - Qt's 'bool HPack::BitIStream::read(quint32 *dstPtr)': takes a number to
      change where it is.
    - Qt's 'bool HPack::BitIStream::read(QByteArray *dstPtr)': leans on
      'HPack::huffman_decode_string(HPack::BitIStream&, QByteArray*)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'HPack.BitIStream.read' has no cute function yet. Qt's 'bool "
        "HPack::BitIStream::read(quint32 *dstPtr)': takes a number to "
        "change where it is. Qt's 'bool HPack::BitIStream::read(QByteArray "
        "*dstPtr)': leans on "
        "'HPack::huffman_decode_string(HPack::BitIStream&, QByteArray*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
