"""
QJpUnicodeConv binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qjpunicode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QJpUnicodeConv to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QJpUnicodeConv(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJpUnicodeConv: a plain Python object standing in
  front of one C++ QJpUnicodeConv.

  C++ hands a QJpUnicodeConv around as a copy, so every C++ QJpUnicodeConv
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJpUnicodeConv that has a ritual and that Python can
  call so far, 19 names in all: 'newConverter', 'asciiToUnicode',
  'jisx0201ToUnicode', 'jisx0201LatinToUnicode', 'jisx0201KanaToUnicode',
  'jisx0208ToUnicode', 'jisx0212ToUnicode', 'unicodeToAscii',
  'unicodeToJisx0201', 'unicodeToJisx0201Latin', 'unicodeToJisx0201Kana',
  'unicodeToJisx0208', 'unicodeToJisx0212', 'sjisToUnicode', 'unicodeToSjis',
  'sjisibmvdcToUnicode', 'unicodeToSjisibmvdc', 'cp932ToUnicode',
  'unicodeToCp932'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJpUnicodeConv::~QJpUnicodeConv()': the destructor: Python removes
    its C++ QJpUnicodeConv by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QJpUnicodeConv is created at the first use, not by
    'QJpUnicodeConv(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJpUnicodeConv back gives a copy the ritual made for
    Python, in a new cute QJpUnicodeConv.
  """

  #  The enums Qt writes inside QJpUnicodeConv, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Rules(CuteNum):
    """
    The enum 'QJpUnicodeConv::Rules' of Qt, with the 11 names Qt gives in it.
    """

    Default = Kee[int](0)
    Unicode = Kee[int](1)
    Unicode_JISX0201 = Kee[int](1)
    Unicode_ASCII = Kee[int](2)
    JISX0221_JISX0201 = Kee[int](3)
    JISX0221_ASCII = Kee[int](4)
    Sun_JDK117 = Kee[int](5)
    Microsoft_CP932 = Kee[int](6)
    NEC_VDC = Kee[int](256)
    UDC = Kee[int](512)
    IBM_VDC = Kee[int](1024)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def newConverter(rule: int) -> Optional[QJpUnicodeConv]:
    """
    Calls Qt's 'QJpUnicodeConv *QJpUnicodeConv::newConverter(int rule)'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#newConverter

    Parameters
    ----------

    rule : int
      Passed on as it is.

    Returns
    -------

    Optional[QJpUnicodeConv]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QJpUnicodeConv *QJpUnicodeConv::newConverter(int rule)
    address = Rituals.call('ritual_ZN14QJpUnicodeConv12newConverterEi', rule)
    return QJpUnicodeConv._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJpUnicodeConv'

  #  A C++ QJpUnicodeConv Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QJpUnicodeConv'

  #  The functions Qt calls itself that QJpUnicodeConv is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'asciiToUnicode': (
          ('_ZNK14QJpUnicodeConv14asciiToUnicodeEjj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'jisx0201LatinToUnicode': (
          ('_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEjj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'jisx0208ToUnicode': (
          ('_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEjj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'jisx0212ToUnicode': (
          ('_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEjj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'unicodeToAscii': (
          ('_ZNK14QJpUnicodeConv14unicodeToAsciiEjj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'unicodeToJisx0201Latin': (
          ('_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEjj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'unicodeToJisx0208': (
          ('_ZNK14QJpUnicodeConv17unicodeToJisx0208Ejj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'unicodeToJisx0212': (
          ('_ZNK14QJpUnicodeConv17unicodeToJisx0212Ejj',
           ('unsigned int', 'number', ''),
           (
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QJpUnicodeConv()'. Naming it makes this a value class: Python
  #  owns every C++ QJpUnicodeConv behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QJpUnicodeConvD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def asciiToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::asciiToUnicode(uint h, uint l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#asciiToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::asciiToUnicode(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv14asciiToUnicodeEjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv14asciiToUnicodeEjj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def asciiToUnicode(self, ascii: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::asciiToUnicode(uint ascii) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#asciiToUnicode

    Parameters
    ----------

    ascii : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::asciiToUnicode(uint ascii) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv14asciiToUnicodeEj', ascii,
    )

  @overload(int, int)
  def jisx0201ToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0201ToUnicode(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0201ToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0201ToUnicode(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17jisx0201ToUnicodeEjj', h, l,
    )

  @overload(int)
  def jisx0201ToUnicode(self, jis: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0201ToUnicode(uint jis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0201ToUnicode

    Parameters
    ----------

    jis : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0201ToUnicode(uint jis) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17jisx0201ToUnicodeEj', jis,
    )

  @overload(int, int)
  def jisx0201LatinToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0201LatinToUnicode(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0201LatinToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0201LatinToUnicode(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEjj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def jisx0201LatinToUnicode(self, jis: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0201LatinToUnicode(uint jis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0201LatinToUnicode

    Parameters
    ----------

    jis : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0201LatinToUnicode(uint jis) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv22jisx0201LatinToUnicodeEj', jis,
    )

  @overload(int, int)
  def jisx0201KanaToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0201KanaToUnicode(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0201KanaToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0201KanaToUnicode(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv21jisx0201KanaToUnicodeEjj', h, l,
    )

  @overload(int)
  def jisx0201KanaToUnicode(self, jis: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0201KanaToUnicode(uint jis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0201KanaToUnicode

    Parameters
    ----------

    jis : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0201KanaToUnicode(uint jis) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv21jisx0201KanaToUnicodeEj', jis,
    )

  @overload(int, int)
  def jisx0208ToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0208ToUnicode(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0208ToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0208ToUnicode(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEjj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def jisx0208ToUnicode(self, jis: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0208ToUnicode(uint jis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0208ToUnicode

    Parameters
    ----------

    jis : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0208ToUnicode(uint jis) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17jisx0208ToUnicodeEj', jis,
    )

  @overload(int, int)
  def jisx0212ToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0212ToUnicode(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0212ToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0212ToUnicode(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEjj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def jisx0212ToUnicode(self, jis: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::jisx0212ToUnicode(uint jis) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#jisx0212ToUnicode

    Parameters
    ----------

    jis : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::jisx0212ToUnicode(uint jis) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17jisx0212ToUnicodeEj', jis,
    )

  @overload(int, int)
  def unicodeToAscii(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToAscii(uint h, uint l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToAscii

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToAscii(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv14unicodeToAsciiEjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv14unicodeToAsciiEjj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def unicodeToAscii(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToAscii(uint unicode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToAscii

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToAscii(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv14unicodeToAsciiEj', unicode,
    )

  @overload(int, int)
  def unicodeToJisx0201(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0201(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0201

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0201(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17unicodeToJisx0201Ejj', h, l,
    )

  @overload(int)
  def unicodeToJisx0201(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0201(uint unicode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0201

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0201(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17unicodeToJisx0201Ej', unicode,
    )

  @overload(int, int)
  def unicodeToJisx0201Latin(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0201Latin(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0201Latin

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0201Latin(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEjj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def unicodeToJisx0201Latin(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0201Latin(uint unicode)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0201Latin

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0201Latin(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv22unicodeToJisx0201LatinEj', unicode,
    )

  @overload(int, int)
  def unicodeToJisx0201Kana(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0201Kana(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0201Kana

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0201Kana(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv21unicodeToJisx0201KanaEjj', h, l,
    )

  @overload(int)
  def unicodeToJisx0201Kana(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0201Kana(uint unicode)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0201Kana

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0201Kana(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv21unicodeToJisx0201KanaEj', unicode,
    )

  @overload(int, int)
  def unicodeToJisx0208(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0208(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0208

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0208(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv17unicodeToJisx0208Ejj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv17unicodeToJisx0208Ejj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def unicodeToJisx0208(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0208(uint unicode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0208

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0208(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17unicodeToJisx0208Ej', unicode,
    )

  @overload(int, int)
  def unicodeToJisx0212(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0212(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0212

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0212(uint h, uint l) const
    ritual = 'ritual_ZNK14QJpUnicodeConv17unicodeToJisx0212Ejj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QJpUnicodeConv17unicodeToJisx0212Ejj'
    return self.uglySide.call(ritual, h, l)

  @overload(int)
  def unicodeToJisx0212(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToJisx0212(uint unicode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToJisx0212

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToJisx0212(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv17unicodeToJisx0212Ej', unicode,
    )

  @overload(int, int)
  def sjisToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::sjisToUnicode(uint h, uint l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#sjisToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::sjisToUnicode(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv13sjisToUnicodeEjj', h, l,
    )

  @overload(int)
  def sjisToUnicode(self, sjis: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::sjisToUnicode(uint sjis) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#sjisToUnicode

    Parameters
    ----------

    sjis : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::sjisToUnicode(uint sjis) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv13sjisToUnicodeEj', sjis,
    )

  @overload(int, int)
  def unicodeToSjis(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToSjis(uint h, uint l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToSjis

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToSjis(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv13unicodeToSjisEjj', h, l,
    )

  @overload(int)
  def unicodeToSjis(self, unicode: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToSjis(uint unicode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToSjis

    Parameters
    ----------

    unicode : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToSjis(uint unicode) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv13unicodeToSjisEj', unicode,
    )

  @overload(int, int)
  def sjisibmvdcToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::sjisibmvdcToUnicode(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#sjisibmvdcToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::sjisibmvdcToUnicode(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv19sjisibmvdcToUnicodeEjj', h, l,
    )

  @overload(int, int)
  def unicodeToSjisibmvdc(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToSjisibmvdc(uint h, uint l)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToSjisibmvdc

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToSjisibmvdc(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv19unicodeToSjisibmvdcEjj', h, l,
    )

  @overload(int, int)
  def cp932ToUnicode(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::cp932ToUnicode(uint h, uint l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#cp932ToUnicode

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::cp932ToUnicode(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv14cp932ToUnicodeEjj', h, l,
    )

  @overload(int, int)
  def unicodeToCp932(self, h: int, l: int) -> int:
    """
    Calls Qt's 'uint QJpUnicodeConv::unicodeToCp932(uint h, uint l) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#unicodeToCp932

    Parameters
    ----------

    h : int
      Passed on as it is.

    l : int
      Passed on as it is.
    """
    #  uint QJpUnicodeConv::unicodeToCp932(uint h, uint l) const
    return self.uglySide.call(
        'ritual_ZNK14QJpUnicodeConv14unicodeToCp932Ejj', h, l,
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

  @overload(int)
  def __init__(self, r: int) -> None:
    """
    Notes what was given, for Qt's 'QJpUnicodeConv::QJpUnicodeConv(int r)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qjpunicodeconv.html#QJpUnicodeConv

    Parameters
    ----------

    r : int
      Passed on as it is.
    """
    #  QJpUnicodeConv::QJpUnicodeConv(int r)
    self._noteCreation(QJpUnicodeConv, lambda: Rituals.call(
        'ritual_ZN14QJpUnicodeConvC1Ei', r,
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
