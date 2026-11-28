"""
HPack::Encoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/hpack_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means HPack::Encoder to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Encoder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::Encoder: a plain Python object standing in
  front of one C++ HPack::Encoder.

  What exists
  -----------

  Every function of Qt's HPack::Encoder that has a ritual and that Python can
  call so far, 5 names in all: 'dynamicTableSize', 'dynamicTableCapacity',
  'maxDynamicTableCapacity', 'setMaxDynamicTableSize', 'setCompressStrings'.
  It can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  10 of the 16 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'HPack; 2 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ HPack::Encoder is created at the first use, not by
    'HPack::Encoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ HPack::Encoder.
  - Each name of Qt's HPack::Encoder that has no cute function yet,
    'encodeHeaderField', 'encodeIndexedField', 'encodeLiteralField',
    'encodeMethod', 'encodeRequest', 'encodeRequestPseudoHeaders',
    'encodeResponse', 'encodeResponsePseudoHeaders', 'encodeSizeUpdate',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HPack::Encoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dynamicTableSize(self) -> int:
    """
    Calls Qt's 'quint32 HPack::Encoder::dynamicTableSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-encoder.html#dynamicTableSize
    """
    #  quint32 HPack::Encoder::dynamicTableSize() const
    return self.uglySide.call('ritual_ZNK5HPack7Encoder16dynamicTableSizeEv')

  def dynamicTableCapacity(self) -> int:
    """
    Calls Qt's 'quint32 HPack::Encoder::dynamicTableCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-encoder.html#dynamicTableCapacity
    """
    #  quint32 HPack::Encoder::dynamicTableCapacity() const
    return self.uglySide.call(
        'ritual_ZNK5HPack7Encoder20dynamicTableCapacityEv',
    )

  def maxDynamicTableCapacity(self) -> int:
    """
    Calls Qt's 'quint32 HPack::Encoder::maxDynamicTableCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-encoder.html#maxDynamicTableCapacity
    """
    #  quint32 HPack::Encoder::maxDynamicTableCapacity() const
    return self.uglySide.call(
        'ritual_ZNK5HPack7Encoder23maxDynamicTableCapacityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxDynamicTableSize(self, size: int) -> None:
    """
    Calls Qt's 'void HPack::Encoder::setMaxDynamicTableSize(quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-encoder.html#setMaxDynamicTableSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void HPack::Encoder::setMaxDynamicTableSize(quint32 size)
    self.uglySide.call(
        'ritual_ZN5HPack7Encoder22setMaxDynamicTableSizeEj', size,
    )

  @overload(bool)
  def setCompressStrings(self, compress: bool) -> None:
    """
    Calls Qt's 'void HPack::Encoder::setCompressStrings(bool compress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-encoder.html#setCompressStrings

    Parameters
    ----------

    compress : bool
      Passed on as it is.
    """
    #  void HPack::Encoder::setCompressStrings(bool compress)
    self.uglySide.call(
        'ritual_ZN5HPack7Encoder18setCompressStringsEb', compress,
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

  @overload(int, bool)
  def __init__(self, maxTableSize: int, compressStrings: bool) -> None:
    """
    Notes what was given, for Qt's 'HPack::Encoder::Encoder(quint32
    maxTableSize, bool compressStrings)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/hpack-encoder.html#Encoder

    Parameters
    ----------

    maxTableSize : int
      Passed on as it is.

    compressStrings : bool
      Passed on as it is.
    """
    #  HPack::Encoder::Encoder(quint32 maxTableSize, bool compressStrings)
    self._noteCreation(Encoder, lambda: Rituals.call(
        'ritual_ZN5HPack7EncoderC1Ejb', maxTableSize, compressStrings,
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
  def encodeHeaderField(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeHeaderField(BitOStream &outputStream,
    const HeaderField &field)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'LiteralIncrementalIndexing'.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeHeaderField' has no cute function yet. Qt's "
        "'bool HPack::Encoder::encodeHeaderField(BitOStream &outputStream, "
        "const HeaderField &field)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'LiteralIncrementalIndexing'.")

  @staticmethod
  def encodeIndexedField(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeIndexedField(BitOStream &outputStream,
    quint32 index) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'Indexed'; did you mean 'QPixelFormat::Indexed'?.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeIndexedField' has no cute function yet. Qt's "
        "'bool HPack::Encoder::encodeIndexedField(BitOStream &outputStream, "
        "quint32 index) const': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'Indexed'; did you mean "
        "'QPixelFormat::Indexed'?.")

  @staticmethod
  def encodeLiteralField(*__, **_) -> Never:
    """
    - Qt's 'bool HPack::Encoder::encodeLiteralField(BitOStream &outputStream,
      BitPattern fieldType, quint32 nameIndex, const QByteArray &value, bool
      withCompression)': the compiler refuses its ritual as it would be
      written here: unknown type name 'BitPattern'; did you mean
      'HPack::BitPattern'?.
    - Qt's 'bool HPack::Encoder::encodeLiteralField(BitOStream &outputStream,
      BitPattern fieldType, const QByteArray &name, const QByteArray &value,
      bool withCompression)': the compiler refuses its ritual as it would be
      written here: unknown type name 'BitPattern'; did you mean
      'HPack::BitPattern'?.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeLiteralField' has no cute function yet. Qt's "
        "'bool HPack::Encoder::encodeLiteralField(BitOStream &outputStream, "
        "BitPattern fieldType, quint32 nameIndex, const QByteArray &value, "
        "bool withCompression)': the compiler refuses its ritual as it "
        "would be written here: unknown type name 'BitPattern'; did you "
        "mean 'HPack::BitPattern'?. Qt's 'bool "
        "HPack::Encoder::encodeLiteralField(BitOStream &outputStream, "
        "BitPattern fieldType, const QByteArray &name, const QByteArray "
        "&value, bool withCompression)': the compiler refuses its ritual as "
        "it would be written here: unknown type name 'BitPattern'; did you "
        "mean 'HPack::BitPattern'?.")

  @staticmethod
  def encodeMethod(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeMethod(BitOStream &outputStream, const
    HeaderField &field)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'LiteralIncrementalIndexing'.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeMethod' has no cute function yet. Qt's 'bool "
        "HPack::Encoder::encodeMethod(BitOStream &outputStream, const "
        "HeaderField &field)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'LiteralIncrementalIndexing'.")

  @staticmethod
  def encodeRequest(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeRequest(class BitOStream &outputStream,
    const HttpHeader &header)': leans on
    'HPack::Encoder::encodeMethod(HPack::BitOStream&, HPack::HeaderField
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeRequest' has no cute function yet. Qt's 'bool "
        "HPack::Encoder::encodeRequest(class BitOStream &outputStream, "
        "const HttpHeader &header)': leans on "
        "'HPack::Encoder::encodeMethod(HPack::BitOStream&, "
        "HPack::HeaderField const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def encodeRequestPseudoHeaders(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeRequestPseudoHeaders(BitOStream
    &outputStream, const HttpHeader &header)': leans on
    'HPack::Encoder::encodeMethod(HPack::BitOStream&, HPack::HeaderField
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeRequestPseudoHeaders' has no cute function "
        "yet. Qt's 'bool "
        "HPack::Encoder::encodeRequestPseudoHeaders(BitOStream "
        "&outputStream, const HttpHeader &header)': leans on "
        "'HPack::Encoder::encodeMethod(HPack::BitOStream&, "
        "HPack::HeaderField const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def encodeResponse(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeResponse(BitOStream &outputStream, const
    HttpHeader &header)': leans on
    'HPack::Encoder::encodeHeaderField(HPack::BitOStream&, HPack::HeaderField
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeResponse' has no cute function yet. Qt's "
        "'bool HPack::Encoder::encodeResponse(BitOStream &outputStream, "
        "const HttpHeader &header)': leans on "
        "'HPack::Encoder::encodeHeaderField(HPack::BitOStream&, "
        "HPack::HeaderField const&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def encodeResponsePseudoHeaders(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeResponsePseudoHeaders(BitOStream
    &outputStream, const HttpHeader &header)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'is_request_pseudo_header'.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeResponsePseudoHeaders' has no cute function "
        "yet. Qt's 'bool "
        "HPack::Encoder::encodeResponsePseudoHeaders(BitOStream "
        "&outputStream, const HttpHeader &header)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'is_request_pseudo_header'.")

  @staticmethod
  def encodeSizeUpdate(*__, **_) -> Never:
    """
    Qt's 'bool HPack::Encoder::encodeSizeUpdate(BitOStream &outputStream,
    quint32 newSize)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'SizeUpdate'.
    """
    raise NotImplementedError(
        "'HPack.Encoder.encodeSizeUpdate' has no cute function yet. Qt's "
        "'bool HPack::Encoder::encodeSizeUpdate(BitOStream &outputStream, "
        "quint32 newSize)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'SizeUpdate'.")
