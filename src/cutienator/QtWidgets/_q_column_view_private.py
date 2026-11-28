"""
QColumnViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColumnViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractItemViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex
  from . import QAbstractItemView, QColumnView, QColumnViewPreviewColumn
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemView = WAIT['QAbstractItemView']
  QModelIndex = WAIT['QModelIndex']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColumnViewPrivate(QAbstractItemViewPrivate):
  """
  The cute side of Qt's QColumnViewPrivate: a plain Python object standing in
  front of one C++ QColumnViewPrivate.

  It is built on the cute 'QAbstractItemViewPrivate', as Qt's
  QColumnViewPrivate is built on Qt's QAbstractItemViewPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QColumnViewPrivate that has a ritual and that Python
  can call so far, 9 names in all: 'q_func', 'updateScrollbars',
  'disconnectView', 'doLayout', 'setPreviewWidget', 'createPreviewColumn',
  'gripMoved', 'clicked', 'columnsInserted'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QColumnView *QColumnViewPrivate::q_func() const': takes in
    Python what 'QColumnView *QColumnViewPrivate::q_func()' takes.
  - Qt's 'QColumnViewPrivate::~QColumnViewPrivate()': the destructor: Python
    never removes a C++ QColumnViewPrivate.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 5 leans on 'QColumnViewGrip; 1 leans on
  'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QColumnViewPrivate is created at the first use, not by
    'QColumnViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColumnViewPrivate.
  - Each name of Qt's QColumnViewPrivate that has no cute function yet,
    '__init__', 'changeCurrentColumn', 'checkColumnCreation', 'closeColumns',
    'createColumn', 'initialize', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColumnViewPrivate'

  #  A C++ QColumnViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QColumnViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setPreviewWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::setPreviewWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewprivate.html#setPreviewWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewPrivate::setPreviewWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN18QColumnViewPrivate16setPreviewWidgetEP7QWidget',
        self._addressOf(widget),
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
    Qt's 'QColumnViewPrivate::QColumnViewPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColumnViewPrivate.__init__' has no cute function yet. Qt's "
        "'QColumnViewPrivate::QColumnViewPrivate()': leans on "
        "'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex "
        "const&, int, int)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QColumnView]:
    """
    Calls Qt's 'QColumnView *QColumnViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnviewprivate.html#q_func

    Returns
    -------

    Optional[QColumnView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QColumnView *QColumnViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QColumnViewPrivate6q_funcEv')
    from . import QColumnView
    return QColumnView._cuteAt(address)

  def updateScrollbars(self) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::updateScrollbars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewprivate.html#updateScrollbars
    """
    #  void QColumnViewPrivate::updateScrollbars()
    self.uglySide.call('ritual_ZN18QColumnViewPrivate16updateScrollbarsEv')

  @overload(QAbstractItemView)
  @overload(NoneType)
  def disconnectView(self, view: Optional[QAbstractItemView]) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::disconnectView(QAbstractItemView
    *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewprivate.html#disconnectView

    Parameters
    ----------

    view : Optional[QAbstractItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewPrivate::disconnectView(QAbstractItemView *view)
    self.uglySide.call(
        'ritual_ZN18QColumnViewPrivate14disconnectViewEP17QAbstractItemView',
        self._addressOf(view),
    )

  def doLayout(self) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::doLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnviewprivate.html#doLayout
    """
    #  void QColumnViewPrivate::doLayout()
    self.uglySide.call('ritual_ZN18QColumnViewPrivate8doLayoutEv')

  def createPreviewColumn(self) -> Optional[QColumnViewPreviewColumn]:
    """
    Calls Qt's 'QColumnViewPreviewColumn
    *QColumnViewPrivate::createPreviewColumn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewprivate.html#createPreviewColumn

    Returns
    -------

    Optional[QColumnViewPreviewColumn]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QColumnViewPreviewColumn *QColumnViewPrivate::createPreviewColumn()
    address = self.uglySide.call(
        'ritual_ZN18QColumnViewPrivate19createPreviewColumnEv',
    )
    from . import QColumnViewPreviewColumn
    return QColumnViewPreviewColumn._cuteAt(address)

  @overload(int)
  def gripMoved(self, offset: int) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::gripMoved(int offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnviewprivate.html#gripMoved

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QColumnViewPrivate::gripMoved(int offset)
    self.uglySide.call('ritual_ZN18QColumnViewPrivate9gripMovedEi', offset)

  @overload(QModelIndex)
  def clicked(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::clicked(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnviewprivate.html#clicked

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QColumnViewPrivate::clicked(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN18QColumnViewPrivate7clickedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex, int, int)
  def columnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QColumnViewPrivate::columnsInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewprivate.html#columnsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QColumnViewPrivate::columnsInserted(const QModelIndex &parent,
    #      int start, int end)
    self.uglySide.call(
        'ritual_ZN18QColumnViewPrivate15columnsInsertedERK11QModelIndexii',
        self._valueOf(parent), start, end,
    )

  @staticmethod
  def changeCurrentColumn(*__, **_) -> Never:
    """
    Qt's 'void QColumnViewPrivate::changeCurrentColumn()': leans on
    'QColumnViewGrip::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColumnViewPrivate.changeCurrentColumn' has no cute function yet. "
        "Qt's 'void QColumnViewPrivate::changeCurrentColumn()': leans on "
        "'QColumnViewGrip::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def checkColumnCreation(*__, **_) -> Never:
    """
    Qt's 'void QColumnViewPrivate::checkColumnCreation(const QModelIndex
    &parent)': leans on 'QColumnViewGrip::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QColumnViewPrivate.checkColumnCreation' has no cute function yet. "
        "Qt's 'void QColumnViewPrivate::checkColumnCreation(const "
        "QModelIndex &parent)': leans on "
        "'QColumnViewGrip::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def closeColumns(*__, **_) -> Never:
    """
    Qt's 'void QColumnViewPrivate::closeColumns(const QModelIndex &parent,
    bool build)': leans on 'QColumnViewGrip::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QColumnViewPrivate.closeColumns' has no cute function yet. Qt's "
        "'void QColumnViewPrivate::closeColumns(const QModelIndex &parent, "
        "bool build)': leans on 'QColumnViewGrip::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def createColumn(*__, **_) -> Never:
    """
    Qt's 'QAbstractItemView *QColumnViewPrivate::createColumn(const
    QModelIndex &index, bool show)': leans on
    'QColumnViewGrip::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColumnViewPrivate.createColumn' has no cute function yet. Qt's "
        "'QAbstractItemView *QColumnViewPrivate::createColumn(const "
        "QModelIndex &index, bool show)': leans on "
        "'QColumnViewGrip::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QColumnViewPrivate::initialize()': leans on
    'QColumnViewGrip::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QColumnViewPrivate.initialize' has no cute function yet. Qt's "
        "'void QColumnViewPrivate::initialize()': leans on "
        "'QColumnViewGrip::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
