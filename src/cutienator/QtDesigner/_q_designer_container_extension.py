"""
QDesignerContainerExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/container.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerContainerExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerContainerExtension: a plain Python object
  standing in front of one C++ QDesignerContainerExtension.

  What exists
  -----------

  Every function of Qt's QDesignerContainerExtension that has a ritual and
  that Python can call so far, 9 names in all: 'count', 'widget',
  'currentIndex', 'setCurrentIndex', 'canAddWidget', 'addWidget',
  'insertWidget', 'canRemove', 'remove'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerContainerExtension::~QDesignerContainerExtension()': the
    destructor: Python never removes a C++ QDesignerContainerExtension.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerContainerExtension is created at the first use, not by
    'QDesignerContainerExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerContainerExtension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerContainerExtension'

  #  A C++ QDesignerContainerExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerContainerExtension'

  #  The functions Qt calls itself that QDesignerContainerExtension is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'count': (
          ('_ZNK27QDesignerContainerExtension5countEv',
           ('int', 'number', ''),
           ()),
      ),
      'widget': (
          ('_ZNK27QDesignerContainerExtension6widgetEi',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('int', 'number', ''),
           )),
      ),
      'currentIndex': (
          ('_ZNK27QDesignerContainerExtension12currentIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'setCurrentIndex': (
          ('_ZN27QDesignerContainerExtension15setCurrentIndexEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'canAddWidget': (
          ('_ZNK27QDesignerContainerExtension12canAddWidgetEv',
           ('bool', 'number', ''),
           ()),
      ),
      'addWidget': (
          ('_ZN27QDesignerContainerExtension9addWidgetEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'insertWidget': (
          ('_ZN27QDesignerContainerExtension12insertWidgetEiP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'canRemove': (
          ('_ZNK27QDesignerContainerExtension9canRemoveEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'remove': (
          ('_ZN27QDesignerContainerExtension6removeEi',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'int QDesignerContainerExtension::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#count
    """
    #  int QDesignerContainerExtension::count() const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerContainerExtension5countEv',
    )

  @overload(int)
  def widget(self, index: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerContainerExtension::widget(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#widget

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
    #  QWidget *QDesignerContainerExtension::widget(int index) const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerContainerExtension6widgetEi', index,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QDesignerContainerExtension::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#currentIndex
    """
    #  int QDesignerContainerExtension::currentIndex() const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerContainerExtension12currentIndexEv',
    )

  def canAddWidget(self) -> bool:
    """
    Calls Qt's 'bool QDesignerContainerExtension::canAddWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#canAddWidget
    """
    #  bool QDesignerContainerExtension::canAddWidget() const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerContainerExtension12canAddWidgetEv',
    )

  @overload(int)
  def canRemove(self, index: int) -> bool:
    """
    Calls Qt's 'bool QDesignerContainerExtension::canRemove(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#canRemove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QDesignerContainerExtension::canRemove(int index) const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerContainerExtension9canRemoveEi', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QDesignerContainerExtension::setCurrentIndex(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QDesignerContainerExtension::setCurrentIndex(int index)
    self.uglySide.call(
        'ritual_ZN27QDesignerContainerExtension15setCurrentIndexEi', index,
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
    'QDesignerContainerExtension::QDesignerContainerExtension()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html
    """
    #  QDesignerContainerExtension::QDesignerContainerExtension()
    self._noteCreation(QDesignerContainerExtension, lambda: Rituals.call(
        'ritual_ZN27QDesignerContainerExtensionC1Ev',
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

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerContainerExtension::addWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#addWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerContainerExtension::addWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN27QDesignerContainerExtension9addWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def insertWidget(self, index: int, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerContainerExtension::insertWidget(int index,
    QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerContainerExtension::insertWidget(int index, QWidget
    #      *widget)
    self.uglySide.call(
        'ritual_ZN27QDesignerContainerExtension12insertWidgetEiP7QWidget',
        index, self._addressOf(widget),
    )

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void QDesignerContainerExtension::remove(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercontainerextension.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QDesignerContainerExtension::remove(int index)
    self.uglySide.call(
        'ritual_ZN27QDesignerContainerExtension6removeEi', index,
    )
