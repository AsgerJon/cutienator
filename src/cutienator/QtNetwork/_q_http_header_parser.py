"""
QHttpHeaderParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpheaderparser_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpHeaderParser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QByteArrayView
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']


class QHttpHeaderParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpHeaderParser: a plain Python object standing in
  front of one C++ QHttpHeaderParser.

  C++ hands a QHttpHeaderParser around as a copy, so every C++
  QHttpHeaderParser behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpHeaderParser that has a ritual and that Python
  can call so far, 26 names in all: 'clear', 'parseHeaders', 'parseStatus',
  'headers', 'setStatusCode', 'getStatusCode', 'getMajorVersion',
  'setMajorVersion', 'getMinorVersion', 'setMinorVersion', 'getReasonPhrase',
  'setReasonPhrase', 'firstHeaderField', 'combinedHeaderValue',
  'headerFieldValues', 'setHeaderField', 'prependHeaderField',
  'appendHeaderField', 'removeHeaderField', 'clearHeaders',
  'setMaxHeaderFieldSize', 'maxHeaderFieldSize', 'setMaxTotalHeaderSize',
  'maxTotalHeaderSize', 'setMaxHeaderFields', 'maxHeaderFields'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpHeaderParser::~QHttpHeaderParser()': the destructor: Python
    removes its C++ QHttpHeaderParser by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 29 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QHttpHeaderParser is created at the first use, not by
    'QHttpHeaderParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpHeaderParser back gives a copy the ritual made
    for Python, in a new cute QHttpHeaderParser.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpHeaderParser'

  #  Qt's '~QHttpHeaderParser()'. Naming it makes this a value class: Python
  #  owns every C++ QHttpHeaderParser behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QHttpHeaderParserD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'const QHttpHeaders &QHttpHeaderParser::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaderparser.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  const QHttpHeaders &QHttpHeaderParser::headers() const
    address = self.uglySide.call('ritual_ZNKR17QHttpHeaderParser7headersEv')
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  def getStatusCode(self) -> int:
    """
    Calls Qt's 'int QHttpHeaderParser::getStatusCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#getStatusCode
    """
    #  int QHttpHeaderParser::getStatusCode() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser13getStatusCodeEv',
    )

  def getMajorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpHeaderParser::getMajorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#getMajorVersion
    """
    #  int QHttpHeaderParser::getMajorVersion() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser15getMajorVersionEv',
    )

  def getMinorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpHeaderParser::getMinorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#getMinorVersion
    """
    #  int QHttpHeaderParser::getMinorVersion() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser15getMinorVersionEv',
    )

  def getReasonPhrase(self) -> str:
    """
    Calls Qt's 'QString QHttpHeaderParser::getReasonPhrase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#getReasonPhrase

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpHeaderParser::getReasonPhrase() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser15getReasonPhraseEv',
    )

  @overload(QByteArrayView)
  @overload(QByteArrayView, QByteArray)
  def firstHeaderField(
      self,
      name: QByteArrayView,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpHeaderParser::firstHeaderField(QByteArrayView
    name, const QByteArray &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#firstHeaderField

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    defaultValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpHeaderParser::firstHeaderField(QByteArrayView name,
    #      const QByteArray &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArray
      defaultValue = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser16firstHeaderFieldE14QByteArrayViewRK'
        '10QByteArray',
        self._valueOf(name), self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArrayView)
  @overload(QByteArrayView, QByteArray)
  def combinedHeaderValue(
      self,
      name: QByteArrayView,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QHttpHeaderParser::combinedHeaderValue(QByteArrayView name, const
    QByteArray &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#combinedHeaderValue

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    defaultValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpHeaderParser::combinedHeaderValue(QByteArrayView name,
    #      const QByteArray &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArray
      defaultValue = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser19combinedHeaderValueE14QByteArrayVie'
        'wRK10QByteArray',
        self._valueOf(name), self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArrayView)
  def headerFieldValues(self, name: QByteArrayView) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QHttpHeaderParser::headerFieldValues(QByteArrayView name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#headerFieldValues

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QHttpHeaderParser::headerFieldValues(QByteArrayView
    #      name) const
    address = self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser17headerFieldValuesE14QByteArrayView',
        self._valueOf(name),
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def maxHeaderFieldSize(self) -> int:
    """
    Calls Qt's 'qsizetype QHttpHeaderParser::maxHeaderFieldSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#maxHeaderFieldSize
    """
    #  qsizetype QHttpHeaderParser::maxHeaderFieldSize() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser18maxHeaderFieldSizeEv',
    )

  def maxTotalHeaderSize(self) -> int:
    """
    Calls Qt's 'qsizetype QHttpHeaderParser::maxTotalHeaderSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#maxTotalHeaderSize
    """
    #  qsizetype QHttpHeaderParser::maxTotalHeaderSize() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser18maxTotalHeaderSizeEv',
    )

  def maxHeaderFields(self) -> int:
    """
    Calls Qt's 'qsizetype QHttpHeaderParser::maxHeaderFields() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#maxHeaderFields
    """
    #  qsizetype QHttpHeaderParser::maxHeaderFields() const
    return self.uglySide.call(
        'ritual_ZNK17QHttpHeaderParser15maxHeaderFieldsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStatusCode(self, code: int) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setStatusCode(int code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setStatusCode

    Parameters
    ----------

    code : int
      Passed on as it is.
    """
    #  void QHttpHeaderParser::setStatusCode(int code)
    self.uglySide.call('ritual_ZN17QHttpHeaderParser13setStatusCodeEi', code)

  @overload(int)
  def setMajorVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setMajorVersion(int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setMajorVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QHttpHeaderParser::setMajorVersion(int version)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser15setMajorVersionEi', version,
    )

  @overload(int)
  def setMinorVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setMinorVersion(int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setMinorVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QHttpHeaderParser::setMinorVersion(int version)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser15setMinorVersionEi', version,
    )

  @overload(str)
  def setReasonPhrase(self, reason: str) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setReasonPhrase(const QString
    &reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setReasonPhrase

    Parameters
    ----------

    reason : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpHeaderParser::setReasonPhrase(const QString &reason)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser15setReasonPhraseERK7QString', reason,
    )

  @overload(QByteArray, QByteArray)
  def setHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpHeaderParser::setHeaderField(const QByteArray &name, const
    #      QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser14setHeaderFieldERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(data),
    )

  @overload(int)
  def setMaxHeaderFieldSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setMaxHeaderFieldSize(qsizetype
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setMaxHeaderFieldSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpHeaderParser::setMaxHeaderFieldSize(qsizetype size)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser21setMaxHeaderFieldSizeEx', size,
    )

  @overload(int)
  def setMaxTotalHeaderSize(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setMaxTotalHeaderSize(qsizetype
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setMaxTotalHeaderSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpHeaderParser::setMaxTotalHeaderSize(qsizetype size)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser21setMaxTotalHeaderSizeEx', size,
    )

  @overload(int)
  def setMaxHeaderFields(self, size: int) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::setMaxHeaderFields(qsizetype size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#setMaxHeaderFields

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QHttpHeaderParser::setMaxHeaderFields(qsizetype size)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser18setMaxHeaderFieldsEx', size,
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
    Notes what was given, for Qt's 'QHttpHeaderParser::QHttpHeaderParser()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#QHttpHeaderParser
    """
    #  QHttpHeaderParser::QHttpHeaderParser()
    self._noteCreation(QHttpHeaderParser, lambda: Rituals.call(
        'ritual_ZN17QHttpHeaderParserC1Ev',
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
    Calls Qt's 'void QHttpHeaderParser::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaderparser.html#clear
    """
    #  void QHttpHeaderParser::clear()
    self.uglySide.call('ritual_ZN17QHttpHeaderParser5clearEv')

  @overload(QByteArrayView)
  def parseHeaders(self, headers: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QHttpHeaderParser::parseHeaders(QByteArrayView
    headers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#parseHeaders

    Parameters
    ----------

    headers : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QHttpHeaderParser::parseHeaders(QByteArrayView headers)
    return self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser12parseHeadersE14QByteArrayView',
        self._valueOf(headers),
    )

  @overload(QByteArrayView)
  def parseStatus(self, status: QByteArrayView) -> bool:
    """
    Calls Qt's 'bool QHttpHeaderParser::parseStatus(QByteArrayView status)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpheaderparser.html#parseStatus

    Parameters
    ----------

    status : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QHttpHeaderParser::parseStatus(QByteArrayView status)
    return self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser11parseStatusE14QByteArrayView',
        self._valueOf(status),
    )

  @overload(QByteArray, QByteArray)
  def prependHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::prependHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#prependHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpHeaderParser::prependHeaderField(const QByteArray &name,
    #      const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser18prependHeaderFieldERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(data),
    )

  @overload(QByteArray, QByteArray)
  def appendHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::appendHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#appendHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpHeaderParser::appendHeaderField(const QByteArray &name,
    #      const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser17appendHeaderFieldERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(data),
    )

  @overload(QByteArrayView)
  def removeHeaderField(self, name: QByteArrayView) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::removeHeaderField(QByteArrayView
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#removeHeaderField

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QHttpHeaderParser::removeHeaderField(QByteArrayView name)
    self.uglySide.call(
        'ritual_ZN17QHttpHeaderParser17removeHeaderFieldE14QByteArrayView',
        self._valueOf(name),
    )

  def clearHeaders(self) -> None:
    """
    Calls Qt's 'void QHttpHeaderParser::clearHeaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpheaderparser.html#clearHeaders
    """
    #  void QHttpHeaderParser::clearHeaders()
    self.uglySide.call('ritual_ZN17QHttpHeaderParser12clearHeadersEv')
