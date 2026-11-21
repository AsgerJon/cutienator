"""
QPdfWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpdfwriter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QPagedPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject, QUuid
  from . import QPdfOutputIntent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QPdfOutputIntent = WAIT['QPdfOutputIntent']
  QUuid = WAIT['QUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfWriter(QObject):
  """
  The cute side of Qt's QPdfWriter: a plain Python object standing in front
  of one C++ QPdfWriter.

  It is built on the cute 'QObject', as Qt's QPdfWriter is built on Qt's
  QObject, and has everything that class has. Qt's QPdfWriter is built on
  Qt's QPagedPaintDevice as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QPdfWriter that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'setPdfVersion',
  'pdfVersion', 'title', 'setTitle', 'creator', 'setCreator', 'documentId',
  'setDocumentId', 'author', 'setAuthor', 'newPage', 'setResolution',
  'resolution', 'setDocumentXmpMetadata', 'documentXmpMetadata',
  'addFileAttachment', 'colorModel', 'setColorModel', 'outputIntent',
  'setOutputIntent'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPdfWriter::~QPdfWriter()': the destructor: Python never removes a
    C++ QPdfWriter.

  What has no ritual
  ------------------

  10 of the 35 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 protected; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QPdfWriter is created at the first use, not by 'QPdfWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfWriter.
  - Qt tells when it has removed the C++ QPdfWriter. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QPdfWriter, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ColorModel(CuteNum, scoped=True):
    """
    The enum 'QPdfWriter::ColorModel' of Qt, with the 4 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    RGB = Kee[int](0)
    Grayscale = Kee[int](1)
    CMYK = Kee[int](2)
    Auto = Kee[int](3)

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
    Calls Qt's 'QString QPdfWriter::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#tr

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
    #  QString QPdfWriter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QPdfWriter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfWriter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfWriter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfWriter::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QPdfWriter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pdfVersion(self) -> QPagedPaintDevice.PdfVersion:
    """
    Calls Qt's 'PdfVersion QPdfWriter::pdfVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#pdfVersion

    Returns
    -------

    QPagedPaintDevice.PdfVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPagedPaintDevice.PdfVersion(number)' gives.
    """
    #  PdfVersion QPdfWriter::pdfVersion() const
    return QPagedPaintDevice.PdfVersion(self.uglySide.call(
        'ritual_ZNK10QPdfWriter10pdfVersionEv',
    ))

  def title(self) -> str:
    """
    Calls Qt's 'QString QPdfWriter::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfWriter::title() const
    return self.uglySide.call('ritual_ZNK10QPdfWriter5titleEv')

  def creator(self) -> str:
    """
    Calls Qt's 'QString QPdfWriter::creator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#creator

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfWriter::creator() const
    return self.uglySide.call('ritual_ZNK10QPdfWriter7creatorEv')

  def documentId(self) -> QUuid:
    """
    Calls Qt's 'QUuid QPdfWriter::documentId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#documentId

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid QPdfWriter::documentId() const
    address = self.uglySide.call('ritual_ZNK10QPdfWriter10documentIdEv')
    from ..QtCore import QUuid
    return QUuid._cuteOwning(address)

  def author(self) -> str:
    """
    Calls Qt's 'QString QPdfWriter::author() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#author

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfWriter::author() const
    return self.uglySide.call('ritual_ZNK10QPdfWriter6authorEv')

  def resolution(self) -> int:
    """
    Calls Qt's 'int QPdfWriter::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#resolution
    """
    #  int QPdfWriter::resolution() const
    return self.uglySide.call('ritual_ZNK10QPdfWriter10resolutionEv')

  def documentXmpMetadata(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QPdfWriter::documentXmpMetadata() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfwriter.html#documentXmpMetadata

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QPdfWriter::documentXmpMetadata() const
    address = self.uglySide.call(
        'ritual_ZNK10QPdfWriter19documentXmpMetadataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def colorModel(self) -> ColorModel:
    """
    Calls Qt's 'ColorModel QPdfWriter::colorModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#colorModel

    Returns
    -------

    ColorModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorModel(number)'
      gives.
    """
    #  ColorModel QPdfWriter::colorModel() const
    return QPdfWriter.ColorModel(self.uglySide.call(
        'ritual_ZNK10QPdfWriter10colorModelEv',
    ))

  def outputIntent(self) -> QPdfOutputIntent:
    """
    Calls Qt's 'QPdfOutputIntent QPdfWriter::outputIntent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#outputIntent

    Returns
    -------

    QPdfOutputIntent
      A new cute QPdfOutputIntent around the copy Qt gave back. Python owns
      it.
    """
    #  QPdfOutputIntent QPdfWriter::outputIntent() const
    address = self.uglySide.call('ritual_ZNK10QPdfWriter12outputIntentEv')
    from . import QPdfOutputIntent
    return QPdfOutputIntent._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPagedPaintDevice.PdfVersion)
  def setPdfVersion(self, version: QPagedPaintDevice.PdfVersion) -> None:
    """
    Calls Qt's 'void QPdfWriter::setPdfVersion(PdfVersion version)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setPdfVersion

    Parameters
    ----------

    version : QPagedPaintDevice.PdfVersion
      Passed on as its number.
    """
    #  void QPdfWriter::setPdfVersion(PdfVersion version)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter13setPdfVersionEN17QPagedPaintDevice10PdfVers'
        'ionE',
        version.value,
    )

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QPdfWriter::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfWriter::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN10QPdfWriter8setTitleERK7QString', title)

  @overload(str)
  def setCreator(self, creator: str) -> None:
    """
    Calls Qt's 'void QPdfWriter::setCreator(const QString &creator)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setCreator

    Parameters
    ----------

    creator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfWriter::setCreator(const QString &creator)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter10setCreatorERK7QString', creator,
    )

  @overload(QUuid)
  def setDocumentId(self, documentId: QUuid) -> None:
    """
    Calls Qt's 'void QPdfWriter::setDocumentId(QUuid documentId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setDocumentId

    Parameters
    ----------

    documentId : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  void QPdfWriter::setDocumentId(QUuid documentId)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter13setDocumentIdE5QUuid',
        self._valueOf(documentId),
    )

  @overload(str)
  def setAuthor(self, author: str) -> None:
    """
    Calls Qt's 'void QPdfWriter::setAuthor(const QString &author)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setAuthor

    Parameters
    ----------

    author : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfWriter::setAuthor(const QString &author)
    self.uglySide.call('ritual_ZN10QPdfWriter9setAuthorERK7QString', author)

  @overload(int)
  def setResolution(self, resolution: int) -> None:
    """
    Calls Qt's 'void QPdfWriter::setResolution(int resolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setResolution

    Parameters
    ----------

    resolution : int
      Passed on as it is.
    """
    #  void QPdfWriter::setResolution(int resolution)
    self.uglySide.call('ritual_ZN10QPdfWriter13setResolutionEi', resolution)

  @overload(QByteArray)
  def setDocumentXmpMetadata(self, xmpMetadata: QByteArray) -> None:
    """
    Calls Qt's 'void QPdfWriter::setDocumentXmpMetadata(const QByteArray
    &xmpMetadata)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfwriter.html#setDocumentXmpMetadata

    Parameters
    ----------

    xmpMetadata : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QPdfWriter::setDocumentXmpMetadata(const QByteArray &xmpMetadata)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter22setDocumentXmpMetadataERK10QByteArray',
        self._valueOf(xmpMetadata),
    )

  @overload(ColorModel)
  def setColorModel(self, model: ColorModel) -> None:
    """
    Calls Qt's 'void QPdfWriter::setColorModel(ColorModel model)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setColorModel

    Parameters
    ----------

    model : ColorModel
      Passed on as its number.
    """
    #  void QPdfWriter::setColorModel(ColorModel model)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter13setColorModelENS_10ColorModelE', model.value,
    )

  @overload(QPdfOutputIntent)
  def setOutputIntent(self, intent: QPdfOutputIntent) -> None:
    """
    Calls Qt's 'void QPdfWriter::setOutputIntent(const QPdfOutputIntent
    &intent)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#setOutputIntent

    Parameters
    ----------

    intent : QPdfOutputIntent
      Passed on as a value: Qt reads the C++ QPdfOutputIntent, which stays
      Python's own.
    """
    #  void QPdfWriter::setOutputIntent(const QPdfOutputIntent &intent)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter15setOutputIntentERK16QPdfOutputIntent',
        self._valueOf(intent),
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

  @overload(str)
  def __init__(self, filename: str) -> None:
    """
    Notes what was given, for Qt's 'QPdfWriter::QPdfWriter(const QString
    &filename)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#QPdfWriter

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPdfWriter::QPdfWriter(const QString &filename)
    self._noteCreation(QPdfWriter, lambda: Rituals.call(
        'ritual_ZN10QPdfWriterC1ERK7QString', filename,
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's 'QPdfWriter::QPdfWriter(QIODevice
    *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#QPdfWriter

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfWriter::QPdfWriter(QIODevice *device)
    self._noteCreation(QPdfWriter, lambda: Rituals.call(
        'ritual_ZN10QPdfWriterC1EP9QIODevice', self._addressOf(device),
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

  def newPage(self) -> bool:
    """
    Calls Qt's 'bool QPdfWriter::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#newPage
    """
    #  bool QPdfWriter::newPage()
    return self.uglySide.call('ritual_ZN10QPdfWriter7newPageEv')

  @overload(str, QByteArray)
  @overload(str, QByteArray, str)
  def addFileAttachment(
      self,
      fileName: str,
      data: QByteArray,
      mimeType: str = '',
  ) -> None:
    """
    Calls Qt's 'void QPdfWriter::addFileAttachment(const QString &fileName,
    const QByteArray &data, const QString &mimeType)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfwriter.html#addFileAttachment

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mimeType : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QPdfWriter::addFileAttachment(const QString &fileName, const
    #      QByteArray &data, const QString &mimeType)
    self.uglySide.call(
        'ritual_ZN10QPdfWriter17addFileAttachmentERK7QStringRK10QByteArrayS'
        '2_',
        fileName, self._valueOf(data), mimeType,
    )
