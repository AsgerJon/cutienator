"""
QWebViewFactory::LoadingInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebView/6.12.0/QtWebView/private/qwebviewfactory_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QWebViewFactory::LoadingInfo to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QWebViewLoadingInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class LoadingInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebViewFactory::LoadingInfo: a plain Python object
  standing in front of one C++ QWebViewFactory::LoadingInfo.

  C++ hands a QWebViewFactory::LoadingInfo around as a copy, so every C++
  QWebViewFactory::LoadingInfo behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebViewFactory::LoadingInfo that has a ritual and
  that Python can call so far, 1 name in all: 'create'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebViewFactory::LoadingInfo::~LoadingInfo()': the destructor:
    Python removes its C++ QWebViewFactory::LoadingInfo by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ QWebViewFactory::LoadingInfo is created at the first use, not by
    'QWebViewFactory::LoadingInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebViewFactory::LoadingInfo back gives a copy the
    ritual made for Python, in a new cute QWebViewFactory::LoadingInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUrl, QWebViewLoadingInfo.LoadStatus, str)
  def create(
      url: QUrl,
      status: QWebViewLoadingInfo.LoadStatus,
      errorString: str,
  ) -> QWebViewLoadingInfo:
    """
    Calls Qt's 'QWebViewLoadingInfo
    QWebViewFactory::LoadingInfo::create(const QUrl &url,
    QWebViewLoadingInfo::LoadStatus status, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewfactory-loadinginfo.html#create

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    status : QWebViewLoadingInfo.LoadStatus
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QWebViewLoadingInfo
      A new cute QWebViewLoadingInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QWebViewLoadingInfo QWebViewFactory::LoadingInfo::create(const QUrl
    #      &url, QWebViewLoadingInfo::LoadStatus status, const QString
    #      &errorString)
    address = Rituals.call(
        'ritual_ZN15QWebViewFactory11LoadingInfo6createERK4QUrlN19QWebViewL'
        'oadingInfo10LoadStatusERK7QString',
        CuteMixin._valueOf(url), status.value, errorString,
    )
    return QWebViewLoadingInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebViewFactory::LoadingInfo'

  #  Qt's '~QWebViewFactory::LoadingInfo()'. Naming it makes this a value
  #  class: Python owns every C++ QWebViewFactory::LoadingInfo behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN15QWebViewFactory11LoadingInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
