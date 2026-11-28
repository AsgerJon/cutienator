"""
QDrWavAudioDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qdrawavaudiodecoder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDrWavAudioDecoder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QPlatformAudioDecoder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QUrl
  from . import QAudioBuffer, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']


class QDrWavAudioDecoder(QPlatformAudioDecoder):
  """
  The cute side of Qt's QDrWavAudioDecoder: a plain Python object standing in
  front of one C++ QDrWavAudioDecoder.

  It is built on the cute 'QPlatformAudioDecoder', as Qt's QDrWavAudioDecoder
  is built on Qt's QPlatformAudioDecoder, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDrWavAudioDecoder that has a ritual and that Python
  can call so far, 6 names in all: 'source', 'sourceDevice', 'audioFormat',
  'setAudioFormat', 'read', 'canReadQrc'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDrWavAudioDecoder::onDecodeFinished(QDrWavDecodeResult a0,
    const std::atomic_bool &decodingStopped)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 4 leans on 'QDrWavAudioDecoder; 3 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file.

  What to expect
  --------------

  - The C++ QDrWavAudioDecoder is created at the first use, not by
    'QDrWavAudioDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDrWavAudioDecoder.
  - Qt tells when it has removed the C++ QDrWavAudioDecoder. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDrWavAudioDecoder that has no cute function yet,
    '__init__', 'loadAndDecodeFile', 'onDecodeFinished', holds a function
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
  __qt_class__ = 'QDrWavAudioDecoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QDrWavAudioDecoder::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrwavaudiodecoder.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QDrWavAudioDecoder::source() const
    address = self.uglySide.call('ritual_ZNK18QDrWavAudioDecoder6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceDevice(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QDrWavAudioDecoder::sourceDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdrwavaudiodecoder.html#sourceDevice

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QDrWavAudioDecoder::sourceDevice() const
    address = self.uglySide.call(
        'ritual_ZNK18QDrWavAudioDecoder12sourceDeviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def audioFormat(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QDrWavAudioDecoder::audioFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdrwavaudiodecoder.html#audioFormat

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QDrWavAudioDecoder::audioFormat() const
    address = self.uglySide.call(
        'ritual_ZNK18QDrWavAudioDecoder11audioFormatEv',
    )
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def canReadQrc(self) -> bool:
    """
    Calls Qt's 'bool QDrWavAudioDecoder::canReadQrc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrwavaudiodecoder.html#canReadQrc
    """
    #  bool QDrWavAudioDecoder::canReadQrc() const
    return self.uglySide.call('ritual_ZNK18QDrWavAudioDecoder10canReadQrcEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioFormat)
  def setAudioFormat(self, a0: QAudioFormat) -> None:
    """
    Calls Qt's 'void QDrWavAudioDecoder::setAudioFormat(const QAudioFormat
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdrwavaudiodecoder.html#setAudioFormat

    Parameters
    ----------

    a0 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  void QDrWavAudioDecoder::setAudioFormat(const QAudioFormat &a0)
    self.uglySide.call(
        'ritual_ZN18QDrWavAudioDecoder14setAudioFormatERK12QAudioFormat',
        self._valueOf(a0),
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
    Qt's 'QDrWavAudioDecoder::QDrWavAudioDecoder(QAudioDecoder *parent)':
    leans on 'QDrWavAudioDecoder::stop()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDrWavAudioDecoder.__init__' has no cute function yet. Qt's "
        "'QDrWavAudioDecoder::QDrWavAudioDecoder(QAudioDecoder *parent)': "
        "leans on 'QDrWavAudioDecoder::stop()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def read(self) -> QAudioBuffer:
    """
    Calls Qt's 'QAudioBuffer QDrWavAudioDecoder::read()'.

    Qt's own words: https://doc.qt.io/qt-6/qdrwavaudiodecoder.html#read

    Returns
    -------

    QAudioBuffer
      A new cute QAudioBuffer around the copy Qt gave back. Python owns it.
    """
    #  QAudioBuffer QDrWavAudioDecoder::read()
    address = self.uglySide.call('ritual_ZN18QDrWavAudioDecoder4readEv')
    from . import QAudioBuffer
    return QAudioBuffer._cuteOwning(address)

  @staticmethod
  def loadAndDecodeFile(*__, **_) -> Never:
    """
    Qt's 'QDrWavDecodeResult QDrWavAudioDecoder::loadAndDecodeFile(const QUrl
    &a0, QIODevice *a1, const QAudioFormat &a2,
    std::shared_ptr<std::atomic_bool> decodingStopped)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'makeResourceError'.
    """
    raise NotImplementedError(
        "'QDrWavAudioDecoder.loadAndDecodeFile' has no cute function yet. "
        "Qt's 'QDrWavDecodeResult "
        "QDrWavAudioDecoder::loadAndDecodeFile(const QUrl &a0, QIODevice "
        "*a1, const QAudioFormat &a2, std::shared_ptr<std::atomic_bool> "
        "decodingStopped)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'makeResourceError'.")

  @staticmethod
  def onDecodeFinished(*__, **_) -> Never:
    """
    Qt's 'void QDrWavAudioDecoder::onDecodeFinished(QDrWavDecodeResult a0,
    const std::atomic_bool &decodingStopped)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QDrWavAudioDecoder.onDecodeFinished' has no cute function yet. "
        "Qt's 'void QDrWavAudioDecoder::onDecodeFinished(QDrWavDecodeResult "
        "a0, const std::atomic_bool &decodingStopped)': takes a type Python "
        "has no way to hand over yet.")
