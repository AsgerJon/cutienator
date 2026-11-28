"""
Qt3DCore::Quick::Quick3DGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dgeometry_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::Quick::Quick3DGeometry to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Quick3DGeometry(QObject):
  """
  The cute side of Qt's Qt3DCore::Quick::Quick3DGeometry: a plain Python
  object standing in front of one C++ Qt3DCore::Quick::Quick3DGeometry.

  It is built on the cute 'QObject', as Qt's Qt3DCore::Quick::Quick3DGeometry
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::Quick3DGeometry that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'parentGeometry'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Quick::Quick3DGeometry::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DCore::Quick::Quick3DGeometry::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<Qt3DCore::QAttribute>
    Qt3DCore::Quick::Quick3DGeometry::attributeList()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::Quick3DGeometry is created at the first use, not
    by 'Qt3DCore::Quick::Quick3DGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::Quick3DGeometry.
  - Qt tells when it has removed the C++ Qt3DCore::Quick::Quick3DGeometry.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::Quick::Quick3DGeometry that has no cute
    function yet, 'attributeList', holds a function that raises
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
    Calls Qt's 'QString Qt3DCore::Quick::Quick3DGeometry::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dgeometry.html#tr

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
    #  QString Qt3DCore::Quick::Quick3DGeometry::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Quick15Quick3DGeometry2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::Quick3DGeometry'

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
    *Qt3DCore::Quick::Quick3DGeometry::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::Quick::Quick3DGeometry::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick15Quick3DGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parentGeometry(self) -> Optional[Qt3DCore.QGeometry]:
    """
    Calls Qt's 'QGeometry *Qt3DCore::Quick::Quick3DGeometry::parentGeometry()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dgeometry.html#parentGeometry

    Returns
    -------

    Optional[Qt3DCore.QGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeometry *Qt3DCore::Quick::Quick3DGeometry::parentGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick15Quick3DGeometry14parentGeometryEv',
    )
    return Qt3DCore.QGeometry._cuteAt(address)

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
    'Qt3DCore::Quick::Quick3DGeometry::Quick3DGeometry(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dgeometry.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Quick::Quick3DGeometry::Quick3DGeometry(QObject *parent)
    self._noteCreation(Quick3DGeometry, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick15Quick3DGeometryC1EP7QObject',
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

  @staticmethod
  def attributeList(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<Qt3DCore::QAttribute>
    Qt3DCore::Quick::Quick3DGeometry::attributeList()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.Quick.Quick3DGeometry.attributeList' has no cute "
        "function yet. Qt's 'QQmlListProperty<Qt3DCore::QAttribute> "
        "Qt3DCore::Quick::Quick3DGeometry::attributeList()': gives a type "
        "Python has no way to take yet.")
