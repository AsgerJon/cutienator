"""
QNetworkRequestFactoryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkrequestfactory_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkRequestFactoryPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
  from . import QNetworkRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QNetworkRequestFactoryPrivate(QSharedData):
  """
  The cute side of Qt's QNetworkRequestFactoryPrivate: a plain Python object
  standing in front of one C++ QNetworkRequestFactoryPrivate.

  It is built on the cute 'QSharedData', as Qt's
  QNetworkRequestFactoryPrivate is built on Qt's QSharedData, and has
  everything that class has.

  C++ hands a QNetworkRequestFactoryPrivate around as a copy, so every C++
  QNetworkRequestFactoryPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QNetworkRequestFactoryPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'newRequest'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkRequestFactoryPrivate::~QNetworkRequestFactoryPrivate()':
    the destructor: Python removes its C++ QNetworkRequestFactoryPrivate by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QNetworkRequestFactoryPrivate is created at the first use, not by
    'QNetworkRequestFactoryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkRequestFactoryPrivate back gives a copy the
    ritual made for Python, in a new cute QNetworkRequestFactoryPrivate.
  - Each name of Qt's QNetworkRequestFactoryPrivate that has no cute function
    yet, 'requestUrl', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkRequestFactoryPrivate'

  #  Qt's '~QNetworkRequestFactoryPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QNetworkRequestFactoryPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QNetworkRequestFactoryPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def newRequest(self, url: QUrl) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest
    QNetworkRequestFactoryPrivate::newRequest(const QUrl &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactoryprivate.html#newRequest

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QNetworkRequestFactoryPrivate::newRequest(const QUrl
    #      &url) const
    address = self.uglySide.call(
        'ritual_ZNK29QNetworkRequestFactoryPrivate10newRequestERK4QUrl',
        self._valueOf(url),
    )
    from . import QNetworkRequest
    return QNetworkRequest._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QNetworkRequestFactoryPrivate::QNetworkRequestFactoryPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactoryprivate.html
    """
    #  QNetworkRequestFactoryPrivate::QNetworkRequestFactoryPrivate()
    self._noteCreation(QNetworkRequestFactoryPrivate, lambda: Rituals.call(
        'ritual_ZN29QNetworkRequestFactoryPrivateC1Ev',
    ))

  @overload(QUrl)
  def __init__(self, baseUrl: QUrl) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkRequestFactoryPrivate::QNetworkRequestFactoryPrivate(const QUrl
    &baseUrl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkrequestfactoryprivate.html

    Parameters
    ----------

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QNetworkRequestFactoryPrivate::QNetworkRequestFactoryPrivate(const
    #      QUrl &baseUrl)
    self._noteCreation(QNetworkRequestFactoryPrivate, lambda: Rituals.call(
        'ritual_ZN29QNetworkRequestFactoryPrivateC1ERK4QUrl',
        self._valueOf(baseUrl),
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

  @staticmethod
  def requestUrl(*__, **_) -> Never:
    """
    Qt's 'QUrl QNetworkRequestFactoryPrivate::requestUrl(const QString *path,
    const QUrlQuery *query) const': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'lcQrequestfactory'.
    """
    raise NotImplementedError(
        "'QNetworkRequestFactoryPrivate.requestUrl' has no cute function "
        "yet. Qt's 'QUrl QNetworkRequestFactoryPrivate::requestUrl(const "
        "QString *path, const QUrlQuery *query) const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'lcQrequestfactory'.")
