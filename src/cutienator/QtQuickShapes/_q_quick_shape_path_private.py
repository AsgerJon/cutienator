"""
QQuickShapePathPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShapePathPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickShapePath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickShapePath = WAIT['QQuickShapePath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapePathPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapePathPrivate: a plain Python object
  standing in front of one C++ QQuickShapePathPrivate.

  What exists
  -----------

  Every function of Qt's QQuickShapePathPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', '_q_fillGradientChanged',
  '_q_strokeGradientChanged', '_q_fillItemDestroyed', 'get'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickShapePath *QQuickShapePathPrivate::q_func() const':
    takes in Python what 'QQuickShapePath *QQuickShapePathPrivate::q_func()'
    takes.
  - Qt's 'void QQuickShapePathPrivate::writeToDebugStream(QDebug &debug)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickShapePathPrivate is created at the first use, not by
    'QQuickShapePathPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapePathPrivate.
  - Each name of Qt's QQuickShapePathPrivate that has no cute function yet,
    '_q_pathChanged', 'handleSceneChange', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickShapePathPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Dirty(CuteNum):
    """
    The enum 'QQuickShapePathPrivate::Dirty' of Qt, with the 13 names Qt
    gives in it.
    """

    DirtyPath = Kee[int](1)
    DirtyStrokeColor = Kee[int](2)
    DirtyStrokeWidth = Kee[int](4)
    DirtyFillColor = Kee[int](8)
    DirtyFillRule = Kee[int](16)
    DirtyStyle = Kee[int](32)
    DirtyDash = Kee[int](64)
    DirtyFillGradient = Kee[int](128)
    DirtyFillTransform = Kee[int](256)
    DirtyFillItem = Kee[int](512)
    DirtyTrim = Kee[int](1024)
    DirtyStrokeGradient = Kee[int](2048)
    DirtyAll = Kee[int](4095)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickShapePath)
  @overload(NoneType)
  def get(p: Optional[QQuickShapePath]) -> Optional[QQuickShapePathPrivate]:
    """
    Calls Qt's 'QQuickShapePathPrivate
    *QQuickShapePathPrivate::get(QQuickShapePath *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepathprivate.html#get

    Parameters
    ----------

    p : Optional[QQuickShapePath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickShapePathPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapePathPrivate *QQuickShapePathPrivate::get(QQuickShapePath
    #      *p)
    address = Rituals.call(
        'ritual_ZN22QQuickShapePathPrivate3getEP15QQuickShapePath',
        CuteMixin._addressOf(p),
    )
    return QQuickShapePathPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapePathPrivate'

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
    Notes what was given, for Qt's
    'QQuickShapePathPrivate::QQuickShapePathPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepathprivate.html#QQuickShapePathPrivate
    """
    #  QQuickShapePathPrivate::QQuickShapePathPrivate()
    self._noteCreation(QQuickShapePathPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickShapePathPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickShapePath]:
    """
    Calls Qt's 'QQuickShapePath *QQuickShapePathPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepathprivate.html#q_func

    Returns
    -------

    Optional[QQuickShapePath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapePath *QQuickShapePathPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickShapePathPrivate6q_funcEv',
    )
    from . import QQuickShapePath
    return QQuickShapePath._cuteAt(address)

  def _q_fillGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePathPrivate::_q_fillGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepathprivate.html#_q_fillGradientChanged
    """
    #  void QQuickShapePathPrivate::_q_fillGradientChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickShapePathPrivate22_q_fillGradientChangedEv',
    )

  def _q_strokeGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePathPrivate::_q_strokeGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepathprivate.html
    """
    #  void QQuickShapePathPrivate::_q_strokeGradientChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickShapePathPrivate24_q_strokeGradientChangedEv',
    )

  def _q_fillItemDestroyed(self) -> None:
    """
    Calls Qt's 'void QQuickShapePathPrivate::_q_fillItemDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepathprivate.html#_q_fillItemDestroyed
    """
    #  void QQuickShapePathPrivate::_q_fillItemDestroyed()
    self.uglySide.call(
        'ritual_ZN22QQuickShapePathPrivate20_q_fillItemDestroyedEv',
    )

  @staticmethod
  def _q_pathChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapePathPrivate::_q_pathChanged()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickShapePathPrivate._q_pathChanged' has no cute function yet. "
        "Qt's 'void QQuickShapePathPrivate::_q_pathChanged()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def handleSceneChange(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapePathPrivate::handleSceneChange()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickShapePathPrivate.handleSceneChange' has no cute function "
        "yet. Qt's 'void QQuickShapePathPrivate::handleSceneChange()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
