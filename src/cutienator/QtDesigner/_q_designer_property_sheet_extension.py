"""
QDesignerPropertySheetExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/propertysheet.h, Qt 6.12.0. Changes made here are lost.
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


class QDesignerPropertySheetExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerPropertySheetExtension: a plain Python
  object standing in front of one C++ QDesignerPropertySheetExtension.

  What exists
  -----------

  Every function of Qt's QDesignerPropertySheetExtension that has a ritual
  and that Python can call so far, 16 names in all: 'count', 'indexOf',
  'propertyName', 'propertyGroup', 'setPropertyGroup', 'hasReset', 'reset',
  'isVisible', 'setVisible', 'isAttribute', 'setAttribute', 'property',
  'setProperty', 'isChanged', 'setChanged', 'isEnabled'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDesignerPropertySheetExtension::~QDesignerPropertySheetExtension()':
    the destructor: Python never removes a C++
    QDesignerPropertySheetExtension.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerPropertySheetExtension is created at the first use, not
    by 'QDesignerPropertySheetExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerPropertySheetExtension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerPropertySheetExtension'

  #  A C++ QDesignerPropertySheetExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerPropertySheetExtension'

  #  The functions Qt calls itself that QDesignerPropertySheetExtension is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'count': (
          ('_ZNK31QDesignerPropertySheetExtension5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'indexOf': (
          ('_ZNK31QDesignerPropertySheetExtension7indexOfERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'propertyName': (
          ('_ZNK31QDesignerPropertySheetExtension12propertyNameEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyGroup': (
          ('_ZNK31QDesignerPropertySheetExtension13propertyGroupEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setPropertyGroup': (
          ('_ZN31QDesignerPropertySheetExtension16setPropertyGroupEiRK7QStr'
           'ing',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'hasReset': (
          ('_ZNK31QDesignerPropertySheetExtension8hasResetEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'reset': (
          ('_ZN31QDesignerPropertySheetExtension5resetEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isVisible': (
          ('_ZNK31QDesignerPropertySheetExtension9isVisibleEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setVisible': (
          ('_ZN31QDesignerPropertySheetExtension10setVisibleEib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'isAttribute': (
          ('_ZNK31QDesignerPropertySheetExtension11isAttributeEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setAttribute': (
          ('_ZN31QDesignerPropertySheetExtension12setAttributeEib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'property': (
          ('_ZNK31QDesignerPropertySheetExtension8propertyEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
           )),
      ),
      'setProperty': (
          ('_ZN31QDesignerPropertySheetExtension11setPropertyEiRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'isChanged': (
          ('_ZNK31QDesignerPropertySheetExtension9isChangedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setChanged': (
          ('_ZN31QDesignerPropertySheetExtension10setChangedEib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'isEnabled': (
          ('_ZNK31QDesignerPropertySheetExtension9isEnabledEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
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

  def count(self) -> int:
    """
    Calls Qt's 'int QDesignerPropertySheetExtension::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#count
    """
    #  int QDesignerPropertySheetExtension::count() const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension5countEv',
    )

  @overload(str)
  def indexOf(self, name: str) -> int:
    """
    Calls Qt's 'int QDesignerPropertySheetExtension::indexOf(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#indexOf

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerPropertySheetExtension::indexOf(const QString &name)
    #      const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension7indexOfERK7QString',
        name,
    )

  @overload(int)
  def propertyName(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerPropertySheetExtension::propertyName(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#propertyName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerPropertySheetExtension::propertyName(int index) const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension12propertyNameEi',
        index,
    )

  @overload(int)
  def propertyGroup(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerPropertySheetExtension::propertyGroup(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#propertyGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerPropertySheetExtension::propertyGroup(int index)
    #      const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension13propertyGroupEi',
        index,
    )

  @overload(int)
  def hasReset(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheetExtension::hasReset(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#hasReset

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheetExtension::hasReset(int index) const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension8hasResetEi',
        index,
    )

  @overload(int)
  def isVisible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheetExtension::isVisible(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#isVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheetExtension::isVisible(int index) const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension9isVisibleEi',
        index,
    )

  @overload(int)
  def isAttribute(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheetExtension::isAttribute(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#isAttribute

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheetExtension::isAttribute(int index) const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension11isAttributeEi',
        index,
    )

  @overload(int)
  def property(self, index: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDesignerPropertySheetExtension::property(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDesignerPropertySheetExtension::property(int index) const
    address = self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension8propertyEi',
        index,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isChanged(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheetExtension::isChanged(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#isChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheetExtension::isChanged(int index) const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension9isChangedEi',
        index,
    )

  @overload(int)
  def isEnabled(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerPropertySheetExtension::isEnabled(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#isEnabled

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheetExtension::isEnabled(int index) const
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZNK31QDesignerPropertySheetExtension9isEnabledEi',
        index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, str)
  def setPropertyGroup(self, index: int, group: str) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheetExtension::setPropertyGroup(int
    index, const QString &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerPropertySheetExtension::setPropertyGroup(int index,
    #      const QString &group)
    self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZN31QDesignerPropertySheetExtension16setPropertyGroupEiRK7Q'
        'String',
        index, group,
    )

  @overload(int, bool)
  def setVisible(self, index: int, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheetExtension::setVisible(int index,
    bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#setVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheetExtension::setVisible(int index, bool b)
    self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZN31QDesignerPropertySheetExtension10setVisibleEib',
        index, b,
    )

  @overload(int, bool)
  def setAttribute(self, index: int, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheetExtension::setAttribute(int index,
    bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#setAttribute

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheetExtension::setAttribute(int index, bool b)
    self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZN31QDesignerPropertySheetExtension12setAttributeEib',
        index, b,
    )

  @overload(int, QVariant)
  def setProperty(self, index: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheetExtension::setProperty(int index,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#setProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerPropertySheetExtension::setProperty(int index, const
    #      QVariant &value)
    self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZN31QDesignerPropertySheetExtension11setPropertyEiRK8QVaria'
        'nt',
        index, self._valueOf(value),
    )

  @overload(int, bool)
  def setChanged(self, index: int, changed: bool) -> None:
    """
    Calls Qt's 'void QDesignerPropertySheetExtension::setChanged(int index,
    bool changed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#setChanged

    Parameters
    ----------

    index : int
      Passed on as it is.

    changed : bool
      Passed on as it is.
    """
    #  void QDesignerPropertySheetExtension::setChanged(int index, bool
    #      changed)
    self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZN31QDesignerPropertySheetExtension10setChangedEib',
        index, changed,
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
    'QDesignerPropertySheetExtension::QDesignerPropertySheetExtension()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html
    """
    #  QDesignerPropertySheetExtension::QDesignerPropertySheetExtension()
    self._noteCreation(QDesignerPropertySheetExtension, lambda: Rituals.call(
        'ritual_ZN31QDesignerPropertySheetExtensionC1Ev',
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
    Calls Qt's 'bool QDesignerPropertySheetExtension::reset(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpropertysheetextension.html#reset

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerPropertySheetExtension::reset(int index)
    return self._callAs(
        'QDesignerPropertySheetExtension',
        'ritual_ZN31QDesignerPropertySheetExtension5resetEi',
        index,
    )
