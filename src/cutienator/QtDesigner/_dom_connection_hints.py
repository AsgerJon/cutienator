"""
DomConnectionHints binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomConnectionHints to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomConnectionHint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomConnectionHint = WAIT['DomConnectionHint']


class DomConnectionHints(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomConnectionHints: a plain Python object standing in
  front of one C++ DomConnectionHints.

  What exists
  -----------

  Every function of Qt's DomConnectionHints that has a ritual and that Python
  can call so far, 2 names in all: 'elementHint', 'setElementHint'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomConnectionHints::~DomConnectionHints()': the destructor: Python
    never removes a C++ DomConnectionHints.
  - Qt's 'void DomConnectionHints::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomConnectionHints::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomConnectionHints is created at the first use, not by
    'DomConnectionHints(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomConnectionHints.
  - Each name of Qt's DomConnectionHints that has no cute function yet,
    'read', 'write', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomConnectionHints'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementHint(self) -> QList[DomConnectionHint]:
    """
    Calls Qt's 'QList<DomConnectionHint *> DomConnectionHints::elementHint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhints.html#elementHint

    Returns
    -------

    QList[DomConnectionHint]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomConnectionHint *> DomConnectionHints::elementHint() const
    address = self.uglySide.call(
        'ritual_ZNK18DomConnectionHints11elementHintEv',
    )
    from . import DomConnectionHint
    return QList[DomConnectionHint]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[DomConnectionHint])
  def setElementHint(self, a: QList[DomConnectionHint]) -> None:
    """
    Calls Qt's 'void DomConnectionHints::setElementHint(const
    QList<DomConnectionHint *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhints.html#setElementHint

    Parameters
    ----------

    a : QList[DomConnectionHint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomConnectionHints::setElementHint(const QList<DomConnectionHint
    #      *> &a)
    self.uglySide.call(
        'ritual_ZN18DomConnectionHints14setElementHintERK5QListIP17DomConne'
        'ctionHintE',
        self._valueOf(a),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'DomConnectionHints::DomConnectionHints()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhints.html#DomConnectionHints
    """
    #  DomConnectionHints::DomConnectionHints()
    self._noteCreation(DomConnectionHints, lambda: Rituals.call(
        'ritual_ZN18DomConnectionHintsC1Ev',
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
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomConnectionHints::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomConnectionHints.read' has no cute function yet. Qt's 'void "
        "DomConnectionHints::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomConnectionHints::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomConnectionHints.write' has no cute function yet. Qt's 'void "
        "DomConnectionHints::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
