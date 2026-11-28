"""
QCoapRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoaprequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtCoap, QCoapMessage

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from . import QCoapRequestPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCoapRequest(QCoapMessage):
  """
  The cute side of Qt's QCoapRequest: a plain Python object standing in front
  of one C++ QCoapRequest.

  It is built on the cute 'QCoapMessage', as Qt's QCoapRequest is built on
  Qt's QCoapMessage, and has everything that class has.

  C++ hands a QCoapRequest around as a copy, so every C++ QCoapRequest behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCoapRequest that has a ritual and that Python can
  call so far, 8 names in all: 'url', 'proxyUrl', 'method', 'isObserve',
  'setUrl', 'setProxyUrl', 'enableObserve', 'd_func'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapRequest::~QCoapRequest()': the destructor: Python removes its
    C++ QCoapRequest by it, and has no other use for it.
  - Qt's 'QCoapRequest &QCoapRequest::operator=(const QCoapRequest &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'const QCoapRequestPrivate *QCoapRequest::d_func() const': takes in
    Python what 'QCoapRequestPrivate *QCoapRequest::d_func()' takes.

  What to expect
  --------------

  - The C++ QCoapRequest is created at the first use, not by
    'QCoapRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapRequest back gives a copy the ritual made for
    Python, in a new cute QCoapRequest.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapRequest'

  #  Qt's '~QCoapRequest()'. Naming it makes this a value class: Python owns
  #  every C++ QCoapRequest behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QCoapRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QCoapRequest::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QCoapRequest::url() const
    address = self.uglySide.call('ritual_ZNK12QCoapRequest3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def proxyUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QCoapRequest::proxyUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#proxyUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QCoapRequest::proxyUrl() const
    address = self.uglySide.call('ritual_ZNK12QCoapRequest8proxyUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def method(self) -> QtCoap.Method:
    """
    Calls Qt's 'QtCoap::Method QCoapRequest::method() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#method

    Returns
    -------

    QtCoap.Method
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QtCoap.Method(number)'
      gives.
    """
    #  QtCoap::Method QCoapRequest::method() const
    return QtCoap.Method(self.uglySide.call(
        'ritual_ZNK12QCoapRequest6methodEv',
    ))

  def isObserve(self) -> bool:
    """
    Calls Qt's 'bool QCoapRequest::isObserve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#isObserve
    """
    #  bool QCoapRequest::isObserve() const
    return self.uglySide.call('ritual_ZNK12QCoapRequest9isObserveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QCoapRequest::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QCoapRequest::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN12QCoapRequest6setUrlERK4QUrl', self._valueOf(url),
    )

  @overload(QUrl)
  def setProxyUrl(self, proxyUrl: QUrl) -> None:
    """
    Calls Qt's 'void QCoapRequest::setProxyUrl(const QUrl &proxyUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#setProxyUrl

    Parameters
    ----------

    proxyUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QCoapRequest::setProxyUrl(const QUrl &proxyUrl)
    self.uglySide.call(
        'ritual_ZN12QCoapRequest11setProxyUrlERK4QUrl',
        self._valueOf(proxyUrl),
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
  @overload(QUrl)
  @overload(QUrl, QCoapMessage.Type)
  @overload(QUrl, QCoapMessage.Type, QUrl)
  def __init__(
      self,
      url: Optional[QUrl] = None,
      type: QCoapMessage.Type = QCoapMessage.Type.NonConfirmable,
      proxyUrl: Optional[QUrl] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCoapRequest::QCoapRequest(const QUrl
    &url, Type type, const QUrl &proxyUrl)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#QCoapRequest

    Parameters
    ----------

    url : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.

    type : QCoapMessage.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QCoapMessage.Type.NonConfirmable.

    proxyUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  QCoapRequest::QCoapRequest(const QUrl &url, Type type, const QUrl
    #      &proxyUrl)
    if url is None:
      from ..QtCore import QUrl
      url = QUrl()
    if proxyUrl is None:
      from ..QtCore import QUrl
      proxyUrl = QUrl()
    self._noteCreation(QCoapRequest, lambda: Rituals.call(
        'ritual_ZN12QCoapRequestC1ERK4QUrlN12QCoapMessage4TypeES2_',
        self._valueOf(url), type.value, self._valueOf(proxyUrl),
    ))

  @overload(str)
  @overload(NoneType)
  @overload(str, QCoapMessage.Type)
  @overload(NoneType, QCoapMessage.Type)
  def __init__(
      self,
      url: Optional[str],
      type: QCoapMessage.Type = QCoapMessage.Type.NonConfirmable,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCoapRequest::QCoapRequest(const char
    *url, Type type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#QCoapRequest

    Parameters
    ----------

    url : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : QCoapMessage.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QCoapMessage.Type.NonConfirmable.
    """
    #  QCoapRequest::QCoapRequest(const char *url, Type type)
    self._noteCreation(QCoapRequest, lambda: Rituals.call(
        'ritual_ZN12QCoapRequestC1EPKcN12QCoapMessage4TypeE',
        self._bytesOf(url), type.value,
    ))

  @overload(THIS)
  def __init__(self, other: QCoapRequest) -> None:
    """
    Notes what was given, for Qt's 'QCoapRequest::QCoapRequest(const
    QCoapRequest &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#QCoapRequest

    Parameters
    ----------

    other : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.
    """
    #  QCoapRequest::QCoapRequest(const QCoapRequest &other)
    self._noteCreation(QCoapRequest, lambda: Rituals.call(
        'ritual_ZN12QCoapRequestC1ERKS_', self._valueOf(other),
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

  def enableObserve(self) -> None:
    """
    Calls Qt's 'void QCoapRequest::enableObserve()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#enableObserve
    """
    #  void QCoapRequest::enableObserve()
    self.uglySide.call('ritual_ZN12QCoapRequest13enableObserveEv')

  def d_func(self) -> Optional[QCoapRequestPrivate]:
    """
    Calls Qt's 'QCoapRequestPrivate *QCoapRequest::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequest.html#d_func

    Returns
    -------

    Optional[QCoapRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapRequestPrivate *QCoapRequest::d_func()
    address = self.uglySide.call('ritual_ZN12QCoapRequest6d_funcEv')
    from . import QCoapRequestPrivate
    return QCoapRequestPrivate._cuteAt(address)
