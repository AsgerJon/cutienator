"""
QMimeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmimedata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QMetaObject, QMetaType, QUrl, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaType = WAIT['QMetaType']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMimeData(QObject):
  """
  The cute side of Qt's QMimeData: a plain Python object standing in front of
  one C++ QMimeData.

  It is built on the cute 'QObject', as Qt's QMimeData is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMimeData that has a ritual and that Python can call
  so far, 24 names in all: 'metaObject', 'tr', 'urls', 'setUrls', 'hasUrls',
  'text', 'setText', 'hasText', 'html', 'setHtml', 'hasHtml', 'imageData',
  'setImageData', 'hasImage', 'colorData', 'setColorData', 'hasColor',
  'data', 'setData', 'removeFormat', 'hasFormat', 'formats', 'clear',
  'retrieveData'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMimeData::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMimeData::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMimeData::~QMimeData()': the destructor: Python never removes a
    C++ QMimeData.
  - Qt's 'QMimeDataPrivate *QMimeData::d_func()': gives 'QMimeDataPrivate',
    which has no cute class yet.
  - Qt's 'const QMimeDataPrivate *QMimeData::d_func() const': gives
    'QMimeDataPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMimeData is created at the first use, not by 'QMimeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeData.
  - Qt tells when it has removed the C++ QMimeData. Every call on the cute
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
    Calls Qt's 'QString QMimeData::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#tr

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
    #  QString QMimeData::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QMimeData2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeData'

  #  A C++ QMimeData Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMimeData'

  #  The functions Qt calls itself that QMimeData is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'formats': (
          'QStringList QMimeData::formats() const',
      ),
  }

  #  The functions Qt calls itself that QMimeData is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'hasFormat': (
          ('_ZNK9QMimeData9hasFormatERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'retrieveData': (
          ('_ZNK9QMimeData12retrieveDataERK7QString9QMetaType',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QMetaType'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMimeData::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMimeData::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QMimeData10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def urls(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QMimeData::urls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#urls

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QMimeData::urls() const
    address = self.uglySide.call('ritual_ZNK9QMimeData4urlsEv')
    from . import QUrl
    return QList[QUrl]._cuteOwning(address)

  def hasUrls(self) -> bool:
    """
    Calls Qt's 'bool QMimeData::hasUrls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#hasUrls
    """
    #  bool QMimeData::hasUrls() const
    return self.uglySide.call('ritual_ZNK9QMimeData7hasUrlsEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QMimeData::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeData::text() const
    return self.uglySide.call('ritual_ZNK9QMimeData4textEv')

  def hasText(self) -> bool:
    """
    Calls Qt's 'bool QMimeData::hasText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#hasText
    """
    #  bool QMimeData::hasText() const
    return self.uglySide.call('ritual_ZNK9QMimeData7hasTextEv')

  def html(self) -> str:
    """
    Calls Qt's 'QString QMimeData::html() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeData::html() const
    return self.uglySide.call('ritual_ZNK9QMimeData4htmlEv')

  def hasHtml(self) -> bool:
    """
    Calls Qt's 'bool QMimeData::hasHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#hasHtml
    """
    #  bool QMimeData::hasHtml() const
    return self.uglySide.call('ritual_ZNK9QMimeData7hasHtmlEv')

  def imageData(self) -> QVariant:
    """
    Calls Qt's 'QVariant QMimeData::imageData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#imageData

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMimeData::imageData() const
    address = self.uglySide.call('ritual_ZNK9QMimeData9imageDataEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  def hasImage(self) -> bool:
    """
    Calls Qt's 'bool QMimeData::hasImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#hasImage
    """
    #  bool QMimeData::hasImage() const
    return self.uglySide.call('ritual_ZNK9QMimeData8hasImageEv')

  def colorData(self) -> QVariant:
    """
    Calls Qt's 'QVariant QMimeData::colorData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#colorData

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMimeData::colorData() const
    address = self.uglySide.call('ritual_ZNK9QMimeData9colorDataEv')
    from . import QVariant
    return QVariant._cuteOwning(address)

  def hasColor(self) -> bool:
    """
    Calls Qt's 'bool QMimeData::hasColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#hasColor
    """
    #  bool QMimeData::hasColor() const
    return self.uglySide.call('ritual_ZNK9QMimeData8hasColorEv')

  @overload(str)
  def data(self, mimetype: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMimeData::data(const QString &mimetype) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#data

    Parameters
    ----------

    mimetype : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMimeData::data(const QString &mimetype) const
    address = self.uglySide.call(
        'ritual_ZNK9QMimeData4dataERK7QString', mimetype,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(str)
  def hasFormat(self, mimetype: str) -> bool:
    """
    Calls Qt's 'bool QMimeData::hasFormat(const QString &mimetype) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#hasFormat

    Parameters
    ----------

    mimetype : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeData::hasFormat(const QString &mimetype) const
    ritual = 'ritual_ZNK9QMimeData9hasFormatERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QMimeData9hasFormatERK7QString'
    return self.uglySide.call(ritual, mimetype)

  def formats(self) -> QStringList:
    """
    Calls Qt's 'QStringList QMimeData::formats() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#formats

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QMimeData::formats() const
    address = self.uglySide.call('ritual_ZNK9QMimeData7formatsEv')
    return QStringList._cuteOwning(address)

  @overload(str, QMetaType)
  def retrieveData(
      self,
      mimetype: str,
      preferredType: QMetaType,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QMimeData::retrieveData(const QString &mimetype,
    QMetaType preferredType) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#retrieveData

    Parameters
    ----------

    mimetype : str
      Passed on as it is: a QString is made of it for the call.

    preferredType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMimeData::retrieveData(const QString &mimetype, QMetaType
    #      preferredType) const
    ritual = 'ritual_ZNK9QMimeData12retrieveDataERK7QString9QMetaType'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QMimeData12retrieveDataERK7QString9QMetaType'
    address = self.uglySide.call(
        ritual, mimetype, self._valueOf(preferredType),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QUrl])
  def setUrls(self, urls: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QMimeData::setUrls(const QList<QUrl> &urls)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#setUrls

    Parameters
    ----------

    urls : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QMimeData::setUrls(const QList<QUrl> &urls)
    self.uglySide.call(
        'ritual_ZN9QMimeData7setUrlsERK5QListI4QUrlE', self._valueOf(urls),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QMimeData::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeData::setText(const QString &text)
    self.uglySide.call('ritual_ZN9QMimeData7setTextERK7QString', text)

  @overload(str)
  def setHtml(self, html: str) -> None:
    """
    Calls Qt's 'void QMimeData::setHtml(const QString &html)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#setHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeData::setHtml(const QString &html)
    self.uglySide.call('ritual_ZN9QMimeData7setHtmlERK7QString', html)

  @overload(QVariant)
  def setImageData(self, image: QVariant) -> None:
    """
    Calls Qt's 'void QMimeData::setImageData(const QVariant &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#setImageData

    Parameters
    ----------

    image : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QMimeData::setImageData(const QVariant &image)
    self.uglySide.call(
        'ritual_ZN9QMimeData12setImageDataERK8QVariant',
        self._valueOf(image),
    )

  @overload(QVariant)
  def setColorData(self, color: QVariant) -> None:
    """
    Calls Qt's 'void QMimeData::setColorData(const QVariant &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#setColorData

    Parameters
    ----------

    color : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QMimeData::setColorData(const QVariant &color)
    self.uglySide.call(
        'ritual_ZN9QMimeData12setColorDataERK8QVariant',
        self._valueOf(color),
    )

  @overload(str, QByteArray)
  def setData(self, mimetype: str, data: QByteArray) -> None:
    """
    Calls Qt's 'void QMimeData::setData(const QString &mimetype, const
    QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#setData

    Parameters
    ----------

    mimetype : str
      Passed on as it is: a QString is made of it for the call.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMimeData::setData(const QString &mimetype, const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN9QMimeData7setDataERK7QStringRK10QByteArray',
        mimetype, self._valueOf(data),
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
    Notes what was given, for Qt's 'QMimeData::QMimeData()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#QMimeData
    """
    #  QMimeData::QMimeData()
    self._noteCreation(QMimeData, lambda: Rituals.call(
        'ritual_ZN9QMimeDataC1Ev',
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
  def removeFormat(self, mimetype: str) -> None:
    """
    Calls Qt's 'void QMimeData::removeFormat(const QString &mimetype)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#removeFormat

    Parameters
    ----------

    mimetype : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeData::removeFormat(const QString &mimetype)
    self.uglySide.call(
        'ritual_ZN9QMimeData12removeFormatERK7QString', mimetype,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QMimeData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmimedata.html#clear
    """
    #  void QMimeData::clear()
    self.uglySide.call('ritual_ZN9QMimeData5clearEv')
