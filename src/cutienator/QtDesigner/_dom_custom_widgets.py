"""
DomCustomWidgets binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomCustomWidgets to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomCustomWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomCustomWidget = WAIT['DomCustomWidget']


class DomCustomWidgets(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomCustomWidgets: a plain Python object standing in
  front of one C++ DomCustomWidgets.

  What exists
  -----------

  Every function of Qt's DomCustomWidgets that has a ritual and that Python
  can call so far, 2 names in all: 'elementCustomWidget',
  'setElementCustomWidget'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomCustomWidgets::~DomCustomWidgets()': the destructor: Python
    never removes a C++ DomCustomWidgets.
  - Qt's 'void DomCustomWidgets::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomCustomWidgets::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomCustomWidgets is created at the first use, not by
    'DomCustomWidgets(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomCustomWidgets.
  - Each name of Qt's DomCustomWidgets that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomCustomWidgets'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementCustomWidget(self) -> QList[DomCustomWidget]:
    """
    Calls Qt's 'QList<DomCustomWidget *>
    DomCustomWidgets::elementCustomWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidgets.html#elementCustomWidget

    Returns
    -------

    QList[DomCustomWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomCustomWidget *> DomCustomWidgets::elementCustomWidget() const
    address = self.uglySide.call(
        'ritual_ZNK16DomCustomWidgets19elementCustomWidgetEv',
    )
    from . import DomCustomWidget
    return QList[DomCustomWidget]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[DomCustomWidget])
  def setElementCustomWidget(self, a: QList[DomCustomWidget]) -> None:
    """
    Calls Qt's 'void DomCustomWidgets::setElementCustomWidget(const
    QList<DomCustomWidget *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidgets.html#setElementCustomWidget

    Parameters
    ----------

    a : QList[DomCustomWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomCustomWidgets::setElementCustomWidget(const
    #      QList<DomCustomWidget *> &a)
    self.uglySide.call(
        'ritual_ZN16DomCustomWidgets22setElementCustomWidgetERK5QListIP15Do'
        'mCustomWidgetE',
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
    Notes what was given, for Qt's 'DomCustomWidgets::DomCustomWidgets()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domcustomwidgets.html#DomCustomWidgets
    """
    #  DomCustomWidgets::DomCustomWidgets()
    self._noteCreation(DomCustomWidgets, lambda: Rituals.call(
        'ritual_ZN16DomCustomWidgetsC1Ev',
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
    Qt's 'void DomCustomWidgets::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomCustomWidgets.read' has no cute function yet. Qt's 'void "
        "DomCustomWidgets::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomCustomWidgets::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomCustomWidgets.write' has no cute function yet. Qt's 'void "
        "DomCustomWidgets::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
