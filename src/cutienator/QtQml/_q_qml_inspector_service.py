"""
QQmlInspectorService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlInspectorService to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQmlDebugService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QWindow
  from ..QtQuick import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlInspectorService(QQmlDebugService):
  """
  The cute side of Qt's QQmlInspectorService: a plain Python object standing
  in front of one C++ QQmlInspectorService.

  It is built on the cute 'QQmlDebugService', as Qt's QQmlInspectorService is
  built on Qt's QQmlDebugService, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlInspectorService that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'addWindow',
  'setParentWindow', 'removeWindow'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlInspectorService::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlInspectorService::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlInspectorService::~QQmlInspectorService()': the destructor:
    Python never removes a C++ QQmlInspectorService.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlInspectorService is created at the first use, not by
    'QQmlInspectorService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlInspectorService.
  - Qt tells when it has removed the C++ QQmlInspectorService. Every call on
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
    Calls Qt's 'QString QQmlInspectorService::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinspectorservice.html#tr

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
    #  QString QQmlInspectorService::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQmlInspectorService2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInspectorService'

  #  A C++ QQmlInspectorService Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlInspectorService'

  #  The functions Qt calls itself that QQmlInspectorService is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'addWindow': (
          ('_ZN20QQmlInspectorService9addWindowEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'setParentWindow': (
          ('_ZN20QQmlInspectorService15setParentWindowEP12QQuickWindowP7QWi'
           'ndow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'removeWindow': (
          ('_ZN20QQmlInspectorService12removeWindowEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
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
    Calls Qt's 'const QMetaObject *QQmlInspectorService::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinspectorservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlInspectorService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQmlInspectorService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickWindow, QWindow)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def setParentWindow(
      self,
      a0: Optional[QQuickWindow],
      a1: Optional[QWindow],
  ) -> None:
    """
    Calls Qt's 'void QQmlInspectorService::setParentWindow(QQuickWindow *a0,
    QWindow *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinspectorservice.html#setParentWindow

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInspectorService::setParentWindow(QQuickWindow *a0, QWindow
    #      *a1)
    self.uglySide.call(
        'ritual_ZN20QQmlInspectorService15setParentWindowEP12QQuickWindowP7'
        'QWindow',
        self._addressOf(a0), self._addressOf(a1),
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

  @overload(float)
  @overload(float, QObject)
  @overload(float, NoneType)
  def __init__(
      self,
      version: float,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlInspectorService::QQmlInspectorService(float version, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinspectorservice.html#QQmlInspectorService

    Parameters
    ----------

    version : float
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlInspectorService::QQmlInspectorService(float version, QObject
    #      *parent)
    self._noteCreation(QQmlInspectorService, lambda: Rituals.call(
        'ritual_ZN20QQmlInspectorServiceC1EfP7QObject',
        version, self._addressOf(parent, 'QObject'),
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

  @overload(QQuickWindow)
  @overload(NoneType)
  def addWindow(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQmlInspectorService::addWindow(QQuickWindow *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinspectorservice.html#addWindow

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInspectorService::addWindow(QQuickWindow *a0)
    self.uglySide.call(
        'ritual_ZN20QQmlInspectorService9addWindowEP12QQuickWindow',
        self._addressOf(a0),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def removeWindow(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQmlInspectorService::removeWindow(QQuickWindow *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinspectorservice.html#removeWindow

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInspectorService::removeWindow(QQuickWindow *a0)
    self.uglySide.call(
        'ritual_ZN20QQmlInspectorService12removeWindowEP12QQuickWindow',
        self._addressOf(a0),
    )
