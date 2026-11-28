"""
HPack::HuffmanDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/huffman_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means HPack::HuffmanDecoder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import HPack

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class HuffmanDecoder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::HuffmanDecoder: a plain Python object standing
  in front of one C++ HPack::HuffmanDecoder.

  C++ hands a HPack::HuffmanDecoder around as a copy, so every C++
  HPack::HuffmanDecoder behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's HPack::HuffmanDecoder that has a ritual and that
  Python can call so far, 3 names in all: 'addTable', 'tableEntry',
  'setTableEntry'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'HPack::HuffmanDecoder::~HuffmanDecoder()': the destructor: Python
    removes its C++ HPack::HuffmanDecoder by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ HPack::HuffmanDecoder is created at the first use, not by
    'HPack::HuffmanDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a HPack::HuffmanDecoder back gives a copy the ritual
    made for Python, in a new cute HPack::HuffmanDecoder.
  - Each name of Qt's HPack::HuffmanDecoder that has no cute function yet,
    '__init__', 'decodeStream', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside HPack::HuffmanDecoder, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BitConstants(CuteNum, scoped=True):
    """
    The enum 'HPack::HuffmanDecoder::BitConstants' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    rootPrefix = Kee[int](9)
    childPrefix = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HPack::HuffmanDecoder'

  #  Qt's '~HPack::HuffmanDecoder()'. Naming it makes this a value class:
  #  Python owns every C++ HPack::HuffmanDecoder behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5HPack14HuffmanDecoderD1Ev'

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

  @overload(WAIT['HPack.PrefixTable'], int, WAIT['HPack.PrefixTableEntry'])
  def setTableEntry(
      self,
      table: HPack.PrefixTable,
      index: int,
      entry: HPack.PrefixTableEntry,
  ) -> None:
    """
    Calls Qt's 'void HPack::HuffmanDecoder::setTableEntry(PrefixTable table,
    quint32 index, PrefixTableEntry entry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-huffmandecoder.html#setTableEntry

    Parameters
    ----------

    table : HPack.PrefixTable
      Passed on as a value: Qt reads the C++ HPack::PrefixTable, which stays
      Python's own.

    index : int
      Passed on as it is.

    entry : HPack.PrefixTableEntry
      Passed on as a value: Qt reads the C++ HPack::PrefixTableEntry, which
      stays Python's own.
    """
    #  void HPack::HuffmanDecoder::setTableEntry(PrefixTable table, quint32
    #      index, PrefixTableEntry entry)
    self.uglySide.call(
        'ritual_ZN5HPack14HuffmanDecoder13setTableEntryENS_11PrefixTableEjN'
        'S_16PrefixTableEntryE',
        self._valueOf(table), index, self._valueOf(entry),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'HPack::HuffmanDecoder::HuffmanDecoder()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'staticHuffmanCodeTable'.
    """
    raise NotImplementedError(
        "'HPack.HuffmanDecoder.__init__' has no cute function yet. Qt's "
        "'HPack::HuffmanDecoder::HuffmanDecoder()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'staticHuffmanCodeTable'.")

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
  def addTable(self, prefixLength: int, indexLength: int) -> int:
    """
    Calls Qt's 'quint32 HPack::HuffmanDecoder::addTable(quint32 prefixLength,
    quint32 indexLength)'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-huffmandecoder.html#addTable

    Parameters
    ----------

    prefixLength : int
      Passed on as it is.

    indexLength : int
      Passed on as it is.
    """
    #  quint32 HPack::HuffmanDecoder::addTable(quint32 prefixLength, quint32
    #      indexLength)
    return self.uglySide.call(
        'ritual_ZN5HPack14HuffmanDecoder8addTableEjj',
        prefixLength, indexLength,
    )

  @overload(WAIT['HPack.PrefixTable'], int)
  def tableEntry(
      self,
      table: HPack.PrefixTable,
      index: int,
  ) -> HPack.PrefixTableEntry:
    """
    Calls Qt's 'PrefixTableEntry
    HPack::HuffmanDecoder::tableEntry(PrefixTable table, quint32 index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-huffmandecoder.html#tableEntry

    Parameters
    ----------

    table : HPack.PrefixTable
      Passed on as a value: Qt reads the C++ HPack::PrefixTable, which stays
      Python's own.

    index : int
      Passed on as it is.

    Returns
    -------

    HPack.PrefixTableEntry
      A new cute HPack::PrefixTableEntry around the copy Qt gave back. Python
      owns it.
    """
    #  PrefixTableEntry HPack::HuffmanDecoder::tableEntry(PrefixTable table,
    #      quint32 index)
    address = self.uglySide.call(
        'ritual_ZN5HPack14HuffmanDecoder10tableEntryENS_11PrefixTableEj',
        self._valueOf(table), index,
    )
    return HPack.PrefixTableEntry._cuteOwning(address)

  @staticmethod
  def decodeStream(*__, **_) -> Never:
    """
    Qt's 'bool HPack::HuffmanDecoder::decodeStream(BitIStream &inputStream,
    QByteArray &outputBuffer)': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'padding_is_valid'.
    """
    raise NotImplementedError(
        "'HPack.HuffmanDecoder.decodeStream' has no cute function yet. Qt's "
        "'bool HPack::HuffmanDecoder::decodeStream(BitIStream &inputStream, "
        "QByteArray &outputBuffer)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'padding_is_valid'.")
