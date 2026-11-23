"""
QBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qbuffer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QIODevice, QIODeviceBase, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QMetaMethod, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaMethod = WAIT['QMetaMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBuffer(QIODevice):
  """
  The cute side of Qt's QBuffer: a plain Python object standing in front of
  one C++ QBuffer.

  It is built on the cute 'QIODevice', as Qt's QBuffer is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBuffer that has a ritual and that Python can call
  so far, 16 names in all: 'metaObject', 'tr', 'buffer', 'setBuffer',
  'setData', 'data', 'open', 'close', 'size', 'pos', 'seek', 'atEnd',
  'canReadLine', 'connectNotify', 'disconnectNotify', 'writeData'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBuffer::~QBuffer()': the destructor: Python never removes a C++
    QBuffer.

  What has no ritual
  ------------------

  10 of the 30 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QBuffer is created at the first use, not by 'QBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBuffer.
  - Qt tells when it has removed the C++ QBuffer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QBuffer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#tr

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
    #  QString QBuffer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QBuffer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBuffer'

  #  A C++ QBuffer Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBuffer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBuffer::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QBuffer10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def buffer(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QBuffer::buffer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#buffer

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QBuffer::buffer() const
    address = self.uglySide.call('ritual_ZNK7QBuffer6bufferEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def data(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QBuffer::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QBuffer::data() const
    address = self.uglySide.call('ritual_ZNK7QBuffer4dataEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QBuffer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#size
    """
    #  qint64 QBuffer::size() const
    ritual = 'ritual_ZNK7QBuffer4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QBuffer4sizeEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QBuffer::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#pos
    """
    #  qint64 QBuffer::pos() const
    ritual = 'ritual_ZNK7QBuffer3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QBuffer3posEv'
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QBuffer::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#atEnd
    """
    #  bool QBuffer::atEnd() const
    ritual = 'ritual_ZNK7QBuffer5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QBuffer5atEndEv'
    return self.uglySide.call(ritual)

  def canReadLine(self) -> bool:
    """
    Calls Qt's 'bool QBuffer::canReadLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#canReadLine
    """
    #  bool QBuffer::canReadLine() const
    ritual = 'ritual_ZNK7QBuffer11canReadLineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QBuffer11canReadLineEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  @overload(NoneType)
  def setBuffer(self, a: Optional[QByteArray]) -> None:
    """
    Calls Qt's 'void QBuffer::setBuffer(QByteArray *a)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#setBuffer

    Parameters
    ----------

    a : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBuffer::setBuffer(QByteArray *a)
    self.uglySide.call(
        'ritual_ZN7QBuffer9setBufferEP10QByteArray', self._addressOf(a),
    )

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QBuffer::setData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QBuffer::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN7QBuffer7setDataERK10QByteArray', self._valueOf(data),
    )

  @overload(str, int)
  @overload(NoneType, int)
  def setData(self, data: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void QBuffer::setData(const char *data, qsizetype len)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#setData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QBuffer::setData(const char *data, qsizetype len)
    self.uglySide.call(
        'ritual_ZN7QBuffer7setDataEPKcx', self._bytesOf(data), len,
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
    Notes what was given, for Qt's 'QBuffer::QBuffer(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#QBuffer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBuffer::QBuffer(QObject *parent)
    self._noteCreation(QBuffer, lambda: Rituals.call(
        'ritual_ZN7QBufferC1EP7QObject', self._addressOf(parent),
    ))

  @overload(QByteArray)
  @overload(QByteArray, QObject)
  @overload(QByteArray, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      buf: Optional[QByteArray],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBuffer::QBuffer(QByteArray *buf, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#QBuffer

    Parameters
    ----------

    buf : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBuffer::QBuffer(QByteArray *buf, QObject *parent)
    self._noteCreation(QBuffer, lambda: Rituals.call(
        'ritual_ZN7QBufferC1EP10QByteArrayP7QObject',
        self._addressOf(buf), self._addressOf(parent),
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

  @overload(QIODeviceBase.OpenMode)
  def open(self, openMode: QIODeviceBase.OpenMode) -> bool:
    """
    Calls Qt's 'bool QBuffer::open(OpenMode openMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#open

    Parameters
    ----------

    openMode : QIODeviceBase.OpenMode
      Passed on as its number.
    """
    #  bool QBuffer::open(OpenMode openMode)
    ritual = (
        'ritual_ZN7QBuffer4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QBuffer4openE6QFlagsIN13QIODeviceBase12OpenModeFla'
          'gEE')
    return self.uglySide.call(ritual, openMode.value)

  def close(self) -> None:
    """
    Calls Qt's 'void QBuffer::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#close
    """
    #  void QBuffer::close()
    ritual = 'ritual_ZN7QBuffer5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QBuffer5closeEv'
    self.uglySide.call(ritual)

  @overload(int)
  def seek(self, off: int) -> bool:
    """
    Calls Qt's 'bool QBuffer::seek(qint64 off)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#seek

    Parameters
    ----------

    off : int
      Passed on as it is.
    """
    #  bool QBuffer::seek(qint64 off)
    ritual = 'ritual_ZN7QBuffer4seekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QBuffer4seekEx'
    return self.uglySide.call(ritual, off)

  @overload(QMetaMethod)
  def connectNotify(self, a0: QMetaMethod) -> None:
    """
    Calls Qt's 'void QBuffer::connectNotify(const QMetaMethod &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#connectNotify

    Parameters
    ----------

    a0 : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QBuffer::connectNotify(const QMetaMethod &a0)
    ritual = 'ritual_ZN7QBuffer13connectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QBuffer13connectNotifyERK11QMetaMethod'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QMetaMethod)
  def disconnectNotify(self, a0: QMetaMethod) -> None:
    """
    Calls Qt's 'void QBuffer::disconnectNotify(const QMetaMethod &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#disconnectNotify

    Parameters
    ----------

    a0 : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QBuffer::disconnectNotify(const QMetaMethod &a0)
    ritual = 'ritual_ZN7QBuffer16disconnectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QBuffer16disconnectNotifyERK11QMetaMethod'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(str, int)
  @overload(NoneType, int)
  def writeData(self, data: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qint64 QBuffer::writeData(const char *data, qint64 len)'.

    Qt's own words: https://doc.qt.io/qt-6/qbuffer.html#writeData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qint64 QBuffer::writeData(const char *data, qint64 len)
    return self.uglySide.call(
        'ritual_ZN7QBuffer9writeDataEPKcx', self._bytesOf(data), len,
    )
