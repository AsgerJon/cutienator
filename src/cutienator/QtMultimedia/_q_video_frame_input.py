"""
QVideoFrameInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qvideoframeinput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QMediaCaptureSession, QPlatformVideoFrameInput, QVideoFrame
  from . import QVideoFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaCaptureSession = WAIT['QMediaCaptureSession']
  QVideoFrame = WAIT['QVideoFrame']
  QVideoFrameFormat = WAIT['QVideoFrameFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoFrameInput(QObject):
  """
  The cute side of Qt's QVideoFrameInput: a plain Python object standing in
  front of one C++ QVideoFrameInput.

  It is built on the cute 'QObject', as Qt's QVideoFrameInput is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoFrameInput that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'tr', 'sendVideoFrame',
  'format', 'captureSession', 'readyToSendVideoFrame', 'setCaptureSession',
  'platformVideoFrameInput'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVideoFrameInput::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QVideoFrameInput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QVideoFrameInput::~QVideoFrameInput()': the destructor: Python
    never removes a C++ QVideoFrameInput.
  - Qt's 'QVideoFrameInputPrivate *QVideoFrameInput::d_func()': gives
    'QVideoFrameInputPrivate', which has no cute class yet.
  - Qt's 'const QVideoFrameInputPrivate *QVideoFrameInput::d_func() const':
    gives 'QVideoFrameInputPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QVideoFrameInput is created at the first use, not by
    'QVideoFrameInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoFrameInput.
  - Qt tells when it has removed the C++ QVideoFrameInput. Every call on the
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
    Calls Qt's 'QString QVideoFrameInput::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeinput.html#tr

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
    #  QString QVideoFrameInput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QVideoFrameInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoFrameInput'

  #  A C++ QVideoFrameInput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoFrameInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVideoFrameInput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVideoFrameInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QVideoFrameInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def format(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QVideoFrameInput::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideoframeinput.html#format

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QVideoFrameInput::format() const
    address = self.uglySide.call('ritual_ZNK16QVideoFrameInput6formatEv')
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QVideoFrameInput::captureSession()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QVideoFrameInput::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK16QVideoFrameInput14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  def platformVideoFrameInput(self) -> Optional[QPlatformVideoFrameInput]:
    """
    Calls Qt's 'QPlatformVideoFrameInput
    *QVideoFrameInput::platformVideoFrameInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#platformVideoFrameInput

    Returns
    -------

    Optional[QPlatformVideoFrameInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVideoFrameInput *QVideoFrameInput::platformVideoFrameInput()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QVideoFrameInput23platformVideoFrameInputEv',
    )
    from . import QPlatformVideoFrameInput
    return QPlatformVideoFrameInput._cuteAt(address)

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
    Calls Qt's 'void QVideoFrameInput::setCaptureSession(QMediaCaptureSession
    *captureSession)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#setCaptureSession

    Parameters
    ----------

    captureSession : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoFrameInput::setCaptureSession(QMediaCaptureSession
    #      *captureSession)
    self.uglySide.call(
        'ritual_ZN16QVideoFrameInput17setCaptureSessionEP20QMediaCaptureSes'
        'sion',
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
    'QVideoFrameInput::QVideoFrameInput(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#QVideoFrameInput

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVideoFrameInput::QVideoFrameInput(QObject *parent)
    self._noteCreation(QVideoFrameInput, lambda: Rituals.call(
        'ritual_ZN16QVideoFrameInputC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QVideoFrameFormat)
  @overload(QVideoFrameFormat, QObject)
  @overload(QVideoFrameFormat, NoneType)
  def __init__(
      self,
      format: QVideoFrameFormat,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QVideoFrameInput::QVideoFrameInput(const
    QVideoFrameFormat &format, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#QVideoFrameInput

    Parameters
    ----------

    format : QVideoFrameFormat
      Passed on as a value: Qt reads the C++ QVideoFrameFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVideoFrameInput::QVideoFrameInput(const QVideoFrameFormat &format,
    #      QObject *parent)
    self._noteCreation(QVideoFrameInput, lambda: Rituals.call(
        'ritual_ZN16QVideoFrameInputC1ERK17QVideoFrameFormatP7QObject',
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

  @overload(QVideoFrame)
  def sendVideoFrame(self, frame: QVideoFrame) -> bool:
    """
    Calls Qt's 'bool QVideoFrameInput::sendVideoFrame(const QVideoFrame
    &frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#sendVideoFrame

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  bool QVideoFrameInput::sendVideoFrame(const QVideoFrame &frame)
    return self.uglySide.call(
        'ritual_ZN16QVideoFrameInput14sendVideoFrameERK11QVideoFrame',
        self._valueOf(frame),
    )

  def readyToSendVideoFrame(self) -> None:
    """
    Calls Qt's 'void QVideoFrameInput::readyToSendVideoFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideoframeinput.html#readyToSendVideoFrame
    """
    #  void QVideoFrameInput::readyToSendVideoFrame()
    self.uglySide.call(
        'ritual_ZN16QVideoFrameInput21readyToSendVideoFrameEv',
    )
