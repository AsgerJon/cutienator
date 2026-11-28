"""
QWebEngineHistoryItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineHistoryItemPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWebEngineHistoryItemPrivate(QSharedData):
  """
  The cute side of Qt's QWebEngineHistoryItemPrivate: a plain Python object
  standing in front of one C++ QWebEngineHistoryItemPrivate.

  It is built on the cute 'QSharedData', as Qt's QWebEngineHistoryItemPrivate
  is built on Qt's QSharedData, and has everything that class has.

  C++ hands a QWebEngineHistoryItemPrivate around as a copy, so every C++
  QWebEngineHistoryItemPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QWebEngineHistoryItemPrivate yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineHistoryItemPrivate::QWebEngineHistoryItemPrivate(
    QtWebEngineCore::WebContentsAdapterClient *client, int index)': names
    'QtWebEngineCore::WebContentsAdapterClient', which has no cute class yet.
  - Qt's 'QWebEngineHistoryItemPrivate::~QWebEngineHistoryItemPrivate()': the
    destructor: Python removes its C++ QWebEngineHistoryItemPrivate by it,
    and has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QWebEngineHistoryItemPrivate is created at the first use, not by
    'QWebEngineHistoryItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineHistoryItemPrivate back gives a copy the
    ritual made for Python, in a new cute QWebEngineHistoryItemPrivate.
  - Each name of Qt's QWebEngineHistoryItemPrivate that has no cute function
    yet, '__init__', 'adapter', holds a function that raises
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
  __qt_class__ = 'QWebEngineHistoryItemPrivate'

  #  Qt's '~QWebEngineHistoryItemPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineHistoryItemPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QWebEngineHistoryItemPrivateD1Ev'

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
    Qt's 'QWebEngineHistoryItemPrivate::QWebEngineHistoryItemPrivate(
    QtWebEngineCore::WebContentsAdapterClient *client, int index)': names
    'QtWebEngineCore::WebContentsAdapterClient', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryItemPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QWebEngineHistoryItemPrivate::QWebEngineHistoryItemPrivate(QtWebEn"
        "gineCore::WebContentsAdapterClient *client, int index)': names "
        "'QtWebEngineCore::WebContentsAdapterClient', which has no cute "
        "class yet.")

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
  def adapter(*__, **_) -> Never:
    """
    Qt's 'QtWebEngineCore::WebContentsAdapter
    *QWebEngineHistoryItemPrivate::adapter() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type
    'QtWebEngineCore::WebContentsAdapterClient'.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryItemPrivate.adapter' has no cute function yet. "
        "Qt's 'QtWebEngineCore::WebContentsAdapter "
        "*QWebEngineHistoryItemPrivate::adapter() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QtWebEngineCore::WebContentsAdapterClient'.")
