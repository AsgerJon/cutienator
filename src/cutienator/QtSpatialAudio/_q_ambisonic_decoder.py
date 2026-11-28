"""
QAmbisonicDecoder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/6.12.0/QtSpatialAudio/private/qambisonicdecoder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAmbisonicDecoder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QAmbisonicDecoder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAmbisonicDecoder: a plain Python object standing in
  front of one C++ QAmbisonicDecoder.

  What exists
  -----------

  Every function of Qt's QAmbisonicDecoder that has a ritual and that Python
  can call so far, 4 names in all: 'hasValidConfig', 'nInputChannels',
  'nOutputChannels', 'outputSamples'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAmbisonicDecoder::~QAmbisonicDecoder()': the destructor: Python
    never removes a C++ QAmbisonicDecoder.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QAmbisonicDecoder is created at the first use, not by
    'QAmbisonicDecoder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAmbisonicDecoder.
  - Each name of Qt's QAmbisonicDecoder that has no cute function yet,
    '__init__', 'processBuffer', 'processBufferWithReverb', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAmbisonicDecoder, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AmbisonicOrder(CuteNum):
    """
    The enum 'QAmbisonicDecoder::AmbisonicOrder' of Qt, with the 6 names Qt
    gives in it.
    """

    Ambisonic1stOrder = Kee[int](1)
    LowQuality = Kee[int](1)
    Ambisonic2ndOrder = Kee[int](2)
    MediumQuality = Kee[int](2)
    Ambisonic3rdOrder = Kee[int](3)
    HighQuality = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAmbisonicDecoder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasValidConfig(self) -> bool:
    """
    Calls Qt's 'bool QAmbisonicDecoder::hasValidConfig() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambisonicdecoder.html#hasValidConfig
    """
    #  bool QAmbisonicDecoder::hasValidConfig() const
    return self.uglySide.call(
        'ritual_ZNK17QAmbisonicDecoder14hasValidConfigEv',
    )

  def nInputChannels(self) -> int:
    """
    Calls Qt's 'int QAmbisonicDecoder::nInputChannels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambisonicdecoder.html#nInputChannels
    """
    #  int QAmbisonicDecoder::nInputChannels() const
    return self.uglySide.call(
        'ritual_ZNK17QAmbisonicDecoder14nInputChannelsEv',
    )

  def nOutputChannels(self) -> int:
    """
    Calls Qt's 'int QAmbisonicDecoder::nOutputChannels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambisonicdecoder.html#nOutputChannels
    """
    #  int QAmbisonicDecoder::nOutputChannels() const
    return self.uglySide.call(
        'ritual_ZNK17QAmbisonicDecoder15nOutputChannelsEv',
    )

  @overload(int)
  def outputSamples(self, nFrames: int) -> int:
    """
    Calls Qt's 'int QAmbisonicDecoder::outputSamples(int nFrames) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qambisonicdecoder.html#outputSamples

    Parameters
    ----------

    nFrames : int
      Passed on as it is.
    """
    #  int QAmbisonicDecoder::outputSamples(int nFrames) const
    return self.uglySide.call(
        'ritual_ZNK17QAmbisonicDecoder13outputSamplesEi', nFrames,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAmbisonicDecoder::QAmbisonicDecoder(AmbisonicOrder a0, int
    sampleRate, int numberOfOutputChannels, QAudioFormat::ChannelConfig a3)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: allocation of incomplete type
    'remove_extent_t<QAmbisonicDecoderFilter[]>' (aka
    'QAmbisonicDecoderFilter').
    """
    raise NotImplementedError(
        "'QAmbisonicDecoder.__init__' has no cute function yet. Qt's "
        "'QAmbisonicDecoder::QAmbisonicDecoder(AmbisonicOrder a0, int "
        "sampleRate, int numberOfOutputChannels, "
        "QAudioFormat::ChannelConfig a3)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "allocation of incomplete type "
        "'remove_extent_t<QAmbisonicDecoderFilter[]>' (aka "
        "'QAmbisonicDecoderFilter').")

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

  @staticmethod
  def processBuffer(*__, **_) -> Never:
    """
    Qt's 'void QAmbisonicDecoder::processBuffer(QSpan<const float *> input,
    QSpan<float> output)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'const QAmbisonicDecoderData'.
    """
    raise NotImplementedError(
        "'QAmbisonicDecoder.processBuffer' has no cute function yet. Qt's "
        "'void QAmbisonicDecoder::processBuffer(QSpan<const float *> input, "
        "QSpan<float> output)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'const QAmbisonicDecoderData'.")

  @staticmethod
  def processBufferWithReverb(*__, **_) -> Never:
    """
    Qt's 'void QAmbisonicDecoder::processBufferWithReverb(QSpan<const float
    *> input, QSpan<const float *, 2> reverb, QSpan<float> output)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QAmbisonicDecoderData'.
    """
    raise NotImplementedError(
        "'QAmbisonicDecoder.processBufferWithReverb' has no cute function "
        "yet. Qt's 'void "
        "QAmbisonicDecoder::processBufferWithReverb(QSpan<const float *> "
        "input, QSpan<const float *, 2> reverb, QSpan<float> output)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QAmbisonicDecoderData'.")
