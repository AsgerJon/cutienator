"""
QSplitterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSplitterPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QFramePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QSize
  from . import QSplitter, QSplitterLayoutStruct, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QSplitterLayoutStruct = WAIT['QSplitterLayoutStruct']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSplitterPrivate(QFramePrivate):
  """
  The cute side of Qt's QSplitterPrivate: a plain Python object standing in
  front of one C++ QSplitterPrivate.

  It is built on the cute 'QFramePrivate', as Qt's QSplitterPrivate is built
  on Qt's QFramePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplitterPrivate that has a ritual and that Python
  can call so far, 14 names in all: 'q_func', 'pick', 'trans', 'init',
  'recalc', 'doResize', 'storeSizes', 'collapsible', 'findWidget',
  'insertWidget_helper', 'insertWidget', 'setGeo', 'updateHandles',
  'shouldShowWidget'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSplitter *QSplitterPrivate::q_func() const': takes in Python
    what 'QSplitter *QSplitterPrivate::q_func()' takes.
  - Qt's 'QSplitterPrivate::~QSplitterPrivate()': the destructor: Python
    never removes a C++ QSplitterPrivate.
  - Qt's 'void QSplitterPrivate::getRange(int index, int *a1, int *a2, int
    *a3, int *a4) const': takes a number to change where it is.
  - Qt's 'void QSplitterPrivate::addContribution(int a0, int *a1, int *a2,
    bool a3) const': takes a number to change where it is.
  - Qt's 'int QSplitterPrivate::adjustPos(int a0, int a1, int *a2, int *a3,
    int *a4, int *a5) const': takes a number to change where it is.
  - Qt's 'void QSplitterPrivate::doMove(bool backwards, int pos, int index,
    int delta, bool mayCollapse, int *positions, int *widths)': takes a
    number to change where it is.
  - Qt's 'int QSplitterPrivate::findWidgetJustBeforeOrJustAfter(int index,
    int delta, int &collapsibleSize) const': takes a number to change where
    it is.
  - Qt's 'void QSplitterPrivate::setSizes_helper(const QList<int> &sizes,
    bool clampNegativeSize)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QSplitterPrivate is created at the first use, not by
    'QSplitterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplitterPrivate.
  - Each name of Qt's QSplitterPrivate that has no cute function yet,
    'addContribution', 'adjustPos', 'doMove',
    'findWidgetJustBeforeOrJustAfter', 'getRange', 'setSizes_helper', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplitterPrivate'

  #  A C++ QSplitterPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSplitterPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def pick(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QSplitterPrivate::pick(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#pick

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QSplitterPrivate::pick(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate4pickERK6QPoint', self._valueOf(pos),
    )

  @overload(QSize)
  def pick(self, s: QSize) -> int:
    """
    Calls Qt's 'int QSplitterPrivate::pick(const QSize &s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#pick

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  int QSplitterPrivate::pick(const QSize &s) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate4pickERK5QSize', self._valueOf(s),
    )

  @overload(QPoint)
  def trans(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QSplitterPrivate::trans(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#trans

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QSplitterPrivate::trans(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate5transERK6QPoint', self._valueOf(pos),
    )

  @overload(QSize)
  def trans(self, s: QSize) -> int:
    """
    Calls Qt's 'int QSplitterPrivate::trans(const QSize &s) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#trans

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  int QSplitterPrivate::trans(const QSize &s) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate5transERK5QSize', self._valueOf(s),
    )

  @overload(QSplitterLayoutStruct)
  @overload(NoneType)
  def collapsible(self, a0: Optional[QSplitterLayoutStruct]) -> bool:
    """
    Calls Qt's 'bool QSplitterPrivate::collapsible(QSplitterLayoutStruct *a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#collapsible

    Parameters
    ----------

    a0 : Optional[QSplitterLayoutStruct]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSplitterPrivate::collapsible(QSplitterLayoutStruct *a0) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate11collapsibleEP21QSplitterLayoutStruct',
        self._addressOf(a0),
    )

  @overload(int)
  def collapsible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QSplitterPrivate::collapsible(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#collapsible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QSplitterPrivate::collapsible(int index) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate11collapsibleEi', index,
    )

  @overload(QWidget)
  @overload(NoneType)
  def findWidget(
      self,
      a0: Optional[QWidget],
  ) -> Optional[QSplitterLayoutStruct]:
    """
    Calls Qt's 'QSplitterLayoutStruct *QSplitterPrivate::findWidget(QWidget
    *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#findWidget

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSplitterLayoutStruct]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitterLayoutStruct *QSplitterPrivate::findWidget(QWidget *a0) const
    address = self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate10findWidgetEP7QWidget',
        self._addressOf(a0),
    )
    from . import QSplitterLayoutStruct
    return QSplitterLayoutStruct._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def shouldShowWidget(self, w: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QSplitterPrivate::shouldShowWidget(const QWidget *w)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterprivate.html#shouldShowWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSplitterPrivate::shouldShowWidget(const QWidget *w) const
    return self.uglySide.call(
        'ritual_ZNK16QSplitterPrivate16shouldShowWidgetEPK7QWidget',
        self._addressOf(w),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSplitterLayoutStruct, int, int, bool)
  @overload(NoneType, int, int, bool)
  def setGeo(
      self,
      s: Optional[QSplitterLayoutStruct],
      pos: int,
      size: int,
      allowCollapse: bool,
  ) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::setGeo(QSplitterLayoutStruct *s, int
    pos, int size, bool allowCollapse)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#setGeo

    Parameters
    ----------

    s : Optional[QSplitterLayoutStruct]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : int
      Passed on as it is.

    size : int
      Passed on as it is.

    allowCollapse : bool
      Passed on as it is.
    """
    #  void QSplitterPrivate::setGeo(QSplitterLayoutStruct *s, int pos, int
    #      size, bool allowCollapse)
    self.uglySide.call(
        'ritual_ZN16QSplitterPrivate6setGeoEP21QSplitterLayoutStructiib',
        self._addressOf(s), pos, size, allowCollapse,
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
    Notes what was given, for Qt's 'QSplitterPrivate::QSplitterPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterprivate.html#QSplitterPrivate
    """
    #  QSplitterPrivate::QSplitterPrivate()
    self._noteCreation(QSplitterPrivate, lambda: Rituals.call(
        'ritual_ZN16QSplitterPrivateC1Ev',
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

  def q_func(self) -> Optional[QSplitter]:
    """
    Calls Qt's 'QSplitter *QSplitterPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#q_func

    Returns
    -------

    Optional[QSplitter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitter *QSplitterPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QSplitterPrivate6q_funcEv')
    from . import QSplitter
    return QSplitter._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#init
    """
    #  void QSplitterPrivate::init()
    self.uglySide.call('ritual_ZN16QSplitterPrivate4initEv')

  @overload()
  @overload(bool)
  def recalc(self, update: bool = False) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::recalc(bool update)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#recalc

    Parameters
    ----------

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSplitterPrivate::recalc(bool update)
    self.uglySide.call('ritual_ZN16QSplitterPrivate6recalcEb', update)

  def doResize(self) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::doResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#doResize
    """
    #  void QSplitterPrivate::doResize()
    self.uglySide.call('ritual_ZN16QSplitterPrivate8doResizeEv')

  def storeSizes(self) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::storeSizes()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#storeSizes
    """
    #  void QSplitterPrivate::storeSizes()
    self.uglySide.call('ritual_ZN16QSplitterPrivate10storeSizesEv')

  @overload(int, QWidget, bool)
  @overload(int, NoneType, bool)
  def insertWidget_helper(
      self,
      index: int,
      widget: Optional[QWidget],
      show: bool,
  ) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::insertWidget_helper(int index, QWidget
    *widget, bool show)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterprivate.html#insertWidget_helper

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    show : bool
      Passed on as it is.
    """
    #  void QSplitterPrivate::insertWidget_helper(int index, QWidget *widget,
    #      bool show)
    self.uglySide.call(
        'ritual_ZN16QSplitterPrivate19insertWidget_helperEiP7QWidgetb',
        index, self._addressOf(widget), show,
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def insertWidget(
      self,
      index: int,
      a1: Optional[QWidget],
  ) -> Optional[QSplitterLayoutStruct]:
    """
    Calls Qt's 'QSplitterLayoutStruct *QSplitterPrivate::insertWidget(int
    index, QWidget *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterprivate.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    a1 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSplitterLayoutStruct]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitterLayoutStruct *QSplitterPrivate::insertWidget(int index,
    #      QWidget *a1)
    address = self.uglySide.call(
        'ritual_ZN16QSplitterPrivate12insertWidgetEiP7QWidget',
        index, self._addressOf(a1),
    )
    from . import QSplitterLayoutStruct
    return QSplitterLayoutStruct._cuteAt(address)

  def updateHandles(self) -> None:
    """
    Calls Qt's 'void QSplitterPrivate::updateHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterprivate.html#updateHandles
    """
    #  void QSplitterPrivate::updateHandles()
    self.uglySide.call('ritual_ZN16QSplitterPrivate13updateHandlesEv')

  @staticmethod
  def addContribution(*__, **_) -> Never:
    """
    Qt's 'void QSplitterPrivate::addContribution(int a0, int *a1, int *a2,
    bool a3) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSplitterPrivate.addContribution' has no cute function yet. Qt's "
        "'void QSplitterPrivate::addContribution(int a0, int *a1, int *a2, "
        "bool a3) const': takes a number to change where it is.")

  @staticmethod
  def adjustPos(*__, **_) -> Never:
    """
    Qt's 'int QSplitterPrivate::adjustPos(int a0, int a1, int *a2, int *a3,
    int *a4, int *a5) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSplitterPrivate.adjustPos' has no cute function yet. Qt's 'int "
        "QSplitterPrivate::adjustPos(int a0, int a1, int *a2, int *a3, int "
        "*a4, int *a5) const': takes a number to change where it is.")

  @staticmethod
  def doMove(*__, **_) -> Never:
    """
    Qt's 'void QSplitterPrivate::doMove(bool backwards, int pos, int index,
    int delta, bool mayCollapse, int *positions, int *widths)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QSplitterPrivate.doMove' has no cute function yet. Qt's 'void "
        "QSplitterPrivate::doMove(bool backwards, int pos, int index, int "
        "delta, bool mayCollapse, int *positions, int *widths)': takes a "
        "number to change where it is.")

  @staticmethod
  def findWidgetJustBeforeOrJustAfter(*__, **_) -> Never:
    """
    Qt's 'int QSplitterPrivate::findWidgetJustBeforeOrJustAfter(int index,
    int delta, int &collapsibleSize) const': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QSplitterPrivate.findWidgetJustBeforeOrJustAfter' has no cute "
        "function yet. Qt's 'int "
        "QSplitterPrivate::findWidgetJustBeforeOrJustAfter(int index, int "
        "delta, int &collapsibleSize) const': takes a number to change "
        "where it is.")

  @staticmethod
  def getRange(*__, **_) -> Never:
    """
    Qt's 'void QSplitterPrivate::getRange(int index, int *a1, int *a2, int
    *a3, int *a4) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSplitterPrivate.getRange' has no cute function yet. Qt's 'void "
        "QSplitterPrivate::getRange(int index, int *a1, int *a2, int *a3, "
        "int *a4) const': takes a number to change where it is.")

  @staticmethod
  def setSizes_helper(*__, **_) -> Never:
    """
    Qt's 'void QSplitterPrivate::setSizes_helper(const QList<int> &sizes,
    bool clampNegativeSize)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSplitterPrivate.setSizes_helper' has no cute function yet. Qt's "
        "'void QSplitterPrivate::setSizes_helper(const QList<int> &sizes, "
        "bool clampNegativeSize)': takes a type Python has no way to hand "
        "over yet.")
