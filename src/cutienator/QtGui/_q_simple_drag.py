"""
QSimpleDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qsimpledrag_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSimpleDrag to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QBasicDrag

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QSimpleDrag(QBasicDrag):
  """
  The cute side of Qt's QSimpleDrag: a plain Python object standing in front
  of one C++ QSimpleDrag.

  It is built on the cute 'QBasicDrag', as Qt's QSimpleDrag is built on Qt's
  QBasicDrag, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSimpleDrag that has a ritual and that Python can
  call so far, 4 names in all: 'startDrag', 'cancel', 'move', 'drop'. It can
  be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSimpleDrag is created at the first use, not by
    'QSimpleDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSimpleDrag.
  - Qt tells when it has removed the C++ QSimpleDrag. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSimpleDrag'

  #  A C++ QSimpleDrag Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSimpleDrag'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSimpleDrag::QSimpleDrag()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsimpledrag.html#QSimpleDrag
    """
    #  QSimpleDrag::QSimpleDrag()
    self._noteCreation(QSimpleDrag, lambda: Rituals.call(
        'ritual_ZN11QSimpleDragC1Ev',
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

  def startDrag(self) -> None:
    """
    Calls Qt's 'void QSimpleDrag::startDrag()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpledrag.html#startDrag
    """
    #  void QSimpleDrag::startDrag()
    ritual = 'ritual_ZN11QSimpleDrag9startDragEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSimpleDrag9startDragEv'
    self.uglySide.call(ritual)

  def cancel(self) -> None:
    """
    Calls Qt's 'void QSimpleDrag::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpledrag.html#cancel
    """
    #  void QSimpleDrag::cancel()
    ritual = 'ritual_ZN11QSimpleDrag6cancelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QSimpleDrag6cancelEv'
    self.uglySide.call(ritual)

  @overload(QPoint, Qt.MouseButtons, Qt.KeyboardModifiers)
  def move(
      self,
      globalPos: QPoint,
      b: Qt.MouseButtons,
      mods: Qt.KeyboardModifiers,
  ) -> None:
    """
    Calls Qt's 'void QSimpleDrag::move(const QPoint &globalPos,
    Qt::MouseButtons b, Qt::KeyboardModifiers mods)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpledrag.html#move

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    b : Qt.MouseButtons
      Passed on as its number.

    mods : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QSimpleDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
    #      Qt::KeyboardModifiers mods)
    ritual = (
        'ritual_ZN11QSimpleDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3'
        '_INS4_16KeyboardModifierEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSimpleDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButt'
          'onEES3_INS4_16KeyboardModifierEE')
    self.uglySide.call(ritual, self._valueOf(globalPos), b.value, mods.value)

  @overload(QPoint, Qt.MouseButtons, Qt.KeyboardModifiers)
  def drop(
      self,
      globalPos: QPoint,
      b: Qt.MouseButtons,
      mods: Qt.KeyboardModifiers,
  ) -> None:
    """
    Calls Qt's 'void QSimpleDrag::drop(const QPoint &globalPos,
    Qt::MouseButtons b, Qt::KeyboardModifiers mods)'.

    Qt's own words: https://doc.qt.io/qt-6/qsimpledrag.html#drop

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    b : Qt.MouseButtons
      Passed on as its number.

    mods : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QSimpleDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
    #      Qt::KeyboardModifiers mods)
    ritual = (
        'ritual_ZN11QSimpleDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3'
        '_INS4_16KeyboardModifierEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QSimpleDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButt'
          'onEES3_INS4_16KeyboardModifierEE')
    self.uglySide.call(ritual, self._valueOf(globalPos), b.value, mods.value)
