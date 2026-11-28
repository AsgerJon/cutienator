"""
QQuickContext2DTile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtile_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickContext2DTile to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from ..QtGui import QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']


class QQuickContext2DTile(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickContext2DTile: a plain Python object standing
  in front of one C++ QQuickContext2DTile.

  What exists
  -----------

  Every function of Qt's QQuickContext2DTile that has a ritual and that
  Python can call so far, 7 names in all: 'dirty', 'markDirty', 'rect',
  'setRect', 'createPainter', 'drawFinished', 'aboutToDraw'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickContext2DTile::~QQuickContext2DTile()': the destructor:
    Python never removes a C++ QQuickContext2DTile.

  What to expect
  --------------

  - The C++ QQuickContext2DTile is created at the first use, not by
    'QQuickContext2DTile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContext2DTile.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContext2DTile'

  #  A C++ QQuickContext2DTile Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContext2DTile'

  #  The functions Qt calls itself that QQuickContext2DTile is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRect': (
          ('_ZN19QQuickContext2DTile7setRectERK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'createPainter': (
          ('_ZN19QQuickContext2DTile13createPainterEbb',
           ('address', 'address', 'QtGui:QPainter'),
           (
               ('bool', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'drawFinished': (
          ('_ZN19QQuickContext2DTile12drawFinishedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'aboutToDraw': (
          ('_ZN19QQuickContext2DTile11aboutToDrawEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dirty(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2DTile::dirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2dtile.html#dirty
    """
    #  bool QQuickContext2DTile::dirty() const
    return self.uglySide.call('ritual_ZNK19QQuickContext2DTile5dirtyEv')

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QQuickContext2DTile::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2dtile.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickContext2DTile::rect() const
    address = self.uglySide.call('ritual_ZNK19QQuickContext2DTile4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setRect(self, r: QRect) -> None:
    """
    Calls Qt's 'void QQuickContext2DTile::setRect(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2dtile.html#setRect

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickContext2DTile::setRect(const QRect &r)
    self.uglySide.call(
        'ritual_ZN19QQuickContext2DTile7setRectERK5QRect', self._valueOf(r),
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
    'QQuickContext2DTile::QQuickContext2DTile()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtile.html#QQuickContext2DTile
    """
    #  QQuickContext2DTile::QQuickContext2DTile()
    self._noteCreation(QQuickContext2DTile, lambda: Rituals.call(
        'ritual_ZN19QQuickContext2DTileC1Ev',
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

  @overload(bool)
  def markDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QQuickContext2DTile::markDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2dtile.html#markDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QQuickContext2DTile::markDirty(bool dirty)
    self.uglySide.call('ritual_ZN19QQuickContext2DTile9markDirtyEb', dirty)

  @overload(bool, bool)
  def createPainter(
      self,
      smooth: bool,
      antialiasing: bool,
  ) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QQuickContext2DTile::createPainter(bool smooth,
    bool antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtile.html#createPainter

    Parameters
    ----------

    smooth : bool
      Passed on as it is.

    antialiasing : bool
      Passed on as it is.

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QQuickContext2DTile::createPainter(bool smooth, bool
    #      antialiasing)
    ritual = 'ritual_ZN19QQuickContext2DTile13createPainterEbb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickContext2DTile13createPainterEbb'
    address = self.uglySide.call(ritual, smooth, antialiasing)
    from ..QtGui import QPainter
    return QPainter._cuteAt(address)

  def drawFinished(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DTile::drawFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtile.html#drawFinished
    """
    #  void QQuickContext2DTile::drawFinished()
    ritual = 'ritual_ZN19QQuickContext2DTile12drawFinishedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickContext2DTile12drawFinishedEv'
    self.uglySide.call(ritual)

  def aboutToDraw(self) -> None:
    """
    Calls Qt's 'void QQuickContext2DTile::aboutToDraw()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2dtile.html#aboutToDraw
    """
    #  void QQuickContext2DTile::aboutToDraw()
    ritual = 'ritual_ZN19QQuickContext2DTile11aboutToDrawEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickContext2DTile11aboutToDrawEv'
    self.uglySide.call(ritual)
