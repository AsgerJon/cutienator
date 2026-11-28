"""
QScriptItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QScriptItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFixed, QScriptAnalysis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScriptAnalysis = WAIT['QScriptAnalysis']


class QScriptItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScriptItem: a plain Python object standing in front
  of one C++ QScriptItem.

  C++ hands a QScriptItem around as a copy, so every C++ QScriptItem behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScriptItem that has a ritual and that Python can
  call so far, 1 name in all: 'height'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScriptItem::~QScriptItem()': the destructor: Python removes its
    C++ QScriptItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScriptItem is created at the first use, not by
    'QScriptItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScriptItem back gives a copy the ritual made for
    Python, in a new cute QScriptItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScriptItem'

  #  Qt's '~QScriptItem()'. Naming it makes this a value class: Python owns
  #  every C++ QScriptItem behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QScriptItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def height(self) -> QFixed:
    """
    Calls Qt's 'QFixed QScriptItem::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscriptitem.html#height

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed QScriptItem::height() const
    address = self.uglySide.call('ritual_ZNK11QScriptItem6heightEv')
    from . import QFixed
    return QFixed._cuteOwning(address)

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

  @overload(int, QScriptAnalysis)
  def __init__(self, p: int, a: QScriptAnalysis) -> None:
    """
    Notes what was given, for Qt's 'QScriptItem::QScriptItem(int p,
    QScriptAnalysis a)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscriptitem.html#QScriptItem

    Parameters
    ----------

    p : int
      Passed on as it is.

    a : QScriptAnalysis
      Passed on as a value: Qt reads the C++ QScriptAnalysis, which stays
      Python's own.
    """
    #  QScriptItem::QScriptItem(int p, QScriptAnalysis a)
    self._noteCreation(QScriptItem, lambda: Rituals.call(
        'ritual_ZN11QScriptItemC1Ei15QScriptAnalysis', p, self._valueOf(a),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QScriptItem::QScriptItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscriptitem.html#QScriptItem
    """
    #  QScriptItem::QScriptItem()
    self._noteCreation(QScriptItem, lambda: Rituals.call(
        'ritual_ZN11QScriptItemC1Ev',
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
