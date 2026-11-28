"""
QOpcUaBinaryDataEncoding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuabinarydataencoding.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpcUaBinaryDataEncoding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaBinaryDataEncoding: a plain Python object
  standing in front of one C++ QOpcUaBinaryDataEncoding.

  C++ hands a QOpcUaBinaryDataEncoding around as a copy, so every C++
  QOpcUaBinaryDataEncoding behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaBinaryDataEncoding that has a ritual and that
  Python can call so far, 4 names in all: 'offset', 'setOffset',
  'truncateBufferToOffset', 'enoughData'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOpcUaBinaryDataEncoding::QOpcUaBinaryDataEncoding(QOpcUaExtensionObject
    &object)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaBinaryDataEncoding::~QOpcUaBinaryDataEncoding()': the
    destructor: Python removes its C++ QOpcUaBinaryDataEncoding by it, and
    has no other use for it.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 7 a template.

  What to expect
  --------------

  - The C++ QOpcUaBinaryDataEncoding is created at the first use, not by
    'QOpcUaBinaryDataEncoding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaBinaryDataEncoding back gives a copy the ritual
    made for Python, in a new cute QOpcUaBinaryDataEncoding.
  - Each name of Qt's QOpcUaBinaryDataEncoding that has no cute function yet,
    'decode', 'decodeArray', 'decodeValueArrayOrScalar', 'encode',
    'encodeArray', 'encodeValueArrayOrScalar', 'upperBound', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaBinaryDataEncoding'

  #  Qt's '~QOpcUaBinaryDataEncoding()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaBinaryDataEncoding behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QOpcUaBinaryDataEncodingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offset(self) -> int:
    """
    Calls Qt's 'int QOpcUaBinaryDataEncoding::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabinarydataencoding.html#offset
    """
    #  int QOpcUaBinaryDataEncoding::offset() const
    return self.uglySide.call(
        'ritual_ZNK24QOpcUaBinaryDataEncoding6offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setOffset(self, offset: int) -> None:
    """
    Calls Qt's 'void QOpcUaBinaryDataEncoding::setOffset(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabinarydataencoding.html#setOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QOpcUaBinaryDataEncoding::setOffset(int offset)
    self.uglySide.call(
        'ritual_ZN24QOpcUaBinaryDataEncoding9setOffsetEi', offset,
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

  @overload(QByteArray)
  @overload(NoneType)
  def __init__(self, buffer: Optional[QByteArray]) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaBinaryDataEncoding::QOpcUaBinaryDataEncoding(QByteArray *buffer)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabinarydataencoding.html

    Parameters
    ----------

    buffer : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpcUaBinaryDataEncoding::QOpcUaBinaryDataEncoding(QByteArray *buffer)
    self._noteCreation(QOpcUaBinaryDataEncoding, lambda: Rituals.call(
        'ritual_ZN24QOpcUaBinaryDataEncodingC1EP10QByteArray',
        self._addressOf(buffer),
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

  def truncateBufferToOffset(self) -> None:
    """
    Calls Qt's 'void QOpcUaBinaryDataEncoding::truncateBufferToOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabinarydataencoding.html
    """
    #  void QOpcUaBinaryDataEncoding::truncateBufferToOffset()
    self.uglySide.call(
        'ritual_ZN24QOpcUaBinaryDataEncoding22truncateBufferToOffsetEv',
    )

  @overload(int)
  def enoughData(self, requiredSize: int) -> bool:
    """
    Calls Qt's 'bool QOpcUaBinaryDataEncoding::enoughData(int requiredSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuabinarydataencoding.html#enoughData

    Parameters
    ----------

    requiredSize : int
      Passed on as it is.
    """
    #  bool QOpcUaBinaryDataEncoding::enoughData(int requiredSize)
    return self.uglySide.call(
        'ritual_ZN24QOpcUaBinaryDataEncoding10enoughDataEi', requiredSize,
    )

  @staticmethod
  def decode(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::decode': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.decode' has no cute function yet. Qt's "
        "'QOpcUaBinaryDataEncoding::decode': a template: a pattern and no "
        "single function.")

  @staticmethod
  def decodeArray(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::decodeArray': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.decodeArray' has no cute function yet. "
        "Qt's 'QOpcUaBinaryDataEncoding::decodeArray': a template: a "
        "pattern and no single function.")

  @staticmethod
  def decodeValueArrayOrScalar(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::decodeValueArrayOrScalar': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.decodeValueArrayOrScalar' has no cute "
        "function yet. Qt's "
        "'QOpcUaBinaryDataEncoding::decodeValueArrayOrScalar': a template: "
        "a pattern and no single function.")

  @staticmethod
  def encode(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::encode': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.encode' has no cute function yet. Qt's "
        "'QOpcUaBinaryDataEncoding::encode': a template: a pattern and no "
        "single function.")

  @staticmethod
  def encodeArray(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::encodeArray': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.encodeArray' has no cute function yet. "
        "Qt's 'QOpcUaBinaryDataEncoding::encodeArray': a template: a "
        "pattern and no single function.")

  @staticmethod
  def encodeValueArrayOrScalar(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::encodeValueArrayOrScalar': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.encodeValueArrayOrScalar' has no cute "
        "function yet. Qt's "
        "'QOpcUaBinaryDataEncoding::encodeValueArrayOrScalar': a template: "
        "a pattern and no single function.")

  @staticmethod
  def upperBound(*__, **_) -> Never:
    """
    Qt's 'QOpcUaBinaryDataEncoding::upperBound': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QOpcUaBinaryDataEncoding.upperBound' has no cute function yet. "
        "Qt's 'QOpcUaBinaryDataEncoding::upperBound': a template: a pattern "
        "and no single function.")
