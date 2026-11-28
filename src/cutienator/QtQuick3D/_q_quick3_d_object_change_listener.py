"""
QQuick3DObjectChangeListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobjectchangelistener_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DObjectChangeListener to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DObject = WAIT['QQuick3DObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DObjectChangeListener(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DObjectChangeListener: a plain Python object
  standing in front of one C++ QQuick3DObjectChangeListener.

  C++ hands a QQuick3DObjectChangeListener around as a copy, so every C++
  QQuick3DObjectChangeListener behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuick3DObjectChangeListener that has a ritual and
  that Python can call so far, 8 names in all: 'itemSiblingOrderChanged',
  'itemVisibilityChanged', 'itemEnabledChanged', 'itemOpacityChanged',
  'itemDestroyed', 'itemChildAdded', 'itemChildRemoved', 'itemParentChanged'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DObjectChangeListener::~QQuick3DObjectChangeListener()': the
    destructor: Python removes its C++ QQuick3DObjectChangeListener by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QQuick3DObjectChangeListener is created at the first use, not by
    'QQuick3DObjectChangeListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DObjectChangeListener back gives a copy the
    ritual made for Python, in a new cute QQuick3DObjectChangeListener.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DObjectChangeListener'

  #  A C++ QQuick3DObjectChangeListener Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DObjectChangeListener'

  #  The functions Qt calls itself that QQuick3DObjectChangeListener is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemSiblingOrderChanged': (
          ('_ZN28QQuick3DObjectChangeListener23itemSiblingOrderChangedEP14Q'
           'Quick3DObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemVisibilityChanged': (
          ('_ZN28QQuick3DObjectChangeListener21itemVisibilityChangedEP14QQu'
           'ick3DObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemEnabledChanged': (
          ('_ZN28QQuick3DObjectChangeListener18itemEnabledChangedEP14QQuick'
           '3DObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemOpacityChanged': (
          ('_ZN28QQuick3DObjectChangeListener18itemOpacityChangedEP14QQuick'
           '3DObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN28QQuick3DObjectChangeListener13itemDestroyedEP14QQuick3DObj'
           'ect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemChildAdded': (
          ('_ZN28QQuick3DObjectChangeListener14itemChildAddedEP14QQuick3DOb'
           'jectS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemChildRemoved': (
          ('_ZN28QQuick3DObjectChangeListener16itemChildRemovedEP14QQuick3D'
           'ObjectS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
      'itemParentChanged': (
          ('_ZN28QQuick3DObjectChangeListener17itemParentChangedEP14QQuick3'
           'DObjectS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
               ('address', 'address', 'QtQuick3D:QQuick3DObject'),
           )),
      ),
  }

  #  Qt's '~QQuick3DObjectChangeListener()'. Naming it makes this a value
  #  class: Python owns every C++ QQuick3DObjectChangeListener behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QQuick3DObjectChangeListenerD1Ev'

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

  @overload(QQuick3DObject)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemSiblingOrderChanged(QQuick3DObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemSiblingOrderChanged(
    #      QQuick3DObject *a0)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener23itemSiblingOrderChangedEP'
        '14QQuick3DObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener23itemSiblingOrderCha'
          'ngedEP14QQuick3DObject')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuick3DObject)
  @overload(NoneType)
  def itemVisibilityChanged(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemVisibilityChanged(QQuick3DObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuick3DObjectChangeListener::itemVisibilityChanged(QQuick3DObject
    #      *a0)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener21itemVisibilityChangedEP14'
        'QQuick3DObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener21itemVisibilityChang'
          'edEP14QQuick3DObject')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuick3DObject)
  @overload(NoneType)
  def itemEnabledChanged(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemEnabledChanged(QQuick3DObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemEnabledChanged(QQuick3DObject
    #      *a0)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener18itemEnabledChangedEP14QQu'
        'ick3DObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener18itemEnabledChangedE'
          'P14QQuick3DObject')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuick3DObject)
  @overload(NoneType)
  def itemOpacityChanged(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemOpacityChanged(QQuick3DObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemOpacityChanged(QQuick3DObject
    #      *a0)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener18itemOpacityChangedEP14QQu'
        'ick3DObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener18itemOpacityChangedE'
          'P14QQuick3DObject')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuick3DObject)
  @overload(NoneType)
  def itemDestroyed(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemDestroyed(QQuick3DObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html#itemDestroyed

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemDestroyed(QQuick3DObject *a0)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener13itemDestroyedEP14QQuick3D'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener13itemDestroyedEP14QQ'
          'uick3DObject')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuick3DObject, QQuick3DObject)
  @overload(QQuick3DObject, NoneType)
  @overload(NoneType, QQuick3DObject)
  @overload(NoneType, NoneType)
  def itemChildAdded(
      self,
      a0: Optional[QQuick3DObject],
      a1: Optional[QQuick3DObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemChildAdded(QQuick3DObject *a0,
    QQuick3DObject *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html#itemChildAdded

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemChildAdded(QQuick3DObject *a0,
    #      QQuick3DObject *a1)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener14itemChildAddedEP14QQuick3'
        'DObjectS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener14itemChildAddedEP14Q'
          'Quick3DObjectS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuick3DObject, QQuick3DObject)
  @overload(QQuick3DObject, NoneType)
  @overload(NoneType, QQuick3DObject)
  @overload(NoneType, NoneType)
  def itemChildRemoved(
      self,
      a0: Optional[QQuick3DObject],
      a1: Optional[QQuick3DObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemChildRemoved(QQuick3DObject *a0,
    QQuick3DObject *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html#itemChildRemoved

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemChildRemoved(QQuick3DObject
    #      *a0, QQuick3DObject *a1)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener16itemChildRemovedEP14QQuic'
        'k3DObjectS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener16itemChildRemovedEP1'
          '4QQuick3DObjectS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuick3DObject, QQuick3DObject)
  @overload(QQuick3DObject, NoneType)
  @overload(NoneType, QQuick3DObject)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      a0: Optional[QQuick3DObject],
      a1: Optional[QQuick3DObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectChangeListener::itemParentChanged(QQuick3DObject *a0,
    QQuick3DObject *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectchangelistener.html

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectChangeListener::itemParentChanged(QQuick3DObject
    #      *a0, QQuick3DObject *a1)
    ritual = (
        'ritual_ZN28QQuick3DObjectChangeListener17itemParentChangedEP14QQui'
        'ck3DObjectS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuick3DObjectChangeListener17itemParentChangedEP'
          '14QQuick3DObjectS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))
