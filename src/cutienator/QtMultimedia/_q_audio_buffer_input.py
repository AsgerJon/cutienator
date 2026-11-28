"""
QAudioBufferInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiobufferinput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAudioBuffer, QAudioFormat, QMediaCaptureSession
  from . import QPlatformAudioBufferInput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioBuffer = WAIT['QAudioBuffer']
  QAudioFormat = WAIT['QAudioFormat']
  QMediaCaptureSession = WAIT['QMediaCaptureSession']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioBufferInput(QObject):
  """
  The cute side of Qt's QAudioBufferInput: a plain Python object standing in
  front of one C++ QAudioBufferInput.

  It is built on the cute 'QObject', as Qt's QAudioBufferInput is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioBufferInput that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'sendAudioBuffer',
  'format', 'captureSession', 'readyToSendAudioBuffer', 'setCaptureSession',
  'platformAudioBufferInput'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioBufferInput::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAudioBufferInput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioBufferInput::~QAudioBufferInput()': the destructor: Python
    never removes a C++ QAudioBufferInput.
  - Qt's 'QAudioBufferInputPrivate *QAudioBufferInput::d_func()': gives
    'QAudioBufferInputPrivate', which has no cute class yet.
  - Qt's 'const QAudioBufferInputPrivate *QAudioBufferInput::d_func() const':
    gives 'QAudioBufferInputPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioBufferInput is created at the first use, not by
    'QAudioBufferInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioBufferInput.
  - Qt tells when it has removed the C++ QAudioBufferInput. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QAudioBufferInput::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferinput.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAudioBufferInput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QAudioBufferInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioBufferInput'

  #  A C++ QAudioBufferInput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioBufferInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioBufferInput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioBufferInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QAudioBufferInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioBufferInput::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiobufferinput.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioBufferInput::format() const
    address = self.uglySide.call('ritual_ZNK17QAudioBufferInput6formatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QAudioBufferInput::captureSession()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QAudioBufferInput::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK17QAudioBufferInput14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def platformAudioBufferInput(self) -> Optional[QPlatformAudioBufferInput]:
    """
    Calls Qt's 'QPlatformAudioBufferInput
    *QAudioBufferInput::platformAudioBufferInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#platformAudioBufferInput

    Returns
    -------

    Optional[QPlatformAudioBufferInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioBufferInput
    #      *QAudioBufferInput::platformAudioBufferInput() const
    address = self.uglySide.call(
        'ritual_ZNK17QAudioBufferInput24platformAudioBufferInputEv',
    )
    from . import QPlatformAudioBufferInput
    return QPlatformAudioBufferInput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      captureSession: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void
    QAudioBufferInput::setCaptureSession(QMediaCaptureSession
    *captureSession)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#setCaptureSession

    Parameters
    ----------

    captureSession : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAudioBufferInput::setCaptureSession(QMediaCaptureSession
    #      *captureSession)
    self.uglySide.call(
        'ritual_ZN17QAudioBufferInput17setCaptureSessionEP20QMediaCaptureSe'
        'ssion',
        self._addressOf(captureSession),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAudioBufferInput::QAudioBufferInput(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#QAudioBufferInput

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioBufferInput::QAudioBufferInput(QObject *parent)
    self._noteCreation(QAudioBufferInput, lambda: Rituals.call(
        'ritual_ZN17QAudioBufferInputC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAudioFormat)
  @overload(QAudioFormat, QObject)
  @overload(QAudioFormat, NoneType)
  def __init__(
      self,
      format: QAudioFormat,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAudioBufferInput::QAudioBufferInput(const QAudioFormat &format, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#QAudioBufferInput

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioBufferInput::QAudioBufferInput(const QAudioFormat &format,
    #      QObject *parent)
    self._noteCreation(QAudioBufferInput, lambda: Rituals.call(
        'ritual_ZN17QAudioBufferInputC1ERK12QAudioFormatP7QObject',
        self._valueOf(format), self._addressOf(parent, 'QObject'),
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

  @overload(QAudioBuffer)
  def sendAudioBuffer(self, audioBuffer: QAudioBuffer) -> bool:
    """
    Calls Qt's 'bool QAudioBufferInput::sendAudioBuffer(const QAudioBuffer
    &audioBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#sendAudioBuffer

    Parameters
    ----------

    audioBuffer : QAudioBuffer
      Passed on as a value: Qt reads the C++ QAudioBuffer, which stays
      Python's own.
    """
    #  bool QAudioBufferInput::sendAudioBuffer(const QAudioBuffer
    #      &audioBuffer)
    return self.uglySide.call(
        'ritual_ZN17QAudioBufferInput15sendAudioBufferERK12QAudioBuffer',
        self._valueOf(audioBuffer),
    )

  def readyToSendAudioBuffer(self) -> None:
    """
    Calls Qt's 'void QAudioBufferInput::readyToSendAudioBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiobufferinput.html#readyToSendAudioBuffer
    """
    #  void QAudioBufferInput::readyToSendAudioBuffer()
    self.uglySide.call(
        'ritual_ZN17QAudioBufferInput22readyToSendAudioBufferEv',
    )
