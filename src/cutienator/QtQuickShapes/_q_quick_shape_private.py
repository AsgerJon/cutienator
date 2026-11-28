"""
QQuickShapePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShapePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick import QQuickWindow, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapePrivate: a plain Python object standing in
  front of one C++ QQuickShapePrivate.

  What exists
  -----------

  Every function of Qt's QQuickShapePrivate that has a ritual and that Python
  can call so far, 12 names in all: 'q_func', 'init', 'selectRendererType',
  'createRenderer', 'createNode', 'sync', '_q_shapePathChanged', 'setStatus',
  'handleSceneChange', 'get', 'getImplicitWidth', 'getImplicitHeight'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickShape *QQuickShapePrivate::q_func() const': takes in
    Python what 'QQuickShape *QQuickShapePrivate::q_func()' takes.
  - Qt's 'QQuickShapePrivate::~QQuickShapePrivate()': the destructor: Python
    never removes a C++ QQuickShapePrivate.
  - Qt's 'void QQuickShapePrivate::asyncShapeReady(void *data)': names
    'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickShapePrivate is created at the first use, not by
    'QQuickShapePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapePrivate.
  - Each name of Qt's QQuickShapePrivate that has no cute function yet,
    'asyncShapeReady', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickShape)
  @overload(NoneType)
  def get(item: Optional[QQuickShape]) -> Optional[QQuickShapePrivate]:
    """
    Calls Qt's 'QQuickShapePrivate *QQuickShapePrivate::get(QQuickShape
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickShape]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapePrivate *QQuickShapePrivate::get(QQuickShape *item)
    address = Rituals.call(
        'ritual_ZN18QQuickShapePrivate3getEP11QQuickShape',
        CuteMixin._addressOf(item),
    )
    return QQuickShapePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapePrivate'

  #  A C++ QQuickShapePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapePrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#getImplicitWidth
    """
    #  qreal QQuickShapePrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK18QQuickShapePrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickShapePrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def getImplicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapePrivate::getImplicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#getImplicitHeight
    """
    #  qreal QQuickShapePrivate::getImplicitHeight() const
    ritual = 'ritual_ZNK18QQuickShapePrivate17getImplicitHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickShapePrivate17getImplicitHeightEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickShape.Status)
  def setStatus(self, newStatus: QQuickShape.Status) -> None:
    """
    Calls Qt's 'void QQuickShapePrivate::setStatus(QQuickShape::Status
    newStatus)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeprivate.html#setStatus

    Parameters
    ----------

    newStatus : QQuickShape.Status
      Passed on as its number.
    """
    #  void QQuickShapePrivate::setStatus(QQuickShape::Status newStatus)
    self.uglySide.call(
        'ritual_ZN18QQuickShapePrivate9setStatusEN11QQuickShape6StatusE',
        newStatus.value,
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
    'QQuickShapePrivate::QQuickShapePrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#QQuickShapePrivate
    """
    #  QQuickShapePrivate::QQuickShapePrivate()
    self._noteCreation(QQuickShapePrivate, lambda: Rituals.call(
        'ritual_ZN18QQuickShapePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickShape]:
    """
    Calls Qt's 'QQuickShape *QQuickShapePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeprivate.html#q_func

    Returns
    -------

    Optional[QQuickShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShape *QQuickShapePrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QQuickShapePrivate6q_funcEv')
    return QQuickShape._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickShapePrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeprivate.html#init
    """
    #  void QQuickShapePrivate::init()
    self.uglySide.call('ritual_ZN18QQuickShapePrivate4initEv')

  def selectRendererType(self) -> QQuickShape.RendererType:
    """
    Calls Qt's 'QQuickShape::RendererType
    QQuickShapePrivate::selectRendererType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#selectRendererType

    Returns
    -------

    QQuickShape.RendererType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShape.RendererType(number)' gives.
    """
    #  QQuickShape::RendererType QQuickShapePrivate::selectRendererType()
    return QQuickShape.RendererType(self.uglySide.call(
        'ritual_ZN18QQuickShapePrivate18selectRendererTypeEv',
    ))

  def createRenderer(self) -> None:
    """
    Calls Qt's 'void QQuickShapePrivate::createRenderer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#createRenderer
    """
    #  void QQuickShapePrivate::createRenderer()
    self.uglySide.call('ritual_ZN18QQuickShapePrivate14createRendererEv')

  def createNode(self) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickShapePrivate::createNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeprivate.html#createNode

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickShapePrivate::createNode()
    address = self.uglySide.call(
        'ritual_ZN18QQuickShapePrivate10createNodeEv',
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def sync(self) -> None:
    """
    Calls Qt's 'void QQuickShapePrivate::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapeprivate.html#sync
    """
    #  void QQuickShapePrivate::sync()
    self.uglySide.call('ritual_ZN18QQuickShapePrivate4syncEv')

  def _q_shapePathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePrivate::_q_shapePathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#_q_shapePathChanged
    """
    #  void QQuickShapePrivate::_q_shapePathChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickShapePrivate19_q_shapePathChangedEv',
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleSceneChange(self, w: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickShapePrivate::handleSceneChange(QQuickWindow *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapeprivate.html#handleSceneChange

    Parameters
    ----------

    w : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapePrivate::handleSceneChange(QQuickWindow *w)
    self.uglySide.call(
        'ritual_ZN18QQuickShapePrivate17handleSceneChangeEP12QQuickWindow',
        self._addressOf(w),
    )

  @staticmethod
  def asyncShapeReady(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapePrivate::asyncShapeReady(void *data)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickShapePrivate.asyncShapeReady' has no cute function yet. "
        "Qt's 'void QQuickShapePrivate::asyncShapeReady(void *data)': names "
        "'void', which has no cute class yet.")
