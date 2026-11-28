"""
QDesignerMemberSheetExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/membersheet.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class QDesignerMemberSheetExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerMemberSheetExtension: a plain Python object
  standing in front of one C++ QDesignerMemberSheetExtension.

  What exists
  -----------

  Every function of Qt's QDesignerMemberSheetExtension that has a ritual and
  that Python can call so far, 14 names in all: 'count', 'indexOf',
  'memberName', 'memberGroup', 'setMemberGroup', 'isVisible', 'setVisible',
  'isSignal', 'isSlot', 'inheritedFromWidget', 'declaredInClass',
  'signature', 'parameterTypes', 'parameterNames'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerMemberSheetExtension::~QDesignerMemberSheetExtension()':
    the destructor: Python never removes a C++ QDesignerMemberSheetExtension.

  What has no ritual
  ------------------

  5 of the 20 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerMemberSheetExtension is created at the first use, not by
    'QDesignerMemberSheetExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMemberSheetExtension.
  - Each name of Qt's QDesignerMemberSheetExtension that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QDesignerMemberSheetExtension'

  #  A C++ QDesignerMemberSheetExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMemberSheetExtension'

  #  The functions Qt calls itself that QDesignerMemberSheetExtension is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'parameterTypes': (
          'QList<QByteArray> '
          'QDesignerMemberSheetExtension::parameterTypes(int) const',
      ),
      'parameterNames': (
          'QList<QByteArray> '
          'QDesignerMemberSheetExtension::parameterNames(int) const',
      ),
  }

  #  The functions Qt calls itself that QDesignerMemberSheetExtension is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'count': (
          ('_ZNK29QDesignerMemberSheetExtension5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'indexOf': (
          ('_ZNK29QDesignerMemberSheetExtension7indexOfERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'memberName': (
          ('_ZNK29QDesignerMemberSheetExtension10memberNameEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'memberGroup': (
          ('_ZNK29QDesignerMemberSheetExtension11memberGroupEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setMemberGroup': (
          ('_ZN29QDesignerMemberSheetExtension14setMemberGroupEiRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'isVisible': (
          ('_ZNK29QDesignerMemberSheetExtension9isVisibleEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setVisible': (
          ('_ZN29QDesignerMemberSheetExtension10setVisibleEib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'isSignal': (
          ('_ZNK29QDesignerMemberSheetExtension8isSignalEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isSlot': (
          ('_ZNK29QDesignerMemberSheetExtension6isSlotEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'inheritedFromWidget': (
          ('_ZNK29QDesignerMemberSheetExtension19inheritedFromWidgetEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'declaredInClass': (
          ('_ZNK29QDesignerMemberSheetExtension15declaredInClassEi',
           ('address', 'text', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'signature': (
          ('_ZNK29QDesignerMemberSheetExtension9signatureEi',
           ('address', 'text', ''),
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
    Calls Qt's 'int QDesignerMemberSheetExtension::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#count
    """
    #  int QDesignerMemberSheetExtension::count() const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension5countEv',
    )

  @overload(str)
  def indexOf(self, name: str) -> int:
    """
    Calls Qt's 'int QDesignerMemberSheetExtension::indexOf(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#indexOf

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMemberSheetExtension::indexOf(const QString &name) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension7indexOfERK7QString',
        name,
    )

  @overload(int)
  def memberName(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheetExtension::memberName(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#memberName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheetExtension::memberName(int index) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension10memberNameEi',
        index,
    )

  @overload(int)
  def memberGroup(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheetExtension::memberGroup(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#memberGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheetExtension::memberGroup(int index) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension11memberGroupEi',
        index,
    )

  @overload(int)
  def isVisible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheetExtension::isVisible(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#isVisible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheetExtension::isVisible(int index) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension9isVisibleEi',
        index,
    )

  @overload(int)
  def isSignal(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheetExtension::isSignal(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#isSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheetExtension::isSignal(int index) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension8isSignalEi',
        index,
    )

  @overload(int)
  def isSlot(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheetExtension::isSlot(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#isSlot

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheetExtension::isSlot(int index) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension6isSlotEi',
        index,
    )

  @overload(int)
  def inheritedFromWidget(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMemberSheetExtension::inheritedFromWidget(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerMemberSheetExtension::inheritedFromWidget(int index)
    #      const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension19inheritedFromWidgetEi',
        index,
    )

  @overload(int)
  def declaredInClass(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheetExtension::declaredInClass(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#declaredInClass

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheetExtension::declaredInClass(int index)
    #      const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension15declaredInClassEi',
        index,
    )

  @overload(int)
  def signature(self, index: int) -> str:
    """
    Calls Qt's 'QString QDesignerMemberSheetExtension::signature(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#signature

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMemberSheetExtension::signature(int index) const
    return self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension9signatureEi',
        index,
    )

  @overload(int)
  def parameterTypes(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QDesignerMemberSheetExtension::parameterTypes(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#parameterTypes

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QDesignerMemberSheetExtension::parameterTypes(int
    #      index) const
    address = self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension14parameterTypesEi',
        index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def parameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QDesignerMemberSheetExtension::parameterNames(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#parameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QDesignerMemberSheetExtension::parameterNames(int
    #      index) const
    address = self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZNK29QDesignerMemberSheetExtension14parameterNamesEi',
        index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, str)
  def setMemberGroup(self, index: int, group: str) -> None:
    """
    Calls Qt's 'void QDesignerMemberSheetExtension::setMemberGroup(int index,
    const QString &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#setMemberGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerMemberSheetExtension::setMemberGroup(int index, const
    #      QString &group)
    self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZN29QDesignerMemberSheetExtension14setMemberGroupEiRK7QStri'
        'ng',
        index, group,
    )

  @overload(int, bool)
  def setVisible(self, index: int, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerMemberSheetExtension::setVisible(int index,
    bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermembersheetextension.html#setVisible

    Parameters
    ----------

    index : int
      Passed on as it is.

    b : bool
      Passed on as it is.
    """
    #  void QDesignerMemberSheetExtension::setVisible(int index, bool b)
    self._callAs(
        'QDesignerMemberSheetExtension',
        'ritual_ZN29QDesignerMemberSheetExtension10setVisibleEib',
        index, b,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDesignerMemberSheetExtension::QDesignerMemberSheetExtension()':
    the class is abstract, so C++ cannot make one, and the C++ class of ours
    does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerMemberSheetExtension.__init__' has no cute function yet. "
        "Qt's "
        "'QDesignerMemberSheetExtension::QDesignerMemberSheetExtension()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
