"""
QDesignerFormWindowCursorInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformwindowcursor.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormWindowCursorInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerFormWindowCursorInterface: a plain Python
  object standing in front of one C++ QDesignerFormWindowCursorInterface.

  What exists
  -----------

  Every function of Qt's QDesignerFormWindowCursorInterface that has a ritual
  and that Python can call so far, 14 names in all: 'formWindow',
  'movePosition', 'position', 'setPosition', 'current', 'widgetCount',
  'widget', 'hasSelection', 'selectedWidgetCount', 'selectedWidget',
  'setProperty', 'setWidgetProperty', 'resetWidgetProperty',
  'isWidgetSelected'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDesignerFormWindowCursorInterface::~QDesignerFormWindowCursorInterface(
    )': the destructor: Python never removes a C++
    QDesignerFormWindowCursorInterface.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerFormWindowCursorInterface is created at the first use,
    not by 'QDesignerFormWindowCursorInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerFormWindowCursorInterface.
  """

  #  The enums Qt writes inside QDesignerFormWindowCursorInterface, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class MoveMode(CuteNum):
    """
    The enum 'QDesignerFormWindowCursorInterface::MoveMode' of Qt, with the 2
    names Qt gives in it.
    """

    MoveAnchor = Kee[int](0)
    KeepAnchor = Kee[int](1)

  class MoveOperation(CuteNum):
    """
    The enum 'QDesignerFormWindowCursorInterface::MoveOperation' of Qt, with
    the 9 names Qt gives in it.
    """

    NoMove = Kee[int](0)
    Start = Kee[int](1)
    End = Kee[int](2)
    Next = Kee[int](3)
    Prev = Kee[int](4)
    Left = Kee[int](5)
    Right = Kee[int](6)
    Up = Kee[int](7)
    Down = Kee[int](8)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerFormWindowCursorInterface'

  #  A C++ QDesignerFormWindowCursorInterface Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerFormWindowCursorInterface'

  #  The functions Qt calls itself that QDesignerFormWindowCursorInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'formWindow': (
          ('_ZNK34QDesignerFormWindowCursorInterface10formWindowEv',
           ('address', 'address', 'QtDesigner:QDesignerFormWindowInterface'),
           ()),
      ),
      'movePosition': (
          ('_ZN34QDesignerFormWindowCursorInterface12movePositionENS_13Move'
           'OperationENS_8MoveModeE',
           ('bool', 'number', ''),
           (
               ('int', 'enum',
                'QtDesigner:QDesignerFormWindowCursorInterface.MoveOperation'),
               ('int', 'enum',
                'QtDesigner:QDesignerFormWindowCursorInterface.MoveMode'),
           )),
      ),
      'position': (
          ('_ZNK34QDesignerFormWindowCursorInterface8positionEv',
           ('int', 'number', ''),
           ()),
      ),
      'setPosition': (
          ('_ZN34QDesignerFormWindowCursorInterface11setPositionEiNS_8MoveM'
           'odeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum',
                'QtDesigner:QDesignerFormWindowCursorInterface.MoveMode'),
           )),
      ),
      'current': (
          ('_ZNK34QDesignerFormWindowCursorInterface7currentEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'widgetCount': (
          ('_ZNK34QDesignerFormWindowCursorInterface11widgetCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'widget': (
          ('_ZNK34QDesignerFormWindowCursorInterface6widgetEi',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('int', 'number', ''),
           )),
      ),
      'hasSelection': (
          ('_ZNK34QDesignerFormWindowCursorInterface12hasSelectionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'selectedWidgetCount': (
          ('_ZNK34QDesignerFormWindowCursorInterface19selectedWidgetCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'selectedWidget': (
          ('_ZNK34QDesignerFormWindowCursorInterface14selectedWidgetEi',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('int', 'number', ''),
           )),
      ),
      'setProperty': (
          ('_ZN34QDesignerFormWindowCursorInterface11setPropertyERK7QString'
           'RK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'setWidgetProperty': (
          ('_ZN34QDesignerFormWindowCursorInterface17setWidgetPropertyEP7QW'
           'idgetRK7QStringRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'resetWidgetProperty': (
          ('_ZN34QDesignerFormWindowCursorInterface19resetWidgetPropertyEP7'
           'QWidgetRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
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

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowCursorInterface::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowCursorInterface::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def position(self) -> int:
    """
    Calls Qt's 'int QDesignerFormWindowCursorInterface::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html#position
    """
    #  int QDesignerFormWindowCursorInterface::position() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface8positionEv',
    )

  def current(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerFormWindowCursorInterface::current()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html#current

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormWindowCursorInterface::current() const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface7currentEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def widgetCount(self) -> int:
    """
    Calls Qt's 'int QDesignerFormWindowCursorInterface::widgetCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html
    """
    #  int QDesignerFormWindowCursorInterface::widgetCount() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface11widgetCountEv',
    )

  @overload(int)
  def widget(self, index: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerFormWindowCursorInterface::widget(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html#widget

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormWindowCursorInterface::widget(int index) const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface6widgetEi', index,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowCursorInterface::hasSelection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html
    """
    #  bool QDesignerFormWindowCursorInterface::hasSelection() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface12hasSelectionEv',
    )

  def selectedWidgetCount(self) -> int:
    """
    Calls Qt's 'int QDesignerFormWindowCursorInterface::selectedWidgetCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html
    """
    #  int QDesignerFormWindowCursorInterface::selectedWidgetCount() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface19selectedWidgetCoun'
        'tEv',
    )

  @overload(int)
  def selectedWidget(self, index: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *QDesignerFormWindowCursorInterface::selectedWidget(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormWindowCursorInterface::selectedWidget(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface14selectedWidgetEi',
        index,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def isWidgetSelected(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool
    QDesignerFormWindowCursorInterface::isWidgetSelected(QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerFormWindowCursorInterface::isWidgetSelected(QWidget
    #      *widget) const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerFormWindowCursorInterface16isWidgetSelectedEP'
        '7QWidget',
        self._addressOf(widget),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, MoveMode)
  def setPosition(
      self,
      pos: int,
      mode: MoveMode = MoveMode.MoveAnchor,
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowCursorInterface::setPosition(int pos,
    MoveMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    pos : int
      Passed on as it is.

    mode : MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      MoveMode.MoveAnchor.
    """
    #  void QDesignerFormWindowCursorInterface::setPosition(int pos, MoveMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN34QDesignerFormWindowCursorInterface11setPositionEiNS_8Mo'
        'veModeE',
        pos, mode.value,
    )

  @overload(str, QVariant)
  def setProperty(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowCursorInterface::setProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerFormWindowCursorInterface::setProperty(const QString
    #      &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN34QDesignerFormWindowCursorInterface11setPropertyERK7QStr'
        'ingRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(QWidget, str, QVariant)
  @overload(NoneType, str, QVariant)
  def setWidgetProperty(
      self,
      widget: Optional[QWidget],
      name: str,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowCursorInterface::setWidgetProperty(QWidget *widget,
    const QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDesignerFormWindowCursorInterface::setWidgetProperty(QWidget
    #      *widget, const QString &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN34QDesignerFormWindowCursorInterface17setWidgetPropertyEP'
        '7QWidgetRK7QStringRK8QVariant',
        self._addressOf(widget), name, self._valueOf(value),
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
    'QDesignerFormWindowCursorInterface::QDesignerFormWindowCursorInterface(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html
    """
    #  QDesignerFormWindowCursorInterface::
    #      QDesignerFormWindowCursorInterface()
    self._noteCreation(
        QDesignerFormWindowCursorInterface, lambda: Rituals.call(
            'ritual_ZN34QDesignerFormWindowCursorInterfaceC1Ev',
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

  @overload(MoveOperation)
  @overload(MoveOperation, MoveMode)
  def movePosition(
      self,
      op: MoveOperation,
      mode: MoveMode = MoveMode.MoveAnchor,
  ) -> bool:
    """
    Calls Qt's 'bool
    QDesignerFormWindowCursorInterface::movePosition(MoveOperation op,
    MoveMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    op : MoveOperation
      Passed on as its number.

    mode : MoveMode
      Passed on as its number. May be left out, as in Qt: it is then
      MoveMode.MoveAnchor.
    """
    #  bool QDesignerFormWindowCursorInterface::movePosition(MoveOperation
    #      op, MoveMode mode)
    return self.uglySide.call(
        'ritual_ZN34QDesignerFormWindowCursorInterface12movePositionENS_13M'
        'oveOperationENS_8MoveModeE',
        op.value, mode.value,
    )

  @overload(QWidget, str)
  @overload(NoneType, str)
  def resetWidgetProperty(
      self,
      widget: Optional[QWidget],
      name: str,
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowCursorInterface::resetWidgetProperty(QWidget *widget,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowcursorinterface.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowCursorInterface::resetWidgetProperty(QWidget
    #      *widget, const QString &name)
    self.uglySide.call(
        'ritual_ZN34QDesignerFormWindowCursorInterface19resetWidgetProperty'
        'EP7QWidgetRK7QString',
        self._addressOf(widget), name,
    )
