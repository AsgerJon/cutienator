"""
QWaylandQuickCompositorQuickExtensionContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorquickextensions_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandQuickCompositorQuickExtensionContainer to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QWaylandQuickCompositor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickCompositorQuickExtensionContainer(QWaylandQuickCompositor):
  """
  The cute side of Qt's QWaylandQuickCompositorQuickExtensionContainer: a
  plain Python object standing in front of one C++
  QWaylandQuickCompositorQuickExtensionContainer.

  It is built on the cute 'QWaylandQuickCompositor', as Qt's
  QWaylandQuickCompositorQuickExtensionContainer is built on Qt's
  QWaylandQuickCompositor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandQuickCompositorQuickExtensionContainer that
  has a ritual and that Python can call so far, 2 names in all: 'metaObject',
  'tr'. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QWaylandQuickCompositorQuickExtensionContainer::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QWaylandQuickCompositorQuickExtensionContainer::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QQmlListProperty<QObject>
    QWaylandQuickCompositorQuickExtensionContainer::data()': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlListProperty<QWaylandCompositorExtension>
    QWaylandQuickCompositorQuickExtensionContainer::extensions()': gives a
    type Python has no way to take yet.
  - Qt's 'qsizetype
    QWaylandQuickCompositorQuickExtensionContainer::countFunction(
    QQmlListProperty<QWaylandCompositorExtension> *list)': names
    'QQmlListProperty<QWaylandCompositorExtension>', which has no cute class
    yet.
  - Qt's 'QWaylandCompositorExtension
    *QWaylandQuickCompositorQuickExtensionContainer::atFunction(
    QQmlListProperty<QWaylandCompositorExtension> *list, qsizetype index)':
    names 'QQmlListProperty<QWaylandCompositorExtension>', which has no cute
    class yet.
  - Qt's 'void
    QWaylandQuickCompositorQuickExtensionContainer::append_extension(
    QQmlListProperty<QWaylandCompositorExtension> *list,
    QWaylandCompositorExtension *extension)': names
    'QQmlListProperty<QWaylandCompositorExtension>', which has no cute class
    yet.
  - Qt's 'void QWaylandQuickCompositorQuickExtensionContainer::clearFunction(
    QQmlListProperty<QWaylandCompositorExtension> *list)': names
    'QQmlListProperty<QWaylandCompositorExtension>', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickCompositorQuickExtensionContainer is created at the
    first use, not by 'QWaylandQuickCompositorQuickExtensionContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QWaylandQuickCompositorQuickExtensionContainer.
  - Qt tells when it has removed the C++
    QWaylandQuickCompositorQuickExtensionContainer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QWaylandQuickCompositorQuickExtensionContainer that has
    no cute function yet, 'append_extension', 'atFunction', 'clearFunction',
    'countFunction', 'data', holds a function that raises
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
    Calls Qt's 'QString
    QWaylandQuickCompositorQuickExtensionContainer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositorquickextensioncontainer.html

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
    #  QString QWaylandQuickCompositorQuickExtensionContainer::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN46QWaylandQuickCompositorQuickExtensionContainer2trEPKcS1'
        '_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickCompositorQuickExtensionContainer'

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
    *QWaylandQuickCompositorQuickExtensionContainer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickcompositorquickextensioncontainer.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QWaylandQuickCompositorQuickExtensionContainer::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK46QWaylandQuickCompositorQuickExtensionContainer10metaOb'
        'jectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  def append_extension(*__, **_) -> Never:
    """
    Qt's 'void
    QWaylandQuickCompositorQuickExtensionContainer::append_extension(
    QQmlListProperty<QWaylandCompositorExtension> *list,
    QWaylandCompositorExtension *extension)': names
    'QQmlListProperty<QWaylandCompositorExtension>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickCompositorQuickExtensionContainer.append_extension' "
        "has no cute function yet. Qt's 'void "
        "QWaylandQuickCompositorQuickExtensionContainer::append_extension(QQ"
        "mlListProperty<QWaylandCompositorExtension> *list, "
        "QWaylandCompositorExtension *extension)': names "
        "'QQmlListProperty<QWaylandCompositorExtension>', which has no cute "
        "class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QWaylandCompositorExtension
    *QWaylandQuickCompositorQuickExtensionContainer::atFunction(
    QQmlListProperty<QWaylandCompositorExtension> *list, qsizetype index)':
    names 'QQmlListProperty<QWaylandCompositorExtension>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickCompositorQuickExtensionContainer.atFunction' has no "
        "cute function yet. Qt's 'QWaylandCompositorExtension "
        "*QWaylandQuickCompositorQuickExtensionContainer::atFunction(QQmlLis"
        "tProperty<QWaylandCompositorExtension> *list, qsizetype index)': "
        "names 'QQmlListProperty<QWaylandCompositorExtension>', which has "
        "no cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQuickCompositorQuickExtensionContainer::clearFunction(
    QQmlListProperty<QWaylandCompositorExtension> *list)': names
    'QQmlListProperty<QWaylandCompositorExtension>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickCompositorQuickExtensionContainer.clearFunction' has "
        "no cute function yet. Qt's 'void "
        "QWaylandQuickCompositorQuickExtensionContainer::clearFunction(QQmlL"
        "istProperty<QWaylandCompositorExtension> *list)': names "
        "'QQmlListProperty<QWaylandCompositorExtension>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandQuickCompositorQuickExtensionContainer::countFunction(
    QQmlListProperty<QWaylandCompositorExtension> *list)': names
    'QQmlListProperty<QWaylandCompositorExtension>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickCompositorQuickExtensionContainer.countFunction' has "
        "no cute function yet. Qt's 'qsizetype "
        "QWaylandQuickCompositorQuickExtensionContainer::countFunction(QQmlL"
        "istProperty<QWaylandCompositorExtension> *list)': names "
        "'QQmlListProperty<QWaylandCompositorExtension>', which has no cute "
        "class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    QWaylandQuickCompositorQuickExtensionContainer::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickCompositorQuickExtensionContainer.data' has no cute "
        "function yet. Qt's 'QQmlListProperty<QObject> "
        "QWaylandQuickCompositorQuickExtensionContainer::data()': gives a "
        "type Python has no way to take yet.")
