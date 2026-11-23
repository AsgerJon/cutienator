"""
QStringDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstringconverter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QStringConverter, QStringConverterBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArrayView, QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStringDecoder(QStringConverter):
  """
  The cute side of Qt's QStringDecoder: a plain Python object standing in
  front of one C++ QStringDecoder.

  It is built on the cute 'QStringConverter', as Qt's QStringDecoder is built
  on Qt's QStringConverter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStringDecoder that has a ritual and that Python can
  call so far, 5 names in all: 'requiredSpace', 'appendToBuffer',
  'invalidateAndReturnNull', 'decodeAsStringImpl', 'decodeAsString'. It can
  be made from Python, in 3 ways; see '__init__'.

  What has no ritual
  ------------------

  10 of the 18 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 2 a template.

  What to expect
  --------------

  - The C++ QStringDecoder is created at the first use, not by
    'QStringDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStringDecoder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringDecoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def requiredSpace(self, inputLength: int) -> int:
    """
    Calls Qt's 'qsizetype QStringDecoder::requiredSpace(qsizetype
    inputLength) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringdecoder.html#requiredSpace

    Parameters
    ----------

    inputLength : int
      Passed on as it is.
    """
    #  qsizetype QStringDecoder::requiredSpace(qsizetype inputLength) const
    return self.uglySide.call(
        'ritual_ZNK14QStringDecoder13requiredSpaceEx', inputLength,
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

  @overload(QStringConverter.Encoding)
  @overload(QStringConverter.Encoding, QStringConverterBase.Flags)
  def __init__(
      self,
      encoding: QStringConverter.Encoding,
      flags: QStringConverterBase.Flags = QStringConverterBase.Flags.Default,
  ) -> None:
    """
    Notes what was given, for Qt's 'QStringDecoder::QStringDecoder(Encoding
    encoding, Flags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringdecoder.html#QStringDecoder

    Parameters
    ----------

    encoding : QStringConverter.Encoding
      Passed on as its number.

    flags : QStringConverterBase.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QStringConverterBase.Flags.Default.
    """
    #  QStringDecoder::QStringDecoder(Encoding encoding, Flags flags)
    self._noteCreation(QStringDecoder, lambda: Rituals.call(
        'ritual_ZN14QStringDecoderC1EN16QStringConverter8EncodingE6QFlagsIN'
        '20QStringConverterBase4FlagEE',
        encoding.value, flags.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStringDecoder::QStringDecoder()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringdecoder.html#QStringDecoder
    """
    #  QStringDecoder::QStringDecoder()
    self._noteCreation(QStringDecoder, lambda: Rituals.call(
        'ritual_ZN14QStringDecoderC1Ev',
    ))

  @overload(str)
  @overload(str, QStringConverterBase.Flags)
  def __init__(
      self,
      name: str,
      f: QStringConverterBase.Flags = QStringConverterBase.Flags.Default,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QStringDecoder::QStringDecoder(QAnyStringView name, Flags f)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringdecoder.html#QStringDecoder

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    f : QStringConverterBase.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QStringConverterBase.Flags.Default.
    """
    #  QStringDecoder::QStringDecoder(QAnyStringView name, Flags f)
    self._noteCreation(QStringDecoder, lambda: Rituals.call(
        'ritual_ZN14QStringDecoderC1E14QAnyStringView6QFlagsIN20QStringConv'
        'erterBase4FlagEE',
        name, f.value,
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

  @overload(QChar, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def appendToBuffer(
      self,
      out: Optional[QChar],
      ba: QByteArrayView,
  ) -> Optional[QChar]:
    """
    Calls Qt's 'QChar *QStringDecoder::appendToBuffer(QChar *out,
    QByteArrayView ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringdecoder.html#appendToBuffer

    Parameters
    ----------

    out : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ba : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChar *QStringDecoder::appendToBuffer(QChar *out, QByteArrayView ba)
    address = self.uglySide.call(
        'ritual_ZN14QStringDecoder14appendToBufferEP5QChar14QByteArrayView',
        self._addressOf(out), self._valueOf(ba),
    )
    from . import QChar
    return QChar._cuteAt(address)

  def invalidateAndReturnNull(self) -> str:
    """
    Calls Qt's 'QString QStringDecoder::invalidateAndReturnNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringdecoder.html#invalidateAndReturnNull

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringDecoder::invalidateAndReturnNull()
    return self.uglySide.call(
        'ritual_ZN14QStringDecoder23invalidateAndReturnNullEv',
    )

  @overload(QByteArrayView)
  def decodeAsStringImpl(self, in_: QByteArrayView) -> str:
    """
    Calls Qt's 'QString QStringDecoder::decodeAsStringImpl(QByteArrayView
    in)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringdecoder.html#decodeAsStringImpl

    Parameters
    ----------

    in_ : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringDecoder::decodeAsStringImpl(QByteArrayView in)
    return self.uglySide.call(
        'ritual_ZN14QStringDecoder18decodeAsStringImplE14QByteArrayView',
        self._valueOf(in_),
    )

  @overload(QByteArrayView)
  def decodeAsString(self, in_: QByteArrayView) -> str:
    """
    Calls Qt's 'QString QStringDecoder::decodeAsString(QByteArrayView in)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringdecoder.html#decodeAsString

    Parameters
    ----------

    in_ : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStringDecoder::decodeAsString(QByteArrayView in)
    return self.uglySide.call(
        'ritual_ZN14QStringDecoder14decodeAsStringE14QByteArrayView',
        self._valueOf(in_),
    )
