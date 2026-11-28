"""
QDesignerLayoutDecorationExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/layoutdecoration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect
  from ..QtWidgets import QLayout, QLayoutItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QPoint = WAIT['QPoint']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerLayoutDecorationExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerLayoutDecorationExtension: a plain Python
  object standing in front of one C++ QDesignerLayoutDecorationExtension.

  What exists
  -----------

  Every function of Qt's QDesignerLayoutDecorationExtension that has a ritual
  and that Python can call so far, 11 names in all: 'widgets', 'itemInfo',
  'indexOf', 'currentInsertMode', 'currentIndex', 'removeWidget',
  'insertRow', 'insertColumn', 'simplify', 'findItemAt', 'adjustIndicator'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDesignerLayoutDecorationExtension::~QDesignerLayoutDecorationExtension(
    )': the destructor: Python never removes a C++
    QDesignerLayoutDecorationExtension.
  - Qt's 'QPair<int, int> QDesignerLayoutDecorationExtension::currentCell()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QDesignerLayoutDecorationExtension::insertWidget(QWidget
    *widget, const QPair<int, int> &cell)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  5 of the 21 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerLayoutDecorationExtension is created at the first use,
    not by 'QDesignerLayoutDecorationExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerLayoutDecorationExtension.
  - Each name of Qt's QDesignerLayoutDecorationExtension that has no cute
    function yet, '__init__', 'currentCell', 'insertWidget', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDesignerLayoutDecorationExtension, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class InsertMode(CuteNum):
    """
    The enum 'QDesignerLayoutDecorationExtension::InsertMode' of Qt, with the
    3 names Qt gives in it.
    """

    InsertWidgetMode = Kee[int](0)
    InsertRowMode = Kee[int](1)
    InsertColumnMode = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerLayoutDecorationExtension'

  #  A C++ QDesignerLayoutDecorationExtension Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerLayoutDecorationExtension'

  #  The functions Qt calls itself that QDesignerLayoutDecorationExtension is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'widgets': (
          'QList<QWidget *> '
          'QDesignerLayoutDecorationExtension::widgets(QLayout *) const',
      ),
      'currentCell': (
          'QPair<int, int> '
          'QDesignerLayoutDecorationExtension::currentCell() const',
      ),
      'insertWidget': (
          'void QDesignerLayoutDecorationExtension::insertWidget(QWidget '
          '*, const QPair<int, int> &)',
      ),
  }

  #  The functions Qt calls itself that QDesignerLayoutDecorationExtension is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemInfo': (
          ('_ZNK34QDesignerLayoutDecorationExtension8itemInfoEi',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('int', 'number', ''),
           )),
      ),
      'indexOf': (
          ('_ZNK34QDesignerLayoutDecorationExtension7indexOfEP7QWidget',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
          ('_ZNK34QDesignerLayoutDecorationExtension7indexOfEP11QLayoutItem',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QLayoutItem'),
           )),
      ),
      'currentInsertMode': (
          ('_ZNK34QDesignerLayoutDecorationExtension17currentInsertModeEv',
           ('int', 'enum',
            'QtDesigner:QDesignerLayoutDecorationExtension.InsertMode'),
           ()),
      ),
      'currentIndex': (
          ('_ZNK34QDesignerLayoutDecorationExtension12currentIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'removeWidget': (
          ('_ZN34QDesignerLayoutDecorationExtension12removeWidgetEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'insertRow': (
          ('_ZN34QDesignerLayoutDecorationExtension9insertRowEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'insertColumn': (
          ('_ZN34QDesignerLayoutDecorationExtension12insertColumnEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'simplify': (
          ('_ZN34QDesignerLayoutDecorationExtension8simplifyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'findItemAt': (
          ('_ZNK34QDesignerLayoutDecorationExtension10findItemAtERK6QPoint',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
          ('_ZNK34QDesignerLayoutDecorationExtension10findItemAtEii',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'adjustIndicator': (
          ('_ZN34QDesignerLayoutDecorationExtension15adjustIndicatorERK6QPo'
           'inti',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
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

  @overload(QLayout)
  @overload(NoneType)
  def widgets(self, layout: Optional[QLayout]) -> QList[QWidget]:
    """
    Calls Qt's 'QList<QWidget *>
    QDesignerLayoutDecorationExtension::widgets(QLayout *layout) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#widgets

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWidget *> QDesignerLayoutDecorationExtension::widgets(QLayout
    #      *layout) const
    address = self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension7widgetsEP7QLayout',
        self._addressOf(layout),
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  @overload(int)
  def itemInfo(self, index: int) -> QRect:
    """
    Calls Qt's 'QRect QDesignerLayoutDecorationExtension::itemInfo(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#itemInfo

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDesignerLayoutDecorationExtension::itemInfo(int index) const
    address = self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension8itemInfoEi',
        index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, widget: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QDesignerLayoutDecorationExtension::indexOf(QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#indexOf

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QDesignerLayoutDecorationExtension::indexOf(QWidget *widget) const
    return self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension7indexOfEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QLayoutItem)
  def indexOf(self, item: Optional[QLayoutItem]) -> int:
    """
    Calls Qt's 'int QDesignerLayoutDecorationExtension::indexOf(QLayoutItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#indexOf

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QDesignerLayoutDecorationExtension::indexOf(QLayoutItem *item)
    #      const
    return self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension7indexOfEP11QLayoutI'
        'tem',
        self._addressOf(item, 'QLayoutItem'),
    )

  def currentInsertMode(self) -> InsertMode:
    """
    Calls Qt's 'InsertMode
    QDesignerLayoutDecorationExtension::currentInsertMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html

    Returns
    -------

    InsertMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InsertMode(number)'
      gives.
    """
    #  InsertMode QDesignerLayoutDecorationExtension::currentInsertMode()
    #      const
    return QDesignerLayoutDecorationExtension.InsertMode(self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension17currentInsertModeE'
        'v',
    ))

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QDesignerLayoutDecorationExtension::currentIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html
    """
    #  int QDesignerLayoutDecorationExtension::currentIndex() const
    return self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension12currentIndexEv',
    )

  @overload(QPoint)
  def findItemAt(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QDesignerLayoutDecorationExtension::findItemAt(const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#findItemAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QDesignerLayoutDecorationExtension::findItemAt(const QPoint &pos)
    #      const
    return self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension10findItemAtERK6QPoi'
        'nt',
        self._valueOf(pos),
    )

  @overload(int, int)
  def findItemAt(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QDesignerLayoutDecorationExtension::findItemAt(int row,
    int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#findItemAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QDesignerLayoutDecorationExtension::findItemAt(int row, int
    #      column) const
    return self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZNK34QDesignerLayoutDecorationExtension10findItemAtEii',
        row, column,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QDesignerLayoutDecorationExtension::QDesignerLayoutDecorationExtension(
    )': the class is abstract, so C++ cannot make one, and the C++ class of
    ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerLayoutDecorationExtension.__init__' has no cute function "
        "yet. Qt's "
        "'QDesignerLayoutDecorationExtension::QDesignerLayoutDecorationExten"
        "sion()': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  @overload(QWidget)
  @overload(NoneType)
  def removeWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerLayoutDecorationExtension::removeWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerLayoutDecorationExtension::removeWidget(QWidget *widget)
    self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZN34QDesignerLayoutDecorationExtension12removeWidgetEP7QWid'
        'get',
        self._addressOf(widget),
    )

  @overload(int)
  def insertRow(self, row: int) -> None:
    """
    Calls Qt's 'void QDesignerLayoutDecorationExtension::insertRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QDesignerLayoutDecorationExtension::insertRow(int row)
    self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZN34QDesignerLayoutDecorationExtension9insertRowEi',
        row,
    )

  @overload(int)
  def insertColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QDesignerLayoutDecorationExtension::insertColumn(int
    column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QDesignerLayoutDecorationExtension::insertColumn(int column)
    self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZN34QDesignerLayoutDecorationExtension12insertColumnEi',
        column,
    )

  def simplify(self) -> None:
    """
    Calls Qt's 'void QDesignerLayoutDecorationExtension::simplify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html#simplify
    """
    #  void QDesignerLayoutDecorationExtension::simplify()
    self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZN34QDesignerLayoutDecorationExtension8simplifyEv',
    )

  @overload(QPoint, int)
  def adjustIndicator(self, pos: QPoint, index: int) -> None:
    """
    Calls Qt's 'void
    QDesignerLayoutDecorationExtension::adjustIndicator(const QPoint &pos,
    int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerlayoutdecorationextension.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    index : int
      Passed on as it is.
    """
    #  void QDesignerLayoutDecorationExtension::adjustIndicator(const QPoint
    #      &pos, int index)
    self._callAs(
        'QDesignerLayoutDecorationExtension',
        'ritual_ZN34QDesignerLayoutDecorationExtension15adjustIndicatorERK6'
        'QPointi',
        self._valueOf(pos), index,
    )

  @staticmethod
  def currentCell(*__, **_) -> Never:
    """
    Qt's 'QPair<int, int> QDesignerLayoutDecorationExtension::currentCell()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDesignerLayoutDecorationExtension.currentCell' has no cute "
        "function yet. Qt's 'QPair<int, int> "
        "QDesignerLayoutDecorationExtension::currentCell() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def insertWidget(*__, **_) -> Never:
    """
    Qt's 'void QDesignerLayoutDecorationExtension::insertWidget(QWidget
    *widget, const QPair<int, int> &cell)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDesignerLayoutDecorationExtension.insertWidget' has no cute "
        "function yet. Qt's 'void "
        "QDesignerLayoutDecorationExtension::insertWidget(QWidget *widget, "
        "const QPair<int, int> &cell)': takes a type Python has no way to "
        "hand over yet.")
