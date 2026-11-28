"""
QQuickItemChangeListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickItemChangeListener to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRectF
  from . import QQuickAnchorsPrivate, QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemChangeListener(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemChangeListener: a plain Python object
  standing in front of one C++ QQuickItemChangeListener.

  C++ hands a QQuickItemChangeListener around as a copy, so every C++
  QQuickItemChangeListener behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickItemChangeListener that has a ritual and that
  Python can call so far, 20 names in all: 'itemGeometryChanged',
  'itemSiblingOrderChanged', 'itemVisibilityChanged', 'itemEnabledChanged',
  'itemOpacityChanged', 'itemDestroyed', 'itemChildAdded',
  'itemChildRemoved', 'itemParentChanged', 'itemRotationChanged',
  'itemImplicitWidthChanged', 'itemImplicitHeightChanged',
  'itemFocusChanged', 'itemScaleChanged', 'itemTransformChanged',
  'anchorPrivate', 'baseDeleted', 'debugName', 'addSourceItem',
  'removeSourceItem'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickItemChangeListener::~QQuickItemChangeListener()': the
    destructor: Python removes its C++ QQuickItemChangeListener by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickItemChangeListener is created at the first use, not by
    'QQuickItemChangeListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickItemChangeListener back gives a copy the ritual
    made for Python, in a new cute QQuickItemChangeListener.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemChangeListener'

  #  A C++ QQuickItemChangeListener Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemChangeListener'

  #  The functions Qt calls itself that QQuickItemChangeListener is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickIte'
           'm20QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemSiblingOrderChanged': (
          ('_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuic'
           'kItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemVisibilityChanged': (
          ('_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickI'
           'tem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemEnabledChanged': (
          ('_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemOpacityChanged': (
          ('_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemChildAdded': (
          ('_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemChildRemoved': (
          ('_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1'
           '_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemParentChanged': (
          ('_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS'
           '1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemRotationChanged': (
          ('_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickIte'
           'm',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQui'
           'ckItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQu'
           'ickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemFocusChanged': (
          ('_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2'
           'Qt11FocusReasonE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('int', 'enum', 'QtCore:Qt.FocusReason'),
           )),
      ),
      'itemScaleChanged': (
          ('_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemTransformChanged': (
          ('_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickIt'
           'emS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'anchorPrivate': (
          ('_ZN24QQuickItemChangeListener13anchorPrivateEv',
           ('address', 'address', 'QtQuick:QQuickAnchorsPrivate'),
           ()),
      ),
      'baseDeleted': (
          ('_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'debugName': (
          ('_ZNK24QQuickItemChangeListener9debugNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'addSourceItem': (
          ('_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'removeSourceItem': (
          ('_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
  }

  #  Qt's '~QQuickItemChangeListener()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickItemChangeListener behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQuickItemChangeListenerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def baseDeleted(self, caller: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQuickItemChangeListener::baseDeleted(const QObject
    *caller) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#baseDeleted

    Parameters
    ----------

    caller : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
    #      const
    ritual = 'ritual_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject')
    return self._callAs(
        'QQuickItemChangeListener', ritual,
        self._addressOf(caller, 'QObject'),
    )

  def debugName(self) -> str:
    """
    Calls Qt's 'QString QQuickItemChangeListener::debugName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#debugName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemChangeListener::debugName() const
    ritual = 'ritual_ZNK24QQuickItemChangeListener9debugNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQuickItemChangeListener9debugNameEv'
    return self._callAs('QQuickItemChangeListener', ritual)

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

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemGeometryChanged(QQuickItem
    *a0, QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuick'
        'Item20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener19itemGeometryChangedEP10'
          'QQuickItem20QQuickGeometryChangeRK6QRectF')
    self._callAs(
        'QQuickItemChangeListener', ritual,
        self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQ'
        'uickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener23itemSiblingOrderChanged'
          'EP10QQuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener21itemVisibilityChangedEP'
          '10QQuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemEnabledChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemEnabledChanged(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemEnabledChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener18itemEnabledChangedEP10Q'
          'QuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemOpacityChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemOpacityChanged(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemOpacityChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener18itemOpacityChangedEP10Q'
          'QuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemDestroyed(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemDestroyed

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuick'
          'Item')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

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
    Calls Qt's 'void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemChildAdded

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
    #      QQuickItem *a1)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS'
        '1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuic'
          'kItemS1_')
    self._callAs(
        'QQuickItemChangeListener', ritual,
        self._addressOf(a0), self._addressOf(a1),
    )

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
    Calls Qt's 'void QQuickItemChangeListener::itemChildRemoved(QQuickItem
    *a0, QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemChildRemoved

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
    #      QQuickItem *a1)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickIte'
        'mS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQu'
          'ickItemS1_')
    self._callAs(
        'QQuickItemChangeListener', ritual,
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemParentChanged(QQuickItem
    *a0, QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemParentChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
    #      QQuickItem *a1)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickIt'
        'emS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener17itemParentChangedEP10QQ'
          'uickItemS1_')
    self._callAs(
        'QQuickItemChangeListener', ritual,
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemRotationChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemRotationChanged(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemRotationChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuick'
        'Item')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener19itemRotationChangedEP10'
          'QQuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem
    #      *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10Q'
        'QuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener24itemImplicitWidthChange'
          'dEP10QQuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem
    #      *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10'
        'QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener25itemImplicitHeightChang'
          'edEP10QQuickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem, Qt.FocusReason)
  @overload(NoneType, Qt.FocusReason)
  def itemFocusChanged(
      self,
      a0: Optional[QQuickItem],
      a1: Qt.FocusReason,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemFocusChanged(QQuickItem
    *a0, Qt::FocusReason a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemFocusChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
    #      Qt::FocusReason a1)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickIte'
        'mN2Qt11FocusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQu'
          'ickItemN2Qt11FocusReasonE')
    self._callAs(
        'QQuickItemChangeListener', ritual, self._addressOf(a0), a1.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemScaleChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::itemScaleChanged(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemScaleChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQu'
          'ickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemTransformChanged(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0, QQuickItem
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#itemTransformChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
    #      QQuickItem *a1)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuic'
        'kItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener20itemTransformChangedEP1'
          '0QQuickItemS1_')
    self._callAs(
        'QQuickItemChangeListener', ritual,
        self._addressOf(a0), self._addressOf(a1),
    )

  def anchorPrivate(self) -> Optional[QQuickAnchorsPrivate]:
    """
    Calls Qt's 'QQuickAnchorsPrivate
    *QQuickItemChangeListener::anchorPrivate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#anchorPrivate

    Returns
    -------

    Optional[QQuickAnchorsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
    ritual = 'ritual_ZN24QQuickItemChangeListener13anchorPrivateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickItemChangeListener13anchorPrivateEv'
    address = self._callAs('QQuickItemChangeListener', ritual)
    from . import QQuickAnchorsPrivate
    return QQuickAnchorsPrivate._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def addSourceItem(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::addSourceItem(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#addSourceItem

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener13addSourceItemEP10QQuick'
          'Item')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def removeSourceItem(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemChangeListener::removeSourceItem(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemchangelistener.html#removeSourceItem

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
    ritual = (
        'ritual_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickItemChangeListener16removeSourceItemEP10QQu'
          'ickItem')
    self._callAs('QQuickItemChangeListener', ritual, self._addressOf(a0))
