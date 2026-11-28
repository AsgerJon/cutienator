"""
QWebEngineBackHistoryModelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineBackHistoryModelPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QWebEngineHistoryModelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWebEngineBackHistoryModelPrivate(QWebEngineHistoryModelPrivate):
  """
  The cute side of Qt's QWebEngineBackHistoryModelPrivate: a plain Python
  object standing in front of one C++ QWebEngineBackHistoryModelPrivate.

  It is built on the cute 'QWebEngineHistoryModelPrivate', as Qt's
  QWebEngineBackHistoryModelPrivate is built on Qt's
  QWebEngineHistoryModelPrivate, and has everything that class has.

  C++ hands a QWebEngineBackHistoryModelPrivate around as a copy, so every
  C++ QWebEngineBackHistoryModelPrivate behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineBackHistoryModelPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'count', 'index',
  'offsetForIndex'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QWebEngineBackHistoryModelPrivate::~QWebEngineBackHistoryModelPrivate(
    )': the destructor: Python removes its C++
    QWebEngineBackHistoryModelPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on
  'QWebEngineBackHistoryModelPrivate.

  What to expect
  --------------

  - The C++ QWebEngineBackHistoryModelPrivate is created at the first use,
    not by 'QWebEngineBackHistoryModelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineBackHistoryModelPrivate back gives a copy
    the ritual made for Python, in a new cute
    QWebEngineBackHistoryModelPrivate.
  - Each name of Qt's QWebEngineBackHistoryModelPrivate that has no cute
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
  __qt_class__ = 'QWebEngineBackHistoryModelPrivate'

  #  A C++ QWebEngineBackHistoryModelPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebEngineBackHistoryModelPrivate'

  #  Qt's '~QWebEngineBackHistoryModelPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ QWebEngineBackHistoryModelPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QWebEngineBackHistoryModelPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QWebEngineBackHistoryModelPrivate::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginebackhistorymodelprivate.html#count
    """
    #  int QWebEngineBackHistoryModelPrivate::count() const
    return self.uglySide.call(
        'ritual_ZNK33QWebEngineBackHistoryModelPrivate5countEv',
    )

  @overload(int)
  def index(self, a0: int) -> int:
    """
    Calls Qt's 'int QWebEngineBackHistoryModelPrivate::index(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginebackhistorymodelprivate.html#index

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWebEngineBackHistoryModelPrivate::index(int a0) const
    ritual = 'ritual_ZNK33QWebEngineBackHistoryModelPrivate5indexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK33QWebEngineBackHistoryModelPrivate5indexEi'
    return self.uglySide.call(ritual, a0)

  @overload(int)
  def offsetForIndex(self, a0: int) -> int:
    """
    Calls Qt's 'int QWebEngineBackHistoryModelPrivate::offsetForIndex(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginebackhistorymodelprivate.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWebEngineBackHistoryModelPrivate::offsetForIndex(int a0) const
    ritual = (
        'ritual_ZNK33QWebEngineBackHistoryModelPrivate14offsetForIndexEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK33QWebEngineBackHistoryModelPrivate14offsetForInde'
          'xEi')
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
    Qt's
    'QWebEngineBackHistoryModelPrivate::QWebEngineBackHistoryModelPrivate(
    const QWebEngineHistoryPrivate *history)': leans on
    'QWebEngineBackHistoryModelPrivate::count() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWebEngineBackHistoryModelPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QWebEngineBackHistoryModelPrivate::QWebEngineBackHistoryModelPriva"
        "te(const QWebEngineHistoryPrivate *history)': leans on "
        "'QWebEngineBackHistoryModelPrivate::count() const', which Qt's "
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
