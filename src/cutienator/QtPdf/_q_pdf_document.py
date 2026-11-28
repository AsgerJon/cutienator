"""
QPdfDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdfdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QImage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractListModel, QIODevice, QMetaObject, QPointF
  from ..QtCore import QSize, QSizeF, QVariant
  from ..QtGui import QColor
  from . import QPdfDocumentRenderOptions, QPdfSelection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QIODevice = WAIT['QIODevice']
  QPdfDocumentRenderOptions = WAIT['QPdfDocumentRenderOptions']
  QPointF = WAIT['QPointF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfDocument(QObject):
  """
  The cute side of Qt's QPdfDocument: a plain Python object standing in front
  of one C++ QPdfDocument.

  It is built on the cute 'QObject', as Qt's QPdfDocument is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfDocument that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'load', 'status',
  'setPassword', 'password', 'metaData', 'error', 'close', 'pageCount',
  'pagePointSize', 'pageLabel', 'pageIndexForLabel', 'pageModel', 'render',
  'getSelection', 'getSelectionAtIndex', 'getAllText', 'passwordChanged',
  'passwordRequired', 'statusChanged', 'pageCountChanged',
  'pageModelChanged', 'fileName'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfDocument::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPdfDocument::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfDocument::~QPdfDocument()': the destructor: Python never
    removes a C++ QPdfDocument.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfDocument is created at the first use, not by
    'QPdfDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfDocument.
  - Qt tells when it has removed the C++ QPdfDocument. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QPdfDocument, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QPdfDocument::Error' of Qt, with the 7 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NULL = Kee[int](0)
    Unknown = Kee[int](1)
    DataNotYetAvailable = Kee[int](2)
    FileNotFound = Kee[int](3)
    InvalidFileFormat = Kee[int](4)
    IncorrectPassword = Kee[int](5)
    UnsupportedSecurityScheme = Kee[int](6)

  class MetaDataField(CuteNum, scoped=True):
    """
    The enum 'QPdfDocument::MetaDataField' of Qt, with the 8 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Title = Kee[int](0)
    Subject = Kee[int](1)
    Author = Kee[int](2)
    Keywords = Kee[int](3)
    Producer = Kee[int](4)
    Creator = Kee[int](5)
    CreationDate = Kee[int](6)
    ModificationDate = Kee[int](7)

  class PageModelRole(CuteNum, scoped=True):
    """
    The enum 'QPdfDocument::PageModelRole' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Label = Kee[int](256)
    PointSize = Kee[int](257)
    NRoles = Kee[int](258)

  class Status(CuteNum, scoped=True):
    """
    The enum 'QPdfDocument::Status' of Qt, with the 5 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    Null = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Unloading = Kee[int](3)
    Error = Kee[int](4)

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
    Calls Qt's 'QString QPdfDocument::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#tr

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
    #  QString QPdfDocument::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QPdfDocument2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfDocument'

  #  A C++ QPdfDocument Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfDocument'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfDocument::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfDocument::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QPdfDocument10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QPdfDocument::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QPdfDocument::status() const
    return QPdfDocument.Status(self.uglySide.call(
        'ritual_ZNK12QPdfDocument6statusEv',
    ))

  def password(self) -> str:
    """
    Calls Qt's 'QString QPdfDocument::password() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfDocument::password() const
    return self.uglySide.call('ritual_ZNK12QPdfDocument8passwordEv')

  @overload(MetaDataField)
  def metaData(self, field: MetaDataField) -> QVariant:
    """
    Calls Qt's 'QVariant QPdfDocument::metaData(MetaDataField field) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#metaData

    Parameters
    ----------

    field : MetaDataField
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPdfDocument::metaData(MetaDataField field) const
    address = self.uglySide.call(
        'ritual_ZNK12QPdfDocument8metaDataENS_13MetaDataFieldE', field.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QPdfDocument::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QPdfDocument::error() const
    return QPdfDocument.Error(self.uglySide.call(
        'ritual_ZNK12QPdfDocument5errorEv',
    ))

  def pageCount(self) -> int:
    """
    Calls Qt's 'int QPdfDocument::pageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#pageCount
    """
    #  int QPdfDocument::pageCount() const
    return self.uglySide.call('ritual_ZNK12QPdfDocument9pageCountEv')

  @overload(int)
  def pagePointSize(self, page: int) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPdfDocument::pagePointSize(int page) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#pagePointSize

    Parameters
    ----------

    page : int
      Passed on as it is.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPdfDocument::pagePointSize(int page) const
    address = self.uglySide.call(
        'ritual_ZNK12QPdfDocument13pagePointSizeEi', page,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QPdfDocument::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfDocument::fileName() const
    return self.uglySide.call('ritual_ZNK12QPdfDocument8fileNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPassword(self, password: str) -> None:
    """
    Calls Qt's 'void QPdfDocument::setPassword(const QString &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPdfDocument::setPassword(const QString &password)
    self.uglySide.call(
        'ritual_ZN12QPdfDocument11setPasswordERK7QString', password,
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
    Notes what was given, for Qt's 'QPdfDocument::QPdfDocument()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#QPdfDocument
    """
    #  QPdfDocument::QPdfDocument()
    self._noteCreation(QPdfDocument, lambda: Rituals.call(
        'ritual_ZN12QPdfDocumentC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QPdfDocument::QPdfDocument(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#QPdfDocument

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfDocument::QPdfDocument(QObject *parent)
    self._noteCreation(QPdfDocument, lambda: Rituals.call(
        'ritual_ZN12QPdfDocumentC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def load(self, fileName: str) -> Error:
    """
    Calls Qt's 'Error QPdfDocument::load(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#load

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QPdfDocument::load(const QString &fileName)
    return QPdfDocument.Error(self.uglySide.call(
        'ritual_ZN12QPdfDocument4loadERK7QString', fileName,
    ))

  @overload(QIODevice)
  @overload(NoneType)
  def load(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QPdfDocument::load(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#load

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPdfDocument::load(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN12QPdfDocument4loadEP9QIODevice', self._addressOf(device),
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QPdfDocument::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#close
    """
    #  void QPdfDocument::close()
    self.uglySide.call('ritual_ZN12QPdfDocument5closeEv')

  @overload(int)
  def pageLabel(self, page: int) -> str:
    """
    Calls Qt's 'QString QPdfDocument::pageLabel(int page)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#pageLabel

    Parameters
    ----------

    page : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPdfDocument::pageLabel(int page)
    return self.uglySide.call('ritual_ZN12QPdfDocument9pageLabelEi', page)

  @overload(str)
  def pageIndexForLabel(self, label: str) -> int:
    """
    Calls Qt's 'int QPdfDocument::pageIndexForLabel(const QString &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocument.html#pageIndexForLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QPdfDocument::pageIndexForLabel(const QString &label)
    return self.uglySide.call(
        'ritual_ZN12QPdfDocument17pageIndexForLabelERK7QString', label,
    )

  def pageModel(self) -> Optional[QAbstractListModel]:
    """
    Calls Qt's 'QAbstractListModel *QPdfDocument::pageModel()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#pageModel

    Returns
    -------

    Optional[QAbstractListModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractListModel *QPdfDocument::pageModel()
    address = self.uglySide.call('ritual_ZN12QPdfDocument9pageModelEv')
    from ..QtCore import QAbstractListModel
    return QAbstractListModel._cuteAt(address)

  @overload(int, QSize)
  @overload(int, QSize, QPdfDocumentRenderOptions)
  def render(
      self,
      page: int,
      imageSize: QSize,
      options: Optional[QPdfDocumentRenderOptions] = None,
  ) -> QImage:
    """
    Calls Qt's 'QImage QPdfDocument::render(int page, QSize imageSize,
    QPdfDocumentRenderOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#render

    Parameters
    ----------

    page : int
      Passed on as it is.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : Optional[QPdfDocumentRenderOptions]
      Passed on as a value: Qt reads the C++ QPdfDocumentRenderOptions, which
      stays Python's own. May be left out, as in Qt: a new
      'QPdfDocumentRenderOptions()' is then passed on.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QPdfDocument::render(int page, QSize imageSize,
    #      QPdfDocumentRenderOptions options)
    if options is None:
      from . import QPdfDocumentRenderOptions
      options = QPdfDocumentRenderOptions()
    address = self.uglySide.call(
        'ritual_ZN12QPdfDocument6renderEi5QSize25QPdfDocumentRenderOptions',
        page, self._valueOf(imageSize), self._valueOf(options),
    )
    return QImage._cuteOwning(address)

  @overload(int, QSize, QPdfDocumentRenderOptions, QImage.Format, QColor)
  def render(
      self,
      page: int,
      imageSize: QSize,
      options: QPdfDocumentRenderOptions,
      format: QImage.Format,
      fillColor: QColor,
  ) -> QImage:
    """
    Calls Qt's 'QImage QPdfDocument::render(int page, QSize imageSize,
    QPdfDocumentRenderOptions options, QImage::Format format, const QColor
    &fillColor)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#render

    Parameters
    ----------

    page : int
      Passed on as it is.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QPdfDocumentRenderOptions
      Passed on as a value: Qt reads the C++ QPdfDocumentRenderOptions, which
      stays Python's own.

    format : QImage.Format
      Passed on as its number.

    fillColor : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QPdfDocument::render(int page, QSize imageSize,
    #      QPdfDocumentRenderOptions options, QImage::Format format, const
    #      QColor &fillColor)
    address = self.uglySide.call(
        'ritual_ZN12QPdfDocument6renderEi5QSize25QPdfDocumentRenderOptionsN'
        '6QImage6FormatERK6QColor',
        page, self._valueOf(imageSize), self._valueOf(options), format.value,
        self._valueOf(fillColor),
    )
    return QImage._cuteOwning(address)

  @overload(int, QPointF, QPointF)
  def getSelection(
      self,
      page: int,
      start: QPointF,
      end: QPointF,
  ) -> QPdfSelection:
    """
    Calls Qt's 'QPdfSelection QPdfDocument::getSelection(int page, QPointF
    start, QPointF end)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#getSelection

    Parameters
    ----------

    page : int
      Passed on as it is.

    start : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    end : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPdfSelection
      A new cute QPdfSelection around the copy Qt gave back. Python owns it.
    """
    #  QPdfSelection QPdfDocument::getSelection(int page, QPointF start,
    #      QPointF end)
    address = self.uglySide.call(
        'ritual_ZN12QPdfDocument12getSelectionEi7QPointFS0_',
        page, self._valueOf(start, 'QPointF'), self._valueOf(end, 'QPointF'),
    )
    from . import QPdfSelection
    return QPdfSelection._cuteOwning(address)

  @overload(int, int, int)
  def getSelectionAtIndex(
      self,
      page: int,
      startIndex: int,
      maxLength: int,
  ) -> QPdfSelection:
    """
    Calls Qt's 'QPdfSelection QPdfDocument::getSelectionAtIndex(int page, int
    startIndex, int maxLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfdocument.html#getSelectionAtIndex

    Parameters
    ----------

    page : int
      Passed on as it is.

    startIndex : int
      Passed on as it is.

    maxLength : int
      Passed on as it is.

    Returns
    -------

    QPdfSelection
      A new cute QPdfSelection around the copy Qt gave back. Python owns it.
    """
    #  QPdfSelection QPdfDocument::getSelectionAtIndex(int page, int
    #      startIndex, int maxLength)
    address = self.uglySide.call(
        'ritual_ZN12QPdfDocument19getSelectionAtIndexEiii',
        page, startIndex, maxLength,
    )
    from . import QPdfSelection
    return QPdfSelection._cuteOwning(address)

  @overload(int)
  def getAllText(self, page: int) -> QPdfSelection:
    """
    Calls Qt's 'QPdfSelection QPdfDocument::getAllText(int page)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#getAllText

    Parameters
    ----------

    page : int
      Passed on as it is.

    Returns
    -------

    QPdfSelection
      A new cute QPdfSelection around the copy Qt gave back. Python owns it.
    """
    #  QPdfSelection QPdfDocument::getAllText(int page)
    address = self.uglySide.call(
        'ritual_ZN12QPdfDocument10getAllTextEi', page,
    )
    from . import QPdfSelection
    return QPdfSelection._cuteOwning(address)

  def passwordChanged(self) -> None:
    """
    Calls Qt's 'void QPdfDocument::passwordChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#passwordChanged
    """
    #  void QPdfDocument::passwordChanged()
    self.uglySide.call('ritual_ZN12QPdfDocument15passwordChangedEv')

  def passwordRequired(self) -> None:
    """
    Calls Qt's 'void QPdfDocument::passwordRequired()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#passwordRequired
    """
    #  void QPdfDocument::passwordRequired()
    self.uglySide.call('ritual_ZN12QPdfDocument16passwordRequiredEv')

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void QPdfDocument::statusChanged(QPdfDocument::Status
    status)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QPdfDocument::statusChanged(QPdfDocument::Status status)
    self.uglySide.call(
        'ritual_ZN12QPdfDocument13statusChangedENS_6StatusE', status.value,
    )

  @overload(int)
  def pageCountChanged(self, pageCount: int) -> None:
    """
    Calls Qt's 'void QPdfDocument::pageCountChanged(int pageCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#pageCountChanged

    Parameters
    ----------

    pageCount : int
      Passed on as it is.
    """
    #  void QPdfDocument::pageCountChanged(int pageCount)
    self.uglySide.call(
        'ritual_ZN12QPdfDocument16pageCountChangedEi', pageCount,
    )

  def pageModelChanged(self) -> None:
    """
    Calls Qt's 'void QPdfDocument::pageModelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfdocument.html#pageModelChanged
    """
    #  void QPdfDocument::pageModelChanged()
    self.uglySide.call('ritual_ZN12QPdfDocument16pageModelChangedEv')
