"""
QQuickItemViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickItemViewAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemViewAttached(QObject):
  """
  The cute side of Qt's QQuickItemViewAttached: a plain Python object
  standing in front of one C++ QQuickItemViewAttached.

  It is built on the cute 'QObject', as Qt's QQuickItemViewAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemViewAttached that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr',
  'isCurrentItem', 'setIsCurrentItem', 'delayRemove', 'setDelayRemove',
  'section', 'setSection', 'prevSection', 'setPrevSection', 'nextSection',
  'setNextSection', 'setSections', 'emitAdd', 'emitRemove', 'viewChanged',
  'currentItemChanged', 'delayRemoveChanged', 'add', 'remove',
  'sectionChanged', 'prevSectionChanged', 'nextSectionChanged', 'pooled',
  'reused'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickItemViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickItemViewAttached::~QQuickItemViewAttached()': the destructor:
    Python never removes a C++ QQuickItemViewAttached.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemViewAttached is created at the first use, not by
    'QQuickItemViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemViewAttached.
  - Qt tells when it has removed the C++ QQuickItemViewAttached. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickItemViewAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewattached.html#tr

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
    #  QString QQuickItemViewAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickItemViewAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewAttached'

  #  A C++ QQuickItemViewAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItemViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickItemViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isCurrentItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewAttached::isCurrentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#isCurrentItem
    """
    #  bool QQuickItemViewAttached::isCurrentItem() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickItemViewAttached13isCurrentItemEv',
    )

  def delayRemove(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewAttached::delayRemove() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#delayRemove
    """
    #  bool QQuickItemViewAttached::delayRemove() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickItemViewAttached11delayRemoveEv',
    )

  def section(self) -> str:
    """
    Calls Qt's 'QString QQuickItemViewAttached::section() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#section

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemViewAttached::section() const
    return self.uglySide.call('ritual_ZNK22QQuickItemViewAttached7sectionEv')

  def prevSection(self) -> str:
    """
    Calls Qt's 'QString QQuickItemViewAttached::prevSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#prevSection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemViewAttached::prevSection() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickItemViewAttached11prevSectionEv',
    )

  def nextSection(self) -> str:
    """
    Calls Qt's 'QString QQuickItemViewAttached::nextSection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#nextSection

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemViewAttached::nextSection() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickItemViewAttached11nextSectionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsCurrentItem(self, c: bool) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::setIsCurrentItem(bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#setIsCurrentItem

    Parameters
    ----------

    c : bool
      Passed on as it is.
    """
    #  void QQuickItemViewAttached::setIsCurrentItem(bool c)
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached16setIsCurrentItemEb', c,
    )

  @overload(bool)
  def setDelayRemove(self, delay: bool) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::setDelayRemove(bool delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#setDelayRemove

    Parameters
    ----------

    delay : bool
      Passed on as it is.
    """
    #  void QQuickItemViewAttached::setDelayRemove(bool delay)
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached14setDelayRemoveEb', delay,
    )

  @overload(str)
  def setSection(self, sect: str) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::setSection(const QString
    &sect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#setSection

    Parameters
    ----------

    sect : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItemViewAttached::setSection(const QString &sect)
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached10setSectionERK7QString', sect,
    )

  @overload(str)
  def setPrevSection(self, sect: str) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::setPrevSection(const QString
    &sect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#setPrevSection

    Parameters
    ----------

    sect : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItemViewAttached::setPrevSection(const QString &sect)
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached14setPrevSectionERK7QString', sect,
    )

  @overload(str)
  def setNextSection(self, sect: str) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::setNextSection(const QString
    &sect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#setNextSection

    Parameters
    ----------

    sect : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItemViewAttached::setNextSection(const QString &sect)
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached14setNextSectionERK7QString', sect,
    )

  @overload(str, str, str)
  def setSections(self, prev: str, sect: str, next: str) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::setSections(const QString &prev,
    const QString &sect, const QString &next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#setSections

    Parameters
    ----------

    prev : str
      Passed on as it is: a QString is made of it for the call.

    sect : str
      Passed on as it is: a QString is made of it for the call.

    next : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickItemViewAttached::setSections(const QString &prev, const
    #      QString &sect, const QString &next)
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached11setSectionsERK7QStringS2_S2_',
        prev, sect, next,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemViewAttached::QQuickItemViewAttached(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#QQuickItemViewAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickItemViewAttached::QQuickItemViewAttached(QObject *parent)
    self._noteCreation(QQuickItemViewAttached, lambda: Rituals.call(
        'ritual_ZN22QQuickItemViewAttachedC1EP7QObject',
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

  def emitAdd(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::emitAdd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#emitAdd
    """
    #  void QQuickItemViewAttached::emitAdd()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached7emitAddEv')

  def emitRemove(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::emitRemove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#emitRemove
    """
    #  void QQuickItemViewAttached::emitRemove()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached10emitRemoveEv')

  def viewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::viewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#viewChanged
    """
    #  void QQuickItemViewAttached::viewChanged()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached11viewChangedEv')

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#currentItemChanged
    """
    #  void QQuickItemViewAttached::currentItemChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached18currentItemChangedEv',
    )

  def delayRemoveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::delayRemoveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#delayRemoveChanged
    """
    #  void QQuickItemViewAttached::delayRemoveChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached18delayRemoveChangedEv',
    )

  def add(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::add()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewattached.html#add
    """
    #  void QQuickItemViewAttached::add()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached3addEv')

  def remove(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewattached.html#remove
    """
    #  void QQuickItemViewAttached::remove()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached6removeEv')

  def sectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::sectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#sectionChanged
    """
    #  void QQuickItemViewAttached::sectionChanged()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached14sectionChangedEv')

  def prevSectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::prevSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#prevSectionChanged
    """
    #  void QQuickItemViewAttached::prevSectionChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached18prevSectionChangedEv',
    )

  def nextSectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::nextSectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewattached.html#nextSectionChanged
    """
    #  void QQuickItemViewAttached::nextSectionChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickItemViewAttached18nextSectionChangedEv',
    )

  def pooled(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::pooled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewattached.html#pooled
    """
    #  void QQuickItemViewAttached::pooled()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached6pooledEv')

  def reused(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewAttached::reused()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewattached.html#reused
    """
    #  void QQuickItemViewAttached::reused()
    self.uglySide.call('ritual_ZN22QQuickItemViewAttached6reusedEv')
