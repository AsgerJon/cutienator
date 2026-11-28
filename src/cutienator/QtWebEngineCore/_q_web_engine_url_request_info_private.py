"""
QWebEngineUrlRequestInfoPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineurlrequestinfo_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineUrlRequestInfoPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from . import QWebEngineUrlRequestInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QWebEngineUrlRequestInfoPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineUrlRequestInfoPrivate: a plain Python
  object standing in front of one C++ QWebEngineUrlRequestInfoPrivate.

  C++ hands a QWebEngineUrlRequestInfoPrivate around as a copy, so every C++
  QWebEngineUrlRequestInfoPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineUrlRequestInfoPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWebEngineUrlRequestInfo
    *QWebEngineUrlRequestInfoPrivate::q_func() const': takes in Python what
    'QWebEngineUrlRequestInfo *QWebEngineUrlRequestInfoPrivate::q_func()'
    takes.
  - Qt's 'QWebEngineUrlRequestInfoPrivate::QWebEngineUrlRequestInfoPrivate(
    QWebEngineUrlRequestInfo::ResourceType resource,
    QWebEngineUrlRequestInfo::NavigationType navigation, const QUrl &u, const
    QUrl &fpu, const QUrl &i, const QByteArray &m,
    QtWebEngineCore::ResourceRequestBody *const rb, const QHash<QByteArray,
    QByteArray> &h, bool isDownload)': takes a type Python has no way to hand
    over yet.
  - Qt's
    'QWebEngineUrlRequestInfoPrivate::~QWebEngineUrlRequestInfoPrivate()':
    the destructor: Python removes its C++ QWebEngineUrlRequestInfoPrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QWebEngineUrlRequestInfoPrivate is created at the first use, not
    by 'QWebEngineUrlRequestInfoPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineUrlRequestInfoPrivate back gives a copy the
    ritual made for Python, in a new cute QWebEngineUrlRequestInfoPrivate.
  - Each name of Qt's QWebEngineUrlRequestInfoPrivate that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineUrlRequestInfoPrivate'

  #  Qt's '~QWebEngineUrlRequestInfoPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineUrlRequestInfoPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QWebEngineUrlRequestInfoPrivateD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebEngineUrlRequestInfoPrivate::QWebEngineUrlRequestInfoPrivate(
    QWebEngineUrlRequestInfo::ResourceType resource,
    QWebEngineUrlRequestInfo::NavigationType navigation, const QUrl &u, const
    QUrl &fpu, const QUrl &i, const QByteArray &m,
    QtWebEngineCore::ResourceRequestBody *const rb, const QHash<QByteArray,
    QByteArray> &h, bool isDownload)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QWebEngineUrlRequestInfoPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QWebEngineUrlRequestInfoPrivate::QWebEngineUrlRequestInfoPrivate(Q"
        "WebEngineUrlRequestInfo::ResourceType resource, "
        "QWebEngineUrlRequestInfo::NavigationType navigation, const QUrl "
        "&u, const QUrl &fpu, const QUrl &i, const QByteArray &m, "
        "QtWebEngineCore::ResourceRequestBody *const rb, const "
        "QHash<QByteArray, QByteArray> &h, bool isDownload)': takes a type "
        "Python has no way to hand over yet.")

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

  def q_func(self) -> Optional[QWebEngineUrlRequestInfo]:
    """
    Calls Qt's 'QWebEngineUrlRequestInfo
    *QWebEngineUrlRequestInfoPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlrequestinfoprivate.html#q_func

    Returns
    -------

    Optional[QWebEngineUrlRequestInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineUrlRequestInfo *QWebEngineUrlRequestInfoPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN31QWebEngineUrlRequestInfoPrivate6q_funcEv',
    )
    return QWebEngineUrlRequestInfo._cuteAt(address)
