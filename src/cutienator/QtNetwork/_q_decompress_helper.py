"""
QDecompressHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qdecompresshelper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDecompressHelper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QByteArrayView
  from . import QByteDataBuffer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QByteDataBuffer = WAIT['QByteDataBuffer']


class QDecompressHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDecompressHelper: a plain Python object standing in
  front of one C++ QDecompressHelper.

  What exists
  -----------

  Every function of Qt's QDecompressHelper that has a ritual and that Python
  can call so far, 16 names in all: 'setEncoding', 'isCountingBytes',
  'setCountingBytesEnabled', 'uncompressedSize', 'hasData', 'feed',
  'isValid', 'clear', 'setDecompressedSafetyCheckThreshold',
  'isSupportedEncoding', 'acceptedEncoding', 'errorString',
  'isPotentialArchiveBomb', 'hasDataInternal', 'countInternal',
  'encodedBytesAvailable'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDecompressHelper::~QDecompressHelper()': the destructor: Python
    never removes a C++ QDecompressHelper.
  - Qt's 'void QDecompressHelper::feed(QByteArray &&data)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QDecompressHelper::feed(QByteDataBuffer &&buffer)': takes a
    type Python has no way to hand over yet.
  - Qt's 'qsizetype QDecompressHelper::read(char *data, qsizetype maxSize)':
    names 'char', which has no cute class yet.
  - Qt's 'qsizetype QDecompressHelper::readInternal(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
  - Qt's 'qsizetype QDecompressHelper::readZLib(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
  - Qt's 'qsizetype QDecompressHelper::readBrotli(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
  - Qt's 'qsizetype QDecompressHelper::readZstandard(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.

  What to expect
  --------------

  - The C++ QDecompressHelper is created at the first use, not by
    'QDecompressHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDecompressHelper.
  - Each name of Qt's QDecompressHelper that has no cute function yet,
    'read', 'readBrotli', 'readInternal', 'readZLib', 'readZstandard', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDecompressHelper, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ContentEncoding(CuteNum):
    """
    The enum 'QDecompressHelper::ContentEncoding' of Qt, with the 5 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Deflate = Kee[int](1)
    GZip = Kee[int](2)
    Brotli = Kee[int](3)
    Zstandard = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView)
  def isSupportedEncoding(encoding: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::isSupportedEncoding(QByteArrayView
    encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#isSupportedEncoding

    Parameters
    ----------

    encoding : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QDecompressHelper::isSupportedEncoding(QByteArrayView encoding)
    return Rituals.call(
        'ritual_ZN17QDecompressHelper19isSupportedEncodingE14QByteArrayView',
        CuteMixin._valueOf(encoding),
    )

  @staticmethod
  def acceptedEncoding() -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList QDecompressHelper::acceptedEncoding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#acceptedEncoding

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList QDecompressHelper::acceptedEncoding()
    address = Rituals.call(
        'ritual_ZN17QDecompressHelper16acceptedEncodingEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDecompressHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isCountingBytes(self) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::isCountingBytes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#isCountingBytes
    """
    #  bool QDecompressHelper::isCountingBytes() const
    return self.uglySide.call(
        'ritual_ZNK17QDecompressHelper15isCountingBytesEv',
    )

  def uncompressedSize(self) -> int:
    """
    Calls Qt's 'qint64 QDecompressHelper::uncompressedSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#uncompressedSize
    """
    #  qint64 QDecompressHelper::uncompressedSize() const
    return self.uglySide.call(
        'ritual_ZNK17QDecompressHelper16uncompressedSizeEv',
    )

  def hasData(self) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::hasData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#hasData
    """
    #  bool QDecompressHelper::hasData() const
    return self.uglySide.call('ritual_ZNK17QDecompressHelper7hasDataEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#isValid
    """
    #  bool QDecompressHelper::isValid() const
    return self.uglySide.call('ritual_ZNK17QDecompressHelper7isValidEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDecompressHelper::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDecompressHelper::errorString() const
    return self.uglySide.call('ritual_ZNK17QDecompressHelper11errorStringEv')

  def isPotentialArchiveBomb(self) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::isPotentialArchiveBomb() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#isPotentialArchiveBomb
    """
    #  bool QDecompressHelper::isPotentialArchiveBomb() const
    return self.uglySide.call(
        'ritual_ZNK17QDecompressHelper22isPotentialArchiveBombEv',
    )

  def hasDataInternal(self) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::hasDataInternal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#hasDataInternal
    """
    #  bool QDecompressHelper::hasDataInternal() const
    return self.uglySide.call(
        'ritual_ZNK17QDecompressHelper15hasDataInternalEv',
    )

  def encodedBytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QDecompressHelper::encodedBytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#encodedBytesAvailable
    """
    #  qint64 QDecompressHelper::encodedBytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK17QDecompressHelper21encodedBytesAvailableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArrayView)
  def setEncoding(self, contentEncoding: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::setEncoding(QByteArrayView
    contentEncoding)'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#setEncoding

    Parameters
    ----------

    contentEncoding : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QDecompressHelper::setEncoding(QByteArrayView contentEncoding)
    return self.uglySide.call(
        'ritual_ZN17QDecompressHelper11setEncodingE14QByteArrayView',
        self._valueOf(contentEncoding),
    )

  @overload(ContentEncoding)
  def setEncoding(self, ce: ContentEncoding) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::setEncoding(ContentEncoding ce)'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#setEncoding

    Parameters
    ----------

    ce : ContentEncoding
      Passed on as its number.
    """
    #  bool QDecompressHelper::setEncoding(ContentEncoding ce)
    return self.uglySide.call(
        'ritual_ZN17QDecompressHelper11setEncodingENS_15ContentEncodingE',
        ce.value,
    )

  @overload(bool)
  def setCountingBytesEnabled(self, shouldCount: bool) -> None:
    """
    Calls Qt's 'void QDecompressHelper::setCountingBytesEnabled(bool
    shouldCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#setCountingBytesEnabled

    Parameters
    ----------

    shouldCount : bool
      Passed on as it is.
    """
    #  void QDecompressHelper::setCountingBytesEnabled(bool shouldCount)
    self.uglySide.call(
        'ritual_ZN17QDecompressHelper23setCountingBytesEnabledEb',
        shouldCount,
    )

  @overload(int)
  def setDecompressedSafetyCheckThreshold(self, threshold: int) -> None:
    """
    Calls Qt's 'void
    QDecompressHelper::setDecompressedSafetyCheckThreshold(qint64
    threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html

    Parameters
    ----------

    threshold : int
      Passed on as it is.
    """
    #  void QDecompressHelper::setDecompressedSafetyCheckThreshold(qint64
    #      threshold)
    self.uglySide.call(
        'ritual_ZN17QDecompressHelper35setDecompressedSafetyCheckThresholdE'
        'x',
        threshold,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDecompressHelper::QDecompressHelper()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#QDecompressHelper
    """
    #  QDecompressHelper::QDecompressHelper()
    self._noteCreation(QDecompressHelper, lambda: Rituals.call(
        'ritual_ZN17QDecompressHelperC1Ev',
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

  @overload(QByteArray)
  def feed(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QDecompressHelper::feed(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#feed

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QDecompressHelper::feed(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QDecompressHelper4feedERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteDataBuffer)
  def feed(self, buffer: QByteDataBuffer) -> None:
    """
    Calls Qt's 'void QDecompressHelper::feed(const QByteDataBuffer &buffer)'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#feed

    Parameters
    ----------

    buffer : QByteDataBuffer
      Passed on as a value: Qt reads the C++ QByteDataBuffer, which stays
      Python's own.
    """
    #  void QDecompressHelper::feed(const QByteDataBuffer &buffer)
    self.uglySide.call(
        'ritual_ZN17QDecompressHelper4feedERK15QByteDataBuffer',
        self._valueOf(buffer),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QDecompressHelper::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdecompresshelper.html#clear
    """
    #  void QDecompressHelper::clear()
    self.uglySide.call('ritual_ZN17QDecompressHelper5clearEv')

  @overload()
  def countInternal(self) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::countInternal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#countInternal
    """
    #  bool QDecompressHelper::countInternal()
    return self.uglySide.call(
        'ritual_ZN17QDecompressHelper13countInternalEv',
    )

  @overload(QByteArray)
  def countInternal(self, data: QByteArray) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::countInternal(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#countInternal

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QDecompressHelper::countInternal(const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN17QDecompressHelper13countInternalERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteDataBuffer)
  def countInternal(self, buffer: QByteDataBuffer) -> bool:
    """
    Calls Qt's 'bool QDecompressHelper::countInternal(const QByteDataBuffer
    &buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdecompresshelper.html#countInternal

    Parameters
    ----------

    buffer : QByteDataBuffer
      Passed on as a value: Qt reads the C++ QByteDataBuffer, which stays
      Python's own.
    """
    #  bool QDecompressHelper::countInternal(const QByteDataBuffer &buffer)
    return self.uglySide.call(
        'ritual_ZN17QDecompressHelper13countInternalERK15QByteDataBuffer',
        self._valueOf(buffer),
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDecompressHelper::read(char *data, qsizetype maxSize)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDecompressHelper.read' has no cute function yet. Qt's 'qsizetype "
        "QDecompressHelper::read(char *data, qsizetype maxSize)': names "
        "'char', which has no cute class yet.")

  @staticmethod
  def readBrotli(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDecompressHelper::readBrotli(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDecompressHelper.readBrotli' has no cute function yet. Qt's "
        "'qsizetype QDecompressHelper::readBrotli(char *data, qsizetype "
        "maxSize)': names 'char', which has no cute class yet.")

  @staticmethod
  def readInternal(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDecompressHelper::readInternal(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDecompressHelper.readInternal' has no cute function yet. Qt's "
        "'qsizetype QDecompressHelper::readInternal(char *data, qsizetype "
        "maxSize)': names 'char', which has no cute class yet.")

  @staticmethod
  def readZLib(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDecompressHelper::readZLib(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDecompressHelper.readZLib' has no cute function yet. Qt's "
        "'qsizetype QDecompressHelper::readZLib(char *data, qsizetype "
        "maxSize)': names 'char', which has no cute class yet.")

  @staticmethod
  def readZstandard(*__, **_) -> Never:
    """
    Qt's 'qsizetype QDecompressHelper::readZstandard(char *data, qsizetype
    maxSize)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDecompressHelper.readZstandard' has no cute function yet. Qt's "
        "'qsizetype QDecompressHelper::readZstandard(char *data, qsizetype "
        "maxSize)': names 'char', which has no cute class yet.")
