"""
QWaylandQuickHardwareLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickhardwarelayer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandQuickHardwareLayer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWaylandQuickItem

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickHardwareLayer(QObject):
  """
  The cute side of Qt's QWaylandQuickHardwareLayer: a plain Python object
  standing in front of one C++ QWaylandQuickHardwareLayer.

  It is built on the cute 'QObject', as Qt's QWaylandQuickHardwareLayer is
  built on Qt's QObject, and has everything that class has. Qt's
  QWaylandQuickHardwareLayer is built on Qt's QQmlParserStatus as well, which
  is not reflected.

  What exists
  -----------

  Every function of Qt's QWaylandQuickHardwareLayer that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'tr',
  'stackingLevel', 'setStackingLevel', 'waylandItem', 'classBegin',
  'componentComplete', 'setSceneGraphPainting', 'initialize',
  'stackingLevelChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickHardwareLayer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWaylandQuickHardwareLayer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandQuickHardwareLayerPrivate
    *QWaylandQuickHardwareLayer::d_func()': gives
    'QWaylandQuickHardwareLayerPrivate', which has no cute class yet.
  - Qt's 'const QWaylandQuickHardwareLayerPrivate
    *QWaylandQuickHardwareLayer::d_func() const': gives
    'QWaylandQuickHardwareLayerPrivate', which has no cute class yet.
  - Qt's 'QWaylandQuickHardwareLayer::~QWaylandQuickHardwareLayer()': the
    destructor: Python never removes a C++ QWaylandQuickHardwareLayer.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickHardwareLayer is created at the first use, not by
    'QWaylandQuickHardwareLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickHardwareLayer.
  - Qt tells when it has removed the C++ QWaylandQuickHardwareLayer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QWaylandQuickHardwareLayer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandQuickHardwareLayer::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QWaylandQuickHardwareLayer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickHardwareLayer'

  #  A C++ QWaylandQuickHardwareLayer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickHardwareLayer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQuickHardwareLayer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickHardwareLayer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QWaylandQuickHardwareLayer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stackingLevel(self) -> int:
    """
    Calls Qt's 'int QWaylandQuickHardwareLayer::stackingLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#stackingLevel
    """
    #  int QWaylandQuickHardwareLayer::stackingLevel() const
    return self.uglySide.call(
        'ritual_ZNK26QWaylandQuickHardwareLayer13stackingLevelEv',
    )

  def waylandItem(self) -> Optional[QWaylandQuickItem]:
    """
    Calls Qt's 'QWaylandQuickItem *QWaylandQuickHardwareLayer::waylandItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#waylandItem

    Returns
    -------

    Optional[QWaylandQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickItem *QWaylandQuickHardwareLayer::waylandItem() const
    address = self.uglySide.call(
        'ritual_ZNK26QWaylandQuickHardwareLayer11waylandItemEv',
    )
    from . import QWaylandQuickItem
    return QWaylandQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStackingLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QWaylandQuickHardwareLayer::setStackingLevel(int
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#setStackingLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QWaylandQuickHardwareLayer::setStackingLevel(int level)
    self.uglySide.call(
        'ritual_ZN26QWaylandQuickHardwareLayer16setStackingLevelEi', level,
    )

  @overload(bool)
  def setSceneGraphPainting(self, a0: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickHardwareLayer::setSceneGraphPainting(bool
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QWaylandQuickHardwareLayer::setSceneGraphPainting(bool a0)
    self.uglySide.call(
        'ritual_ZN26QWaylandQuickHardwareLayer21setSceneGraphPaintingEb', a0,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickHardwareLayer::QWaylandQuickHardwareLayer(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandQuickHardwareLayer::QWaylandQuickHardwareLayer(QObject
    #      *parent)
    self._noteCreation(QWaylandQuickHardwareLayer, lambda: Rituals.call(
        'ritual_ZN26QWaylandQuickHardwareLayerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickHardwareLayer::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#classBegin
    """
    #  void QWaylandQuickHardwareLayer::classBegin()
    ritual = 'ritual_ZN26QWaylandQuickHardwareLayer10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QWaylandQuickHardwareLayer10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickHardwareLayer::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#componentComplete
    """
    #  void QWaylandQuickHardwareLayer::componentComplete()
    ritual = 'ritual_ZN26QWaylandQuickHardwareLayer17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QWaylandQuickHardwareLayer17componentCompleteEv')
    self.uglySide.call(ritual)

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickHardwareLayer::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html#initialize
    """
    #  void QWaylandQuickHardwareLayer::initialize()
    self.uglySide.call('ritual_ZN26QWaylandQuickHardwareLayer10initializeEv')

  def stackingLevelChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickHardwareLayer::stackingLevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickhardwarelayer.html
    """
    #  void QWaylandQuickHardwareLayer::stackingLevelChanged()
    self.uglySide.call(
        'ritual_ZN26QWaylandQuickHardwareLayer20stackingLevelChangedEv',
    )
