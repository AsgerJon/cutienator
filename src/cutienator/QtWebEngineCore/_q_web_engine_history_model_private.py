"""
QWebEngineHistoryModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineHistoryModelPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWebEngineHistoryModelPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineHistoryModelPrivate: a plain Python object
  standing in front of one C++ QWebEngineHistoryModelPrivate.

  C++ hands a QWebEngineHistoryModelPrivate around as a copy, so every C++
  QWebEngineHistoryModelPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineHistoryModelPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'count', 'index',
  'offsetForIndex'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineHistoryModelPrivate::~QWebEngineHistoryModelPrivate()':
    the destructor: Python removes its C++ QWebEngineHistoryModelPrivate by
    it, and has no other use for it.
  - Qt's 'QtWebEngineCore::WebContentsAdapter
    *QWebEngineHistoryModelPrivate::adapter() const': gives
    'QtWebEngineCore::WebContentsAdapter', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on
  'QWebEngineHistoryModelPrivate.

  What to expect
  --------------

  - The C++ QWebEngineHistoryModelPrivate is created at the first use, not by
    'QWebEngineHistoryModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineHistoryModelPrivate back gives a copy the
    ritual made for Python, in a new cute QWebEngineHistoryModelPrivate.
  - Each name of Qt's QWebEngineHistoryModelPrivate that has no cute function
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
  __qt_class__ = 'QWebEngineHistoryModelPrivate'

  #  A C++ QWebEngineHistoryModelPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineHistoryModelPrivate'

  #  The functions Qt calls itself that QWebEngineHistoryModelPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'count': (
          ('_ZNK29QWebEngineHistoryModelPrivate5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'index': (
          ('_ZNK29QWebEngineHistoryModelPrivate5indexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'offsetForIndex': (
          ('_ZNK29QWebEngineHistoryModelPrivate14offsetForIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QWebEngineHistoryModelPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineHistoryModelPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QWebEngineHistoryModelPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QWebEngineHistoryModelPrivate::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodelprivate.html#count
    """
    #  int QWebEngineHistoryModelPrivate::count() const
    return self.uglySide.call(
        'ritual_ZNK29QWebEngineHistoryModelPrivate5countEv',
    )

  @overload(int)
  def index(self, a0: int) -> int:
    """
    Calls Qt's 'int QWebEngineHistoryModelPrivate::index(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodelprivate.html#index

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWebEngineHistoryModelPrivate::index(int a0) const
    ritual = 'ritual_ZNK29QWebEngineHistoryModelPrivate5indexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QWebEngineHistoryModelPrivate5indexEi'
    return self.uglySide.call(ritual, a0)

  @overload(int)
  def offsetForIndex(self, a0: int) -> int:
    """
    Calls Qt's 'int QWebEngineHistoryModelPrivate::offsetForIndex(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodelprivate.html#offsetForIndex

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWebEngineHistoryModelPrivate::offsetForIndex(int a0) const
    return self.uglySide.call(
        'ritual_ZNK29QWebEngineHistoryModelPrivate14offsetForIndexEi', a0,
    )

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
    Qt's 'QWebEngineHistoryModelPrivate::QWebEngineHistoryModelPrivate(const
    QWebEngineHistoryPrivate *history)': leans on
    'QWebEngineHistoryModelPrivate::offsetForIndex(int) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryModelPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QWebEngineHistoryModelPrivate::QWebEngineHistoryModelPrivate(const"
        " QWebEngineHistoryPrivate *history)': leans on "
        "'QWebEngineHistoryModelPrivate::offsetForIndex(int) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    *QWebEngineHistoryModelPrivate::adapter() const': gives
    'QtWebEngineCore::WebContentsAdapter', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineHistoryModelPrivate.adapter' has no cute function yet. "
        "Qt's 'QtWebEngineCore::WebContentsAdapter "
        "*QWebEngineHistoryModelPrivate::adapter() const': gives "
        "'QtWebEngineCore::WebContentsAdapter', which has no cute class yet."
    )
