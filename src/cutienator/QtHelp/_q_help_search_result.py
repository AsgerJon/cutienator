"""
QHelpSearchResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpsearchresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QHelpSearchResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHelpSearchResult: a plain Python object standing in
  front of one C++ QHelpSearchResult.

  C++ hands a QHelpSearchResult around as a copy, so every C++
  QHelpSearchResult behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHelpSearchResult that has a ritual and that Python
  can call so far, 3 names in all: 'title', 'url', 'snippet'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHelpSearchResult::~QHelpSearchResult()': the destructor: Python
    removes its C++ QHelpSearchResult by it, and has no other use for it.
  - Qt's 'QHelpSearchResult &QHelpSearchResult::operator=(const
    QHelpSearchResult &other)': assignment: Python binds a name and has no
    operator for it.

  What to expect
  --------------

  - The C++ QHelpSearchResult is created at the first use, not by
    'QHelpSearchResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHelpSearchResult back gives a copy the ritual made
    for Python, in a new cute QHelpSearchResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpSearchResult'

  #  Qt's '~QHelpSearchResult()'. Naming it makes this a value class: Python
  #  owns every C++ QHelpSearchResult behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QHelpSearchResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def title(self) -> str:
    """
    Calls Qt's 'QString QHelpSearchResult::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchresult.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpSearchResult::title() const
    return self.uglySide.call('ritual_ZNK17QHelpSearchResult5titleEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHelpSearchResult::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchresult.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHelpSearchResult::url() const
    address = self.uglySide.call('ritual_ZNK17QHelpSearchResult3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def snippet(self) -> str:
    """
    Calls Qt's 'QString QHelpSearchResult::snippet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchresult.html#snippet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpSearchResult::snippet() const
    return self.uglySide.call('ritual_ZNK17QHelpSearchResult7snippetEv')

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
    Notes what was given, for Qt's 'QHelpSearchResult::QHelpSearchResult()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresult.html#QHelpSearchResult
    """
    #  QHelpSearchResult::QHelpSearchResult()
    self._noteCreation(QHelpSearchResult, lambda: Rituals.call(
        'ritual_ZN17QHelpSearchResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHelpSearchResult) -> None:
    """
    Notes what was given, for Qt's
    'QHelpSearchResult::QHelpSearchResult(const QHelpSearchResult &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresult.html#QHelpSearchResult

    Parameters
    ----------

    other : QHelpSearchResult
      Passed on as a value: Qt reads the C++ QHelpSearchResult, which stays
      Python's own.
    """
    #  QHelpSearchResult::QHelpSearchResult(const QHelpSearchResult &other)
    self._noteCreation(QHelpSearchResult, lambda: Rituals.call(
        'ritual_ZN17QHelpSearchResultC1ERKS_', self._valueOf(other),
    ))

  @overload(QUrl, str, str)
  def __init__(self, url: QUrl, title: str, snippet: str) -> None:
    """
    Notes what was given, for Qt's
    'QHelpSearchResult::QHelpSearchResult(const QUrl &url, const QString
    &title, const QString &snippet)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchresult.html#QHelpSearchResult

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    title : str
      Passed on as it is: a QString is made of it for the call.

    snippet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QHelpSearchResult::QHelpSearchResult(const QUrl &url, const QString
    #      &title, const QString &snippet)
    self._noteCreation(QHelpSearchResult, lambda: Rituals.call(
        'ritual_ZN17QHelpSearchResultC1ERK4QUrlRK7QStringS5_',
        self._valueOf(url), title, snippet,
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


#  Qt's 'QList<QHelpSearchResult>': the list of QHelpSearchResult, which
#  'QList[QHelpSearchResult]' gives. It is made here, so that there is one as
#  soon as there can be a QHelpSearchResult.
QList.createKind(
    QHelpSearchResult, 'value',
    make='ritual_list_make_QHelpSearchResult',
    add='ritual_list_add_QHelpSearchResult',
    size='ritual_list_size_QHelpSearchResult',
    at='ritual_list_at_QHelpSearchResult',
    drop='ritual_list_drop_QHelpSearchResult',
)
