"""
QPlaceSearchResultPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qplacesearchresult_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPlaceSearchResultPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData
from . import QPlaceSearchResult

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceSearchResultPrivate(QSharedData):
  """
  The cute side of Qt's QPlaceSearchResultPrivate: a plain Python object
  standing in front of one C++ QPlaceSearchResultPrivate.

  It is built on the cute 'QSharedData', as Qt's QPlaceSearchResultPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QPlaceSearchResultPrivate around as a copy, so every C++
  QPlaceSearchResultPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceSearchResultPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'compare', 'clone', 'type'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceSearchResultPrivate::~QPlaceSearchResultPrivate()': the
    destructor: Python removes its C++ QPlaceSearchResultPrivate by it, and
    has no other use for it.
  - Qt's 'const QSharedDataPointer<QPlaceSearchResultPrivate>
    &QPlaceSearchResultPrivate::extract_d(const QPlaceSearchResult &other)':
    gives a type Python has no way to take yet.
  - Qt's 'void QPlaceSearchResultPrivate::copyIfPossible(
    QSharedDataPointer<QPlaceSearchResultPrivate> &d_ptr, const
    QPlaceSearchResult &other)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QPlaceSearchResultPrivate is created at the first use, not by
    'QPlaceSearchResultPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceSearchResultPrivate back gives a copy the
    ritual made for Python, in a new cute QPlaceSearchResultPrivate.
  - Each name of Qt's QPlaceSearchResultPrivate that has no cute function
    yet, 'copyIfPossible', 'extract_d', holds a function that raises
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
  __qt_class__ = 'QPlaceSearchResultPrivate'

  #  A C++ QPlaceSearchResultPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceSearchResultPrivate'

  #  The functions Qt calls itself that QPlaceSearchResultPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'compare': (
          ('_ZNK25QPlaceSearchResultPrivate7compareEPKS_',
           ('bool', 'number', ''),
           (
               ('address', 'address',
                'QtLocation:QPlaceSearchResultPrivate'),
           )),
      ),
      'clone': (
          ('_ZNK25QPlaceSearchResultPrivate5cloneEv',
           ('address', 'address', 'QtLocation:QPlaceSearchResultPrivate'),
           ()),
      ),
      'type': (
          ('_ZNK25QPlaceSearchResultPrivate4typeEv',
           ('int', 'enum', 'QtLocation:QPlaceSearchResult.SearchResultType'),
           ()),
      ),
  }

  #  Qt's '~QPlaceSearchResultPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPlaceSearchResultPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QPlaceSearchResultPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def compare(self, other: Optional[QPlaceSearchResultPrivate]) -> bool:
    """
    Calls Qt's 'bool QPlaceSearchResultPrivate::compare(const
    QPlaceSearchResultPrivate *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresultprivate.html#compare

    Parameters
    ----------

    other : Optional[QPlaceSearchResultPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlaceSearchResultPrivate::compare(const
    #      QPlaceSearchResultPrivate *other) const
    ritual = 'ritual_ZNK25QPlaceSearchResultPrivate7compareEPKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QPlaceSearchResultPrivate7compareEPKS_'
    return self.uglySide.call(ritual, self._addressOf(other))

  def clone(self) -> Optional[QPlaceSearchResultPrivate]:
    """
    Calls Qt's 'QPlaceSearchResultPrivate *QPlaceSearchResultPrivate::clone()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresultprivate.html#clone

    Returns
    -------

    Optional[QPlaceSearchResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceSearchResultPrivate *QPlaceSearchResultPrivate::clone() const
    ritual = 'ritual_ZNK25QPlaceSearchResultPrivate5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QPlaceSearchResultPrivate5cloneEv'
    address = self.uglySide.call(ritual)
    return QPlaceSearchResultPrivate._cuteAt(address)

  def type(self) -> QPlaceSearchResult.SearchResultType:
    """
    Calls Qt's 'QPlaceSearchResult::SearchResultType
    QPlaceSearchResultPrivate::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresultprivate.html#type

    Returns
    -------

    QPlaceSearchResult.SearchResultType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlaceSearchResult.SearchResultType(number)' gives.
    """
    #  QPlaceSearchResult::SearchResultType QPlaceSearchResultPrivate::type()
    #      const
    ritual = 'ritual_ZNK25QPlaceSearchResultPrivate4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QPlaceSearchResultPrivate4typeEv'
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchResultPrivate::QPlaceSearchResultPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresultprivate.html
    """
    #  QPlaceSearchResultPrivate::QPlaceSearchResultPrivate()
    self._noteCreation(QPlaceSearchResultPrivate, lambda: Rituals.call(
        'ritual_ZN25QPlaceSearchResultPrivateC1Ev',
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
  def copyIfPossible(*__, **_) -> Never:
    """
    Qt's 'void QPlaceSearchResultPrivate::copyIfPossible(
    QSharedDataPointer<QPlaceSearchResultPrivate> &d_ptr, const
    QPlaceSearchResult &other)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QPlaceSearchResultPrivate.copyIfPossible' has no cute function "
        "yet. Qt's 'void "
        "QPlaceSearchResultPrivate::copyIfPossible(QSharedDataPointer<QPlace"
        "SearchResultPrivate> &d_ptr, const QPlaceSearchResult &other)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def extract_d(*__, **_) -> Never:
    """
    Qt's 'const QSharedDataPointer<QPlaceSearchResultPrivate>
    &QPlaceSearchResultPrivate::extract_d(const QPlaceSearchResult &other)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlaceSearchResultPrivate.extract_d' has no cute function yet. "
        "Qt's 'const QSharedDataPointer<QPlaceSearchResultPrivate> "
        "&QPlaceSearchResultPrivate::extract_d(const QPlaceSearchResult "
        "&other)': gives a type Python has no way to take yet.")
