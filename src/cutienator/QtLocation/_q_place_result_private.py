"""
QPlaceResultPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qplaceresult_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QPlaceResultPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QPlaceSearchResult, QPlaceSearchResultPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceResultPrivate(QPlaceSearchResultPrivate):
  """
  The cute side of Qt's QPlaceResultPrivate: a plain Python object standing
  in front of one C++ QPlaceResultPrivate.

  It is built on the cute 'QPlaceSearchResultPrivate', as Qt's
  QPlaceResultPrivate is built on Qt's QPlaceSearchResultPrivate, and has
  everything that class has.

  C++ hands a QPlaceResultPrivate around as a copy, so every C++
  QPlaceResultPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceResultPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'compare', 'clone', 'type'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QPlaceResultPrivate::copyIfPossible(
    QSharedDataPointer<QPlaceSearchResultPrivate> &d_ptr, const
    QPlaceSearchResult &other)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QPlaceResultPrivate::~QPlaceResultPrivate()': the destructor:
    Python removes its C++ QPlaceResultPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlaceResultPrivate is created at the first use, not by
    'QPlaceResultPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceResultPrivate back gives a copy the ritual made
    for Python, in a new cute QPlaceResultPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceResultPrivate'

  #  A C++ QPlaceResultPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceResultPrivate'

  #  Qt's '~QPlaceResultPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPlaceResultPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QPlaceResultPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlaceSearchResultPrivate)
  @overload(NoneType)
  def compare(self, other: Optional[QPlaceSearchResultPrivate]) -> bool:
    """
    Calls Qt's 'bool QPlaceResultPrivate::compare(const
    QPlaceSearchResultPrivate *other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresultprivate.html#compare

    Parameters
    ----------

    other : Optional[QPlaceSearchResultPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlaceResultPrivate::compare(const QPlaceSearchResultPrivate
    #      *other) const
    ritual = (
        'ritual_ZNK19QPlaceResultPrivate7compareEPK25QPlaceSearchResultPriv'
        'ate')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QPlaceResultPrivate7compareEPK25QPlaceSearchResu'
          'ltPrivate')
    return self.uglySide.call(ritual, self._addressOf(other))

  def clone(self) -> Optional[QPlaceSearchResultPrivate]:
    """
    Calls Qt's 'QPlaceSearchResultPrivate *QPlaceResultPrivate::clone()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresultprivate.html#clone

    Returns
    -------

    Optional[QPlaceSearchResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceSearchResultPrivate *QPlaceResultPrivate::clone() const
    ritual = 'ritual_ZNK19QPlaceResultPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QPlaceResultPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QPlaceSearchResultPrivate._cuteAt(address)

  def type(self) -> QPlaceSearchResult.SearchResultType:
    """
    Calls Qt's 'QPlaceSearchResult::SearchResultType
    QPlaceResultPrivate::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceresultprivate.html#type

    Returns
    -------

    QPlaceSearchResult.SearchResultType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlaceSearchResult.SearchResultType(number)' gives.
    """
    #  QPlaceSearchResult::SearchResultType QPlaceResultPrivate::type() const
    ritual = 'ritual_ZNK19QPlaceResultPrivate4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QPlaceResultPrivate4typeEv'
    return QPlaceSearchResult.SearchResultType(self.uglySide.call(ritual))

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
