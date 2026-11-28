"""
QHelpSearchQuery binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpsearchengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList, QStringList


class QHelpSearchQuery(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHelpSearchQuery: a plain Python object standing in
  front of one C++ QHelpSearchQuery.

  C++ hands a QHelpSearchQuery around as a copy, so every C++
  QHelpSearchQuery behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QHelpSearchQuery yet. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHelpSearchQuery::~QHelpSearchQuery()': the destructor: Python
    removes its C++ QHelpSearchQuery by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QHelpSearchQuery is created at the first use, not by
    'QHelpSearchQuery(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHelpSearchQuery back gives a copy the ritual made
    for Python, in a new cute QHelpSearchQuery.
  """

  #  The enums Qt writes inside QHelpSearchQuery, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FieldName(CuteNum):
    """
    The enum 'QHelpSearchQuery::FieldName' of Qt, with the 6 names Qt gives
    in it.
    """

    DEFAULT = Kee[int](0)
    FUZZY = Kee[int](1)
    WITHOUT = Kee[int](2)
    PHRASE = Kee[int](3)
    ALL = Kee[int](4)
    ATLEAST = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpSearchQuery'

  #  Qt's '~QHelpSearchQuery()'. Naming it makes this a value class: Python
  #  owns every C++ QHelpSearchQuery behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QHelpSearchQueryD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QHelpSearchQuery::QHelpSearchQuery()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquery.html#QHelpSearchQuery
    """
    #  QHelpSearchQuery::QHelpSearchQuery()
    self._noteCreation(QHelpSearchQuery, lambda: Rituals.call(
        'ritual_ZN16QHelpSearchQueryC1Ev',
    ))

  @overload(FieldName, QStringList)
  def __init__(self, field: FieldName, wordList_: QStringList) -> None:
    """
    Notes what was given, for Qt's
    'QHelpSearchQuery::QHelpSearchQuery(FieldName field, const QStringList
    &wordList_)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquery.html#QHelpSearchQuery

    Parameters
    ----------

    field : FieldName
      Passed on as its number.

    wordList_ : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QHelpSearchQuery::QHelpSearchQuery(FieldName field, const QStringList
    #      &wordList_)
    self._noteCreation(QHelpSearchQuery, lambda: Rituals.call(
        'ritual_ZN16QHelpSearchQueryC1ENS_9FieldNameERK5QListI7QStringE',
        field.value, self._valueOf(wordList_),
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


#  Qt's 'QList<QHelpSearchQuery>': the list of QHelpSearchQuery, which
#  'QList[QHelpSearchQuery]' gives. It is made here, so that there is one as
#  soon as there can be a QHelpSearchQuery.
QList.createKind(
    QHelpSearchQuery, 'value',
    make='ritual_list_make_QHelpSearchQuery',
    add='ritual_list_add_QHelpSearchQuery',
    size='ritual_list_size_QHelpSearchQuery',
    at='ritual_list_at_QHelpSearchQuery',
    drop='ritual_list_drop_QHelpSearchQuery',
)
