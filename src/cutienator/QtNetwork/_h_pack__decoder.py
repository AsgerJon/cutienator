"""
HPack::Decoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/hpack_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means HPack::Decoder to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Decoder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::Decoder: a plain Python object standing in
  front of one C++ HPack::Decoder.

  What exists
  -----------

  Every function of Qt's HPack::Decoder that has a ritual and that Python can
  call so far, 5 names in all: 'dynamicTableSize', 'dynamicTableCapacity',
  'maxDynamicTableCapacity', 'setMaxDynamicTableSize',
  'setMaxHeaderListSize'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const HttpHeader &HPack::Decoder::decodedHeader() const': gives a
    type Python has no way to take yet.
  - Qt's 'void HPack::Decoder::handleStreamError(BitIStream &inputStream)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here; 2 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file; 1 leans on 'HPack.

  What to expect
  --------------

  - The C++ HPack::Decoder is created at the first use, not by
    'HPack::Decoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ HPack::Decoder.
  - Each name of Qt's HPack::Decoder that has no cute function yet,
    'decodeHeaderFields', 'decodeIndexedField', 'decodeLiteralField',
    'decodeSizeUpdate', 'decodedHeader', 'handleStreamError',
    'processDecodedField', holds a function that raises
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
  __qt_class__ = 'HPack::Decoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dynamicTableSize(self) -> int:
    """
    Calls Qt's 'quint32 HPack::Decoder::dynamicTableSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-decoder.html#dynamicTableSize
    """
    #  quint32 HPack::Decoder::dynamicTableSize() const
    return self.uglySide.call('ritual_ZNK5HPack7Decoder16dynamicTableSizeEv')

  def dynamicTableCapacity(self) -> int:
    """
    Calls Qt's 'quint32 HPack::Decoder::dynamicTableCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-decoder.html#dynamicTableCapacity
    """
    #  quint32 HPack::Decoder::dynamicTableCapacity() const
    return self.uglySide.call(
        'ritual_ZNK5HPack7Decoder20dynamicTableCapacityEv',
    )

  def maxDynamicTableCapacity(self) -> int:
    """
    Calls Qt's 'quint32 HPack::Decoder::maxDynamicTableCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-decoder.html#maxDynamicTableCapacity
    """
    #  quint32 HPack::Decoder::maxDynamicTableCapacity() const
    return self.uglySide.call(
        'ritual_ZNK5HPack7Decoder23maxDynamicTableCapacityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxDynamicTableSize(self, size: int) -> None:
    """
    Calls Qt's 'void HPack::Decoder::setMaxDynamicTableSize(quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-decoder.html#setMaxDynamicTableSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void HPack::Decoder::setMaxDynamicTableSize(quint32 size)
    self.uglySide.call(
        'ritual_ZN5HPack7Decoder22setMaxDynamicTableSizeEj', size,
    )

  @overload(int)
  def setMaxHeaderListSize(self, size: int) -> None:
    """
    Calls Qt's 'void HPack::Decoder::setMaxHeaderListSize(quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-decoder.html#setMaxHeaderListSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void HPack::Decoder::setMaxHeaderListSize(quint32 size)
    self.uglySide.call(
        'ritual_ZN5HPack7Decoder20setMaxHeaderListSizeEj', size,
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

  @overload(int)
  def __init__(self, maxTableSize: int) -> None:
    """
    Notes what was given, for Qt's 'HPack::Decoder::Decoder(quint32
    maxTableSize)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/hpack-decoder.html#Decoder

    Parameters
    ----------

    maxTableSize : int
      Passed on as it is.
    """
    #  HPack::Decoder::Decoder(quint32 maxTableSize)
    self._noteCreation(Decoder, lambda: Rituals.call(
        'ritual_ZN5HPack7DecoderC1Ej', maxTableSize,
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

  @staticmethod
  def decodeHeaderFields(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Decoder::decodeHeaderFields(class BitIStream
    &inputStream)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'LiteralIncrementalIndexing'.
    """
    raise NotImplementedError(
        "'HPack.Decoder.decodeHeaderFields' has no cute function yet. Qt's "
        "'bool HPack::Decoder::decodeHeaderFields(class BitIStream "
        "&inputStream)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'LiteralIncrementalIndexing'.")

  @staticmethod
  def decodeIndexedField(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Decoder::decodeIndexedField(BitIStream &inputStream)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'Indexed'; did
    you mean 'QPixelFormat::Indexed'?.
    """
    raise NotImplementedError(
        "'HPack.Decoder.decodeIndexedField' has no cute function yet. Qt's "
        "'bool HPack::Decoder::decodeIndexedField(BitIStream "
        "&inputStream)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'Indexed'; did you mean "
        "'QPixelFormat::Indexed'?.")

  @staticmethod
  def decodeLiteralField(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Decoder::decodeLiteralField(BitPattern fieldType,
    BitIStream &inputStream)': the compiler refuses its ritual as it would be
    written here: unknown type name 'BitPattern'; did you mean
    'HPack::BitPattern'?.
    """
    raise NotImplementedError(
        "'HPack.Decoder.decodeLiteralField' has no cute function yet. Qt's "
        "'bool HPack::Decoder::decodeLiteralField(BitPattern fieldType, "
        "BitIStream &inputStream)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'BitPattern'; did you "
        "mean 'HPack::BitPattern'?.")

  @staticmethod
  def decodeSizeUpdate(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Decoder::decodeSizeUpdate(BitIStream &inputStream)':
    leans on 'HPack::BitIStream::read(unsigned int*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'HPack.Decoder.decodeSizeUpdate' has no cute function yet. Qt's "
        "'bool HPack::Decoder::decodeSizeUpdate(BitIStream &inputStream)': "
        "leans on 'HPack::BitIStream::read(unsigned int*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def decodedHeader(*__, **_) -> Never:
    """
    Qt's 'const HttpHeader &HPack::Decoder::decodedHeader() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'HPack.Decoder.decodedHeader' has no cute function yet. Qt's "
        "'const HttpHeader &HPack::Decoder::decodedHeader() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def handleStreamError(*__, **_) -> Never:
    """
    Qt's 'void HPack::Decoder::handleStreamError(BitIStream &inputStream)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'HPack.Decoder.handleStreamError' has no cute function yet. Qt's "
        "'void HPack::Decoder::handleStreamError(BitIStream &inputStream)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def processDecodedField(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Decoder::processDecodedField(BitPattern fieldType,
    const QByteArray &name, const QByteArray &value)': the compiler refuses
    its ritual as it would be written here: unknown type name 'BitPattern';
    did you mean 'HPack::BitPattern'?.
    """
    raise NotImplementedError(
        "'HPack.Decoder.processDecodedField' has no cute function yet. Qt's "
        "'bool HPack::Decoder::processDecodedField(BitPattern fieldType, "
        "const QByteArray &name, const QByteArray &value)': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'BitPattern'; did you mean 'HPack::BitPattern'?.")
