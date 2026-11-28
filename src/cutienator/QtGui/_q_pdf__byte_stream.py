"""
QPdf::ByteStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPdf::ByteStream to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ByteStream(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPdf::ByteStream: a plain Python object standing in
  front of one C++ QPdf::ByteStream.

  C++ hands a QPdf::ByteStream around as a copy, so every C++
  QPdf::ByteStream behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPdf::ByteStream that has a ritual and that Python
  can call so far, 5 names in all: 'stream', 'clear', 'maxMemorySize',
  'chunkSize', 'prepareBuffer'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdf::ByteStream::~ByteStream()': the destructor: Python removes
    its C++ QPdf::ByteStream by it, and has no other use for it.
  - Qt's 'ByteStream &QPdf::ByteStream::operator<<(char chr)': takes a single
    letter as C has it.
  - Qt's 'ByteStream &QPdf::ByteStream::operator<<(const char *str)': gives a
    type Python has no way to take yet.
  - Qt's 'ByteStream &QPdf::ByteStream::operator<<(const QByteArray &str)':
    gives a type Python has no way to take yet.
  - Qt's 'ByteStream &QPdf::ByteStream::operator<<(const ByteStream &src)':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 17 functions Qt declares: 3 leans on 'qt_int_to_string(int,
  char*)', which Qt's source does not mark for use from outside Qt and has no
  code for that could be taken; 2 leans on 'qt_real_to_string(double,
  char*)', which Qt's source does not mark for use from outside Qt and has no
  code for that could be taken.

  What to expect
  --------------

  - The C++ QPdf::ByteStream is created at the first use, not by
    'QPdf::ByteStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPdf::ByteStream back gives a copy the ritual made
    for Python, in a new cute QPdf::ByteStream.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def maxMemorySize() -> int:
    """
    Calls Qt's 'int QPdf::ByteStream::maxMemorySize()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#maxMemorySize
    """
    #  int QPdf::ByteStream::maxMemorySize()
    return Rituals.call('ritual_ZN4QPdf10ByteStream13maxMemorySizeEv')

  @staticmethod
  def chunkSize() -> int:
    """
    Calls Qt's 'int QPdf::ByteStream::chunkSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#chunkSize
    """
    #  int QPdf::ByteStream::chunkSize()
    return Rituals.call('ritual_ZN4QPdf10ByteStream9chunkSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdf::ByteStream'

  #  Qt's '~QPdf::ByteStream()'. Naming it makes this a value class: Python
  #  owns every C++ QPdf::ByteStream behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN4QPdf10ByteStreamD1Ev'

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

  @overload()
  @overload(bool)
  def __init__(self, fileBacking: bool = False) -> None:
    """
    Notes what was given, for Qt's 'QPdf::ByteStream::ByteStream(bool
    fileBacking)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#ByteStream

    Parameters
    ----------

    fileBacking : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QPdf::ByteStream::ByteStream(bool fileBacking)
    self._noteCreation(ByteStream, lambda: Rituals.call(
        'ritual_ZN4QPdf10ByteStreamC1Eb', fileBacking,
    ))

  @overload(QByteArray)
  @overload(NoneType)
  @overload(QByteArray, bool)
  @overload(NoneType, bool)
  def __init__(
      self,
      ba: Optional[QByteArray],
      fileBacking: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPdf::ByteStream::ByteStream(QByteArray
    *ba, bool fileBacking)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#ByteStream

    Parameters
    ----------

    ba : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileBacking : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QPdf::ByteStream::ByteStream(QByteArray *ba, bool fileBacking)
    self._noteCreation(ByteStream, lambda: Rituals.call(
        'ritual_ZN4QPdf10ByteStreamC1EP10QByteArrayb',
        self._addressOf(ba), fileBacking,
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

  def stream(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QPdf::ByteStream::stream()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#stream

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QPdf::ByteStream::stream()
    address = self.uglySide.call('ritual_ZN4QPdf10ByteStream6streamEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QPdf::ByteStream::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#clear
    """
    #  void QPdf::ByteStream::clear()
    self.uglySide.call('ritual_ZN4QPdf10ByteStream5clearEv')

  def prepareBuffer(self) -> None:
    """
    Calls Qt's 'void QPdf::ByteStream::prepareBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdf-bytestream.html#prepareBuffer
    """
    #  void QPdf::ByteStream::prepareBuffer()
    self.uglySide.call('ritual_ZN4QPdf10ByteStream13prepareBufferEv')
