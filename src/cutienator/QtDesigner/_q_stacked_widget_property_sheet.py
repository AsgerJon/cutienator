"""
QStackedWidgetPropertySheet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QStackedWidgetPropertySheet to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDesignerPropertySheet

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from ..QtWidgets import QStackedWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QStackedWidget = WAIT['QStackedWidget']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStackedWidgetPropertySheet(QDesignerPropertySheet):
  """
  The cute side of Qt's QStackedWidgetPropertySheet: a plain Python object
  standing in front of one C++ QStackedWidgetPropertySheet.

  It is built on the cute 'QDesignerPropertySheet', as Qt's
  QStackedWidgetPropertySheet is built on Qt's QDesignerPropertySheet, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QStackedWidgetPropertySheet that has a ritual and
  that Python can call so far, 5 names in all: 'setProperty', 'property',
  'reset', 'isEnabled', 'checkProperty'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QStackedWidgetPropertySheet is created at the first use, not by
    'QStackedWidgetPropertySheet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStackedWidgetPropertySheet.
  - Qt tells when it has removed the C++ QStackedWidgetPropertySheet. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def checkProperty(propertyName: str) -> bool:
    """
    Calls Qt's 'bool QStackedWidgetPropertySheet::checkProperty(const QString
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetpropertysheet.html#checkProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QStackedWidgetPropertySheet::checkProperty(const QString
    #      &propertyName)
    return Rituals.call(
        'ritual_ZN27QStackedWidgetPropertySheet13checkPropertyERK7QString',
        propertyName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStackedWidgetPropertySheet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def property(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QStackedWidgetPropertySheet::property(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetpropertysheet.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QStackedWidgetPropertySheet::property(int index) const
    ritual = 'ritual_ZNK27QStackedWidgetPropertySheet8propertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QStackedWidgetPropertySheet8propertyEi'
    address = self.uglySide.call(ritual, index)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QStackedWidgetPropertySheet::isEnabled(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetpropertysheet.html#isEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QStackedWidgetPropertySheet::isEnabled(int index) const
    ritual = 'ritual_ZNK27QStackedWidgetPropertySheet9isEnabledEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QStackedWidgetPropertySheet9isEnabledEi'
    return self.uglySide.call(ritual, index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setProperty(self, index: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QStackedWidgetPropertySheet::setProperty(int index,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetpropertysheet.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QStackedWidgetPropertySheet::setProperty(int index, const
    #      QVariant &value)
    ritual = (
        'ritual_ZN27QStackedWidgetPropertySheet11setPropertyEiRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QStackedWidgetPropertySheet11setPropertyEiRK8QVar'
          'iant')
    self.uglySide.call(ritual, index, self._valueOf(value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStackedWidget)
  @overload(NoneType)
  @overload(QStackedWidget, QObject)
  @overload(QStackedWidget, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      object: Optional[QStackedWidget],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QStackedWidgetPropertySheet::QStackedWidgetPropertySheet(QStackedWidget
    *object, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetpropertysheet.html

    Parameters
    ----------

    object : Optional[QStackedWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStackedWidgetPropertySheet::QStackedWidgetPropertySheet(
    #      QStackedWidget *object, QObject *parent)
    self._noteCreation(QStackedWidgetPropertySheet, lambda: Rituals.call(
        'ritual_ZN27QStackedWidgetPropertySheetC1EP14QStackedWidgetP7QObjec'
        't',
        self._addressOf(object), self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def reset(self, index: int) -> bool:
    """
    Calls Qt's 'bool QStackedWidgetPropertySheet::reset(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgetpropertysheet.html#reset

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QStackedWidgetPropertySheet::reset(int index)
    ritual = 'ritual_ZN27QStackedWidgetPropertySheet5resetEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QStackedWidgetPropertySheet5resetEi'
    return self.uglySide.call(ritual, index)
