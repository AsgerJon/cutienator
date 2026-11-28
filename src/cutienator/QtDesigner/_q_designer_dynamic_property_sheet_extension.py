"""
QDesignerDynamicPropertySheetExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/dynamicpropertysheet.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QDesignerDynamicPropertySheetExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerDynamicPropertySheetExtension: a plain
  Python object standing in front of one C++
  QDesignerDynamicPropertySheetExtension.

  What exists
  -----------

  Every function of Qt's QDesignerDynamicPropertySheetExtension that has a
  ritual and that Python can call so far, 5 names in all:
  'dynamicPropertiesAllowed', 'addDynamicProperty', 'removeDynamicProperty',
  'isDynamicProperty', 'canAddDynamicProperty'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerDynamicPropertySheetExtension::
    ~QDesignerDynamicPropertySheetExtension()': the destructor: Python never
    removes a C++ QDesignerDynamicPropertySheetExtension.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerDynamicPropertySheetExtension is created at the first
    use, not by 'QDesignerDynamicPropertySheetExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerDynamicPropertySheetExtension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerDynamicPropertySheetExtension'

  #  A C++ QDesignerDynamicPropertySheetExtension Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerDynamicPropertySheetExtension'

  #  The functions Qt calls itself that
  #  QDesignerDynamicPropertySheetExtension is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'dynamicPropertiesAllowed': (
          ('_ZNK38QDesignerDynamicPropertySheetExtension24dynamicProperties'
           'AllowedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'addDynamicProperty': (
          ('_ZN38QDesignerDynamicPropertySheetExtension18addDynamicProperty'
           'ERK7QStringRK8QVariant',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'removeDynamicProperty': (
          ('_ZN38QDesignerDynamicPropertySheetExtension21removeDynamicPrope'
           'rtyEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isDynamicProperty': (
          ('_ZNK38QDesignerDynamicPropertySheetExtension17isDynamicProperty'
           'Ei',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'canAddDynamicProperty': (
          ('_ZNK38QDesignerDynamicPropertySheetExtension21canAddDynamicProp'
           'ertyERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dynamicPropertiesAllowed(self) -> bool:
    """
    Calls Qt's 'bool
    QDesignerDynamicPropertySheetExtension::dynamicPropertiesAllowed()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdynamicpropertysheetextension.html
    """
    #  bool
    #      QDesignerDynamicPropertySheetExtension::dynamicPropertiesAllowed()
    #      const
    return self._callAs(
        'QDesignerDynamicPropertySheetExtension',
        'ritual_ZNK38QDesignerDynamicPropertySheetExtension24dynamicPropert'
        'iesAllowedEv',
    )

  @overload(int)
  def isDynamicProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool
    QDesignerDynamicPropertySheetExtension::isDynamicProperty(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdynamicpropertysheetextension.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerDynamicPropertySheetExtension::isDynamicProperty(int
    #      index) const
    return self._callAs(
        'QDesignerDynamicPropertySheetExtension',
        'ritual_ZNK38QDesignerDynamicPropertySheetExtension17isDynamicPrope'
        'rtyEi',
        index,
    )

  @overload(str)
  def canAddDynamicProperty(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool
    QDesignerDynamicPropertySheetExtension::canAddDynamicProperty(const
    QString &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdynamicpropertysheetextension.html

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerDynamicPropertySheetExtension::canAddDynamicProperty(
    #      const QString &propertyName) const
    return self._callAs(
        'QDesignerDynamicPropertySheetExtension',
        'ritual_ZNK38QDesignerDynamicPropertySheetExtension21canAddDynamicP'
        'ropertyERK7QString',
        propertyName,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDesignerDynamicPropertySheetExtension::
    QDesignerDynamicPropertySheetExtension()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdynamicpropertysheetextension.html
    """
    #  QDesignerDynamicPropertySheetExtension::
    #      QDesignerDynamicPropertySheetExtension()
    self._noteCreation(
        QDesignerDynamicPropertySheetExtension, lambda: Rituals.call(
            'ritual_ZN38QDesignerDynamicPropertySheetExtensionC1Ev',
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

  @overload(str, QVariant)
  def addDynamicProperty(self, propertyName: str, value: QVariant) -> int:
    """
    Calls Qt's 'int
    QDesignerDynamicPropertySheetExtension::addDynamicProperty(const QString
    &propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdynamicpropertysheetextension.html

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  int QDesignerDynamicPropertySheetExtension::addDynamicProperty(const
    #      QString &propertyName, const QVariant &value)
    return self._callAs(
        'QDesignerDynamicPropertySheetExtension',
        'ritual_ZN38QDesignerDynamicPropertySheetExtension18addDynamicPrope'
        'rtyERK7QStringRK8QVariant',
        propertyName, self._valueOf(value),
    )

  @overload(int)
  def removeDynamicProperty(self, index: int) -> bool:
    """
    Calls Qt's 'bool
    QDesignerDynamicPropertySheetExtension::removeDynamicProperty(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerdynamicpropertysheetextension.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerDynamicPropertySheetExtension::removeDynamicProperty(int
    #      index)
    return self._callAs(
        'QDesignerDynamicPropertySheetExtension',
        'ritual_ZN38QDesignerDynamicPropertySheetExtension21removeDynamicPr'
        'opertyEi',
        index,
    )
