"""
QSvgExtraStates binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QSvgExtraStates to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSvgDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgDocument = WAIT['QSvgDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgExtraStates(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgExtraStates: a plain Python object standing in
  front of one C++ QSvgExtraStates.

  C++ hands a QSvgExtraStates around as a copy, so every C++ QSvgExtraStates
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgExtraStates that has a ritual and that Python
  can call so far, 1 name in all: 'doc'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgExtraStates::~QSvgExtraStates()': the destructor: Python
    removes its C++ QSvgExtraStates by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSvgExtraStates is created at the first use, not by
    'QSvgExtraStates(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgExtraStates back gives a copy the ritual made for
    Python, in a new cute QSvgExtraStates.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgExtraStates'

  #  Qt's '~QSvgExtraStates()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgExtraStates behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSvgExtraStatesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def doc(self) -> Optional[QSvgDocument]:
    """
    Calls Qt's 'const QSvgDocument *QSvgExtraStates::doc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgextrastates.html#doc

    Returns
    -------

    Optional[QSvgDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSvgDocument *QSvgExtraStates::doc() const
    address = self.uglySide.call('ritual_ZNK15QSvgExtraStates3docEv')
    from . import QSvgDocument
    return QSvgDocument._cuteAt(address)

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
    Notes what was given, for Qt's 'QSvgExtraStates::QSvgExtraStates()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgextrastates.html#QSvgExtraStates
    """
    #  QSvgExtraStates::QSvgExtraStates()
    self._noteCreation(QSvgExtraStates, lambda: Rituals.call(
        'ritual_ZN15QSvgExtraStatesC1Ev',
    ))

  @overload(QSvgDocument)
  @overload(NoneType)
  def __init__(self, doc: Optional[QSvgDocument]) -> None:
    """
    Notes what was given, for Qt's 'QSvgExtraStates::QSvgExtraStates(const
    QSvgDocument *doc)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgextrastates.html#QSvgExtraStates

    Parameters
    ----------

    doc : Optional[QSvgDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSvgExtraStates::QSvgExtraStates(const QSvgDocument *doc)
    self._noteCreation(QSvgExtraStates, lambda: Rituals.call(
        'ritual_ZN15QSvgExtraStatesC1EPK12QSvgDocument',
        self._addressOf(doc),
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
