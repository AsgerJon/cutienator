"""
QQmlCompositeFilterBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlcompositefilterbase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlCompositeFilterBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlFilterCompositor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlCompositeFilterBasePrivate, QQmlFilterCompositorPrivate
  from . import QQmlSortFilterProxyModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlFilterCompositorPrivate = WAIT['QQmlFilterCompositorPrivate']
  QQmlSortFilterProxyModel = WAIT['QQmlSortFilterProxyModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlCompositeFilterBase(QQmlFilterCompositor):
  """
  The cute side of Qt's QQmlCompositeFilterBase: a plain Python object
  standing in front of one C++ QQmlCompositeFilterBase.

  It is built on the cute 'QQmlFilterCompositor', as Qt's
  QQmlCompositeFilterBase is built on Qt's QQmlFilterCompositor, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlCompositeFilterBase that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'update',
  'isActive', 'column', 'setColumn', 'supportColumnFiltering',
  'refreshCache', 'd_func'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlCompositeFilterBase::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlCompositeFilterBase::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlCompositeFilterBase::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'const QQmlCompositeFilterBasePrivate
    *QQmlCompositeFilterBase::d_func() const': takes in Python what
    'QQmlCompositeFilterBasePrivate *QQmlCompositeFilterBase::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlCompositeFilterBase is created at the first use, not by
    'QQmlCompositeFilterBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlCompositeFilterBase.
  - Qt tells when it has removed the C++ QQmlCompositeFilterBase. Every call
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
    Calls Qt's 'QString QQmlCompositeFilterBase::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#tr

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
    #  QString QQmlCompositeFilterBase::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQmlCompositeFilterBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCompositeFilterBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlCompositeFilterBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlCompositeFilterBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlCompositeFilterBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQmlCompositeFilterBase::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#isActive
    """
    #  bool QQmlCompositeFilterBase::isActive() const
    ritual = 'ritual_ZNK23QQmlCompositeFilterBase8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQmlCompositeFilterBase8isActiveEv'
    return self.uglySide.call(ritual)

  def column(self) -> int:
    """
    Calls Qt's 'int QQmlCompositeFilterBase::column() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#column
    """
    #  int QQmlCompositeFilterBase::column() const
    ritual = 'ritual_ZNK23QQmlCompositeFilterBase6columnEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQmlCompositeFilterBase6columnEv'
    return self.uglySide.call(ritual)

  def supportColumnFiltering(self) -> bool:
    """
    Calls Qt's 'bool QQmlCompositeFilterBase::supportColumnFiltering()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html
    """
    #  bool QQmlCompositeFilterBase::supportColumnFiltering() const
    ritual = 'ritual_ZNK23QQmlCompositeFilterBase22supportColumnFilteringEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QQmlCompositeFilterBase22supportColumnFilteringE'
          'v')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QQmlCompositeFilterBase::setColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#setColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QQmlCompositeFilterBase::setColumn(int column)
    ritual = 'ritual_ZN23QQmlCompositeFilterBase9setColumnEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQmlCompositeFilterBase9setColumnEi'
    self.uglySide.call(ritual, column)

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
    'QQmlCompositeFilterBase::QQmlCompositeFilterBase(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlCompositeFilterBase::QQmlCompositeFilterBase(QObject *parent)
    self._noteCreation(QQmlCompositeFilterBase, lambda: Rituals.call(
        'ritual_ZN23QQmlCompositeFilterBaseC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlFilterCompositorPrivate, QObject)
  @overload(QQmlFilterCompositorPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      priv: Optional[QQmlFilterCompositorPrivate],
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlCompositeFilterBase::QQmlCompositeFilterBase(
    QQmlFilterCompositorPrivate *priv, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html

    Parameters
    ----------

    priv : Optional[QQmlFilterCompositorPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlCompositeFilterBase::QQmlCompositeFilterBase(
    #      QQmlFilterCompositorPrivate *priv, QObject *parent)
    self._noteCreation(QQmlCompositeFilterBase, lambda: Rituals.call(
        'ritual_ZN23QQmlCompositeFilterBaseC1EP27QQmlFilterCompositorPrivat'
        'eP7QObject',
        self._addressOf(priv), self._addressOf(parent, 'QObject'),
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

  @overload(QQmlSortFilterProxyModel)
  @overload(NoneType)
  def update(self, model: Optional[QQmlSortFilterProxyModel]) -> None:
    """
    Calls Qt's 'void QQmlCompositeFilterBase::update(const
    QQmlSortFilterProxyModel *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#update

    Parameters
    ----------

    model : Optional[QQmlSortFilterProxyModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlCompositeFilterBase::update(const QQmlSortFilterProxyModel
    #      *model)
    ritual = (
        'ritual_ZN23QQmlCompositeFilterBase6updateEPK24QQmlSortFilterProxyM'
        'odel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQmlCompositeFilterBase6updateEPK24QQmlSortFilter'
          'ProxyModel')
    self.uglySide.call(ritual, self._addressOf(model))

  def refreshCache(self) -> None:
    """
    Calls Qt's 'void QQmlCompositeFilterBase::refreshCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#refreshCache
    """
    #  void QQmlCompositeFilterBase::refreshCache()
    ritual = 'ritual_ZN23QQmlCompositeFilterBase12refreshCacheEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQmlCompositeFilterBase12refreshCacheEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQmlCompositeFilterBasePrivate]:
    """
    Calls Qt's 'QQmlCompositeFilterBasePrivate
    *QQmlCompositeFilterBase::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcompositefilterbase.html#d_func

    Returns
    -------

    Optional[QQmlCompositeFilterBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlCompositeFilterBasePrivate *QQmlCompositeFilterBase::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQmlCompositeFilterBase6d_funcEv',
    )
    from . import QQmlCompositeFilterBasePrivate
    return QQmlCompositeFilterBasePrivate._cuteAt(address)
