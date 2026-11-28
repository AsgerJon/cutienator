"""
QTreeWidgetItemIteratorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtreewidgetitemiterator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTreeWidgetItemIteratorPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTreeModel, QTreeWidgetItem, QTreeWidgetItemIterator
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTreeModel = WAIT['QTreeModel']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']
  QTreeWidgetItemIterator = WAIT['QTreeWidgetItemIterator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeWidgetItemIteratorPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTreeWidgetItemIteratorPrivate: a plain Python object
  standing in front of one C++ QTreeWidgetItemIteratorPrivate.

  C++ hands a QTreeWidgetItemIteratorPrivate around as a copy, so every C++
  QTreeWidgetItemIteratorPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QTreeWidgetItemIteratorPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'q_func', 'nextSibling',
  'ensureValidIterator', 'next', 'previous'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTreeWidgetItemIterator
    *QTreeWidgetItemIteratorPrivate::q_func() const': takes in Python what
    'QTreeWidgetItemIterator *QTreeWidgetItemIteratorPrivate::q_func()'
    takes.
  - Qt's 'QTreeWidgetItemIteratorPrivate
    &QTreeWidgetItemIteratorPrivate::operator=(const
    QTreeWidgetItemIteratorPrivate &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'QTreeWidgetItemIteratorPrivate::~QTreeWidgetItemIteratorPrivate()':
    the destructor: Python removes its C++ QTreeWidgetItemIteratorPrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTreeWidgetItemIteratorPrivate is created at the first use, not
    by 'QTreeWidgetItemIteratorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTreeWidgetItemIteratorPrivate back gives a copy the
    ritual made for Python, in a new cute QTreeWidgetItemIteratorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidgetItemIteratorPrivate'

  #  Qt's '~QTreeWidgetItemIteratorPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QTreeWidgetItemIteratorPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QTreeWidgetItemIteratorPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def nextSibling(
      self,
      item: Optional[QTreeWidgetItem],
  ) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem
    *QTreeWidgetItemIteratorPrivate::nextSibling(const QTreeWidgetItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html#nextSibling

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::nextSibling(const
    #      QTreeWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK30QTreeWidgetItemIteratorPrivate11nextSiblingEPK15QTreeW'
        'idgetItem',
        self._addressOf(item),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

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

  @overload(QTreeWidgetItemIterator, QTreeModel)
  @overload(QTreeWidgetItemIterator, NoneType)
  @overload(NoneType, QTreeModel)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QTreeWidgetItemIterator],
      model: Optional[QTreeModel],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItemIteratorPrivate::QTreeWidgetItemIteratorPrivate(
    QTreeWidgetItemIterator *q, QTreeModel *model)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html

    Parameters
    ----------

    q : Optional[QTreeWidgetItemIterator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QTreeModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTreeWidgetItemIteratorPrivate::QTreeWidgetItemIteratorPrivate(
    #      QTreeWidgetItemIterator *q, QTreeModel *model)
    self._noteCreation(QTreeWidgetItemIteratorPrivate, lambda: Rituals.call(
        'ritual_ZN30QTreeWidgetItemIteratorPrivateC1EP23QTreeWidgetItemIter'
        'atorP10QTreeModel',
        self._addressOf(q), self._addressOf(model),
    ))

  @overload(THIS)
  def __init__(self, other: QTreeWidgetItemIteratorPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QTreeWidgetItemIteratorPrivate::QTreeWidgetItemIteratorPrivate(const
    QTreeWidgetItemIteratorPrivate &other)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html

    Parameters
    ----------

    other : QTreeWidgetItemIteratorPrivate
      Passed on as a value: Qt reads the C++ QTreeWidgetItemIteratorPrivate,
      which stays Python's own.
    """
    #  QTreeWidgetItemIteratorPrivate::QTreeWidgetItemIteratorPrivate(const
    #      QTreeWidgetItemIteratorPrivate &other)
    self._noteCreation(QTreeWidgetItemIteratorPrivate, lambda: Rituals.call(
        'ritual_ZN30QTreeWidgetItemIteratorPrivateC1ERKS_',
        self._valueOf(other),
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

  def q_func(self) -> Optional[QTreeWidgetItemIterator]:
    """
    Calls Qt's 'QTreeWidgetItemIterator
    *QTreeWidgetItemIteratorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html#q_func

    Returns
    -------

    Optional[QTreeWidgetItemIterator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItemIterator *QTreeWidgetItemIteratorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QTreeWidgetItemIteratorPrivate6q_funcEv',
    )
    from . import QTreeWidgetItemIterator
    return QTreeWidgetItemIterator._cuteAt(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def ensureValidIterator(
      self,
      itemToBeRemoved: Optional[QTreeWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void
    QTreeWidgetItemIteratorPrivate::ensureValidIterator(const QTreeWidgetItem
    *itemToBeRemoved)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html

    Parameters
    ----------

    itemToBeRemoved : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidgetItemIteratorPrivate::ensureValidIterator(const
    #      QTreeWidgetItem *itemToBeRemoved)
    self.uglySide.call(
        'ritual_ZN30QTreeWidgetItemIteratorPrivate19ensureValidIteratorEPK1'
        '5QTreeWidgetItem',
        self._addressOf(itemToBeRemoved),
    )

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def next(
      self,
      current: Optional[QTreeWidgetItem],
  ) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::next(const
    QTreeWidgetItem *current)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html#next

    Parameters
    ----------

    current : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::next(const
    #      QTreeWidgetItem *current)
    address = self.uglySide.call(
        'ritual_ZN30QTreeWidgetItemIteratorPrivate4nextEPK15QTreeWidgetItem',
        self._addressOf(current),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def previous(
      self,
      current: Optional[QTreeWidgetItem],
  ) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem
    *QTreeWidgetItemIteratorPrivate::previous(const QTreeWidgetItem
    *current)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidgetitemiteratorprivate.html#previous

    Parameters
    ----------

    current : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidgetItemIteratorPrivate::previous(const
    #      QTreeWidgetItem *current)
    address = self.uglySide.call(
        'ritual_ZN30QTreeWidgetItemIteratorPrivate8previousEPK15QTreeWidget'
        'Item',
        self._addressOf(current),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)
