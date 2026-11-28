"""
QTextureFileData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtexturefiledata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextureFileData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QByteArrayView, QDebug, QSize
  from . import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']


class QTextureFileData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextureFileData: a plain Python object standing in
  front of one C++ QTextureFileData.

  C++ hands a QTextureFileData around as a copy, so every C++
  QTextureFileData behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextureFileData that has a ritual and that Python
  can call so far, 25 names in all: 'isNull', 'isValid', 'clear', 'data',
  'setData', 'dataOffset', 'setDataOffset', 'dataLength', 'setDataLength',
  'getDataView', 'numLevels', 'setNumLevels', 'numFaces', 'setNumFaces',
  'size', 'setSize', 'glFormat', 'setGLFormat', 'glInternalFormat',
  'setGLInternalFormat', 'glBaseInternalFormat', 'setGLBaseInternalFormat',
  'logName', 'setLogName', '__rlshift__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextureFileData::QTextureFileData(QTextureFileData &&a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QTextureFileData &QTextureFileData::operator=(const
    QTextureFileData &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QTextureFileData &QTextureFileData::operator=(QTextureFileData
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QTextureFileData::~QTextureFileData()': the destructor: Python
    removes its C++ QTextureFileData by it, and has no other use for it.
  - Qt's 'void QTextureFileData::swap(QTextureFileData &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QMap<QByteArray, QByteArray> QTextureFileData::keyValueMetadata()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QTextureFileData::setKeyValueMetadata(const QMap<QByteArray,
    QByteArray> &keyValues)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QTextureFileData is created at the first use, not by
    'QTextureFileData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextureFileData back gives a copy the ritual made
    for Python, in a new cute QTextureFileData.
  - Each name of Qt's QTextureFileData that has no cute function yet,
    'keyValueMetadata', 'setKeyValueMetadata', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextureFileData, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'QTextureFileData::Mode' of Qt, with the 2 names Qt gives in it.
    """

    ByteArrayMode = Kee[int](0)
    ImageMode = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextureFileData'

  #  Qt's '~QTextureFileData()'. Naming it makes this a value class: Python
  #  owns every C++ QTextureFileData behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QTextureFileDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QTextureFileData::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#isNull
    """
    #  bool QTextureFileData::isNull() const
    return self.uglySide.call('ritual_ZNK16QTextureFileData6isNullEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextureFileData::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#isValid
    """
    #  bool QTextureFileData::isValid() const
    return self.uglySide.call('ritual_ZNK16QTextureFileData7isValidEv')

  def data(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextureFileData::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextureFileData::data() const
    address = self.uglySide.call('ritual_ZNK16QTextureFileData4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(int)
  @overload(int, int)
  def dataOffset(self, level: int = 0, face: int = 0) -> int:
    """
    Calls Qt's 'int QTextureFileData::dataOffset(int level, int face) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#dataOffset

    Parameters
    ----------

    level : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QTextureFileData::dataOffset(int level, int face) const
    return self.uglySide.call(
        'ritual_ZNK16QTextureFileData10dataOffsetEii', level, face,
    )

  @overload()
  @overload(int)
  @overload(int, int)
  def dataLength(self, level: int = 0, face: int = 0) -> int:
    """
    Calls Qt's 'int QTextureFileData::dataLength(int level, int face) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#dataLength

    Parameters
    ----------

    level : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QTextureFileData::dataLength(int level, int face) const
    return self.uglySide.call(
        'ritual_ZNK16QTextureFileData10dataLengthEii', level, face,
    )

  @overload()
  @overload(int)
  @overload(int, int)
  def getDataView(self, level: int = 0, face: int = 0) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QTextureFileData::getDataView(int level, int
    face) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#getDataView

    Parameters
    ----------

    level : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QTextureFileData::getDataView(int level, int face)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QTextureFileData11getDataViewEii', level, face,
    )
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  def numLevels(self) -> int:
    """
    Calls Qt's 'int QTextureFileData::numLevels() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#numLevels
    """
    #  int QTextureFileData::numLevels() const
    return self.uglySide.call('ritual_ZNK16QTextureFileData9numLevelsEv')

  def numFaces(self) -> int:
    """
    Calls Qt's 'int QTextureFileData::numFaces() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#numFaces
    """
    #  int QTextureFileData::numFaces() const
    return self.uglySide.call('ritual_ZNK16QTextureFileData8numFacesEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QTextureFileData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QTextureFileData::size() const
    address = self.uglySide.call('ritual_ZNK16QTextureFileData4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def glFormat(self) -> int:
    """
    Calls Qt's 'quint32 QTextureFileData::glFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#glFormat
    """
    #  quint32 QTextureFileData::glFormat() const
    return self.uglySide.call('ritual_ZNK16QTextureFileData8glFormatEv')

  def glInternalFormat(self) -> int:
    """
    Calls Qt's 'quint32 QTextureFileData::glInternalFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#glInternalFormat
    """
    #  quint32 QTextureFileData::glInternalFormat() const
    return self.uglySide.call(
        'ritual_ZNK16QTextureFileData16glInternalFormatEv',
    )

  def glBaseInternalFormat(self) -> int:
    """
    Calls Qt's 'quint32 QTextureFileData::glBaseInternalFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#glBaseInternalFormat
    """
    #  quint32 QTextureFileData::glBaseInternalFormat() const
    return self.uglySide.call(
        'ritual_ZNK16QTextureFileData20glBaseInternalFormatEv',
    )

  def logName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextureFileData::logName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#logName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextureFileData::logName() const
    address = self.uglySide.call('ritual_ZNK16QTextureFileData7logNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QTextureFileData::setData(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QTextureFileData::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData7setDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QImage)
  @overload(QImage, int)
  @overload(QImage, int, int)
  def setData(self, image: QImage, level: int = 0, face: int = 0) -> None:
    """
    Calls Qt's 'void QTextureFileData::setData(const QImage &image, int
    level, int face)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setData

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    level : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTextureFileData::setData(const QImage &image, int level, int
    #      face)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData7setDataERK6QImageii',
        self._valueOf(image), level, face,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  def setDataOffset(
      self,
      offset: int,
      level: int = 0,
      face: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QTextureFileData::setDataOffset(int offset, int level,
    int face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#setDataOffset

    Parameters
    ----------

    offset : int
      Passed on as it is.

    level : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTextureFileData::setDataOffset(int offset, int level, int face)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData13setDataOffsetEiii',
        offset, level, face,
    )

  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  def setDataLength(
      self,
      length: int,
      level: int = 0,
      face: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QTextureFileData::setDataLength(int length, int level,
    int face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#setDataLength

    Parameters
    ----------

    length : int
      Passed on as it is.

    level : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    face : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QTextureFileData::setDataLength(int length, int level, int face)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData13setDataLengthEiii',
        length, level, face,
    )

  @overload(int)
  def setNumLevels(self, num: int) -> None:
    """
    Calls Qt's 'void QTextureFileData::setNumLevels(int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setNumLevels

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QTextureFileData::setNumLevels(int num)
    self.uglySide.call('ritual_ZN16QTextureFileData12setNumLevelsEi', num)

  @overload(int)
  def setNumFaces(self, num: int) -> None:
    """
    Calls Qt's 'void QTextureFileData::setNumFaces(int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setNumFaces

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QTextureFileData::setNumFaces(int num)
    self.uglySide.call('ritual_ZN16QTextureFileData11setNumFacesEi', num)

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QTextureFileData::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QTextureFileData::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData7setSizeERK5QSize', self._valueOf(size),
    )

  @overload(int)
  def setGLFormat(self, format: int) -> None:
    """
    Calls Qt's 'void QTextureFileData::setGLFormat(quint32 format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setGLFormat

    Parameters
    ----------

    format : int
      Passed on as it is.
    """
    #  void QTextureFileData::setGLFormat(quint32 format)
    self.uglySide.call('ritual_ZN16QTextureFileData11setGLFormatEj', format)

  @overload(int)
  def setGLInternalFormat(self, format: int) -> None:
    """
    Calls Qt's 'void QTextureFileData::setGLInternalFormat(quint32 format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#setGLInternalFormat

    Parameters
    ----------

    format : int
      Passed on as it is.
    """
    #  void QTextureFileData::setGLInternalFormat(quint32 format)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData19setGLInternalFormatEj', format,
    )

  @overload(int)
  def setGLBaseInternalFormat(self, format: int) -> None:
    """
    Calls Qt's 'void QTextureFileData::setGLBaseInternalFormat(quint32
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#setGLBaseInternalFormat

    Parameters
    ----------

    format : int
      Passed on as it is.
    """
    #  void QTextureFileData::setGLBaseInternalFormat(quint32 format)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData23setGLBaseInternalFormatEj', format,
    )

  @overload(QByteArray)
  def setLogName(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QTextureFileData::setLogName(const QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#setLogName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QTextureFileData::setLogName(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN16QTextureFileData10setLogNameERK10QByteArray',
        self._valueOf(name),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QTextureFileData &d)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QTextureFileData &d)
    address = Rituals.call(
        'ritual_Zls6QDebugRK16QTextureFileData',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(Mode)
  def __init__(self, mode: Mode = Mode.ByteArrayMode) -> None:
    """
    Notes what was given, for Qt's 'QTextureFileData::QTextureFileData(Mode
    mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#QTextureFileData

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.ByteArrayMode.
    """
    #  QTextureFileData::QTextureFileData(Mode mode)
    self._noteCreation(QTextureFileData, lambda: Rituals.call(
        'ritual_ZN16QTextureFileDataC1ENS_4ModeE', mode.value,
    ))

  @overload(THIS)
  def __init__(self, other: QTextureFileData) -> None:
    """
    Notes what was given, for Qt's 'QTextureFileData::QTextureFileData(const
    QTextureFileData &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexturefiledata.html#QTextureFileData

    Parameters
    ----------

    other : QTextureFileData
      Passed on as a value: Qt reads the C++ QTextureFileData, which stays
      Python's own.
    """
    #  QTextureFileData::QTextureFileData(const QTextureFileData &other)
    self._noteCreation(QTextureFileData, lambda: Rituals.call(
        'ritual_ZN16QTextureFileDataC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QTextureFileData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexturefiledata.html#clear
    """
    #  void QTextureFileData::clear()
    self.uglySide.call('ritual_ZN16QTextureFileData5clearEv')

  @staticmethod
  def keyValueMetadata(*__, **_) -> Never:
    """
    Qt's 'QMap<QByteArray, QByteArray> QTextureFileData::keyValueMetadata()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextureFileData.keyValueMetadata' has no cute function yet. Qt's "
        "'QMap<QByteArray, QByteArray> QTextureFileData::keyValueMetadata() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setKeyValueMetadata(*__, **_) -> Never:
    """
    Qt's 'void QTextureFileData::setKeyValueMetadata(const QMap<QByteArray,
    QByteArray> &keyValues)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QTextureFileData.setKeyValueMetadata' has no cute function yet. "
        "Qt's 'void QTextureFileData::setKeyValueMetadata(const "
        "QMap<QByteArray, QByteArray> &keyValues)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QTextureFileData::swap(QTextureFileData &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextureFileData.swap' has no cute function yet. Qt's 'void "
        "QTextureFileData::swap(QTextureFileData &other)': takes a type "
        "Python has no way to hand over yet.")
