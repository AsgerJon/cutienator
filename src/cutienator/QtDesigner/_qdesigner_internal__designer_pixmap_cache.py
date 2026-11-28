"""
qdesigner_internal::DesignerPixmapCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DesignerPixmapCache to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPixmap

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DesignerPixmapCache(QObject):
  """
  The cute side of Qt's qdesigner_internal::DesignerPixmapCache: a plain
  Python object standing in front of one C++
  qdesigner_internal::DesignerPixmapCache.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::DesignerPixmapCache is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DesignerPixmapCache that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'pixmap', 'clear', 'reloaded'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::DesignerPixmapCache::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::DesignerPixmapCache::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::DesignerPixmapCache is created at the first
    use, not by 'qdesigner_internal::DesignerPixmapCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::DesignerPixmapCache.
  - Qt tells when it has removed the C++
    qdesigner_internal::DesignerPixmapCache. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString qdesigner_internal::DesignerPixmapCache::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designerpixmapcache.html#tr

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
    #  QString qdesigner_internal::DesignerPixmapCache::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19DesignerPixmapCache2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DesignerPixmapCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::DesignerPixmapCache::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designerpixmapcache.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::DesignerPixmapCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19DesignerPixmapCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(WAIT['qdesigner_internal.PropertySheetPixmapValue'])
  def pixmap(
      self,
      value: qdesigner_internal.PropertySheetPixmapValue,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap qdesigner_internal::DesignerPixmapCache::pixmap(const
    PropertySheetPixmapValue &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designerpixmapcache.html#pixmap

    Parameters
    ----------

    value : qdesigner_internal.PropertySheetPixmapValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetPixmapValue, which stays Python's own.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::DesignerPixmapCache::pixmap(const
    #      PropertySheetPixmapValue &value) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19DesignerPixmapCache6pixmapERKNS_24'
        'PropertySheetPixmapValueE',
        self._valueOf(value),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DesignerPixmapCache::DesignerPixmapCache(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designerpixmapcache.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::DesignerPixmapCache::DesignerPixmapCache(QObject
    #      *parent)
    self._noteCreation(DesignerPixmapCache, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19DesignerPixmapCacheC1EP7QObject',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DesignerPixmapCache::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designerpixmapcache.html#clear
    """
    #  void qdesigner_internal::DesignerPixmapCache::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19DesignerPixmapCache5clearEv',
    )

  def reloaded(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::DesignerPixmapCache::reloaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designerpixmapcache.html
    """
    #  void qdesigner_internal::DesignerPixmapCache::reloaded()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19DesignerPixmapCache8reloadedEv',
    )
