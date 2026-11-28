"""
QWebEngineForwardHistoryModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineForwardHistoryModelPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QWebEngineHistoryModelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWebEngineForwardHistoryModelPrivate(QWebEngineHistoryModelPrivate):
  """
  The cute side of Qt's QWebEngineForwardHistoryModelPrivate: a plain Python
  object standing in front of one C++ QWebEngineForwardHistoryModelPrivate.

  It is built on the cute 'QWebEngineHistoryModelPrivate', as Qt's
  QWebEngineForwardHistoryModelPrivate is built on Qt's
  QWebEngineHistoryModelPrivate, and has everything that class has.

  C++ hands a QWebEngineForwardHistoryModelPrivate around as a copy, so every
  C++ QWebEngineForwardHistoryModelPrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineForwardHistoryModelPrivate that has a
  ritual and that Python can call so far, 3 names in all: 'count', 'index',
  'offsetForIndex'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineForwardHistoryModelPrivate::
    ~QWebEngineForwardHistoryModelPrivate()': the destructor: Python removes
    its C++ QWebEngineForwardHistoryModelPrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on
  'QWebEngineForwardHistoryModelPrivate.

  What to expect
  --------------

  - The C++ QWebEngineForwardHistoryModelPrivate is created at the first use,
    not by 'QWebEngineForwardHistoryModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineForwardHistoryModelPrivate back gives a
    copy the ritual made for Python, in a new cute
    QWebEngineForwardHistoryModelPrivate.
  - Each name of Qt's QWebEngineForwardHistoryModelPrivate that has no cute
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
  __qt_class__ = 'QWebEngineForwardHistoryModelPrivate'

  #  A C++ QWebEngineForwardHistoryModelPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineForwardHistoryModelPrivate'

  #  Qt's '~QWebEngineForwardHistoryModelPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QWebEngineForwardHistoryModelPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN36QWebEngineForwardHistoryModelPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QWebEngineForwardHistoryModelPrivate::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineforwardhistorymodelprivate.html#count
    """
    #  int QWebEngineForwardHistoryModelPrivate::count() const
    return self.uglySide.call(
        'ritual_ZNK36QWebEngineForwardHistoryModelPrivate5countEv',
    )

  @overload(int)
  def index(self, a0: int) -> int:
    """
    Calls Qt's 'int QWebEngineForwardHistoryModelPrivate::index(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineforwardhistorymodelprivate.html#index

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWebEngineForwardHistoryModelPrivate::index(int a0) const
    return self.uglySide.call(
        'ritual_ZNK36QWebEngineForwardHistoryModelPrivate5indexEi', a0,
    )

  @overload(int)
  def offsetForIndex(self, a0: int) -> int:
    """
    Calls Qt's 'int QWebEngineForwardHistoryModelPrivate::offsetForIndex(int
    a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineforwardhistorymodelprivate.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWebEngineForwardHistoryModelPrivate::offsetForIndex(int a0) const
    ritual = (
        'ritual_ZNK36QWebEngineForwardHistoryModelPrivate14offsetForIndexEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QWebEngineForwardHistoryModelPrivate14offsetForI'
          'ndexEi')
    return self.uglySide.call(ritual, a0)

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
    Qt's 'QWebEngineForwardHistoryModelPrivate::
    QWebEngineForwardHistoryModelPrivate(const QWebEngineHistoryPrivate
    *history)': leans on 'QWebEngineForwardHistoryModelPrivate::count()
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebEngineForwardHistoryModelPrivate.__init__' has no cute "
        "function yet. Qt's "
        "'QWebEngineForwardHistoryModelPrivate::QWebEngineForwardHistoryMode"
        "lPrivate(const QWebEngineHistoryPrivate *history)': leans on "
        "'QWebEngineForwardHistoryModelPrivate::count() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
