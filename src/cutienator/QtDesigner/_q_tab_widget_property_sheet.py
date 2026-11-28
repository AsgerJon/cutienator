"""
QTabWidgetPropertySheet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_tabwidget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTabWidgetPropertySheet to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDesignerPropertySheet

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from ..QtWidgets import QTabWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTabWidget = WAIT['QTabWidget']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTabWidgetPropertySheet(QDesignerPropertySheet):
  """
  The cute side of Qt's QTabWidgetPropertySheet: a plain Python object
  standing in front of one C++ QTabWidgetPropertySheet.

  It is built on the cute 'QDesignerPropertySheet', as Qt's
  QTabWidgetPropertySheet is built on Qt's QDesignerPropertySheet, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QTabWidgetPropertySheet that has a ritual and that
  Python can call so far, 5 names in all: 'setProperty', 'property', 'reset',
  'isEnabled', 'checkProperty'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TabWidgetProperty
    QTabWidgetPropertySheet::tabWidgetPropertyFromName(const QString &name)':
    gives the enum 'QTabWidgetPropertySheet::TabWidgetProperty', whose class
    cannot be named here.

  What to expect
  --------------

  - The C++ QTabWidgetPropertySheet is created at the first use, not by
    'QTabWidgetPropertySheet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTabWidgetPropertySheet.
  - Qt tells when it has removed the C++ QTabWidgetPropertySheet. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QTabWidgetPropertySheet that has no cute function yet,
    'tabWidgetPropertyFromName', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def checkProperty(propertyName: str) -> bool:
    """
    Calls Qt's 'bool QTabWidgetPropertySheet::checkProperty(const QString
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgetpropertysheet.html#checkProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QTabWidgetPropertySheet::checkProperty(const QString
    #      &propertyName)
    return Rituals.call(
        'ritual_ZN23QTabWidgetPropertySheet13checkPropertyERK7QString',
        propertyName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTabWidgetPropertySheet'

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
    Calls Qt's 'QVariant QTabWidgetPropertySheet::property(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgetpropertysheet.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTabWidgetPropertySheet::property(int index) const
    ritual = 'ritual_ZNK23QTabWidgetPropertySheet8propertyEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QTabWidgetPropertySheet8propertyEi'
    address = self.uglySide.call(ritual, index)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QTabWidgetPropertySheet::isEnabled(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgetpropertysheet.html#isEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabWidgetPropertySheet::isEnabled(int index) const
    ritual = 'ritual_ZNK23QTabWidgetPropertySheet9isEnabledEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QTabWidgetPropertySheet9isEnabledEi'
    return self.uglySide.call(ritual, index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QVariant)
  def setProperty(self, index: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QTabWidgetPropertySheet::setProperty(int index, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgetpropertysheet.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTabWidgetPropertySheet::setProperty(int index, const QVariant
    #      &value)
    ritual = 'ritual_ZN23QTabWidgetPropertySheet11setPropertyEiRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QTabWidgetPropertySheet11setPropertyEiRK8QVariant')
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

  @overload(QTabWidget)
  @overload(NoneType)
  @overload(QTabWidget, QObject)
  @overload(QTabWidget, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      object: Optional[QTabWidget],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTabWidgetPropertySheet::QTabWidgetPropertySheet(QTabWidget *object,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgetpropertysheet.html

    Parameters
    ----------

    object : Optional[QTabWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTabWidgetPropertySheet::QTabWidgetPropertySheet(QTabWidget *object,
    #      QObject *parent)
    self._noteCreation(QTabWidgetPropertySheet, lambda: Rituals.call(
        'ritual_ZN23QTabWidgetPropertySheetC1EP10QTabWidgetP7QObject',
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
    Calls Qt's 'bool QTabWidgetPropertySheet::reset(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidgetpropertysheet.html#reset

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QTabWidgetPropertySheet::reset(int index)
    ritual = 'ritual_ZN23QTabWidgetPropertySheet5resetEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QTabWidgetPropertySheet5resetEi'
    return self.uglySide.call(ritual, index)

  @staticmethod
  def tabWidgetPropertyFromName(*__, **_) -> Never:
    """
    Qt's 'TabWidgetProperty
    QTabWidgetPropertySheet::tabWidgetPropertyFromName(const QString &name)':
    gives the enum 'QTabWidgetPropertySheet::TabWidgetProperty', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QTabWidgetPropertySheet.tabWidgetPropertyFromName' has no cute "
        "function yet. Qt's 'TabWidgetProperty "
        "QTabWidgetPropertySheet::tabWidgetPropertyFromName(const QString "
        "&name)': gives the enum "
        "'QTabWidgetPropertySheet::TabWidgetProperty', whose class cannot "
        "be named here.")
