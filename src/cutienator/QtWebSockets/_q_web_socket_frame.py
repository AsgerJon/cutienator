"""
QWebSocketFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketframe_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWebSocketFrame to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebSocketFrame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebSocketFrame: a plain Python object standing in
  front of one C++ QWebSocketFrame.

  C++ hands a QWebSocketFrame around as a copy, so every C++ QWebSocketFrame
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebSocketFrame that has a ritual and that Python
  can call so far, 23 names in all: 'tr', 'setMaxAllowedFrameSize',
  'maxAllowedFrameSize', 'maxFrameSize', 'closeCode', 'closeReason',
  'isFinalFrame', 'isControlFrame', 'isDataFrame', 'isContinuationFrame',
  'hasMask', 'mask', 'rsv1', 'rsv2', 'rsv3', 'opCode', 'payload', 'clear',
  'isValid', 'isDone', 'readFrame', 'setError', 'checkValidity'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ProcessingState QWebSocketFrame::readFrameHeader(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
  - Qt's 'ProcessingState QWebSocketFrame::readFramePayloadLength(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
  - Qt's 'ProcessingState QWebSocketFrame::readFrameMask(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
  - Qt's 'ProcessingState QWebSocketFrame::readFramePayload(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
  - Qt's 'QWebSocketFrame::~QWebSocketFrame()': the destructor: Python
    removes its C++ QWebSocketFrame by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QWebSocketFrame is created at the first use, not by
    'QWebSocketFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebSocketFrame back gives a copy the ritual made for
    Python, in a new cute QWebSocketFrame.
  - Each name of Qt's QWebSocketFrame that has no cute function yet,
    'readFrameHeader', 'readFrameMask', 'readFramePayload',
    'readFramePayloadLength', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QWebSocketFrame::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketFrame::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN15QWebSocketFrame2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  def maxFrameSize() -> int:
    """
    Calls Qt's 'quint64 QWebSocketFrame::maxFrameSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#maxFrameSize
    """
    #  quint64 QWebSocketFrame::maxFrameSize()
    return Rituals.call('ritual_ZN15QWebSocketFrame12maxFrameSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocketFrame'

  #  Qt's '~QWebSocketFrame()'. Naming it makes this a value class: Python
  #  owns every C++ QWebSocketFrame behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QWebSocketFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def maxAllowedFrameSize(self) -> int:
    """
    Calls Qt's 'quint64 QWebSocketFrame::maxAllowedFrameSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketframe.html#maxAllowedFrameSize
    """
    #  quint64 QWebSocketFrame::maxAllowedFrameSize() const
    return self.uglySide.call(
        'ritual_ZNK15QWebSocketFrame19maxAllowedFrameSizeEv',
    )

  def closeCode(self) -> QWebSocketProtocol.CloseCode:
    """
    Calls Qt's 'QWebSocketProtocol::CloseCode QWebSocketFrame::closeCode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#closeCode

    Returns
    -------

    QWebSocketProtocol.CloseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.CloseCode(number)' gives.
    """
    #  QWebSocketProtocol::CloseCode QWebSocketFrame::closeCode() const
    return QWebSocketProtocol.CloseCode(self.uglySide.call(
        'ritual_ZNK15QWebSocketFrame9closeCodeEv',
    ))

  def closeReason(self) -> str:
    """
    Calls Qt's 'QString QWebSocketFrame::closeReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#closeReason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketFrame::closeReason() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame11closeReasonEv')

  def isFinalFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::isFinalFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#isFinalFrame
    """
    #  bool QWebSocketFrame::isFinalFrame() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame12isFinalFrameEv')

  def isControlFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::isControlFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketframe.html#isControlFrame
    """
    #  bool QWebSocketFrame::isControlFrame() const
    return self.uglySide.call(
        'ritual_ZNK15QWebSocketFrame14isControlFrameEv',
    )

  def isDataFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::isDataFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#isDataFrame
    """
    #  bool QWebSocketFrame::isDataFrame() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame11isDataFrameEv')

  def isContinuationFrame(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::isContinuationFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketframe.html#isContinuationFrame
    """
    #  bool QWebSocketFrame::isContinuationFrame() const
    return self.uglySide.call(
        'ritual_ZNK15QWebSocketFrame19isContinuationFrameEv',
    )

  def hasMask(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::hasMask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#hasMask
    """
    #  bool QWebSocketFrame::hasMask() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame7hasMaskEv')

  def mask(self) -> int:
    """
    Calls Qt's 'quint32 QWebSocketFrame::mask() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#mask
    """
    #  quint32 QWebSocketFrame::mask() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame4maskEv')

  def rsv1(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::rsv1() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#rsv1
    """
    #  bool QWebSocketFrame::rsv1() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame4rsv1Ev')

  def rsv2(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::rsv2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#rsv2
    """
    #  bool QWebSocketFrame::rsv2() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame4rsv2Ev')

  def rsv3(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::rsv3() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#rsv3
    """
    #  bool QWebSocketFrame::rsv3() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame4rsv3Ev')

  def opCode(self) -> QWebSocketProtocol.OpCode:
    """
    Calls Qt's 'QWebSocketProtocol::OpCode QWebSocketFrame::opCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#opCode

    Returns
    -------

    QWebSocketProtocol.OpCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.OpCode(number)' gives.
    """
    #  QWebSocketProtocol::OpCode QWebSocketFrame::opCode() const
    return QWebSocketProtocol.OpCode(self.uglySide.call(
        'ritual_ZNK15QWebSocketFrame6opCodeEv',
    ))

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebSocketFrame::payload() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebSocketFrame::payload() const
    address = self.uglySide.call('ritual_ZNK15QWebSocketFrame7payloadEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#isValid
    """
    #  bool QWebSocketFrame::isValid() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame7isValidEv')

  def isDone(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::isDone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#isDone
    """
    #  bool QWebSocketFrame::isDone() const
    return self.uglySide.call('ritual_ZNK15QWebSocketFrame6isDoneEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxAllowedFrameSize(self, maxAllowedFrameSize: int) -> None:
    """
    Calls Qt's 'void QWebSocketFrame::setMaxAllowedFrameSize(quint64
    maxAllowedFrameSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketframe.html#setMaxAllowedFrameSize

    Parameters
    ----------

    maxAllowedFrameSize : int
      Passed on as it is.
    """
    #  void QWebSocketFrame::setMaxAllowedFrameSize(quint64
    #      maxAllowedFrameSize)
    self.uglySide.call(
        'ritual_ZN15QWebSocketFrame22setMaxAllowedFrameSizeEy',
        maxAllowedFrameSize,
    )

  @overload(QWebSocketProtocol.CloseCode, str)
  def setError(
      self,
      code: QWebSocketProtocol.CloseCode,
      closeReason: str,
  ) -> None:
    """
    Calls Qt's 'void QWebSocketFrame::setError(QWebSocketProtocol::CloseCode
    code, const QString &closeReason)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#setError

    Parameters
    ----------

    code : QWebSocketProtocol.CloseCode
      Passed on as its number.

    closeReason : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketFrame::setError(QWebSocketProtocol::CloseCode code,
    #      const QString &closeReason)
    self.uglySide.call(
        'ritual_ZN15QWebSocketFrame8setErrorEN18QWebSocketProtocol9CloseCod'
        'eERK7QString',
        code.value, closeReason,
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
    Notes what was given, for Qt's 'QWebSocketFrame::QWebSocketFrame()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketframe.html#QWebSocketFrame
    """
    #  QWebSocketFrame::QWebSocketFrame()
    self._noteCreation(QWebSocketFrame, lambda: Rituals.call(
        'ritual_ZN15QWebSocketFrameC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QWebSocketFrame::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#clear
    """
    #  void QWebSocketFrame::clear()
    self.uglySide.call('ritual_ZN15QWebSocketFrame5clearEv')

  @overload(QIODevice)
  @overload(NoneType)
  def readFrame(self, pIoDevice: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QWebSocketFrame::readFrame(QIODevice *pIoDevice)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#readFrame

    Parameters
    ----------

    pIoDevice : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketFrame::readFrame(QIODevice *pIoDevice)
    self.uglySide.call(
        'ritual_ZN15QWebSocketFrame9readFrameEP9QIODevice',
        self._addressOf(pIoDevice),
    )

  def checkValidity(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketFrame::checkValidity()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketframe.html#checkValidity
    """
    #  bool QWebSocketFrame::checkValidity()
    return self.uglySide.call('ritual_ZN15QWebSocketFrame13checkValidityEv')

  @staticmethod
  def readFrameHeader(*__, **_) -> Never:
    """
    Qt's 'ProcessingState QWebSocketFrame::readFrameHeader(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QWebSocketFrame.readFrameHeader' has no cute function yet. Qt's "
        "'ProcessingState QWebSocketFrame::readFrameHeader(QIODevice "
        "*pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', "
        "whose class cannot be named here.")

  @staticmethod
  def readFrameMask(*__, **_) -> Never:
    """
    Qt's 'ProcessingState QWebSocketFrame::readFrameMask(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QWebSocketFrame.readFrameMask' has no cute function yet. Qt's "
        "'ProcessingState QWebSocketFrame::readFrameMask(QIODevice "
        "*pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', "
        "whose class cannot be named here.")

  @staticmethod
  def readFramePayload(*__, **_) -> Never:
    """
    Qt's 'ProcessingState QWebSocketFrame::readFramePayload(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QWebSocketFrame.readFramePayload' has no cute function yet. Qt's "
        "'ProcessingState QWebSocketFrame::readFramePayload(QIODevice "
        "*pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', "
        "whose class cannot be named here.")

  @staticmethod
  def readFramePayloadLength(*__, **_) -> Never:
    """
    Qt's 'ProcessingState QWebSocketFrame::readFramePayloadLength(QIODevice
    *pIoDevice)': gives the enum 'QWebSocketFrame::ProcessingState', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QWebSocketFrame.readFramePayloadLength' has no cute function yet. "
        "Qt's 'ProcessingState "
        "QWebSocketFrame::readFramePayloadLength(QIODevice *pIoDevice)': "
        "gives the enum 'QWebSocketFrame::ProcessingState', whose class "
        "cannot be named here.")
