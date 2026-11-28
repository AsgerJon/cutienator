"""
Qt3DCore::QBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qbuffer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBuffer(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DCore::QBuffer: a plain Python object standing in
  front of one C++ Qt3DCore::QBuffer.

  It is built on the cute 'Qt3DCore::QNode', as Qt's Qt3DCore::QBuffer is
  built on Qt's Qt3DCore::QNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QBuffer that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'usage',
  'accessType', 'setData', 'data', 'updateData', 'setUsage', 'setAccessType',
  'dataChanged', 'usageChanged', 'accessTypeChanged', 'dataAvailable',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QBuffer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Qt3DCore::QBuffer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QBuffer::~QBuffer()': the destructor: Python never
    removes a C++ Qt3DCore::QBuffer.
  - Qt's 'const QBufferPrivate *Qt3DCore::QBuffer::d_func() const': takes in
    Python what 'QBufferPrivate *Qt3DCore::QBuffer::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QBuffer is created at the first use, not by
    'Qt3DCore::QBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QBuffer.
  - Qt tells when it has removed the C++ Qt3DCore::QBuffer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DCore::QBuffer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AccessType(CuteNum):
    """
    The enum 'Qt3DCore::QBuffer::AccessType' of Qt, with the 3 names Qt gives
    in it.
    """

    Write = Kee[int](1)
    Read = Kee[int](2)
    ReadWrite = Kee[int](3)

  class UsageType(CuteNum):
    """
    The enum 'Qt3DCore::QBuffer::UsageType' of Qt, with the 9 names Qt gives
    in it.
    """

    StreamDraw = Kee[int](35040)
    StreamRead = Kee[int](35041)
    StreamCopy = Kee[int](35042)
    StaticDraw = Kee[int](35044)
    StaticRead = Kee[int](35045)
    StaticCopy = Kee[int](35046)
    DynamicDraw = Kee[int](35048)
    DynamicRead = Kee[int](35049)
    DynamicCopy = Kee[int](35050)

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
    Calls Qt's 'QString Qt3DCore::QBuffer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#tr

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
    #  QString Qt3DCore::QBuffer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore7QBuffer2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QBuffer'

  #  A C++ Qt3DCore::QBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QBuffer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QBuffer::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore7QBuffer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def usage(self) -> UsageType:
    """
    Calls Qt's 'UsageType Qt3DCore::QBuffer::usage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#usage

    Returns
    -------

    UsageType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UsageType(number)' gives.
    """
    #  UsageType Qt3DCore::QBuffer::usage() const
    return QBuffer.UsageType(self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QBuffer5usageEv',
    ))

  def accessType(self) -> AccessType:
    """
    Calls Qt's 'AccessType Qt3DCore::QBuffer::accessType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#accessType

    Returns
    -------

    AccessType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AccessType(number)'
      gives.
    """
    #  AccessType Qt3DCore::QBuffer::accessType() const
    return QBuffer.AccessType(self.uglySide.call(
        'ritual_ZNK8Qt3DCore7QBuffer10accessTypeEv',
    ))

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DCore::QBuffer::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DCore::QBuffer::data() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore7QBuffer4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setData(self, bytes: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::setData(const QByteArray &bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#setData

    Parameters
    ----------

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DCore::QBuffer::setData(const QByteArray &bytes)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer7setDataERK10QByteArray',
        self._valueOf(bytes),
    )

  @overload(UsageType)
  def setUsage(self, usage: UsageType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::setUsage(UsageType usage)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#setUsage

    Parameters
    ----------

    usage : UsageType
      Passed on as its number.
    """
    #  void Qt3DCore::QBuffer::setUsage(UsageType usage)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer8setUsageENS0_9UsageTypeE', usage.value,
    )

  @overload(AccessType)
  def setAccessType(self, access: AccessType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::setAccessType(AccessType access)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#setAccessType

    Parameters
    ----------

    access : AccessType
      Passed on as its number.
    """
    #  void Qt3DCore::QBuffer::setAccessType(AccessType access)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer13setAccessTypeENS0_10AccessTypeE',
        access.value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QBuffer::QBuffer(Qt3DCore::QNode *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#QBuffer

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QBuffer::QBuffer(Qt3DCore::QNode *parent)
    self._noteCreation(QBuffer, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore7QBufferC1EPNS_5QNodeE', self._addressOf(parent),
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

  @overload(int, QByteArray)
  def updateData(self, offset: int, bytes: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::updateData(int offset, const
    QByteArray &bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#updateData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DCore::QBuffer::updateData(int offset, const QByteArray
    #      &bytes)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer10updateDataEiRK10QByteArray',
        offset, self._valueOf(bytes),
    )

  @overload(QByteArray)
  def dataChanged(self, bytes: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::dataChanged(const QByteArray
    &bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#dataChanged

    Parameters
    ----------

    bytes : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DCore::QBuffer::dataChanged(const QByteArray &bytes)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer11dataChangedERK10QByteArray',
        self._valueOf(bytes),
    )

  @overload(UsageType)
  def usageChanged(self, usage: UsageType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::usageChanged(UsageType usage)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#usageChanged

    Parameters
    ----------

    usage : UsageType
      Passed on as its number.
    """
    #  void Qt3DCore::QBuffer::usageChanged(UsageType usage)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer12usageChangedENS0_9UsageTypeE',
        usage.value,
    )

  @overload(AccessType)
  def accessTypeChanged(self, access: AccessType) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::accessTypeChanged(AccessType
    access)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#accessTypeChanged

    Parameters
    ----------

    access : AccessType
      Passed on as its number.
    """
    #  void Qt3DCore::QBuffer::accessTypeChanged(AccessType access)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore7QBuffer17accessTypeChangedENS0_10AccessTypeE',
        access.value,
    )

  def dataAvailable(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBuffer::dataAvailable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#dataAvailable
    """
    #  void Qt3DCore::QBuffer::dataAvailable()
    self.uglySide.call('ritual_ZN8Qt3DCore7QBuffer13dataAvailableEv')

  def d_func(self) -> Optional[Qt3DCore.QBufferPrivate]:
    """
    Calls Qt's 'QBufferPrivate *Qt3DCore::QBuffer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbuffer.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QBufferPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBufferPrivate *Qt3DCore::QBuffer::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore7QBuffer6d_funcEv')
    return Qt3DCore.QBufferPrivate._cuteAt(address)
