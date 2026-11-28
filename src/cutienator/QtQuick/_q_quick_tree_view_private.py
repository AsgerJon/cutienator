"""
QQuickTreeViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktreeview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTreeViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickTableViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRect, QVariant
  from . import QQuickTreeView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickTreeView = WAIT['QQuickTreeView']
  QRect = WAIT['QRect']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTreeViewPrivate(QQuickTableViewPrivate):
  """
  The cute side of Qt's QQuickTreeViewPrivate: a plain Python object standing
  in front of one C++ QQuickTreeViewPrivate.

  It is built on the cute 'QQuickTableViewPrivate', as Qt's
  QQuickTreeViewPrivate is built on Qt's QQuickTableViewPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTreeViewPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'get', 'modelImpl',
  'setModelImpl', 'updateItemProperties', 'updateSelection'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTreeView *QQuickTreeViewPrivate::q_func() const': takes
    in Python what 'QQuickTreeView *QQuickTreeViewPrivate::q_func()' takes.
  - Qt's 'QQuickTreeViewPrivate::~QQuickTreeViewPrivate()': the destructor:
    Python never removes a C++ QQuickTreeViewPrivate.
  - Qt's 'void QQuickTreeViewPrivate::dataChangedCallback(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQuickTreeViewPrivate is created at the first use, not by
    'QQuickTreeViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTreeViewPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTreeView)
  @overload(NoneType)
  def get(q: Optional[QQuickTreeView]) -> Optional[QQuickTreeViewPrivate]:
    """
    Calls Qt's 'QQuickTreeViewPrivate
    *QQuickTreeViewPrivate::get(QQuickTreeView *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeviewprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickTreeView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTreeViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTreeViewPrivate *QQuickTreeViewPrivate::get(QQuickTreeView *q)
    address = Rituals.call(
        'ritual_ZN21QQuickTreeViewPrivate3getEP14QQuickTreeView',
        CuteMixin._addressOf(q),
    )
    return QQuickTreeViewPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTreeViewPrivate'

  #  A C++ QQuickTreeViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTreeViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def modelImpl(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTreeViewPrivate::modelImpl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewprivate.html#modelImpl

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTreeViewPrivate::modelImpl() const
    ritual = 'ritual_ZNK21QQuickTreeViewPrivate9modelImplEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickTreeViewPrivate9modelImplEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModelImpl(self, newModel: QVariant) -> None:
    """
    Calls Qt's 'void QQuickTreeViewPrivate::setModelImpl(const QVariant
    &newModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewprivate.html#setModelImpl

    Parameters
    ----------

    newModel : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickTreeViewPrivate::setModelImpl(const QVariant &newModel)
    ritual = 'ritual_ZN21QQuickTreeViewPrivate12setModelImplERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTreeViewPrivate12setModelImplERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(newModel))

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
    'QQuickTreeViewPrivate::QQuickTreeViewPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewprivate.html#QQuickTreeViewPrivate
    """
    #  QQuickTreeViewPrivate::QQuickTreeViewPrivate()
    self._noteCreation(QQuickTreeViewPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuickTreeViewPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickTreeView]:
    """
    Calls Qt's 'QQuickTreeView *QQuickTreeViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickTreeView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTreeView *QQuickTreeViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickTreeViewPrivate6q_funcEv')
    from . import QQuickTreeView
    return QQuickTreeView._cuteAt(address)

  @overload(int, QObject, bool)
  @overload(int, NoneType, bool)
  def updateItemProperties(
      self,
      flatIndex: int,
      object: Optional[QObject],
      init: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickTreeViewPrivate::updateItemProperties(int
    flatIndex, QObject *object, bool init)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewprivate.html#updateItemProperties

    Parameters
    ----------

    flatIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    init : bool
      Passed on as it is.
    """
    #  void QQuickTreeViewPrivate::updateItemProperties(int flatIndex,
    #      QObject *object, bool init)
    ritual = (
        'ritual_ZN21QQuickTreeViewPrivate20updateItemPropertiesEiP7QObjectb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTreeViewPrivate20updateItemPropertiesEiP7QO'
          'bjectb')
    self.uglySide.call(
        ritual, flatIndex, self._addressOf(object, 'QObject'), init,
    )

  @overload(QRect, QRect)
  def updateSelection(
      self,
      oldSelection: QRect,
      newSelection: QRect,
  ) -> None:
    """
    Calls Qt's 'void QQuickTreeViewPrivate::updateSelection(const QRect
    &oldSelection, const QRect &newSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeviewprivate.html#updateSelection

    Parameters
    ----------

    oldSelection : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    newSelection : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickTreeViewPrivate::updateSelection(const QRect &oldSelection,
    #      const QRect &newSelection)
    ritual = 'ritual_ZN21QQuickTreeViewPrivate15updateSelectionERK5QRectS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickTreeViewPrivate15updateSelectionERK5QRectS2'
          '_')
    self.uglySide.call(
        ritual, self._valueOf(oldSelection), self._valueOf(newSelection),
    )
