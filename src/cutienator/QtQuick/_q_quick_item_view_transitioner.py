"""
QQuickItemViewTransitioner binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickItemViewTransitioner to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQuickItemViewTransitionChangeListener
  from . import QQuickItemViewTransitionableItem, QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItemViewTransitionChangeListener = WAIT['QQuickItemViewTransitionChangeListener']
  QQuickItemViewTransitionableItem = WAIT['QQuickItemViewTransitionableItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemViewTransitioner(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemViewTransitioner: a plain Python object
  standing in front of one C++ QQuickItemViewTransitioner.

  C++ hands a QQuickItemViewTransitioner around as a copy, so every C++
  QQuickItemViewTransitioner behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickItemViewTransitioner that has a ritual and
  that Python can call so far, 9 names in all: 'canTransition',
  'transitionNextReposition', 'addToTargetLists', 'resetTargetLists',
  'transitionObject', 'targetItems', 'setPopulateTransitionEnabled',
  'populateTransitionEnabled', 'setChangeListener'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickItemViewTransitioner::~QQuickItemViewTransitioner()': the
    destructor: Python removes its C++ QQuickItemViewTransitioner by it, and
    has no other use for it.
  - Qt's 'const QList<int>
    &QQuickItemViewTransitioner::targetIndexes(QQuickItemViewTransitioner::
    TransitionType type) const': gives a type Python has no way to take yet.
  - Qt's 'void QQuickItemViewTransitioner::finishedTransition(
    QQuickItemViewTransitionJob *job, QQuickItemViewTransitionableItem
    *item)': names 'QQuickItemViewTransitionJob', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQuickItemViewTransitioner is created at the first use, not by
    'QQuickItemViewTransitioner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickItemViewTransitioner back gives a copy the
    ritual made for Python, in a new cute QQuickItemViewTransitioner.
  - Each name of Qt's QQuickItemViewTransitioner that has no cute function
    yet, 'finishedTransition', 'targetIndexes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickItemViewTransitioner, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class TransitionType(CuteNum):
    """
    The enum 'QQuickItemViewTransitioner::TransitionType' of Qt, with the 5
    names Qt gives in it.
    """

    NoTransition = Kee[int](0)
    PopulateTransition = Kee[int](1)
    AddTransition = Kee[int](2)
    MoveTransition = Kee[int](3)
    RemoveTransition = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewTransitioner'

  #  Qt's '~QQuickItemViewTransitioner()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickItemViewTransitioner behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuickItemViewTransitionerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TransitionType, bool)
  def canTransition(self, type: TransitionType, asTarget: bool) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewTransitioner::canTransition(QQuickItemViewTransitioner::
    TransitionType type, bool asTarget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html#canTransition

    Parameters
    ----------

    type : TransitionType
      Passed on as its number.

    asTarget : bool
      Passed on as it is.
    """
    #  bool QQuickItemViewTransitioner::canTransition(
    #      QQuickItemViewTransitioner::TransitionType type, bool asTarget)
    #      const
    return self.uglySide.call(
        'ritual_ZNK26QQuickItemViewTransitioner13canTransitionENS_14Transit'
        'ionTypeEb',
        type.value, asTarget,
    )

  @overload(TransitionType, bool)
  def transitionObject(
      self,
      type: TransitionType,
      asTarget: bool,
  ) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition
    *QQuickItemViewTransitioner::transitionObject(
    QQuickItemViewTransitioner::TransitionType type, bool asTarget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html#transitionObject

    Parameters
    ----------

    type : TransitionType
      Passed on as its number.

    asTarget : bool
      Passed on as it is.

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickItemViewTransitioner::transitionObject(
    #      QQuickItemViewTransitioner::TransitionType type, bool asTarget)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickItemViewTransitioner16transitionObjectENS_14Tran'
        'sitionTypeEb',
        type.value, asTarget,
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  @overload(TransitionType)
  def targetItems(self, type: TransitionType) -> QList[QObject]:
    """
    Calls Qt's 'const QList<QObject *>
    &QQuickItemViewTransitioner::targetItems(QQuickItemViewTransitioner::
    TransitionType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html#targetItems

    Parameters
    ----------

    type : TransitionType
      Passed on as its number.

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QObject *> &QQuickItemViewTransitioner::targetItems(
    #      QQuickItemViewTransitioner::TransitionType type) const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickItemViewTransitioner11targetItemsENS_14Transitio'
        'nTypeE',
        type.value,
    )
    from ..QtCore import QObject
    return QList[QObject]._cuteOwning(address)

  def populateTransitionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewTransitioner::populateTransitionEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html
    """
    #  bool QQuickItemViewTransitioner::populateTransitionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickItemViewTransitioner25populateTransitionEnabledE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPopulateTransitionEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewTransitioner::setPopulateTransitionEnabled(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQuickItemViewTransitioner::setPopulateTransitionEnabled(bool b)
    self.uglySide.call(
        'ritual_ZN26QQuickItemViewTransitioner28setPopulateTransitionEnable'
        'dEb',
        b,
    )

  @overload(QQuickItemViewTransitionChangeListener)
  @overload(NoneType)
  def setChangeListener(
      self,
      obj: Optional[QQuickItemViewTransitionChangeListener],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitioner::setChangeListener(
    QQuickItemViewTransitionChangeListener *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html#setChangeListener

    Parameters
    ----------

    obj : Optional[QQuickItemViewTransitionChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewTransitioner::setChangeListener(
    #      QQuickItemViewTransitionChangeListener *obj)
    self.uglySide.call(
        'ritual_ZN26QQuickItemViewTransitioner17setChangeListenerEP38QQuick'
        'ItemViewTransitionChangeListener',
        self._addressOf(obj, 'QQuickItemViewTransitionChangeListener'),
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
    'QQuickItemViewTransitioner::QQuickItemViewTransitioner()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html
    """
    #  QQuickItemViewTransitioner::QQuickItemViewTransitioner()
    self._noteCreation(QQuickItemViewTransitioner, lambda: Rituals.call(
        'ritual_ZN26QQuickItemViewTransitionerC1Ev',
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

  @overload(QQuickItemViewTransitionableItem, TransitionType, bool)
  @overload(NoneType, TransitionType, bool)
  def transitionNextReposition(
      self,
      item: Optional[QQuickItemViewTransitionableItem],
      type: TransitionType,
      isTarget: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitioner::transitionNextReposition(
    QQuickItemViewTransitionableItem *item,
    QQuickItemViewTransitioner::TransitionType type, bool isTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html

    Parameters
    ----------

    item : Optional[QQuickItemViewTransitionableItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : TransitionType
      Passed on as its number.

    isTarget : bool
      Passed on as it is.
    """
    #  void QQuickItemViewTransitioner::transitionNextReposition(
    #      QQuickItemViewTransitionableItem *item,
    #      QQuickItemViewTransitioner::TransitionType type, bool isTarget)
    self.uglySide.call(
        'ritual_ZN26QQuickItemViewTransitioner24transitionNextRepositionEP3'
        '2QQuickItemViewTransitionableItemNS_14TransitionTypeEb',
        self._addressOf(item), type.value, isTarget,
    )

  @overload(TransitionType, QQuickItemViewTransitionableItem, int)
  @overload(TransitionType, NoneType, int)
  def addToTargetLists(
      self,
      type: TransitionType,
      item: Optional[QQuickItemViewTransitionableItem],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitioner::addToTargetLists(
    QQuickItemViewTransitioner::TransitionType type,
    QQuickItemViewTransitionableItem *item, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html#addToTargetLists

    Parameters
    ----------

    type : TransitionType
      Passed on as its number.

    item : Optional[QQuickItemViewTransitionableItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QQuickItemViewTransitioner::addToTargetLists(
    #      QQuickItemViewTransitioner::TransitionType type,
    #      QQuickItemViewTransitionableItem *item, int index)
    self.uglySide.call(
        'ritual_ZN26QQuickItemViewTransitioner16addToTargetListsENS_14Trans'
        'itionTypeEP32QQuickItemViewTransitionableItemi',
        type.value, self._addressOf(item), index,
    )

  def resetTargetLists(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewTransitioner::resetTargetLists()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitioner.html#resetTargetLists
    """
    #  void QQuickItemViewTransitioner::resetTargetLists()
    self.uglySide.call(
        'ritual_ZN26QQuickItemViewTransitioner16resetTargetListsEv',
    )

  @staticmethod
  def finishedTransition(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewTransitioner::finishedTransition(
    QQuickItemViewTransitionJob *job, QQuickItemViewTransitionableItem
    *item)': names 'QQuickItemViewTransitionJob', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewTransitioner.finishedTransition' has no cute "
        "function yet. Qt's 'void "
        "QQuickItemViewTransitioner::finishedTransition(QQuickItemViewTransi"
        "tionJob *job, QQuickItemViewTransitionableItem *item)': names "
        "'QQuickItemViewTransitionJob', which has no cute class yet.")

  @staticmethod
  def targetIndexes(*__, **_) -> Never:
    """
    Qt's 'const QList<int>
    &QQuickItemViewTransitioner::targetIndexes(QQuickItemViewTransitioner::
    TransitionType type) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewTransitioner.targetIndexes' has no cute function "
        "yet. Qt's 'const QList<int> "
        "&QQuickItemViewTransitioner::targetIndexes(QQuickItemViewTransition"
        "er::TransitionType type) const': gives a type Python has no way to "
        "take yet.")
