"""
QQuickPathPolyline binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathPolyline to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickCurve

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathPolyline(QQuickCurve):
  """
  The cute side of Qt's QQuickPathPolyline: a plain Python object standing in
  front of one C++ QQuickPathPolyline.

  It is built on the cute 'QQuickCurve', as Qt's QQuickPathPolyline is built
  on Qt's QQuickCurve, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathPolyline that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'path', 'setPath',
  'start', 'pathChanged', 'startChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathPolyline::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPathPolyline::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathPolyline::addToPath(QPainterPath &path, const
    QQuickPathData &data)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathPolyline is created at the first use, not by
    'QQuickPathPolyline(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathPolyline.
  - Qt tells when it has removed the C++ QQuickPathPolyline. Every call on
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
    Calls Qt's 'QString QQuickPathPolyline::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathpolyline.html#tr

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
    #  QString QQuickPathPolyline::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickPathPolyline2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathPolyline'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathPolyline::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathpolyline.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathPolyline::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickPathPolyline10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def path(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPathPolyline::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathpolyline.html#path

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPathPolyline::path() const
    address = self.uglySide.call('ritual_ZNK18QQuickPathPolyline4pathEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def start(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickPathPolyline::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathpolyline.html#start

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickPathPolyline::start() const
    address = self.uglySide.call('ritual_ZNK18QQuickPathPolyline5startEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setPath(self, path: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPathPolyline::setPath(const QVariant &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathpolyline.html#setPath

    Parameters
    ----------

    path : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPathPolyline::setPath(const QVariant &path)
    self.uglySide.call(
        'ritual_ZN18QQuickPathPolyline7setPathERK8QVariant',
        self._valueOf(path),
    )

  @overload(QList[QPointF])
  def setPath(self, path: QList[QPointF]) -> None:
    """
    Calls Qt's 'void QQuickPathPolyline::setPath(const QList<QPointF>
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathpolyline.html#setPath

    Parameters
    ----------

    path : QList[QPointF]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickPathPolyline::setPath(const QList<QPointF> &path)
    self.uglySide.call(
        'ritual_ZN18QQuickPathPolyline7setPathERK5QListI7QPointFE',
        self._valueOf(path),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPathPolyline::QQuickPathPolyline(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathpolyline.html#QQuickPathPolyline

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathPolyline::QQuickPathPolyline(QObject *parent)
    self._noteCreation(QQuickPathPolyline, lambda: Rituals.call(
        'ritual_ZN18QQuickPathPolylineC1EP7QObject',
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

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathPolyline::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathpolyline.html#pathChanged
    """
    #  void QQuickPathPolyline::pathChanged()
    self.uglySide.call('ritual_ZN18QQuickPathPolyline11pathChangedEv')

  def startChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathPolyline::startChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathpolyline.html#startChanged
    """
    #  void QQuickPathPolyline::startChanged()
    self.uglySide.call('ritual_ZN18QQuickPathPolyline12startChangedEv')
