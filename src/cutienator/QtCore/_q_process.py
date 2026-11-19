"""
QProcess binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ._q_byte_array import QByteArray
from ._q_i_o_device import QIODevice
from ._q_i_o_device_base import QIODeviceBase
from ._q_meta_object import QMetaObject
from ._q_object import QObject
from ._q_process_exit_status import ExitStatus
from ._q_process_input_channel_mode import InputChannelMode
from ._q_process_process_channel import ProcessChannel
from ._q_process_process_channel_mode import ProcessChannelMode
from ._q_process_process_error import ProcessError
from ._q_process_process_state import ProcessState
from ._q_process_unix_process_flag import UnixProcessFlag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProcess(QIODevice):
  """
  The cute side of Qt's QProcess: a plain Python object standing in front of
  one C++ QProcess.

  It is built on the cute 'QIODevice', as Qt's QProcess is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProcess that has a ritual and that Python can call
  so far, 40 names in all: 'metaObject', 'tr', 'start', 'startCommand',
  'open', 'program', 'setProgram', 'processChannelMode',
  'setProcessChannelMode', 'inputChannelMode', 'setInputChannelMode',
  'readChannel', 'setReadChannel', 'closeReadChannel', 'closeWriteChannel',
  'setStandardInputFile', 'setStandardOutputFile', 'setStandardErrorFile',
  'setStandardOutputProcess', 'failChildProcessModifier',
  'setUnixProcessParameters', 'workingDirectory', 'setWorkingDirectory',
  'error', 'state', 'processId', 'waitForStarted', 'waitForReadyRead',
  'waitForBytesWritten', 'waitForFinished', 'readAllStandardOutput',
  'readAllStandardError', 'exitCode', 'exitStatus', 'bytesToWrite',
  'isSequential', 'close', 'nullDevice', 'terminate', 'kill'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProcess::~QProcess()': the destructor: Python never removes a C++
    QProcess.
  - Qt's 'bool QProcess::startDetached(qint64 *pid)': takes a number to
    change where it is.
  - Qt's 'UnixProcessParameters QProcess::unixProcessParameters() const':
    gives 'QProcess::UnixProcessParameters', which has no cute class yet.
  - Qt's 'void QProcess::setUnixProcessParameters(const UnixProcessParameters
    &params)': names 'QProcess::UnixProcessParameters', which has no cute
    class yet.
  - Qt's 'void QProcess::setProcessEnvironment(const QProcessEnvironment
    &environment)': names 'QProcessEnvironment', which has no cute class yet.
  - Qt's 'QProcessEnvironment QProcess::processEnvironment() const': gives
    'QProcessEnvironment', which has no cute class yet.

  What has no ritual
  ------------------

  29 of the 76 functions Qt declares: 13 takes or gives a type that cannot be
  passed yet; 6 a signal; 4 private; 3 protected; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QProcess is created at the first use, not by 'QProcess(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProcess.
  - Qt tells when it has removed the C++ QProcess. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QProcess, and the names Qt has for the
  #  combinations of its flags enums.
  ExitStatus = ExitStatus
  InputChannelMode = InputChannelMode
  ProcessChannel = ProcessChannel
  ProcessChannelMode = ProcessChannelMode
  ProcessError = ProcessError
  ProcessState = ProcessState
  UnixProcessFlag = UnixProcessFlag
  UnixProcessFlags = UnixProcessFlag

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
    Calls Qt's 'QString QProcess::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#tr

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
    #  QString QProcess::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QProcess2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def nullDevice() -> str:
    """
    Calls Qt's 'QString QProcess::nullDevice()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#nullDevice

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcess::nullDevice()
    return Rituals.call('ritual_ZN8QProcess10nullDeviceEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProcess'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QProcess::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QProcess::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QProcess10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def program(self) -> str:
    """
    Calls Qt's 'QString QProcess::program() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#program

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcess::program() const
    return self.uglySide.call('ritual_ZNK8QProcess7programEv')

  def processChannelMode(self) -> ProcessChannelMode:
    """
    Calls Qt's 'ProcessChannelMode QProcess::processChannelMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#processChannelMode

    Returns
    -------

    ProcessChannelMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ProcessChannelMode(number)' gives.
    """
    #  ProcessChannelMode QProcess::processChannelMode() const
    return ProcessChannelMode(self.uglySide.call(
        'ritual_ZNK8QProcess18processChannelModeEv',
    ))

  def inputChannelMode(self) -> InputChannelMode:
    """
    Calls Qt's 'InputChannelMode QProcess::inputChannelMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#inputChannelMode

    Returns
    -------

    InputChannelMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InputChannelMode(number)'
      gives.
    """
    #  InputChannelMode QProcess::inputChannelMode() const
    return InputChannelMode(self.uglySide.call(
        'ritual_ZNK8QProcess16inputChannelModeEv',
    ))

  def readChannel(self) -> ProcessChannel:
    """
    Calls Qt's 'ProcessChannel QProcess::readChannel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#readChannel

    Returns
    -------

    ProcessChannel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProcessChannel(number)'
      gives.
    """
    #  ProcessChannel QProcess::readChannel() const
    return ProcessChannel(self.uglySide.call(
        'ritual_ZNK8QProcess11readChannelEv',
    ))

  def workingDirectory(self) -> str:
    """
    Calls Qt's 'QString QProcess::workingDirectory() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#workingDirectory

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcess::workingDirectory() const
    return self.uglySide.call('ritual_ZNK8QProcess16workingDirectoryEv')

  def error(self) -> ProcessError:
    """
    Calls Qt's 'QProcess::ProcessError QProcess::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#error

    Returns
    -------

    ProcessError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProcessError(number)'
      gives.
    """
    #  QProcess::ProcessError QProcess::error() const
    return ProcessError(self.uglySide.call('ritual_ZNK8QProcess5errorEv'))

  def state(self) -> ProcessState:
    """
    Calls Qt's 'QProcess::ProcessState QProcess::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#state

    Returns
    -------

    ProcessState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProcessState(number)'
      gives.
    """
    #  QProcess::ProcessState QProcess::state() const
    return ProcessState(self.uglySide.call('ritual_ZNK8QProcess5stateEv'))

  def processId(self) -> int:
    """
    Calls Qt's 'qint64 QProcess::processId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#processId
    """
    #  qint64 QProcess::processId() const
    return self.uglySide.call('ritual_ZNK8QProcess9processIdEv')

  def exitCode(self) -> int:
    """
    Calls Qt's 'int QProcess::exitCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#exitCode
    """
    #  int QProcess::exitCode() const
    return self.uglySide.call('ritual_ZNK8QProcess8exitCodeEv')

  def exitStatus(self) -> ExitStatus:
    """
    Calls Qt's 'QProcess::ExitStatus QProcess::exitStatus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#exitStatus

    Returns
    -------

    ExitStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ExitStatus(number)'
      gives.
    """
    #  QProcess::ExitStatus QProcess::exitStatus() const
    return ExitStatus(self.uglySide.call(
        'ritual_ZNK8QProcess10exitStatusEv',
    ))

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QProcess::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#bytesToWrite
    """
    #  qint64 QProcess::bytesToWrite() const
    return self.uglySide.call('ritual_ZNK8QProcess12bytesToWriteEv')

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QProcess::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#isSequential
    """
    #  bool QProcess::isSequential() const
    return self.uglySide.call('ritual_ZNK8QProcess12isSequentialEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setProgram(self, program: str) -> None:
    """
    Calls Qt's 'void QProcess::setProgram(const QString &program)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#setProgram

    Parameters
    ----------

    program : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProcess::setProgram(const QString &program)
    self.uglySide.call('ritual_ZN8QProcess10setProgramERK7QString', program)

  @overload(ProcessChannelMode)
  def setProcessChannelMode(self, mode: ProcessChannelMode) -> None:
    """
    Calls Qt's 'void QProcess::setProcessChannelMode(ProcessChannelMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocess.html#setProcessChannelMode

    Parameters
    ----------

    mode : ProcessChannelMode
      Passed on as its number.
    """
    #  void QProcess::setProcessChannelMode(ProcessChannelMode mode)
    self.uglySide.call(
        'ritual_ZN8QProcess21setProcessChannelModeENS_18ProcessChannelModeE',
        mode.value,
    )

  @overload(InputChannelMode)
  def setInputChannelMode(self, mode: InputChannelMode) -> None:
    """
    Calls Qt's 'void QProcess::setInputChannelMode(InputChannelMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#setInputChannelMode

    Parameters
    ----------

    mode : InputChannelMode
      Passed on as its number.
    """
    #  void QProcess::setInputChannelMode(InputChannelMode mode)
    self.uglySide.call(
        'ritual_ZN8QProcess19setInputChannelModeENS_16InputChannelModeE',
        mode.value,
    )

  @overload(ProcessChannel)
  def setReadChannel(self, channel: ProcessChannel) -> None:
    """
    Calls Qt's 'void QProcess::setReadChannel(ProcessChannel channel)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#setReadChannel

    Parameters
    ----------

    channel : ProcessChannel
      Passed on as its number.
    """
    #  void QProcess::setReadChannel(ProcessChannel channel)
    self.uglySide.call(
        'ritual_ZN8QProcess14setReadChannelENS_14ProcessChannelE',
        channel.value,
    )

  @overload(str)
  def setStandardInputFile(self, fileName: str) -> None:
    """
    Calls Qt's 'void QProcess::setStandardInputFile(const QString
    &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#setStandardInputFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProcess::setStandardInputFile(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN8QProcess20setStandardInputFileERK7QString', fileName,
    )

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def setStandardOutputFile(
      self,
      fileName: str,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.Truncate,
  ) -> None:
    """
    Calls Qt's 'void QProcess::setStandardOutputFile(const QString &fileName,
    OpenMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocess.html#setStandardOutputFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.Truncate.
    """
    #  void QProcess::setStandardOutputFile(const QString &fileName, OpenMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN8QProcess21setStandardOutputFileERK7QString6QFlagsIN13QIO'
        'DeviceBase12OpenModeFlagEE',
        fileName, mode.value,
    )

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def setStandardErrorFile(
      self,
      fileName: str,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.Truncate,
  ) -> None:
    """
    Calls Qt's 'void QProcess::setStandardErrorFile(const QString &fileName,
    OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#setStandardErrorFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.Truncate.
    """
    #  void QProcess::setStandardErrorFile(const QString &fileName, OpenMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN8QProcess20setStandardErrorFileERK7QString6QFlagsIN13QIOD'
        'eviceBase12OpenModeFlagEE',
        fileName, mode.value,
    )

  @overload(THIS)
  @overload(NoneType)
  def setStandardOutputProcess(
      self,
      destination: Optional[QProcess],
  ) -> None:
    """
    Calls Qt's 'void QProcess::setStandardOutputProcess(QProcess
    *destination)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocess.html#setStandardOutputProcess

    Parameters
    ----------

    destination : Optional[QProcess]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProcess::setStandardOutputProcess(QProcess *destination)
    self.uglySide.call(
        'ritual_ZN8QProcess24setStandardOutputProcessEPS_',
        self._addressOf(destination),
    )

  @overload(UnixProcessFlags)
  def setUnixProcessParameters(self, flagsOnly: UnixProcessFlags) -> None:
    """
    Calls Qt's 'void QProcess::setUnixProcessParameters(UnixProcessFlags
    flagsOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocess.html#setUnixProcessParameters

    Parameters
    ----------

    flagsOnly : UnixProcessFlags
      Passed on as its number.
    """
    #  void QProcess::setUnixProcessParameters(UnixProcessFlags flagsOnly)
    self.uglySide.call(
        'ritual_ZN8QProcess24setUnixProcessParametersE6QFlagsINS_15UnixProc'
        'essFlagEE',
        flagsOnly.value,
    )

  @overload(str)
  def setWorkingDirectory(self, dir: str) -> None:
    """
    Calls Qt's 'void QProcess::setWorkingDirectory(const QString &dir)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#setWorkingDirectory

    Parameters
    ----------

    dir : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProcess::setWorkingDirectory(const QString &dir)
    self.uglySide.call(
        'ritual_ZN8QProcess19setWorkingDirectoryERK7QString', dir,
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
    Notes what was given, for Qt's 'QProcess::QProcess(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#QProcess

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QProcess::QProcess(QObject *parent)
    self._noteCreation(QProcess, lambda: Rituals.call(
        'ritual_ZN8QProcessC1EP7QObject', self._addressOf(parent),
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

  @overload()
  @overload(QIODeviceBase.OpenMode)
  def start(
      self,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QProcess::start(OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#start

    Parameters
    ----------

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QProcess::start(OpenMode mode)
    self.uglySide.call(
        'ritual_ZN8QProcess5startE6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        mode.value,
    )

  @overload(str)
  @overload(str, QIODeviceBase.OpenMode)
  def startCommand(
      self,
      command: str,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> None:
    """
    Calls Qt's 'void QProcess::startCommand(const QString &command, OpenMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#startCommand

    Parameters
    ----------

    command : str
      Passed on as it is: a QString is made of it for the call.

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  void QProcess::startCommand(const QString &command, OpenMode mode)
    self.uglySide.call(
        'ritual_ZN8QProcess12startCommandERK7QString6QFlagsIN13QIODeviceBas'
        'e12OpenModeFlagEE',
        command, mode.value,
    )

  @overload()
  @overload(QIODeviceBase.OpenMode)
  def open(
      self,
      mode: QIODeviceBase.OpenMode = QIODeviceBase.OpenMode.ReadWrite,
  ) -> bool:
    """
    Calls Qt's 'bool QProcess::open(OpenMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#open

    Parameters
    ----------

    mode : QIODeviceBase.OpenMode
      Passed on as its number. May be left out, as in Qt: it is then
      QIODeviceBase.OpenMode.ReadWrite.
    """
    #  bool QProcess::open(OpenMode mode)
    return self.uglySide.call(
        'ritual_ZN8QProcess4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE',
        mode.value,
    )

  @overload(ProcessChannel)
  def closeReadChannel(self, channel: ProcessChannel) -> None:
    """
    Calls Qt's 'void QProcess::closeReadChannel(ProcessChannel channel)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#closeReadChannel

    Parameters
    ----------

    channel : ProcessChannel
      Passed on as its number.
    """
    #  void QProcess::closeReadChannel(ProcessChannel channel)
    self.uglySide.call(
        'ritual_ZN8QProcess16closeReadChannelENS_14ProcessChannelE',
        channel.value,
    )

  def closeWriteChannel(self) -> None:
    """
    Calls Qt's 'void QProcess::closeWriteChannel()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#closeWriteChannel
    """
    #  void QProcess::closeWriteChannel()
    self.uglySide.call('ritual_ZN8QProcess17closeWriteChannelEv')

  @overload(str)
  @overload(NoneType)
  @overload(str, int)
  @overload(NoneType, int)
  def failChildProcessModifier(
      self,
      description: Optional[str],
      error: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QProcess::failChildProcessModifier(const char
    *description, int error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocess.html#failChildProcessModifier

    Parameters
    ----------

    description : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    error : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QProcess::failChildProcessModifier(const char *description, int
    #      error)
    self.uglySide.call(
        'ritual_ZN8QProcess24failChildProcessModifierEPKci',
        self._bytesOf(description), error,
    )

  @overload()
  @overload(int)
  def waitForStarted(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QProcess::waitForStarted(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#waitForStarted

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QProcess::waitForStarted(int msecs)
    return self.uglySide.call('ritual_ZN8QProcess14waitForStartedEi', msecs)

  @overload()
  @overload(int)
  def waitForReadyRead(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QProcess::waitForReadyRead(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#waitForReadyRead

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QProcess::waitForReadyRead(int msecs)
    return self.uglySide.call(
        'ritual_ZN8QProcess16waitForReadyReadEi', msecs,
    )

  @overload()
  @overload(int)
  def waitForBytesWritten(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QProcess::waitForBytesWritten(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#waitForBytesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QProcess::waitForBytesWritten(int msecs)
    return self.uglySide.call(
        'ritual_ZN8QProcess19waitForBytesWrittenEi', msecs,
    )

  @overload()
  @overload(int)
  def waitForFinished(self, msecs: int = 30000) -> bool:
    """
    Calls Qt's 'bool QProcess::waitForFinished(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#waitForFinished

    Parameters
    ----------

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 30000.
    """
    #  bool QProcess::waitForFinished(int msecs)
    return self.uglySide.call('ritual_ZN8QProcess15waitForFinishedEi', msecs)

  def readAllStandardOutput(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QProcess::readAllStandardOutput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocess.html#readAllStandardOutput

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QProcess::readAllStandardOutput()
    address = self.uglySide.call(
        'ritual_ZN8QProcess21readAllStandardOutputEv',
    )
    return QByteArray._cuteOwning(address)

  def readAllStandardError(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QProcess::readAllStandardError()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#readAllStandardError

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QProcess::readAllStandardError()
    address = self.uglySide.call(
        'ritual_ZN8QProcess20readAllStandardErrorEv',
    )
    return QByteArray._cuteOwning(address)

  def close(self) -> None:
    """
    Calls Qt's 'void QProcess::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#close
    """
    #  void QProcess::close()
    self.uglySide.call('ritual_ZN8QProcess5closeEv')

  def terminate(self) -> None:
    """
    Calls Qt's 'void QProcess::terminate()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#terminate
    """
    #  void QProcess::terminate()
    self.uglySide.call('ritual_ZN8QProcess9terminateEv')

  def kill(self) -> None:
    """
    Calls Qt's 'void QProcess::kill()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocess.html#kill
    """
    #  void QProcess::kill()
    self.uglySide.call('ritual_ZN8QProcess4killEv')
