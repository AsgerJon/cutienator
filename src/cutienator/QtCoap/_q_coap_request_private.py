"""
QCoapRequestPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoaprequest_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapRequestPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QtCoap, QCoapMessagePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QCoapRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCoapRequest = WAIT['QCoapRequest']
  QUrl = WAIT['QUrl']


class QCoapRequestPrivate(QCoapMessagePrivate):
  """
  The cute side of Qt's QCoapRequestPrivate: a plain Python object standing
  in front of one C++ QCoapRequestPrivate.

  It is built on the cute 'QCoapMessagePrivate', as Qt's QCoapRequestPrivate
  is built on Qt's QCoapMessagePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapRequestPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'clone', 'setUrl', 'adjustUrl',
  'createRequest'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapRequestPrivate::~QCoapRequestPrivate()': the destructor:
    Python never removes a C++ QCoapRequestPrivate.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QCoapMessagePrivate.

  What to expect
  --------------

  - The C++ QCoapRequestPrivate is created at the first use, not by
    'QCoapRequestPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapRequestPrivate.
  - Each name of Qt's QCoapRequestPrivate that has no cute function yet,
    '__init__', 'adjustedUrl', 'isUrlValid', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCoapRequest, QtCoap.Method)
  @overload(QCoapRequest, QtCoap.Method, bool)
  def createRequest(
      other: QCoapRequest,
      method: QtCoap.Method,
      isSecure: bool = False,
  ) -> QCoapRequest:
    """
    Calls Qt's 'QCoapRequest QCoapRequestPrivate::createRequest(const
    QCoapRequest &other, QtCoap::Method method, bool isSecure)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoaprequestprivate.html#createRequest

    Parameters
    ----------

    other : QCoapRequest
      Passed on as a value: Qt reads the C++ QCoapRequest, which stays
      Python's own.

    method : QtCoap.Method
      Passed on as its number.

    isSecure : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QCoapRequest
      A new cute QCoapRequest around the copy Qt gave back. Python owns it.
    """
    #  QCoapRequest QCoapRequestPrivate::createRequest(const QCoapRequest
    #      &other, QtCoap::Method method, bool isSecure)
    address = Rituals.call(
        'ritual_ZN19QCoapRequestPrivate13createRequestERK12QCoapRequestN6Qt'
        'Coap6MethodEb',
        CuteMixin._valueOf(other), method.value, isSecure,
    )
    from . import QCoapRequest
    return QCoapRequest._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapRequestPrivate'

  #  A C++ QCoapRequestPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapRequestPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QCoapRequestPrivate]:
    """
    Calls Qt's 'QCoapRequestPrivate *QCoapRequestPrivate::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequestprivate.html#clone

    Returns
    -------

    Optional[QCoapRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapRequestPrivate *QCoapRequestPrivate::clone() const
    address = self.uglySide.call('ritual_ZNK19QCoapRequestPrivate5cloneEv')
    return QCoapRequestPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QCoapRequestPrivate::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequestprivate.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QCoapRequestPrivate::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN19QCoapRequestPrivate6setUrlERK4QUrl', self._valueOf(url),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QCoapRequestPrivate::QCoapRequestPrivate(const QUrl &url,
      QCoapMessage::Type type, const QUrl &proxyUrl)': leans on
      'QCoapMessagePrivate::QCoapMessagePrivate(QCoapMessage::Type)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'QCoapRequestPrivate::QCoapRequestPrivate(const
      QCoapRequestPrivate &other)': leans on
      'QCoapMessagePrivate::QCoapMessagePrivate(QCoapMessagePrivate const&)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapRequestPrivate.__init__' has no cute function yet. Qt's "
        "'QCoapRequestPrivate::QCoapRequestPrivate(const QUrl &url, "
        "QCoapMessage::Type type, const QUrl &proxyUrl)': leans on "
        "'QCoapMessagePrivate::QCoapMessagePrivate(QCoapMessage::Type)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's "
        "'QCoapRequestPrivate::QCoapRequestPrivate(const "
        "QCoapRequestPrivate &other)': leans on "
        "'QCoapMessagePrivate::QCoapMessagePrivate(QCoapMessagePrivate "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(bool)
  def adjustUrl(self, secure: bool) -> None:
    """
    Calls Qt's 'void QCoapRequestPrivate::adjustUrl(bool secure)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoaprequestprivate.html#adjustUrl

    Parameters
    ----------

    secure : bool
      Passed on as it is.
    """
    #  void QCoapRequestPrivate::adjustUrl(bool secure)
    self.uglySide.call('ritual_ZN19QCoapRequestPrivate9adjustUrlEb', secure)

  @staticmethod
  def adjustedUrl(*__, **_) -> Never:
    """
    Qt's 'QUrl QCoapRequestPrivate::adjustedUrl(const QUrl &url, bool
    secure)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'CoapSecureScheme'; did you mean 'QWebEngineUrlScheme::SecureScheme'?.
    """
    raise NotImplementedError(
        "'QCoapRequestPrivate.adjustedUrl' has no cute function yet. Qt's "
        "'QUrl QCoapRequestPrivate::adjustedUrl(const QUrl &url, bool "
        "secure)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'CoapSecureScheme'; did you mean "
        "'QWebEngineUrlScheme::SecureScheme'?.")

  @staticmethod
  def isUrlValid(*__, **_) -> Never:
    """
    Qt's 'bool QCoapRequestPrivate::isUrlValid(const QUrl &url)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'CoapScheme'.
    """
    raise NotImplementedError(
        "'QCoapRequestPrivate.isUrlValid' has no cute function yet. Qt's "
        "'bool QCoapRequestPrivate::isUrlValid(const QUrl &url)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'CoapScheme'.")
