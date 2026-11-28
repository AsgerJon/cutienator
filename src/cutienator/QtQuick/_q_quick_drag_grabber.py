"""
QQuickDragGrabber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDragGrabber to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDragGrabber(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDragGrabber: a plain Python object standing in
  front of one C++ QQuickDragGrabber.

  C++ hands a QQuickDragGrabber around as a copy, so every C++
  QQuickDragGrabber behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickDragGrabber that has a ritual and that Python
  can call so far, 5 names in all: 'target', 'setTarget', 'resetTarget',
  'isEmpty', 'grab'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickDragGrabber::~QQuickDragGrabber()': the destructor: Python
    removes its C++ QQuickDragGrabber by it, and has no other use for it.
  - Qt's 'iterator QQuickDragGrabber::begin()': gives a type Python has no
    way to take yet.
  - Qt's 'iterator QQuickDragGrabber::end()': gives a type Python has no way
    to take yet.
  - Qt's 'iterator QQuickDragGrabber::release(iterator at)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QVarLengthArray<QQuickItem *, 4> &QQuickDragGrabber::ignoreList()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QQuickDragGrabber is created at the first use, not by
    'QQuickDragGrabber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDragGrabber back gives a copy the ritual made
    for Python, in a new cute QQuickDragGrabber.
  - Each name of Qt's QQuickDragGrabber that has no cute function yet,
    'begin', 'end', 'ignoreList', 'release', holds a function that raises
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
  __qt_class__ = 'QQuickDragGrabber'

  #  Qt's '~QQuickDragGrabber()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickDragGrabber behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QQuickDragGrabberD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickDragGrabber::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraggrabber.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDragGrabber::target() const
    address = self.uglySide.call('ritual_ZNK17QQuickDragGrabber6targetEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickDragGrabber::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraggrabber.html#isEmpty
    """
    #  bool QQuickDragGrabber::isEmpty() const
    return self.uglySide.call('ritual_ZNK17QQuickDragGrabber7isEmptyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setTarget(self, target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickDragGrabber::setTarget(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraggrabber.html#setTarget

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragGrabber::setTarget(QObject *target)
    self.uglySide.call(
        'ritual_ZN17QQuickDragGrabber9setTargetEP7QObject',
        self._addressOf(target, 'QObject'),
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
    Notes what was given, for Qt's 'QQuickDragGrabber::QQuickDragGrabber()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdraggrabber.html#QQuickDragGrabber
    """
    #  QQuickDragGrabber::QQuickDragGrabber()
    self._noteCreation(QQuickDragGrabber, lambda: Rituals.call(
        'ritual_ZN17QQuickDragGrabberC1Ev',
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

  def resetTarget(self) -> None:
    """
    Calls Qt's 'void QQuickDragGrabber::resetTarget()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraggrabber.html#resetTarget
    """
    #  void QQuickDragGrabber::resetTarget()
    self.uglySide.call('ritual_ZN17QQuickDragGrabber11resetTargetEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def grab(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDragGrabber::grab(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdraggrabber.html#grab

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragGrabber::grab(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN17QQuickDragGrabber4grabEP10QQuickItem',
        self._addressOf(item),
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'iterator QQuickDragGrabber::begin()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuickDragGrabber.begin' has no cute function yet. Qt's 'iterator "
        "QQuickDragGrabber::begin()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'iterator QQuickDragGrabber::end()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuickDragGrabber.end' has no cute function yet. Qt's 'iterator "
        "QQuickDragGrabber::end()': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def ignoreList(*__, **_) -> Never:
    """
    Qt's 'QVarLengthArray<QQuickItem *, 4> &QQuickDragGrabber::ignoreList()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickDragGrabber.ignoreList' has no cute function yet. Qt's "
        "'QVarLengthArray<QQuickItem *, 4> "
        "&QQuickDragGrabber::ignoreList()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'iterator QQuickDragGrabber::release(iterator at)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickDragGrabber.release' has no cute function yet. Qt's "
        "'iterator QQuickDragGrabber::release(iterator at)': takes a type "
        "Python has no way to hand over yet.")
