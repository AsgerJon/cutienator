"""
QLegendMarkerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qlegendmarker_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLegendMarkerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import LegendMarkerItem, QAbstractSeries, QLegend, QLegendMarker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLegend = WAIT['QLegend']
  QLegendMarker = WAIT['QLegendMarker']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLegendMarkerPrivate(QObject):
  """
  The cute side of Qt's QLegendMarkerPrivate: a plain Python object standing
  in front of one C++ QLegendMarkerPrivate.

  It is built on the cute 'QObject', as Qt's QLegendMarkerPrivate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLegendMarkerPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'item',
  'series', 'relatedObject', 'invalidateLegend', 'invalidateAllItems',
  'updated', 'handleShapeChange', 'q_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLegendMarkerPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QLegendMarkerPrivate::~QLegendMarkerPrivate()': the destructor:
    Python never removes a C++ QLegendMarkerPrivate.
  - Qt's 'const QLegendMarker *QLegendMarkerPrivate::q_func() const': takes
    in Python what 'QLegendMarker *QLegendMarkerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLegendMarkerPrivate is created at the first use, not by
    'QLegendMarkerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLegendMarkerPrivate.
  - Qt tells when it has removed the C++ QLegendMarkerPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QLegendMarkerPrivate::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarkerprivate.html#tr

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
    #  QString QLegendMarkerPrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QLegendMarkerPrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLegendMarkerPrivate'

  #  A C++ QLegendMarkerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLegendMarkerPrivate'

  #  The functions Qt calls itself that QLegendMarkerPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'series': (
          ('_ZN20QLegendMarkerPrivate6seriesEv',
           ('address', 'address', 'QtCharts:QAbstractSeries'),
           ()),
      ),
      'relatedObject': (
          ('_ZN20QLegendMarkerPrivate13relatedObjectEv',
           ('address', 'address', 'QtCore:QObject'),
           ()),
      ),
      'updated': (
          ('_ZN20QLegendMarkerPrivate7updatedEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLegendMarkerPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarkerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLegendMarkerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QLegendMarkerPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def item(self) -> Optional[LegendMarkerItem]:
    """
    Calls Qt's 'LegendMarkerItem *QLegendMarkerPrivate::item() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarkerprivate.html#item

    Returns
    -------

    Optional[LegendMarkerItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LegendMarkerItem *QLegendMarkerPrivate::item() const
    address = self.uglySide.call('ritual_ZNK20QLegendMarkerPrivate4itemEv')
    from . import LegendMarkerItem
    return LegendMarkerItem._cuteAt(address)

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

  @overload(QLegendMarker, QLegend)
  @overload(QLegendMarker, NoneType)
  @overload(NoneType, QLegend)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QLegendMarker],
      legend: Optional[QLegend],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QLegendMarkerPrivate::QLegendMarkerPrivate(QLegendMarker *q, QLegend
    *legend)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarkerprivate.html#QLegendMarkerPrivate

    Parameters
    ----------

    q : Optional[QLegendMarker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QLegendMarkerPrivate::QLegendMarkerPrivate(QLegendMarker *q, QLegend
    #      *legend)
    self._noteCreation(QLegendMarkerPrivate, lambda: Rituals.call(
        'ritual_ZN20QLegendMarkerPrivateC1EP13QLegendMarkerP7QLegend',
        self._addressOf(q), self._addressOf(legend),
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

  def series(self) -> Optional[QAbstractSeries]:
    """
    Calls Qt's 'QAbstractSeries *QLegendMarkerPrivate::series()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarkerprivate.html#series

    Returns
    -------

    Optional[QAbstractSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeries *QLegendMarkerPrivate::series()
    address = self.uglySide.call('ritual_ZN20QLegendMarkerPrivate6seriesEv')
    from . import QAbstractSeries
    return QAbstractSeries._cuteAt(address)

  def relatedObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QLegendMarkerPrivate::relatedObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarkerprivate.html#relatedObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QLegendMarkerPrivate::relatedObject()
    address = self.uglySide.call(
        'ritual_ZN20QLegendMarkerPrivate13relatedObjectEv',
    )
    return QObject._cuteAt(address)

  def invalidateLegend(self) -> None:
    """
    Calls Qt's 'void QLegendMarkerPrivate::invalidateLegend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarkerprivate.html#invalidateLegend
    """
    #  void QLegendMarkerPrivate::invalidateLegend()
    self.uglySide.call('ritual_ZN20QLegendMarkerPrivate16invalidateLegendEv')

  def invalidateAllItems(self) -> None:
    """
    Calls Qt's 'void QLegendMarkerPrivate::invalidateAllItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarkerprivate.html#invalidateAllItems
    """
    #  void QLegendMarkerPrivate::invalidateAllItems()
    self.uglySide.call(
        'ritual_ZN20QLegendMarkerPrivate18invalidateAllItemsEv',
    )

  def updated(self) -> None:
    """
    Calls Qt's 'void QLegendMarkerPrivate::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarkerprivate.html#updated
    """
    #  void QLegendMarkerPrivate::updated()
    self.uglySide.call('ritual_ZN20QLegendMarkerPrivate7updatedEv')

  def handleShapeChange(self) -> None:
    """
    Calls Qt's 'void QLegendMarkerPrivate::handleShapeChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlegendmarkerprivate.html#handleShapeChange
    """
    #  void QLegendMarkerPrivate::handleShapeChange()
    self.uglySide.call(
        'ritual_ZN20QLegendMarkerPrivate17handleShapeChangeEv',
    )

  def q_func(self) -> Optional[QLegendMarker]:
    """
    Calls Qt's 'QLegendMarker *QLegendMarkerPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlegendmarkerprivate.html#q_func

    Returns
    -------

    Optional[QLegendMarker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLegendMarker *QLegendMarkerPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QLegendMarkerPrivate6q_funcEv')
    from . import QLegendMarker
    return QLegendMarker._cuteAt(address)
