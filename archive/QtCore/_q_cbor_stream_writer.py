"""
QCborStreamWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcborstreamwriter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QByteArrayView, QIODevice, QLatin1String
  from . import qfloat16
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QIODevice = WAIT['QIODevice']
  QLatin1String = WAIT['QLatin1String']
  qfloat16 = WAIT['qfloat16']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCborStreamWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCborStreamWriter: a plain Python object standing in
  front of one C++ QCborStreamWriter.

  What exists
  -----------

  Every function of Qt's QCborStreamWriter that has a ritual and that Python
  can call so far, 11 names in all: 'setDevice', 'device', 'append',
  'appendByteString', 'appendTextString', 'appendNull', 'appendUndefined',
  'startArray', 'endArray', 'startMap', 'endMap'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborStreamWriter::~QCborStreamWriter()': the destructor: Python
    never removes a C++ QCborStreamWriter.
  - Qt's 'void QCborStreamWriter::append(qint64 i)': takes in Python what
    'void QCborStreamWriter::append(quint64 u)' takes.
  - Qt's 'void QCborStreamWriter::append(QCborNegativeInteger n)': names the
    enum 'QCborNegativeInteger', whose class cannot be named here.
  - Qt's 'void QCborStreamWriter::append(QCborTag tag)': names the enum
    'QCborTag', whose class cannot be named here.
  - Qt's 'void QCborStreamWriter::append(QCborKnownTags tag)': names the enum
    'QCborKnownTags', whose class cannot be named here.
  - Qt's 'void QCborStreamWriter::append(QCborSimpleType st)': names the enum
    'QCborSimpleType', whose class cannot be named here.
  - Qt's 'void QCborStreamWriter::append(double d)': takes in Python what
    'void QCborStreamWriter::append(float f)' takes.
  - Qt's 'void QCborStreamWriter::append(int i)': takes in Python what 'void
    QCborStreamWriter::append(quint64 u)' takes.
  - Qt's 'void QCborStreamWriter::append(uint u)': takes in Python what 'void
    QCborStreamWriter::append(quint64 u)' takes.

  What has no ritual
  ------------------

  5 of the 36 functions Qt declares: 2 forbidden; 2 takes or gives a type
  that cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QCborStreamWriter is created at the first use, not by
    'QCborStreamWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCborStreamWriter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborStreamWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QCborStreamWriter::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QCborStreamWriter::device() const
    address = self.uglySide.call('ritual_ZNK17QCborStreamWriter6deviceEv')
    from . import QIODevice
    return QIODevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCborStreamWriter::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter9setDeviceEP9QIODevice',
        self._addressOf(device),
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

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's
    'QCborStreamWriter::QCborStreamWriter(QIODevice *device)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamwriter.html#QCborStreamWriter

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCborStreamWriter::QCborStreamWriter(QIODevice *device)
    self._noteCreation(QCborStreamWriter, lambda: Rituals.call(
        'ritual_ZN17QCborStreamWriterC1EP9QIODevice',
        self._addressOf(device),
    ))

  @overload(QByteArray)
  def __init__(self, data: Optional[QByteArray]) -> None:
    """
    Notes what was given, for Qt's
    'QCborStreamWriter::QCborStreamWriter(QByteArray *data)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamwriter.html#QCborStreamWriter

    Parameters
    ----------

    data : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCborStreamWriter::QCborStreamWriter(QByteArray *data)
    self._noteCreation(QCborStreamWriter, lambda: Rituals.call(
        'ritual_ZN17QCborStreamWriterC1EP10QByteArray',
        self._addressOf(data),
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

  @overload(int)
  def append(self, u: int) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(quint64 u)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    u : int
      Passed on as it is.
    """
    #  void QCborStreamWriter::append(quint64 u)
    self.uglySide.call('ritual_ZN17QCborStreamWriter6appendEy', u)

  @overload(QByteArrayView)
  def append(self, ba: QByteArrayView) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(QByteArrayView ba)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    ba : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QCborStreamWriter::append(QByteArrayView ba)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter6appendE14QByteArrayView',
        self._valueOf(ba),
    )

  @overload(QLatin1String)
  def append(self, str: QLatin1String) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(QLatin1StringView str)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    str : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QCborStreamWriter::append(QLatin1StringView str)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter6appendE13QLatin1String',
        self._valueOf(str),
    )

  @overload(str)
  def append(self, str: str) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(QStringView str)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCborStreamWriter::append(QStringView str)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter6appendE11QStringView', str,
    )

  @overload(qfloat16)
  def append(self, f: qfloat16) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(qfloat16 f)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    f : qfloat16
      Passed on as a value: Qt reads the C++ qfloat16, which stays Python's
      own.
    """
    #  void QCborStreamWriter::append(qfloat16 f)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter6appendE8qfloat16', self._valueOf(f),
    )

  @overload(float)
  def append(self, f: float) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(float f)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  void QCborStreamWriter::append(float f)
    self.uglySide.call('ritual_ZN17QCborStreamWriter6appendEf', f)

  @overload(bool)
  def append(self, b: bool) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QCborStreamWriter::append(bool b)
    self.uglySide.call('ritual_ZN17QCborStreamWriter6appendEb', b)

  @overload(NoneType)
  @overload(str, int)
  @overload(NoneType, int)
  def append(self, str: Optional[str], size: int = -1) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::append(const char *str, qsizetype
    size)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#append

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QCborStreamWriter::append(const char *str, qsizetype size)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter6appendEPKcx', self._bytesOf(str), size,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def appendByteString(self, data: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::appendByteString(const char *data,
    qsizetype len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamwriter.html#appendByteString

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QCborStreamWriter::appendByteString(const char *data, qsizetype
    #      len)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter16appendByteStringEPKcx',
        self._bytesOf(data), len,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def appendTextString(self, utf8: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::appendTextString(const char *utf8,
    qsizetype len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamwriter.html#appendTextString

    Parameters
    ----------

    utf8 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QCborStreamWriter::appendTextString(const char *utf8, qsizetype
    #      len)
    self.uglySide.call(
        'ritual_ZN17QCborStreamWriter16appendTextStringEPKcx',
        self._bytesOf(utf8), len,
    )

  def appendNull(self) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::appendNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#appendNull
    """
    #  void QCborStreamWriter::appendNull()
    self.uglySide.call('ritual_ZN17QCborStreamWriter10appendNullEv')

  def appendUndefined(self) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::appendUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborstreamwriter.html#appendUndefined
    """
    #  void QCborStreamWriter::appendUndefined()
    self.uglySide.call('ritual_ZN17QCborStreamWriter15appendUndefinedEv')

  @overload()
  def startArray(self) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::startArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#startArray
    """
    #  void QCborStreamWriter::startArray()
    self.uglySide.call('ritual_ZN17QCborStreamWriter10startArrayEv')

  @overload(int)
  def startArray(self, count: int) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::startArray(quint64 count)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#startArray

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QCborStreamWriter::startArray(quint64 count)
    self.uglySide.call('ritual_ZN17QCborStreamWriter10startArrayEy', count)

  def endArray(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamWriter::endArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#endArray
    """
    #  bool QCborStreamWriter::endArray()
    return self.uglySide.call('ritual_ZN17QCborStreamWriter8endArrayEv')

  @overload()
  def startMap(self) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::startMap()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#startMap
    """
    #  void QCborStreamWriter::startMap()
    self.uglySide.call('ritual_ZN17QCborStreamWriter8startMapEv')

  @overload(int)
  def startMap(self, count: int) -> None:
    """
    Calls Qt's 'void QCborStreamWriter::startMap(quint64 count)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#startMap

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QCborStreamWriter::startMap(quint64 count)
    self.uglySide.call('ritual_ZN17QCborStreamWriter8startMapEy', count)

  def endMap(self) -> bool:
    """
    Calls Qt's 'bool QCborStreamWriter::endMap()'.

    Qt's own words: https://doc.qt.io/qt-6/qcborstreamwriter.html#endMap
    """
    #  bool QCborStreamWriter::endMap()
    return self.uglySide.call('ritual_ZN17QCborStreamWriter6endMapEv')
