"""
QPlaceSearchSuggestionReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacesearchsuggestionreply.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QPlaceReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceSearchSuggestionReply(QPlaceReply):
  """
  The cute side of Qt's QPlaceSearchSuggestionReply: a plain Python object
  standing in front of one C++ QPlaceSearchSuggestionReply.

  It is built on the cute 'QPlaceReply', as Qt's QPlaceSearchSuggestionReply
  is built on Qt's QPlaceReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlaceSearchSuggestionReply that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'suggestions', 'type', 'setSuggestions'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlaceSearchSuggestionReply::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QPlaceSearchSuggestionReply::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlaceSearchSuggestionReply::~QPlaceSearchSuggestionReply()': the
    destructor: Python never removes a C++ QPlaceSearchSuggestionReply.
  - Qt's 'QPlaceSearchSuggestionReplyPrivate
    *QPlaceSearchSuggestionReply::d_func()': gives
    'QPlaceSearchSuggestionReplyPrivate', which has no cute class yet.
  - Qt's 'const QPlaceSearchSuggestionReplyPrivate
    *QPlaceSearchSuggestionReply::d_func() const': gives
    'QPlaceSearchSuggestionReplyPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPlaceSearchSuggestionReply is created at the first use, not by
    'QPlaceSearchSuggestionReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlaceSearchSuggestionReply.
  - Qt tells when it has removed the C++ QPlaceSearchSuggestionReply. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPlaceSearchSuggestionReply::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchsuggestionreply.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceSearchSuggestionReply::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QPlaceSearchSuggestionReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceSearchSuggestionReply'

  #  A C++ QPlaceSearchSuggestionReply Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlaceSearchSuggestionReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlaceSearchSuggestionReply::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchsuggestionreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlaceSearchSuggestionReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QPlaceSearchSuggestionReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def suggestions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QPlaceSearchSuggestionReply::suggestions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchsuggestionreply.html#suggestions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlaceSearchSuggestionReply::suggestions() const
    address = self.uglySide.call(
        'ritual_ZNK27QPlaceSearchSuggestionReply11suggestionsEv',
    )
    return QStringList._cuteOwning(address)

  def type(self) -> QPlaceReply.Type:
    """
    Calls Qt's 'Type QPlaceSearchSuggestionReply::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchsuggestionreply.html#type

    Returns
    -------

    QPlaceReply.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QPlaceReply.Type(number)'
      gives.
    """
    #  Type QPlaceSearchSuggestionReply::type() const
    ritual = 'ritual_ZNK27QPlaceSearchSuggestionReply4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QPlaceSearchSuggestionReply4typeEv'
    return QPlaceReply.Type(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setSuggestions(self, suggestions: QStringList) -> None:
    """
    Calls Qt's 'void QPlaceSearchSuggestionReply::setSuggestions(const
    QStringList &suggestions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchsuggestionreply.html#setSuggestions

    Parameters
    ----------

    suggestions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceSearchSuggestionReply::setSuggestions(const QStringList
    #      &suggestions)
    self.uglySide.call(
        'ritual_ZN27QPlaceSearchSuggestionReply14setSuggestionsERK5QListI7Q'
        'StringE',
        self._valueOf(suggestions),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchSuggestionReply::QPlaceSearchSuggestionReply(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchsuggestionreply.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPlaceSearchSuggestionReply::QPlaceSearchSuggestionReply(QObject
    #      *parent)
    self._noteCreation(QPlaceSearchSuggestionReply, lambda: Rituals.call(
        'ritual_ZN27QPlaceSearchSuggestionReplyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
