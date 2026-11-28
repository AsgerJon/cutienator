"""
QWaylandQtTextInputMethodManagerQuickExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorquickextensions_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandQtTextInputMethodManagerQuickExtension to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QWaylandQtTextInputMethodManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQtTextInputMethodManagerQuickExtension(QWaylandQtTextInputMethodManager):
  """
  The cute side of Qt's QWaylandQtTextInputMethodManagerQuickExtension: a
  plain Python object standing in front of one C++
  QWaylandQtTextInputMethodManagerQuickExtension.

  It is built on the cute 'QWaylandQtTextInputMethodManager', as Qt's
  QWaylandQtTextInputMethodManagerQuickExtension is built on Qt's
  QWaylandQtTextInputMethodManager, and has everything that class has. Qt's
  QWaylandQtTextInputMethodManagerQuickExtension is built on Qt's
  QQmlParserStatus as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QWaylandQtTextInputMethodManagerQuickExtension that
  has a ritual and that Python can call so far, 4 names in all: 'metaObject',
  'tr', 'classBegin', 'componentComplete'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QWaylandQtTextInputMethodManagerQuickExtension::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QWaylandQtTextInputMethodManagerQuickExtension::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QQmlListProperty<QObject>
    QWaylandQtTextInputMethodManagerQuickExtension::data()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQtTextInputMethodManagerQuickExtension is created at the
    first use, not by 'QWaylandQtTextInputMethodManagerQuickExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QWaylandQtTextInputMethodManagerQuickExtension.
  - Each name of Qt's QWaylandQtTextInputMethodManagerQuickExtension that has
    no cute function yet, 'data', holds a function that raises
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
    QWaylandQtTextInputMethodManagerQuickExtension::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandqttextinputmethodmanagerquickextension.html

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
    #  QString QWaylandQtTextInputMethodManagerQuickExtension::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension2trEPKcS1'
        '_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQtTextInputMethodManagerQuickExtension'

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
    *QWaylandQtTextInputMethodManagerQuickExtension::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandqttextinputmethodmanagerquickextension.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QWaylandQtTextInputMethodManagerQuickExtension::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK46QWaylandQtTextInputMethodManagerQuickExtension10metaOb'
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void
    QWaylandQtTextInputMethodManagerQuickExtension::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandqttextinputmethodmanagerquickextension.html
    """
    #  void QWaylandQtTextInputMethodManagerQuickExtension::classBegin()
    ritual = (
        'ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension10classBe'
        'ginEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN46QWaylandQtTextInputMethodManagerQuickExtension10c'
          'lassBeginEv')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void
    QWaylandQtTextInputMethodManagerQuickExtension::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandqttextinputmethodmanagerquickextension.html
    """
    #  void
    #      QWaylandQtTextInputMethodManagerQuickExtension::componentComplete(
    #      )
    ritual = (
        'ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension17compone'
        'ntCompleteEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN46QWaylandQtTextInputMethodManagerQuickExtension17c'
          'omponentCompleteEv')
    self.uglySide.call(ritual)

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    QWaylandQtTextInputMethodManagerQuickExtension::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethodManagerQuickExtension.data' has no cute "
        "function yet. Qt's 'QQmlListProperty<QObject> "
        "QWaylandQtTextInputMethodManagerQuickExtension::data()': gives a "
        "type Python has no way to take yet.")
