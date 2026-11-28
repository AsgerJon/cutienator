"""
QDeclarativeGeoMapItemGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemgroup_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapItemGroup to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDeclarativeGeoMap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMapItemGroup(QQuickItem):
  """
  The cute side of Qt's QDeclarativeGeoMapItemGroup: a plain Python object
  standing in front of one C++ QDeclarativeGeoMapItemGroup.

  It is built on the cute 'QQuickItem', as Qt's QDeclarativeGeoMapItemGroup
  is built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapItemGroup that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'setQuickMap', 'quickMap', 'mapItemOpacity', 'mapItemOpacityChanged',
  'addTransitionFinished', 'removeTransitionFinished', 'classBegin',
  'componentComplete', 'onMapSizeChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoMapItemGroup::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoMapItemGroup::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoMapItemGroup::~QDeclarativeGeoMapItemGroup()': the
    destructor: Python never removes a C++ QDeclarativeGeoMapItemGroup.
  - Qt's 'void
    QDeclarativeGeoMapItemGroup::setParentGroup(QDeclarativeGeoMapItemGroup
    &parentGroup)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapItemGroup is created at the first use, not by
    'QDeclarativeGeoMapItemGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMapItemGroup.
  - Qt tells when it has removed the C++ QDeclarativeGeoMapItemGroup. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoMapItemGroup that has no cute function
    yet, 'setParentGroup', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QDeclarativeGeoMapItemGroup::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#tr

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
    #  QString QDeclarativeGeoMapItemGroup::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapItemGroup'

  #  A C++ QDeclarativeGeoMapItemGroup Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMapItemGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoMapItemGroup::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoMapItemGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapItemGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def quickMap(self) -> Optional[QDeclarativeGeoMap]:
    """
    Calls Qt's 'QDeclarativeGeoMap *QDeclarativeGeoMapItemGroup::quickMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#quickMap

    Returns
    -------

    Optional[QDeclarativeGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoMap *QDeclarativeGeoMapItemGroup::quickMap() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapItemGroup8quickMapEv',
    )
    from . import QDeclarativeGeoMap
    return QDeclarativeGeoMap._cuteAt(address)

  def mapItemOpacity(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMapItemGroup::mapItemOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#mapItemOpacity
    """
    #  qreal QDeclarativeGeoMapItemGroup::mapItemOpacity() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativeGeoMapItemGroup14mapItemOpacityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativeGeoMap)
  @overload(NoneType)
  def setQuickMap(self, quickMap: Optional[QDeclarativeGeoMap]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemGroup::setQuickMap(QDeclarativeGeoMap *quickMap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#setQuickMap

    Parameters
    ----------

    quickMap : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemGroup::setQuickMap(QDeclarativeGeoMap
    #      *quickMap)
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroup11setQuickMapEP18QDeclarativ'
        'eGeoMap',
        self._addressOf(quickMap),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativeGeoMapItemGroup::QDeclarativeGeoMapItemGroup(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoMapItemGroup::QDeclarativeGeoMapItemGroup(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativeGeoMapItemGroup, lambda: Rituals.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroupC1EP10QQuickItem',
        self._addressOf(parent),
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

  def mapItemOpacityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemGroup::mapItemOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html
    """
    #  void QDeclarativeGeoMapItemGroup::mapItemOpacityChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroup21mapItemOpacityChangedEv',
    )

  def addTransitionFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemGroup::addTransitionFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html
    """
    #  void QDeclarativeGeoMapItemGroup::addTransitionFinished()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroup21addTransitionFinishedEv',
    )

  def removeTransitionFinished(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemGroup::removeTransitionFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html
    """
    #  void QDeclarativeGeoMapItemGroup::removeTransitionFinished()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroup24removeTransitionFinishedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemGroup::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#classBegin
    """
    #  void QDeclarativeGeoMapItemGroup::classBegin()
    ritual = 'ritual_ZN27QDeclarativeGeoMapItemGroup10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QDeclarativeGeoMapItemGroup10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemGroup::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#componentComplete
    """
    #  void QDeclarativeGeoMapItemGroup::componentComplete()
    ritual = 'ritual_ZN27QDeclarativeGeoMapItemGroup17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativeGeoMapItemGroup17componentCompleteEv')
    self.uglySide.call(ritual)

  def onMapSizeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemGroup::onMapSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitemgroup.html#onMapSizeChanged
    """
    #  void QDeclarativeGeoMapItemGroup::onMapSizeChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativeGeoMapItemGroup16onMapSizeChangedEv',
    )

  @staticmethod
  def setParentGroup(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoMapItemGroup::setParentGroup(QDeclarativeGeoMapItemGroup
    &parentGroup)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoMapItemGroup.setParentGroup' has no cute function "
        "yet. Qt's 'void "
        "QDeclarativeGeoMapItemGroup::setParentGroup(QDeclarativeGeoMapItemG"
        "roup &parentGroup)': takes a type Python has no way to hand over "
        "yet.")
