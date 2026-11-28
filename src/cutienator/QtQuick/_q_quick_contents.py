"""
QQuickContents binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickContents to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from . import QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContents(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickContents: a plain Python object standing in
  front of one C++ QQuickContents.

  What exists
  -----------

  Every function of Qt's QQuickContents that has a ritual and that Python can
  call so far, 10 names in all: 'rectF', 'calcGeometry', 'complete',
  'itemGeometryChanged', 'itemDestroyed', 'itemChildAdded',
  'itemChildRemoved', 'calcHeight', 'calcWidth', 'updateRect'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickContents::~QQuickContents()': the destructor: Python never
    removes a C++ QQuickContents.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickContents is created at the first use, not by
    'QQuickContents(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContents.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContents'

  #  A C++ QQuickContents Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContents'

  #  The functions Qt calls itself that QQuickContents is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN14QQuickContents19itemGeometryChangedEP10QQuickItem20QQuickG'
           'eometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN14QQuickContents13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemChildAdded': (
          ('_ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemChildRemoved': (
          ('_ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
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

  def rectF(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickContents::rectF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#rectF

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickContents::rectF() const
    address = self.uglySide.call('ritual_ZNK14QQuickContents5rectFEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's 'QQuickContents::QQuickContents(QQuickItem
    *item)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#QQuickContents

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickContents::QQuickContents(QQuickItem *item)
    self._noteCreation(QQuickContents, lambda: Rituals.call(
        'ritual_ZN14QQuickContentsC1EP10QQuickItem', self._addressOf(item),
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def calcGeometry(self, changed: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickContents::calcGeometry(QQuickItem *changed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#calcGeometry

    Parameters
    ----------

    changed : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickContents::calcGeometry(QQuickItem *changed)
    self.uglySide.call(
        'ritual_ZN14QQuickContents12calcGeometryEP10QQuickItem',
        self._addressOf(changed),
    )

  def complete(self) -> None:
    """
    Calls Qt's 'void QQuickContents::complete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#complete
    """
    #  void QQuickContents::complete()
    self.uglySide.call('ritual_ZN14QQuickContents8completeEv')

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickContents::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontents.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickContents::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &a2)
    ritual = (
        'ritual_ZN14QQuickContents19itemGeometryChangedEP10QQuickItem20QQui'
        'ckGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickContents19itemGeometryChangedEP10QQuickItem'
          '20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(a2),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickContents::itemDestroyed(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContents::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN14QQuickContents13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickContents13itemDestroyedEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildAdded(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickContents::itemChildAdded(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#itemChildAdded

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContents::itemChildAdded(QQuickItem *a0, QQuickItem *a1)
    ritual = 'ritual_ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickContents14itemChildAddedEP10QQuickItemS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemChildRemoved(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickContents::itemChildRemoved(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontents.html#itemChildRemoved

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContents::itemChildRemoved(QQuickItem *a0, QQuickItem *a1)
    ritual = 'ritual_ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickContents16itemChildRemovedEP10QQuickItemS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def calcHeight(self, changed: Optional[QQuickItem] = None) -> bool:
    """
    Calls Qt's 'bool QQuickContents::calcHeight(QQuickItem *changed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#calcHeight

    Parameters
    ----------

    changed : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQuickContents::calcHeight(QQuickItem *changed)
    return self.uglySide.call(
        'ritual_ZN14QQuickContents10calcHeightEP10QQuickItem',
        self._addressOf(changed),
    )

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def calcWidth(self, changed: Optional[QQuickItem] = None) -> bool:
    """
    Calls Qt's 'bool QQuickContents::calcWidth(QQuickItem *changed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#calcWidth

    Parameters
    ----------

    changed : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQuickContents::calcWidth(QQuickItem *changed)
    return self.uglySide.call(
        'ritual_ZN14QQuickContents9calcWidthEP10QQuickItem',
        self._addressOf(changed),
    )

  def updateRect(self) -> None:
    """
    Calls Qt's 'void QQuickContents::updateRect()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontents.html#updateRect
    """
    #  void QQuickContents::updateRect()
    self.uglySide.call('ritual_ZN14QQuickContents10updateRectEv')
