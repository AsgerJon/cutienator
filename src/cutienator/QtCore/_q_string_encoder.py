"""
QStringEncoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstringconverter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QStringConverter, QStringConverterBase


class QStringEncoder(QStringConverter):
  """
  The cute side of Qt's QStringEncoder: a plain Python object standing in
  front of one C++ QStringEncoder.

  It is built on the cute 'QStringConverter', as Qt's QStringEncoder is built
  on Qt's QStringConverter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStringEncoder that has a ritual and that Python can
  call so far, 1 name in all: 'requiredSpace'. It can be made from Python, in
  3 ways; see '__init__'.

  What has no ritual
  ------------------

  11 of the 15 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 3 private; 2 a template; 1 protected.

  What to expect
  --------------

  - The C++ QStringEncoder is created at the first use, not by
    'QStringEncoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStringEncoder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringEncoder'

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
    Calls Qt's 'qsizetype QStringEncoder::requiredSpace(qsizetype
    inputLength) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstringencoder.html#requiredSpace

    Parameters
    ----------

    inputLength : int
      Passed on as it is.
    """
    #  qsizetype QStringEncoder::requiredSpace(qsizetype inputLength) const
    return self.uglySide.call(
        'ritual_ZNK14QStringEncoder13requiredSpaceEx', inputLength,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QStringEncoder::QStringEncoder()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringencoder.html#QStringEncoder
    """
    #  QStringEncoder::QStringEncoder()
    self._noteCreation(QStringEncoder, lambda: Rituals.call(
        'ritual_ZN14QStringEncoderC1Ev',
    ))

  @overload(QStringConverter.Encoding)
  @overload(QStringConverter.Encoding, QStringConverterBase.Flags)
  def __init__(
      self,
      encoding: QStringConverter.Encoding,
      flags: QStringConverterBase.Flags = QStringConverterBase.Flags.Default,
  ) -> None:
    """
    Notes what was given, for Qt's 'QStringEncoder::QStringEncoder(Encoding
    encoding, Flags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringencoder.html#QStringEncoder

    Parameters
    ----------

    encoding : QStringConverter.Encoding
      Passed on as its number.

    flags : QStringConverterBase.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QStringConverterBase.Flags.Default.
    """
    #  QStringEncoder::QStringEncoder(Encoding encoding, Flags flags)
    self._noteCreation(QStringEncoder, lambda: Rituals.call(
        'ritual_ZN14QStringEncoderC1EN16QStringConverter8EncodingE6QFlagsIN'
        '20QStringConverterBase4FlagEE',
        encoding.value, flags.value,
    ))

  @overload(str)
  @overload(str, QStringConverterBase.Flags)
  def __init__(
      self,
      name: str,
      flags: QStringConverterBase.Flags = QStringConverterBase.Flags.Default,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QStringEncoder::QStringEncoder(QAnyStringView name, Flags flags)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstringencoder.html#QStringEncoder

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    flags : QStringConverterBase.Flags
      Passed on as its number. May be left out, as in Qt: it is then
      QStringConverterBase.Flags.Default.
    """
    #  QStringEncoder::QStringEncoder(QAnyStringView name, Flags flags)
    self._noteCreation(QStringEncoder, lambda: Rituals.call(
        'ritual_ZN14QStringEncoderC1E14QAnyStringView6QFlagsIN20QStringConv'
        'erterBase4FlagEE',
        name, flags.value,
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
