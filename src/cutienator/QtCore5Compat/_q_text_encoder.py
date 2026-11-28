"""
QTextEncoder binding of the Qt C++
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

  from ..QtCore import QByteArray, QChar
  from . import QTextCodec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QTextCodec = WAIT['QTextCodec']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextEncoder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextEncoder: a plain Python object standing in front
  of one C++ QTextEncoder.

  What exists
  -----------

  Every function of Qt's QTextEncoder that has a ritual and that Python can
  call so far, 2 names in all: 'fromUnicode', 'hasFailure'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextEncoder::~QTextEncoder()': the destructor: Python never
    removes a C++ QTextEncoder.
  - Qt's 'QByteArray QTextEncoder::fromUnicode(QStringView str)': takes in
    Python what 'QByteArray QTextEncoder::fromUnicode(const QString &str)'
    takes.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QTextEncoder is created at the first use, not by
    'QTextEncoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextEncoder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextEncoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasFailure(self) -> bool:
    """
    Calls Qt's 'bool QTextEncoder::hasFailure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextencoder.html#hasFailure
    """
    #  bool QTextEncoder::hasFailure() const
    return self.uglySide.call('ritual_ZNK12QTextEncoder10hasFailureEv')

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
    Notes what was given, for Qt's 'QTextEncoder::QTextEncoder(const
    QTextCodec *codec)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextencoder.html#QTextEncoder

    Parameters
    ----------

    codec : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextEncoder::QTextEncoder(const QTextCodec *codec)
    self._noteCreation(QTextEncoder, lambda: Rituals.call(
        'ritual_ZN12QTextEncoderC1EPK10QTextCodec', self._addressOf(codec),
    ))

  @overload(QTextCodec, QStringConverterBase.Flags)
  @overload(NoneType, QStringConverterBase.Flags)
  def __init__(
      self,
      codec: Optional[QTextCodec],
      flags: QStringConverterBase.Flags,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextEncoder::QTextEncoder(const
    QTextCodec *codec, QTextCodec::ConversionFlags flags)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextencoder.html#QTextEncoder

    Parameters
    ----------

    codec : Optional[QTextCodec]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : QStringConverterBase.Flags
      Passed on as its number.
    """
    #  QTextEncoder::QTextEncoder(const QTextCodec *codec,
    #      QTextCodec::ConversionFlags flags)
    self._noteCreation(QTextEncoder, lambda: Rituals.call(
        'ritual_ZN12QTextEncoderC1EPK10QTextCodec6QFlagsIN20QStringConverte'
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

  @overload(str)
  def fromUnicode(self, str: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextEncoder::fromUnicode(const QString &str)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextencoder.html#fromUnicode

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextEncoder::fromUnicode(const QString &str)
    address = self.uglySide.call(
        'ritual_ZN12QTextEncoder11fromUnicodeERK7QString', str,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QChar, int)
  @overload(NoneType, int)
  def fromUnicode(self, uc: Optional[QChar], len: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextEncoder::fromUnicode(const QChar *uc, int
    len)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextencoder.html#fromUnicode

    Parameters
    ----------

    uc : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    len : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextEncoder::fromUnicode(const QChar *uc, int len)
    address = self.uglySide.call(
        'ritual_ZN12QTextEncoder11fromUnicodeEPK5QChari',
        self._addressOf(uc), len,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)
