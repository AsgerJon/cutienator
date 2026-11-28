"""
Q3DScenePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/q3dscene_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Q3DScenePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from . import Q3DScene
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']


class Q3DScenePrivate(QObjectPrivate):
  """
  The cute side of Qt's Q3DScenePrivate: a plain Python object standing in
  front of one C++ Q3DScenePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's Q3DScenePrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DScenePrivate that has a ritual and that Python
  can call so far, 8 names in all: 'q_func', 'setViewport',
  'setViewportSize', 'setWindowSize', 'windowSize', 'updateDefaultViewports',
  'markDirty', 'isInArea'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Q3DScene *Q3DScenePrivate::q_func() const': takes in Python
    what 'Q3DScene *Q3DScenePrivate::q_func()' takes.
  - Qt's 'Q3DScenePrivate::~Q3DScenePrivate()': the destructor: Python never
    removes a C++ Q3DScenePrivate.
  - Qt's 'void Q3DScenePrivate::sync(Q3DScenePrivate &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ Q3DScenePrivate is created at the first use, not by
    'Q3DScenePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DScenePrivate.
  - Each name of Qt's Q3DScenePrivate that has no cute function yet, 'sync',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DScenePrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def windowSize(self) -> QSize:
    """
    Calls Qt's 'QSize Q3DScenePrivate::windowSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#windowSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Q3DScenePrivate::windowSize() const
    address = self.uglySide.call('ritual_ZNK15Q3DScenePrivate10windowSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRect, int, int)
  def isInArea(self, area: QRect, x: int, y: int) -> bool:
    """
    Calls Qt's 'bool Q3DScenePrivate::isInArea(const QRect area, int x, int
    y) const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#isInArea

    Parameters
    ----------

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  bool Q3DScenePrivate::isInArea(const QRect area, int x, int y) const
    return self.uglySide.call(
        'ritual_ZNK15Q3DScenePrivate8isInAreaE5QRectii',
        self._valueOf(area), x, y,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setViewport(self, viewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setViewport(const QRect viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#setViewport

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScenePrivate::setViewport(const QRect viewport)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate11setViewportE5QRect',
        self._valueOf(viewport),
    )

  @overload(int, int)
  def setViewportSize(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setViewportSize(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#setViewportSize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void Q3DScenePrivate::setViewportSize(int width, int height)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate15setViewportSizeEii', width, height,
    )

  @overload(QSize)
  def setWindowSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setWindowSize(QSize size)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#setWindowSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Q3DScenePrivate::setWindowSize(QSize size)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate13setWindowSizeE5QSize',
        self._valueOf(size),
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
    Notes what was given, for Qt's 'Q3DScenePrivate::Q3DScenePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#Q3DScenePrivate
    """
    #  Q3DScenePrivate::Q3DScenePrivate()
    self._noteCreation(Q3DScenePrivate, lambda: Rituals.call(
        'ritual_ZN15Q3DScenePrivateC1Ev',
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

  def q_func(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *Q3DScenePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#q_func

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *Q3DScenePrivate::q_func()
    address = self.uglySide.call('ritual_ZN15Q3DScenePrivate6q_funcEv')
    from . import Q3DScene
    return Q3DScene._cuteAt(address)

  def updateDefaultViewports(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::updateDefaultViewports()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#updateDefaultViewports
    """
    #  void Q3DScenePrivate::updateDefaultViewports()
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate22updateDefaultViewportsEv',
    )

  def markDirty(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#markDirty
    """
    #  void Q3DScenePrivate::markDirty()
    self.uglySide.call('ritual_ZN15Q3DScenePrivate9markDirtyEv')

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void Q3DScenePrivate::sync(Q3DScenePrivate &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DScenePrivate.sync' has no cute function yet. Qt's 'void "
        "Q3DScenePrivate::sync(Q3DScenePrivate &other)': takes a type "
        "Python has no way to hand over yet.")
