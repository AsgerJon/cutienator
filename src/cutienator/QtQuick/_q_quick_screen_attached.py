"""
QQuickScreenAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickscreen_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickScreenAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickScreenInfo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QScreen
  from . import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScreenAttached(QQuickScreenInfo):
  """
  The cute side of Qt's QQuickScreenAttached: a plain Python object standing
  in front of one C++ QQuickScreenAttached.

  It is built on the cute 'QQuickScreenInfo', as Qt's QQuickScreenAttached is
  built on Qt's QQuickScreenInfo, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScreenAttached that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'angleBetween',
  'windowChanged', 'screenChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScreenAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickScreenAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickScreenAttached::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickScreenAttached is created at the first use, not by
    'QQuickScreenAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScreenAttached.
  - Qt tells when it has removed the C++ QQuickScreenAttached. Every call on
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
    Calls Qt's 'QString QQuickScreenAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreenattached.html#tr

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
    #  QString QQuickScreenAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickScreenAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScreenAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScreenAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreenattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScreenAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickScreenAttached10metaObjectEv',
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, attachee: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickScreenAttached::QQuickScreenAttached(QObject *attachee)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreenattached.html#QQuickScreenAttached

    Parameters
    ----------

    attachee : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickScreenAttached::QQuickScreenAttached(QObject *attachee)
    self._noteCreation(QQuickScreenAttached, lambda: Rituals.call(
        'ritual_ZN20QQuickScreenAttachedC1EP7QObject',
        self._addressOf(attachee, 'QObject'),
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

  @overload(int, int)
  def angleBetween(self, a: int, b: int) -> int:
    """
    Calls Qt's 'int QQuickScreenAttached::angleBetween(int a, int b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreenattached.html#angleBetween

    Parameters
    ----------

    a : int
      Passed on as it is.

    b : int
      Passed on as it is.
    """
    #  int QQuickScreenAttached::angleBetween(int a, int b)
    return self.uglySide.call(
        'ritual_ZN20QQuickScreenAttached12angleBetweenEii', a, b,
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowChanged(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickScreenAttached::windowChanged(QQuickWindow *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreenattached.html#windowChanged

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScreenAttached::windowChanged(QQuickWindow *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickScreenAttached13windowChangedEP12QQuickWindow',
        self._addressOf(a0),
    )

  @overload(QScreen)
  @overload(NoneType)
  def screenChanged(self, a0: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QQuickScreenAttached::screenChanged(QScreen *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreenattached.html#screenChanged

    Parameters
    ----------

    a0 : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScreenAttached::screenChanged(QScreen *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickScreenAttached13screenChangedEP7QScreen',
        self._addressOf(a0),
    )
