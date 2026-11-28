"""
QQuickTextAreaAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTextAreaAttached to be private: it declares the class in a
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
  from . import QQuickTextArea
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTextArea = WAIT['QQuickTextArea']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextAreaAttached(QObject):
  """
  The cute side of Qt's QQuickTextAreaAttached: a plain Python object
  standing in front of one C++ QQuickTextAreaAttached.

  It is built on the cute 'QObject', as Qt's QQuickTextAreaAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextAreaAttached that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'flickable',
  'setFlickable', 'flickableChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextAreaAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTextAreaAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTextAreaAttachedPrivate *QQuickTextAreaAttached::d_func()':
    gives 'QQuickTextAreaAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickTextAreaAttachedPrivate
    *QQuickTextAreaAttached::d_func() const': gives
    'QQuickTextAreaAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTextAreaAttached is created at the first use, not by
    'QQuickTextAreaAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextAreaAttached.
  - Qt tells when it has removed the C++ QQuickTextAreaAttached. Every call
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
    Calls Qt's 'QString QQuickTextAreaAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextareaattached.html#tr

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
    #  QString QQuickTextAreaAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickTextAreaAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextAreaAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextAreaAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextAreaAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTextAreaAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def flickable(self) -> Optional[QQuickTextArea]:
    """
    Calls Qt's 'QQuickTextArea *QQuickTextAreaAttached::flickable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaattached.html#flickable

    Returns
    -------

    Optional[QQuickTextArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextArea *QQuickTextAreaAttached::flickable() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTextAreaAttached9flickableEv',
    )
    from . import QQuickTextArea
    return QQuickTextArea._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTextArea)
  @overload(NoneType)
  def setFlickable(self, control: Optional[QQuickTextArea]) -> None:
    """
    Calls Qt's 'void QQuickTextAreaAttached::setFlickable(QQuickTextArea
    *control)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaattached.html#setFlickable

    Parameters
    ----------

    control : Optional[QQuickTextArea]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextAreaAttached::setFlickable(QQuickTextArea *control)
    self.uglySide.call(
        'ritual_ZN22QQuickTextAreaAttached12setFlickableEP14QQuickTextArea',
        self._addressOf(control),
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
    'QQuickTextAreaAttached::QQuickTextAreaAttached(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaattached.html#QQuickTextAreaAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickTextAreaAttached::QQuickTextAreaAttached(QObject *parent)
    self._noteCreation(QQuickTextAreaAttached, lambda: Rituals.call(
        'ritual_ZN22QQuickTextAreaAttachedC1EP7QObject',
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

  def flickableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextAreaAttached::flickableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextareaattached.html#flickableChanged
    """
    #  void QQuickTextAreaAttached::flickableChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickTextAreaAttached16flickableChangedEv',
    )
