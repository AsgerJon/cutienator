"""
ChartItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means ChartItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList
from . import ChartElement

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import AbstractDomain, QAbstractSeriesPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartItem(ChartElement):
  """
  The cute side of Qt's ChartItem: a plain Python object standing in front of
  one C++ ChartItem.

  It is built on the cute 'ChartElement', as Qt's ChartItem is built on Qt's
  ChartElement, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartItem that has a ritual and that Python can call
  so far, 6 names in all: 'metaObject', 'tr', 'domain', 'cleanup',
  'seriesPrivate', 'handleDomainUpdated'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartItem::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ChartItem::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ ChartItem is created at the first use, not by 'ChartItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartItem.
  - Qt tells when it has removed the C++ ChartItem. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's ChartItem that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString ChartItem::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartitem.html#tr

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
    #  QString ChartItem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9ChartItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartItem'

  #  The functions Qt calls itself that ChartItem is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'cleanup': (
          ('_ZN9ChartItem7cleanupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleDomainUpdated': (
          ('_ZN9ChartItem19handleDomainUpdatedEv',
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
    Calls Qt's 'const QMetaObject *ChartItem::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartItem::metaObject() const
    address = self.uglySide.call('ritual_ZNK9ChartItem10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def domain(self) -> Optional[AbstractDomain]:
    """
    Calls Qt's 'AbstractDomain *ChartItem::domain() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartitem.html#domain

    Returns
    -------

    Optional[AbstractDomain]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractDomain *ChartItem::domain() const
    address = self.uglySide.call('ritual_ZNK9ChartItem6domainEv')
    from . import AbstractDomain
    return AbstractDomain._cuteAt(address)

  def seriesPrivate(self) -> Optional[QAbstractSeriesPrivate]:
    """
    Calls Qt's 'QAbstractSeriesPrivate *ChartItem::seriesPrivate() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartitem.html#seriesPrivate

    Returns
    -------

    Optional[QAbstractSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSeriesPrivate *ChartItem::seriesPrivate() const
    address = self.uglySide.call('ritual_ZNK9ChartItem13seriesPrivateEv')
    from . import QAbstractSeriesPrivate
    return QAbstractSeriesPrivate._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'ChartItem::ChartItem(QAbstractSeriesPrivate *series, QGraphicsItem
    *item)': the class is abstract, so C++ cannot make one, and the C++ class
    of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'ChartItem.__init__' has no cute function yet. Qt's "
        "'ChartItem::ChartItem(QAbstractSeriesPrivate *series, "
        "QGraphicsItem *item)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void ChartItem::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/chartitem.html#cleanup
    """
    #  void ChartItem::cleanup()
    ritual = 'ritual_ZN9ChartItem7cleanupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9ChartItem7cleanupEv'
    self.uglySide.call(ritual)

  def handleDomainUpdated(self) -> None:
    """
    Calls Qt's 'void ChartItem::handleDomainUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/chartitem.html#handleDomainUpdated
    """
    #  void ChartItem::handleDomainUpdated()
    ritual = 'ritual_ZN9ChartItem19handleDomainUpdatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9ChartItem19handleDomainUpdatedEv'
    self.uglySide.call(ritual)


#  Qt's 'QList<ChartItem *>': the list of ChartItem, which 'QList[ChartItem]'
#  gives. It is made here, so that there is one as soon as there can be a
#  ChartItem.
QList.createKind(
    ChartItem, 'address',
    make='ritual_list_make_ChartItem_ptr',
    add='ritual_list_add_ChartItem_ptr',
    size='ritual_list_size_ChartItem_ptr',
    at='ritual_list_at_ChartItem_ptr',
    drop='ritual_list_drop_ChartItem_ptr',
)
