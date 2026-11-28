"""
qdesigner_internal::Selection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_objectinspector_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::Selection to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QObject


class Selection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::Selection: a plain Python object
  standing in front of one C++ qdesigner_internal::Selection.

  C++ hands a qdesigner_internal::Selection around as a copy, so every C++
  qdesigner_internal::Selection behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::Selection that has a ritual and
  that Python can call so far, 3 names in all: 'empty', 'clear', 'selection'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::Selection::~Selection()': the destructor:
    Python removes its C++ qdesigner_internal::Selection by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::Selection is created at the first use, not by
    'qdesigner_internal::Selection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::Selection back gives a copy the
    ritual made for Python, in a new cute qdesigner_internal::Selection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::Selection'

  #  Qt's '~qdesigner_internal::Selection()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::Selection behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal9SelectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def empty(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Selection::empty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selection.html#empty
    """
    #  bool qdesigner_internal::Selection::empty() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9Selection5emptyEv',
    )

  def selection(self) -> QList[QObject]:
    """
    Calls Qt's 'QObjectList qdesigner_internal::Selection::selection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selection.html#selection

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QObjectList qdesigner_internal::Selection::selection() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9Selection9selectionEv',
    )
    from ..QtCore import QObject
    return QList[QObject]._cuteOwning(address)

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

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Selection::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selection.html#clear
    """
    #  void qdesigner_internal::Selection::clear()
    self.uglySide.call('ritual_ZN18qdesigner_internal9Selection5clearEv')
