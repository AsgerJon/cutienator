"""
QTextDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qtextcodec.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringConverterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QString
  from . import QTextCodec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QString = WAIT['QString']
  QTextCodec = WAIT['QTextCodec']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextDecoder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextDecoder: a plain Python object standing in front
  of one C++ QTextDecoder.

  What exists
  -----------

  Every function of Qt's QTextDecoder that has a ritual and that Python can
  call so far, 3 names in all: 'toUnicode', 'hasFailure', 'needsMoreData'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextDecoder::~QTextDecoder()': the destructor: Python never
    removes a C++ QTextDecoder.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QTextDecoder is created at the first use, not by
    'QTextDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextDecoder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextDecoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasFailure(self) -> bool:
    """
    Calls Qt's 'bool QTextDecoder::hasFailure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#hasFailure
    """
    #  bool QTextDecoder::hasFailure() const
    return self.uglySide.call('ritual_ZNK12QTextDecoder10hasFailureEv')

  def needsMoreData(self) -> bool:
    """
    Calls Qt's 'bool QTextDecoder::needsMoreData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#needsMoreData
    """
    #  bool QTextDecoder::needsMoreData() const
    return self.uglySide.call('ritual_ZNK12QTextDecoder13needsMoreDataEv')

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

  @overload(QTextCodec)
  @overload(NoneType)
  def __init__(self, codec: Optional[QTextCodec]) -> None:
    """
    Notes what was given, for Qt's 'QTextDecoder::QTextDecoder(const
    QTextCodec *codec)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#QTextDecoder

    Parameters
    ----------

    codec : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextDecoder::QTextDecoder(const QTextCodec *codec)
    self._noteCreation(QTextDecoder, lambda: Rituals.call(
        'ritual_ZN12QTextDecoderC1EPK10QTextCodec', self._addressOf(codec),
    ))

  @overload(QTextCodec, QStringConverterBase.Flags)
  @overload(NoneType, QStringConverterBase.Flags)
  def __init__(
      self,
      codec: Optional[QTextCodec],
      flags: QStringConverterBase.Flags,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextDecoder::QTextDecoder(const
    QTextCodec *codec, QTextCodec::ConversionFlags flags)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#QTextDecoder

    Parameters
    ----------

    codec : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QStringConverterBase.Flags
      Passed on as its number.
    """
    #  QTextDecoder::QTextDecoder(const QTextCodec *codec,
    #      QTextCodec::ConversionFlags flags)
    self._noteCreation(QTextDecoder, lambda: Rituals.call(
        'ritual_ZN12QTextDecoderC1EPK10QTextCodec6QFlagsIN20QStringConverte'
        'rBase4FlagEE',
        self._addressOf(codec), flags.value,
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

  @overload(str, int)
  @overload(NoneType, int)
  def toUnicode(self, chars: Optional[str], len: int) -> str:
    """
    Calls Qt's 'QString QTextDecoder::toUnicode(const char *chars, int len)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#toUnicode

    Parameters
    ----------

    chars : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDecoder::toUnicode(const char *chars, int len)
    return self.uglySide.call(
        'ritual_ZN12QTextDecoder9toUnicodeEPKci', self._bytesOf(chars), len,
    )

  @overload(QByteArray)
  def toUnicode(self, ba: QByteArray) -> str:
    """
    Calls Qt's 'QString QTextDecoder::toUnicode(const QByteArray &ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#toUnicode

    Parameters
    ----------

    ba : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDecoder::toUnicode(const QByteArray &ba)
    return self.uglySide.call(
        'ritual_ZN12QTextDecoder9toUnicodeERK10QByteArray',
        self._valueOf(ba),
    )

  @overload(QString, str, int)
  @overload(QString, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def toUnicode(
      self,
      target: Optional[QString],
      chars: Optional[str],
      len: int,
  ) -> None:
    """
    Calls Qt's 'void QTextDecoder::toUnicode(QString *target, const char
    *chars, int len)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdecoder.html#toUnicode

    Parameters
    ----------

    target : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    chars : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QTextDecoder::toUnicode(QString *target, const char *chars, int
    #      len)
    self.uglySide.call(
        'ritual_ZN12QTextDecoder9toUnicodeEP7QStringPKci',
        self._addressOf(target), self._bytesOf(chars), len,
    )
