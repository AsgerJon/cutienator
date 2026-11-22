"""
QTextDocumentWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextdocumentwriter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice
  from . import QTextDocument, QTextDocumentFragment
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QTextDocument = WAIT['QTextDocument']
  QTextDocumentFragment = WAIT['QTextDocumentFragment']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextDocumentWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextDocumentWriter: a plain Python object standing
  in front of one C++ QTextDocumentWriter.

  What exists
  -----------

  Every function of Qt's QTextDocumentWriter that has a ritual and that
  Python can call so far, 8 names in all: 'setFormat', 'format', 'setDevice',
  'device', 'setFileName', 'fileName', 'write', 'supportedDocumentFormats'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextDocumentWriter::~QTextDocumentWriter()': the destructor:
    Python never removes a C++ QTextDocumentWriter.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QTextDocumentWriter is created at the first use, not by
    'QTextDocumentWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextDocumentWriter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def supportedDocumentFormats() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QTextDocumentWriter::supportedDocumentFormats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentwriter.html#supportedDocumentFormats

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QTextDocumentWriter::supportedDocumentFormats()
    address = Rituals.call(
        'ritual_ZN19QTextDocumentWriter24supportedDocumentFormatsEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextDocumentWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTextDocumentWriter::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#format

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTextDocumentWriter::format() const
    address = self.uglySide.call('ritual_ZNK19QTextDocumentWriter6formatEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QTextDocumentWriter::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QTextDocumentWriter::device() const
    address = self.uglySide.call('ritual_ZNK19QTextDocumentWriter6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QTextDocumentWriter::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocumentWriter::fileName() const
    return self.uglySide.call('ritual_ZNK19QTextDocumentWriter8fileNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setFormat(self, format: QByteArray) -> None:
    """
    Calls Qt's 'void QTextDocumentWriter::setFormat(const QByteArray
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#setFormat

    Parameters
    ----------

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QTextDocumentWriter::setFormat(const QByteArray &format)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentWriter9setFormatERK10QByteArray',
        self._valueOf(format),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QTextDocumentWriter::setDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocumentWriter::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentWriter9setDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QTextDocumentWriter::setFileName(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentwriter.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextDocumentWriter::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN19QTextDocumentWriter11setFileNameERK7QString', fileName,
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
    Notes what was given, for Qt's
    'QTextDocumentWriter::QTextDocumentWriter()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentwriter.html#QTextDocumentWriter
    """
    #  QTextDocumentWriter::QTextDocumentWriter()
    self._noteCreation(QTextDocumentWriter, lambda: Rituals.call(
        'ritual_ZN19QTextDocumentWriterC1Ev',
    ))

  @overload(QIODevice, QByteArray)
  @overload(NoneType, QByteArray)
  def __init__(
      self,
      device: Optional[QIODevice],
      format: QByteArray,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentWriter::QTextDocumentWriter(QIODevice *device, const
    QByteArray &format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentwriter.html#QTextDocumentWriter

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    format : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QTextDocumentWriter::QTextDocumentWriter(QIODevice *device, const
    #      QByteArray &format)
    self._noteCreation(QTextDocumentWriter, lambda: Rituals.call(
        'ritual_ZN19QTextDocumentWriterC1EP9QIODeviceRK10QByteArray',
        self._addressOf(device), self._valueOf(format),
    ))

  @overload(str)
  @overload(str, QByteArray)
  def __init__(
      self,
      fileName: str,
      format: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextDocumentWriter::QTextDocumentWriter(const QString &fileName, const
    QByteArray &format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocumentwriter.html#QTextDocumentWriter

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    format : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QTextDocumentWriter::QTextDocumentWriter(const QString &fileName,
    #      const QByteArray &format)
    if format is None:
      from ..QtCore import QByteArray
      format = QByteArray()
    self._noteCreation(QTextDocumentWriter, lambda: Rituals.call(
        'ritual_ZN19QTextDocumentWriterC1ERK7QStringRK10QByteArray',
        fileName, self._valueOf(format),
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

  @overload(QTextDocument)
  @overload(NoneType)
  def write(self, document: Optional[QTextDocument]) -> bool:
    """
    Calls Qt's 'bool QTextDocumentWriter::write(const QTextDocument
    *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#write

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTextDocumentWriter::write(const QTextDocument *document)
    return self.uglySide.call(
        'ritual_ZN19QTextDocumentWriter5writeEPK13QTextDocument',
        self._addressOf(document),
    )

  @overload(QTextDocumentFragment)
  def write(self, fragment: QTextDocumentFragment) -> bool:
    """
    Calls Qt's 'bool QTextDocumentWriter::write(const QTextDocumentFragment
    &fragment)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocumentwriter.html#write

    Parameters
    ----------

    fragment : QTextDocumentFragment
      Passed on as a value: Qt reads the C++ QTextDocumentFragment, which
      stays Python's own.
    """
    #  bool QTextDocumentWriter::write(const QTextDocumentFragment &fragment)
    return self.uglySide.call(
        'ritual_ZN19QTextDocumentWriter5writeERK21QTextDocumentFragment',
        self._valueOf(fragment),
    )
