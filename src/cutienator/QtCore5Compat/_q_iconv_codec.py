"""
QIconvCodec binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QIconvCodec to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QTextCodec

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIconvCodec(QTextCodec):
  """
  The cute side of Qt's QIconvCodec: a plain Python object standing in front
  of one C++ QIconvCodec.

  It is built on the cute 'QTextCodec', as Qt's QIconvCodec is built on Qt's
  QTextCodec, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIconvCodec that has a ritual and that Python can
  call so far, 3 names in all: 'name', 'mibEnum', 'init'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIconvCodec::~QIconvCodec()': the destructor: Python never removes
    a C++ QIconvCodec.
  - Qt's 'QString QIconvCodec::convertToUnicode(const char *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'QByteArray QIconvCodec::convertFromUnicode(const QChar *a0, int a1,
    ConverterState *a2) const': names 'QTextCodec::ConverterState', which has
    no cute class yet.
  - Qt's 'iconv_t QIconvCodec::createIconv_t(const char *to, const char
    *from) const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QIconvCodec is created at the first use, not by
    'QIconvCodec(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIconvCodec.
  - Each name of Qt's QIconvCodec that has no cute function yet,
    'createIconv_t', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QIconvCodec, each a class in here as in
  #  C++.

  class IconvState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QIconvCodec::IconvState: a plain Python object
    standing in front of one C++ QIconvCodec::IconvState.

    What exists
    -----------

    Every function of Qt's QIconvCodec::IconvState that has a ritual and that
    Python can call so far, 1 name in all: 'saveChars'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QIconvCodec::IconvState::IconvState(iconv_t x)': names 'void',
      which has no cute class yet.
    - Qt's 'QIconvCodec::IconvState::~IconvState()': the destructor: Python
      never removes a C++ QIconvCodec::IconvState.

    What to expect
    --------------

    - The C++ QIconvCodec::IconvState is created at the first use, not by
      'QIconvCodec::IconvState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QIconvCodec::IconvState.
    - Each name of Qt's QIconvCodec::IconvState that has no cute function
      yet, '__init__', holds a function that raises 'NotImplementedError',
      and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QIconvCodec::IconvState'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QIconvCodec::IconvState::IconvState(iconv_t x)': names 'void',
      which has no cute class yet.
      """
      raise NotImplementedError(
          "'QIconvCodec.IconvState.__init__' has no cute function yet. Qt's "
          "'QIconvCodec::IconvState::IconvState(iconv_t x)': names 'void', "
          "which has no cute class yet.")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str, int)
    @overload(NoneType, int)
    def saveChars(self, c: Optional[str], count: int) -> None:
      """
      Calls Qt's 'void QIconvCodec::IconvState::saveChars(const char *c, int
      count)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qiconvcodec-iconvstate.html#saveChars

      Parameters
      ----------

      c : Optional[str]
        Passed on as the bytes of the text. None is passed on as no text.

      count : int
        Passed on as it is.
      """
      #  void QIconvCodec::IconvState::saveChars(const char *c, int count)
      self.uglySide.call(
          'ritual_ZN11QIconvCodec10IconvState9saveCharsEPKci',
          self._bytesOf(c), count,
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconvCodec'

  #  A C++ QIconvCodec Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIconvCodec'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QIconvCodec::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconvcodec.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QIconvCodec::name() const
    ritual = 'ritual_ZNK11QIconvCodec4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QIconvCodec4nameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def mibEnum(self) -> int:
    """
    Calls Qt's 'int QIconvCodec::mibEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconvcodec.html#mibEnum
    """
    #  int QIconvCodec::mibEnum() const
    ritual = 'ritual_ZNK11QIconvCodec7mibEnumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QIconvCodec7mibEnumEv'
    return self.uglySide.call(ritual)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QIconvCodec::QIconvCodec()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qiconvcodec.html#QIconvCodec
    """
    #  QIconvCodec::QIconvCodec()
    self._noteCreation(QIconvCodec, lambda: Rituals.call(
        'ritual_ZN11QIconvCodecC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QIconvCodec::init() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconvcodec.html#init
    """
    #  void QIconvCodec::init() const
    self.uglySide.call('ritual_ZNK11QIconvCodec4initEv')

  @staticmethod
  def createIconv_t(*__, **_) -> Never:
    """
    Qt's 'iconv_t QIconvCodec::createIconv_t(const char *to, const char
    *from) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QIconvCodec.createIconv_t' has no cute function yet. Qt's "
        "'iconv_t QIconvCodec::createIconv_t(const char *to, const char "
        "*from) const': gives a type Python has no way to take yet.")
