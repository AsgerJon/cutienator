"""
QHttpNetworkHeader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkheader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkHeader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QByteArrayView, QUrl
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QUrl = WAIT['QUrl']


class QHttpNetworkHeader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpNetworkHeader: a plain Python object standing in
  front of one C++ QHttpNetworkHeader.

  What exists
  -----------

  Every function of Qt's QHttpNetworkHeader that has a ritual and that Python
  can call so far, 9 names in all: 'url', 'setUrl', 'majorVersion',
  'minorVersion', 'contentLength', 'setContentLength', 'header',
  'headerField', 'setHeaderField'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpNetworkHeader::~QHttpNetworkHeader()': the destructor: Python
    never removes a C++ QHttpNetworkHeader.

  What to expect
  --------------

  - The C++ QHttpNetworkHeader is created at the first use, not by
    'QHttpNetworkHeader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpNetworkHeader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkHeader'

  #  A C++ QHttpNetworkHeader Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpNetworkHeader'

  #  The functions Qt calls itself that QHttpNetworkHeader is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'url': (
          ('_ZNK18QHttpNetworkHeader3urlEv',
           ('address', 'value', 'QtCore:QUrl'),
           ()),
      ),
      'setUrl': (
          ('_ZN18QHttpNetworkHeader6setUrlERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'majorVersion': (
          ('_ZNK18QHttpNetworkHeader12majorVersionEv',
           ('int', 'number', ''),
           ()),
      ),
      'minorVersion': (
          ('_ZNK18QHttpNetworkHeader12minorVersionEv',
           ('int', 'number', ''),
           ()),
      ),
      'contentLength': (
          ('_ZNK18QHttpNetworkHeader13contentLengthEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setContentLength': (
          ('_ZN18QHttpNetworkHeader16setContentLengthEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'header': (
          ('_ZNK18QHttpNetworkHeader6headerEv',
           ('address', 'value', 'QtNetwork:QHttpHeaders'),
           ()),
      ),
      'headerField': (
          ('_ZNK18QHttpNetworkHeader11headerFieldE14QByteArrayViewRK10QByte'
           'Array',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('address', 'value', 'QtCore:QByteArrayView'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'setHeaderField': (
          ('_ZN18QHttpNetworkHeader14setHeaderFieldERK10QByteArrayS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
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

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHttpNetworkHeader::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkheader.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHttpNetworkHeader::url() const
    address = self._callAs(
        'QHttpNetworkHeader', 'ritual_ZNK18QHttpNetworkHeader3urlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def majorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkHeader::majorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheader.html#majorVersion
    """
    #  int QHttpNetworkHeader::majorVersion() const
    return self._callAs(
        'QHttpNetworkHeader',
        'ritual_ZNK18QHttpNetworkHeader12majorVersionEv',
    )

  def minorVersion(self) -> int:
    """
    Calls Qt's 'int QHttpNetworkHeader::minorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheader.html#minorVersion
    """
    #  int QHttpNetworkHeader::minorVersion() const
    return self._callAs(
        'QHttpNetworkHeader',
        'ritual_ZNK18QHttpNetworkHeader12minorVersionEv',
    )

  def contentLength(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkHeader::contentLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheader.html#contentLength
    """
    #  qint64 QHttpNetworkHeader::contentLength() const
    return self._callAs(
        'QHttpNetworkHeader',
        'ritual_ZNK18QHttpNetworkHeader13contentLengthEv',
    )

  def header(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QHttpNetworkHeader::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkheader.html#header

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QHttpNetworkHeader::header() const
    address = self._callAs(
        'QHttpNetworkHeader', 'ritual_ZNK18QHttpNetworkHeader6headerEv',
    )
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  @overload(QByteArrayView)
  @overload(QByteArrayView, QByteArray)
  def headerField(
      self,
      name: QByteArrayView,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkHeader::headerField(QByteArrayView
    name, const QByteArray &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheader.html#headerField

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
    #  QByteArray QHttpNetworkHeader::headerField(QByteArrayView name, const
    #      QByteArray &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArray
      defaultValue = QByteArray()
    address = self._callAs(
        'QHttpNetworkHeader',
        'ritual_ZNK18QHttpNetworkHeader11headerFieldE14QByteArrayViewRK10QB'
        'yteArray',
        self._valueOf(name), self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeader::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkheader.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QHttpNetworkHeader::setUrl(const QUrl &url)
    self._callAs(
        'QHttpNetworkHeader', 'ritual_ZN18QHttpNetworkHeader6setUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(int)
  def setContentLength(self, length: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeader::setContentLength(qint64 length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheader.html#setContentLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QHttpNetworkHeader::setContentLength(qint64 length)
    self._callAs(
        'QHttpNetworkHeader',
        'ritual_ZN18QHttpNetworkHeader16setContentLengthEx',
        length,
    )

  @overload(QByteArray, QByteArray)
  def setHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeader::setHeaderField(const QByteArray
    &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheader.html#setHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkHeader::setHeaderField(const QByteArray &name, const
    #      QByteArray &data)
    self._callAs(
        'QHttpNetworkHeader',
        'ritual_ZN18QHttpNetworkHeader14setHeaderFieldERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(data),
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
