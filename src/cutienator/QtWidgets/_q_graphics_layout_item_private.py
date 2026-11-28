"""
QGraphicsLayoutItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayoutitem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsLayoutItemPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSizeF
  from . import QGraphicsItem, QGraphicsLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsLayoutItem = WAIT['QGraphicsLayoutItem']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsLayoutItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsLayoutItemPrivate: a plain Python object
  standing in front of one C++ QGraphicsLayoutItemPrivate.

  C++ hands a QGraphicsLayoutItemPrivate around as a copy, so every C++
  QGraphicsLayoutItemPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QGraphicsLayoutItemPrivate that has a ritual and
  that Python can call so far, 9 names in all: 'q_func', 'get', 'init',
  'parentItem', 'ensureUserSizeHints', 'setSize', 'setSizeComponent',
  'hasHeightForWidth', 'hasWidthForHeight'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsLayoutItem *QGraphicsLayoutItemPrivate::q_func()
    const': takes in Python what 'QGraphicsLayoutItem
    *QGraphicsLayoutItemPrivate::q_func()' takes.
  - Qt's 'QGraphicsLayoutItemPrivate::~QGraphicsLayoutItemPrivate()': the
    destructor: Python removes its C++ QGraphicsLayoutItemPrivate by it, and
    has no other use for it.
  - Qt's 'const QGraphicsLayoutItemPrivate
    *QGraphicsLayoutItemPrivate::get(const QGraphicsLayoutItem *q)': takes in
    Python what 'QGraphicsLayoutItemPrivate
    *QGraphicsLayoutItemPrivate::get(QGraphicsLayoutItem *q)' takes.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QGraphicsLayoutItemPrivate is created at the first use, not by
    'QGraphicsLayoutItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsLayoutItemPrivate back gives a copy the
    ritual made for Python, in a new cute QGraphicsLayoutItemPrivate.
  - Each name of Qt's QGraphicsLayoutItemPrivate that has no cute function
    yet, 'effectiveSizeHints', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphicsLayoutItemPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SizeComponent(CuteNum):
    """
    The enum 'QGraphicsLayoutItemPrivate::SizeComponent' of Qt, with the 2
    names Qt gives in it.
    """

    Width = Kee[int](0)
    Height = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def get(
      q: Optional[QGraphicsLayoutItem],
  ) -> Optional[QGraphicsLayoutItemPrivate]:
    """
    Calls Qt's 'QGraphicsLayoutItemPrivate
    *QGraphicsLayoutItemPrivate::get(QGraphicsLayoutItem *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#get

    Parameters
    ----------

    q : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsLayoutItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItemPrivate
    #      *QGraphicsLayoutItemPrivate::get(QGraphicsLayoutItem *q)
    address = Rituals.call(
        'ritual_ZN26QGraphicsLayoutItemPrivate3getEP19QGraphicsLayoutItem',
        CuteMixin._addressOf(q, 'QGraphicsLayoutItem'),
    )
    return QGraphicsLayoutItemPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLayoutItemPrivate'

  #  Qt's '~QGraphicsLayoutItemPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QGraphicsLayoutItemPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QGraphicsLayoutItemPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parentItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsLayoutItemPrivate::parentItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#parentItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsLayoutItemPrivate::parentItem() const
    address = self.uglySide.call(
        'ritual_ZNK26QGraphicsLayoutItemPrivate10parentItemEv',
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsLayoutItemPrivate::hasHeightForWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#hasHeightForWidth
    """
    #  bool QGraphicsLayoutItemPrivate::hasHeightForWidth() const
    return self.uglySide.call(
        'ritual_ZNK26QGraphicsLayoutItemPrivate17hasHeightForWidthEv',
    )

  def hasWidthForHeight(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsLayoutItemPrivate::hasWidthForHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#hasWidthForHeight
    """
    #  bool QGraphicsLayoutItemPrivate::hasWidthForHeight() const
    return self.uglySide.call(
        'ritual_ZNK26QGraphicsLayoutItemPrivate17hasWidthForHeightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.SizeHint, QSizeF)
  def setSize(self, which: Qt.SizeHint, size: QSizeF) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItemPrivate::setSize(Qt::SizeHint which,
    const QSizeF &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#setSize

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QGraphicsLayoutItemPrivate::setSize(Qt::SizeHint which, const
    #      QSizeF &size)
    self.uglySide.call(
        'ritual_ZN26QGraphicsLayoutItemPrivate7setSizeEN2Qt8SizeHintERK6QSi'
        'zeF',
        which.value, self._valueOf(size),
    )

  @overload(Qt.SizeHint, SizeComponent, float)
  def setSizeComponent(
      self,
      which: Qt.SizeHint,
      component: SizeComponent,
      value: float,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsLayoutItemPrivate::setSizeComponent(Qt::SizeHint which,
    SizeComponent component, qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#setSizeComponent

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    component : SizeComponent
      Passed on as its number.

    value : float
      Passed on as it is.
    """
    #  void QGraphicsLayoutItemPrivate::setSizeComponent(Qt::SizeHint which,
    #      SizeComponent component, qreal value)
    self.uglySide.call(
        'ritual_ZN26QGraphicsLayoutItemPrivate16setSizeComponentEN2Qt8SizeH'
        'intENS_13SizeComponentEd',
        which.value, component.value, value,
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

  @overload(QGraphicsLayoutItem, bool)
  @overload(NoneType, bool)
  def __init__(
      self,
      parent: Optional[QGraphicsLayoutItem],
      isLayout: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLayoutItemPrivate::QGraphicsLayoutItemPrivate(
    QGraphicsLayoutItem *parent, bool isLayout)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html

    Parameters
    ----------

    parent : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isLayout : bool
      Passed on as it is.
    """
    #  QGraphicsLayoutItemPrivate::QGraphicsLayoutItemPrivate(
    #      QGraphicsLayoutItem *parent, bool isLayout)
    self._noteCreation(QGraphicsLayoutItemPrivate, lambda: Rituals.call(
        'ritual_ZN26QGraphicsLayoutItemPrivateC1EP19QGraphicsLayoutItemb',
        self._addressOf(parent, 'QGraphicsLayoutItem'), isLayout,
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

  def q_func(self) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsLayoutItemPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsLayoutItemPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QGraphicsLayoutItemPrivate6q_funcEv',
    )
    from . import QGraphicsLayoutItem
    return QGraphicsLayoutItem._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItemPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html#init
    """
    #  void QGraphicsLayoutItemPrivate::init()
    self.uglySide.call('ritual_ZN26QGraphicsLayoutItemPrivate4initEv')

  def ensureUserSizeHints(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutItemPrivate::ensureUserSizeHints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutitemprivate.html
    """
    #  void QGraphicsLayoutItemPrivate::ensureUserSizeHints()
    self.uglySide.call(
        'ritual_ZN26QGraphicsLayoutItemPrivate19ensureUserSizeHintsEv',
    )

  @staticmethod
  def effectiveSizeHints(*__, **_) -> Never:
    """
    Qt's 'QSizeF *QGraphicsLayoutItemPrivate::effectiveSizeHints(const QSizeF
    &constraint) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'normalizeHints'.
    """
    raise NotImplementedError(
        "'QGraphicsLayoutItemPrivate.effectiveSizeHints' has no cute "
        "function yet. Qt's 'QSizeF "
        "*QGraphicsLayoutItemPrivate::effectiveSizeHints(const QSizeF "
        "&constraint) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'normalizeHints'.")
