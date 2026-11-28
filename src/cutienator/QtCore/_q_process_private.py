"""
QProcessPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QProcessPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QIODevicePrivate, QProcess

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QProcessEnvironmentPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProcessPrivate(QIODevicePrivate):
  """
  The cute side of Qt's QProcessPrivate: a plain Python object standing in
  front of one C++ QProcessPrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QProcessPrivate is
  built on Qt's QIODevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProcessPrivate that has a ritual and that Python
  can call so far, 5 names in all: 'q_func', 'commitChannels', 'setError',
  'setErrorAndEmit', 'environmentPrivate'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QProcess *QProcessPrivate::q_func() const': takes in Python
    what 'QProcess *QProcessPrivate::q_func()' takes.
  - Qt's 'QProcessPrivate::~QProcessPrivate()': the destructor: Python never
    removes a C++ QProcessPrivate.

  What has no ritual
  ------------------

  29 of the 37 functions Qt declares: 15 cannot be called and cannot be
  called through the meta-object and cannot be copied; 13 leans on
  'QProcessPrivate; 1 Qt's library has no name for it, and its code in Qt's
  source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QProcessPrivate is created at the first use, not by
    'QProcessPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProcessPrivate.
  - Each name of Qt's QProcessPrivate that has no cute function yet,
    '_q_canReadStandardError', '_q_canReadStandardOutput', '_q_canWrite',
    '_q_processDied', '_q_startupNotification', 'bytesAvailableInChannel',
    'cleanup', 'closeChannel', 'closeChannels', 'closeWriteChannel',
    'destroyPipe', 'killProcess', 'openChannel', 'openChannels',
    'openChannelsForDetached', 'processFinished', 'processStarted',
    'readFromChannel', 'start', 'startDetached', 'startProcess',
    'terminateProcess', 'tryReadFromChannel', 'waitForBytesWritten',
    'waitForDeadChild', 'waitForFinished', 'waitForReadyRead',
    'waitForStarted', 'writeToStdin', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QProcessPrivate, each a class in here as in
  #  C++.

  class Channel(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QProcessPrivate::Channel: a plain Python object
    standing in front of one C++ QProcessPrivate::Channel.

    C++ hands a QProcessPrivate::Channel around as a copy, so every C++
    QProcessPrivate::Channel behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QProcessPrivate::Channel that has a ritual and
    that Python can call so far, 3 names in all: 'clear', 'pipeTo',
    'pipeFrom'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Channel &QProcessPrivate::Channel::operator=(const QString
      &fileName)': assignment: Python binds a name and has no operator for
      it.
    - Qt's 'QProcessPrivate::Channel::~Channel()': the destructor: Python
      removes its C++ QProcessPrivate::Channel by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QProcessPrivate::Channel is created at the first use, not by
      'QProcessPrivate::Channel(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QProcessPrivate::Channel back gives a copy the
      ritual made for Python, in a new cute QProcessPrivate::Channel.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QProcessPrivate = WAIT['QProcessPrivate']

    #  The enums Qt writes inside QProcessPrivate::Channel, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class ProcessChannelType(CuteNum):
      """
      The enum 'QProcessPrivate::Channel::ProcessChannelType' of Qt, with the
      4 names Qt gives in it.
      """

      Normal = Kee[int](0)
      PipeSource = Kee[int](1)
      PipeSink = Kee[int](2)
      Redirect = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QProcessPrivate::Channel'

    #  Qt's '~QProcessPrivate::Channel()'. Naming it makes this a value
    #  class: Python owns every C++ QProcessPrivate::Channel behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QProcessPrivate7ChannelD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def clear(self) -> None:
      """
      Calls Qt's 'void QProcessPrivate::Channel::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qprocessprivate-channel.html#clear
      """
      #  void QProcessPrivate::Channel::clear()
      self.uglySide.call('ritual_ZN15QProcessPrivate7Channel5clearEv')

    @overload(QProcessPrivate)
    @overload(NoneType)
    def pipeTo(self, other: Optional[QProcessPrivate]) -> None:
      """
      Calls Qt's 'void QProcessPrivate::Channel::pipeTo(QProcessPrivate
      *other)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qprocessprivate-channel.html#pipeTo

      Parameters
      ----------

      other : Optional[QProcessPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QProcessPrivate::Channel::pipeTo(QProcessPrivate *other)
      self.uglySide.call(
          'ritual_ZN15QProcessPrivate7Channel6pipeToEPS_',
          self._addressOf(other),
      )

    @overload(QProcessPrivate)
    @overload(NoneType)
    def pipeFrom(self, other: Optional[QProcessPrivate]) -> None:
      """
      Calls Qt's 'void QProcessPrivate::Channel::pipeFrom(QProcessPrivate
      *other)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qprocessprivate-channel.html#pipeFrom

      Parameters
      ----------

      other : Optional[QProcessPrivate]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QProcessPrivate::Channel::pipeFrom(QProcessPrivate *other)
      self.uglySide.call(
          'ritual_ZN15QProcessPrivate7Channel8pipeFromEPS_',
          self._addressOf(other),
      )

  class UnixExtras(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QProcessPrivate::UnixExtras: a plain Python object
    standing in front of one C++ QProcessPrivate::UnixExtras.

    C++ hands a QProcessPrivate::UnixExtras around as a copy, so every C++
    QProcessPrivate::UnixExtras behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QProcessPrivate::UnixExtras yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QProcessPrivate::UnixExtras::~UnixExtras()': the destructor:
      Python removes its C++ QProcessPrivate::UnixExtras by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QProcessPrivate::UnixExtras is created at the first use, not by
      'QProcessPrivate::UnixExtras(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QProcessPrivate::UnixExtras back gives a copy the
      ritual made for Python, in a new cute QProcessPrivate::UnixExtras.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QProcessPrivate::UnixExtras'

    #  Qt's '~QProcessPrivate::UnixExtras()'. Naming it makes this a value
    #  class: Python owns every C++ QProcessPrivate::UnixExtras behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QProcessPrivate10UnixExtrasD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProcessPrivate'

  #  A C++ QProcessPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QProcessPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def environmentPrivate(self) -> Optional[QProcessEnvironmentPrivate]:
    """
    Calls Qt's 'const QProcessEnvironmentPrivate
    *QProcessPrivate::environmentPrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessprivate.html#environmentPrivate

    Returns
    -------

    Optional[QProcessEnvironmentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QProcessEnvironmentPrivate
    #      *QProcessPrivate::environmentPrivate() const
    address = self.uglySide.call(
        'ritual_ZNK15QProcessPrivate18environmentPrivateEv',
    )
    from . import QProcessEnvironmentPrivate
    return QProcessEnvironmentPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QProcess.ProcessError)
  @overload(QProcess.ProcessError, str)
  def setError(
      self,
      error: QProcess.ProcessError,
      description: str = '',
  ) -> None:
    """
    Calls Qt's 'void QProcessPrivate::setError(QProcess::ProcessError error,
    const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessprivate.html#setError

    Parameters
    ----------

    error : QProcess.ProcessError
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QProcessPrivate::setError(QProcess::ProcessError error, const
    #      QString &description)
    self.uglySide.call(
        'ritual_ZN15QProcessPrivate8setErrorEN8QProcess12ProcessErrorERK7QS'
        'tring',
        error.value, description,
    )

  @overload(QProcess.ProcessError)
  @overload(QProcess.ProcessError, str)
  def setErrorAndEmit(
      self,
      error: QProcess.ProcessError,
      description: str = '',
  ) -> None:
    """
    Calls Qt's 'void QProcessPrivate::setErrorAndEmit(QProcess::ProcessError
    error, const QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessprivate.html#setErrorAndEmit

    Parameters
    ----------

    error : QProcess.ProcessError
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QProcessPrivate::setErrorAndEmit(QProcess::ProcessError error,
    #      const QString &description)
    self.uglySide.call(
        'ritual_ZN15QProcessPrivate15setErrorAndEmitEN8QProcess12ProcessErr'
        'orERK7QString',
        error.value, description,
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
    Notes what was given, for Qt's 'QProcessPrivate::QProcessPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessprivate.html#QProcessPrivate
    """
    #  QProcessPrivate::QProcessPrivate()
    self._noteCreation(QProcessPrivate, lambda: Rituals.call(
        'ritual_ZN15QProcessPrivateC1Ev',
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

  def q_func(self) -> Optional[QProcess]:
    """
    Calls Qt's 'QProcess *QProcessPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessprivate.html#q_func

    Returns
    -------

    Optional[QProcess]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProcess *QProcessPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QProcessPrivate6q_funcEv')
    return QProcess._cuteAt(address)

  def commitChannels(self) -> None:
    """
    Calls Qt's 'void QProcessPrivate::commitChannels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessprivate.html#commitChannels
    """
    #  void QProcessPrivate::commitChannels() const
    self.uglySide.call('ritual_ZNK15QProcessPrivate14commitChannelsEv')

  @staticmethod
  def _q_canReadStandardError(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::_q_canReadStandardError()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate._q_canReadStandardError' has no cute function "
        "yet. Qt's 'bool QProcessPrivate::_q_canReadStandardError()': leans "
        "on 'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def _q_canReadStandardOutput(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::_q_canReadStandardOutput()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate._q_canReadStandardOutput' has no cute function "
        "yet. Qt's 'bool QProcessPrivate::_q_canReadStandardOutput()': "
        "leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def _q_canWrite(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::_q_canWrite()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate._q_canWrite' has no cute function yet. Qt's 'bool "
        "QProcessPrivate::_q_canWrite()': leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def _q_processDied(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::_q_processDied()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate._q_processDied' has no cute function yet. Qt's "
        "'void QProcessPrivate::_q_processDied()': leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def _q_startupNotification(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::_q_startupNotification()': leans on
    'QProcessPrivate::processStarted(QString*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate._q_startupNotification' has no cute function yet. "
        "Qt's 'bool QProcessPrivate::_q_startupNotification()': leans on "
        "'QProcessPrivate::processStarted(QString*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def bytesAvailableInChannel(*__, **_) -> Never:
    """
    Qt's 'qint64 QProcessPrivate::bytesAvailableInChannel(const Channel
    *channel) const': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.bytesAvailableInChannel' has no cute function "
        "yet. Qt's 'qint64 QProcessPrivate::bytesAvailableInChannel(const "
        "Channel *channel) const': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def cleanup(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::cleanup()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.cleanup' has no cute function yet. Qt's 'void "
        "QProcessPrivate::cleanup()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def closeChannel(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::closeChannel(Channel *channel)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.closeChannel' has no cute function yet. Qt's "
        "'void QProcessPrivate::closeChannel(Channel *channel)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def closeChannels(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::closeChannels()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.closeChannels' has no cute function yet. Qt's "
        "'void QProcessPrivate::closeChannels()': leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def closeWriteChannel(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::closeWriteChannel()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.closeWriteChannel' has no cute function yet. Qt's "
        "'void QProcessPrivate::closeWriteChannel()': leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def destroyPipe(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::destroyPipe(Q_PIPE *pipe)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.destroyPipe' has no cute function yet. Qt's 'void "
        "QProcessPrivate::destroyPipe(Q_PIPE *pipe)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def killProcess(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::killProcess()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.killProcess' has no cute function yet. Qt's 'void "
        "QProcessPrivate::killProcess()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def openChannel(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::openChannel(Channel &channel)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.openChannel' has no cute function yet. Qt's 'bool "
        "QProcessPrivate::openChannel(Channel &channel)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def openChannels(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::openChannels()': leans on
    'QProcessPrivate::openChannel(QProcessPrivate::Channel&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.openChannels' has no cute function yet. Qt's "
        "'bool QProcessPrivate::openChannels()': leans on "
        "'QProcessPrivate::openChannel(QProcessPrivate::Channel&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def openChannelsForDetached(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::openChannelsForDetached()': leans on
    'QProcessPrivate::openChannel(QProcessPrivate::Channel&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.openChannelsForDetached' has no cute function "
        "yet. Qt's 'bool QProcessPrivate::openChannelsForDetached()': leans "
        "on 'QProcessPrivate::openChannel(QProcessPrivate::Channel&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def processFinished(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::processFinished()': leans on
    'QProcessPrivate::cleanup()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.processFinished' has no cute function yet. Qt's "
        "'void QProcessPrivate::processFinished()': leans on "
        "'QProcessPrivate::cleanup()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def processStarted(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::processStarted(QString *errorMessage)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.processStarted' has no cute function yet. Qt's "
        "'bool QProcessPrivate::processStarted(QString *errorMessage)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def readFromChannel(*__, **_) -> Never:
    """
    Qt's 'qint64 QProcessPrivate::readFromChannel(const Channel *channel,
    char *data, qint64 maxlen)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.readFromChannel' has no cute function yet. Qt's "
        "'qint64 QProcessPrivate::readFromChannel(const Channel *channel, "
        "char *data, qint64 maxlen)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::start(QIODevice::OpenMode mode)': leans on
    'QProcessPrivate::startProcess()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.start' has no cute function yet. Qt's 'void "
        "QProcessPrivate::start(QIODevice::OpenMode mode)': leans on "
        "'QProcessPrivate::startProcess()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def startDetached(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::startDetached(qint64 *pPid)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.startDetached' has no cute function yet. Qt's "
        "'bool QProcessPrivate::startDetached(qint64 *pPid)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def startProcess(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::startProcess()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.startProcess' has no cute function yet. Qt's "
        "'void QProcessPrivate::startProcess()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def terminateProcess(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::terminateProcess()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.terminateProcess' has no cute function yet. Qt's "
        "'void QProcessPrivate::terminateProcess()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def tryReadFromChannel(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::tryReadFromChannel(Channel *channel)': leans
    on 'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.tryReadFromChannel' has no cute function yet. "
        "Qt's 'bool QProcessPrivate::tryReadFromChannel(Channel *channel)': "
        "leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def waitForBytesWritten(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::waitForBytesWritten(const QDeadlineTimer
    &deadline)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.waitForBytesWritten' has no cute function yet. "
        "Qt's 'bool QProcessPrivate::waitForBytesWritten(const "
        "QDeadlineTimer &deadline)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def waitForDeadChild(*__, **_) -> Never:
    """
    Qt's 'void QProcessPrivate::waitForDeadChild()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'forkfd_info'.
    """
    raise NotImplementedError(
        "'QProcessPrivate.waitForDeadChild' has no cute function yet. Qt's "
        "'void QProcessPrivate::waitForDeadChild()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'forkfd_info'.")

  @staticmethod
  def waitForFinished(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::waitForFinished(const QDeadlineTimer
    &deadline)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.waitForFinished' has no cute function yet. Qt's "
        "'bool QProcessPrivate::waitForFinished(const QDeadlineTimer "
        "&deadline)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def waitForReadyRead(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::waitForReadyRead(const QDeadlineTimer
    &deadline)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.waitForReadyRead' has no cute function yet. Qt's "
        "'bool QProcessPrivate::waitForReadyRead(const QDeadlineTimer "
        "&deadline)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def waitForStarted(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::waitForStarted(const QDeadlineTimer
    &deadline)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QProcessPrivate.waitForStarted' has no cute function yet. Qt's "
        "'bool QProcessPrivate::waitForStarted(const QDeadlineTimer "
        "&deadline)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def writeToStdin(*__, **_) -> Never:
    """
    Qt's 'bool QProcessPrivate::writeToStdin()': leans on
    'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QProcessPrivate.writeToStdin' has no cute function yet. Qt's "
        "'bool QProcessPrivate::writeToStdin()': leans on "
        "'QProcessPrivate::closeChannel(QProcessPrivate::Channel*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
