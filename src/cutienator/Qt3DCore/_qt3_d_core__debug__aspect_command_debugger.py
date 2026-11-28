"""
Qt3DCore::Debug::AspectCommandDebugger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/aspectcommanddebugger_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Debug::AspectCommandDebugger to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtNetwork import QTcpServer
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtNetwork import QTcpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QTcpSocket = WAIT['QTcpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AspectCommandDebugger(QTcpServer):
  """
  The cute side of Qt's Qt3DCore::Debug::AspectCommandDebugger: a plain
  Python object standing in front of one C++
  Qt3DCore::Debug::AspectCommandDebugger.

  It is built on the cute 'QTcpServer', as Qt's
  Qt3DCore::Debug::AspectCommandDebugger is built on Qt's QTcpServer, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Debug::AspectCommandDebugger that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'initialize', 'asynchronousReplyFinished', 'sendReply',
  'onCommandReceived', 'executeCommand'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Debug::AspectCommandDebugger::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::Debug::AspectCommandDebugger::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Debug::AspectCommandDebugger is created at the first
    use, not by 'Qt3DCore::Debug::AspectCommandDebugger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Debug::AspectCommandDebugger.
  - Qt tells when it has removed the C++
    Qt3DCore::Debug::AspectCommandDebugger. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  #  The classes Qt writes inside Qt3DCore::Debug::AspectCommandDebugger,
  #  each a class in here as in C++.

  class ReadBuffer(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer:
    a plain Python object standing in front of one C++
    Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer.

    C++ hands a Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer around as
    a copy, so every C++ Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer
    that has a ritual and that Python can call so far, 3 names in all:
    'size', 'insert', 'trim'. None can be made from Python: one comes out of
    a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::~ReadBuffer()':
      the destructor: Python removes its C++
      Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer is created
      at the first use, not by
      'Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer
      back gives a copy the ritual made for Python, in a new cute
      Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer'

    #  Qt's '~Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer()'. Naming
    #  it makes this a value class: Python owns every C++
    #  Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10ReadBufferD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def size(self) -> int:
      """
      Calls Qt's 'qsizetype
      Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::size() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger-readbuffer.html
      """
      #  qsizetype Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::size()
      #      const
      return self.uglySide.call(
          'ritual_ZNK8Qt3DCore5Debug21AspectCommandDebugger10ReadBuffer4siz'
          'eEv',
      )

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

    @overload(QByteArray)
    def insert(self, array: QByteArray) -> None:
      """
      Calls Qt's 'void
      Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::insert(const
      QByteArray &array)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger-readbuffer.html

      Parameters
      ----------

      array : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.
      """
      #  void
      #      Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::insert(const
      #      QByteArray &array)
      self.uglySide.call(
          'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10ReadBuffer6inse'
          'rtERK10QByteArray',
          self._valueOf(array),
      )

    def trim(self) -> None:
      """
      Calls Qt's 'void
      Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::trim()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger-readbuffer.html
      """
      #  void Qt3DCore::Debug::AspectCommandDebugger::ReadBuffer::trim()
      self.uglySide.call(
          'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10ReadBuffer4trim'
          'Ev',
      )

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
    Calls Qt's 'QString Qt3DCore::Debug::AspectCommandDebugger::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html#tr

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
    #  QString Qt3DCore::Debug::AspectCommandDebugger::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Debug::AspectCommandDebugger'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::Debug::AspectCommandDebugger::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DCore::Debug::AspectCommandDebugger::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Debug21AspectCommandDebugger10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(WAIT['Qt3DCore.QSystemInformationService'])
  @overload(NoneType)
  def __init__(
      self,
      parent: Optional[Qt3DCore.QSystemInformationService] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::Debug::AspectCommandDebugger::AspectCommandDebugger(
    QSystemInformationService *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QSystemInformationService]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Debug::AspectCommandDebugger::AspectCommandDebugger(
    #      QSystemInformationService *parent)
    self._noteCreation(AspectCommandDebugger, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebuggerC1EPNS_25QSystemInf'
        'ormationServiceE',
        self._addressOf(parent),
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::Debug::AspectCommandDebugger::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html
    """
    #  void Qt3DCore::Debug::AspectCommandDebugger::initialize()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger10initializeEv',
    )

  @overload(WAIT['Qt3DCore.Debug.AsynchronousCommandReply'])
  @overload(NoneType)
  def asynchronousReplyFinished(
      self,
      reply: Optional[Qt3DCore.Debug.AsynchronousCommandReply],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Debug::AspectCommandDebugger::asynchronousReplyFinished(
    AsynchronousCommandReply *reply)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html

    Parameters
    ----------

    reply : Optional[Qt3DCore.Debug.AsynchronousCommandReply]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DCore::Debug::AspectCommandDebugger::asynchronousReplyFinished(
    #      AsynchronousCommandReply *reply)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger25asynchronousReply'
        'FinishedEPNS0_24AsynchronousCommandReplyE',
        self._addressOf(reply),
    )

  @overload(QTcpSocket, QByteArray)
  @overload(NoneType, QByteArray)
  def sendReply(
      self,
      socket: Optional[QTcpSocket],
      data: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Debug::AspectCommandDebugger::sendReply(QTcpSocket *socket,
    const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html

    Parameters
    ----------

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DCore::Debug::AspectCommandDebugger::sendReply(QTcpSocket
    #      *socket, const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger9sendReplyEP10QTcpS'
        'ocketRK10QByteArray',
        self._addressOf(socket), self._valueOf(data),
    )

  @overload(QTcpSocket)
  @overload(NoneType)
  def onCommandReceived(self, socket: Optional[QTcpSocket]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Debug::AspectCommandDebugger::onCommandReceived(QTcpSocket
    *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html

    Parameters
    ----------

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Debug::AspectCommandDebugger::onCommandReceived(
    #      QTcpSocket *socket)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger17onCommandReceived'
        'EP10QTcpSocket',
        self._addressOf(socket),
    )

  @overload(str, QTcpSocket)
  @overload(str, NoneType)
  def executeCommand(
      self,
      command: str,
      socket: Optional[QTcpSocket],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Debug::AspectCommandDebugger::executeCommand(const QString
    &command, QTcpSocket *socket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-debug-aspectcommanddebugger.html

    Parameters
    ----------

    command : str
      Passed on as it is: a QString is made of it for the call.

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Debug::AspectCommandDebugger::executeCommand(const
    #      QString &command, QTcpSocket *socket)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Debug21AspectCommandDebugger14executeCommandERK'
        '7QStringP10QTcpSocket',
        command, self._addressOf(socket),
    )
