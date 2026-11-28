"""
QWebEngineHistoryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineHistoryPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QWebEngineHistoryPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineHistoryPrivate: a plain Python object
  standing in front of one C++ QWebEngineHistoryPrivate.

  What exists
  -----------

  Every function of Qt's QWebEngineHistoryPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'updateItems',
  'urlOrImageProviderUrl'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QWebEngineHistoryPrivate::QWebEngineHistoryPrivate(QtWebEngineCore::
    WebContentsAdapterClient *client, const ImageProviderUrl
    &imageProviderUrl)': names 'QtWebEngineCore::WebContentsAdapterClient',
    which has no cute class yet.
  - Qt's 'QWebEngineHistoryPrivate::~QWebEngineHistoryPrivate()': the
    destructor: Python never removes a C++ QWebEngineHistoryPrivate.
  - Qt's 'QtWebEngineCore::WebContentsAdapter
    *QWebEngineHistoryPrivate::adapter() const': gives
    'QtWebEngineCore::WebContentsAdapter', which has no cute class yet.

  What to expect
  --------------

  - The C++ QWebEngineHistoryPrivate is created at the first use, not by
    'QWebEngineHistoryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineHistoryPrivate.
  - Each name of Qt's QWebEngineHistoryPrivate that has no cute function yet,
    '__init__', 'adapter', holds a function that raises
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
  __qt_class__ = 'QWebEngineHistoryPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def urlOrImageProviderUrl(self, url: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineHistoryPrivate::urlOrImageProviderUrl(const
    QUrl &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistoryprivate.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineHistoryPrivate::urlOrImageProviderUrl(const QUrl &url)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QWebEngineHistoryPrivate21urlOrImageProviderUrlERK4QUr'
        'l',
        self._valueOf(url),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
    Qt's
    'QWebEngineHistoryPrivate::QWebEngineHistoryPrivate(QtWebEngineCore::
    WebContentsAdapterClient *client, const ImageProviderUrl
    &imageProviderUrl)': names 'QtWebEngineCore::WebContentsAdapterClient',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryPrivate.__init__' has no cute function yet. Qt's "
        "'QWebEngineHistoryPrivate::QWebEngineHistoryPrivate(QtWebEngineCore"
        "::WebContentsAdapterClient *client, const ImageProviderUrl "
        "&imageProviderUrl)': names "
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

  def updateItems(self) -> None:
    """
    Calls Qt's 'void QWebEngineHistoryPrivate::updateItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistoryprivate.html#updateItems
    """
    #  void QWebEngineHistoryPrivate::updateItems() const
    self.uglySide.call('ritual_ZNK24QWebEngineHistoryPrivate11updateItemsEv')

  @staticmethod
  def adapter(*__, **_) -> Never:
    """
    Qt's 'QtWebEngineCore::WebContentsAdapter
    *QWebEngineHistoryPrivate::adapter() const': gives
    'QtWebEngineCore::WebContentsAdapter', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryPrivate.adapter' has no cute function yet. Qt's "
        "'QtWebEngineCore::WebContentsAdapter "
        "*QWebEngineHistoryPrivate::adapter() const': gives "
        "'QtWebEngineCore::WebContentsAdapter', which has no cute class yet."
    )
