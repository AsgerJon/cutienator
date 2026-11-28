"""
QPlaceProposedSearchResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceproposedsearchresult.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QPlaceSearchResult

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlaceProposedSearchResultPrivate, QPlaceSearchRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']


class QPlaceProposedSearchResult(QPlaceSearchResult):
  """
  The cute side of Qt's QPlaceProposedSearchResult: a plain Python object
  standing in front of one C++ QPlaceProposedSearchResult.

  It is built on the cute 'QPlaceSearchResult', as Qt's
  QPlaceProposedSearchResult is built on Qt's QPlaceSearchResult, and has
  everything that class has.

  C++ hands a QPlaceProposedSearchResult around as a copy, so every C++
  QPlaceProposedSearchResult behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPlaceProposedSearchResult that has a ritual and
  that Python can call so far, 3 names in all: 'searchRequest',
  'setSearchRequest', 'd_func'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceProposedSearchResult::~QPlaceProposedSearchResult()': the
    destructor: Python removes its C++ QPlaceProposedSearchResult by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 leans on
  'QSharedDataPointer<QPlaceSearchResultPrivate>.

  What to expect
  --------------

  - The C++ QPlaceProposedSearchResult is created at the first use, not by
    'QPlaceProposedSearchResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceProposedSearchResult back gives a copy the
    ritual made for Python, in a new cute QPlaceProposedSearchResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceProposedSearchResult'

  #  Qt's '~QPlaceProposedSearchResult()'. Naming it makes this a value
  #  class: Python owns every C++ QPlaceProposedSearchResult behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QPlaceProposedSearchResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def searchRequest(self) -> QPlaceSearchRequest:
    """
    Calls Qt's 'QPlaceSearchRequest
    QPlaceProposedSearchResult::searchRequest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceproposedsearchresult.html#searchRequest

    Returns
    -------

    QPlaceSearchRequest
      A new cute QPlaceSearchRequest around the copy Qt gave back. Python
      owns it.
    """
    #  QPlaceSearchRequest QPlaceProposedSearchResult::searchRequest() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlaceProposedSearchResult13searchRequestEv',
    )
    from . import QPlaceSearchRequest
    return QPlaceSearchRequest._cuteOwning(address)

  def d_func(self) -> Optional[QPlaceProposedSearchResultPrivate]:
    """
    Calls Qt's 'const QPlaceProposedSearchResultPrivate
    *QPlaceProposedSearchResult::d_func() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceproposedsearchresult.html#d_func

    Returns
    -------

    Optional[QPlaceProposedSearchResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlaceProposedSearchResultPrivate
    #      *QPlaceProposedSearchResult::d_func() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlaceProposedSearchResult6d_funcEv',
    )
    from . import QPlaceProposedSearchResultPrivate
    return QPlaceProposedSearchResultPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlaceSearchRequest)
  def setSearchRequest(self, request: QPlaceSearchRequest) -> None:
    """
    Calls Qt's 'void QPlaceProposedSearchResult::setSearchRequest(const
    QPlaceSearchRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceproposedsearchresult.html#setSearchRequest

    Parameters
    ----------

    request : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  void QPlaceProposedSearchResult::setSearchRequest(const
    #      QPlaceSearchRequest &request)
    self.uglySide.call(
        'ritual_ZN26QPlaceProposedSearchResult16setSearchRequestERK19QPlace'
        'SearchRequest',
        self._valueOf(request),
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
    Notes what was given, for Qt's
    'QPlaceProposedSearchResult::QPlaceProposedSearchResult()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceproposedsearchresult.html
    """
    #  QPlaceProposedSearchResult::QPlaceProposedSearchResult()
    self._noteCreation(QPlaceProposedSearchResult, lambda: Rituals.call(
        'ritual_ZN26QPlaceProposedSearchResultC1Ev',
    ))

  @overload(QPlaceSearchResult)
  def __init__(self, other: QPlaceSearchResult) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceProposedSearchResult::QPlaceProposedSearchResult(const
    QPlaceSearchResult &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceproposedsearchresult.html

    Parameters
    ----------

    other : QPlaceSearchResult
      Passed on as a value: Qt reads the C++ QPlaceSearchResult, which stays
      Python's own.
    """
    #  QPlaceProposedSearchResult::QPlaceProposedSearchResult(const
    #      QPlaceSearchResult &other)
    self._noteCreation(QPlaceProposedSearchResult, lambda: Rituals.call(
        'ritual_ZN26QPlaceProposedSearchResultC1ERK18QPlaceSearchResult',
        self._valueOf(other),
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
